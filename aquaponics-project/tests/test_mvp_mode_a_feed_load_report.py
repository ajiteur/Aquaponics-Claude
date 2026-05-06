import unittest

from src.mvp_mode_a_feed_load_report import (
    BASIL_SALEABLE_OUTPUT_UNRESOLVED,
    BIOFILTER_REMOVAL_UNAVAILABLE,
    FEED_COST_UNAVAILABLE,
    INPUT_MODE,
    NH3_RISK_UNAVAILABLE,
    TAN_CONCENTRATION_UNAVAILABLE,
    TANK_SUITABILITY_UNAVAILABLE,
    ModeAFeedLoadReportValidationError,
    build_mode_a_feed_load_report,
)


class ModeAFeedLoadReportTests(unittest.TestCase):
    def test_builds_valid_report_with_expected_loads(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

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
        self.assertEqual(report["scenario_id"], "demo_mode_a")
        self.assertEqual(report["input_mode"], INPUT_MODE)
        self.assertEqual(report["inputs"]["feed_kg_day"], 1.0)
        self.assertEqual(report["inputs"]["protein_fraction"], 0.32)
        self.assertAlmostEqual(report["loads"]["tan_n_load_kg_day"], 0.02944)
        self.assertAlmostEqual(report["loads"]["tan_n_load_g_day"], 29.44)
        self.assertAlmostEqual(report["loads"]["oxygen_demand_g_day"], 134.5408)
        self.assertAlmostEqual(
            report["loads"]["alkalinity_demand_g_caco3_day"], 210.2016
        )

    def test_calculation_basis_and_boundary_notes_are_load_only(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

        self.assertEqual(report["calculation_basis"]["input_mode"], INPUT_MODE)
        self.assertEqual(
            report["calculation_basis"]["tan_load_basis"],
            "TAN-N/ammonia-N load, not TAN concentration",
        )
        self.assertIn(
            "not confirmed biofilter removal",
            report["calculation_basis"]["oxygen_demand_basis"],
        )
        self.assertIn("No feed-cost calculation.", report["calculation_basis"]["calculation_limits"])
        self.assertIn("No tank-suitability calculation.", report["calculation_basis"]["calculation_limits"])
        self.assertIn("No crop saleability calculation.", report["calculation_basis"]["calculation_limits"])
        self.assertIn(
            "Report labels do not calculate or populate saleable_harvest_mass_kg.",
            report["boundary_notes"],
        )

    def test_reports_missing_context_status_labels_when_context_is_absent(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

        labels = set(report["status_labels"])
        self.assertIn(TAN_CONCENTRATION_UNAVAILABLE, labels)
        self.assertIn(NH3_RISK_UNAVAILABLE, labels)
        self.assertIn(FEED_COST_UNAVAILABLE, labels)
        self.assertIn(TANK_SUITABILITY_UNAVAILABLE, labels)
        self.assertIn(BIOFILTER_REMOVAL_UNAVAILABLE, labels)
        self.assertIn(BASIL_SALEABLE_OUTPUT_UNRESOLVED, labels)

    def test_suppresses_tan_concentration_label_only_with_required_context(self) -> None:
        partial_context_report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            water_volume_context_available=True,
            time_basis_context_available=True,
        )
        full_context_report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            water_volume_context_available=True,
            time_basis_context_available=True,
            exchange_or_retention_context_available=True,
        )

        self.assertIn(
            TAN_CONCENTRATION_UNAVAILABLE, partial_context_report["status_labels"]
        )
        self.assertNotIn(
            TAN_CONCENTRATION_UNAVAILABLE, full_context_report["status_labels"]
        )

    def test_suppresses_nh3_risk_label_only_with_ph_and_temperature_context(self) -> None:
        partial_context_report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            ph_context_available=True,
        )
        full_context_report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            ph_context_available=True,
            temperature_context_available=True,
        )

        self.assertIn(NH3_RISK_UNAVAILABLE, partial_context_report["status_labels"])
        self.assertNotIn(NH3_RISK_UNAVAILABLE, full_context_report["status_labels"])

    def test_rejects_missing_scenario_id(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError, "scenario_id is required"
        ):
            build_mode_a_feed_load_report(
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=0.32,
            )

    def test_rejects_unsupported_input_mode(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            "input_mode must be 'mode_a_direct_feed'",
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a",
                input_mode="mode_b_biomass_derived",
                feed_kg_day=1.0,
                protein_fraction=0.32,
            )

    def test_wraps_invalid_feed_and_protein_validation(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError, "feed_kg_day must be non-negative"
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a",
                input_mode=INPUT_MODE,
                feed_kg_day=-0.1,
                protein_fraction=0.32,
            )

        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            "protein_fraction must be between 0 and 1 inclusive",
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a",
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=1.01,
            )

    def test_optional_context_is_echoed_without_changing_calculations(self) -> None:
        baseline = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )
        with_context = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            feed_class="growout",
            protein_basis="demo feed label",
            feeding_frequency_per_day=2,
            fcr_band=[1.5, 1.8],
            architecture_context="dwc_raft_context_only",
            water_volume_context_available=True,
            time_basis_context_available=True,
            exchange_or_retention_context_available=True,
            ph_context_available=True,
            temperature_context_available=True,
            feed_price_context_available=True,
            tank_volume_context_available=True,
            stocking_density_context_available=True,
            biofilter_capacity_context_available=True,
        )

        self.assertEqual(with_context["loads"], baseline["loads"])
        self.assertEqual(with_context["optional_context"]["feed_class"], "growout")
        self.assertEqual(
            with_context["optional_context"]["protein_basis"], "demo feed label"
        )
        self.assertEqual(with_context["optional_context"]["feeding_frequency_per_day"], 2)
        self.assertEqual(with_context["optional_context"]["fcr_band"], [1.5, 1.8])
        self.assertEqual(
            with_context["optional_context"]["architecture_context"],
            "dwc_raft_context_only",
        )

    def test_does_not_populate_basil_saleable_output_as_a_number(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

        self.assertNotIn("saleable_harvest_mass_kg", report)
        self.assertIn(BASIL_SALEABLE_OUTPUT_UNRESOLVED, report["status_labels"])

    def test_load_only_report_does_not_include_water_quality_context(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

        self.assertNotIn("water_quality_context", report)
        self.assertIn(TAN_CONCENTRATION_UNAVAILABLE, report["status_labels"])
        self.assertIn(NH3_RISK_UNAVAILABLE, report["status_labels"])
        self.assertNotIn("aeration_solids_context", report)

    def test_report_includes_water_quality_context_with_complete_p1_inputs(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope="fish_tank",
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        water_quality = report["water_quality_context"]
        self.assertEqual(water_quality["concentration_scope"], "fish_tank")
        self.assertEqual(
            water_quality["concentration_assumption"], "upper_bound_no_removal"
        )
        self.assertEqual(water_quality["effective_water_volume_l"], 7800.0)
        self.assertEqual(water_quality["accumulation_period_day"], 1.0)
        self.assertEqual(water_quality["ph"], 7.0)
        self.assertEqual(water_quality["water_temp_c"], 28.0)
        self.assertIs(water_quality["freshwater_assumption"], True)
        self.assertEqual(
            water_quality["unit_basis"]["estimated_tan_n_mg_l"], "mg TAN-N/L"
        )

    def test_report_uses_existing_tan_n_load_output_for_p1_concentration(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope="fish_tank",
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        expected_concentration = report["loads"]["tan_n_load_g_day"] * 1000.0 / 7800.0
        self.assertAlmostEqual(
            report["water_quality_context"]["estimated_tan_n_mg_l"],
            expected_concentration,
        )

    def test_report_returns_expected_example_p1_values(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope="fish_tank",
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        water_quality = report["water_quality_context"]
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

    def test_p1_context_suppresses_only_water_quality_missing_labels(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope="fish_tank",
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        labels = set(report["status_labels"])
        self.assertNotIn(TAN_CONCENTRATION_UNAVAILABLE, labels)
        self.assertNotIn(NH3_RISK_UNAVAILABLE, labels)
        self.assertIn(FEED_COST_UNAVAILABLE, labels)
        self.assertIn(TANK_SUITABILITY_UNAVAILABLE, labels)
        self.assertIn(BIOFILTER_REMOVAL_UNAVAILABLE, labels)
        self.assertIn(BASIL_SALEABLE_OUTPUT_UNRESOLVED, labels)
        self.assertNotIn("aeration_solids_context", report)

    def test_rejects_partial_p1_inputs(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            (
                "partial P1 water-quality input group; missing field\\(s\\): "
                "accumulation_period_day, concentration_scope, ph, water_temp_c, "
                "freshwater_assumption"
            ),
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a_p1",
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=0.32,
                effective_water_volume_l=7800,
            )

    def test_rejects_invalid_p1_inputs(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            "concentration_scope must be 'fish_tank'",
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a_p1",
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=0.32,
                effective_water_volume_l=7800,
                accumulation_period_day=1,
                concentration_scope="system_average",
                ph=7.0,
                water_temp_c=28.0,
                freshwater_assumption=True,
            )

        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            "freshwater_assumption must be true for this first helper",
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a_p1",
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=0.32,
                effective_water_volume_l=7800,
                accumulation_period_day=1,
                concentration_scope="fish_tank",
                ph=7.0,
                water_temp_c=28.0,
                freshwater_assumption=False,
            )

    def test_report_does_not_include_aeration_solids_context_without_p1_5_inputs(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

        self.assertNotIn("aeration_solids_context", report)

    def test_report_includes_aeration_solids_context_when_requested(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            include_aeration_solids_context=True,
        )

        self.assertIn("aeration_solids_context", report)
        self.assertEqual(
            set(report["aeration_solids_context"]),
            {
                "oxygen_context",
                "aeration_context",
                "dwc_root_zone_context",
                "solids_context",
                "status_labels",
                "boundary_notes",
            },
        )

    def test_report_includes_aeration_solids_context_when_p1_5_input_supplied(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            measured_do_mg_l=5.0,
        )

        self.assertIn("aeration_solids_context", report)
        self.assertEqual(
            report["aeration_solids_context"]["aeration_context"][
                "measured_do_mg_l"
            ],
            5.0,
        )

    def test_aeration_solids_context_uses_existing_load_and_feed_inputs(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            include_aeration_solids_context=True,
            dry_solids_coefficient=0.25,
        )

        context = report["aeration_solids_context"]
        self.assertEqual(
            context["oxygen_context"]["nitrification_oxygen_demand_g_day"],
            report["loads"]["oxygen_demand_g_day"],
        )
        self.assertEqual(context["solids_context"]["feed_kg_day"], report["inputs"]["feed_kg_day"])
        self.assertAlmostEqual(
            context["solids_context"]["estimated_dry_solids_potential_kg_day"],
            0.25,
        )

    def test_aeration_solids_echoes_measured_do_without_safe_unsafe_label(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            measured_do_mg_l=5.0,
        )

        context = report["aeration_solids_context"]
        self.assertEqual(context["aeration_context"]["measured_do_mg_l"], 5.0)
        self.assertFalse(_contains_key(context, "safe"))
        self.assertFalse(_contains_key(context, "unsafe"))

    def test_p1_5_labels_stay_inside_aeration_solids_context(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            include_aeration_solids_context=True,
        )

        section_labels = set(report["aeration_solids_context"]["status_labels"])
        self.assertIn("total_oxygen_demand_unavailable", section_labels)
        self.assertIn(
            "aeration_capacity_unavailable_without_equipment_and_transfer_basis",
            section_labels,
        )
        self.assertNotIn(
            "total_oxygen_demand_unavailable",
            report["status_labels"],
        )
        self.assertNotIn(
            "aeration_capacity_unavailable_without_equipment_and_transfer_basis",
            report["status_labels"],
        )

    def test_rejects_invalid_p1_5_inputs(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            "measured_do_mg_l must be non-negative",
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a_p1_5",
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=0.32,
                measured_do_mg_l=-0.1,
            )

        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            "include_aeration_solids_context must be a boolean",
        ):
            build_mode_a_feed_load_report(
                scenario_id="demo_mode_a_p1_5",
                input_mode=INPUT_MODE,
                feed_kg_day=1.0,
                protein_fraction=0.32,
                include_aeration_solids_context="yes",  # type: ignore[arg-type]
            )

    def test_p1_and_p1_5_contexts_can_coexist(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope="fish_tank",
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
            include_aeration_solids_context=True,
            measured_do_mg_l=5.0,
            dry_solids_coefficient=0.25,
            dry_solids_basis="demo_scenario_input_not_canon",
        )

        self.assertIn("water_quality_context", report)
        self.assertIn("aeration_solids_context", report)
        self.assertEqual(
            report["optional_context"]["dry_solids_basis"],
            "demo_scenario_input_not_canon",
        )
        self.assertAlmostEqual(
            report["aeration_solids_context"]["solids_context"][
                "estimated_dry_solids_potential_kg_day"
            ],
            0.25,
        )

    def test_disallowed_calculated_fields_are_not_output_keys(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

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

    def test_p1_5_disallowed_calculated_fields_are_not_output_keys(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p1_5",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            include_aeration_solids_context=True,
            measured_do_mg_l=5.0,
            dry_solids_coefficient=0.25,
        )

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
