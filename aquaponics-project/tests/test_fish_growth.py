import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import fish_growth as fg  # noqa: E402

CANON = PROJECT_ROOT / "data/knowledge/species/fish/tilapia.json"


class RecordTests(unittest.TestCase):
    def test_runtime_matches_canon_and_is_candidate(self):
        canon = json.loads(CANON.read_text(encoding="utf-8"))["growth_feed_model"]
        self.assertEqual(fg.load_model(), canon)
        self.assertEqual(canon["status"], "candidate_pending_user_review")
        self.assertEqual(canon["approval_batch"], "pending_batch_003")
        for key in ("feed_conversion_ratio", "feeding_rate_pct_body_weight_by_size", "temperature_response"):
            meta = canon[key]["review_metadata"]
            for field in ("source_gate", "confidence", "confidence_reason", "corroboration"):
                self.assertIn(field, meta, key)


class FactorTests(unittest.TestCase):
    def setUp(self):
        self.model = fg.load_model()

    def test_temperature_points(self):
        self.assertEqual(fg.temperature_factor(16.0, self.model), 0.0)
        self.assertEqual(fg.temperature_factor(17.0, self.model), 0.0)
        self.assertAlmostEqual(fg.temperature_factor(22.0, self.model), 0.333)
        self.assertEqual(fg.temperature_factor(28.0, self.model), 1.0)
        self.assertEqual(fg.temperature_factor(32.0, self.model), 1.0)
        self.assertEqual(fg.temperature_factor(40.0, self.model), 0.0)

    def test_feeding_table(self):
        self.assertEqual(fg.feeding_rate_pct(0.2, self.model), 17.5)
        self.assertEqual(fg.feeding_rate_pct(100.0, self.model, "low"), 1.5)
        self.assertEqual(fg.feeding_rate_pct(500.0, self.model, "high"), 3.0)

    def test_gain_uses_fcr_and_temperature(self):
        self.assertAlmostEqual(fg.daily_gain_kg(1.7, 28.0, self.model), 1.0)
        self.assertAlmostEqual(fg.daily_gain_kg(1.7, 22.0, self.model), 0.333)
        self.assertEqual(fg.daily_gain_kg(1.7, 15.0, self.model), 0.0)


class UviCheckTests(unittest.TestCase):
    def test_table_range_brackets_uvi_at_uvi_temperatures(self):
        check = fg.uvi_check()
        cases = check["cases"]
        low = cases["low_feed_uvi_seasonal_24_to_29c_mean_over_year"]["model_end_g"]
        high = cases["high_feed_uvi_seasonal_24_to_29c_mean_over_year"]["model_end_g"]
        self.assertLess(low, check["published_end_g"])
        self.assertGreater(high, check["published_end_g"])


if __name__ == "__main__":
    unittest.main()
