param(
    [ValidateSet('gauche', 'droite', 'aucune')][string]$Moitie = 'gauche',
    [Parameter(Mandatory=$true)][string]$TitreContient,
    [double]$PositionClicX = 0.5,
    [double]$PositionClicY = 0.93,
    [int]$DelaiApresClicMs = 300,
    [int]$DelaiApresCollerMs = 300,
    [switch]$SansEnvoi,
    [switch]$SeulementValider,
    [string]$DossierEtat = '',
    [string]$Agent = ''
)

if ($DossierEtat -and $Agent) {
    $cheminCalib = Join-Path (Join-Path $DossierEtat $Agent) 'calibration.json'
    if (Test-Path -LiteralPath $cheminCalib) {
        $calib = Get-Content -LiteralPath $cheminCalib -Raw -Encoding UTF8 | ConvertFrom-Json
        if (-not $PSBoundParameters.ContainsKey('PositionClicX')) { $PositionClicX = $calib.PositionClicX }
        if (-not $PSBoundParameters.ContainsKey('PositionClicY')) { $PositionClicY = $calib.PositionClicY }
    }
}

Add-Type -AssemblyName System.Windows.Forms

Add-Type @'
using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;

public struct RectFEnvoi {
    public int Left;
    public int Top;
    public int Right;
    public int Bottom;
}

public class FenetreFinderEnvoi {
    public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);

    [DllImport("user32.dll")]
    public static extern bool EnumWindows(EnumWindowsProc lpEnumFunc, IntPtr lParam);

    [DllImport("user32.dll")]
    public static extern int GetWindowText(IntPtr hWnd, StringBuilder text, int count);

    [DllImport("user32.dll")]
    public static extern int GetWindowTextLength(IntPtr hWnd);

    [DllImport("user32.dll")]
    public static extern bool IsWindowVisible(IntPtr hWnd);

    [DllImport("user32.dll")]
    public static extern bool GetWindowRect(IntPtr hWnd, out RectFEnvoi rect);

    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);

    [DllImport("user32.dll")]
    public static extern void SetCursorPos(int x, int y);

    [DllImport("user32.dll")]
    public static extern void mouse_event(uint dwFlags, uint dx, uint dy, uint dwData, int dwExtraInfo);

    public static List<KeyValuePair<IntPtr, string>> Lister(string titreContient) {
        List<KeyValuePair<IntPtr, string>> resultat = new List<KeyValuePair<IntPtr, string>>();
        EnumWindows((hWnd, lParam) => {
            if (!IsWindowVisible(hWnd)) return true;
            int len = GetWindowTextLength(hWnd);
            if (len > 0) {
                StringBuilder sb = new StringBuilder(len + 1);
                GetWindowText(hWnd, sb, sb.Capacity);
                string titre = sb.ToString();
                if (titre.IndexOf(titreContient, StringComparison.OrdinalIgnoreCase) >= 0) {
                    resultat.Add(new KeyValuePair<IntPtr, string>(hWnd, titre));
                }
            }
            return true;
        }, IntPtr.Zero);
        return resultat;
    }
}
'@

$MOUSEEVENTF_LEFTDOWN = 0x0002
$MOUSEEVENTF_LEFTUP = 0x0004

$candidats = [FenetreFinderEnvoi]::Lister($TitreContient)

if ($Moitie -ne 'aucune') {
    $ecran = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
    $milieuEcran = $ecran.Left + ($ecran.Width / 2)
    $candidats = $candidats | Where-Object {
        $rect = New-Object RectFEnvoi
        [FenetreFinderEnvoi]::GetWindowRect($_.Key, [ref]$rect) | Out-Null
        $centreX = ($rect.Left + $rect.Right) / 2
        if ($Moitie -eq 'gauche') { $centreX -lt $milieuEcran } else { $centreX -ge $milieuEcran }
    }
}

$nombre = @($candidats).Count
if ($nombre -eq 0) {
    Write-Error "Aucune fenetre trouvee (TitreContient='$TitreContient', Moitie=$Moitie)."
    exit 1
}
if ($nombre -gt 1) {
    Write-Error "Plusieurs fenetres correspondent, preciser TitreContient : $(($candidats | ForEach-Object { $_.Value }) -join ' | ')"
    exit 1
}

$hwnd = $candidats[0].Key
$titre = $candidats[0].Value
. (Join-Path $PSScriptRoot 'focus_fiable.ps1')
Assert-FocusFenetre -Hwnd $hwnd -Reactiver

$rect = New-Object RectFEnvoi
[FenetreFinderEnvoi]::GetWindowRect($hwnd, [ref]$rect) | Out-Null
$largeur = $rect.Right - $rect.Left
$hauteur = $rect.Bottom - $rect.Top
$x = [int]($rect.Left + $largeur * $PositionClicX)
$y = [int]($rect.Top + $hauteur * $PositionClicY)

if (-not $SeulementValider) {
    [FenetreFinderEnvoi]::SetCursorPos($x, $y)
    Start-Process -FilePath 'powershell.exe' -ArgumentList @('-NoProfile', '-WindowStyle', 'Hidden', '-File', (Join-Path $PSScriptRoot 'afficher_indicateur_clic.ps1'), '-X', $x, '-Y', $y) -WindowStyle Hidden -Wait
    Assert-FocusFenetre -Hwnd $hwnd -Reactiver
    [FenetreFinderEnvoi]::mouse_event($MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    [FenetreFinderEnvoi]::mouse_event($MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    Start-Sleep -Milliseconds $DelaiApresClicMs

    [System.Windows.Forms.SendKeys]::SendWait('^v')
    Start-Sleep -Milliseconds $DelaiApresCollerMs
}

if (-not $SansEnvoi) {
    [System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
}

Write-Output "Fenetre ciblee : $titre"
Write-Output "Clic en : $x, $y"
Write-Output "Colle : $(-not $SeulementValider)"
Write-Output "Envoye : $(-not $SansEnvoi)"
