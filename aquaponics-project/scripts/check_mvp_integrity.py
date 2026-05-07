#!/usr/bin/env python3
"""MVP Integrity Snapshot Runner for the aquaponics MVP demo path."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FLOAT_TOLERANCE = 1e-9

CORE_COMPILE_FILES = (
    "src/feed_waste_tan_loads.py",
    "src/mvp_tan_nh3_risk.py",
    "src/mvp_aeration_solids_context.py",
    "src/mvp_operating_cost_pressure.py",
    "src/mvp_mode_a_feed_load_report.py",
    "scripts/build_mvp_mode_a_feed_load_report.py",
)

UNIT_TEST_MODULES = (
    "tests.test_feed_waste_tan_loads",
    "tests.test_mvp_tan_nh3_risk",
    "tests.test_mvp_aeration_solids_context",
    "tests.test_mvp_operating_cost_pressure",
    "tests.test_mvp_mode_a_feed_load_report",
    "tests.test_build_mvp_mode_a_feed_load_report",
)

DEMO_INPUTS = (
    ("load_only", "scripts/example_mvp_mode_a_feed_load_inputs.json"),
    ("p1_water_quality", "scripts/example_mvp_mode_a_p1_water_quality_inputs.json"),
    ("p1_5_aeration_solids", "scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json"),
    ("p2a_operating_cost", "scripts/example_mvp_mode_a_p2a_operating_cost_inputs.json"),
)

EXPECTED_P2A_VALUES = {
    ("loads", "tan_n_load_kg_day"): 0.02944,
    ("loads", "tan_n_load_g_day"): 29.44,
    ("loads", "oxygen_demand_g_day"): 134.5408,
    ("loads", "alkalinity_demand_g_caco3_day"): 210.2016,
    ("water_quality_context", "estimated_tan_n_mg_l"): 3.7743589743589743,
    (
        "water_quality_context",
        "estimated_unionized_nh3_fraction",
    ): 0.006971085009084945,
    ("water_quality_context", "estimated_nh3_n_mg_l"): 0.026311377265059072,
    ("water_quality_context", "estimated_nh3_mg_l"): 0.031949529536143155,
    (
        "aeration_solids_context",
        "aeration_context",
        "measured_do_mg_l",
    ): 5.0,
    (
        "aeration_solids_context",
        "solids_context",
        "estimated_dry_solids_potential_kg_day",
    ): 0.25,
    (
        "operating_cost_pressure",
        "cost_outputs",
        "category_costs",
        "feed",
        "scenario_feed_cost_per_day",
    ): 45.0,
    (
        "operating_cost_pressure",
        "cost_outputs",
        "category_costs",
        "power",
        "scenario_power_kwh_day",
    ): 7.2,
    (
        "operating_cost_pressure",
        "cost_outputs",
        "category_costs",
        "power",
        "scenario_power_cost_per_day",
    ): 54.0,
    (
        "operating_cost_pressure",
        "cost_outputs",
        "selected_operating_cost_pressure_subtotal",
    ): 99.0,
}

FORBIDDEN_KEYS = {
    "saleable_harvest_mass_kg",
    "tank_suitability",
    "biofilter_removal",
    "aeration_capacity",
    "oxygen_transfer_capacity",
    "total_oxygen_demand",
    "fish_respiration_oxygen_demand",
    "wet_sludge",
    "tss",
    "system_safe",
    "fish_safe",
    "safe",
    "unsafe",
    "profitability",
    "profit",
    "gross_margin",
    "contribution_margin",
    "roi",
    "payback",
    "break_even",
    "economic_viability",
    "fish_revenue",
    "basil_revenue",
    "crop_revenue",
    "total_operating_cost",
}

APPROVED_OPERATING_COST_PRESSURE_KEYS = {
    "scenario_feed_cost_per_day",
    "scenario_power_cost_per_day",
    "selected_operating_cost_pressure_subtotal",
}


@dataclass
class CommandResult:
    args: list[str]
    returncode: int
    stdout: str
    stderr: str


@dataclass
class IntegritySnapshot:
    mode: str
    commit: str = "unavailable"
    compile_status: str = "SKIPPED"
    tests_status: str = "SKIPPED"
    demos_status: str = "NOT RUN"
    expected_values_status: str = "NOT RUN"
    forbidden_keys_status: str = "NOT RUN"
    protected_paths_status: str = "NOT RUN"
    git_status: str = ""
    latest_demo_values: dict[str, Any] = field(default_factory=dict)
    forbidden_key_hits: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return not self.failures


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the MVP Integrity Snapshot Runner."
    )
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--quick", action="store_true", help="Run demo checks only.")
    mode_group.add_argument("--full", action="store_true", help="Run full integrity checks.")
    args = parser.parse_args(argv)
    args.mode = "quick" if args.quick else "full"
    return args


def run_command(args: list[str], *, cwd: Path = PROJECT_ROOT) -> CommandResult:
    completed = subprocess.run(
        args,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return CommandResult(
        args=args,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def run_py_compile() -> tuple[str, list[str]]:
    result = run_command([sys.executable, "-m", "py_compile", *CORE_COMPILE_FILES])
    if result.returncode == 0:
        return "PASS", []
    return "FAIL", [_format_command_failure("py_compile", result)]


def run_unit_tests() -> tuple[str, list[str]]:
    result = run_command([sys.executable, "-m", "unittest", *UNIT_TEST_MODULES])
    if result.returncode == 0:
        return "PASS", []
    return "FAIL", [_format_command_failure("unit tests", result)]


def run_demo_commands() -> tuple[dict[str, dict[str, Any]], list[str]]:
    reports: dict[str, dict[str, Any]] = {}
    failures: list[str] = []

    for demo_name, input_path in DEMO_INPUTS:
        result = run_command(
            [
                sys.executable,
                "scripts/build_mvp_mode_a_feed_load_report.py",
                "--input",
                input_path,
            ]
        )
        if result.returncode != 0:
            failures.append(_format_command_failure(f"demo {demo_name}", result))
            continue
        try:
            parsed = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            failures.append(f"demo {demo_name} stdout was not valid JSON: {exc}")
            continue
        if not isinstance(parsed, dict):
            failures.append(f"demo {demo_name} stdout JSON was not an object")
            continue
        reports[demo_name] = parsed

    return reports, failures


def check_expected_p2a_values(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    for path, expected in EXPECTED_P2A_VALUES.items():
        try:
            actual = value_at_path(report, path)
        except KeyError:
            failures.append(f"missing expected value: {'.'.join(path)}")
            continue
        if not isinstance(actual, (int, float)) or isinstance(actual, bool):
            failures.append(f"expected numeric value at {'.'.join(path)}, got {actual!r}")
            continue
        if abs(float(actual) - expected) > FLOAT_TOLERANCE:
            failures.append(
                f"{'.'.join(path)} expected {expected!r}, got {actual!r}"
            )
    return failures


def value_at_path(value: dict[str, Any], path: tuple[str, ...]) -> Any:
    current: Any = value
    for key in path:
        if not isinstance(current, dict) or key not in current:
            raise KeyError(key)
        current = current[key]
    return current


def scan_forbidden_keys(reports: dict[str, Any]) -> list[str]:
    hits: list[str] = []
    for report_name, report in reports.items():
        hits.extend(_scan_value_for_forbidden_keys(report, report_name))
    return sorted(hits)


def _scan_value_for_forbidden_keys(value: Any, path: str) -> list[str]:
    hits: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key in FORBIDDEN_KEYS and key not in APPROVED_OPERATING_COST_PRESSURE_KEYS:
                hits.append(child_path)
            hits.extend(_scan_value_for_forbidden_keys(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits.extend(_scan_value_for_forbidden_keys(child, f"{path}[{index}]"))
    return hits


def run_protected_path_diff_check() -> tuple[str, list[str]]:
    result = run_command(
        [
            "git",
            "--no-pager",
            "diff",
            "--name-only",
            "--",
            "data/knowledge",
            "data/simulation",
            "src/simulate_day.py",
        ]
    )
    if result.returncode != 0:
        return "FAIL", [_format_command_failure("protected path diff", result)]
    changed_paths = [line for line in result.stdout.splitlines() if line.strip()]
    if changed_paths:
        return "DIRTY", ["protected path diff is non-empty: " + ", ".join(changed_paths)]
    return "CLEAN", []


def get_git_status_short() -> str:
    result = run_command(["git", "status", "--short"])
    if result.returncode != 0:
        return "unavailable"
    return result.stdout.strip() or "clean"


def get_commit_short() -> str:
    result = run_command(["git", "rev-parse", "--short", "HEAD"])
    if result.returncode != 0:
        return "unavailable"
    return result.stdout.strip() or "unavailable"


def extract_latest_demo_values(p2a_report: dict[str, Any]) -> dict[str, Any]:
    return {
        "tan_n_load_g_day": value_at_path(p2a_report, ("loads", "tan_n_load_g_day")),
        "oxygen_demand_g_day": value_at_path(
            p2a_report, ("loads", "oxygen_demand_g_day")
        ),
        "alkalinity_demand_g_caco3_day": value_at_path(
            p2a_report, ("loads", "alkalinity_demand_g_caco3_day")
        ),
        "estimated_tan_n_mg_l": value_at_path(
            p2a_report, ("water_quality_context", "estimated_tan_n_mg_l")
        ),
        "estimated_nh3_n_mg_l": value_at_path(
            p2a_report, ("water_quality_context", "estimated_nh3_n_mg_l")
        ),
        "estimated_nh3_mg_l": value_at_path(
            p2a_report, ("water_quality_context", "estimated_nh3_mg_l")
        ),
        "estimated_dry_solids_potential_kg_day": value_at_path(
            p2a_report,
            (
                "aeration_solids_context",
                "solids_context",
                "estimated_dry_solids_potential_kg_day",
            ),
        ),
        "scenario_feed_cost_per_day": value_at_path(
            p2a_report,
            (
                "operating_cost_pressure",
                "cost_outputs",
                "category_costs",
                "feed",
                "scenario_feed_cost_per_day",
            ),
        ),
        "scenario_power_cost_per_day": value_at_path(
            p2a_report,
            (
                "operating_cost_pressure",
                "cost_outputs",
                "category_costs",
                "power",
                "scenario_power_cost_per_day",
            ),
        ),
        "selected_operating_cost_pressure_subtotal": value_at_path(
            p2a_report,
            (
                "operating_cost_pressure",
                "cost_outputs",
                "selected_operating_cost_pressure_subtotal",
            ),
        ),
        "selected_operating_cost_pressure_currency": value_at_path(
            p2a_report,
            (
                "operating_cost_pressure",
                "cost_outputs",
                "selected_operating_cost_pressure_currency",
            ),
        ),
    }


def run_integrity_snapshot(mode: str) -> IntegritySnapshot:
    snapshot = IntegritySnapshot(mode=mode, commit=get_commit_short())

    if mode == "full":
        snapshot.compile_status, compile_failures = run_py_compile()
        snapshot.failures.extend(compile_failures)
        snapshot.tests_status, test_failures = run_unit_tests()
        snapshot.failures.extend(test_failures)

    reports, demo_failures = run_demo_commands()
    if demo_failures:
        snapshot.demos_status = "FAIL"
        snapshot.failures.extend(demo_failures)
    else:
        snapshot.demos_status = "PASS"

    p2a_report = reports.get("p2a_operating_cost")
    if p2a_report is None:
        snapshot.expected_values_status = "FAIL"
        snapshot.failures.append("p2a_operating_cost demo report was unavailable")
    else:
        expected_failures = check_expected_p2a_values(p2a_report)
        if expected_failures:
            snapshot.expected_values_status = "FAIL"
            snapshot.failures.extend(expected_failures)
        else:
            snapshot.expected_values_status = "PASS"
        try:
            snapshot.latest_demo_values = extract_latest_demo_values(p2a_report)
        except KeyError as exc:
            snapshot.failures.append(f"latest demo value missing: {exc}")

    forbidden_hits = scan_forbidden_keys(reports)
    snapshot.forbidden_key_hits = forbidden_hits
    if forbidden_hits:
        snapshot.forbidden_keys_status = "FOUND"
        snapshot.failures.append("forbidden output keys found: " + ", ".join(forbidden_hits))
    else:
        snapshot.forbidden_keys_status = "NONE FOUND"

    snapshot.protected_paths_status, protected_failures = run_protected_path_diff_check()
    snapshot.failures.extend(protected_failures)

    if mode == "full":
        snapshot.git_status = get_git_status_short()

    return snapshot


def build_snapshot_text(snapshot: IntegritySnapshot) -> str:
    title_status = "PASS" if snapshot.passed else "FAIL"
    lines = [
        f"MVP INTEGRITY SNAPSHOT - {title_status}",
        "",
        f"Mode: {snapshot.mode}",
        f"Commit: {snapshot.commit}",
        f"Compile: {snapshot.compile_status}",
        f"Tests: {snapshot.tests_status}",
        f"Demos: {snapshot.demos_status}",
        f"Expected values: {snapshot.expected_values_status}",
        f"Forbidden keys: {snapshot.forbidden_keys_status}",
        f"Protected paths: {snapshot.protected_paths_status}",
    ]

    if snapshot.mode == "full":
        lines.extend(["", "Git status:", snapshot.git_status])

    if snapshot.latest_demo_values:
        currency = snapshot.latest_demo_values.get(
            "selected_operating_cost_pressure_currency", "scenario currency"
        )
        lines.extend(
            [
                "",
                "Latest demo values:",
                f"- TAN-N load: {snapshot.latest_demo_values['tan_n_load_g_day']} g/day",
                f"- O2 demand: {snapshot.latest_demo_values['oxygen_demand_g_day']} g/day",
                (
                    "- Alkalinity demand: "
                    f"{snapshot.latest_demo_values['alkalinity_demand_g_caco3_day']} "
                    "g CaCO3/day"
                ),
                (
                    "- TAN-N concentration: "
                    f"{snapshot.latest_demo_values['estimated_tan_n_mg_l']} mg/L"
                ),
                f"- NH3-N: {snapshot.latest_demo_values['estimated_nh3_n_mg_l']} mg/L",
                f"- NH3: {snapshot.latest_demo_values['estimated_nh3_mg_l']} mg/L",
                (
                    "- Dry-solids potential: "
                    f"{snapshot.latest_demo_values['estimated_dry_solids_potential_kg_day']} "
                    "kg/day"
                ),
                (
                    f"- Feed cost: {snapshot.latest_demo_values['scenario_feed_cost_per_day']} "
                    f"{currency}/day"
                ),
                (
                    f"- Power cost: {snapshot.latest_demo_values['scenario_power_cost_per_day']} "
                    f"{currency}/day"
                ),
                (
                    "- Selected cost-pressure subtotal: "
                    f"{snapshot.latest_demo_values['selected_operating_cost_pressure_subtotal']} "
                    f"{currency}/day"
                ),
            ]
        )

    lines.extend(
        [
            "",
            "Guardrails:",
            "- No safety claims",
            "- No revenue/profitability claims",
            "- No total operating cost",
            "- No saleable_harvest_mass_kg",
        ]
    )

    if snapshot.failures:
        lines.extend(["", "Failures:"])
        lines.extend(f"- {failure}" for failure in snapshot.failures)

    return "\n".join(lines) + "\n"


def _format_command_failure(name: str, result: CommandResult) -> str:
    command = " ".join(result.args)
    stderr = result.stderr.strip()
    stdout = result.stdout.strip()
    detail = stderr or stdout or "no output"
    return f"{name} failed with exit code {result.returncode}: {command}; {detail}"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    snapshot = run_integrity_snapshot(args.mode)
    print(build_snapshot_text(snapshot), end="")
    return 0 if snapshot.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
