"""Balayage en lecture seule : chemins vers un ancien dossier racine cités dans les fichiers texte d'un arbre.

Usage : balayer_chemins.py <arbre> <ancienne_racine> [--sortie rapport.tsv] [--ignorer NOM ...]

Pour chaque fichier concerné : projet (premier dossier sous <arbre>), nombre d'occurrences, noms de
dossiers cités sous l'ancienne racine, chemin du fichier. Ne modifie rien. Les fichiers .env* ne sont
jamais lus ; les dossiers ignorés ne sont pas parcourus.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import Counter, defaultdict

IGNORES = {".git", "node_modules", ".venv", "venv", "__pycache__", "site-packages"}
TAILLE_MAX = 5 * 1024 * 1024


def motif(ancienne: str) -> re.Pattern:
    parties = [re.escape(p) for p in re.split(r"[\\/]+", ancienne.strip("\\/")) if p]
    sep = r"(?:\\\\|\\|/)+"
    return re.compile((sep.join(parties) + sep + r"([^\\/\"'`|)\s,;:*?<>]+)").encode("utf-8"), re.IGNORECASE)


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser()
    p.add_argument("arbre")
    p.add_argument("ancienne_racine")
    p.add_argument("--sortie")
    p.add_argument("--ignorer", nargs="*", default=[])
    a = p.parse_args()

    rx = motif(a.ancienne_racine)
    ignores = IGNORES | set(a.ignorer)
    base = os.path.abspath(a.arbre)
    par_projet: dict[str, Counter] = defaultdict(Counter)
    lignes = []
    for dossier, sous, fichiers in os.walk(base):
        sous[:] = [s for s in sous if s not in ignores]
        rel_dossier = os.path.relpath(dossier, base)
        projet = "(racine)" if rel_dossier == "." else rel_dossier.split(os.sep)[0]
        for f in fichiers:
            if f.lower().startswith(".env") or f == "journal_session.md":
                continue
            chemin = os.path.join(dossier, f)
            try:
                if os.path.getsize(chemin) > TAILLE_MAX:
                    continue
                with open(chemin, "rb") as fh:
                    contenu = fh.read()
            except OSError:
                continue
            if b"\x00" in contenu[:8192]:
                continue
            trouves = rx.findall(contenu)
            if not trouves:
                continue
            noms = Counter(t.decode("utf-8", "replace") for t in trouves)
            par_projet[projet].update(noms)
            lignes.append((projet, sum(noms.values()), ",".join(sorted(noms)), chemin))

    if a.sortie:
        with open(a.sortie, "w", encoding="utf-8") as out:
            for ligne in sorted(lignes):
                out.write("\t".join(str(x) for x in ligne) + "\n")
    print(f"Fichiers concernés : {len(lignes)} dans {len(par_projet)} projet(s)")
    for projet in sorted(par_projet):
        c = par_projet[projet]
        nb = sum(1 for l in lignes if l[0] == projet)
        print(f"{projet} : {nb} fichier(s), {sum(c.values())} occurrence(s) -> " +
              ", ".join(f"{n}({k})" for n, k in c.most_common(6)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
