import subprocess
import sys
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PH_VALUES = [5.8, 6.0, 6.4, 6.8, 7.0]
WATER_TEMP_VALUES = [24.0, 28.0]
AIR_TEMP_VALUES = [20.0, 24.0, 28.0]
DO_MG_L = 5.5
UNIONIZED_NH3_MG_L = 0.05


def run_case(
    fish: str,
    plant: str,
    pH: float,
    water_temp_c: float,
    air_temp_c: float,
    do_mg_l: float,
    nh3_mg_l: float,
    mode: str,
) -> dict:
    cmd = [
        sys.executable,
        "src/simulate_overlap_score.py",
        fish,
        plant,
        str(pH),
        str(water_temp_c),
        str(air_temp_c),
        str(do_mg_l),
        str(nh3_mg_l),
        mode,
    ]

    result = subprocess.run(
        cmd,
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Scenario failed:\nCommand: {' '.join(cmd)}\n\nSTDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
        )

    return json.loads(result.stdout)


def summarize_case(case: dict) -> dict:
    fish_score = case["fish_assessment"]["overall_fish_score"]

    plant_score = None
    plant_assessment = case.get("plant_assessment")
    if plant_assessment and "overall_plant_score" in plant_assessment:
        plant_score = plant_assessment["overall_plant_score"]

    return {
        "pH": case["inputs"]["pH"],
        "water_temp_c": case["inputs"]["water_temperature_c"],
        "air_temp_c": case["inputs"]["air_temperature_c"],
        "mode": case["inputs"]["mode"],
        "fish_score": fish_score,
        "plant_score": plant_score,
        "nitrification_score": case["nitrification_assessment"]["score"],
        "mode_pH_score": case["mode_assessment"]["mode_pH_score"],
        "raw_average_score": case["raw_average_score"],
        "balance_score": case["balance_score"],
        "overall_system_score": case["overall_system_score"],
    }


def print_table(title: str, rows: list[dict], max_rows: int = 10) -> None:
    print(f"\n=== {title} ===")
    for row in rows[:max_rows]:
        print(
            f"pH={row['pH']:<4} "
            f"water={row['water_temp_c']:<4} "
            f"air={row['air_temp_c']:<4} "
            f"mode={row['mode']:<28} "
            f"fish={row['fish_score']:<5} "
            f"plant={row['plant_score']:<5} "
            f"nitrif={row['nitrification_score']:<5} "
            f"overall={row['overall_system_score']:<5}"
        )


def main() -> None:
    fish = "tilapia"
    plant = "lettuce"

    scenarios = []

    for mode in ["robust_compromise_mode", "plant_yield_optimization_mode"]:
        for pH in PH_VALUES:
            for water_temp_c in WATER_TEMP_VALUES:
                for air_temp_c in AIR_TEMP_VALUES:
                    raw = run_case(
                        fish=fish,
                        plant=plant,
                        pH=pH,
                        water_temp_c=water_temp_c,
                        air_temp_c=air_temp_c,
                        do_mg_l=DO_MG_L,
                        nh3_mg_l=UNIONIZED_NH3_MG_L,
                        mode=mode,
                    )
                    scenarios.append(summarize_case(raw))

    best = sorted(scenarios, key=lambda x: x["overall_system_score"], reverse=True)
    worst = sorted(scenarios, key=lambda x: x["overall_system_score"])

    print_table("Best scenarios", best, max_rows=10)
    print_table("Worst scenarios", worst, max_rows=10)

    output_path = PROJECT_ROOT / "data" / "simulation" / "tradeoff_matrix_results.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(scenarios, f, indent=2)

    print(f"\nSaved full results to: {output_path}")


if __name__ == "__main__":
    main()