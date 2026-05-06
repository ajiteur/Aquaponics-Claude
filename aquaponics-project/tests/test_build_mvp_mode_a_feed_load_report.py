import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "build_mvp_mode_a_feed_load_report.py"
EXAMPLE_INPUT_PATH = (
    PROJECT_ROOT / "scripts" / "example_mvp_mode_a_feed_load_inputs.json"
)
P1_EXAMPLE_INPUT_PATH = (
    PROJECT_ROOT / "scripts" / "example_mvp_mode_a_p1_water_quality_inputs.json"
)
P1_5_EXAMPLE_INPUT_PATH = (
    PROJECT_ROOT / "scripts" / "example_mvp_mode_a_p1_5_aeration_solids_inputs.json"
)


class BuildMvpModeAFeedLoadReportScriptTests(unittest.TestCase):
    def test_script_reads_example_input_and_prints_valid_json(self) -> None:
        result = run_script("--input", str(EXAMPLE_INPUT_PATH))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        report = json.loads(result.stdout)
        self.assertEqual(
            set(report),
            {
                "scenario_id",
                "input_mode",
                "inputs",
                "optional_context",
                "loads",
                "calculation_basis",
                "status_labels",
                "boundary_notes",
            },
        )
        self.assertEqual(report["scenario_id"], "demo_mode_a_tilapia_basil_dwc")
        self.assertEqual(report["input_mode"], "mode_a_direct_feed")
        self.assertNotIn("water_quality_context", report)
        self.assertNotIn("aeration_solids_context", report)

    def test_output_includes_expected_load_values(self) -> None:
        report = run_example_report()

        self.assertAlmostEqual(report["loads"]["tan_n_load_kg_day"], 0.02944)
        self.assertAlmostEqual(report["loads"]["tan_n_load_g_day"], 29.44)
        self.assertAlmostEqual(report["loads"]["oxygen_demand_g_day"], 134.5408)
        self.assertAlmostEqual(
            report["loads"]["alkalinity_demand_g_caco3_day"], 210.2016
        )

    def test_p1_example_still_has_water_quality_without_aeration_solids(self) -> None:
        report = run_p1_example_report()

        self.assertIn("water_quality_context", report)
        self.assertNotIn("aeration_solids_context", report)

    def test_script_reads_p1_example_and_prints_water_quality_context(self) -> None:
        result = run_script("--input", str(P1_EXAMPLE_INPUT_PATH))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        report = json.loads(result.stdout)
        self.assertEqual(report["scenario_id"], "demo_mode_a_tilapia_basil_dwc_p1")
        self.assertEqual(report["input_mode"], "mode_a_direct_feed")
        self.assertIn("water_quality_context", report)

        water_quality = report["water_quality_context"]
        self.assertEqual(water_quality["concentration_scope"], "fish_tank")
        self.assertEqual(
            water_quality["concentration_assumption"], "upper_bound_no_removal"
        )
        self.assertAlmostEqual(
            water_quality["estimated_tan_n_mg_l"], 3.7743589743589743
        )
        self.assertAlmostEqual(
            water_quality["estimated_unionized_nh3_fraction"],
            0.006971085009084945,
        )
        self.assertAlmostEqual(
            water_quality["estimated_nh3_n_mg_l"], 0.026311377265059072
        )
        self.assertAlmostEqual(
            water_quality["estimated_nh3_mg_l"], 0.031949529536143155
        )

    def test_p1_output_keeps_loads_and_suppresses_only_p1_missing_labels(self) -> None:
        report = run_p1_example_report()

        self.assertAlmostEqual(report["loads"]["tan_n_load_kg_day"], 0.02944)
        self.assertAlmostEqual(report["loads"]["tan_n_load_g_day"], 29.44)
        self.assertAlmostEqual(report["loads"]["oxygen_demand_g_day"], 134.5408)
        self.assertAlmostEqual(
            report["loads"]["alkalinity_demand_g_caco3_day"], 210.2016
        )

        labels = set(report["status_labels"])
        self.assertNotIn(
            "tan_concentration_unavailable_without_volume_time_exchange_or_removal",
            labels,
        )
        self.assertNotIn("nh3_risk_unavailable_without_ph_and_temperature", labels)
        self.assertIn("feed_cost_unavailable_without_feed_price", labels)
        self.assertIn(
            "tank_suitability_unavailable_without_volume_and_stocking_density",
            labels,
        )
        self.assertIn(
            "biofilter_removal_unavailable_without_capacity_and_conversion_assumption",
            labels,
        )
        self.assertIn(
            "basil_saleable_output_unresolved_without_observed_or_reviewed_value",
            labels,
        )

    def test_script_reads_p1_5_example_and_prints_p1_and_p1_5_sections(self) -> None:
        result = run_script("--input", str(P1_5_EXAMPLE_INPUT_PATH))

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        report = json.loads(result.stdout)
        self.assertEqual(report["scenario_id"], "demo_mode_a_tilapia_basil_dwc_p1_5")
        self.assertIn("water_quality_context", report)
        self.assertIn("aeration_solids_context", report)

        self.assertAlmostEqual(report["loads"]["tan_n_load_kg_day"], 0.02944)
        self.assertAlmostEqual(report["loads"]["tan_n_load_g_day"], 29.44)
        self.assertAlmostEqual(report["loads"]["oxygen_demand_g_day"], 134.5408)
        self.assertAlmostEqual(
            report["loads"]["alkalinity_demand_g_caco3_day"], 210.2016
        )

        aeration_solids = report["aeration_solids_context"]
        self.assertEqual(
            aeration_solids["oxygen_context"]["nitrification_oxygen_demand_g_day"],
            134.5408,
        )
        self.assertEqual(
            aeration_solids["aeration_context"]["measured_do_mg_l"], 5.0
        )
        self.assertAlmostEqual(
            aeration_solids["solids_context"][
                "estimated_dry_solids_potential_kg_day"
            ],
            0.25,
        )
        self.assertIn(
            "total_oxygen_demand_unavailable",
            aeration_solids["status_labels"],
        )
        self.assertNotIn("total_oxygen_demand_unavailable", report["status_labels"])

    def test_output_includes_missing_context_status_labels(self) -> None:
        report = run_example_report()

        labels = set(report["status_labels"])
        self.assertIn(
            "tan_concentration_unavailable_without_volume_time_exchange_or_removal",
            labels,
        )
        self.assertIn("nh3_risk_unavailable_without_ph_and_temperature", labels)
        self.assertIn("feed_cost_unavailable_without_feed_price", labels)
        self.assertIn(
            "tank_suitability_unavailable_without_volume_and_stocking_density",
            labels,
        )
        self.assertIn(
            "biofilter_removal_unavailable_without_capacity_and_conversion_assumption",
            labels,
        )
        self.assertIn(
            "basil_saleable_output_unresolved_without_observed_or_reviewed_value",
            labels,
        )

    def test_fails_clearly_for_missing_input_argument(self) -> None:
        result = run_script()

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("--input", result.stderr)

    def test_fails_clearly_for_missing_input_path(self) -> None:
        result = run_script("--input", "scripts/does_not_exist_mode_a_input.json")

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("input path does not exist or is not a file", result.stderr)

    def test_fails_clearly_for_invalid_input_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            invalid_path = Path(temp_dir) / "invalid.json"
            invalid_path.write_text("{invalid json", encoding="utf-8")

            result = run_script("--input", str(invalid_path))

        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("invalid input JSON", result.stderr)

    def test_script_does_not_write_output_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            before = sorted(Path(temp_dir).iterdir())
            result = subprocess.run(
                [sys.executable, str(SCRIPT_PATH), "--input", str(EXAMPLE_INPUT_PATH)],
                cwd=temp_dir,
                capture_output=True,
                text=True,
            )
            after = sorted(Path(temp_dir).iterdir())

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(before, after)

    def test_output_does_not_include_disallowed_calculated_field_keys(self) -> None:
        report = run_example_report()

        for disallowed_key in {
            "saleable_harvest_mass_kg",
            "tan_mg_l",
            "unionized_nh3_mg_l",
            "feed_cost",
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
            "aeration_capacity_sufficient",
        }:
            self.assertFalse(_contains_key(report, disallowed_key), disallowed_key)

    def test_p1_and_p1_5_outputs_do_not_include_disallowed_calculated_field_keys(self) -> None:
        reports = [run_p1_example_report(), run_p1_5_example_report()]

        for report in reports:
            for disallowed_key in {
                "saleable_harvest_mass_kg",
                "feed_cost",
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
                "aeration_capacity_sufficient",
            }:
                self.assertFalse(_contains_key(report, disallowed_key), disallowed_key)


def run_script(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), *args],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )


def run_example_report() -> dict:
    result = run_script("--input", str(EXAMPLE_INPUT_PATH))
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


def run_p1_example_report() -> dict:
    result = run_script("--input", str(P1_EXAMPLE_INPUT_PATH))
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


def run_p1_5_example_report() -> dict:
    result = run_script("--input", str(P1_5_EXAMPLE_INPUT_PATH))
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return json.loads(result.stdout)


def _contains_key(value: object, target_key: str) -> bool:
    if isinstance(value, dict):
        return target_key in value or any(
            _contains_key(child, target_key) for child in value.values()
        )
    if isinstance(value, list):
        return any(_contains_key(child, target_key) for child in value)
    return False


if __name__ == "__main__":
    unittest.main()
