"""Run a scenario day by day for N days and save one result file.

Unlike simulate_n_days.py, this keeps the chained per-day scenario files in a
temporary folder, so long runs (a full crop cycle) don't create dozens of files
with ever-longer names. Day logs are still written by simulate_day.py.

Usage:
    python src/simulate_crop_cycle.py <scenario_path> <num_days> [--out <result_path>]
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_ROOT / "data" / "simulation" / "results"


def run_one_day(scenario_path: Path) -> Path:
    result = subprocess.run(
        [sys.executable, "src/simulate_day.py", str(scenario_path)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"simulate_day failed\n{result.stdout}\n{result.stderr}")
    for line in result.stdout.splitlines():
        if line.startswith("Saved updated scenario to:"):
            return Path(line.replace("Saved updated scenario to:", "").strip())
    raise RuntimeError(f"Could not find saved scenario path in output:\n{result.stdout}")


def run_cycle(scenario_path: Path, num_days: int) -> dict:
    daily = []
    with tempfile.TemporaryDirectory() as tmp:
        working = Path(tmp) / "working.json"
        shutil.copyfile(scenario_path, working)
        for _ in range(num_days):
            saved = run_one_day(working)
            shutil.move(str(saved), working)
            state = json.loads(working.read_text(encoding="utf-8"))
            derived = state.get("derived", {})
            daily.append(
                {
                    "day": state["time"]["day"],
                    "plant_growth_score": derived.get("plant_growth_score"),
                    "plant_score_relative_to_anchor": derived.get("plant_score_relative_to_anchor"),
                    "nitrate_availability_score": derived.get("nitrate_availability_score"),
                    "harvestable_cut_mass_g_per_plant": derived.get("harvestable_cut_mass_g_per_plant"),
                    "tan_mg_L": state["water_state"]["tan_mg_L"],
                    "unionized_nh3_mg_L": state["water_state"]["unionized_nh3_mg_L"],
                    "nitrate_mg_L": state["water_state"]["nitrate_mg_L"],
                    "pH": state["water_state"]["pH"],
                    "harvest_event": derived.get("harvest_event_today"),
                }
            )
        final_state = json.loads(working.read_text(encoding="utf-8"))

    events = final_state.get("harvest_events", [])
    scores = [d["plant_growth_score"] for d in daily if d["plant_growth_score"] is not None]
    return {
        "scenario_source": scenario_path.relative_to(PROJECT_ROOT).as_posix()
        if scenario_path.is_relative_to(PROJECT_ROOT)
        else str(scenario_path),
        "scenario_id": final_state.get("scenario_id"),
        "num_days": num_days,
        "estimate_status": "scenario_estimate",
        "note": "Scenario estimate, not validated. Derived runtime output; not canon and not observed data.",
        "summary": {
            "harvest_event_count": len(events),
            "total_harvested_mass_kg": round(sum(e["harvested_mass_kg"] for e in events), 3),
            "mean_plant_growth_score": round(sum(scores) / len(scores), 3) if scores else None,
            "min_plant_growth_score": min(scores) if scores else None,
        },
        "harvest_events": events,
        "daily": daily,
        "final_state": final_state,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("scenario_path")
    parser.add_argument("num_days", type=int)
    parser.add_argument("--out", help="Result path (default data/simulation/results/<scenario_id>_<N>d.json)")
    args = parser.parse_args()

    scenario_path = Path(args.scenario_path)
    if not scenario_path.is_absolute():
        scenario_path = PROJECT_ROOT / scenario_path
    result = run_cycle(scenario_path, args.num_days)

    out = Path(args.out) if args.out else RESULTS_DIR / f"{result['scenario_id']}_{args.num_days}d.json"
    if not out.is_absolute():
        out = PROJECT_ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({"saved_to": str(out), "summary": result["summary"], "harvest_events": result["harvest_events"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
