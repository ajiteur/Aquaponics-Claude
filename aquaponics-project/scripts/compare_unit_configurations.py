#!/usr/bin/env python3
"""Compare candidate aquaponics unit configurations, per location.

For each configuration and location, compares revenue per output unit with
labour + electricity cost per output unit, and reports what is left per m2 per
year to pay for heating, fixed costs (CAPEX), consumables and owner income.

Output is a scenario estimate, not validated. It is not total operating cost,
profit or viability: heating, CAPEX, consumables and fish revenue are left out
and listed as gaps.

Cases:
    low  = lowest yield, price and saleability with highest labour, wage and power
    mid  = midpoint of every range
    high = highest yield, price and saleability with lowest labour, wage and power

Usage:
    python scripts/compare_unit_configurations.py
        [--inputs data/scenarios/unit_configuration_candidates_v0.json]
        [--out data/simulation/results/unit_configuration_comparison.json]
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUTS = PROJECT_ROOT / "data" / "scenarios" / "unit_configuration_candidates_v0.json"
DEFAULT_OUT = PROJECT_ROOT / "data" / "simulation" / "results" / "unit_configuration_comparison.json"
CASES = ("low", "mid", "high")
# Inputs where a higher value helps the result. Others (costs) hurt it.
FAVOURABLE_HIGH = {"yield", "price", "saleability"}


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return str(path)


def pick(rng: dict | None, case: str, favourable_high: bool) -> float | None:
    """Value of a {low, high} range for a case, taking the direction into account."""
    if rng is None or rng.get("low") is None or rng.get("high") is None:
        return None
    lo, hi = float(rng["low"]), float(rng["high"])
    if case == "mid":
        return (lo + hi) / 2
    best = case == "high"
    if favourable_high:
        return hi if best else lo
    return lo if best else hi


def resolve(spec: dict | None, location: dict, location_id: str) -> dict | None:
    """Turn a config input spec into a {low, high, ...} range for one location."""
    if spec is None:
        return None
    if "ref" in spec:
        return location.get(spec["ref"])
    if "by_location" in spec:
        return spec["by_location"].get(location_id)
    return spec


def evaluate(config: dict, location_id: str, location: dict) -> dict:
    ranges = {
        "yield": resolve(config.get("yield_units_per_m2_yr"), location, location_id),
        "price": resolve(config.get("price_per_unit"), location, location_id),
        "saleability": resolve(config.get("saleability_rate"), location, location_id),
        "wage": location.get("wage_per_hour"),
        "power_price": location.get("electricity_per_kwh"),
        "kwh_m2": config.get("electricity_kwh_per_m2_yr"),
        "labour_m2": config.get("labour_h_per_m2_yr"),
        "labour_unit": config.get("labour_h_per_unit"),
    }
    required = ["yield", "price", "saleability", "wage", "power_price", "kwh_m2"]
    missing = [k for k in required if ranges[k] is None or ranges[k].get("low") is None]
    if ranges["labour_m2"] is None and ranges["labour_unit"] is None:
        missing.append("labour")
    owner = config.get("labour_mode") == "owner_uncosted"
    fx = location.get("eur_per_currency_unit_for_comparison")
    if isinstance(fx, dict):
        fx = fx.get("value")
    result = {
        "location": location_id,
        "currency_code": location.get("currency_code"),
        "missing_inputs": missing,
        "cases": {},
    }
    if missing:
        return result

    for case in CASES:
        v = {k: pick(r, case, k in FAVOURABLE_HIGH) for k, r in ranges.items() if r is not None}
        units = v["yield"]
        if "labour_m2" in v:
            labour_h_m2 = v["labour_m2"]
        else:
            labour_h_m2 = v["labour_unit"] * units
        saleable_units = units * v["saleability"]
        revenue_m2 = saleable_units * v["price"]
        power_cost_m2 = v["kwh_m2"] * v["power_price"]
        labour_cost_m2 = 0.0 if owner else labour_h_m2 * v["wage"]
        cost_m2 = labour_cost_m2 + power_cost_m2
        headroom_m2 = revenue_m2 - cost_m2
        net_price_per_harvested = v["price"] * v["saleability"]
        power_per_harvested = power_cost_m2 / units
        # Labour hours per harvested unit at which revenue just covers labour + power.
        breakeven_labour_h_per_unit = (net_price_per_harvested - power_per_harvested) / v["wage"]
        row = {
            "inputs_used": {k: round(x, 4) for k, x in v.items()},
            "labour_h_per_m2_yr": round(labour_h_m2, 3),
            "labour_h_per_harvested_unit": round(labour_h_m2 / units, 4),
            "revenue_per_m2_yr": round(revenue_m2, 2),
            "revenue_per_saleable_unit": round(v["price"], 3),
            "labour_cost_per_m2_yr": round(labour_cost_m2, 2),
            "electricity_cost_per_m2_yr": round(power_cost_m2, 2),
            "labour_plus_electricity_cost_per_saleable_unit": round(cost_m2 / saleable_units, 3),
            "headroom_per_m2_yr": round(headroom_m2, 2),
            "headroom_per_saleable_unit": round(headroom_m2 / saleable_units, 3),
            "breakeven_labour_h_per_harvested_unit": round(breakeven_labour_h_per_unit, 4),
            "covers_labour_and_electricity": headroom_m2 > 0,
        }
        if owner:
            row["owner_hours_per_m2_yr"] = round(labour_h_m2, 3)
            row["headroom_per_owner_hour"] = round(headroom_m2 / labour_h_m2, 2) if labour_h_m2 else None
        if fx and location.get("currency_code") != "EUR":
            row["eur_comparison"] = {
                "revenue_per_m2_yr": round(revenue_m2 * fx, 2),
                "headroom_per_m2_yr": round(headroom_m2 * fx, 2),
                "note": "Converted at the research pack's ECB reference rate for comparison only.",
            }
        result["cases"][case] = row

    low, high = result["cases"]["low"]["covers_labour_and_electricity"], result["cases"]["high"]["covers_labour_and_electricity"]
    result["verdict"] = (
        "clears_in_all_cases" if low else "clears_only_in_favourable_cases" if high else "fails_in_all_cases"
    )
    return result


def build(inputs_path: Path) -> dict:
    data = json.loads(inputs_path.read_text(encoding="utf-8"))
    locations = data["locations"]
    rows = []
    for config in data["configurations"]:
        for location_id in config.get("locations", list(locations)):
            evaluated = evaluate(config, location_id, locations[location_id])
            rows.append({
                "config_id": config["config_id"],
                "label": config["label"],
                "crop": config["crop"],
                "output_unit": config["output_unit"],
                "labour_mode": config["labour_mode"],
                **evaluated,
            })
    return {
        "estimate_status": "scenario_estimate",
        "label": "Scenario estimate, not validated. Labour + electricity only: heating, CAPEX, consumables and fish revenue are not included, so this is not total operating cost, profit or viability.",
        "generated_by": "scripts/compare_unit_configurations.py",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "inputs_file": rel(inputs_path),
        "case_definitions": {
            "low": "lowest yield, price and saleability; highest labour, wage and electricity",
            "mid": "midpoint of every range",
            "high": "highest yield, price and saleability; lowest labour, wage and electricity",
        },
        "headroom_meaning": "Revenue minus labour and electricity. It must still pay for heating, CAPEX, consumables and (where uncosted) owner time.",
        "not_in_cost_lines": data.get("not_in_cost_lines", {}),
        "results": rows,
    }


def summary_table(output: dict) -> str:
    lines = [
        "| Config | Location | Headroom per m2/yr (low / mid / high) | Labour h per unit used | Break-even labour h per unit | Verdict |",
        "|---|---|---|---|---|---|",
    ]
    for r in output["results"]:
        if r["missing_inputs"]:
            lines.append(f"| {r['config_id']} | {r['location']} | missing: {', '.join(r['missing_inputs'])} | | | gap |")
            continue
        c = r["cases"]
        cur = r["currency_code"]
        head = " / ".join(f"{c[k]['headroom_per_m2_yr']:,.0f}" for k in CASES)
        used = f"{c['high']['labour_h_per_harvested_unit']}-{c['low']['labour_h_per_harvested_unit']}"
        be = f"{c['low']['breakeven_labour_h_per_harvested_unit']}-{c['high']['breakeven_labour_h_per_harvested_unit']}"
        lines.append(f"| {r['config_id']} | {r['location']} | {cur} {head} | {used} | {be} | {r['verdict']} |")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--inputs", default=str(DEFAULT_INPUTS))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    def to_path(p: str) -> Path:
        path = Path(p)
        return path if path.is_absolute() else PROJECT_ROOT / path

    output = build(to_path(args.inputs))
    out = to_path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Saved to {rel(out)}\n")
    print(summary_table(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
