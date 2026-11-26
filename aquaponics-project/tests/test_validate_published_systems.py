import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import validate_published_systems as vps  # noqa: E402


class ObservationRecordTests(unittest.TestCase):
    def test_records_have_reliability_and_are_candidates(self):
        data = json.loads(vps.OBS_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["approval_batch"], "pending_batch_003")
        self.assertGreaterEqual(len(data["records"]), 3)
        for rec in data["records"]:
            self.assertIn(rec["source_metadata"]["source_tier"], ("tier_1", "tier_2", "tier_3"))
            for key in ("source_gate", "confidence", "confidence_reason", "corroboration"):
                self.assertIn(key, rec["review_metadata"], rec["system_id"])


class MetricTests(unittest.TestCase):
    def test_metric_error(self):
        m = vps.metric("x", 12.0, 10.0)
        self.assertAlmostEqual(m["error_fraction"], 0.2)
        self.assertTrue(m["within_25_percent"])
        self.assertFalse(vps.metric("x", 13.0, 10.0)["within_25_percent"])
        self.assertTrue(vps.metric("x", 12.0, 10.0)["scored"])

    def test_unscored_keeps_error_and_reason(self):
        m = vps.unscored(vps.metric("x", 20.0, 10.0), "why")
        self.assertFalse(m["scored"])
        self.assertEqual(m["excluded_reason"], "why")
        self.assertAlmostEqual(m["error_fraction"], 1.0)

    def test_hold_published_ph_zeroes_drift(self):
        s = {"nitrogen_model": {"pH_drift_per_mg_l_tan_removed": 0.01}}
        vps.hold_published_ph(s)
        self.assertEqual(s["nitrogen_model"]["pH_drift_per_mg_l_tan_removed"], 0.0)

    def test_metric_range(self):
        self.assertEqual(vps.metric_range("x", 1.1, 1.0, 1.2)["error_fraction"], 0.0)
        self.assertAlmostEqual(vps.metric_range("x", 0.5, 1.0, 1.2)["error_fraction"], -0.5)


class CommittedResultTests(unittest.TestCase):
    def test_results_file_is_labelled_and_lists_failures(self):
        results = json.loads(vps.RESULTS_PATH.read_text(encoding="utf-8"))
        self.assertEqual(results["estimate_status"], "scenario_estimate")
        self.assertEqual(len(results["cases"]), 3)
        flagged = [
            f"{c['system_id']}: {m['metric']}"
            for c in results["cases"] for m in c["metrics"] if m["scored"] and m["within_25_percent"] is False
        ]
        self.assertEqual(len(flagged), len(results["failures"]))

    def test_unscored_metrics_carry_a_reason(self):
        results = json.loads(vps.RESULTS_PATH.read_text(encoding="utf-8"))
        unscored = [m for c in results["cases"] for m in c["metrics"] if not m["scored"]]
        self.assertEqual(len(unscored), len(results["excluded_from_score"]))
        for m in unscored:
            self.assertTrue(m["excluded_reason"])
        self.assertEqual(results["scored_metric_count"],
                         sum(1 for c in results["cases"] for m in c["metrics"] if m["scored"]))


if __name__ == "__main__":
    unittest.main()
