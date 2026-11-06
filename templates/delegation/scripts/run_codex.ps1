param(
    [Parameter(Mandatory = $true)][string]$Brief,
    [Parameter(Mandatory = $true)][ValidatePattern('^[A-Za-z0-9][A-Za-z0-9_-]*$')][string]$Name,
    [string]$Root = (Split-Path -Parent $PSScriptRoot),
    [ValidateSet('read-only', 'workspace-write')][string]$Sandbox = 'workspace-write',
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path -LiteralPath $Root).ProviderPath
$utf8 = New-Object Text.UTF8Encoding $false
$briefText = if (Test-Path -LiteralPath $Brief -PathType Leaf) {
    [IO.File]::ReadAllText((Resolve-Path -LiteralPath $Brief).ProviderPath)
} else { $Brief }
$preamble = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'PREAMBULE.md'))
$dir = Join-Path $Root ("_codex\runs\{0}_{1}_{2}" -f (Get-Date -Format 'yyyyMMdd_HHmmss_fff'), $Name, ([guid]::NewGuid().ToString('N').Substring(0, 8)))
New-Item -ItemType Directory -Path $dir | Out-Null
$briefFile = Join-Path $dir 'brief.md'
[IO.File]::WriteAllText($briefFile, "$preamble`n`n# Brief`n$briefText", $utf8)
$report = Join-Path $dir 'rapport.md'
$log = Join-Path $dir 'log.txt'
$relative = $briefFile.Substring($Root.TrimEnd('\', '/').Length + 1).Replace('\', '/')
$message = "Lis le fichier $relative, execute-le et termine par le rapport final au format demande."
$cx = $null
if ($env:LOCALAPPDATA) {
    $cx = Get-ChildItem -Path "$env:LOCALAPPDATA\OpenAI\Codex\bin\*\codex.exe" -File -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 1 -ExpandProperty FullName
}
if (-not $cx) {
    $command = Get-Command codex -CommandType Application, ExternalScript -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($command) { $cx = $command.Source }
}
if (-not $cx) {
    if ($DryRun) { $cx = 'codex' }
    else { throw 'Codex introuvable : installer l''application Codex ou ajouter Codex CLI au PATH.' }
}
$arguments = @('exec', '--sandbox', $Sandbox, '-C', $Root, '-o', $report, $message)
if ($DryRun) {
    $quoted = @($cx) + $arguments | ForEach-Object { "'" + $_.Replace("'", "''") + "'" }
    Write-Output ('& ' + ($quoted -join ' ') + " *> '$($log.Replace("'", "''"))'")
    return
}
$previousPreference = $ErrorActionPreference
try {
    $ErrorActionPreference = 'Continue'
    & $cx @arguments *> $log
    $code = $LASTEXITCODE
} finally { $ErrorActionPreference = $previousPreference }
if (Test-Path -LiteralPath $log) {
    $logText = Get-Content -LiteralPath $log -Raw
    [IO.File]::WriteAllText($log, [string]$logText, $utf8)
}
if (-not (Test-Path -LiteralPath $report)) {
    [IO.File]::WriteAllText($report, "STATUT: ECHEC`nFICHIERS: inconnus`nVERIFS: executant -> code $code`nOUVERT: rapport absent ; consulter $log`n", $utf8)
    if ($code -eq 0) { $code = 1 }
} else {
    $reportText = [IO.File]::ReadAllText($report)
    [IO.File]::WriteAllText($report, $reportText, $utf8)
}
Get-Content -LiteralPath $report -Encoding UTF8
exit $code
