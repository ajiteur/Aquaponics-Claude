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
GRAVEL_VARIANT = "media_bed_gravel_ebb_flow"
GRAVEL_LOADING_PRIMARY = 3.6  # SRAC 453 trickling-filter design criterion, kg feed/m3/day
OPEN_CANOPY_B = 0.394  # Ciriello 2021 exponent, open-canopy sensitivity


def hold_published_ph(scenario: dict) -> None:
    """Keep pH at the published trial mean for the whole run.

    The daily model's pH drift (0.01 per mg/L TAN nitrified) has no alkalinity buffer,
    so a system the paper reports at a steady mean pH would otherwise drift down and
    change the plant score part-way through the run (UQ-018).
    """
    scenario["nitrogen_model"]["pH_drift_per_mg_l_tan_removed"] = 0.0


# pH-free runs (UQ-018): the carbonate alkalinity buffer with pH not held. Start and
# source-water alkalinity are not reported by Knaus or Savidov, so each run is an
# assumption band, reported but not scored.
PH_FREE_ALKALINITY_BAND = {
    "soft_50": 50.0,     # near the Dutch legal minimum (60 mg/L HCO3- = 49 as CaCO3)
    "tap_140": 140.0,    # Dutch tap water, Waternet/Dunea 131 to 156 as CaCO3
    "hard_250": 250.0,   # South Indian borewell range 150 to 400+
}
PH_FREE_RETURNS = {
    "nitrification_only": {},
    "all_returns_upper": {"nh3_excretion_credit_g_CaCO3_per_g_N": 3.57,
                          "denitrified_share_of_residual_n_loss": 1.0,
                          "plant_uptake_return_eq_per_mol_N": 1.0},
}
UVI_RAINWATER_EXCHANGE = 0.024  # ISTA6: 2.61 m3/day of rainwater on 111.2 m3
UVI_RAINWATER_ALKALINITY = 0.0  # rainwater; assumption (no cited value)
UVI_BASE_G_PER_KG_FEED = {"min": 11.2, "max": 12.5}  # derived from Rakocy et al. ISTA6 doses


def free_ph(scenario: dict, start_alk: float, source_alk: float, returns: dict | None = None,
            exchange: float | None = None, target_ph: float | None = None) -> None:
    """Turn on the carbonate alkalinity buffer and let pH move (no hold)."""
    scenario["water_chemistry"] = {
        "model": "carbonate_alkalinity_buffer",
        "source_water_alkalinity_mg_L_as_CaCO3": source_alk,
        "water_exchange_fraction_per_day": exchange,
        **(returns or {}),
    }
    scenario["water_state"]["alkalinity_mg_L_as_CaCO3"] = start_alk
    scenario["water_state"].pop("dissolved_co2_mg_L", None)
    policy = scenario["operations_policy"]
    policy["pH_control_enabled"] = target_ph is not None
    policy["base_dosing_enabled"] = target_ph is not None
    if target_ph is not None:
        scenario["water_chemistry"]["target_pH"] = target_ph


def ph_trace(daily: list[dict]) -> dict:
    ph = [d["pH"] for d in daily]
    return {"start": ph[0], "day_25": ph[min(24, len(ph) - 1)], "end": ph[-1], "mean": round(sum(ph) / len(ph), 3)}


def ph_free_block(s: dict, days: int, per_plant, observed: float | None, observed_label: str) -> dict:
    """Run the scenario with pH free across the alkalinity and return-term bands."""
    runs = {}
    for alk_label, alk in PH_FREE_ALKALINITY_BAND.items():
        for ret_label, ret in PH_FREE_RETURNS.items():
            t = copy.deepcopy(s)
            free_ph(t, alk, alk, ret)
            r = run_scenario(t, days)
            value = per_plant(r)
            runs[f"{alk_label}__{ret_label}"] = {
                "pH": ph_trace(r["daily"]),
                "alkalinity_end_mg_L_as_CaCO3": r["final_state"]["water_state"]["alkalinity_mg_L_as_CaCO3"],
                observed_label: round(value, 3),
                "error_vs_observed": None if not observed else round(value / observed - 1, 3),
            }
    return {
        "status": "reported, not scored",
        "reason": "start and source-water alkalinity and the return terms are not reported, so each run is an assumption band (UQ-018)",
        "assumptions": [
            "Start alkalinity equals source-water alkalinity; dissolved CO2 held at the level implied by the published pH and that alkalinity.",
            "No base dosing (none reported).",
            "Exchange as in the scored run (nitrate_sinks: 1.5 percent a day).",
            "nitrification_only: 7.05 g CaCO3 per g N nitrified, no returns. all_returns_upper: plus NH3 excretion credit 3.57, all residual N loss denitrified, 1 eq per mol NO3-N taken up (upper bounds).",
        ],
        "runs": runs,
    }


