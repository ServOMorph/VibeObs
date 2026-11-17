#!/usr/bin/env python3
"""Contrôle qualité mécanique de DOCUMENTATION/ (sans correctif automatique)."""

import re
import subprocess
import sys
from datetime import date
from itertools import combinations
from pathlib import Path


KIT_ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
DOCS_DIR = KIT_ROOT / "DOCUMENTATION"
INDEX_PATH = DOCS_DIR / "INDEX.md"
EXCLUDED_NAMES = {"INDEX.md", "agent_role.md"}
EXCLUDED_DIRS = {"_contexte"}
FRONTMATTER_KEYS = ("type", "description", "tags", "maj")
SECRET_PATTERNS = (
    re.compile(r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|password|passwd|client[_-]?secret)\b\s*[:=]\s*['\"]?[A-Za-z0-9+/=_-]{16,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def git_output(*args):
    try:
        result = subprocess.run(
            ["git", "-C", str(KIT_ROOT), *args], capture_output=True, text=True,
            encoding="utf-8",
        )
    except OSError:
        return None
    return result.stdout if result.returncode == 0 else None


def documents():
    if not DOCS_DIR.exists():
        return []
    return [
        path for path in sorted(DOCS_DIR.rglob("*.md"))
        if path.name not in EXCLUDED_NAMES and not (set(path.relative_to(DOCS_DIR).parts) & EXCLUDED_DIRS)
    ]


def check_index():
    errors = []
    if not INDEX_PATH.exists():
        return ["DOCUMENTATION/INDEX.md introuvable"]
    content = INDEX_PATH.read_text(encoding="utf-8")
    listed = set()
    for match in re.finditer(r"^\|\s*\[[^\]]+\]\(([^)]+)\)\s*\|", content, re.MULTILINE):
        target = match.group(1).strip()
        if target.endswith(".md"):
            listed.add(target)
            if not (DOCS_DIR / target).is_file():
                errors.append(f"INDEX.md : document listé introuvable : {target}")
    for path in documents():
        rel = path.relative_to(DOCS_DIR).as_posix()
        if rel not in listed:
            errors.append(f"INDEX.md : .md non listé (orphelin) : {rel}")
    for line in content.splitlines():
        if not line.startswith("|") or "](" not in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 4 and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[3]):
            errors.append(f"INDEX.md : date MAJ absente ou invalide : {cells[0]}")
    return errors


def check_links():
    errors = []
    pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)")
    for path in sorted(DOCS_DIR.rglob("*.md")):
        for match in pattern.finditer(path.read_text(encoding="utf-8")):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if any(char in target for char in "{<>"):
                continue
            if not (path.parent / target).resolve().exists():
                errors.append(f"Lien mort : {target} (dans {path.relative_to(KIT_ROOT).as_posix()})")
    return errors


def prose_lines(path):
    lines, in_code = set(), False
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = " ".join(line.split())
        if stripped.startswith("```"):
            in_code = not in_code
        elif not in_code and len(stripped) >= 50 and not stripped.startswith(("#", "|", "<!--")):
            lines.add(stripped)
    return lines


def check_doublons():
    errors = []
    docs = documents()
    prose = {path: prose_lines(path) for path in docs}
    for first, second in combinations(docs, 2):
        count = len(prose[first] & prose[second])
        if count >= 3:
            errors.append(
                "Doublon potentiel : "
                f"{first.relative_to(DOCS_DIR).as_posix()} / {second.relative_to(DOCS_DIR).as_posix()} "
                f"({count} lignes de prose identiques)"
            )
    return errors


def check_style():
    errors = []
    for path in documents():
        rel = path.relative_to(DOCS_DIR)
        content = path.read_text(encoding="utf-8")
        if rel.parts[0] in {"10_concepts", "20_guides"} and len(content.splitlines()) > 200:
            errors.append(f"Règle d'écriture : {rel.as_posix()} dépasse 200 lignes")
        if not content.startswith("---\n"):
            errors.append(f"Règle d'écriture : frontmatter absent dans {rel.as_posix()}")
            continue
        for key in FRONTMATTER_KEYS:
            if not re.search(rf"^{key}:\s*\S", content, re.MULTILINE):
                errors.append(f"Règle d'écriture : clé frontmatter manquante ({key}) dans {rel.as_posix()}")
    return errors


def journal_body(content):
    content = content.replace("\r\n", "\n")
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            content = content[end + 5:]
    return content.strip()


