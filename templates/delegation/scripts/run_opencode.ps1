param(
    [Parameter(Mandatory = $true)][string]$Brief,
    [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9][A-Za-z0-9_-]*$')][string]$Name,
    [string]$Root,
    [string]$Model = 'opencode/deepseek-v4.1-flash-free',
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
function Get-OpenCodeFinalMessage {
    param([string]$LogText)

    $cleanText = $LogText -replace '\x1B\][^\x07\x1B]*(?:\x07|\x1B\\)', ''
    $cleanText = $cleanText -replace '\x1B\[[0-?]*[ -/]*[@-~]', ''
    $lines = @($cleanText -split '\r?\n')
    $parts = @()
    $messageId = $null
    $hasEvents = $false
    foreach ($line in $lines) {
        try { $event = $line | ConvertFrom-Json -ErrorAction Stop } catch { continue }
        if ($event.type -in @('step_start', 'step_finish', 'tool_use', 'text', 'error')) {
            $hasEvents = $true
        }
        if ($event.type -eq 'text' -and $null -ne $event.part.text) {
            if ($event.part.messageID -ne $messageId) {
                $parts = @()
                $messageId = $event.part.messageID
            }
            $parts += [string]$event.part.text
        }
    }
    if ($hasEvents) {
        $text = ($parts -join "`n") -replace '\x1B\][^\x07\x1B]*(?:\x07|\x1B\\)', ''
        return ($text -replace '\x1B\[[0-?]*[ -/]*[@-~]', '').Trim()
    }

    $statusLines = @($lines | Select-String -Pattern '^\s*STATUT\s*:')
    if ($statusLines.Count -eq 0) { return '' }
    $statusIndex = $statusLines[-1].LineNumber - 1
    $start = 0
    for ($i = 0; $i -lt $statusIndex; $i++) {
        if ($lines[$i] -match '^(?:[^\p{L}\p{N}\s]+|\u00D4\S+)\s+(?:Read|Grep|Glob|Bash|Write|Edit|Task)\b|^\$\s|^>\s+(?:build|plan)\b') {
            $start = $i + 1
        }
    }
    return ($lines[$start..($lines.Count - 1)] -join "`n").Trim()
}

if (-not $Root) { $Root = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent }
$Root = (Resolve-Path -LiteralPath $Root).ProviderPath
$utf8 = New-Object Text.UTF8Encoding $false
$briefText = if (Test-Path -LiteralPath $Brief -PathType Leaf) {
    [IO.File]::ReadAllText((Resolve-Path -LiteralPath $Brief).ProviderPath)
} else { $Brief }
$preamble = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'PREAMBULE.md'))
$dir = Join-Path $Root ("_codex\runs\{0}_oc_{1}_{2}" -f (Get-Date -Format 'yyyyMMdd_HHmmss_fff'), $Name, ([guid]::NewGuid().ToString('N').Substring(0, 8)))
New-Item -ItemType Directory -Path $dir | Out-Null
$briefFile = Join-Path $dir 'brief.md'
[IO.File]::WriteAllText($briefFile, "$preamble`n`n# Brief`n$briefText", $utf8)
$log = Join-Path $dir 'log.txt'
$report = Join-Path $dir 'rapport.md'
$command = Get-Command opencode -CommandType Application, ExternalScript -ErrorAction SilentlyContinue | Select-Object -First 1
$executable = if ($command) { $command.Source } else { 'opencode' }
$message = 'Execute le brief joint (brief.md) et termine par le rapport final au format demande.'
$arguments = @('run', $message, '-m', $Model, '--dir', $Root, '-f', $briefFile, '--format', 'json')
if ($DryRun) {
    $quoted = @($executable) + $arguments | ForEach-Object { "'" + $_.Replace("'", "''") + "'" }
    Write-Output ('& ' + ($quoted -join ' ') + " *> '$($log.Replace("'", "''"))'")
    return
}
if (-not $command) { throw 'OpenCode introuvable : installer OpenCode et l''ajouter au PATH.' }
$previousPreference = $ErrorActionPreference
try {
    $ErrorActionPreference = 'Continue'
    & $executable @arguments *> $log
    $code = $LASTEXITCODE
} finally { $ErrorActionPreference = $previousPreference }
$logText = [string](Get-Content -LiteralPath $log -Raw)
[IO.File]::WriteAllText($log, $logText, $utf8)
$finalMessage = Get-OpenCodeFinalMessage -LogText $logText
$reportLines = @($finalMessage -split '\r?\n')
if (-not ($reportLines -match '^\s*STATUT\s*:')) {
    $reportLines = @('STATUT: ECHEC', 'FICHIERS: inconnus', "VERIFS: executant -> code $code", "OUVERT: rapport absent ou incomplet ; consulter $log")
    if ($code -eq 0) { $code = 1 }
}
[IO.File]::WriteAllLines($report, [string[]]$reportLines, $utf8)
Get-Content -LiteralPath $report -Encoding UTF8
exit $code
