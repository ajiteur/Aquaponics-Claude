import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import nitrification_model as nm  # noqa: E402
import simulate_day  # noqa: E402
import simulate_overlap_score as overlap  # noqa: E402

CANON_MODELS = PROJECT_ROOT / "data/knowledge/models/nitrification_models.json"


class ModelRecordTests(unittest.TestCase):
    def test_runtime_record_matches_canon(self):
        canon = json.loads(CANON_MODELS.read_text(encoding="utf-8"))
        canon_record = next(r for r in canon["records"] if r["model_id"] == nm.MODEL_ID)
        self.assertEqual(nm.load_model(), canon_record)
        self.assertEqual(canon_record["status"], "candidate_pending_user_review")

    def test_media_loading_uses_low_end(self):
        loading = nm.media_feed_loading_low_end()
        self.assertEqual(loading["biofilter_mbbr"], 8.0)
        self.assertEqual(loading["biofilter_fluidized_sand"], 16.0)


class FactorTests(unittest.TestCase):
    def setUp(self):
        self.model = nm.load_model()

    def test_ph_factor(self):
        self.assertEqual(nm.ph_factor(5.9, self.model), 0.0)
        self.assertAlmostEqual(nm.ph_factor(6.5, self.model), 0.5)
        self.assertEqual(nm.ph_factor(7.4, self.model), 1.0)

    def test_temperature_factor(self):
        self.assertEqual(nm.temperature_factor(28.0, self.model), 1.0)
        self.assertAlmostEqual(nm.temperature_factor(20.0, self.model), 1.0 - 5 * 0.04275)

    def test_do_factor(self):
        self.assertEqual(nm.do_factor(5.5, self.model), 1.0)
        self.assertAlmostEqual(nm.do_factor(1.0, self.model), 0.5)

    def test_tan_per_feed_prefers_protein_formula(self):
        value, basis = nm.tan_mg_per_g_feed({"feed_protein_fraction": 0.32}, {})
        self.assertAlmostEqual(value, 0.32 * 0.092 * 1000)
        self.assertIn("canonical", basis)
        value, basis = nm.tan_mg_per_g_feed({"feed_protein_fraction": None}, {"tan_generation_mg_per_g_feed": 30.0})
        self.assertEqual(value, 30.0)
        self.assertIn("placeholder", basis)


class MassBalanceTests(unittest.TestCase):
    def setUp(self):
        self.model = nm.load_model()

    def run_days(self, input_g, capacity_g, days=30, tan=0.6, pH=7.2):
        for _ in range(days):
            step = nm.step_day(
                tan_mg_l=tan, daily_tan_input_g=input_g, capacity_g_day=capacity_g,
                water_volume_l=6000.0, pH=pH, water_temp_c=28.0, do_mg_l=5.5,
                maturity=1.0, model=self.model,
            )
            tan = step["new_tan_mg_L"]
        return tan, step

    def test_settles_at_steady_state_below_capacity(self):
        tan, step = self.run_days(input_g=27.0, capacity_g=60.0)
        expected = nm.steady_state_tan_mg_l(27.0, 60.0, 4.0)
        self.assertAlmostEqual(tan, expected, delta=0.05)
        self.assertAlmostEqual(step["tan_removed_g"], 27.0, delta=0.1)

    def test_accumulates_when_load_exceeds_capacity(self):
        tan, _ = self.run_days(input_g=90.0, capacity_g=60.0)
        self.assertGreater(tan, 10.0)
        self.assertIsNone(nm.steady_state_tan_mg_l(90.0, 60.0, 4.0))

    def test_raft_capacity(self):
        surfaces = {"raft_grow_area_m2": 10.0}
        cap = nm.capacity_g_tan_day(surfaces, self.model, 30.0, {})
        self.assertAlmostEqual(cap, 10.0 * 180.0 * 30.0 / 1000.0)
        surfaces["dedicated_biofilter"] = {"variant_id": "biofilter_mbbr", "media_volume_m3": 0.1}
        cap2 = nm.capacity_g_tan_day(surfaces, self.model, 30.0, nm.media_feed_loading_low_end())
        self.assertAlmostEqual(cap2 - cap, 0.1 * 8.0 * 1000.0 * 30.0 / 1000.0)

    def test_surfaces_derived_for_raft_without_explicit_block(self):
        profile = json.loads((PROJECT_ROOT / "data/simulation/species/plants/basil.json").read_text(encoding="utf-8"))
        scenario = {"crop_system_type": "architecture_dwc_raft", "system": {}, "plant_crop": {"plant_count": 80}}
        self.assertAlmostEqual(nm.resolve_surfaces(scenario, profile)["raft_grow_area_m2"], 10.0)
        self.assertIsNone(nm.resolve_surfaces({"system": {}, "plant_crop": {"plant_count": 80}}, profile))

    def test_nh3_from_chemistry(self):
        nh3 = nm.unionized_nh3(2.0, 6.9, 28.0)
        self.assertGreater(nh3["nh3_mg_L"], nh3["nh3_n_mg_L"])
        self.assertLess(nh3["nh3_mg_L"], 0.05)


class BasilPhScoringTests(unittest.TestCase):
    def setUp(self):
        self.basil = overlap.load_species_profile("basil", "plant")

    def test_aquaponic_context_scores_uvi_ph(self):
        for pH in (6.9, 7.0, 7.4, 7.6):
            result = overlap.score_plant(self.basil, pH, 26.5, "aquaponics_coupled")
            self.assertEqual(result["pH_score"], 1.0, pH)
            self.assertEqual(result["pH_basis"], "aquaponics_coupled_pH_scoring")
        self.assertEqual(overlap.score_plant(self.basil, 7.8, 26.5, "aquaponics_coupled")["pH_score"], 0.0)

    def test_hydroponic_context_unchanged(self):
        self.assertEqual(overlap.score_plant(self.basil, 7.4, 26.5)["pH_score"], 0.0)
        self.assertEqual(overlap.score_plant(self.basil, 6.0, 26.5)["pH_score"], 1.0)

    def test_species_without_aquaponic_block_falls_back(self):
        lettuce = overlap.load_species_profile("lettuce", "plant")
        result = overlap.score_plant(lettuce, 6.5, 20.0, "aquaponics_coupled")
        self.assertEqual(result["pH_basis"], "hydroponic_pH_ranges")


class ShootNUptakeTests(unittest.TestCase):
    def test_uptake_from_growth(self):
        basil = overlap.load_species_profile("basil", "plant")
        uptake = simulate_day.shoot_n_uptake_g_day(basil, 10.0, 90)
        self.assertAlmostEqual(uptake, 10.0 * 90 * 0.112 * 0.04)
        model = basil["nutrient_response"]["shoot_n_uptake_model"]
        self.assertEqual(model["status"], "candidate_pending_user_review")
        for key in ("shoot_dry_matter_fraction", "tissue_n_fraction_of_dry_mass"):
            self.assertIn("confidence", model[key]["evidence_assessment"])

    def test_no_model_or_no_growth_returns_none(self):
        basil = overlap.load_species_profile("basil", "plant")
        self.assertIsNone(simulate_day.shoot_n_uptake_g_day(basil, None, 90))
        lettuce = overlap.load_species_profile("lettuce", "plant")
        self.assertIsNone(simulate_day.shoot_n_uptake_g_day(lettuce, 10.0, 90))


if __name__ == "__main__":
    unittest.main()
