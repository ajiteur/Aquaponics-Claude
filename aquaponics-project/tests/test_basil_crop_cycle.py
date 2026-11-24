import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import simulate_day  # noqa: E402


def basil_profile():
    return json.loads((PROJECT_ROOT / "data/simulation/species/plants/basil.json").read_text(encoding="utf-8"))


class CropCycleCalibrationTests(unittest.TestCase):
    def test_calibration_matches_anchor(self):
        cal = simulate_day.crop_cycle_calibration(basil_profile())
        self.assertIsNotNone(cal)
        # 2.0 kg/m2 at 8 plants/m2 over 28 days
        self.assertAlmostEqual(cal["target_cut_mass_g_per_plant"], 250.0)
        self.assertAlmostEqual(cal["ideal_rate_g_per_plant_day"], 250.0 / 28)

    def test_no_calibration_without_cycle_context(self):
        self.assertIsNone(simulate_day.crop_cycle_calibration({"validation_benchmarks": {}}))

    def test_full_cycle_at_ideal_scores_hits_anchor(self):
        profile = basil_profile()
        scenario = {"time": {"day": 0}}
        crop = {"species_id": "plant_basil", "plant_count": 80, "days_since_transplant": 0}
        event = None
        for day in range(28):
            crop["days_since_transplant"] += 1
            event = simulate_day.update_harvestable_mass(scenario, crop, profile, 1.0, 1.0) or event
            scenario["time"]["day"] += 1
        self.assertIsNotNone(event)
        self.assertAlmostEqual(event["harvested_mass_kg_per_m2"], 2.0, places=2)
        self.assertIsNone(event["saleable_harvest_mass_kg"])
        self.assertEqual(event["estimate_status"], "scenario_estimate")
        self.assertEqual(crop["days_since_transplant"], 0)
        self.assertEqual(crop["harvestable_cut_mass_g_per_plant"], 0.0)

    def test_explicit_cull_fraction_sets_saleable_mass(self):
        profile = basil_profile()
        scenario = {"time": {"day": 27}}
        crop = {
            "species_id": "plant_basil",
            "plant_count": 8,
            "days_since_transplant": 28,
            "harvestable_cut_mass_g_per_plant": 241.071,
            "harvest_policy": {"cull_fraction": 0.1},
        }
        event = simulate_day.update_harvestable_mass(scenario, crop, profile, 1.0, 1.0)
        self.assertAlmostEqual(event["harvested_mass_kg"], 2.0, places=3)
        self.assertAlmostEqual(event["saleable_harvest_mass_kg"], 1.8, places=3)


if __name__ == "__main__":
    unittest.main()
