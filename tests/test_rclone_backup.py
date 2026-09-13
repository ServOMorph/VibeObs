import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).parent.parent / "templates" / "rclone_backup" / "backup_project.py"
SPEC = importlib.util.spec_from_file_location("rclone_backup", SCRIPT_PATH)
rclone_backup = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rclone_backup)


class TestRcloneBackup(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project = Path(self.temp_dir.name) / "Projet"
        self.project.mkdir()
        self.config = Path(self.temp_dir.name) / "rclone_backup.json"
        self.config.write_text(
            json.dumps({"remote": "projet_drive", "folder": "Projet"}), encoding="utf-8"
        )
        self.original_config = rclone_backup.CONFIG
        self.original_rclone = rclone_backup.RCLONE
        rclone_backup.CONFIG = self.config
        rclone_backup.RCLONE = Path(sys.executable)

    def tearDown(self):
        rclone_backup.CONFIG = self.original_config
        rclone_backup.RCLONE = self.original_rclone
        self.temp_dir.cleanup()

    def test_sync_uses_configured_canonical_folder(self):
        with patch.object(rclone_backup.subprocess, "run") as run:
            run.return_value.returncode = 0
            with patch.object(sys, "argv", ["backup_project.py", str(self.project)]):
                self.assertEqual(rclone_backup.main(), 0)

        command = run.call_args.args[0]
        self.assertEqual(command[1:4], ["sync", str(self.project), "projet_drive:BackUps/Projet"])
        self.assertIn("**/.env.*", command)
        self.assertIn("**/rclone.conf", command)
        self.assertIn("**/SECRETS.local.md", command)

    def test_check_is_one_way_and_does_not_sync(self):
        with patch.object(rclone_backup.subprocess, "run") as run:
            run.return_value.returncode = 0
            with patch.object(sys, "argv", ["backup_project.py", str(self.project), "--check"]):
                self.assertEqual(rclone_backup.main(), 0)

        command = run.call_args.args[0]
        self.assertEqual(command[1], "check")
        self.assertIn("--one-way", command)

    def test_rejects_path_as_drive_folder(self):
        self.config.write_text(
            json.dumps({"remote": "projet_drive", "folder": "BackUps/Autre"}), encoding="utf-8"
        )
        with patch.object(sys, "argv", ["backup_project.py", str(self.project)]):
            self.assertEqual(rclone_backup.main(), 1)


if __name__ == "__main__":
    unittest.main()
