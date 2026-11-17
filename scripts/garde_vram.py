"""Hook PreToolUse : bloque toute commande qui charge le GPU sans jeton VRAM VertIA détenu par cette session.

Code 0 : commande autorisée. Code 2 : commande bloquée (message renvoyé au modèle).
"""

import json
import os
import re
import sys
import time
from pathlib import Path

SESSION = os.environ.get("VRAM_SESSION", "vibeobs")
LOCK = Path(os.environ.get("VERTIA_ORCH_DIR", r"D:\ServOMorph\VertIA_v3\_orchestration")) / "state" / "lock.json"
MOTIFS_GPU = [
    r"(?<![\w.])py(thon[0-9.]*)?(\.exe)?\s+(\S*[\\/])?ollama_call\.py",
    r"\bollama(\.exe)?\s+(run|serve)\b",
    r"11434/api/(generate|chat|embed)",
    r"\bcomfyui\b",
    r"torch\.cuda",
    r"(?<![\w.])py(thon[0-9.]*)?(\.exe)?\s+(\S*[\\/])?(gen_images(_qwen)?|gen_musique)\.py",
    r"blender(\.exe)?[\"']?\s+(-b|--background|-P|--python)\b",
]
TEXTE_AFFICHE = re.compile(
    r"\b(echo|printf|Write-Host|Write-Output)\b((?:\s+-\w+)*)\s+(\"(?:[^\"\\]|\\.)*\"|'[^']*')",
    re.IGNORECASE,
)
SUBSTITUTION = re.compile(r"\$\([^)]*\)|`[^`]*`")
ACQUIRE = (
    r"D:\ServOMorph\VertIA_v3\_orchestration\vram_lock.py acquire " + SESSION + " --wait (sans --long pour Ollama)"
)
PYTHON_VERTIA = r"D:\ServOMorph\VertIA_v3\.venv\Scripts\python.exe"


def jeton_detenu() -> bool:
    try:
        lock = json.loads(LOCK.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return lock.get("holder") == SESSION and lock.get("expires", 0) > time.time()


def _texte_neutralise(m: re.Match) -> str:
    texte = m.group(3)
    gardes = " ".join(SUBSTITUTION.findall(texte)) if texte.startswith('"') else ""
    return f"{m.group(1)}{m.group(2)} {gardes}"


def neutraliser_textes(commande: str) -> str:
    return TEXTE_AFFICHE.sub(_texte_neutralise, commande)


def main() -> int:
    try:
        donnees = json.load(sys.stdin)
    except ValueError:
        return 0
    commande = str((donnees.get("tool_input") or {}).get("command", ""))
    if "vram_lock.py" in commande:
        return 0
    analysee = neutraliser_textes(commande)
    if not any(re.search(m, analysee, re.IGNORECASE) for m in MOTIFS_GPU):
        return 0
    if jeton_detenu():
        return 0
    message = (
        f"BLOQUE : commande GPU sans jeton VRAM pour la session « {SESSION} ». "
        f"Lancer en arrière-plan : {PYTHON_VERTIA} {ACQUIRE}, attendre le code 0 (code 7 = pause GPU utilisateur), puis relancer ; "
        f"Fin de tâche : `ollama stop <modèle>`, puis `release {SESSION}`.\n"
    )
    sys.stderr.buffer.write(message.encode("utf-8"))
    return 2


if __name__ == "__main__":
    sys.exit(main())
