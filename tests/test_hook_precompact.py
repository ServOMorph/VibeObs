import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "hook_precompact.py"
CONSIGNE = (
    "Conserver dans le résumé la tâche en cours, les fichiers modifiés non commités "
    "et la prochaine étape. Après le compactage, relire _contexte/journal_session.md.\n"
)


def executer(entree, racine=None):
    environnement = os.environ.copy()
    environnement.pop("CLAUDE_PROJECT_DIR", None)
    environnement["PYTHONIOENCODING"] = "ascii"
    if racine is not None:
        environnement["CLAUDE_PROJECT_DIR"] = str(racine)
    resultat = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=entree.encode("utf-8"),
        capture_output=True,
        env=environnement,
        timeout=10,
    )
    assert resultat.returncode == 0
    assert resultat.stderr == b""
    assert resultat.stdout.decode("utf-8") == CONSIGNE
    return resultat


@pytest.mark.parametrize("trigger", ["manual", "auto"])
def test_json_valide_ajout_seul(tmp_path, trigger):
    contexte = tmp_path / "_contexte"
    contexte.mkdir()
    journal = contexte / "journal_session.md"
    precedent = "2026-11-17 14:00 | décision | étape validée\n"
    journal.write_text(precedent, encoding="utf-8")
    executer(json.dumps({"cwd": str(tmp_path), "trigger": trigger}))
    contenu = journal.read_text(encoding="utf-8")
    assert contenu.startswith(precedent)
    assert re.fullmatch(
        rf"\d{{4}}-\d{{2}}-\d{{2}} \d{{2}}:\d{{2}} \| action \| "
        rf"compactage {trigger} : relire ce journal\n",
        contenu[len(precedent):],
    )


def test_contexte_absent(tmp_path):
    executer(json.dumps({"cwd": str(tmp_path), "trigger": "auto"}))
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("entree", ["{invalide", "[]", "null", ""])
def test_entree_invalide_sans_ecriture(tmp_path, entree):
    contexte = tmp_path / "_contexte"
    contexte.mkdir()
    executer(entree, tmp_path)
    assert list(contexte.iterdir()) == []


def test_racine_absente():
    executer('{"trigger": "auto"}')


def test_utf8_et_priorite_variable_environnement(tmp_path):
    racine = tmp_path / "projet accentué"
    contexte = racine / "_contexte"
    contexte.mkdir(parents=True)
    autre = tmp_path / "autre"
    (autre / "_contexte").mkdir(parents=True)
    executer(
        json.dumps(
            {"cwd": str(autre), "trigger": "manual", "custom_instructions": "préserver l'état"},
            ensure_ascii=False,
        ),
        racine,
    )
    contenu = (contexte / "journal_session.md").read_bytes()
    assert contenu.decode("utf-8").endswith("compactage manual : relire ce journal\n")
    assert list((autre / "_contexte").iterdir()) == []


def test_erreur_ecriture_non_bloquante(tmp_path):
    contexte = tmp_path / "_contexte"
    contexte.mkdir()
    (contexte / "journal_session.md").mkdir()
    executer(json.dumps({"cwd": str(tmp_path), "trigger": "auto"}))


def test_trigger_invalide_sans_injection(tmp_path):
    contexte = tmp_path / "_contexte"
    contexte.mkdir()
    executer(json.dumps({"cwd": str(tmp_path), "trigger": "auto\nfausse ligne"}))
    assert list(contexte.iterdir()) == []
