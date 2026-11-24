import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("rev", PROJECT_ROOT / "scripts" / "build_basil_revenue_range.py")
rev = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rev)


def write(tmp: Path, name: str, data: dict) -> Path:
    path = tmp / name
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


class BasilRevenueRangeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.result = write(self.tmp, "r.json", {
            "scenario_id": "s",
            "harvest_events": [{
                "species_id": "plant_basil", "harvested_mass_kg_per_m2": 2.0, "harvested_mass_kg": 20.0,
                "grow_area_m2_at_anchor_density": 10.0, "output_basis": "runtime_native_calibrated_simulation",
            }],
            "daily": [{"tan_mg_L": 1.0, "unionized_nh3_mg_L": 0.1, "nitrate_mg_L": 40.0}],
        })
        self.inputs = write(self.tmp, "i.json", {"cases": {
            name: {"price_per_saleable_kg": p, "saleability_rate": 0.9, "provenance": {"currency_code": "EUR"}}
            for name, p in (("conservative", 7.0), ("base", 8.0), ("optimistic", 9.0))
        }})

    def test_revenue_math(self):
        out = rev.build([self.result], self.inputs, 13)
        base = out["scenarios"][0]["cases"]["base"]
        self.assertAlmostEqual(base["saleable_kg_per_m2_per_harvest"], 1.8)
        self.assertAlmostEqual(base["gross_revenue_per_m2_per_harvest"], 14.4)
        self.assertAlmostEqual(base["gross_revenue_per_m2_per_year"], 187.2)
        self.assertAlmostEqual(base["gross_revenue_per_year_for_scenario_area"], 1872.0)
        self.assertEqual(out["range_gross_revenue_per_m2_per_year"], {"low": 163.8, "high": 210.6})

    def test_labelled_and_cost_free(self):
        out = rev.build([self.result], self.inputs, 13)
        self.assertEqual(out["estimate_status"], "scenario_estimate")
        text = json.dumps(out)
        for key in ("profit", "margin_per", "break_even", "cost_per"):
            self.assertNotIn(f'"{key}', text)

    def test_missing_price_is_reported_not_filled(self):
        inputs = write(self.tmp, "i2.json", {"cases": {"base": {"price_per_saleable_kg": None, "saleability_rate": 0.9}}})
        out = rev.build([self.result], inputs, 13)
        self.assertEqual(out["scenarios"][0]["cases"]["base"], {"missing_inputs": ["price_per_saleable_kg"]})

    def test_run_without_basil_harvest_fails(self):
        empty = write(self.tmp, "e.json", {"scenario_id": "e", "harvest_events": []})
        with self.assertRaises(ValueError):
            rev.build([empty], self.inputs, 13)


if __name__ == "__main__":
    unittest.main()
