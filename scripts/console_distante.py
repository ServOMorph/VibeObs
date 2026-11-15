"""Lit l'écran d'une console Windows et y envoie des touches, même PC verrouillé.

Usage :
  python console_distante.py lire <pid> [lignes]
  python console_distante.py touche <pid> <texte>   (ENTREE, ECHAP, HAUT, BAS, TAB ou texte libre)
"""

import ctypes
import sys
from ctypes import wintypes

k32 = ctypes.WinDLL("kernel32", use_last_error=True)
GENERIC_RW = 0xC0000000
SHARE_RW = 3
OPEN_EXISTING = 3
KEY_EVENT = 1
TOUCHES = {"ENTREE": (0x0D, "\r"), "ECHAP": (0x1B, "\x1b"), "HAUT": (0x26, "\0"), "BAS": (0x28, "\0"), "TAB": (0x09, "\t")}


class COORD(ctypes.Structure):
    _fields_ = [("X", wintypes.SHORT), ("Y", wintypes.SHORT)]


class SMALL_RECT(ctypes.Structure):
    _fields_ = [("Left", wintypes.SHORT), ("Top", wintypes.SHORT), ("Right", wintypes.SHORT), ("Bottom", wintypes.SHORT)]


class CSBI(ctypes.Structure):
    _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", wintypes.WORD),
                ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]


class KEY_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("bKeyDown", wintypes.BOOL), ("wRepeatCount", wintypes.WORD), ("wVirtualKeyCode", wintypes.WORD),
                ("wVirtualScanCode", wintypes.WORD), ("UnicodeChar", wintypes.WCHAR), ("dwControlKeyState", wintypes.DWORD)]


class INPUT_RECORD(ctypes.Structure):
    _fields_ = [("EventType", wintypes.WORD), ("Event", KEY_EVENT_RECORD)]


def attacher(pid: int) -> None:
    k32.FreeConsole()
    if not k32.AttachConsole(pid):
        raise SystemExit(f"ERREUR: console du processus {pid} inaccessible (code {ctypes.get_last_error()})")


def ouvrir(nom: str):
    h = k32.CreateFileW(nom, GENERIC_RW, SHARE_RW, None, OPEN_EXISTING, 0, None)
    if h in (0, -1, wintypes.HANDLE(-1).value):
        raise SystemExit(f"ERREUR: ouverture {nom} impossible")
    return h


def lire(pid: int, lignes: int) -> str:
    attacher(pid)
    h = ouvrir("CONOUT$")
    info = CSBI()
    k32.GetConsoleScreenBufferInfo(h, ctypes.byref(info))
    largeur = info.dwSize.X
    fin = info.dwCursorPosition.Y
    debut = max(0, fin - lignes + 1)
    sortie = []
    buf = ctypes.create_unicode_buffer(largeur)
    lus = wintypes.DWORD()
    for y in range(debut, min(fin + 15, info.dwSize.Y)):
        k32.ReadConsoleOutputCharacterW(h, buf, largeur, COORD(0, y), ctypes.byref(lus))
        sortie.append(buf.value[: lus.value].rstrip())
    while sortie and not sortie[-1]:
        sortie.pop()
    return "\n".join(sortie)


def touche(pid: int, texte: str) -> None:
    attacher(pid)
    h = ouvrir("CONIN$")
    sequence = [TOUCHES[texte]] if texte in TOUCHES else [(0, c) for c in texte]
    records = []
    for vk, ch in sequence:
        for bas in (True, False):
            r = INPUT_RECORD()
            r.EventType = KEY_EVENT
            r.Event = KEY_EVENT_RECORD(bas, 1, vk, 0, ch, 0)
            records.append(r)
    tableau = (INPUT_RECORD * len(records))(*records)
    ecrits = wintypes.DWORD()
    if not k32.WriteConsoleInputW(h, tableau, len(records), ctypes.byref(ecrits)):
        raise SystemExit(f"ERREUR: envoi impossible (code {ctypes.get_last_error()})")


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[1] not in ("lire", "touche"):
        print(__doc__, file=sys.stderr)
        return 1
    pid = int(sys.argv[2])
    if sys.argv[1] == "lire":
        texte = lire(pid, int(sys.argv[3]) if len(sys.argv) > 3 else 40)
        k32.FreeConsole()
        sys.stdout.buffer.write(texte.encode("utf-8", "replace") + b"\n")
    else:
        if len(sys.argv) < 4:
            print("ERREUR: texte manquant", file=sys.stderr)
            return 1
        touche(pid, sys.argv[3])
        k32.FreeConsole()
        print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
