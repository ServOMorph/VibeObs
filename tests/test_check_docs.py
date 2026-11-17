import os
import subprocess
import sys
import unittest
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_docs
from check_docs import journal_body

AVANT = "---\ntype: decision\nmaj: 2026-11-01\n---\n\n# Journal\n\n- 2026-11-01 : décision A.\n"


def append_only(previous, current):
    return journal_body(current).startswith(journal_body(previous))


class JournalAppendOnlyTests(unittest.TestCase):
    def test_maj_frontmatter_acceptee(self):
        apres = AVANT.replace("maj: 2026-11-01", "maj: 2026-11-15")
        self.assertTrue(append_only(AVANT, apres))

    def test_ajout_accepte(self):
        apres = AVANT + "- 2026-11-15 : décision B.\n"
        self.assertTrue(append_only(AVANT, apres))

    def test_modification_refusee(self):
        apres = AVANT.replace("décision A", "décision A modifiée")
        self.assertFalse(append_only(AVANT, apres))

    def test_fins_de_ligne_crlf_neutres(self):
        self.assertTrue(append_only(AVANT, AVANT.replace("\n", "\r\n")))


@pytest.fixture
def repository(tmp_path, monkeypatch):
    monkeypatch.setattr(check_docs, "KIT_ROOT", tmp_path)
    monkeypatch.setattr(check_docs, "DOCS_DIR", tmp_path / "DOCUMENTATION")
    monkeypatch.setattr(check_docs, "INDEX_PATH", tmp_path / "DOCUMENTATION/INDEX.md")
    subprocess.run(["git", "init", str(tmp_path)], check=True, capture_output=True)
    return tmp_path


def commit_source(root, source="scripts/tool.py", day="2026-11-15", subject="feat: changement"):
    path = root / source
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(subject + "\n")
    env = dict(os.environ, GIT_AUTHOR_NAME="Test", GIT_AUTHOR_EMAIL="test@example.invalid",
               GIT_COMMITTER_NAME="Test", GIT_COMMITTER_EMAIL="test@example.invalid",
               GIT_AUTHOR_DATE=f"{day}T12:00:00+00:00", GIT_COMMITTER_DATE=f"{day}T12:00:00+00:00")
    subprocess.run(["git", "-C", str(root), "add", "--", source], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(root), "-c", "core.hooksPath=", "-c", "commit.gpgsign=false",
                    "commit", "-m", subject], env=env, check=True, capture_output=True)


def write_guide(root, body="`scripts/tool.py`", updated="2026-11-14", folder="20_guides"):
    path = root / "DOCUMENTATION" / folder / "guide.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\ntype: guide\ndescription: test\ntags: test\nmaj: {updated}\n---\n\n{body}\n", encoding="utf-8")
    return path


def test_newer_cited_source_warns_once_with_evidence(repository):
    commit_source(repository)
    write_guide(repository, "`scripts/tool.py` et `../../scripts/tool.py`")
    warnings = check_docs.check_stale_guides()
    assert len(warnings) == 1
    assert warnings[0].startswith("AVERTISSEMENT : 20_guides/guide.md")
    assert "maj 2026-11-14" in warnings[0]
    assert "scripts/tool.py (2026-11-15," in warnings[0]
    assert "feat: changement" in warnings[0]
    assert warnings[0].count("scripts/tool.py") == 1


@pytest.mark.parametrize("day,subject", [
    ("2026-11-13", "feat: ancien"),
    ("2026-11-14", "feat: même jour"),
    ("2026-11-15", "close(kit): session"),
    ("2026-11-15", "update: synchronisation"),
])
def test_old_same_day_and_housekeeping_commits_are_silent(repository, day, subject):
    commit_source(repository, day=day, subject=subject)
    write_guide(repository)
    assert check_docs.check_stale_guides() == []


def test_close_does_not_hide_earlier_functional_change(repository):
    commit_source(repository)
    commit_source(repository, day="2026-11-16", subject="close(kit): session")
    write_guide(repository)
    warnings = check_docs.check_stale_guides()
    assert len(warnings) == 1
    assert "2026-11-15" in warnings[0]
    assert "close(kit)" not in warnings[0]


def test_sources_links_and_prompt_markdown_are_supported(repository):
    commit_source(repository, source=".claude/commands/tool.md")
    write_guide(repository, "## Sources\n\n[Commande](../../.claude/commands/tool.md#section)")
    assert len(check_docs.check_stale_guides()) == 1


def test_documentation_and_uncited_changes_are_silent(repository):
    commit_source(repository, source="README.md")
    commit_source(repository)
    write_guide(repository, "`README.md` et `scripts/missing.py` et `scripts/*.py`")
    assert check_docs.check_stale_guides() == []


def test_untracked_source_and_non_guide_are_silent(repository):
    (repository / "untracked.py").write_text("pass\n", encoding="utf-8")
    write_guide(repository, "`untracked.py`")
    commit_source(repository)
    write_guide(repository, folder="10_concepts")
    assert check_docs.check_stale_guides() == []


@pytest.mark.parametrize("updated", ["2026-02-30", "inconnue", "", "2026-11-15\nextra: valeur"])
def test_invalid_or_current_date_is_silent(repository, updated):
    commit_source(repository)
    write_guide(repository, updated=updated)
    assert check_docs.check_stale_guides() == []


def test_references_stay_in_repository(repository, tmp_path):
    outside = tmp_path.parent / "outside.py"
    outside.write_text("pass\n", encoding="utf-8")
    path = write_guide(repository, "`../../../outside.py` `https://example.org/code.py` `$VAR/tool.py`")
    assert check_docs.cited_files(path, path.read_text(encoding="utf-8")) == []


def test_unavailable_git_is_silent(repository, monkeypatch):
    commit_source(repository)
    write_guide(repository)
    monkeypatch.setattr(check_docs, "git_output", lambda *args: None)
    assert check_docs.check_stale_guides() == []


@pytest.mark.parametrize("errors,expected", [([], 0), (["erreur existante"], 1)])
def test_warnings_preserve_exit_code(monkeypatch, capsys, errors, expected):
    for name in ("check_index", "check_links", "check_doublons", "check_style",
                 "check_journal_append_only", "check_invariants"):
        monkeypatch.setattr(check_docs, name, lambda: [])
    monkeypatch.setattr(check_docs, "check_index", lambda: errors)
    monkeypatch.setattr(check_docs, "check_stale_guides", lambda: ["AVERTISSEMENT : guide"])
    assert check_docs.main() == expected
    output = capsys.readouterr().out
    assert "AVERTISSEMENT : guide" in output
    if errors:
        assert "erreur existante" in output


if __name__ == "__main__":
    unittest.main()
