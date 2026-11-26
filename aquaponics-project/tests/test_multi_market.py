"""Multi-market tests: every price is tied to a market, and a new country is data only.

The stub market 'testland' below copies Dutch catalog rows under a test currency (XTS, the
ISO 4217 code reserved for testing). Its numbers are test-only, not evidence.
"""

import copy
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


audit = load("audit_market_tags_t", "scripts/audit_market_tags.py")
sw = load("compare_swaps_mm", "scripts/compare_swaps.py")
cs = sw.cs


def add_stub_market(tmp: Path):
    """Write copies of the real catalog files with a third market added as data only."""
    components = json.loads(cs.DEFAULT_COMPONENTS.read_text(encoding="utf-8"))
    species = json.loads(cs.DEFAULT_SPECIES.read_text(encoding="utf-8"))
    locations = json.loads(cs.DEFAULT_LOCATIONS.read_text(encoding="utf-8"))
    new_components = []
    for c in components["components"]:
        if c["region"] != "netherlands":
            continue
        t = copy.deepcopy(c)
        t["component_id"] = c["component_id"].replace("_nl", "") + "_tl"
        t["region"], t["currency_code"] = "testland", "XTS"
        if t.get("capex_per_unit") and t["capex_per_unit"].get("market"):
            t["capex_per_unit"]["market"].update(region="testland", currency_code="XTS")
        new_components.append(t)
    components["components"] += new_components
    for r in list(components["running_inputs"]):
        if r["region"] == "netherlands":
            t = copy.deepcopy(r)
            t["region"] = "testland"
            if t.get("currency_code"):
                t["currency_code"] = "XTS"
            t["market"].update(region="testland", currency_code=t.get("currency_code"))
            components["running_inputs"].append(t)
    loc = copy.deepcopy(locations["locations"]["netherlands"])
    loc["currency_code"] = "XTS"
    for key in ("wage_per_hour", "electricity_per_kwh"):
        loc[key]["price_year"] = {"low": 2026, "high": 2026}
        loc[key]["price_year_basis"] = "stated_in_source"
    locations["locations"]["testland"] = loc
    paths = []
    for name, doc in (("c.json", components), ("s.json", species), ("l.json", locations)):
        p = tmp / name
        p.write_text(json.dumps(doc), encoding="utf-8")
        paths.append(p)
    return paths


def stub_build():
    base = json.loads((PROJECT_ROOT / "runs" / "configure_basil_dwc_nl.json").read_text(encoding="utf-8"))["configurator"]["build"]
    build = copy.deepcopy(base)
    build.update(build_id="stub", region="testland", location="testland")
    build.pop("simulation_check", None)
    comps = {}
    for cat, ids in build["components"].items():
        if cat.startswith("_") or not ids:
            comps[cat] = ids
            continue
        conv = lambda i: i.replace("_nl", "") + "_tl"
        comps[cat] = [conv(i) for i in ids] if isinstance(ids, list) else conv(ids)
    build["components"] = comps
    return build


class MarketTagTests(unittest.TestCase):
    def test_every_price_has_a_consistent_market_tag(self):
        result = audit.audit()
        bad = [f for f in result["flags"] if "no market tag" in f or "differs from" in f or "no currency_code" in f]
        self.assertEqual(bad, [])
        catalog = json.loads(cs.DEFAULT_COMPONENTS.read_text(encoding="utf-8"))
        for c in catalog["components"]:
            if c.get("capex_per_unit"):
                m = c["capex_per_unit"]["market"]
                self.assertEqual(m["region"], c["region"], c["component_id"])
        for r in catalog["running_inputs"]:
            self.assertIn("market", r, r["input_id"])
            unit_cur = r["unit"][:3] if r["unit"][:3] in ("EUR", "INR") else None
            self.assertEqual(r.get("currency_code"), unit_cur, r["input_id"])

    def test_untagged_years_are_flagged_in_results(self):
        spec = json.loads((PROJECT_ROOT / "runs" / "configure_basil_dwc_karnataka.json").read_text(encoding="utf-8"))
        res = cs.build_result(spec["configurator"]["build"], run_simulation=False)
        self.assertTrue(any("electricity_per_kwh" in f and "one end" in f for f in res["market"]["flags"]))
        self.assertEqual(res["market"]["currency_code"], "INR")

    def test_currency_mismatch_is_an_error(self):
        spec = json.loads((PROJECT_ROOT / "runs" / "configure_basil_dwc_nl.json").read_text(encoding="utf-8"))
        build = spec["configurator"]["build"]
        build["location"] = "karnataka"  # INR location with EUR parts
        with self.assertRaises(cs.ConfigError):
            cs.build_result(build, run_simulation=False)


class NewCountryIsDataOnlyTests(unittest.TestCase):
    """Adding a market touches only data files: rows with a new region and currency, and a location."""

    def test_stub_market_builds_and_swaps(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = add_stub_market(Path(tmp))
            res = cs.build_result(stub_build(), *paths, run_simulation=False)
            self.assertEqual(res["currency_code"], "XTS")
            mid = res["cases"]["mid"]
            self.assertIsNotNone(mid["cost_per_kg_plant"])
            self.assertTrue(all(t["currency_code"] == "XTS" for t in res["market"]["tags"]))
            self.assertFalse(any("wage_per_hour" in f for f in res["market"]["flags"]))
            swaps = sw.compare_swaps({"base": stub_build(), "options": [
                {"swap_id": "heat_pump", "kind": "heating",
                 "patch": {"heating": {"enabled": True, "source": "heat_pump"},
                           "components": {"heating": "heating_heat_pump_air_water_tl"}}}]}, *paths)
            self.assertTrue(all(r["status"] == "ran" for r in swaps["swaps"]))
            self.assertEqual(swaps["currency_code"], "XTS")
            # Same numbers as the Dutch rows it copies, so the code treats markets alike.
            nl = json.loads((PROJECT_ROOT / "runs" / "configure_basil_dwc_nl.json").read_text(encoding="utf-8"))["configurator"]["build"]
            nl.pop("simulation_check", None)
            nl_res = cs.build_result(nl, *paths, run_simulation=False)
            self.assertEqual(mid["cost_per_kg_plant"], nl_res["cases"]["mid"]["cost_per_kg_plant"])

    def test_parts_from_another_market_are_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = add_stub_market(Path(tmp))
            build = stub_build()
            build["components"]["fish_tank"] = "fish_tank_ibc_1000l_used_nl"
            with self.assertRaises(cs.ConfigError):
                cs.build_result(build, *paths, run_simulation=False)


if __name__ == "__main__":
    unittest.main()
