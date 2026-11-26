"""Tests for scripts/configure_system.py and the component catalog.

Numbers in the fixtures below are test-only, not evidence.
"""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("configure_system", PROJECT_ROOT / "scripts" / "configure_system.py")
cs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cs)

REL = {"source_tier": "tier_3", "source_gate": "conditional", "source_gate_reason": "test",
       "confidence": "low", "confidence_reason": "test", "corroboration": {"status": "single_source", "source_ids": []}}


def fixture_files(tmp: Path, tank_price=100.0, pump_price=50.0):
    components = {
        "metadata": {"catalog_id": "t", "status": "candidate", "approval_status": "x"},
        "sources": {},
        "design_rules": {
            "fish_tank_retention_h": {"low": 1.0, "high": 1.0},
            "clarifier_hrt_min": {"low": 30.0, "high": 30.0},
            "air_lpm_per_kg_feed_day": {"low": 100.0, "high": 100.0},
            "raft_air_share_of_fish_air": {"low": 0.5, "high": 0.5},
            "raft_water_depth_m": {"low": 0.3, "high": 0.3},
            "raft_trough_width_m": {"low": 1.5, "high": 1.5},
            "makeup_water_fraction_per_day": {"low": 0.01, "high": 0.01},
            "land_to_grow_area_ratio_uvi": {"low": 2.0, "high": 2.0},
            "feeding_rate_architecture_factor": {"values": {"dwc_raft": 1.0, "nft": 0.25, "media_bed": 0.25}},
            "separate_biofilter_needed_for": {"values": ["nft"]},
        },
        "components": [
            {"component_id": "tank_a", "name": "Tank A", "category": "fish_tank", "role": "fish_tank", "region": "here",
             "sizing": {"driver": "fish_tank_volume_m3", "mode": "discrete", "capacity_per_unit": 1.0, "unit_label": "tanks"},
             "capex_per_unit": {"low": tank_price, "high": tank_price}, "lifetime_years": {"low": 10, "high": 10},
             "energy": None, "occupies_floor": True, "footprint_m2_per_unit": 1.5, "trade_offs": ["cheap"], "price_reliability": REL},
            {"component_id": "tank_b", "name": "Tank B", "category": "fish_tank", "role": "fish_tank", "region": "here",
             "sizing": {"driver": "fish_tank_volume_m3", "mode": "discrete", "capacity_per_unit": 1.0, "unit_label": "tanks"},
             "capex_per_unit": {"low": tank_price * 2, "high": tank_price * 2}, "lifetime_years": {"low": 10, "high": 10},
             "energy": None, "occupies_floor": True, "footprint_m2_per_unit": 1.5, "trade_offs": ["dear"], "price_reliability": REL},
            {"component_id": "pump_a", "name": "Pump A", "category": "water_pump", "role": "water_pump", "region": "here",
             "sizing": {"driver": "recirculation_flow_lph", "mode": "discrete", "capacity_per_unit": 10000.0, "unit_label": "pumps", "min_units": 1},
             "capex_per_unit": None if pump_price is None else {"low": pump_price, "high": pump_price},
             "lifetime_years": {"low": 5, "high": 5},
             "energy": {"power_w_per_unit": {"low": 100.0, "high": 100.0}, "duty_hours_per_day": 24},
             "trade_offs": [], "price_reliability": REL},
            {"component_id": "liner_a", "name": "Liner", "category": "grow_unit", "role": "liner", "region": "here",
             "architectures": ["dwc_raft"],
             "sizing": {"driver": "liner_area_m2", "mode": "continuous", "per_driver_unit": 1.0, "unit_label": "m2"},
             "capex_per_unit": {"low": 10.0, "high": 10.0}, "lifetime_years": {"low": 10, "high": 10},
             "energy": None, "trade_offs": [], "price_reliability": REL},
        ],
        "running_inputs": [
            {"input_id": "fish_feed_price_per_kg", "region": "here", "unit": "x/kg", "value": {"low": 1.0, "high": 2.0}},
        ],
        "labour_regimes": [
            {"regime_id": "hired", "label": "hired", "hours_per_m2_yr": {"low": 1.0, "high": 1.0}, "costed": True},
            {"regime_id": "owner", "label": "owner", "hours_per_m2_yr": {"low": 1.0, "high": 1.0}, "costed": False},
        ],
    }
    species = {
        "fish": [{"species_key": "fish1", "canon_ref": "x", "status": "candidate", "sizing": {
            "fcr": {"low": 2.0, "high": 2.0},
            "annual_production_kg_per_m3_tank": {"low": 100.0, "high": 100.0},
            "harvest_weight_kg": {"low": 0.5, "high": 0.5},
            "survival_fraction": {"low": 1.0, "high": 1.0}}}],
        "plants": [{"species_key": "plant1", "canon_ref": "x", "status": "candidate", "simulation_supported": False, "sizing": {
            "yield_kg_per_m2_yr": {"low": 10.0, "high": 20.0, "favourable": "high", "applies_to_architectures": ["dwc_raft"]},
            "feeding_rate_ratio_g_per_m2_day": {"low": 100.0, "high": 100.0},
            "heads_per_m2_yr": {"low": 10.0, "high": 10.0}}}],
    }
    locations = {"locations": {"here": {"currency_code": "EUR", "wage_per_hour": {"low": 10.0, "high": 10.0},
                                        "electricity_per_kwh": {"low": 0.1, "high": 0.1}}}}
    paths = []
    for name, doc in (("c.json", components), ("s.json", species), ("l.json", locations)):
        p = tmp / name
        p.write_text(json.dumps(doc), encoding="utf-8")
        paths.append(p)
    return paths


