import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

KIT = Path(sys.argv[1])
OUT = Path(sys.argv[2])
CODE = Path(__file__).read_text(encoding="utf-8")


def ecrire(nom, rows, entree):
    meta = [{"label": "gen_dash.py", "value": CODE, "type": "code", "lang": "python"}, {"label": "Entrée", "value": entree}]
    (OUT / nom).write_text(json.dumps({"rows": rows, "meta": meta}, ensure_ascii=False), encoding="utf-8")


dates = subprocess.run(["git", "-C", str(KIT), "log", "--format=%cs"], capture_output=True, text=True, check=True).stdout.split()
semaines = {}
for d in dates:
    j = dt.date.fromisoformat(d)
    lundi = (j - dt.timedelta(days=j.weekday())).isoformat()
    semaines[lundi] = semaines.get(lundi, 0) + 1
debut = min(dt.date.fromisoformat(s) for s in semaines)
fin = max(dt.date.fromisoformat(s) for s in semaines)
rows, s = [], debut
while s <= fin:
    rows.append({"semaine": s.isoformat(), "commits": semaines.get(s.isoformat(), 0)})
    s += dt.timedelta(days=7)
ecrire("commits.json", rows, "git log --format=%cs (dépôt du kit)")

versions = []
for m in re.finditer(r"^## (v(\d+)\.(\d+)) — (\d{4}-\d{2}-\d{2})", (KIT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M):
    versions.append({"version": m.group(1), "majeure": int(m.group(2)), "mineure": int(m.group(3)), "date": m.group(4)})
versions.sort(key=lambda v: (v["majeure"], v["mineure"]))
for v in versions:
    v["type"] = "majeure" if v["mineure"] == 0 else "mineure"
ecrire("versions.json", versions, "CHANGELOG.md, titres « ## vX.Y — date »")

projets = []
for ligne in (KIT / "DEPLOYMENTS.md").read_text(encoding="utf-8").split("## Remotes rclone")[0].splitlines():
    cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
    if len(cellules) == 5 and re.match(r"v\d", cellules[3]):
        version = re.match(r"v\d+\.\d+", cellules[3]).group(0)
        projets.append({
            "projet": cellules[0],
            "version": version,
            "statut": "archivé" if "archivé" in cellules[3] else "actif",
            "date": cellules[4],
        })
ecrire("projets.json", projets, "DEPLOYMENTS.md, premier tableau (chemins non repris)")

signals = (KIT / "_contexte" / "signals.md").read_text(encoding="utf-8")
actions = signals.split("## Garde-fous permanents")[0]
backlog = (KIT / "_contexte" / "backlog.md").read_text(encoding="utf-8")
categories = re.findall(r"^- \[(\w+)\]", backlog, re.M)
etat = [
    {"indicateur": "commandes", "valeur": len(list((KIT / ".claude" / "commands").glob("*.md")))},
    {"indicateur": "actions_ouvertes", "valeur": len(re.findall(r"^- ", actions, re.M))},
    {"indicateur": "backlog", "valeur": len(categories)},
]
for c in sorted(set(categories)):
    etat.append({"indicateur": "backlog_" + c, "valeur": categories.count(c)})
ecrire("etat.json", etat, ".claude/commands/*.md ; _contexte/signals.md (actions ouvertes) ; _contexte/backlog.md")
print(len(rows), len(versions), len(projets), etat)

changements = []
texte = (KIT / "CHANGELOG.md").read_text(encoding="utf-8")
blocs = re.split(r"^## (v\d+\.\d+) — (\d{4}-\d{2}-\d{2})\s*$", texte, flags=re.M)
entrees = [(blocs[i], blocs[i + 1], blocs[i + 2]) for i in range(1, len(blocs) - 2, 3)]
entrees.sort(key=lambda e: tuple(int(x) for x in e[0][1:].split(".")), reverse=True)
for version, date, corps in entrees[:2]:
    rubrique = ""
    for ligne in corps.splitlines():
        if ligne.startswith("### "):
            rubrique = ligne[4:].strip()
        elif ligne.startswith("- "):
            changements.append({"version": version, "date": date, "rubrique": rubrique, "changement": ligne[2:].strip()})
ecrire("changements.json", changements, "CHANGELOG.md, entrées des deux dernières versions")
print(len(changements), [c["version"] for c in changements])
