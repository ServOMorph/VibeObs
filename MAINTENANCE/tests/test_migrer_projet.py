import os
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import migrer_projet as mp  # noqa: E402

pytestmark = pytest.mark.skipif(os.name != "nt", reason="robocopy requis")


@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(mp, "processus_actifs", lambda _d: [])
    src = tmp_path / "C" / "projet"
    (src / "sous").mkdir(parents=True)
    (src / "a.txt").write_text("bonjour", encoding="utf-8")
    (src / ".env").write_text("SECRET=1", encoding="utf-8")
    (src / "sous" / "conf.py").write_text(
        f'BASE = r"{src}"\nAUTRE = "{str(src).replace(chr(92), "/")}/x"\n'
        f'JSON = "{str(src).replace(chr(92), chr(92) * 2)}"\n', encoding="utf-8")
    (src / "bin.dat").write_bytes(b"\x00\x01" + str(src).encode())
    dest = tmp_path / "D"
    dest.mkdir()
    return src, dest, tmp_path / "Q"


def lancer(*args):
    return mp.main([str(a) for a in args])


def test_parcours_complet(env):
    src, dest, q = env
    cible = dest / "projet"
    assert lancer("copier", src, "--destination", dest) == 0
    assert lancer("verifier", src, "--destination", dest) == 0
    assert lancer("chemins", src, "--destination", dest, "--appliquer") == 0
    conf = (cible / "sous" / "conf.py").read_text(encoding="utf-8")
    assert str(src) not in conf
    assert f'r"{cible}"' in conf
    assert f'{str(cible).replace(chr(92), "/")}/x' in conf
    assert str(cible).replace("\\", "\\\\") in conf
    assert str(src).encode() in (cible / "bin.dat").read_bytes()
    assert lancer("quarantaine", src, "--destination", dest, "--quarantaine", q) == 1
    assert src.exists()
    assert lancer("quarantaine", src, "--destination", dest, "--quarantaine", q, "--confirmer") == 0
    assert not src.exists()
    jours = list(q.iterdir())
    assert len(jours) == 1
    assert (jours[0] / "projet" / ".env").read_text(encoding="utf-8") == "SECRET=1"
    assert "| projet |" in (jours[0] / "manifeste.md").read_text(encoding="utf-8")


def test_chemins_exclure_ext(env):
    src, dest, _ = env
    (src / "trace.log").write_text(str(src), encoding="utf-8")
    lancer("copier", src, "--destination", dest)
    lancer("chemins", src, "--destination", dest, "--appliquer", "--exclure-ext", "log")
    assert (dest / "projet" / "trace.log").read_text(encoding="utf-8") == str(src)
    assert str(src) not in (dest / "projet" / "sous" / "conf.py").read_text(encoding="utf-8")


def test_chemins_exclure_nom(env):
    src, dest, _ = env
    (src / "CLAUDE.md").write_text(str(src), encoding="utf-8")
    lancer("copier", src, "--destination", dest)
    lancer("chemins", src, "--destination", dest, "--appliquer", "--exclure-nom", "claude.md")
    assert (dest / "projet" / "CLAUDE.md").read_text(encoding="utf-8") == str(src)
    assert str(src) not in (dest / "projet" / "sous" / "conf.py").read_text(encoding="utf-8")


def test_fichiers_proteges_jamais_modifies(env):
    src, dest, _ = env
    (src / "sous" / "AGENTS.md").write_text(str(src), encoding="utf-8")
    lancer("copier", src, "--destination", dest)
    trouves = mp.chercher_chemins([str(dest / "projet")], str(src), str(dest / "projet"), True)
    assert (dest / "projet" / "sous" / "AGENTS.md").read_text(encoding="utf-8") == str(src)
    assert any("AGENTS.md  [protégé" in f for f, _ in trouves)


def test_copier_refuse_cible_existante(env):
    src, dest, _ = env
    (dest / "projet").mkdir()
    assert lancer("copier", src, "--destination", dest) == 1


def test_copier_refuse_si_processus(env, monkeypatch):
    src, dest, _ = env
    monkeypatch.setattr(mp, "processus_actifs", lambda _d: ["1 python.exe run.py"])
    assert lancer("copier", src, "--destination", dest) == 1
    assert not (dest / "projet").exists()


def test_verifier_detecte_ecart(env):
    src, dest, _ = env
    lancer("copier", src, "--destination", dest)
    (dest / "projet" / "a.txt").write_text("modifié", encoding="utf-8")
    assert lancer("verifier", src, "--destination", dest) == 1


def test_env_jamais_lu(env, monkeypatch):
    src, dest, _ = env
    lus = []
    vrai = mp.sha256
    monkeypatch.setattr(mp, "sha256", lambda c: lus.append(c) or vrai(c))
    lancer("copier", src, "--destination", dest)
    lancer("verifier", src, "--destination", dest)
    assert not any(os.path.basename(c) == ".env" for c in lus)
    assert all(".env" not in f for f, _ in mp.chercher_chemins([str(src)], str(src), "X", False))


def test_sans_lecture_ne_hache_rien(env, monkeypatch):
    src, dest, _ = env
    monkeypatch.setattr(mp, "sha256", lambda c: pytest.fail("lecture interdite"))
    monkeypatch.setattr(mp, "fichiers_texte", lambda r: pytest.fail("lecture interdite"))
    assert lancer("copier", src, "--destination", dest, "--sans-lecture") == 0
    assert lancer("verifier", src, "--destination", dest, "--sans-lecture") == 0
    assert lancer("analyser", src, "--destination", dest, "--sans-lecture") == 0


def test_processus_actifs_ignore_le_script(tmp_path):
    cible = tmp_path / "vide"
    cible.mkdir()
    r = subprocess.run([sys.executable, mp.__file__, "analyser", str(cible), "--destination",
                        str(tmp_path / "D")], capture_output=True, text=True, encoding="utf-8")
    assert "Processus actifs : 0" in r.stdout


def test_processus_actifs_detecte_un_processus(tmp_path):
    cible = tmp_path / "actif"
    cible.mkdir()
    p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)", str(cible)])
    try:
        assert any(str(p.pid) in l for l in mp.processus_actifs(cible))
    finally:
        p.kill()


def test_quarantaine_doublon_sans_copie_active(env):
    src, dest, q = env
    assert lancer("quarantaine", src, "--destination", dest, "--quarantaine", q, "--confirmer") == 1
    assert lancer("quarantaine", src, "--destination", dest, "--quarantaine", q,
                  "--confirmer", "--sans-copie-active", "--motif", "Doublon") == 0
    assert not src.exists()