BUILD = {
    "build_id": "t", "region": "here", "location": "here", "fish": "fish1", "plant": "plant1",
    "grow_architecture": "dwc_raft", "target": {"grow_area_m2": 10},
    "components": {"fish_tank": "tank_a", "water_pump": "pump_a", "grow_unit": ["liner_a"]},
    "labour_regime": "hired",
}


class SizingAndCostTests(unittest.TestCase):
    def run_build(self, build=None, **kw):
        with tempfile.TemporaryDirectory() as tmp:
            c, s, l = fixture_files(Path(tmp), **kw)
            return cs.build_result(json.loads(json.dumps(build or BUILD)), c, s, l, run_simulation=False)

    def test_sizing_chain(self):
        mid = self.run_build()["cases"]["mid"]
        sz = mid["sizing"]
        # 10 m2 x 100 g/m2/day = 1 kg feed/day; 365 kg/yr; FCR 2 -> 182.5 kg fish; 100 kg/m3/yr -> 1.825 m3
        self.assertAlmostEqual(sz["feed_kg_day"], 1.0)
        self.assertAlmostEqual(sz["fish_kg_yr"], 182.5)
        self.assertAlmostEqual(sz["fish_tank_volume_m3"], 1.825)
        self.assertAlmostEqual(sz["recirculation_flow_lph"], 1825.0)
        self.assertAlmostEqual(sz["plant_kg_yr"], 150.0)   # mid yield 15
        self.assertAlmostEqual(sz["air_flow_lpm"], 150.0)  # 1 kg x 100 x (1 + 0.5)
        self.assertAlmostEqual(sz["liner_area_m2"], 14.0)  # 10 x (1 + 2 x 0.3 / 1.5)
        self.assertAlmostEqual(sz["minimum_area_m2"], 13.0)  # 10 + 2 tanks x 1.5
        self.assertAlmostEqual(sz["planning_area_m2_uvi_ratio"], 20.0)

    def test_costs_and_shares(self):
        mid = self.run_build()["cases"]["mid"]
        tank = next(l for l in mid["components"] if l["component_id"] == "tank_a")
        self.assertEqual(tank["quantity"], 2)            # ceil(1.825)
        self.assertEqual(tank["capex_per_year"], 20.0)   # 2 x 100 / 10
        pump = next(l for l in mid["components"] if l["component_id"] == "pump_a")
        self.assertEqual(pump["electricity_kwh_yr"], 876.0)
        feed = next(r for r in mid["running"] if r["line_id"] == "feed")
        self.assertEqual(feed["cost_per_year"], 547.5)   # 365 kg x 1.5
        self.assertEqual(mid["labour"]["cost_per_year"], 100.0)
        self.assertAlmostEqual(sum(b["share"] for b in mid["breakdown"]), 1.0, places=2)
        self.assertAlmostEqual(mid["cost_per_kg_plant"], mid["annual_cost_counted"] / 150.0, places=2)

    def test_cases_are_ordered(self):
        c = self.run_build()["cases"]
        self.assertLess(c["low_cost"]["cost_per_kg_plant"], c["mid"]["cost_per_kg_plant"])
        self.assertLess(c["mid"]["cost_per_kg_plant"], c["high_cost"]["cost_per_kg_plant"])

    def test_missing_price_is_a_gap_not_a_number(self):
        res = self.run_build(pump_price=None)
        mid = res["cases"]["mid"]
        pump = next(l for l in mid["components"] if l["component_id"] == "pump_a")
        self.assertIsNone(pump["capex_per_year"])
        self.assertIn("pump_a: price", res["gaps"])
        self.assertTrue(any("Fingerlings: price" in g for g in res["gaps"]))
        # electricity is still counted because the power rating is known
        self.assertIsNotNone(pump["electricity_cost_per_year"])

    def test_owner_labour_is_reported_not_costed(self):
        build = dict(BUILD, labour_regime="owner")
        mid = self.run_build(build)["cases"]["mid"]
        self.assertIsNone(mid["labour"]["cost_per_year"])
        self.assertEqual(mid["labour"]["hours_per_year"], 10.0)

    def test_output_target_sets_area(self):
        build = dict(BUILD, target={"plant_output_kg_per_year": 300})
        mid = self.run_build(build)["cases"]["mid"]
        self.assertAlmostEqual(mid["sizing"]["grow_area_m2"], 20.0)

    def test_alternatives_swap_within_role(self):
        alts = self.run_build()["alternatives_mid"]
        self.assertEqual([a["alternative"] for a in alts], ["tank_b"])
        self.assertGreater(alts[0]["change_per_kg_plant_mid"], 0)

    def test_yield_missing_for_other_architecture(self):
        build = dict(BUILD, grow_architecture="nft", components={"fish_tank": "tank_a"})
        res = self.run_build(build)
        self.assertIsNone(res["cases"]["mid"]["cost_per_kg_plant"])
        self.assertTrue(any("plant yield" in g for g in res["gaps"]))

    def test_bad_inputs_raise_config_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            c, s, l = fixture_files(Path(tmp))
            for bad in (dict(BUILD, plant="nope"), dict(BUILD, components={"fish_tank": "pump_a"}),
                        dict(BUILD, target={})):
                with self.assertRaises(cs.ConfigError):
                    cs.build_result(bad, c, s, l, run_simulation=False)

    def test_result_is_labelled_scenario_estimate(self):
        res = self.run_build()
        self.assertEqual(res["estimate_status"], "scenario_estimate")
        self.assertIn("not validated", res["label"])


