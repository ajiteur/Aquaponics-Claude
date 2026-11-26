import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import simulate_day  # noqa: E402
import simulate_overlap_score as overlap  # noqa: E402


class YieldResponseTests(unittest.TestCase):
    def setUp(self):
        self.basil = overlap.load_species_profile("basil", "plant")

    def test_anchor_unchanged(self):
        f = simulate_day.yield_response_factors(self.basil, 8.0, None)
        self.assertEqual((f["density_factor"], f["light_factor"]), (1.0, 1.0))
        self.assertEqual(simulate_day.yield_response_factors(self.basil, 8.0, 25.0)["light_factor"], 1.0)

    def test_density_lowers_per_plant_but_raises_per_m2(self):
        f = simulate_day.yield_response_factors(self.basil, 32.0, None)["density_factor"]
        self.assertLess(f, 1.0)
        self.assertGreater(32.0 * f, 8.0)
        self.assertAlmostEqual(f, 4.0 ** (0.394 - 1.0), places=3)
        self.assertEqual(simulate_day.yield_response_factors(self.basil, 4.0, None)["density_factor"], 1.0)

    def test_light_points(self):
        light = lambda dli: simulate_day.yield_response_factors(self.basil, 8.0, dli)["light_factor"]
        self.assertAlmostEqual(light(9.3), 0.56)
        self.assertAlmostEqual(light(5.5), 0.166)
        self.assertLess(light(3.0), light(5.5))
        self.assertEqual(light(0.0), 0.0)

    def test_model_is_candidate(self):
        model = self.basil["yield_response_model"]
        self.assertEqual(model["approval_batch"], "pending_batch_003")
        for key in ("density_response", "light_response"):
            self.assertIn("confidence", model[key]["review_metadata"])


if __name__ == "__main__":
    unittest.main()
