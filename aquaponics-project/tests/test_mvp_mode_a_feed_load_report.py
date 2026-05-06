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
from src.mvp_operating_cost_pressure import (
    FEED_PRICE_MISSING,
    MIXED_CURRENCY_SUBTOTAL_UNAVAILABLE,
    POWER_COST_USES_NAMEPLATE_KW,
    SELECTED_COST_PRESSURE_ONLY,
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

    def test_report_does_not_include_operating_cost_pressure_without_p2a_inputs(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
        )

        self.assertNotIn("operating_cost_pressure", report)

    def test_report_includes_operating_cost_pressure_when_requested(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p2a",
            input_mode=INPUT_MODE,
            feed_kg_day=1.0,
            protein_fraction=0.32,
            include_operating_cost_pressure=True,
        )

        self.assertIn("operating_cost_pressure", report)
        cost_context = report["operating_cost_pressure"]
        self.assertEqual(
            set(cost_context),
            {
                "cost_inputs",
                "cost_outputs",
                "cost_basis",
                "cost_status_labels",
                "cost_boundary_notes",
            },
        )
        self.assertEqual(cost_context["cost_outputs"]["supplied_categories"], [])
        self.assertIsNone(
            cost_context["cost_outputs"][
                "selected_operating_cost_pressure_subtotal"
            ]
        )
        self.assertIn(FEED_PRICE_MISSING, cost_context["cost_status_labels"])
        self.assertIn(
            "electricity_tariff_missing", cost_context["cost_status_labels"]
        )
        self.assertIn(
            "equipment_power_or_runtime_missing",
            cost_context["cost_status_labels"],
        )

    def test_report_includes_operating_cost_pressure_with_feed_cost_inputs(self) -> None:
        report = _p2a_base_report(**_feed_cost_inputs())

        cost_context = report["operating_cost_pressure"]
        self.assertEqual(
            cost_context["cost_inputs"]["feed"]["feed_kg_day"],
            report["inputs"]["feed_kg_day"],
        )
        self.assertAlmostEqual(
            cost_context["cost_outputs"]["category_costs"]["feed"][
                "scenario_feed_cost_per_day"
            ],
            45.0,
        )
        self.assertEqual(
            cost_context["cost_outputs"]["selected_operating_cost_pressure_subtotal"],
            45.0,
        )
        self.assertNotIn(FEED_COST_UNAVAILABLE, report["status_labels"])

    def test_report_includes_operating_cost_pressure_with_power_cost_inputs(self) -> None:
        report = _p2a_base_report(**_power_cost_inputs())

        power_outputs = report["operating_cost_pressure"]["cost_outputs"][
            "category_costs"
        ]["power"]
        self.assertAlmostEqual(power_outputs["equipment"][0]["device_kwh_day"], 4.8)
        self.assertAlmostEqual(power_outputs["equipment"][1]["device_kwh_day"], 2.4)
        self.assertAlmostEqual(power_outputs["scenario_power_kwh_day"], 7.2)
        self.assertAlmostEqual(power_outputs["scenario_power_cost_per_day"], 54.0)
        self.assertEqual(
            report["operating_cost_pressure"]["cost_outputs"][
                "selected_operating_cost_pressure_subtotal"
            ],
            54.0,
        )
        self.assertIn(FEED_COST_UNAVAILABLE, report["status_labels"])

    def test_report_returns_expected_combined_p2a_values(self) -> None:
        report = _p2a_base_report(**_feed_cost_inputs(), **_power_cost_inputs())

        cost_context = report["operating_cost_pressure"]
        category_costs = cost_context["cost_outputs"]["category_costs"]
        self.assertAlmostEqual(
            category_costs["feed"]["scenario_feed_cost_per_day"], 45.0
        )
        self.assertAlmostEqual(
            category_costs["power"]["equipment"][0]["device_kwh_day"], 4.8
        )
        self.assertAlmostEqual(
            category_costs["power"]["equipment"][1]["device_kwh_day"], 2.4
        )
        self.assertAlmostEqual(
            category_costs["power"]["scenario_power_kwh_day"], 7.2
        )
        self.assertAlmostEqual(
            category_costs["power"]["scenario_power_cost_per_day"], 54.0
        )
        self.assertAlmostEqual(
            cost_context["cost_outputs"][
                "selected_operating_cost_pressure_subtotal"
            ],
            99.0,
        )
        self.assertIn(
            POWER_COST_USES_NAMEPLATE_KW,
            cost_context["cost_status_labels"],
        )

    def test_report_rejects_partial_feed_cost_input_group(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            (
                "partial P2a feed-cost input group; missing field\\(s\\): "
                "feed_price_currency, feed_price_date, feed_price_geography, "
                "feed_price_source_type"
            ),
        ):
            _p2a_base_report(feed_price_per_kg=45.0)

    def test_report_rejects_partial_power_cost_input_group(self) -> None:
        with self.assertRaisesRegex(
            ModeAFeedLoadReportValidationError,
            (
                "partial P2a power-cost input group; missing field\\(s\\): "
                "electricity_price_currency, electricity_tariff_date, "
                "electricity_price_geography, electricity_tariff_class, "
                "electricity_tariff_source_type"
            ),
        ):
            _p2a_base_report(
                equipment_power_records=_power_cost_inputs()[
                    "equipment_power_records"
                ],
                electricity_price_per_kwh=7.5,
            )

    def test_report_handles_mixed_p2a_currencies_without_subtotal(self) -> None:
        feed_inputs = _feed_cost_inputs()
        power_inputs = _power_cost_inputs()
        power_inputs["electricity_price_currency"] = "USD"

        report = _p2a_base_report(**feed_inputs, **power_inputs)
        cost_context = report["operating_cost_pressure"]

        self.assertIsNone(
            cost_context["cost_outputs"][
                "selected_operating_cost_pressure_subtotal"
            ]
        )
        self.assertIn(
            MIXED_CURRENCY_SUBTOTAL_UNAVAILABLE,
            cost_context["cost_status_labels"],
        )

    def test_p2a_labels_stay_inside_operating_cost_pressure(self) -> None:
        report = _p2a_base_report(**_feed_cost_inputs(), **_power_cost_inputs())

        cost_labels = report["operating_cost_pressure"]["cost_status_labels"]
        self.assertIn(SELECTED_COST_PRESSURE_ONLY, cost_labels)
        self.assertIn(POWER_COST_USES_NAMEPLATE_KW, cost_labels)
        self.assertNotIn(SELECTED_COST_PRESSURE_ONLY, report["status_labels"])
        self.assertNotIn(POWER_COST_USES_NAMEPLATE_KW, report["status_labels"])

    def test_p2a_can_coexist_with_p1_and_p1_5_contexts(self) -> None:
        report = build_mode_a_feed_load_report(
            scenario_id="demo_mode_a_p2a",
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
            **_feed_cost_inputs(),
            **_power_cost_inputs(),
        )

        self.assertIn("water_quality_context", report)
        self.assertIn("aeration_solids_context", report)
        self.assertIn("operating_cost_pressure", report)
        self.assertAlmostEqual(
            report["operating_cost_pressure"]["cost_outputs"][
                "selected_operating_cost_pressure_subtotal"
            ],
            99.0,
        )

    def test_p2a_disallowed_calculated_fields_are_not_output_keys(self) -> None:
        report = _p2a_base_report(**_feed_cost_inputs(), **_power_cost_inputs())

        for disallowed_key in {
            "saleable_harvest_mass_kg",
            "total_operating_cost",
            "profitability",
            "revenue",
            "gross_margin",
            "contribution_margin",
            "roi",
            "payback",
            "break_even",
            "economic_viability",
            "fish_revenue",
            "basil_revenue",
            "crop_revenue",
        }:
            self.assertFalse(_contains_key(report, disallowed_key), disallowed_key)

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


def _p2a_base_report(**kwargs: object) -> dict:
    return build_mode_a_feed_load_report(
        scenario_id="demo_mode_a_p2a",
        input_mode=INPUT_MODE,
        feed_kg_day=1.0,
        protein_fraction=0.32,
        **kwargs,
    )


def _feed_cost_inputs() -> dict:
    return {
        "feed_price_per_kg": 45.0,
        "feed_price_currency": "INR",
        "feed_price_date": "2026-05-06",
        "feed_price_geography": "India scenario",
        "feed_price_source_type": "demo_scenario_input",
    }


def _power_cost_inputs() -> dict:
    return {
        "equipment_power_records": [
            {
                "device_id": "demo_pump",
                "device_role": "water_circulation",
                "device_kw": 0.2,
                "runtime_h_day": 24,
                "load_fraction": 1.0,
                "power_basis": "nameplate_kw",
            },
            {
                "device_id": "demo_blower",
                "device_role": "aeration",
                "device_kw": 0.1,
                "runtime_h_day": 24,
                "load_fraction": 1.0,
                "power_basis": "nameplate_kw",
            },
        ],
        "electricity_price_per_kwh": 7.5,
        "electricity_price_currency": "INR",
        "electricity_tariff_date": "2026-05-06",
        "electricity_price_geography": "India scenario",
        "electricity_tariff_class": "demo_scenario_input",
        "electricity_tariff_source_type": "demo_scenario_input",
    }


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
