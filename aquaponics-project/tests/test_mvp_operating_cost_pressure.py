import unittest

from src.mvp_operating_cost_pressure import (
    MIXED_CURRENCY_SUBTOTAL_UNAVAILABLE,
    NOT_CANON_NOT_MARKET_TRUTH,
    NOT_PROFITABILITY,
    POWER_COST_USES_NAMEPLATE_KW,
    REVENUE_INPUTS_MISSING,
    SCENARIO_ESTIMATE,
    SELECTED_COST_PRESSURE_ONLY,
    OperatingCostPressureValidationError,
    build_operating_cost_pressure,
    calculate_feed_cost_pressure,
    calculate_power_cost_pressure,
)


class MvpOperatingCostPressureTests(unittest.TestCase):
    def test_feed_cost_uses_feed_times_price(self) -> None:
        result = calculate_feed_cost_pressure(**feed_inputs())

        self.assertEqual(
            result["cost_outputs"]["scenario_feed_cost_per_day"],
            45.0,
        )
        self.assertEqual(result["cost_outputs"]["currency"], "INR")

    def test_feed_cost_requires_money_metadata(self) -> None:
        inputs = feed_inputs()
        inputs["feed_price_currency"] = ""

        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "feed_price_currency must be non-empty",
        ):
            calculate_feed_cost_pressure(**inputs)

        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "feed_price_date is required",
        ):
            build_operating_cost_pressure(
                feed_kg_day=1.0,
                feed_price_per_kg=45.0,
                feed_price_currency="INR",
                feed_price_geography="India scenario",
                feed_price_source_type="demo_scenario_input",
            )

    def test_feed_cost_output_is_labeled_as_scenario_not_canon_not_profitability(self) -> None:
        result = calculate_feed_cost_pressure(**feed_inputs())

        labels = set(result["cost_status_labels"])
        self.assertIn(SCENARIO_ESTIMATE, labels)
        self.assertIn(NOT_CANON_NOT_MARKET_TRUTH, labels)
        self.assertIn(NOT_PROFITABILITY, labels)
        self.assertIn(SELECTED_COST_PRESSURE_ONLY, labels)
        self.assertIn(REVENUE_INPUTS_MISSING, labels)

    def test_power_kwh_uses_power_runtime_and_load_fraction(self) -> None:
        result = calculate_power_cost_pressure(
            equipment_records=[
                equipment_record(
                    device_id="pump",
                    device_kw=0.2,
                    runtime_h_day=12,
                    load_fraction=0.5,
                    power_basis="measured_kw",
                )
            ],
            **electricity_inputs(),
        )

        device = result["cost_outputs"]["equipment"][0]
        self.assertAlmostEqual(device["device_kwh_day"], 1.2)

    def test_power_cost_uses_kwh_and_tariff(self) -> None:
        result = calculate_power_cost_pressure(
            equipment_records=[
                equipment_record(
                    device_id="pump",
                    device_kw=0.2,
                    runtime_h_day=24,
                    load_fraction=1.0,
                    power_basis="measured_kw",
                )
            ],
            **electricity_inputs(),
        )

        self.assertAlmostEqual(result["cost_outputs"]["scenario_power_kwh_day"], 4.8)
        self.assertAlmostEqual(
            result["cost_outputs"]["scenario_power_cost_per_day"], 36.0
        )

    def test_multiple_equipment_records_sum_correctly(self) -> None:
        result = calculate_power_cost_pressure(
            equipment_records=[
                equipment_record(device_id="pump", device_kw=0.2),
                equipment_record(device_id="blower", device_kw=0.1),
            ],
            **electricity_inputs(),
        )

        self.assertAlmostEqual(result["cost_outputs"]["scenario_power_kwh_day"], 7.2)
        self.assertAlmostEqual(
            result["cost_outputs"]["scenario_power_cost_per_day"], 54.0
        )

    def test_nameplate_power_basis_emits_uncertainty_label(self) -> None:
        result = calculate_power_cost_pressure(
            equipment_records=[
                equipment_record(power_basis="nameplate_kw"),
            ],
            **electricity_inputs(),
        )

        self.assertIn(POWER_COST_USES_NAMEPLATE_KW, result["cost_status_labels"])

    def test_measured_power_basis_does_not_emit_nameplate_uncertainty_label(self) -> None:
        result = calculate_power_cost_pressure(
            equipment_records=[
                equipment_record(power_basis="measured_kw"),
            ],
            **electricity_inputs(),
        )

        self.assertNotIn(POWER_COST_USES_NAMEPLATE_KW, result["cost_status_labels"])

    def test_combined_helper_calculates_selected_subtotal_when_currencies_match(self) -> None:
        result = build_operating_cost_pressure(
            **feed_inputs(),
            equipment_records=[
                equipment_record(device_id="pump", device_kw=0.2),
                equipment_record(device_id="blower", device_kw=0.1),
            ],
            **electricity_inputs(),
        )

        self.assertAlmostEqual(
            result["cost_outputs"]["selected_operating_cost_pressure_subtotal"],
            99.0,
        )
        self.assertEqual(
            result["cost_outputs"]["selected_operating_cost_pressure_currency"],
            "INR",
        )
        self.assertIn("feed", result["cost_outputs"]["supplied_categories"])
        self.assertIn("power", result["cost_outputs"]["supplied_categories"])

    def test_combined_helper_does_not_output_total_operating_cost(self) -> None:
        result = build_operating_cost_pressure(**feed_inputs())

        self.assertFalse(_contains_key(result, "total_operating_cost"))

    def test_mixed_currencies_do_not_produce_subtotal(self) -> None:
        electricity = electricity_inputs()
        electricity["electricity_price_currency"] = "EUR"

        result = build_operating_cost_pressure(
            **feed_inputs(),
            equipment_records=[equipment_record()],
            **electricity,
        )

        self.assertIsNone(
            result["cost_outputs"]["selected_operating_cost_pressure_subtotal"]
        )
        self.assertIsNone(
            result["cost_outputs"]["selected_operating_cost_pressure_currency"]
        )
        self.assertIn(
            MIXED_CURRENCY_SUBTOTAL_UNAVAILABLE,
            result["cost_status_labels"],
        )

    def test_rejects_negative_feed_price(self) -> None:
        inputs = feed_inputs()
        inputs["feed_price_per_kg"] = -1.0

        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "feed_price_per_kg must be non-negative",
        ):
            calculate_feed_cost_pressure(**inputs)

    def test_rejects_runtime_over_24_hours(self) -> None:
        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "runtime_h_day must be <= 24",
        ):
            calculate_power_cost_pressure(
                equipment_records=[equipment_record(runtime_h_day=24.1)],
                **electricity_inputs(),
            )

    def test_rejects_invalid_load_fraction(self) -> None:
        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "load_fraction must be between 0 and 1 inclusive",
        ):
            calculate_power_cost_pressure(
                equipment_records=[equipment_record(load_fraction=1.01)],
                **electricity_inputs(),
            )

    def test_rejects_unsupported_power_basis(self) -> None:
        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "power_basis must be one of",
        ):
            calculate_power_cost_pressure(
                equipment_records=[
                    equipment_record(power_basis="estimated_kw"),
                ],
                **electricity_inputs(),
            )

    def test_power_cost_requires_tariff_metadata(self) -> None:
        tariff = electricity_inputs()
        tariff["electricity_tariff_class"] = ""

        with self.assertRaisesRegex(
            OperatingCostPressureValidationError,
            "electricity_tariff_class must be non-empty",
        ):
            calculate_power_cost_pressure(
                equipment_records=[equipment_record()],
                **tariff,
            )

    def test_feed_only_output_does_not_mark_electricity_missing(self) -> None:
        result = build_operating_cost_pressure(**feed_inputs())

        labels = set(result["cost_status_labels"])
        self.assertNotIn("electricity_tariff_missing", labels)
        self.assertNotIn("equipment_power_or_runtime_missing", labels)
        self.assertEqual(result["cost_outputs"]["supplied_categories"], ["feed"])

    def test_electricity_only_output_does_not_mark_feed_missing(self) -> None:
        result = build_operating_cost_pressure(
            equipment_records=[equipment_record()],
            **electricity_inputs(),
        )

        labels = set(result["cost_status_labels"])
        self.assertNotIn("feed_price_missing", labels)
        self.assertNotIn("feed_price_metadata_incomplete", labels)
        self.assertEqual(result["cost_outputs"]["supplied_categories"], ["power"])

    def test_direct_helper_example(self) -> None:
        result = build_operating_cost_pressure(
            **feed_inputs(),
            equipment_records=[
                equipment_record(device_id="pump", device_role="pump", device_kw=0.2),
                equipment_record(
                    device_id="blower", device_role="blower", device_kw=0.1
                ),
            ],
            **electricity_inputs(),
        )

        feed = result["cost_outputs"]["category_costs"]["feed"]
        power = result["cost_outputs"]["category_costs"]["power"]
        equipment = power["equipment"]

        self.assertEqual(feed["scenario_feed_cost_per_day"], 45.0)
        self.assertAlmostEqual(equipment[0]["device_kwh_day"], 4.8)
        self.assertAlmostEqual(equipment[1]["device_kwh_day"], 2.4)
        self.assertAlmostEqual(power["scenario_power_kwh_day"], 7.2)
        self.assertAlmostEqual(power["scenario_power_cost_per_day"], 54.0)
        self.assertAlmostEqual(
            result["cost_outputs"]["selected_operating_cost_pressure_subtotal"],
            99.0,
        )
        self.assertIn(POWER_COST_USES_NAMEPLATE_KW, result["cost_status_labels"])
        self.assertIn(SELECTED_COST_PRESSURE_ONLY, result["cost_status_labels"])
        self.assertIn(NOT_PROFITABILITY, result["cost_status_labels"])

    def test_output_does_not_include_disallowed_calculated_field_keys(self) -> None:
        result = build_operating_cost_pressure(
            **feed_inputs(),
            equipment_records=[equipment_record()],
            **electricity_inputs(),
        )

        for disallowed_key in DISALLOWED_OUTPUT_KEYS:
            self.assertFalse(_contains_key(result, disallowed_key), disallowed_key)


