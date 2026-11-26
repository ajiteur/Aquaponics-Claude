import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import heat_demand as hd  # noqa: E402


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.models = hd.load_models()

    def test_records_are_candidates_with_reliability(self):
        for model_id in (
            "climate_normals_de_bilt_1991_2020",
            "climate_normals_bengaluru_1991_2020",
            "greenhouse_heat_demand_degree_hour",
        ):
            rec = self.models[model_id]
            self.assertEqual(rec["status"], "candidate_pending_user_review")
            self.assertEqual(rec["approval_batch"], "pending_batch_003")
        normals = self.models["climate_normals_de_bilt_1991_2020"]
        for key in ("source_gate", "confidence", "confidence_reason", "corroboration"):
            self.assertIn(key, normals["review_metadata"])
        self.assertIn(normals["source_metadata"]["source_tier"], ("tier_1", "tier_2", "tier_3"))

    def test_normals_have_twelve_months(self):
        for model_id in ("climate_normals_de_bilt_1991_2020", "climate_normals_bengaluru_1991_2020"):
            monthly = self.models[model_id]["monthly"]
            self.assertEqual(len(monthly["t_min_c"]), 12)
            self.assertEqual(len(monthly["t_max_c"]), 12)
        rad = self.models["climate_normals_de_bilt_1991_2020"]["monthly"]["global_radiation_mj_m2_month"]
        self.assertEqual(sum(rad), 3648)


class PhysicsTests(unittest.TestCase):
    def setUp(self):
        self.nl = hd.load_models()["climate_normals_de_bilt_1991_2020"]

    def test_day_length(self):
        self.assertAlmostEqual(hd.day_length_hours(0.0, 100), 12.0, places=6)
        self.assertGreater(hd.day_length_hours(52.1, 172), 16.0)
        self.assertLess(hd.day_length_hours(52.1, 355), 8.0)

    def test_hourly_profile_conserves_radiation_and_range(self):
        for month in (0, 6):
            hours = hd.hourly_profile(self.nl, month)
            daily_mj = sum(h["solar_w_m2"] for h in hours) * 3600 / 1e6
            expected = self.nl["monthly"]["global_radiation_mj_m2_month"][month] / hd.DAYS_IN_MONTH[month]
            self.assertAlmostEqual(daily_mj, expected, delta=0.03 * expected)
            temps = [h["t_c"] for h in hours]
            self.assertLessEqual(max(temps), self.nl["monthly"]["t_max_c"][month] + 1e-9)
            self.assertGreaterEqual(min(temps), self.nl["monthly"]["t_min_c"][month] - 1e-9)

    def test_demand_monotonic(self):
        low = hd.annual_heat_demand_mj_m2(self.nl, 6.0, 0.5, 12, 8)["annual_mj_m2"]
        high = hd.annual_heat_demand_mj_m2(self.nl, 6.0, 0.5, 20, 18)["annual_mj_m2"]
        screened = hd.annual_heat_demand_mj_m2(self.nl, 6.0, 0.5, 20, 18, night_k_factor=0.645)["annual_mj_m2"]
        more_sun = hd.annual_heat_demand_mj_m2(self.nl, 6.0, 0.9, 20, 18)["annual_mj_m2"]
        self.assertLess(low, high)
        self.assertLess(screened, high)
        self.assertLess(more_sun, high)


class ResultTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results = hd.build_results(
            gas_price_eur_m3={"low": 1.339, "high": 1.454}, electricity_inr_kwh={"low": 3.45, "high": 7.1}
        )

    def test_labelled_scenario_estimate(self):
        self.assertEqual(self.results["estimate_status"], "scenario_estimate")
        self.assertIn("not validated", self.results["label"])

    def test_calibration_reproduces_kema_radish(self):
        case = next(c for c in self.results["netherlands_glasshouse"]["cases"] if c["case_id"] == "kema_radish_12_8")
        self.assertAlmostEqual(case["heat_demand_mj_m2_yr"]["low"], 381.5, delta=0.5)
        self.assertAlmostEqual(case["heat_demand_mj_m2_yr"]["high"], 381.5, delta=0.5)

    def test_pot_plant_check_within_ten_percent(self):
        check = next(v for v in self.results["calibration"]["validation"] if v["point_id"] == "kema2012_cold_pot_plant")
        self.assertLess(abs(check["error_fraction"]["low"]), 0.10)
        self.assertLess(abs(check["error_fraction"]["high"]), 0.10)

    def test_cost_is_a_range_and_basil_warmer_costs_more(self):
        cases = {c["case_id"]: c for c in self.results["netherlands_glasshouse"]["cases"]}
        for case in cases.values():
            self.assertLessEqual(case["gas_cost_eur_m2_yr"]["low"], case["gas_cost_eur_m2_yr"]["high"])
        self.assertGreater(cases["basil_preferred_26"]["gas_m3_m2_yr"]["low"], cases["kema_cold_pot_plant_15_13"]["gas_m3_m2_yr"]["high"])
        self.assertTrue(cases["basil_preferred_26"]["extrapolated_beyond_calibration"])
        self.assertLess(
            cases["basil_preferred_26_night_screen"]["gas_m3_m2_yr"]["high"], cases["basil_preferred_26"]["gas_m3_m2_yr"]["high"]
        )

    def test_karnataka_no_heat_at_chilling_floor(self):
        heating = self.results["karnataka_polyhouse"]["heating"]
        floor = next(c for c in heating["cases"] if c["case_id"] == "chilling_protection_10c")
        self.assertEqual(floor["heat_demand_kwh_th_m2_yr"]["high"], 0)
        self.assertFalse(any(c["case_id"].endswith("_night_screen") for c in heating["cases"]))
        cooling = self.results["karnataka_polyhouse"]["cooling"]
        kwh = cooling["fan_pad_electricity_kwh_m2_yr_if_run_every_day"]
        cost = cooling["electricity_cost_inr_m2_yr_if_run_every_day"]
        self.assertAlmostEqual(cost["low"], kwh["low"] * 3.45, delta=3)
        self.assertAlmostEqual(cost["high"], kwh["high"] * 7.1, delta=4)

    def test_missing_price_stays_missing(self):
        results = hd.build_results(gas_price_eur_m3=None)
        self.assertIsNone(results["netherlands_glasshouse"]["cases"][0]["gas_cost_eur_m2_yr"])
        self.assertEqual(results["netherlands_glasshouse"]["gas_price_basis"], "missing")
        self.assertIsNone(results["karnataka_polyhouse"]["cooling"]["electricity_cost_inr_m2_yr_if_run_every_day"])

    def test_karnataka_tariff_is_the_approved_one(self):
        rate = hd.karnataka_tariff()
        self.assertIsNotNone(rate)
        self.assertEqual(rate["approval_status"], "approved")


if __name__ == "__main__":
    unittest.main()
