import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def run_step(command: list[str], step_name: str) -> None:
    print(f"\n=== Running: {step_name} ===")
    print("Command:", " ".join(command))
    result = subprocess.run(command, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        raise RuntimeError(f"{step_name} failed with exit code {result.returncode}")

def main():
    if len(sys.argv) < 2:
        raise ValueError(
            "Usage: python src/run_pipeline.py <run_config_filename.yaml>\n"
            "Example: python src/run_pipeline.py fao_ch02.yaml"
        )

    run_config_name = sys.argv[1]

    python_cmd = sys.executable

    run_step(
        [python_cmd, "src/extract_claims.py", run_config_name],
        "extract_claims"
    )

    run_step(
        [python_cmd, "src/review_claims.py"],
        "review_claims"
    )

    run_step(
        [python_cmd, "src/merge_facts.py"],
        "merge_facts"
    )

    run_step(
        [python_cmd, "src/promote_provisionals.py"],
        "promote_provisionals"
    )

    print("\n=== Pipeline completed successfully ===")
    print(f"Run config used: {run_config_name}")

if __name__ == "__main__":
    main()