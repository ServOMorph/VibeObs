[CmdletBinding(DefaultParameterSetName = 'Run')]
param(
    [Parameter(Mandatory = $true, ParameterSetName = 'Run')][string]$Brief,
    [Parameter(Mandatory = $true, ParameterSetName = 'Run')][ValidatePattern('^[A-Za-z0-9][A-Za-z0-9_-]*$')][string]$Name,
    [Parameter(ParameterSetName = 'Run')][string]$Root,
    [Parameter(ParameterSetName = 'Run')][ValidateSet('read-only', 'workspace-write')][string]$Sandbox = 'workspace-write',
    [Parameter(ParameterSetName = 'Run')][switch]$DryRun,
    [Parameter(Mandatory = $true, ParameterSetName = 'Statut')][switch]$Statut,
    [Parameter(Mandatory = $true, ParameterSetName = 'Passe')][switch]$Passe,
    [Parameter(ParameterSetName = 'Passe')][string]$ArgsB64 = ''
)

$ErrorActionPreference = 'Stop'
$codexHome = Join-Path $env:USERPROFILE '.codex'
$blocage = Join-Path $codexHome 'delegation_bloquee.flag'
$politiqueFile = Join-Path $codexHome 'politique_delegation.json'
$verrouFile = Join-Path $codexHome 'delegation.lock'

$politique = [ordered]@{
    modele = 'gpt-6.2-sol'
    binaire = ''
    seuil_5h = 50
    seuil_7j = 60
    attente_verrou_s = 300
    quota_inconnu = 'bloquer'
}
if (Test-Path -LiteralPath $politiqueFile) {
    $lue = Get-Content -LiteralPath $politiqueFile -Raw -Encoding UTF8 | ConvertFrom-Json
    foreach ($cle in @($politique.Keys)) {
        if ($null -ne $lue.$cle -and "$($lue.$cle)" -ne '') { $politique[$cle] = $lue.$cle }
    }
}

function Get-QuotaCodex {
    $sessions = Join-Path $codexHome 'sessions'
    if (-not (Test-Path -LiteralPath $sessions)) { return $null }
    $fichiers = Get-ChildItem -LiteralPath $sessions -Recurse -Filter 'rollout-*.jsonl' -File -ErrorAction SilentlyContinue |
        Sort-Object LastWriteTime -Descending | Select-Object -First 8
    foreach ($fichier in $fichiers) {
        $flux = $null
        $texte = $null
        try {
            $flux = New-Object IO.FileStream($fichier.FullName, [IO.FileMode]::Open, [IO.FileAccess]::Read, [IO.FileShare]::ReadWrite)
            $taille = [Math]::Min([long]$flux.Length, 2097152L)
            [void]$flux.Seek(-$taille, [IO.SeekOrigin]::End)
            $octets = New-Object byte[] $taille
            $lu = 0
            while ($lu -lt $taille) {
                $n = $flux.Read($octets, $lu, $taille - $lu)
                if ($n -le 0) { break }
                $lu += $n
            }
            $texte = [Text.Encoding]::UTF8.GetString($octets, 0, $lu)
        } catch { continue } finally { if ($flux) { $flux.Dispose() } }
        $lignes = $texte -split "`n"
        for ($i = $lignes.Count - 1; $i -ge 0; $i--) {
            if ($lignes[$i] -notmatch '"rate_limits":\{[^}]*"primary":\{') { continue }
            try { $evenement = $lignes[$i] | ConvertFrom-Json } catch { continue }
            $limites = $evenement.payload.rate_limits
            if (-not $limites -or -not $limites.primary) { continue }
            return [pscustomobject]@{
                releve = [string]$evenement.timestamp
                primaire = $limites.primary
                secondaire = $limites.secondary
            }
        }
    }
    return $null
}

function Get-BinaireCodex {
    $cx = $null
    if ($politique.binaire -and (Test-Path -LiteralPath $politique.binaire -PathType Leaf)) { $cx = [string]$politique.binaire }
    if (-not $cx -and $env:LOCALAPPDATA) {
        $cx = Get-ChildItem -Path "$env:LOCALAPPDATA\OpenAI\Codex\bin\*\codex.exe" -File -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending | Select-Object -First 1 -ExpandProperty FullName
    }
    if (-not $cx) {
        $command = Get-Command codex -CommandType Application, ExternalScript -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($command) { $cx = $command.Source }
    }
    return $cx
}

function Get-PourcentageEffectif($fenetre) {
    if (-not $fenetre) { return $null }
    $maintenant = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
    if ($fenetre.resets_at -and $maintenant -ge [long]$fenetre.resets_at) { return 0.0 }
    return [double]$fenetre.used_percent
}

function Test-QuotaCodex {
    $quota = Get-QuotaCodex
    if (-not $quota) {
        return [pscustomobject]@{ ok = ($politique.quota_inconnu -eq 'laisser'); message = 'quota Codex illisible (aucun releve dans les sessions)'; p5 = $null; p7 = $null; releve = $null }
    }
    $p5 = Get-PourcentageEffectif $quota.primaire
    $p7 = Get-PourcentageEffectif $quota.secondaire
    $ok = $true
    $motifs = @()
    if ($null -ne $p5 -and $p5 -ge [double]$politique.seuil_5h) { $ok = $false; $motifs += "fenetre 5 h a $p5 % (seuil $($politique.seuil_5h) %)" }
    if ($null -ne $p7 -and $p7 -ge [double]$politique.seuil_7j) { $ok = $false; $motifs += "fenetre 7 jours a $p7 % (seuil $($politique.seuil_7j) %)" }
    $message = if ($ok) { 'sous les seuils' } else { $motifs -join ' ; ' }
    return [pscustomobject]@{ ok = $ok; message = $message; p5 = $p5; p7 = $p7; releve = $quota.releve }
}

