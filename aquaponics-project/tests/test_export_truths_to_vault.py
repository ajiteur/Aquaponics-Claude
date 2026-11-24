import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import export_truths_to_vault as exporter  # noqa: E402


class ExportTruthsTests(unittest.TestCase):
    def test_note_title_is_filename_safe(self):
        title = exporter.note_title({"fact_id": "X_1", "statement": "Yield was 2.0 kg/m2: high? [yes]."})
        self.assertEqual(title, "X_1 Yield was 2.0 kg per m2 high yes")

    def test_link_explainers_links_first_mention_only(self):
        out = exporter.link_explainers("pH affects TAN; pH again.")
        self.assertEqual(out.count("[[Reference/Explainers/pH|pH]]"), 1)
        self.assertIn("[[Reference/Explainers/TAN|TAN]]", out)

    def test_every_fact_gets_one_note_and_hub_exists(self):
        outputs = exporter.build_outputs()
        facts = exporter.load_facts()
        truth_notes = [p for p in outputs if p.parent != exporter.TRUTHS_ROOT and p.stem != p.parent.name]
        self.assertEqual(len(truth_notes), len(facts))
        self.assertIn(exporter.TRUTHS_ROOT / "Truths.md", outputs)

    def test_candidate_truth_is_marked(self):
        outputs = exporter.build_outputs()
        candidate = next(t for p, t in outputs.items() if p.name.startswith("CROP_0001"))
        self.assertIn('status: "provisional"', candidate)
        self.assertIn("**Candidate truth.**", candidate)


if __name__ == "__main__":
    unittest.main()
