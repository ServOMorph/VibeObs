"""Hook UserPromptSubmit : signale au modèle que le contexte dépasse le seuil de /compact.

Taille du contexte = input + cache_creation + cache_read du dernier appel lu dans le transcript.
Seuil : variable COMPACT_SEUIL (défaut 600000 tokens, 60 % d'une fenêtre de 1 M).
"""

import json
import os
import sys

SEUIL = int(os.environ.get("COMPACT_SEUIL", "600000"))
FIN_LUE = 2_000_000


def taille_contexte(chemin: str) -> int:
    with open(chemin, "rb") as f:
        f.seek(0, os.SEEK_END)
        f.seek(max(0, f.tell() - FIN_LUE))
        lignes = f.read().decode("utf-8", "replace").splitlines()
    for ligne in reversed(lignes):
        try:
            message = json.loads(ligne).get("message")
        except ValueError:
            continue
        usage = message.get("usage") if isinstance(message, dict) else None
        if usage:
            return sum(usage.get(k, 0) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    return 0


def main() -> int:
    try:
        chemin = json.load(sys.stdin).get("transcript_path", "")
        taille = taille_contexte(chemin) if chemin else 0
    except (ValueError, OSError):
        return 0
    if taille >= SEUIL:
        message = (
            f"Contexte à {taille} tokens (seuil {SEUIL}). Au début de ta réponse, proposer en une ligne "
            "à l'utilisateur de faire /compact à la prochaine fin d'étape.\n"
        )
        sys.stdout.buffer.write(message.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