def uvi_base_check(base: dict) -> dict:
    """Base the buffer model needs to hold UVI's pH, against UVI's recorded base use."""
    days = 28
    out = {}
    for ret_label, ret in PH_FREE_RETURNS.items():
        for alk in (88.6, 113.2):
            t = copy.deepcopy(base)
            t["scenario_id"] = f"validation_uvi_base_use_{ret_label}_{int(alk)}"
            t["water_state"]["pH"] = 7.25
            free_ph(t, alk, UVI_RAINWATER_ALKALINITY, ret, exchange=UVI_RAINWATER_EXCHANGE, target_ph=7.25)
            r = run_scenario(t, days)
            dosed = sum(sum((d.get("base_dose_g_total") or {}).values()) for d in r["daily"])
            feed = sum(d["daily_feed_kg"] or 0.0 for d in r["daily"])
            out[f"{ret_label}__start_alk_{alk}"] = {
                "base_g_per_kg_feed": round(dosed / feed, 1) if feed else None,
                "pH_end": r["daily"][-1]["pH"],
                "alkalinity_end_mg_L_as_CaCO3": r["final_state"]["water_state"]["alkalinity_mg_L_as_CaCO3"],
            }
    return {
        "check": "base needed to hold pH 7.25 (UVI range 7.0 to 7.5) with 2.4 percent a day rainwater exchange",
        "status": "reported, not scored",
        "observed_base_g_per_kg_feed": UVI_BASE_G_PER_KG_FEED,
        "observed_basis": "40.65 kg Ca(OH)2 + 38.85 kg KOH a year (projected), Rakocy et al. ISTA6; per kg feed is our arithmetic",
        "assumptions": [
            "Rainwater make-up alkalinity 0 mg/L (no cited value).",
            "Base mix 50/50 KOH and Ca(OH)2 by alkalinity; 28-day run of the UVI feed-ratio basil scenario.",
            "The whole 2.4 percent a day counts as exchange; part of UVI's make-up only replaces evapotranspiration, so this overstates the dilution loss.",
        ],
        "runs": out,
    }


def metric(name: str, model: float, observed: float, note: str | None = None) -> dict:
    error = model / observed - 1.0 if observed else None
    return {
        "metric": name,
        "model": round(model, 3),
        "observed": observed,
        "error_fraction": None if error is None else round(error, 3),
        "within_25_percent": None if error is None else abs(error) <= FAIL_THRESHOLD,
        "scored": True,
        "note": note,
    }


