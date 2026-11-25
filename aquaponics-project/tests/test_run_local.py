"""Tests for run.py, the local entry point. Numbers in fixtures are test-only, not evidence."""

import csv
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("run_local", PROJECT_ROOT / "run.py")
run_local = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(run_local)

TEST_INPUTS = {
    "configurations": [
        {
            "config_id": "T1",
            "label": "test config",
            "crop": "basil",
            "output_unit": "kg",
            "labour_mode": "hired",
            "yield_units_per_m2_yr": {"low": 10, "high": 20},
            "saleability_rate": {"low": 0.8, "high": 0.9},
            "labour_h_per_unit": {"low": 0.1, "high": 0.2},
            "electricity_kwh_per_m2_yr": {"low": 10, "high": 20},
            "price_per_unit": {"ref": "price"},
        }
    ],
    "locations": {
        "here": {
            "currency_code": "EUR",
            "wage_per_hour": {"low": 10, "high": 10},
            "electricity_per_kwh": {"low": 0.1, "high": 0.1},
            "price": {"low": 5, "high": 5},
        },
        "there": {
            "currency_code": "EUR",
            "wage_per_hour": {"low": 10, "high": 10},
            "electricity_per_kwh": {"low": 0.1, "high": 0.1},
            "price": {"low": 5, "high": 5},
        },
    },
}


class OverrideTests(unittest.TestCase):
    def test_sets_nested_value_and_matches_list_items_by_id(self):
        data = json.loads(json.dumps(TEST_INPUTS))
        notes = run_local.apply_overrides(data, {
            "locations.here.wage_per_hour": {"low": 1, "high": 2},
            "configurations.T1.labour_h_per_unit": {"low": 0.3, "high": 0.4},
            "_comment": "ignored",
        })
        self.assertEqual(data["locations"]["here"]["wage_per_hour"], {"low": 1, "high": 2})
        self.assertEqual(data["configurations"][0]["labour_h_per_unit"]["low"], 0.3)
        self.assertEqual(len(notes), 2)

    def test_typo_in_path_is_an_error(self):
        data = json.loads(json.dumps(TEST_INPUTS))
        with self.assertRaises(run_local.RunError):
            run_local.apply_overrides(data, {"locations.hre.wage_per_hour": 1})
        with self.assertRaises(run_local.RunError):
            run_local.apply_overrides(data, {"configurations.T9.price_per_unit": 1})

    def test_new_final_key_is_flagged(self):
        data = json.loads(json.dumps(TEST_INPUTS))
        notes = run_local.apply_overrides(data, {"locations.here.new_field": 1})
        self.assertTrue(any(n.startswith("new key added") for n in notes))


class RunTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.tmp_path = Path(self.tmp.name)
        self._out_root = run_local.OUT_ROOT
        run_local.OUT_ROOT = self.tmp_path / "out"

    def tearDown(self):
        run_local.OUT_ROOT = self._out_root
        self.tmp.cleanup()

    def write_run(self, spec):
        path = self.tmp_path / "t.json"
        path.write_text(json.dumps(spec), encoding="utf-8")
        return path

    def test_short_simulation_writes_summary_and_csv(self):
        path = self.write_run({
            "simulation": {
                "scenario": "data/simulation/scenarios/basil_raft_crop_cycle.json",
                "days": 2,
                "overrides": {"feeding.feed_rate_percent_body_weight_per_day": 1.0},
            }
        })
        with redirect_stdout(io.StringIO()) as out:
            self.assertEqual(run_local.run(path), 0)
        self.assertIn("Scenario estimate, not validated", out.getvalue())
        out_dir = run_local.OUT_ROOT / "t"
        rows = list(csv.DictReader(open(out_dir / "simulation_daily.csv", encoding="utf-8")))
        self.assertEqual(len(rows), 2)
        self.assertTrue((out_dir / "summary.txt").is_file())

    def test_unit_economics_skips_cleanly_without_compare_script(self):
        original = run_local.COMPARE_SCRIPT
        run_local.COMPARE_SCRIPT = self.tmp_path / "missing.py"
        try:
            path = self.write_run({"unit_economics": {}})
            with redirect_stdout(io.StringIO()) as out:
                self.assertEqual(run_local.run(path), 0)
            self.assertIn("skipped", out.getvalue())
        finally:
            run_local.COMPARE_SCRIPT = original

    @unittest.skipUnless(run_local.COMPARE_SCRIPT.is_file(), "needs scripts/compare_unit_configurations.py (PR #10)")
    def test_unit_economics_filters_locations_and_scales_area(self):
        inputs = self.tmp_path / "inputs.json"
        inputs.write_text(json.dumps(TEST_INPUTS), encoding="utf-8")
        path = self.write_run({
            "farm_area_m2": 100,
            "unit_economics": {"inputs": str(inputs), "locations": ["here"]},
        })
        with redirect_stdout(io.StringIO()):
            self.assertEqual(run_local.run(path), 0)
        rows = list(csv.DictReader(open(run_local.OUT_ROOT / "t" / "unit_economics.csv", encoding="utf-8")))
        self.assertEqual({r["location"] for r in rows}, {"here"})
        mid = next(r for r in rows if r["case"] == "mid")
        self.assertAlmostEqual(float(mid["headroom_for_farm_area_yr"]), round(float(mid["headroom_per_m2_yr"]) * 100), 0)
        self.assertEqual(mid["estimate_status"], "scenario_estimate")

    def test_bad_json_and_unknown_run_are_reported(self):
        bad = self.tmp_path / "bad.json"
        bad.write_text("{ not json", encoding="utf-8")
        with self.assertRaises(run_local.RunError):
            run_local.run(bad)
        with self.assertRaises(run_local.RunError):
            run_local.find_run_file("no_such_run_xyz")

    def test_example_run_files_are_valid_json(self):
        for f in run_local.RUNS_DIR.glob("*.json"):
            spec = json.loads(f.read_text(encoding="utf-8"))
            self.assertTrue(spec.get("simulation") or spec.get("unit_economics"), f.name)


if __name__ == "__main__":
    unittest.main()
