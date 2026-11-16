import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "garde_vram.py"


def lancer(commande: str) -> int:
    with tempfile.TemporaryDirectory() as dossier:
        env = dict(os.environ, VERTIA_ORCH_DIR=dossier, VRAM_SESSION="test")
        resultat = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=json.dumps({"tool_input": {"command": commande}}).encode("utf-8"),
            capture_output=True,
            env=env,
        )
    return resultat.returncode


class GardeVramTests(unittest.TestCase):
    def test_execution_bloquee(self):
        for commande in [
            'python ollama_call.py "bonjour"',
            r'python D:\ServOMorph\VibeObs\ollama_call.py "x"',
            "py ollama_call.py x",
            "python3.13 ./ollama_call.py x",
            "ollama run qwen2.5:7b",
            "curl http://localhost:11434/api/generate",
            "python outils/production/gen_images_qwen.py spec.json sortie",
            "python outils/musique/gen_musique.py spec.json musique",
            "python gen_images.py",
            r'"C:\Program Files\Blender Foundation\Blender 4.2\blender.exe" -b scene.blend -a',
            "blender --background scene.blend --python rendu.py",
        ]:
            with self.subTest(commande=commande):
                self.assertEqual(lancer(commande), 2)

    def test_mention_autorisee(self):
        for commande in [
            "cp templates/ollama_call.py projet/",
            "diff ollama_call.py templates/ollama_call.py",
            "sed -n 1,80p ollama_call.py",
            "git diff -- ollama_call.py",
            "python -m pytest tests/test_ollama_call.py -q",
            "ollama list",
            "cat outils/production/gen_images_qwen.py",
            "python -m pytest tests/test_gen_musique.py -q",
            "grep -rn blender projets/",
        ]:
            with self.subTest(commande=commande):
                self.assertEqual(lancer(commande), 0)


if __name__ == "__main__":
    unittest.main()