if ($Statut) {
    $etat = Test-QuotaCodex
    Write-Output ("modele={0} seuil_5h={1} seuil_7j={2} attente_verrou_s={3}" -f $politique.modele, $politique.seuil_5h, $politique.seuil_7j, $politique.attente_verrou_s)
    $bloque = Test-Path -LiteralPath $blocage
    Write-Output ("flag_blocage={0}" -f $bloque)
    Write-Output ("releve={0} p5h={1} p7j={2} verdict_quota={3}" -f $etat.releve, $etat.p5, $etat.p7, $etat.message)
    if ($bloque) { Write-Output "DELEGATION BLOQUEE par l'utilisateur ($blocage) : ne pas lancer Codex, le flag prime sur le quota." }
    elseif ($etat.ok) { Write-Output 'DELEGATION AUTORISEE : flag absent, quota sous les seuils.' }
    else { Write-Output 'DELEGATION REFUSEE : seuil de quota atteint.' }
    exit 0
}

if ((Test-Path -LiteralPath $blocage) -and -not $DryRun) {
    [Console]::Error.WriteLine("Delegation a Codex bloquee par l'utilisateur ($blocage). Ne pas contourner : router vers Ollama, OpenCode ou un sous-agent Claude.")
    exit 3
}

$verrou = $null
$code = 0
try {
    if (-not $DryRun) {
        $limite = (Get-Date).AddSeconds([int]$politique.attente_verrou_s)
        while (-not $verrou) {
            try {
                $verrou = New-Object IO.FileStream($verrouFile, [IO.FileMode]::OpenOrCreate, [IO.FileAccess]::ReadWrite, [IO.FileShare]::None)
            } catch [IO.IOException] {
                if ((Get-Date) -ge $limite) {
                    [Console]::Error.WriteLine("Un autre appel a Codex est en cours ($verrouFile) : delai de $($politique.attente_verrou_s) s depasse. Reessayer plus tard.")
                    $code = 4
                    break
                }
                Start-Sleep -Seconds 2
            }
        }
        if ($code -eq 0) {
            $etat = Test-QuotaCodex
            if (-not $etat.ok) {
                [Console]::Error.WriteLine("Delegation a Codex bloquee par la politique ($politiqueFile) : $($etat.message). Releve du $($etat.releve). Ne pas contourner : router vers Ollama, OpenCode ou un sous-agent Claude.")
                $code = 5
            }
        }
    }
    if ($code -eq 0 -and $Passe) {
        $cx = Get-BinaireCodex
        if (-not $cx) { throw 'Codex introuvable : installer l''application Codex ou ajouter Codex CLI au PATH.' }
        $restants = New-Object System.Collections.Generic.List[string]
        $i = 0
        $args2 = @()
        if ($ArgsB64) {
            $decoded = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($ArgsB64))
            $args2 = @($decoded.Split([char]0) | Where-Object { $_ -ne $null })
            if ($args2.Count -gt 0 -and $args2[$args2.Count - 1] -eq '') { $args2 = @($args2[0..($args2.Count - 2)]) }
        }
        while ($i -lt $args2.Count) {
            if ($args2[$i] -eq '-m' -or $args2[$i] -eq '--model') { $i += 2; continue }
            $restants.Add([string]$args2[$i])
            $i++
        }
        $position = $restants.IndexOf('exec')
        if ($position -ge 0) { $restants.InsertRange($position + 1, [string[]]@('-m', [string]$politique.modele)) }
        else { $restants.InsertRange(0, [string[]]@('-m', [string]$politique.modele)) }
        $transmis = @($restants.ToArray() | ForEach-Object { $_ -replace '(\\*)"', '$1$1\"' })
        & $cx @transmis
        $code = $LASTEXITCODE
    } elseif ($code -eq 0) {
        if (-not $Root) { $Root = Split-Path -Parent $MyInvocation.MyCommand.Path | Split-Path -Parent }
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
        $cx = Get-BinaireCodex
        if (-not $cx) {
            if ($DryRun) { $cx = 'codex' }
            else { throw 'Codex introuvable : installer l''application Codex ou ajouter Codex CLI au PATH.' }
        }
        $arguments = @('exec', '-m', [string]$politique.modele, '--sandbox', $Sandbox, '-C', $Root, '-o', $report, $message)
        if ($DryRun) {
            $quoted = @($cx) + $arguments | ForEach-Object { "'" + $_.Replace("'", "''") + "'" }
            Write-Output ('& ' + ($quoted -join ' ') + " 2>&1 | ForEach-Object { `$_.ToString() } | Out-File -LiteralPath '$($log.Replace("'", "''"))' -Encoding utf8")
            exit 0
        }
        $previousPreference = $ErrorActionPreference
        try {
            $ErrorActionPreference = 'Continue'
            & $cx @arguments 2>&1 | ForEach-Object { $_.ToString() } | Out-File -LiteralPath $log -Encoding utf8
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
    }
} finally {
    if ($verrou) { $verrou.Dispose() }
}
exit $code
