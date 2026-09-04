[CmdletBinding()]
param(
    [switch]$Production,
    [string]$SiteId
)

$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$envFile = Join-Path $projectRoot '.env.netlify'

if (Test-Path -LiteralPath $envFile) {
    Get-Content -LiteralPath $envFile | ForEach-Object {
        if ($_ -match '^\s*(NETLIFY_AUTH_TOKEN|NETLIFY_SITE_ID)\s*=\s*(.+?)\s*$') {
            Set-Item -Path "Env:$($matches[1])" -Value $matches[2]
        }
    }
}

if (-not $env:NETLIFY_AUTH_TOKEN) {
    throw 'NETLIFY_AUTH_TOKEN est absent. Créez .env.netlify depuis .env.netlify.example.'
}

if ($SiteId) {
    $env:NETLIFY_SITE_ID = $SiteId
}

$arguments = @('netlify', 'deploy', '--build')
if ($Production) {
    $arguments += '--prod'
}
if ($env:NETLIFY_SITE_ID) {
    $arguments += "--site=$($env:NETLIFY_SITE_ID)"
}

Push-Location $projectRoot
try {
    & npx @arguments
    if ($LASTEXITCODE -ne 0) {
        throw "Le déploiement Netlify a échoué (code $LASTEXITCODE)."
    }
}
finally {
    Pop-Location
}