class RealCatalogTests(unittest.TestCase):
    """The shipped catalog must keep the reliability fields AGENTS.md 6A asks for."""

    @classmethod
    def setUpClass(cls):
        cls.components = json.loads(cs.DEFAULT_COMPONENTS.read_text(encoding="utf-8"))
        cls.species = json.loads(cs.DEFAULT_SPECIES.read_text(encoding="utf-8"))

    def test_components_have_reliability_and_known_sources(self):
        sources = set(self.components["sources"])
        ids = set()
        for c in self.components["components"]:
            self.assertNotIn(c["component_id"], ids)
            ids.add(c["component_id"])
            self.assertEqual(c["status"], "candidate")
            self.assertIn(c["region"], ("netherlands", "india", "any"))
            rel_block = c["price_reliability"]
            for key in ("source_tier", "source_gate", "source_gate_reason", "confidence", "confidence_reason", "corroboration"):
                self.assertIn(key, rel_block, c["component_id"])
            for sid in rel_block["corroboration"]["source_ids"]:
                self.assertIn(sid, sources, c["component_id"])
            for field in ("capex_per_unit", "lifetime_years"):
                for sid in (c.get(field) or {}).get("source_ids", []):
                    self.assertIn(sid, sources, c["component_id"])
            self.assertTrue(c["trade_offs"], c["component_id"])

    def test_core_categories_have_options_in_both_regions(self):
        for region in ("netherlands", "india"):
            cats = {c["category"] for c in self.components["components"] if c["region"] in (region, "any")}
            for cat in ("fish_tank", "grow_unit", "water_pump", "aeration", "solids_filter", "structure"):
                self.assertIn(cat, cats, f"{region} lacks {cat}")

    def test_species_point_at_canon(self):
        for entry in self.species["fish"] + self.species["plants"]:
            self.assertTrue((PROJECT_ROOT / entry["canon_ref"]).is_file(), entry["canon_ref"])
            for key, spec in entry["sizing"].items():
                # Per-architecture ratios carry their reliability block on each value.
                specs = [v for v in spec["values"].values() if v] if "values" in spec else [spec]
                for one in specs:
                    self.assertIn("confidence", one, f"{entry['species_key']}.{key}")
                    self.assertIn("corroboration", one, f"{entry['species_key']}.{key}")

    def test_example_runs_build(self):
        for name in ("configure_basil_dwc_nl", "configure_basil_dwc_karnataka"):
            spec = json.loads((PROJECT_ROOT / "runs" / f"{name}.json").read_text(encoding="utf-8"))
            res = cs.build_result(spec["configurator"]["build"], run_simulation=False)
            mid = res["cases"]["mid"]
            self.assertIsNotNone(mid["cost_per_kg_plant"], name)
            self.assertGreater(mid["sizing"]["plant_kg_yr"], 0)


class RunFileTests(unittest.TestCase):
    def test_run_py_configurator_block(self):
        spec = importlib.util.spec_from_file_location("run_local_cfg", PROJECT_ROOT / "run.py")
        run_local = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(run_local)
        run_spec = json.loads((PROJECT_ROOT / "runs" / "configure_basil_dwc_nl.json").read_text(encoding="utf-8"))
        block = run_spec["configurator"]
        block["build_overrides"] = {"simulation_check": None, "target.grow_area_m2": 50}
        with tempfile.TemporaryDirectory() as tmp:
            result, lines = run_local.run_configurator(block, Path(tmp))
            self.assertTrue((Path(tmp) / "configurator_result.json").is_file())
            self.assertTrue((Path(tmp) / "configurator_cost_breakdown.csv").is_file())
        self.assertEqual(result["cases"]["mid"]["sizing"]["grow_area_m2"], 50.0)
        self.assertTrue(any("Cost per kg of plant output" in l for l in lines))


if __name__ == "__main__":
    unittest.main()