def feed_inputs() -> dict:
    return {
        "feed_kg_day": 1.0,
        "feed_price_per_kg": 45.0,
        "feed_price_currency": "INR",
        "feed_price_date": "2026-05-06",
        "feed_price_geography": "India scenario",
        "feed_price_source_type": "demo_scenario_input",
        "feed_class": "grow_out",
        "protein_percentage": 32.0,
        "package_size_kg": 20.0,
        "feed_price_source_reference": "demo_input",
    }


def electricity_inputs() -> dict:
    return {
        "electricity_price_per_kwh": 7.5,
        "electricity_price_currency": "INR",
        "electricity_tariff_date": "2026-05-06",
        "electricity_tariff_class": "demo_scenario_input",
        "electricity_tariff_source_type": "demo_scenario_input",
        "electricity_price_geography": "India scenario",
        "electricity_tariff_source_reference": "demo_input",
    }


def equipment_record(
    *,
    device_id: str = "pump",
    device_role: str = "pump",
    device_kw: float = 0.2,
    runtime_h_day: float = 24,
    load_fraction: float = 1.0,
    power_basis: str = "nameplate_kw",
) -> dict:
    return {
        "device_id": device_id,
        "device_role": device_role,
        "device_kw": device_kw,
        "runtime_h_day": runtime_h_day,
        "load_fraction": load_fraction,
        "power_basis": power_basis,
    }


DISALLOWED_OUTPUT_KEYS = {
    "profitability",
    "profit",
    "revenue",
    "gross_margin",
    "contribution_margin",
    "roi",
    "ROI",
    "payback",
    "break_even",
    "economic_viability",
    "fish_revenue",
    "basil_revenue",
    "crop_revenue",
    "saleable_harvest_mass_kg",
    "total_operating_cost",
    "buffer_cost",
    "water_cost",
    "labor_cost",
    "backup_power_cost",
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
