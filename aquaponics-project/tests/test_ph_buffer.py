import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import ph_buffer as pb  # noqa: E402

CANON = PROJECT_ROOT / "data/knowledge/models/water_chemistry_models.json"


def water(ph=7.0, alk=100.0):
    return {"pH": ph, "alkalinity_mg_L_as_CaCO3": alk}


class PhBufferTests(unittest.TestCase):
    def setUp(self):
        self.model = pb.load_model()

    def test_runtime_matches_canon_and_is_candidate(self):
        record = next(r for r in json.loads(CANON.read_text(encoding="utf-8"))["records"] if r["model_id"] == pb.MODEL_ID)
        self.assertEqual(self.model, record)
        self.assertEqual(record["status"], "candidate_pending_user_review")
        for coeff in record["coefficients"].values():
            meta = coeff.get("review_metadata")
            if meta:
                self.assertIn(meta["confidence"], ("high", "medium", "low"))
                self.assertTrue(meta["confidence_reason"])
                self.assertIn("status", meta["corroboration"])

    def test_constants_match_25c_reference(self):
        self.assertAlmostEqual(pb.pk1(25.0, self.model), 6.35, places=2)
        self.assertAlmostEqual(pb.pk2(25.0, self.model), 10.33, places=2)
        self.assertLess(pb.pk1(30.0, self.model), pb.pk1(20.0, self.model))

    def test_course_worked_example(self):
        # 100 mg/L alkalinity and 40 mg/L CO2 give about pH 6.7 (6.8 in the course table, no activity correction).
        self.assertAlmostEqual(pb.ph_from_alkalinity(100.0, 40.0, 25.0, self.model), 6.69, places=2)

    def test_round_trip(self):
        co2 = pb.co2_from_ph(7.3, 120.0, 26.0, self.model)
        self.assertAlmostEqual(pb.ph_from_alkalinity(120.0, co2, 26.0, self.model), 7.3, places=4)
        self.assertAlmostEqual(pb.alkalinity_for_ph(7.3, co2, 26.0, self.model), 120.0, places=3)

    def step(self, **kw):
        args = dict(water=water(), cfg={"source_water_alkalinity_mg_L_as_CaCO3": 100.0}, temp_c=25.0,
                    tan_nitrified_mg_l=1.0, residual_n_loss_mg_l=0.0, plant_no3_uptake_mg_l=0.0,
                    exchange_fraction=0.0, target_ph=None, model=self.model)
        args.update(kw)
        return pb.step_day(**args)

    def test_nitrification_consumes_7_05_per_mg_n_and_lowers_ph(self):
        r = self.step()
        self.assertAlmostEqual(r["alkalinity_mg_L_as_CaCO3"], 100.0 - 7.05, places=6)
        self.assertLess(r["pH"], 7.0)

    def test_returns_and_exchange(self):
        r = self.step(cfg={"source_water_alkalinity_mg_L_as_CaCO3": 200.0, "nh3_excretion_credit_g_CaCO3_per_g_N": 3.57,
                           "denitrified_share_of_residual_n_loss": 1.0, "plant_uptake_return_eq_per_mol_N": 1.0},
                      residual_n_loss_mg_l=0.5, plant_no3_uptake_mg_l=0.5, exchange_fraction=0.1)
        t = r["terms_mg_L_as_CaCO3"]
        self.assertAlmostEqual(t["nh3_excretion_credit"], 3.57)
        self.assertAlmostEqual(t["denitrification_return"], 1.785)
        self.assertAlmostEqual(t["plant_uptake_return"], 1.786, places=3)
        self.assertAlmostEqual(t["water_exchange"], 10.0)

    def test_base_dosing_restores_target_and_reports_base_mass(self):
        r = self.step(target_ph=7.0)
        self.assertAlmostEqual(r["pH"], 7.0, places=3)
        self.assertAlmostEqual(r["terms_mg_L_as_CaCO3"]["base_dose"], 7.05, places=2)
        koh = r["base_dose_g_per_m3"]["KOH"]
        self.assertAlmostEqual(koh * 0.892 + r["base_dose_g_per_m3"]["Ca(OH)2"] * 1.351, 7.05, places=2)

    def test_dose_cap(self):
        r = self.step(target_ph=7.0, tan_nitrified_mg_l=10.0, cfg={"source_water_alkalinity_mg_L_as_CaCO3": 100.0,
                                                                   "max_base_dose_mg_L_as_CaCO3_per_day": 5.0})
        self.assertAlmostEqual(r["terms_mg_L_as_CaCO3"]["base_dose"], 5.0)
        self.assertLess(r["pH"], 7.0)

    def test_requires_source_water(self):
        with self.assertRaises(ValueError):
            self.step(cfg={})


class SimulateDayIntegrationTests(unittest.TestCase):
    def test_buffer_scenario_tracks_alkalinity_and_doses_base(self):
        import tempfile
        from simulate_crop_cycle import run_cycle

        scenario = json.loads((PROJECT_ROOT / "data/simulation/scenarios/basil_raft_crop_cycle_uvi_feed_ratio.json").read_text(encoding="utf-8"))
        scenario["water_chemistry"] = {"model": pb.MODEL_ID, "source_water_alkalinity_mg_L_as_CaCO3": 120.0, "target_pH": 6.9}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "buffer_test.json"
            path.write_text(json.dumps(scenario), encoding="utf-8")
            result = run_cycle(path, 2)
        day = result["daily"][-1]
        self.assertLess(day["alkalinity_mg_L_as_CaCO3"], 120.0 + 30.0)
        self.assertAlmostEqual(day["pH"], 6.9, delta=0.02)
        self.assertTrue(day["base_dose_g_total"])
        self.assertEqual(result["final_state"]["derived"]["ph_buffer"]["model_basis"], "carbonate_alkalinity_buffer_candidate")


if __name__ == "__main__":
    unittest.main()
