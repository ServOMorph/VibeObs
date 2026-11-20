"""Migration sécurisée d'un dossier de projet vers un nouvel emplacement.

Étapes (une commande chacune, validation humaine entre deux) :
  analyser     état du dossier source : taille, git, processus actifs, chemins en dur
  copier       copie robocopy vers <destination>\\<nom> (refus si la cible existe)
  verifier     comparaison source / copie (SHA-256, git HEAD, git status)
  chemins      liste des chemins en dur ; --appliquer pour les remplacer
  quarantaine  copie de la source en quarantaine, vérification, retrait de la source
               (exige --confirmer)

Options de sécurité :
  --sans-lecture  aucune lecture de contenu (pas de SHA-256, pas de recherche de chemins) ;
                  la vérification se limite aux noms et tailles.
  Les fichiers .env* ne sont jamais lus : vérifiés par taille seulement, exclus des recherches.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import shutil
import stat
import subprocess
import sys
from pathlib import Path

DESTINATION_DEFAUT = r"D:\ServOMorph"
QUARANTAINE_DEFAUT = r"D:\_quarantaine"
DOSSIERS_IGNORES = {".git", "node_modules", ".venv", "venv", "__pycache__", "site-packages"}
TAILLE_MAX_TEXTE = 5 * 1024 * 1024
FICHIERS_PROTEGES = {"claude.md", "agents.md", "gemini.md"}


def chemin_long(p: str | Path) -> str:
    p = os.path.abspath(str(p))
    if os.name != "nt" or p.startswith("\\\\?\\"):
        return p
    return "\\\\?\\" + p


def est_env(nom: str) -> bool:
    return nom.lower().startswith(".env")


def parcourir(racine: str | Path, ignorer: set[str] | None = None):
    base = chemin_long(racine)
    for dossier, sous, fichiers in os.walk(base):
        if ignorer:
            sous[:] = [s for s in sous if s not in ignorer]
        for f in fichiers:
            complet = os.path.join(dossier, f)
            yield os.path.relpath(complet, base), complet


def sha256(chemin: str) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as fh:
        for bloc in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(bloc)
    return h.hexdigest()


def empreintes(racine: str | Path, sans_lecture: bool) -> dict[str, str]:
    res = {}
    for rel, complet in parcourir(racine):
        nom = os.path.basename(rel)
        if sans_lecture or est_env(nom):
            res[rel] = f"taille:{os.path.getsize(complet)}"
        else:
            res[rel] = sha256(complet)
    return res


def git(dossier: str | Path, *args: str) -> str | None:
    try:
        r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return r.stdout.strip() if r.returncode == 0 else None


def etat_git(dossier: str | Path) -> dict:
    if not os.path.isdir(os.path.join(str(dossier), ".git")):
        return {"git": False}
    statut = git(dossier, "status", "--porcelain")
    return {
        "git": True,
        "branche": git(dossier, "rev-parse", "--abbrev-ref", "HEAD"),
        "head": git(dossier, "rev-parse", "HEAD"),
        "remote": git(dossier, "remote", "get-url", "origin"),
        "non_commites": len(statut.splitlines()) if statut else 0,
        "non_pousses": git(dossier, "rev-list", "--count", "@{u}..HEAD"),
    }


def processus_actifs(dossier: str | Path) -> list[str]:
    if os.name != "nt":
        return []
    motif = str(Path(dossier)).replace("'", "''")
    exclus = f"@($PID, {os.getpid()})"
    cmd = ("Get-CimInstance Win32_Process | Where-Object { $_.ProcessId -notin " + exclus +
           " -and ($_.CommandLine -like '*" + motif +
           "*' -or $_.ExecutablePath -like '" + motif + "*') } | "
           "ForEach-Object { \"$($_.ProcessId) $($_.Name) $($_.CommandLine)\" }")
    try:
        r = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return ["ERREUR: détection des processus impossible"]
    return [l for l in r.stdout.splitlines() if l.strip() and "Get-CimInstance" not in l]


def variantes(ancien: str, nouveau: str) -> list[tuple[str, str]]:
    a = str(Path(ancien)).rstrip("\\/")
    n = str(Path(nouveau)).rstrip("\\/")
    paires = [
        (a.replace("\\", "\\\\"), n.replace("\\", "\\\\")),
        (a, n),
        (a.replace("\\", "/"), n.replace("\\", "/")),
    ]
    vues, res = set(), []
    for x, y in paires:
        if x not in vues:
            vues.add(x)
            res.append((x, y))
    return res


def motifs_octets(ancien: str, nouveau: str) -> list[tuple[re.Pattern, bytes]]:
    res = []
    for x, y in variantes(ancien, nouveau):
        for enc in ("utf-8", "cp1252"):
            try:
                xb, yb = x.encode(enc), y.encode(enc)
            except UnicodeEncodeError:
                continue
            if all(p.pattern != re.escape(xb) for p, _ in res):
                res.append((re.compile(re.escape(xb), re.IGNORECASE), yb))
    return res


def fichiers_texte(racine: str | Path, exclure_ext: tuple[str, ...] = (),
                   exclure_noms: tuple[str, ...] = ()):
    noms = {n.lower() for n in exclure_noms}
    for rel, complet in parcourir(racine, DOSSIERS_IGNORES):
        nom = os.path.basename(rel)
        if est_env(nom) or rel.lower().endswith(exclure_ext) or nom.lower() in noms:
            continue
        try:
            if os.path.getsize(complet) > TAILLE_MAX_TEXTE:
                continue
            with open(complet, "rb") as fh:
                contenu = fh.read()
        except OSError:
            continue
        if b"\x00" in contenu[:8192]:
            continue
        yield rel, complet, contenu


def chercher_chemins(racines: list[str], ancien: str, nouveau: str, appliquer: bool,
                     exclure_ext: tuple[str, ...] = (),
                     exclure_noms: tuple[str, ...] = ()) -> list[tuple[str, int]]:
    motifs = motifs_octets(ancien, nouveau)
    trouves = []
    for racine in racines:
        for rel, complet, contenu in fichiers_texte(racine, exclure_ext, exclure_noms):
            nouveau_contenu, total = contenu, 0
            for motif, remplacement in motifs:
                nouveau_contenu, n = motif.subn(lambda _m, r=remplacement: r, nouveau_contenu)
                total += n
            if total:
                protege = os.path.basename(rel).lower() in FICHIERS_PROTEGES
                etiquette = os.path.join(racine, rel) + ("  [protégé, non modifié]" if protege else "")
                trouves.append((etiquette, total))
                if appliquer and not protege:
                    with open(complet, "wb") as fh:
                        fh.write(nouveau_contenu)
    return trouves


def robocopy(source: str | Path, cible: str | Path) -> int:
    r = subprocess.run(["robocopy", str(source), str(cible), "/E", "/COPY:DAT", "/DCOPY:DAT",
                        "/R:1", "/W:1", "/NFL", "/NDL", "/NP", "/NJH"], capture_output=True,
                       text=True, encoding="cp850", errors="replace")
    print(r.stdout.strip())
    return r.returncode


def comparer(source: str | Path, cible: str | Path, sans_lecture: bool) -> list[str]:
    a, b = empreintes(source, sans_lecture), empreintes(cible, sans_lecture)
    ecarts = [f"différent: {k}" for k in a if k in b and a[k] != b[k]]
    ecarts += [f"absent de la copie: {k}" for k in a if k not in b]
    ecarts += [f"en trop dans la copie: {k}" for k in b if k not in a]
    print(f"Fichiers source {len(a)} / copie {len(b)} / écarts {len(ecarts)}")
    ga, gb = etat_git(source), etat_git(cible)
    if ga.get("git"):
        for cle in ("head", "non_commites"):
            if ga.get(cle) != gb.get(cle):
                ecarts.append(f"git {cle}: source={ga.get(cle)} copie={gb.get(cle)}")
    return ecarts


def _forcer_ecriture(fonction, chemin, _info):
    os.chmod(chemin, stat.S_IWRITE)
    fonction(chemin)


def ajouter_manifeste(dossier_q: Path, nom: str, source: Path, motif: str, active: str) -> None:
    manifeste = dossier_q / "manifeste.md"
    if not manifeste.exists():
        manifeste.write_text(
            f"# Manifeste de quarantaine — {dossier_q.name}\n\n"
            "| Élément | Origine | Date | Motif | Copie active |\n"
            "|---|---|---|---|---|\n", encoding="utf-8")
    with open(manifeste, "a", encoding="utf-8") as fh:
        fh.write(f"| {nom} | {source} | {dt.date.today().isoformat()} | {motif} | {active} |\n")


def cmd_analyser(a) -> int:
    src = Path(a.source)
    if not src.is_dir():
        print(f"ERREUR: {src} introuvable")
        return 1
    tailles = [os.path.getsize(c) for _, c in parcourir(src)]
    print(f"Dossier : {src}")
    print(f"Fichiers : {len(tailles)}  Mo : {sum(tailles) / 1048576:.1f}")
    for k, v in etat_git(src).items():
        print(f"{k} : {v}")
    cible = Path(a.destination) / src.name
    print(f"Cible : {cible} ({'EXISTE DÉJÀ' if cible.exists() else 'libre'})")
    procs = processus_actifs(src)
    print(f"Processus actifs : {len(procs)}")
    for p in procs:
        print(f"  {p}")
    if a.sans_lecture:
        print("Chemins en dur : non recherchés (--sans-lecture)")
    else:
        trouves = chercher_chemins([str(src)], str(src), str(cible), appliquer=False)
        print(f"Chemins en dur vers la source : {len(trouves)} fichier(s)")
        for f, n in trouves:
            print(f"  {n:>3}  {f}")
    return 0


def cmd_copier(a) -> int:
    src = Path(a.source)
    cible = Path(a.destination) / src.name
    if not src.is_dir():
        print(f"ERREUR: {src} introuvable")
        return 1
    if cible.exists():
        print(f"ARRÊT: {cible} existe déjà")
        return 1
    procs = processus_actifs(src)
    if procs:
        print("ARRÊT: processus actifs dans la source :")
        for p in procs:
            print(f"  {p}")
        return 1
    rc = robocopy(src, cible)
    if rc >= 8:
        print(f"ÉCHEC robocopy (code {rc})")
        return 1
    print(f"Copie terminée : {cible} (robocopy code {rc}, < 8 = succès)")
    return 0


def cmd_verifier(a) -> int:
    src = Path(a.source)
    cible = Path(a.destination) / src.name
    ecarts = comparer(src, cible, a.sans_lecture)
    for e in ecarts:
        print(f"  {e}")
    print("CONFORME" if not ecarts else "NON CONFORME")
    return 0 if not ecarts else 1


def cmd_chemins(a) -> int:
    src = Path(a.source)
    cible = Path(a.destination) / src.name
    racines = a.dans or [str(cible)]
    exclure = tuple("." + e.lower().lstrip(".") for e in (a.exclure_ext or []))
    trouves = chercher_chemins(racines, str(src), str(cible), appliquer=a.appliquer,
                               exclure_ext=exclure, exclure_noms=tuple(a.exclure_nom or []))
    verbe = "remplacé(s)" if a.appliquer else "trouvé(s)"
    print(f"Ancien : {src}\nNouveau : {cible}\n{len(trouves)} fichier(s), occurrences {verbe} :")
    for f, n in trouves:
        print(f"  {n:>3}  {f}")
    return 0


def cmd_quarantaine(a) -> int:
    src = Path(a.source)
    cible = Path(a.destination) / src.name
    dossier_q = Path(a.quarantaine) / dt.date.today().isoformat()
    q = dossier_q / src.name
    if not a.confirmer:
        print("ARRÊT: --confirmer requis (validation humaine)")
        return 1
    if not src.is_dir():
        print(f"ERREUR: {src} introuvable")
        return 1
    if not a.sans_copie_active and not cible.is_dir():
        print(f"ARRÊT: copie active {cible} absente")
        return 1
    if q.exists():
        print(f"ARRÊT: {q} existe déjà")
        return 1
    procs = processus_actifs(src)
    if procs:
        print("ARRÊT: processus actifs dans la source")
        return 1
    dossier_q.mkdir(parents=True, exist_ok=True)
    rc = robocopy(src, q)
    if rc >= 8:
        print(f"ÉCHEC robocopy (code {rc}), source conservée")
        return 1
    ecarts = comparer(src, q, a.sans_lecture)
    if ecarts:
        for e in ecarts:
            print(f"  {e}")
        print("ARRÊT: copie en quarantaine non conforme, source conservée")
        return 1
    if sys.version_info >= (3, 12):
        shutil.rmtree(chemin_long(src), onexc=_forcer_ecriture)
    else:
        shutil.rmtree(chemin_long(src), onerror=_forcer_ecriture)
    if src.exists():
        print(f"ATTENTION: {src} n'a pas pu être entièrement retiré")
        return 1
    active = "aucune" if a.sans_copie_active else str(cible)
    ajouter_manifeste(dossier_q, src.name, src, a.motif, active)
    print(f"Source retirée. Quarantaine : {q}\nManifeste : {dossier_q / 'manifeste.md'}")
    return 0


def construire_parseur() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="commande", required=True)

    def commun(s):
        s.add_argument("source")
        s.add_argument("--destination", default=DESTINATION_DEFAUT)
        s.add_argument("--sans-lecture", action="store_true")
        return s

    commun(sp.add_parser("analyser")).set_defaults(f=cmd_analyser)
    commun(sp.add_parser("copier")).set_defaults(f=cmd_copier)
    commun(sp.add_parser("verifier")).set_defaults(f=cmd_verifier)
    s = commun(sp.add_parser("chemins"))
    s.add_argument("--dans", nargs="*", help="dossiers où chercher (défaut : la copie)")
    s.add_argument("--appliquer", action="store_true")
    s.add_argument("--exclure-ext", nargs="*", help="extensions ignorées, ex. log")
    s.add_argument("--exclure-nom", nargs="*", help="noms de fichiers ignorés, ex. CLAUDE.md")
    s.set_defaults(f=cmd_chemins)
    s = commun(sp.add_parser("quarantaine"))
    s.add_argument("--quarantaine", default=QUARANTAINE_DEFAUT)
    s.add_argument("--motif", default="Migration C: vers D:")
    s.add_argument("--confirmer", action="store_true")
    s.add_argument("--sans-copie-active", action="store_true",
                   help="mise en quarantaine sans copie active (doublon)")
    s.set_defaults(f=cmd_quarantaine)
    return p


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    a = construire_parseur().parse_args(argv)
    return a.f(a)


if __name__ == "__main__":
    sys.exit(main())
