"""Tests for scripts/compare_swaps.py and the heating-source option in configure_system.py.

Numbers in the fixtures are test-only, not evidence.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, PROJECT_ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sw = load("compare_swaps_t", "scripts/compare_swaps.py")
tc = load("test_configure_system_t", "tests/test_configure_system.py")
cs = sw.cs


def fixture_with_heating(tmp: Path):
    c, s, l = tc.fixture_files(tmp)
    doc = json.loads(c.read_text(encoding="utf-8"))
    doc["running_inputs"] += [
        {"input_id": "greenhouse_heat_demand_m3_gas_per_m2_yr", "region": "here", "unit": "m3/m2/yr", "value": {"low": 10.0, "high": 10.0}},
        {"input_id": "natural_gas_price_per_m3", "region": "here", "unit": "x/m3", "value": {"low": 1.0, "high": 1.0}},
        {"input_id": "gas_heat_kwh_per_m3", "region": "here", "unit": "kWh/m3", "value": {"low": 8.0, "high": 8.0}},
        {"input_id": "heat_pump_seasonal_cop", "region": "here", "unit": "-", "value": {"low": 4.0, "high": 4.0}, "favourable": "high"},
    ]
    doc["components"].append(
        {"component_id": "hp_a", "name": "Heat pump", "category": "heating", "role": "heat_source", "region": "here",
         "sizing": {"driver": "structure_area_m2", "mode": "continuous", "per_driver_unit": 1.0, "unit_label": "m2"},
         "capex_per_unit": {"low": 5.0, "high": 5.0}, "lifetime_years": {"low": None, "high": None},
         "energy": None, "trade_offs": ["x"], "price_reliability": tc.REL})
    c.write_text(json.dumps(doc), encoding="utf-8")
    return c, s, l


BASE = dict(tc.BUILD, heating={"enabled": True}, structure_area_basis="planning_area_m2_uvi_ratio")


class HeatingSourceTests(unittest.TestCase):
    def evaluate(self, build):
        with tempfile.TemporaryDirectory() as tmp:
            paths = fixture_with_heating(Path(tmp))
            return cs.build_result(json.loads(json.dumps(build)), *paths, run_simulation=False)["cases"]["mid"]

    def test_gas_boiler_costs_gas(self):
        mid = self.evaluate(BASE)
        heat = next(r for r in mid["running"] if r["line_id"] == "heating")
        # structure = 10 m2 grow x land ratio 2 = 20 m2; 20 x 10 m3 = 200 m3 at 1.0
        self.assertEqual(heat["quantity"], 200.0)
        self.assertEqual(heat["cost_per_year"], 200.0)
        self.assertTrue(any("gas boiler" in g for g in mid["gaps"]))

    def test_heat_pump_turns_gas_into_electricity(self):
        build = dict(BASE, heating={"enabled": True, "source": "heat_pump"},
                     components=dict(BASE["components"], heating="hp_a"))
        mid = self.evaluate(build)
        heat = next(r for r in mid["running"] if r["line_id"] == "heating")
        # 200 m3 x 8 kWh/m3 = 1600 kWh heat / COP 4 = 400 kWh x 0.1 = 40
        self.assertEqual(heat["quantity"], 400.0)
        self.assertEqual(heat["cost_per_year"], 40.0)
        self.assertTrue(any("hp_a: lifetime" in g for g in mid["gaps"]))
        self.assertFalse(any("gas boiler" in g for g in mid["gaps"]))

    def test_unknown_heating_source_is_an_error(self):
        with self.assertRaises(cs.ConfigError):
            self.evaluate(dict(BASE, heating={"enabled": True, "source": "wood"}))


class SwapTests(unittest.TestCase):
    def compare(self, spec):
        with tempfile.TemporaryDirectory() as tmp:
            paths = fixture_with_heating(Path(tmp))
            return sw.compare_swaps(json.loads(json.dumps(spec)), *paths)

    def test_deep_merge_replaces_lists_and_merges_dicts(self):
        out = sw.deep_merge({"a": {"x": 1, "y": 2}, "b": [1, 2]}, {"a": {"y": 3}, "b": []})
        self.assertEqual(out, {"a": {"x": 1, "y": 3}, "b": []})

    def test_component_alternatives_are_added_with_deltas(self):
        res = self.compare({"base": BASE, "options": []})
        row = next(r for r in res["swaps"] if r["swap_id"] == "part_tank_b")
        self.assertEqual(row["status"], "ran")
        self.assertGreater(row["mid"]["cost_per_kg_plant"]["change"], 0)
        self.assertEqual(row["mid"]["plant_kg_yr"]["change"], 0)
        self.assertTrue(row["like_for_like"])
        self.assertEqual(res["estimate_status"], "scenario_estimate")

    def test_architecture_swap_reports_missing_yield_as_gap(self):
        spec = {"base": BASE, "include_component_alternatives": False, "options": [
            {"swap_id": "nft", "patch": {"grow_architecture": "nft", "components": {"grow_unit": []}}}]}
        row = self.compare(spec)["swaps"][0]
        self.assertIsNone(row["mid"]["cost_per_kg_plant"]["swap"])
        self.assertIsNotNone(row["mid"]["cost_per_m2_grow_yr"]["change"])
        self.assertLess(row["mid"]["feed_kg_yr"]["change"], 0)
        self.assertFalse(row["like_for_like"])
        self.assertTrue(any("plant yield" in g for g in row["new_gaps"]))

    def test_bad_swap_is_reported_not_raised(self):
        spec = {"base": BASE, "include_component_alternatives": False, "options": [
            {"swap_id": "bad", "patch": {"components": {"fish_tank": "nope"}}}]}
        row = self.compare(spec)["swaps"][0]
        self.assertEqual(row["status"], "not_run")
        self.assertTrue(sw.summary_lines(self.compare(spec)))

    def test_shipped_swap_runs(self):
        for name in ("swaps_basil_nl", "swaps_basil_karnataka"):
            spec = json.loads((PROJECT_ROOT / "runs" / f"{name}.json").read_text(encoding="utf-8"))
            res = sw.compare_swaps(spec["swaps"])
            self.assertTrue(all(r["status"] == "ran" for r in res["swaps"]), name)
            kinds = {r["kind"] for r in res["swaps"]}
            self.assertIn("architecture", kinds)
            self.assertIn("component", kinds)
        nl = sw.compare_swaps(json.loads((PROJECT_ROOT / "runs" / "swaps_basil_nl.json").read_text(encoding="utf-8"))["swaps"])
        hp = next(r for r in nl["swaps"] if r["swap_id"] == "heat_pump")
        self.assertIsNotNone(hp["mid"]["cost_per_kg_plant"]["change"])
        self.assertGreater(hp["mid"]["electricity_kwh_yr"]["change"], 0)

    def test_run_py_swaps_block(self):
        run_local = load("run_local_sw", "run.py")
        spec = json.loads((PROJECT_ROOT / "runs" / "swaps_basil_karnataka.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            result, lines = run_local.run_swaps(spec["swaps"], Path(tmp))
            self.assertTrue((Path(tmp) / "swaps_result.json").is_file())
            self.assertTrue((Path(tmp) / "swaps_comparison.csv").is_file())
        self.assertTrue(any(l.startswith("SWAPS") for l in lines))


class RelativeYieldTests(unittest.TestCase):
    def test_nft_yield_from_sourced_ratio(self):
        with tempfile.TemporaryDirectory() as tmp:
            c, s, l = tc.fixture_files(Path(tmp))
            doc = json.loads(s.read_text(encoding="utf-8"))
            doc["plants"][0]["sizing"]["yield_relative_to_reference_architecture"] = {
                "reference_architecture": "dwc_raft", "values": {"nft": {"low": 0.5, "high": 0.5}, "media_bed": None}}
            s.write_text(json.dumps(doc), encoding="utf-8")
            nft = cs.build_result(dict(tc.BUILD, grow_architecture="nft", components={"fish_tank": "tank_a", "water_pump": "pump_a"}),
                                  c, s, l, run_simulation=False)["cases"]["mid"]
            media = cs.build_result(dict(tc.BUILD, grow_architecture="media_bed", components={"fish_tank": "tank_a", "water_pump": "pump_a"}),
                                    c, s, l, run_simulation=False)["cases"]["mid"]
        # DWC mid yield 15 kg/m2/yr x 0.5 x 10 m2
        self.assertEqual(nft["sizing"]["plant_kg_yr"], 75.0)
        self.assertIn("ratio", nft["sizing"]["plant_yield_basis"])
        self.assertIsNone(media["sizing"]["plant_kg_yr"])
        self.assertTrue(any("plant yield" in g for g in media["gaps"]))


if __name__ == "__main__":
    unittest.main()
