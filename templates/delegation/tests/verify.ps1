$ErrorActionPreference = 'Stop'
$templateRoot = Split-Path -Parent $PSScriptRoot
$scripts = @(Get-ChildItem -LiteralPath $templateRoot -Filter '*.ps1' -Recurse)
foreach ($script in $scripts) {
    $tokens = $null
    $parseErrors = $null
    [void][System.Management.Automation.Language.Parser]::ParseFile($script.FullName, [ref]$tokens, [ref]$parseErrors)
    if ($parseErrors.Count) { throw ($parseErrors | Out-String) }
}
Write-Output "Syntaxe : $($scripts.Count) scripts OK"
$tempBase = [IO.Path]::GetFullPath($env:TEMP).TrimEnd('\')
$testRoot = Join-Path $tempBase ('test_delegation_install_' + [guid]::NewGuid().ToString('N'))
function Assert-True($condition, [string]$message) {
    if (-not $condition) { throw $message }
}
try {
    & (Join-Path $templateRoot 'install.ps1') -Projet $testRoot -NomProjet 'Projet test' | Out-Null
    $expected = @('_codex/run_codex.ps1', '_codex/run_opencode.ps1', '_codex/PREAMBULE.md', 'opencode.json', '.gitignore')
    foreach ($relative in $expected) {
        $path = Join-Path $testRoot $relative
        Assert-True (Test-Path -LiteralPath $path -PathType Leaf) "Fichier absent : $relative"
        $bytes = [IO.File]::ReadAllBytes($path)
        Assert-True (-not ($bytes.Length -ge 3 -and $bytes[0] -eq 239 -and $bytes[1] -eq 187 -and $bytes[2] -eq 191)) "BOM : $relative"
    }
    $preamble = [IO.File]::ReadAllText((Join-Path $testRoot '_codex/PREAMBULE.md'))
    Assert-True ($preamble.Contains('Projet test') -and -not $preamble.Contains('[[')) 'Substitution du preambule incorrecte'
    $config = [IO.File]::ReadAllText((Join-Path $testRoot 'opencode.json')) | ConvertFrom-Json
    Assert-True ($config.permission.bash.'*' -eq 'deny' -and $config.permission.webfetch -eq 'deny') 'Permissions incorrectes'
    [IO.File]::AppendAllText((Join-Path $testRoot '_codex/PREAMBULE.md'), "`nPersonnalisation conservee.")
    [IO.File]::WriteAllText((Join-Path $testRoot 'opencode.json'), '{"permission":{"edit":"deny"}}')
    $hashes = @{}
    foreach ($relative in $expected) { $hashes[$relative] = (Get-FileHash -LiteralPath (Join-Path $testRoot $relative)).Hash }
    & (Join-Path $templateRoot 'install.ps1') -Projet $testRoot -NomProjet 'Ne pas remplacer' | Out-Null
    foreach ($relative in $expected) {
        Assert-True ($hashes[$relative] -eq (Get-FileHash -LiteralPath (Join-Path $testRoot $relative)).Hash) "Fichier ecrase : $relative"
    }
    $ignore = [IO.File]::ReadAllLines((Join-Path $testRoot '.gitignore'))
    Assert-True (@($ignore | Where-Object { $_ -eq '_codex/runs/' }).Count -eq 1) 'Exclusion dupliquee'
    Write-Output 'Installation, UTF-8 sans BOM, permissions et idempotence : OK'
    $briefPath = Join-Path $testRoot 'brief avec espaces.md'
    [IO.File]::WriteAllText($briefPath, 'Brief depuis fichier : lecture seule.')
    $codexOutput = & (Join-Path $testRoot '_codex/run_codex.ps1') -Brief $briefPath -Name 'test-codex' -Sandbox read-only -DryRun
    $openOutput = & (Join-Path $testRoot '_codex/run_opencode.ps1') -Brief 'Brief autonome de test.' -Name 'test-open' -Root $testRoot -DryRun
    Assert-True ($codexOutput.Contains("'--sandbox' 'read-only'")) 'Commande Codex incorrecte'
    Assert-True ($openOutput.Contains("'run' 'Execute le brief joint")) 'Message OpenCode absent'
    Assert-True ($openOutput.IndexOf("'run'") -lt $openOutput.IndexOf("'-m'")) 'Ordre OpenCode incorrect'
    Assert-True ($openOutput.Contains("'opencode/deepseek-v4.1-flash-free'")) 'Modele incorrect'
    $runs = @(Get-ChildItem -LiteralPath (Join-Path $testRoot '_codex/runs') -Directory)
    Assert-True ($runs.Count -eq 2) 'Nombre de simulations incorrect'
    foreach ($run in $runs) {
        $brief = [IO.File]::ReadAllText((Join-Path $run.FullName 'brief.md'))
        Assert-True ($brief.Contains('Projet test') -and $brief.Contains('# Brief')) 'Brief incomplet'
        Assert-True (@(Get-ChildItem -LiteralPath $run.FullName -File).Count -eq 1) 'DryRun a produit autre chose que le brief'
    }
    Assert-True (([IO.File]::ReadAllText((Join-Path ($runs | Where-Object Name -Like '*test-codex*').FullName 'brief.md'))).Contains('Brief depuis fichier')) 'Brief fichier non charge'
    Write-Output 'Codex -DryRun et OpenCode -DryRun : OK, aucun executant lance'
} finally {
    $resolvedTest = [IO.Path]::GetFullPath($testRoot)
    Assert-True ($resolvedTest.StartsWith($tempBase + '\', [StringComparison]::OrdinalIgnoreCase) -and ([IO.Path]::GetFileName($resolvedTest) -like 'test_delegation_install_*')) 'Nettoyage hors perimetre refuse'
    if (Test-Path -LiteralPath $resolvedTest) {
        try {
            Remove-Item -LiteralPath $resolvedTest -Recurse -Force
            Write-Output 'Dossier temporaire nettoye'
        } catch { Write-Warning "Nettoyage impossible : $resolvedTest ; $($_.Exception.Message)" }
    }
}
