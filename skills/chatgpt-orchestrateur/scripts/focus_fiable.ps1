if (-not ('FocusFiable' -as [type])) {
Add-Type @'
using System;
using System.Runtime.InteropServices;
using System.Threading;

public class FocusFiable {
    [DllImport("user32.dll")] static extern bool SetForegroundWindow(IntPtr h);
    [DllImport("user32.dll")] static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")] static extern IntPtr GetAncestor(IntPtr h, uint flags);
    [DllImport("user32.dll")] static extern bool IsIconic(IntPtr h);
    [DllImport("user32.dll")] static extern bool ShowWindow(IntPtr h, int cmd);
    [DllImport("user32.dll")] static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
    [DllImport("user32.dll")] static extern bool AttachThreadInput(uint a, uint b, bool attach);
    [DllImport("kernel32.dll")] static extern uint GetCurrentThreadId();
    [DllImport("user32.dll")] static extern void keybd_event(byte vk, byte scan, uint flags, UIntPtr extra);

    public static bool EstAuPremierPlan(IntPtr h) {
        IntPtr fg = GetForegroundWindow();
        return fg != IntPtr.Zero && GetAncestor(fg, 2) == GetAncestor(h, 2);
    }

    public static bool Activer(IntPtr h, int essais) {
        if (IsIconic(h)) ShowWindow(h, 9);
        for (int i = 0; i < essais; i++) {
            keybd_event(0x12, 0, 0, UIntPtr.Zero);
            keybd_event(0x12, 0, 2, UIntPtr.Zero);
            uint pid;
            uint threadAvant = GetWindowThreadProcessId(GetForegroundWindow(), out pid);
            uint threadCourant = GetCurrentThreadId();
            bool attache = threadAvant != 0 && threadAvant != threadCourant && AttachThreadInput(threadCourant, threadAvant, true);
            SetForegroundWindow(h);
            if (attache) AttachThreadInput(threadCourant, threadAvant, false);
            Thread.Sleep(150);
            if (EstAuPremierPlan(h)) return true;
        }
        return false;
    }
}
'@
}

function Assert-FocusFenetre {
    param([Parameter(Mandatory=$true)][IntPtr]$Hwnd, [switch]$Reactiver)
    if ([FocusFiable]::EstAuPremierPlan($Hwnd)) { return }
    if ($Reactiver -and [FocusFiable]::Activer($Hwnd, 5)) { return }
    Write-Error "Focus non obtenu sur la fenetre ciblee, aucun clic effectue."
    exit 2
}
