#!/usr/bin/env python3
"""Lance le moteur Intercom générique du kit avec la racine du kit."""
import os
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ["INTERCOM_ROOT"] = str(ROOT)
runpy.run_path(ROOT / "templates" / "intercom" / "intercom.py", run_name="__main__")
