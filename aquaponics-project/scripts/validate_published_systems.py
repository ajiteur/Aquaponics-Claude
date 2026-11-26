"""Validate the daily simulation against published aquaponics systems beyond UVI.

Observations: data/knowledge/validation/published_system_observations.json.
Writes data/simulation/results/published_system_validation.json.

Each case builds a scenario from the UVI crop-cycle scenario plus the published
inputs, runs it, and reports model vs observed with the error for each metric.
Inputs a paper does not report are filled with a labelled assumption. All results
are scenario estimates, not validated.

Usage: python scripts/validate_published_systems.py
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import fish_growth  # noqa: E402
from simulate_crop_cycle import run_cycle  # noqa: E402

OBS_PATH = PROJECT_ROOT / "data" / "knowledge" / "validation" / "published_system_observations.json"
BASE_SCENARIO = PROJECT_ROOT / "data" / "simulation" / "scenarios" / "basil_raft_crop_cycle_uvi_feed_ratio.json"
RESULTS_PATH = PROJECT_ROOT / "data" / "simulation" / "results" / "published_system_validation.json"
FAIL_THRESHOLD = 0.25


def metric(name: str, model: float, observed: float, note: str | None = None) -> dict:
    error = model / observed - 1.0 if observed else None
    return {
        "metric": name,
        "model": round(model, 3),
        "observed": observed,
        "error_fraction": None if error is None else round(error, 3),
        "within_25_percent": None if error is None else abs(error) <= FAIL_THRESHOLD,
        "note": note,
    }


def metric_range(name: str, model: float, low: float, high: float, note: str | None = None) -> dict:
    if model < low:
        error = model / low - 1.0
    elif model > high:
        error = model / high - 1.0
    else:
        error = 0.0
    return {
        "metric": name,
        "model": round(model, 3),
        "observed": {"min": low, "max": high},
        "error_fraction": round(error, 3),
        "error_basis": "distance to the nearest end of the published range",
        "within_25_percent": abs(error) <= FAIL_THRESHOLD,
        "note": note,
    }


def run_scenario(scenario: dict, days: int) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / f"{scenario['scenario_id']}.json"
        path.write_text(json.dumps(scenario, indent=2), encoding="utf-8")
        return run_cycle(path, days)


def knaus_case(rec: dict, base: dict) -> dict:
    i, o = rec["inputs"], rec["observed"]
    s = copy.deepcopy(base)
    s["scenario_id"] = "validation_knaus_2018_tilapia"
    s["system"].update({
        "water_volume_l": float(i["water_volume_l"]),
        "fish_tank_volume_l": float(i["fish_tank_volume_l"]),
        "nitrification_surfaces": {
            "raft_grow_area_m2": i["plant_area_m2_derived"],
            "dedicated_biofilter": None,
            "basis": "assumption: gravel bed area treated as raft-equivalent nitrifying surface",
        },
    })
    s["water_state"].update({
        "pH": i["pH"], "water_temperature_c": i["water_temperature_c"], "air_temperature_c": i["water_temperature_c"],
        "dissolved_oxygen_mg_L": i["do_mg_L"], "tan_mg_L": o["tan_mg_L_mean"], "nitrate_mg_L": o["no3_n_mg_L_mean"],
    })
    s["fish_batch"].update({
        "count": i["fish_count"], "total_biomass_kg": i["fish_start_biomass_kg"],
        "average_weight_g": round(i["fish_start_biomass_kg"] * 1000 / i["fish_count"], 2),
    })
    s["plant_crop"]["plant_count"] = i["plant_count_derived"]
    s["plant_crop"]["planting_density_plants_m2"] = i["plant_count_derived"] / i["plant_area_m2_derived"]
    s["feeding"].update({"fixed_feed_kg_per_day": i["feed_kg_per_day"], "feed_protein_fraction": i["feed_protein_fraction"]})
    basil_by_dli = {}
    for label, dli in i["dli_mol_m2_day_derived"].items():
        s["light"] = {"dli_mol_m2_day": dli, "basis": i["dli_basis"]}
        r = run_scenario(s, i["days"])
        g = sum(e["harvested_mass_kg"] for e in r["harvest_events"]) * 1000 / i["plant_count_derived"]
        basil_by_dli[label] = g + r["final_state"]["plant_crop"].get("harvestable_cut_mass_g_per_plant", 0.0)
        run = r

    fish = run["final_state"]["fish_batch"]
    gain = fish["total_biomass_kg"] - i["fish_start_biomass_kg"]
    model_fcr = i["feed_kg_per_day"] * i["days"] / gain if gain > 0 else None
    nitrate = [d["nitrate_mg_L"] for d in run["daily"]]
    tan = [d["tan_mg_L"] for d in run["daily"]]
    return {
        "system_id": rec["system_id"],
        "assumptions": [
            "Gravel bed area counted as raft-equivalent nitrifying surface.",
            "Nitrate sinks use the UVI-calibrated residual loss and 1.5 percent daily exchange (Knaus exchange not reported).",
            "Start TAN and nitrate set to the published means (start values not reported).",
            "All 180 plant positions are treated as basil for N uptake and yield (the beds were mixed herbs); density 18 plants/m2 counts all herbs.",
            "Fish, TAN and nitrate metrics come from the low-DLI run (light does not change them except through plant N uptake).",
        ],
        "metrics": [
            metric("fish_end_biomass_kg", fish["total_biomass_kg"], o["fish_end_biomass_kg"]),
            metric("fcr", model_fcr, o["fcr"], "model FCR is the sourced 1.7 divided by the temperature factor"),
            metric("tan_mg_L_mean", sum(tan) / len(tan), o["tan_mg_L_mean"]),
            metric("no3_n_mg_L_mean", sum(nitrate) / len(nitrate), o["no3_n_mg_L_mean"],
                   f"published SD {o['no3_n_mg_L_sd']}; model end value {round(nitrate[-1], 2)}"),
            *[
                metric(f"basil_fresh_g_per_plant_dli_{label}", g, o["basil_fresh_g_per_plant"],
                       f"DLI {i['dli_mol_m2_day_derived'][label]} mol/m2/d ({i['dli_basis']}); density {round(i['plant_count_derived'] / i['plant_area_m2_derived'], 1)} plants/m2")
                for label, g in basil_by_dli.items()
            ],
        ],
    }


def savidov_case(rec: dict, base: dict) -> dict:
    i, o = rec["inputs"], rec["observed"]
    s = copy.deepcopy(base)
    s["scenario_id"] = "validation_savidov_2005_basil"
    s["water_state"].update({"pH": i["pH"], "water_temperature_c": i["water_temperature_c"], "air_temperature_c": i["water_temperature_c"]})
    anchor = run_scenario(s, i["basil_cycle_days_derived"])["harvest_events"][0]
    per_m2_year_anchor_density = anchor["harvested_mass_kg_per_m2"] * 365 / i["basil_cycle_days_derived"]
    s["plant_crop"]["planting_density_plants_m2"] = i["basil_density_plants_m2_derived"]
    event = run_scenario(s, i["basil_cycle_days_derived"])["harvest_events"][0]
    per_m2_year = event["harvested_mass_kg_per_m2"] * 365 / i["basil_cycle_days_derived"]

    feed = i["feed_pct_bw"]

    def savidov_rate(w: float, model: dict, pick: str = "mid") -> float:
        if w <= 100:
            return feed["at_100_g"]
        if w >= 400:
            return feed["at_400_g"]
        return feed["at_100_g"] + (feed["at_400_g"] - feed["at_100_g"]) * (w - 100) / 300

    model = fish_growth.load_model()
    w = i["fish_start_mean_g"]
    for _ in range(i["fish_days"]):
        w += fish_growth.daily_gain_kg(w * savidov_rate(w, model) / 100.0, i["water_temperature_c"], model)
    return {
        "system_id": rec["system_id"],
        "assumptions": [
            "Feed per m2 not reported: the UVI feed ratio scenario supplies nitrogen, so nitrate is not limiting.",
            "Basil at Savidov's derived density of 31.8 plants/m2 through the candidate density response.",
            "DLI not set: 16 h photoperiod with supplemental light of at least 300 umol/m2/s gives at least 17 mol/m2/d (derived), above the light plateau.",
            "Fish fed Savidov's schedule (2.5 percent at 100 g falling to 1.25 percent at 400 g), linear between.",
        ],
        "metrics": [
            metric("basil_kg_m2_trough_per_year_at_savidov_density", per_m2_year, o["basil_kg_m2_trough_area_per_year_derived"],
                   "candidate density response (Ciriello 2021 exponent)"),
            metric("basil_kg_m2_trough_per_year_at_uvi_density", per_m2_year_anchor_density,
                   o["basil_kg_m2_trough_area_per_year_derived"], "reference: model run at the UVI anchor density (8 plants/m2)"),
            metric("fish_harvest_mean_g", w, o["fish_harvest_mean_g_derived"], o["fish_harvest_basis"]),
        ],
    }


def khater_case(rec: dict) -> dict:
    i, o = rec["inputs"], rec["observed"]
    model = fish_growth.load_model()
    out = {}
    for pick in ("mid", "high"):
        end = fish_growth.grow_out(i["fish_start_mean_g"], i["days"], model, lambda d: i["water_temperature_c"], pick)
        out[pick] = (end - i["fish_start_mean_g"]) / i["days"]
    return {
        "system_id": rec["system_id"],
        "assumptions": ["Feed not reported: SRAC 282 table, mid and high rows."],
        "metrics": [
            metric_range("fish_gain_g_per_day_mid_table_feed", out["mid"], o["fish_gain_g_per_day"]["min"], o["fish_gain_g_per_day"]["max"]),
            metric_range("fish_gain_g_per_day_high_table_feed", out["high"], o["fish_gain_g_per_day"]["min"], o["fish_gain_g_per_day"]["max"]),
            metric_range("fcr", model["feed_conversion_ratio"]["simulation_default"] / fish_growth.temperature_factor(i["water_temperature_c"], model),
                         o["fcr"]["min"], o["fcr"]["max"], "model FCR at 23.5 C = 1.7 / temperature factor"),
        ],
    }


def build() -> dict:
    obs = {r["system_id"]: r for r in json.loads(OBS_PATH.read_text(encoding="utf-8"))["records"]}
    base = json.loads(BASE_SCENARIO.read_text(encoding="utf-8"))
    cases = [
        knaus_case(obs["knaus_2018_rostock_tilapia"], base),
        savidov_case(obs["savidov_2005_alberta_basil"], base),
        khater_case(obs["khater_2023_benha_tilapia_lettuce"]),
    ]
    failures = [
        f"{c['system_id']}: {m['metric']} ({m['error_fraction']:+.0%})"
        for c in cases for m in c["metrics"] if m["within_25_percent"] is False
    ]
    return {
        "estimate_status": "scenario_estimate",
        "label": "scenario estimate, not validated",
        "fail_threshold_abs_error_fraction": FAIL_THRESHOLD,
        "cases": cases,
        "failures": failures,
    }


def main() -> None:
    results = build()
    RESULTS_PATH.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    for case in results["cases"]:
        print(case["system_id"])
        for m in case["metrics"]:
            print(f"  {m['metric']}: model {m['model']} vs {m['observed']} -> {m['error_fraction']}")
    print("Failures:", *results["failures"], sep="\n  ")


if __name__ == "__main__":
    main()
