import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import nitrate_sinks as ns  # noqa: E402

CANON_MODELS = PROJECT_ROOT / "data/knowledge/models/nitrification_models.json"


def basil():
    return json.loads((PROJECT_ROOT / "data/simulation/species/plants/basil.json").read_text(encoding="utf-8"))


class NitrateSinkTests(unittest.TestCase):
    def setUp(self):
        self.model = ns.load_model()

    def test_runtime_record_matches_canon_and_is_candidate(self):
        canon = json.loads(CANON_MODELS.read_text(encoding="utf-8"))
        record = next(r for r in canon["records"] if r["model_id"] == ns.MODEL_ID)
        self.assertEqual(self.model, record)
        self.assertEqual(record["status"], "candidate_pending_user_review")
        for part in ("water_exchange", "residual_loss"):
            meta = record[part]["review_metadata"]
            self.assertIn(meta["confidence"], ("high", "medium", "low"))
            self.assertTrue(meta["confidence_reason"])
            self.assertIn("status", meta["corroboration"])

    def test_calibration_closes_the_anchor_balance(self):
        f = ns.calibrated_residual_loss_fraction(self.model, 30.0, basil())
        anchors = self.model["residual_loss"]["calibration"]["anchors"]
        nitrified = anchors["feed_ratio_g_per_m2_day"] * 30.0 / 1000.0
        uptake = ns.anchor_shoot_n_uptake_g_per_m2_day(basil())
        exchange = 0.015 * anchors["nitrate_n_mg_L"] * anchors["water_volume_l_per_m2_grow_area"] / 1000.0
        self.assertAlmostEqual(nitrified, uptake + exchange + f * nitrified)
        self.assertTrue(0.5 < f < 0.9)

    def test_steady_state_holds_anchor_nitrate(self):
        f = ns.calibrated_residual_loss_fraction(self.model, 30.0, basil())
        anchors = self.model["residual_loss"]["calibration"]["anchors"]
        vol = anchors["water_volume_l_per_m2_grow_area"]
        nitrified = anchors["feed_ratio_g_per_m2_day"] * 30.0 / vol  # mg/L per day per m2 of area
        uptake = ns.anchor_shoot_n_uptake_g_per_m2_day(basil()) * 1000.0 / vol
        nitrate = 10.0
        for _ in range(2000):
            nitrate = ns.apply_sinks(nitrate_mg_l=nitrate, nitrified_mg_l=nitrified, plant_uptake_mg_l=uptake,
                                     exchange_fraction=0.015, residual_loss_fraction=f)["new_nitrate_mg_L"]
        self.assertAlmostEqual(nitrate, anchors["nitrate_n_mg_L"], delta=1.0)

    def test_sinks_never_go_negative(self):
        step = ns.apply_sinks(nitrate_mg_l=0.1, nitrified_mg_l=0.5, plant_uptake_mg_l=0.4,
                              exchange_fraction=0.015, residual_loss_fraction=0.9)
        self.assertGreaterEqual(step["new_nitrate_mg_L"], 0.0)

    def test_no_calibration_without_uptake_model(self):
        self.assertIsNone(ns.calibrated_residual_loss_fraction(self.model, 30.0, {"validation_benchmarks": {}}))


if __name__ == "__main__":
    unittest.main()
