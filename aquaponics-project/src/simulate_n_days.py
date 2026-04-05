from pathlib import Path
import subprocess
import sys
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def run_one_day(scenario_path: Path) -> Path:
    cmd = [
        sys.executable,
        "src/simulate_day.py",
        str(scenario_path)
    ]

    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"simulate_day failed\n\nSTDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    lines = result.stdout.splitlines()
    saved_line = None
    for line in lines:
        if line.startswith("Saved updated scenario to:"):
            saved_line = line
            break

    if saved_line is None:
        raise RuntimeError(f"Could not find saved scenario path in output:\n{result.stdout}")

    saved_path = saved_line.replace("Saved updated scenario to:", "").strip()
    return Path(saved_path)


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    if len(sys.argv) < 3:
        raise ValueError(
            "Usage:\n"
            "python src/simulate_n_days.py <scenario_path> <num_days>\n\n"
            "Example:\n"
            "python src/simulate_n_days.py data\\simulation\\scenarios\\starter_tilapia_lettuce_system.json 30"
        )

    scenario_path = Path(sys.argv[1])
    if not scenario_path.is_absolute():
        scenario_path = PROJECT_ROOT / scenario_path

    num_days = int(sys.argv[2])

    if not scenario_path.exists():
        raise FileNotFoundError(f"Scenario not found: {scenario_path}")

    current_path = scenario_path
    history = []

    for _ in range(num_days):
        current_path = run_one_day(current_path)
        scenario = load_json(current_path)

        history.append({
            "day": scenario["time"]["day"],
            "scenario_file": str(current_path),
            "pH": scenario["water_state"]["pH"],
            "tan_mg_L": scenario["water_state"]["tan_mg_L"],
            "unionized_nh3_mg_L": scenario["water_state"]["unionized_nh3_mg_L"],
            "nitrate_mg_L": scenario["water_state"]["nitrate_mg_L"],
            "fish_biomass_kg": scenario["fish_batch"]["total_biomass_kg"],
            "avg_fish_weight_g": scenario["fish_batch"]["average_weight_g"],
            "plant_avg_biomass_g": scenario["plant_crop"]["average_biomass_g"],
            "daily_operating_cost": scenario["derived"]["daily_operating_cost"],
            "system_stability_score": scenario["derived"]["system_stability_score"]
        })

    output_path = PROJECT_ROOT / "data" / "simulation" / "multi_day_summary.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

    print(f"Saved multi-day summary to: {output_path}")
    print(json.dumps({
        "days_simulated": num_days,
        "final_day": history[-1] if history else None
    }, indent=2))


if __name__ == "__main__":
    main()