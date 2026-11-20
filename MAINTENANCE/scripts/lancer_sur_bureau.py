"""Lance un .bat dans une console visible et place ses fenêtres sur un bureau virtuel Windows.

Exécution avec le Python du venv qui contient pyvda : D:\\_outils\\venv_bureaux\\Scripts\\python.exe

Exemple :
  lancer_sur_bureau.py D:\\ServOMorph\\TableauDeBord\\run_tableau_de_bord.bat --bureau Accueil ^
      --fenetre run_tableau_de_bord --fenetre TableauDeBord

Les fenêtres sont repérées par un fragment de titre (--fenetre, répétable). Seules les fenêtres
nouvelles ou dont le titre a changé depuis le lancement sont déplacées : une fenêtre déjà ouverte
au même titre n'est jamais touchée. Le bureau courant de l'utilisateur n'est jamais changé.
"""

from __future__ import annotations

import argparse
import ctypes
import subprocess
import sys
import time
from ctypes import wintypes

from pyvda import AppView, get_virtual_desktops

user32 = ctypes.windll.user32
CREATE_NEW_CONSOLE = 0x00000010
EnumProc = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)


def titres_fenetres() -> dict[int, str]:
    res: dict[int, str] = {}

    def cb(hwnd, _):
        if user32.IsWindowVisible(hwnd):
            n = user32.GetWindowTextLengthW(hwnd)
            if n:
                buf = ctypes.create_unicode_buffer(n + 1)
                user32.GetWindowTextW(hwnd, buf, n + 1)
                res[hwnd] = buf.value
        return True

    user32.EnumWindows(EnumProc(cb), 0)
    return res


def trouver_bureau(nom: str):
    for d in get_virtual_desktops():
        if nom.lower() in d.name.lower():
            return d
    return None


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser()
    p.add_argument("bat")
    p.add_argument("--bureau", required=True, help="fragment du nom du bureau virtuel")
    p.add_argument("--fenetre", action="append", default=[], help="fragment de titre à déplacer")
    p.add_argument("--attente", type=float, default=45.0, help="secondes d'attente maximale")
    p.add_argument("--attendre-tout", action="store_true",
                   help="attendre toute la durée pour déplacer aussi les fenêtres tardives")
    a = p.parse_args()

    bureau = trouver_bureau(a.bureau)
    if bureau is None:
        print(f"ERREUR: bureau '{a.bureau}' introuvable")
        return 1
    print(f"Bureau cible : {bureau.number} {bureau.name}")

    avant = titres_fenetres()
    subprocess.Popen(["cmd", "/c", a.bat], creationflags=CREATE_NEW_CONSOLE)

    fragments = [f.lower() for f in a.fenetre]
    deplacees: dict[int, str] = {}
    limite = time.time() + a.attente
    while time.time() < limite:
        for hwnd, titre in titres_fenetres().items():
            if hwnd in deplacees:
                continue
            if avant.get(hwnd) == titre:
                continue
            if not any(f in titre.lower() for f in fragments):
                continue
            vue = AppView(hwnd=hwnd)
            if vue.desktop_id != bureau.id:
                vue.move(bureau)
            deplacees[hwnd] = titre
            print(f"Déplacée : [{hwnd}] {titre}")
        if len(deplacees) >= len(fragments) and not a.attendre_tout:
            break
        time.sleep(0.5)

    manquants = [f for f in fragments if not any(f in t.lower() for t in deplacees.values())]
    for f in manquants:
        print(f"ATTENTION: aucune fenêtre trouvée pour '{f}'")
    return 0 if not manquants else 2


if __name__ == "__main__":
    sys.exit(main())
