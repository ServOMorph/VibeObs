param(
    [Parameter(Mandatory = $true)][string]$Projet,
    [string]$NomProjet,
    [string]$FichiersRegles = 'Lire les consignes du projet applicables au perimetre du brief.',
    [string]$Interdits = 'Aucune generation de contenu, aucun deploiement ni redemarrage de service sans demande explicite.',
    [string]$Verifications = 'Executer uniquement les controles pertinents autorises par le brief ; signaler ceux impossibles a lancer.'
)

$ErrorActionPreference = 'Stop'
$utf8 = New-Object Text.UTF8Encoding $false
New-Item -ItemType Directory -Path $Projet -Force | Out-Null
$Projet = (Resolve-Path -LiteralPath $Projet).ProviderPath
if (-not $NomProjet) { $NomProjet = Split-Path -Leaf $Projet }
$destination = Join-Path $Projet '_codex'
New-Item -ItemType Directory -Path $destination -Force | Out-Null
foreach ($name in @('run_codex.ps1', 'run_opencode.ps1')) {
    $target = Join-Path $destination $name
    if (-not (Test-Path -LiteralPath $target)) {
        $sourceText = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "scripts\$name"))
        [IO.File]::WriteAllText($target, $sourceText, $utf8)
    }
}
$preamblePath = Join-Path $destination 'PREAMBULE.md'
if (-not (Test-Path -LiteralPath $preamblePath)) {
    $text = [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'PREAMBULE.md.template'))
    $text = $text.Replace('[[PROJET]]', $NomProjet).Replace('[[FICHIERS_REGLES]]', $FichiersRegles).Replace('[[INTERDITS]]', $Interdits).Replace('[[VERIFICATIONS]]', $Verifications)
    [IO.File]::WriteAllText($preamblePath, $text, $utf8)
}
$config = Join-Path $Projet 'opencode.json'
if (-not (Test-Path -LiteralPath $config)) {
    [IO.File]::WriteAllText($config, [IO.File]::ReadAllText((Join-Path $PSScriptRoot 'opencode.json.template')), $utf8)
}
$ignorePath = Join-Path $Projet '.gitignore'
$ignore = if (Test-Path -LiteralPath $ignorePath) { [IO.File]::ReadAllText($ignorePath) } else { '' }
if (-not (@($ignore -split '\r?\n') | Where-Object { $_.Trim() -in @('_codex/runs/', '/_codex/runs/', '_codex/runs', '/_codex/runs') })) {
    $separator = if ($ignore.Length -gt 0 -and -not $ignore.EndsWith("`n")) { "`n" } else { '' }
    [IO.File]::AppendAllText($ignorePath, "$separator`_codex/runs/`n", $utf8)
}
Write-Output "Installation prete : $destination"
Write-Output 'Suite : relire le preambule et les permissions OpenCode existantes ; rediger un brief autonome avec perimetre explicite.'
Write-Output 'Tester avec -DryRun, puis lancer un seul executant par perimetre. Relire uniquement le rapport, le journal en cas de probleme.'
Write-Output 'Les fichiers existants sont conserves ; les nouveaux parametres ne les remplacent pas.'
