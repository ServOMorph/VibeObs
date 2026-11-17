"""Hook PreCompact : journalise le compactage et rappelle l'état à conserver."""

import json
import os
import sys
from datetime import datetime
from pathlib import Path


CONSIGNE = (
    "Conserver dans le résumé la tâche en cours, les fichiers modifiés non commités "
    "et la prochaine étape. Après le compactage, relire _contexte/journal_session.md.\n"
)


def main() -> int:
    try:
        donnees = json.loads(sys.stdin.buffer.read().decode("utf-8"))
        racine = os.environ.get("CLAUDE_PROJECT_DIR") or donnees.get("cwd")
        trigger = donnees.get("trigger")
        if racine and trigger in ("manual", "auto"):
            contexte = Path(racine) / "_contexte"
            if contexte.is_dir():
                ligne = (
                    f"{datetime.now():%Y-%m-%d %H:%M} | action | "
                    f"compactage {trigger} : relire ce journal\n"
                )
                with (contexte / "journal_session.md").open(
                    "a", encoding="utf-8", newline="\n"
                ) as journal:
                    journal.write(ligne)
    except Exception:
        pass
    try:
        sys.stdout.buffer.write(CONSIGNE.encode("utf-8"))
        sys.stdout.buffer.flush()
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