def unscored(m: dict, reason: str) -> dict:
    """Keep a metric in the report but out of the pass/fail count, with the reason."""
    m["scored"] = False
    m["excluded_reason"] = reason
    return m


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
        "scored": True,
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
    bed = i["grow_bed"]
    vol = bed["gravel_volume_m3_total_derived"]
    mid_volume = round((vol["min"] + vol["max"]) / 2, 3)

    def gravel_surfaces(volume_m3: float, loading: float | None) -> dict:
        return {
            "raft_grow_area_m2": 0.0,
            "dedicated_biofilter": None,
            "media_beds": [{"variant_id": GRAVEL_VARIANT, "media_volume_m3": volume_m3, "feed_loading_kg_per_m3_day": loading}],
            "basis": "gravel ebb-and-flow beds as media volume x feed loading (candidate variant media_bed_gravel_ebb_flow)",
        }

    s["system"].update({
        "water_volume_l": float(i["water_volume_l"]),
        "fish_tank_volume_l": float(i["fish_tank_volume_l"]),
        "nitrification_surfaces": gravel_surfaces(mid_volume, GRAVEL_LOADING_PRIMARY),
    })
    s["water_state"].update({
        "pH": i["pH"], "water_temperature_c": i["water_temperature_c"], "air_temperature_c": i["water_temperature_c"],
        "dissolved_oxygen_mg_L": i["do_mg_L"], "tan_mg_L": o["tan_mg_L_mean"], "nitrate_mg_L": o["no3_n_mg_L_mean"],
    })
    hold_published_ph(s)
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

    s["light"] = {"dli_mol_m2_day": i["dli_mol_m2_day_derived"]["mid"], "basis": i["dli_basis"]}

    def knaus_basil(r: dict) -> float:
        g = sum(e["harvested_mass_kg"] for e in r["harvest_events"]) * 1000 / i["plant_count_derived"]
        return g + r["final_state"]["plant_crop"].get("harvestable_cut_mass_g_per_plant", 0.0)

    ph_free = ph_free_block(s, i["days"], knaus_basil, o["basil_fresh_g_per_plant"], "basil_fresh_g_per_plant_dli_mid")

    # Nitrogen sensitivity: gravel volume and loading at the ends of their ranges, plus
    # the old raft-equivalent treatment, for comparison only.
    tan_sensitivity = {}
    for label, surfaces in {
        "low_capacity_fao_1_0_kg_m3_min_volume": gravel_surfaces(vol["min"], 1.0),
        "high_capacity_srac_3_6_kg_m3_max_volume": gravel_surfaces(vol["max"], 3.6),
        "old_raft_equivalent_10_m2": {"raft_grow_area_m2": i["plant_area_m2_derived"], "dedicated_biofilter": None,
                                      "basis": "previous assumption: gravel bed area as raft-equivalent surface"},
    }.items():
        t = copy.deepcopy(s)
        t["system"]["nitrification_surfaces"] = surfaces
        daily = run_scenario(t, i["days"])["daily"]
        tan_sensitivity[label] = {
            "tan_mg_L_mean": round(sum(d["tan_mg_L"] for d in daily) / len(daily), 3),
            "no3_n_mg_L_mean": round(sum(d["nitrate_mg_L"] for d in daily) / len(daily), 2),
        }

    basil_metrics = []
    for label, g in basil_by_dli.items():
        m = metric(f"basil_fresh_g_per_plant_dli_{label}", g, o["basil_fresh_g_per_plant"],
                   f"DLI {i['dli_mol_m2_day_derived'][label]} mol/m2/d; density "
                   f"{round(i['plant_count_derived'] / i['plant_area_m2_derived'], 1)} plants/m2; published SD {o['basil_fresh_g_per_plant_sd']} g")
        if label != "mid":
            unscored(m, "DLI bound (sensitivity band); the scored basil case is the midpoint DLI")
        basil_metrics.append(m)

    fish = run["final_state"]["fish_batch"]
    gain = fish["total_biomass_kg"] - i["fish_start_biomass_kg"]
    model_fcr = i["feed_kg_per_day"] * i["days"] / gain if gain > 0 else None
    nitrate = [d["nitrate_mg_L"] for d in run["daily"]]
    tan = [d["tan_mg_L"] for d in run["daily"]]
    return {
        "system_id": rec["system_id"],
        "assumptions": [
            f"Gravel beds counted as media volume ({mid_volume} m3, from 2,000 kg at a sand bulk-density proxy of 1,400 to 1,600 kg/m3) at the trickling-filter loading of {GRAVEL_LOADING_PRIMARY} kg feed/m3/day (SRAC 453); FAO 589 low end and the old raft-equivalent treatment are in the sensitivity block.",
            "Nitrate sinks use the UVI-calibrated residual loss and 1.5 percent daily exchange (Knaus exchange not reported).",
            "Start TAN and nitrate set to the published means (start values not reported).",
            "pH held at the published mean of 8.0 for all 70 days (the model's pH drift has no alkalinity buffer; without the hold pH fell to about 7.5 by day 25 and the basil score doubled).",
            "Basil is scored at the midpoint of the two DLI bounds (photoperiod not reported); the bounds are a sensitivity band, not scored.",
            "All 180 plant positions are treated as basil for N uptake and yield (the beds were mixed herbs); density 18 plants/m2 counts all herbs.",
            "Fish, TAN and nitrate metrics come from the high-DLI run (light does not change them except through plant N uptake).",
            "Basil per-plant density factor uses the closed-canopy rule (b = 0 above 8 plants/m2).",
        ],
        "ph_free": ph_free,
        "sensitivity": {
            "tan_and_nitrate_by_gravel_capacity": tan_sensitivity,
            "basil_dli_band_g_per_plant": {
                "low": round(basil_by_dli["low"], 2), "high": round(basil_by_dli["high"], 2),
                "observed_inside_band": basil_by_dli["low"] <= o["basil_fresh_g_per_plant"] <= basil_by_dli["high"],
            },
        },
        "metrics": [
            metric("fish_end_biomass_kg", fish["total_biomass_kg"], o["fish_end_biomass_kg"]),
            metric("fcr", model_fcr, o["fcr"], "model FCR is the sourced 1.7 divided by the temperature factor"),
            metric("tan_mg_L_mean", sum(tan) / len(tan), o["tan_mg_L_mean"]),
            metric("no3_n_mg_L_mean", sum(nitrate) / len(nitrate), o["no3_n_mg_L_mean"],
                   f"published SD {o['no3_n_mg_L_sd']}; model end value {round(nitrate[-1], 2)}"),
            *basil_metrics,
        ],
    }


