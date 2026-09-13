"""Sauvegarde miroir d'un dossier de projet vers Google Drive via rclone."""

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RCLONE = Path(os.environ["LOCALAPPDATA"]) / "rclone" / "rclone.exe"
CONFIG = Path(__file__).with_name("rclone_backup.json")

EXCLUDES = [
    ".git/**",
    "node_modules/**",
    "__pycache__/**",
    "venv/**",
    ".venv/**",
    "dist/**",
    "build/**",
    "test-results/**",
    "playwright-report/**",
    ".pytest_cache/**",
    ".ruff_cache/**",
    ".mypy_cache/**",
    "coverage/**",
    "htmlcov/**",
    ".netlify/**",
    "tmp/**",
    "**/.env",
    "**/.env.*",
    "**/*.pem",
    "**/*.key",
    "**/*.p12",
    "**/*.pfx",
    "**/credentials*.json",
    "**/token*.json",
    "**/rclone.conf",
    "**/settings.local.json",
    "**/SECRETS.local.md",
]


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    if len(sys.argv) not in {2, 3} or (len(sys.argv) == 3 and sys.argv[2] != "--check"):
        print("Usage: python backup_project.py <chemin_projet> [--check]")
        return 1

    if not RCLONE.exists():
        print(f"ERREUR : rclone introuvable à {RCLONE}")
        return 1

    try:
        config = json.loads(CONFIG.read_text(encoding="utf-8"))
        remote = config["remote"].strip()
        drive_folder = config["folder"].strip()
    except (FileNotFoundError, KeyError, json.JSONDecodeError, AttributeError):
        print(f"ERREUR : compte Google Drive non configuré dans {CONFIG}")
        return 1
    if not remote or not drive_folder or drive_folder in {".", ".."} or "/" in drive_folder or "\\" in drive_folder:
        print(f"ERREUR : compte Google Drive non configuré dans {CONFIG}")
        return 1

    project_path = Path(sys.argv[1])
    if not project_path.is_dir():
        print(f"ERREUR : dossier introuvable {project_path}")
        return 1

    drive_dest = f"{remote}:BackUps/{drive_folder}"
    check_only = len(sys.argv) == 3
    command = [str(RCLONE), "check" if check_only else "sync", str(project_path), drive_dest]
    if check_only:
        command.append("--one-way")
    for pattern in EXCLUDES:
        command += ["--exclude", pattern]

    action = "Contrôle" if check_only else "Sauvegarde"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action} {project_path} -> {drive_dest}")
    result = subprocess.run(
        command, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    if result.returncode != 0:
        print(f"ERREUR {action.lower()} : {result.stderr.strip()}")
        return 1

    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action} OK -> {drive_dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