def check_journal_append_only():
    journal = DOCS_DIR / "30_decisions" / "journal.md"
    if not journal.exists():
        return ["Journal introuvable : 30_decisions/journal.md"]
    commits = git_output("log", "--format=%H", "--", "DOCUMENTATION/30_decisions/journal.md")
    if commits is None:
        return ["Journal : git indisponible, contrôle append-only non effectué"]
    errors = []
    for commit in commits.split():
        current = git_output("show", f"{commit}:DOCUMENTATION/30_decisions/journal.md")
        previous = git_output("show", f"{commit}~1:DOCUMENTATION/30_decisions/journal.md")
        if current is not None and previous is not None:
            if not journal_body(current).startswith(journal_body(previous)):
                errors.append(f"Journal non append-only : le commit {commit[:8]} a modifié des lignes existantes")
    return errors


def check_invariants():
    errors = []
    history = git_output("log", "--format=%H%x00%s", "--name-only")
    if history is None:
        errors.append("Invariants : git indisponible, contrôle des commits non effectué")
    else:
        for block in history.split("\n\n"):
            lines = block.splitlines()
            if not lines or "\x00" not in lines[0]:
                continue
            _, subject = lines[0].split("\x00", 1)
            if "(documentation)" in subject:
                for changed in lines[1:]:
                    if changed and not changed.startswith("DOCUMENTATION/"):
                        errors.append(f"Invariant : le commit « {subject} » touche {changed} hors de DOCUMENTATION/")
    for path in sorted(DOCS_DIR.rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        for pattern in SECRET_PATTERNS:
            match = pattern.search(content)
            if match:
                line = content[:match.start()].count("\n") + 1
                errors.append(f"Invariant : secret potentiel dans {path.relative_to(KIT_ROOT).as_posix()}:{line}")
    return errors


def cited_files(path, content):
    """Résout les citations exactes, sans deviner les chemins ni développer les motifs."""
    tokens = re.findall(r"(?<!`)`([^`\n]+)`(?!`)", content)
    sources = re.search(r"^#{1,6} Sources[^\n]*\n(.*?)(?=^#{1,6} |\Z)", content, re.MULTILINE | re.DOTALL)
    if sources:
        tokens.extend(re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", sources.group(1)))
    found = set()
    for token in tokens:
        token = token.split("#", 1)[0].replace("\\", "/")
        if not token or re.search(r"[\s*?<>${}:]", token) or token.startswith(("/", "~")):
            continue
        bases = (path.parent,) if token.startswith(("./", "../")) else (KIT_ROOT, path.parent)
        for base in bases:
            candidate = (base / token).resolve()
            if candidate.is_relative_to(KIT_ROOT) and candidate.is_file():
                if candidate != path:
                    found.add(candidate.relative_to(KIT_ROOT).as_posix())
                break
    return sorted(found)


def check_stale_guides():
    """Alerte indicative : une source citée a un commit utile postérieur à la date maj."""
    warnings = []
    history = {}
    for path in documents():
        if path.relative_to(DOCS_DIR).parts[0] != "20_guides":
            continue
        content = path.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
        if not frontmatter:
            continue
        match = re.search(r"^maj:\s*['\"]?(\d{4}-\d{2}-\d{2})['\"]?\s*$", frontmatter.group(1), re.MULTILINE)
        if not match:
            continue
        try:
            updated = date.fromisoformat(match.group(1))
        except ValueError:
            continue
        changes = []
        for source in cited_files(path, content):
            source_path = Path(source)
            if source_path.suffix in {".md", ".txt"} and not (
                source.startswith((".claude/", "templates/"))
                or source_path.name in {"AGENTS.md", "CLAUDE.md", "GEMINI.md"}
            ):
                continue
            if source not in history:
                history[source] = git_output("--literal-pathspecs", "log", "--format=%cs%x00%h%x00%s", "--", source)
            for line in (history[source] or "").splitlines():
                fields = line.split("\x00", 2)
                if len(fields) != 3:
                    continue
                committed, commit, subject = fields
                if re.match(r"^(?:close\(|update:)", subject, re.IGNORECASE):
                    continue
                try:
                    newer = date.fromisoformat(committed) > updated
                except ValueError:
                    continue
                if newer:
                    changes.append(f"{source} ({committed}, {commit} : {subject})")
                break
        if changes:
            warnings.append(
                f"AVERTISSEMENT : {path.relative_to(DOCS_DIR).as_posix()} "
                f"probablement en retard (maj {updated}) ; source(s) : {' ; '.join(changes)}"
            )
    return warnings


def main():
    checks = (check_index, check_links, check_doublons, check_style, check_journal_append_only, check_invariants)
    errors = [error for check in checks for error in check()]
    for warning in check_stale_guides():
        print(warning)
    if errors:
        print("ECARTS DETECTES :")
        print("\n".join(f"  - {error}" for error in errors))
        return 1
    print("Tous les contrôles sont passants.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