def savidov_case(rec: dict, base: dict) -> dict:
    i, o = rec["inputs"], rec["observed"]
    s = copy.deepcopy(base)
    s["scenario_id"] = "validation_savidov_2005_basil"
    s["water_state"].update({"pH": i["pH"], "water_temperature_c": i["water_temperature_c"], "air_temperature_c": i["water_temperature_c"]})
    hold_published_ph(s)
    anchor = run_scenario(s, i["basil_cycle_days_derived"])["harvest_events"][0]
    per_m2_year_anchor_density = anchor["harvested_mass_kg_per_m2"] * 365 / i["basil_cycle_days_derived"]
    s["plant_crop"]["planting_density_plants_m2"] = i["basil_density_plants_m2_derived"]
    event = run_scenario(s, i["basil_cycle_days_derived"])["harvest_events"][0]
    per_m2_year = event["harvested_mass_kg_per_m2"] * 365 / i["basil_cycle_days_derived"]
    s["plant_crop"]["yield_response_overrides"] = {"density_exponent_b": OPEN_CANOPY_B}
    event_open = run_scenario(s, i["basil_cycle_days_derived"])["harvest_events"][0]
    per_m2_year_open = event_open["harvested_mass_kg_per_m2"] * 365 / i["basil_cycle_days_derived"]
    s["plant_crop"].pop("yield_response_overrides")

    s["plant_crop"]["planting_density_plants_m2"] = i["basil_density_plants_m2_derived"]
    cycle_days = i["basil_cycle_days_derived"]
    ph_free = ph_free_block(
        s, cycle_days, lambda r: r["harvest_events"][0]["harvested_mass_kg_per_m2"] * 365 / cycle_days,
        o["basil_kg_m2_trough_area_per_year_derived"], "basil_kg_m2_trough_per_year")
    ph_free["assumptions"].append("Savidov held pH 6.1 to 6.3 with base and acid dosing, so a free run shows the drift that dosing removed, not the published system.")

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
            "Basil at Savidov's derived density of 31.8 plants/m2 through the candidate closed-canopy density rule (b = 0 above 8 plants/m2); the open-canopy exponent is in the sensitivity block.",
            "DLI not set: 16 h photoperiod with supplemental light of at least 300 umol/m2/s gives at least 17 mol/m2/d (derived), above the light plateau.",
            "Fish fed Savidov's schedule (2.5 percent at 100 g falling to 1.25 percent at 400 g), linear between.",
            "pH held at the published 6.2 (the model's pH drift has no alkalinity buffer).",
            "Fish harvest weight is scored against the report's own per-fish range (0.50 to 0.64 kg); the 630 g point assumes no mortality and is kept in the note.",
        ],
        "metrics": [
            metric("basil_kg_m2_trough_per_year_at_savidov_density", per_m2_year, o["basil_kg_m2_trough_area_per_year_derived"],
                   "candidate closed-canopy density rule (b = 0)"),
            metric("basil_kg_m2_trough_per_year_at_uvi_density", per_m2_year_anchor_density,
                   o["basil_kg_m2_trough_area_per_year_derived"], "reference: model run at the UVI anchor density (8 plants/m2)"),
            metric_range("fish_harvest_mean_g", w, o["fish_harvest_mean_g_text_range"]["min"], o["fish_harvest_mean_g_text_range"]["max"],
                         f"derived point {o['fish_harvest_mean_g_derived']} g ({o['fish_harvest_basis']}); model vs that point {w / o['fish_harvest_mean_g_derived'] - 1:+.1%}"),
        ],
        "ph_free": ph_free,
        "sensitivity": {
            "basil_kg_m2_trough_per_year_open_canopy_b_0_394": round(per_m2_year_open, 2),
            "error_fraction": round(per_m2_year_open / o["basil_kg_m2_trough_area_per_year_derived"] - 1, 3),
        },
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
        "assumptions": [
            "Feed not reported: SRAC 282 table, mid and high rows.",
            "FCR is reported but not scored: the published 0.92 to 1.20 is below the Tier 1 range of 1.4 to 1.8, feed intake is not printed so it cannot be checked, and Eq. 5 mixes per-fish gain with the final fish count (UQ-017).",
        ],
        "sensitivity": {
            "fcr_if_temperature_lowers_intake_not_conversion": model["feed_conversion_ratio"]["simulation_default"],
            "error_fraction_vs_published_max": round(model["feed_conversion_ratio"]["simulation_default"] / o["fcr"]["max"] - 1, 3),
            "note": "Even with no temperature penalty on conversion, the sourced FCR of 1.7 is 42 percent above the published maximum.",
        },
        "metrics": [
            metric_range("fish_gain_g_per_day_mid_table_feed", out["mid"], o["fish_gain_g_per_day"]["min"], o["fish_gain_g_per_day"]["max"]),
            metric_range("fish_gain_g_per_day_high_table_feed", out["high"], o["fish_gain_g_per_day"]["min"], o["fish_gain_g_per_day"]["max"]),
            unscored(metric_range("fcr", model["feed_conversion_ratio"]["simulation_default"] / fish_growth.temperature_factor(i["water_temperature_c"], model),
                                  o["fcr"]["min"], o["fcr"]["max"], "model FCR at 23.5 C = 1.7 / temperature factor"),
                     "published FCR below the Tier 1 range and not checkable (feed intake not printed); see UQ-017"),
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
        for c in cases for m in c["metrics"] if m["scored"] and m["within_25_percent"] is False
    ]
    excluded = [
        f"{c['system_id']}: {m['metric']} ({m['error_fraction']:+.0%}): {m['excluded_reason']}"
        for c in cases for m in c["metrics"] if not m["scored"]
    ]
    scored = [m for c in cases for m in c["metrics"] if m["scored"]]
    return {
        "estimate_status": "scenario_estimate",
        "label": "scenario estimate, not validated",
        "fail_threshold_abs_error_fraction": FAIL_THRESHOLD,
        "cases": cases,
        "scored_metric_count": len(scored),
        "failures": failures,
        "excluded_from_score": excluded,
        "ph_buffer_checks": {"uvi_base_use": uvi_base_check(base)},
        "ph_note": "Scored runs hold pH at the published mean (approved Batch 005, B1). pH-free runs with the candidate carbonate alkalinity buffer are in each case's ph_free block and in ph_buffer_checks; they are reported, not scored.",
    }


def main() -> None:
    results = build()
    RESULTS_PATH.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    for case in results["cases"]:
        print(case["system_id"])
        for m in case["metrics"]:
            print(f"  {m['metric']}: model {m['model']} vs {m['observed']} -> {m['error_fraction']}")
    print(f"Failures ({len(results['failures'])} of {results['scored_metric_count']} scored):", *results["failures"], sep="\n  ")
    print("Reported, not scored:", *results["excluded_from_score"], sep="\n  ")
    for case in results["cases"]:
        for label, run in case.get("ph_free", {}).get("runs", {}).items():
            print(f"  pH free {case['system_id']} {label}: {run}")
    for label, run in results["ph_buffer_checks"]["uvi_base_use"]["runs"].items():
        print(f"  UVI base use {label}: {run}")


if __name__ == "__main__":
    main()
