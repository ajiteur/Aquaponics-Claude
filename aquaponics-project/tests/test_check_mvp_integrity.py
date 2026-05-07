import contextlib
import importlib.util
import io
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = PROJECT_ROOT / "scripts" / "check_mvp_integrity.py"

spec = importlib.util.spec_from_file_location("check_mvp_integrity", SCRIPT_PATH)
integrity = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["check_mvp_integrity"] = integrity
spec.loader.exec_module(integrity)


class CheckMvpIntegrityTests(unittest.TestCase):
    def test_default_mode_is_full(self) -> None:
        args = integrity.parse_args([])

        self.assertEqual(args.mode, "full")

    def test_quick_mode_is_supported(self) -> None:
        args = integrity.parse_args(["--quick"])

        self.assertEqual(args.mode, "quick")

    def test_expected_p2a_values_pass_for_current_demo_output(self) -> None:
        reports, failures = integrity.run_demo_commands()

        self.assertEqual(failures, [])
        self.assertIn("p2a_operating_cost", reports)
        self.assertEqual(
            integrity.check_expected_p2a_values(reports["p2a_operating_cost"]),
            [],
        )

    def test_forbidden_key_scan_recurses_through_dicts_and_lists(self) -> None:
        reports = {
            "demo": {
                "outer": [
                    {"safe": False},
                    {"nested": {"total_operating_cost": 1}},
                ]
            }
        }

        self.assertEqual(
            integrity.scan_forbidden_keys(reports),
            [
                "demo.outer[0].safe",
                "demo.outer[1].nested.total_operating_cost",
            ],
        )

    def test_approved_operating_cost_pressure_keys_are_not_forbidden(self) -> None:
        reports = {
            "demo": {
                "scenario_feed_cost_per_day": 45.0,
                "scenario_power_cost_per_day": 54.0,
                "selected_operating_cost_pressure_subtotal": 99.0,
            }
        }

        self.assertEqual(integrity.scan_forbidden_keys(reports), [])

    def test_snapshot_text_includes_guardrails_and_latest_values(self) -> None:
        snapshot = integrity.IntegritySnapshot(
            mode="quick",
            commit="abc123",
            demos_status="PASS",
            expected_values_status="PASS",
            forbidden_keys_status="NONE FOUND",
            protected_paths_status="CLEAN",
            latest_demo_values={
                "tan_n_load_g_day": 29.44,
                "oxygen_demand_g_day": 134.5408,
                "alkalinity_demand_g_caco3_day": 210.2016,
                "estimated_tan_n_mg_l": 3.7743589743589743,
                "estimated_nh3_n_mg_l": 0.026311377265059072,
                "estimated_nh3_mg_l": 0.031949529536143155,
                "estimated_dry_solids_potential_kg_day": 0.25,
                "scenario_feed_cost_per_day": 45.0,
                "scenario_power_cost_per_day": 54.0,
                "selected_operating_cost_pressure_subtotal": 99.0,
                "selected_operating_cost_pressure_currency": "INR",
            },
        )

        text = integrity.build_snapshot_text(snapshot)

        self.assertIn("MVP INTEGRITY SNAPSHOT - PASS", text)
        self.assertIn("- TAN-N load: 29.44 g/day", text)
        self.assertIn("- Feed cost: 45.0 INR/day", text)
        self.assertIn("- No saleable_harvest_mass_kg", text)

    def test_quick_main_returns_zero_and_prints_snapshot(self) -> None:
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            exit_code = integrity.main(["--quick"])

        output = stdout.getvalue()
        self.assertEqual(exit_code, 0, output)
        self.assertIn("Mode: quick", output)
        self.assertIn("Demos: PASS", output)
        self.assertIn("Expected values: PASS", output)
        self.assertIn("Protected paths: CLEAN", output)


if __name__ == "__main__":
    unittest.main()
