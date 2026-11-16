import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

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


if __name__ == "__main__":
    unittest.main()
