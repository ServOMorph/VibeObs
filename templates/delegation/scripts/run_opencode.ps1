param(
    [Parameter(Mandatory = $true)][string]$Brief,
    [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9][A-Za-z0-9_-]*$')][string]$Name,
    [string]$Root = (Split-Path -Parent $PSScriptRoot),
    [string]$Model = 'opencode/deepseek-v4.1-flash-free',
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
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
$arguments = @('run', $message, '-m', $Model, '--dir', $Root, '-f', $briefFile)
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
$cleanText = $logText -replace '\x1B\[[0-?]*[ -/]*[@-~]', ''
$lines = @($cleanText -split '\r?\n')
$matches = @($lines | Select-String -Pattern '^\s*STATUT\s*:')
$reportLines = @()
if ($matches.Count -gt 0) {
    $start = $matches[-1].LineNumber - 1
    for ($i = $start; $i -lt $lines.Count -and $reportLines.Count -lt 15; $i++) {
        $reportLines += $lines[$i]
        if ($lines[$i] -match '^\s*OUVERT\s*:') { break }
    }
}
if (-not ($reportLines -match '^\s*OUVERT\s*:')) {
    $reportLines = @('STATUT: ECHEC', 'FICHIERS: inconnus', "VERIFS: executant -> code $code", "OUVERT: rapport absent ou incomplet ; consulter $log")
    if ($code -eq 0) { $code = 1 }
}
[IO.File]::WriteAllLines($report, [string[]]$reportLines, $utf8)
Get-Content -LiteralPath $report -Encoding UTF8
exit $code
