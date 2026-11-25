import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("cuc", PROJECT_ROOT / "scripts" / "compare_unit_configurations.py")
cuc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cuc)


def rng(lo, hi):
    return {"low": lo, "high": hi}


LOCATION = {
    "currency_code": "EUR", "eur_per_currency_unit_for_comparison": 1.0,
    "wage_per_hour": rng(16.0, 20.0), "electricity_per_kwh": rng(0.2, 0.3),
    "basil_saleability_rate": rng(0.8, 1.0), "basil_wholesale_price_per_kg": rng(8.0, 10.0),
}


def config(**over):
    base = {
        "config_id": "X", "label": "x", "crop": "basil", "output_unit": "kg", "labour_mode": "hired",
        "yield_units_per_m2_yr": rng(10.0, 20.0),
        "price_per_unit": {"ref": "basil_wholesale_price_per_kg"},
        "saleability_rate": {"ref": "basil_saleability_rate"},
        "labour_h_per_m2_yr": rng(2.0, 4.0),
        "electricity_kwh_per_m2_yr": rng(100.0, 100.0),
    }
    base.update(over)
    return base


class CompareUnitConfigurationsTests(unittest.TestCase):
    def test_low_and_high_cases(self):
        out = cuc.evaluate(config(), "nl", LOCATION)
        low, high = out["cases"]["low"], out["cases"]["high"]
        # low: 10 kg x 0.8 x 8 = 64; labour 4 h x 20 = 80; power 100 x 0.3 = 30
        self.assertAlmostEqual(low["revenue_per_m2_yr"], 64.0)
        self.assertAlmostEqual(low["headroom_per_m2_yr"], 64.0 - 80.0 - 30.0)
        # high: 20 x 1.0 x 10 = 200; labour 2 x 16 = 32; power 100 x 0.2 = 20
        self.assertAlmostEqual(high["headroom_per_m2_yr"], 148.0)
        # break-even labour h/kg in high case: (10 x 1.0 - 20/20) / 16
        self.assertAlmostEqual(high["breakeven_labour_h_per_harvested_unit"], 0.5625)
        self.assertEqual(out["verdict"], "clears_only_in_favourable_cases")

    def test_labour_per_unit_scales_with_yield(self):
        c = config(labour_h_per_unit=rng(0.5, 0.5))
        del c["labour_h_per_m2_yr"]
        out = cuc.evaluate(c, "nl", LOCATION)
        self.assertAlmostEqual(out["cases"]["low"]["labour_h_per_m2_yr"], 5.0)
        self.assertAlmostEqual(out["cases"]["high"]["labour_h_per_m2_yr"], 10.0)

    def test_owner_mode_costs_no_cash_labour(self):
        out = cuc.evaluate(config(labour_mode="owner_uncosted"), "nl", LOCATION)
        low = out["cases"]["low"]
        self.assertEqual(low["labour_cost_per_m2_yr"], 0.0)
        self.assertEqual(low["owner_hours_per_m2_yr"], 4.0)
        self.assertAlmostEqual(low["headroom_per_owner_hour"], (64.0 - 30.0) / 4.0)

    def test_fx_given_as_object(self):
        loc = dict(LOCATION, currency_code="INR", eur_per_currency_unit_for_comparison={"value": 0.01})
        out = cuc.evaluate(config(), "in", loc)
        self.assertAlmostEqual(out["cases"]["high"]["eur_comparison"]["headroom_per_m2_yr"], 1.48)

    def test_missing_price_is_a_gap_not_a_number(self):
        c = config(price_per_unit={"by_location": {"nl": None}})
        out = cuc.evaluate(c, "nl", LOCATION)
        self.assertEqual(out["missing_inputs"], ["price"])
        self.assertEqual(out["cases"], {})

    def test_real_inputs_file_is_labelled(self):
        out = cuc.build(cuc.DEFAULT_INPUTS)
        self.assertEqual(out["estimate_status"], "scenario_estimate")
        self.assertIn("not total operating cost", out["label"])
        locations = {r["location"] for r in out["results"]}
        self.assertTrue({"netherlands", "india", "karnataka", "tamil_nadu", "andhra_pradesh", "telangana"} <= locations)
        text = json.dumps(out)
        for word in ('"profit', '"roi', '"payback', '"viable'):
            self.assertNotIn(word, text)


if __name__ == "__main__":
    unittest.main()
