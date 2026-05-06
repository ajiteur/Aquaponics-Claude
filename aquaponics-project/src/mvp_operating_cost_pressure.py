"""Isolated P2a operating-cost pressure helper."""

from __future__ import annotations

import math
from numbers import Real
from typing import Any


FEED_PRICE_MISSING = "feed_price_missing"
FEED_PRICE_METADATA_INCOMPLETE = "feed_price_metadata_incomplete"
ELECTRICITY_TARIFF_MISSING = "electricity_tariff_missing"
ELECTRICITY_TARIFF_METADATA_INCOMPLETE = (
    "electricity_tariff_metadata_incomplete"
)
EQUIPMENT_POWER_OR_RUNTIME_MISSING = "equipment_power_or_runtime_missing"
POWER_COST_USES_NAMEPLATE_KW = "power_cost_uses_nameplate_kw_not_measured_kw"
SELECTED_COST_PRESSURE_ONLY = (
    "selected_cost_pressure_only_not_total_operating_cost"
)
MIXED_CURRENCY_SUBTOTAL_UNAVAILABLE = (
    "selected_cost_pressure_subtotal_unavailable_due_to_mixed_currencies"
)
REVENUE_INPUTS_MISSING = "revenue_inputs_missing_profitability_blocked"
NOT_CANON_NOT_MARKET_TRUTH = "not_canon_not_market_truth"
SCENARIO_ESTIMATE = "scenario_estimate"
NOT_PROFITABILITY = "not_profitability"

ALLOWED_POWER_BASIS = {"measured_kw", "nameplate_kw"}


class OperatingCostPressureValidationError(ValueError):
    """Raised when operating-cost pressure inputs are invalid."""


def calculate_feed_cost_pressure(
    *,
    feed_kg_day: float,
    feed_price_per_kg: float,
    feed_price_currency: str,
    feed_price_date: str,
    feed_price_geography: str,
    feed_price_source_type: str,
    feed_class: Any | None = None,
    protein_percentage: float | None = None,
    package_size_kg: float | None = None,
    feed_price_source_reference: Any | None = None,
) -> dict[str, Any]:
    """Calculate scenario daily feed-cost pressure from explicit inputs."""

    validated_feed_kg_day = _validate_non_negative_number(
        "feed_kg_day", feed_kg_day
    )
    validated_feed_price_per_kg = _validate_non_negative_number(
        "feed_price_per_kg", feed_price_per_kg
    )
    validated_currency = _validate_required_string(
        "feed_price_currency", feed_price_currency
    )
    validated_date = _validate_required_string("feed_price_date", feed_price_date)
    validated_geography = _validate_required_string(
        "feed_price_geography", feed_price_geography
    )
    validated_source_type = _validate_required_string(
        "feed_price_source_type", feed_price_source_type
    )
    validated_protein_percentage = _validate_optional_non_negative_number(
        "protein_percentage", protein_percentage
    )
    validated_package_size_kg = _validate_optional_non_negative_number(
        "package_size_kg", package_size_kg
    )

    scenario_feed_cost_per_day = _clean_float(
        validated_feed_kg_day * validated_feed_price_per_kg
    )

    return {
        "cost_category": "feed",
        "cost_inputs": {
            "feed_kg_day": validated_feed_kg_day,
            "feed_price_per_kg": validated_feed_price_per_kg,
            "feed_price_currency": validated_currency,
            "feed_price_date": validated_date,
            "feed_price_geography": validated_geography,
            "feed_price_source_type": validated_source_type,
            "feed_class": feed_class,
            "protein_percentage": validated_protein_percentage,
            "package_size_kg": validated_package_size_kg,
            "feed_price_source_reference": feed_price_source_reference,
        },
        "cost_outputs": {
            "scenario_feed_cost_per_day": scenario_feed_cost_per_day,
            "currency": validated_currency,
        },
        "cost_basis": {
            "formula": "feed_kg_day * feed_price_per_kg",
            "quantity_basis": "kg feed/day",
            "price_basis": "scenario currency/kg feed",
            "output_basis": "scenario currency/day",
        },
        "cost_status_labels": _base_status_labels(),
        "cost_boundary_notes": _boundary_notes(),
    }


def calculate_power_cost_pressure(
    *,
    equipment_records: list[dict[str, Any]],
    electricity_price_per_kwh: float,
    electricity_price_currency: str,
    electricity_tariff_date: str,
    electricity_price_geography: str,
    electricity_tariff_class: str,
    electricity_tariff_source_type: str,
    electricity_tariff_source_reference: Any | None = None,
) -> dict[str, Any]:
    """Calculate scenario daily equipment electricity-cost pressure."""

    validated_equipment_records = _validate_equipment_records(equipment_records)
    validated_electricity_price = _validate_non_negative_number(
        "electricity_price_per_kwh", electricity_price_per_kwh
    )
    validated_currency = _validate_required_string(
        "electricity_price_currency", electricity_price_currency
    )
    validated_tariff_date = _validate_required_string(
        "electricity_tariff_date", electricity_tariff_date
    )
    validated_geography = _validate_required_string(
        "electricity_price_geography", electricity_price_geography
    )
    validated_tariff_class = _validate_required_string(
        "electricity_tariff_class", electricity_tariff_class
    )
    validated_source_type = _validate_required_string(
        "electricity_tariff_source_type", electricity_tariff_source_type
    )

    device_outputs = []
    scenario_power_kwh_day = 0.0
    scenario_power_cost_per_day = 0.0
    uses_nameplate_kw = False

    for record in validated_equipment_records:
        device_kwh_day = _clean_float(
            record["device_kw"] * record["runtime_h_day"] * record["load_fraction"]
        )
        scenario_device_power_cost_per_day = _clean_float(
            device_kwh_day * validated_electricity_price
        )
        scenario_power_kwh_day = _clean_float(
            scenario_power_kwh_day + device_kwh_day
        )
        scenario_power_cost_per_day = _clean_float(
            scenario_power_cost_per_day + scenario_device_power_cost_per_day
        )
        uses_nameplate_kw = (
            uses_nameplate_kw or record["power_basis"] == "nameplate_kw"
        )
        device_outputs.append(
            {
                "device_id": record["device_id"],
                "device_role": record["device_role"],
                "device_kw": record["device_kw"],
                "runtime_h_day": record["runtime_h_day"],
                "load_fraction": record["load_fraction"],
                "power_basis": record["power_basis"],
                "device_kwh_day": device_kwh_day,
                "scenario_device_power_cost_per_day": (
                    scenario_device_power_cost_per_day
                ),
                "currency": validated_currency,
            }
        )

    labels = _base_status_labels()
    if uses_nameplate_kw:
        labels.append(POWER_COST_USES_NAMEPLATE_KW)

    return {
        "cost_category": "power",
        "cost_inputs": {
            "equipment_records": validated_equipment_records,
            "electricity_price_per_kwh": validated_electricity_price,
            "electricity_price_currency": validated_currency,
            "electricity_tariff_date": validated_tariff_date,
            "electricity_price_geography": validated_geography,
            "electricity_tariff_class": validated_tariff_class,
            "electricity_tariff_source_type": validated_source_type,
            "electricity_tariff_source_reference": (
                electricity_tariff_source_reference
            ),
        },
        "cost_outputs": {
            "equipment": device_outputs,
            "scenario_power_kwh_day": scenario_power_kwh_day,
            "scenario_power_cost_per_day": scenario_power_cost_per_day,
            "currency": validated_currency,
        },
        "cost_basis": {
            "kwh_formula": "sum(device_kw * runtime_h_day * load_fraction)",
            "cost_formula": "scenario_power_kwh_day * electricity_price_per_kwh",
            "power_basis": "measured_kw preferred; nameplate_kw flagged",
            "output_basis": "scenario currency/day",
        },
        "cost_status_labels": labels,
        "cost_boundary_notes": _boundary_notes(),
    }


def build_operating_cost_pressure(
    *,
    feed_kg_day: float | None = None,
    feed_price_per_kg: float | None = None,
    feed_price_currency: str | None = None,
    feed_price_date: str | None = None,
    feed_price_geography: str | None = None,
    feed_price_source_type: str | None = None,
    feed_class: Any | None = None,
    protein_percentage: float | None = None,
    package_size_kg: float | None = None,
    feed_price_source_reference: Any | None = None,
    equipment_records: list[dict[str, Any]] | None = None,
    electricity_price_per_kwh: float | None = None,
    electricity_price_currency: str | None = None,
    electricity_tariff_date: str | None = None,
    electricity_price_geography: str | None = None,
    electricity_tariff_class: str | None = None,
    electricity_tariff_source_type: str | None = None,
    electricity_tariff_source_reference: Any | None = None,
) -> dict[str, Any]:
    """Build selected operating-cost pressure from supplied categories."""

    feed_requested = _feed_inputs_supplied(
        feed_kg_day=feed_kg_day,
        feed_price_per_kg=feed_price_per_kg,
        feed_price_currency=feed_price_currency,
        feed_price_date=feed_price_date,
        feed_price_geography=feed_price_geography,
        feed_price_source_type=feed_price_source_type,
        feed_class=feed_class,
        protein_percentage=protein_percentage,
        package_size_kg=package_size_kg,
        feed_price_source_reference=feed_price_source_reference,
    )
    power_requested = _power_inputs_supplied(
        equipment_records=equipment_records,
        electricity_price_per_kwh=electricity_price_per_kwh,
        electricity_price_currency=electricity_price_currency,
        electricity_tariff_date=electricity_tariff_date,
        electricity_price_geography=electricity_price_geography,
        electricity_tariff_class=electricity_tariff_class,
        electricity_tariff_source_type=electricity_tariff_source_type,
        electricity_tariff_source_reference=electricity_tariff_source_reference,
    )

    category_results: dict[str, dict[str, Any]] = {}
    labels = _base_status_labels()

    if feed_requested:
        category_results["feed"] = calculate_feed_cost_pressure(
            feed_kg_day=feed_kg_day,
            feed_price_per_kg=feed_price_per_kg,
            feed_price_currency=feed_price_currency,
            feed_price_date=feed_price_date,
            feed_price_geography=feed_price_geography,
            feed_price_source_type=feed_price_source_type,
            feed_class=feed_class,
            protein_percentage=protein_percentage,
            package_size_kg=package_size_kg,
            feed_price_source_reference=feed_price_source_reference,
        )

    if power_requested:
        category_results["power"] = calculate_power_cost_pressure(
            equipment_records=equipment_records,
            electricity_price_per_kwh=electricity_price_per_kwh,
            electricity_price_currency=electricity_price_currency,
            electricity_tariff_date=electricity_tariff_date,
            electricity_price_geography=electricity_price_geography,
            electricity_tariff_class=electricity_tariff_class,
            electricity_tariff_source_type=electricity_tariff_source_type,
            electricity_tariff_source_reference=electricity_tariff_source_reference,
        )

    category_costs = _category_cost_outputs(category_results)
    subtotal, subtotal_currency = _selected_subtotal(category_costs, labels)

    for result in category_results.values():
        labels.extend(result["cost_status_labels"])

    return {
        "cost_inputs": {
            category: result["cost_inputs"]
            for category, result in category_results.items()
        },
        "cost_outputs": {
            "supplied_categories": list(category_results),
            "category_costs": category_costs,
            "selected_operating_cost_pressure_subtotal": subtotal,
            "selected_operating_cost_pressure_currency": subtotal_currency,
        },
        "cost_basis": {
            "subtotal_basis": (
                "sum of supplied calculable operating-cost pressure categories "
                "when currencies match"
            ),
            "subtotal_is_not_complete_operating_cost": True,
            "category_basis": {
                category: result["cost_basis"]
                for category, result in category_results.items()
            },
        },
        "cost_status_labels": _dedupe(labels),
        "cost_boundary_notes": _boundary_notes(),
    }


def _category_cost_outputs(
    category_results: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    outputs: dict[str, dict[str, Any]] = {}
    if "feed" in category_results:
        feed_outputs = category_results["feed"]["cost_outputs"]
        outputs["feed"] = {
            "scenario_feed_cost_per_day": (
                feed_outputs["scenario_feed_cost_per_day"]
            ),
            "currency": feed_outputs["currency"],
        }
    if "power" in category_results:
        power_outputs = category_results["power"]["cost_outputs"]
        outputs["power"] = {
            "equipment": power_outputs["equipment"],
            "scenario_power_kwh_day": power_outputs["scenario_power_kwh_day"],
            "scenario_power_cost_per_day": (
                power_outputs["scenario_power_cost_per_day"]
            ),
            "currency": power_outputs["currency"],
        }
    return outputs


def _selected_subtotal(
    category_costs: dict[str, dict[str, Any]], labels: list[str]
) -> tuple[float | None, str | None]:
    money_values: list[tuple[float, str]] = []
    if "feed" in category_costs:
        money_values.append(
            (
                category_costs["feed"]["scenario_feed_cost_per_day"],
                category_costs["feed"]["currency"],
            )
        )
    if "power" in category_costs:
        money_values.append(
            (
                category_costs["power"]["scenario_power_cost_per_day"],
                category_costs["power"]["currency"],
            )
        )

    if not money_values:
        return None, None

    currencies = {currency for _, currency in money_values}
    if len(currencies) != 1:
        labels.append(MIXED_CURRENCY_SUBTOTAL_UNAVAILABLE)
        return None, None

    currency = next(iter(currencies))
    return _clean_float(sum(value for value, _ in money_values)), currency


def _validate_equipment_records(
    equipment_records: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    if equipment_records is None:
        raise OperatingCostPressureValidationError("equipment_records is required")
    if not isinstance(equipment_records, list) or not equipment_records:
        raise OperatingCostPressureValidationError(
            "equipment_records must be a non-empty list"
        )

    validated_records: list[dict[str, Any]] = []
    for index, record in enumerate(equipment_records):
        if not isinstance(record, dict):
            raise OperatingCostPressureValidationError(
                f"equipment_records[{index}] must be a record"
            )
        device_id = _validate_required_string(
            f"equipment_records[{index}].device_id", record.get("device_id")
        )
        device_role = _validate_required_string(
            f"equipment_records[{index}].device_role", record.get("device_role")
        )
        device_kw = _validate_non_negative_number(
            f"equipment_records[{index}].device_kw", record.get("device_kw")
        )
        runtime_h_day = _validate_non_negative_number(
            f"equipment_records[{index}].runtime_h_day",
            record.get("runtime_h_day"),
        )
        if runtime_h_day > 24:
            raise OperatingCostPressureValidationError(
                f"equipment_records[{index}].runtime_h_day must be <= 24"
            )
        load_fraction = _validate_fraction(
            f"equipment_records[{index}].load_fraction",
            record.get("load_fraction"),
        )
        power_basis = _validate_required_string(
            f"equipment_records[{index}].power_basis", record.get("power_basis")
        )
        if power_basis not in ALLOWED_POWER_BASIS:
            raise OperatingCostPressureValidationError(
                f"equipment_records[{index}].power_basis must be one of: "
                + ", ".join(sorted(ALLOWED_POWER_BASIS))
            )
        validated_records.append(
            {
                "device_id": device_id,
                "device_role": device_role,
                "device_kw": device_kw,
                "runtime_h_day": runtime_h_day,
                "load_fraction": load_fraction,
                "power_basis": power_basis,
            }
        )
    return validated_records


def _validate_non_negative_number(name: str, value: float) -> float:
    numeric_value = _validate_number(name, value)
    if numeric_value < 0:
        raise OperatingCostPressureValidationError(f"{name} must be non-negative")
    return numeric_value


def _validate_optional_non_negative_number(
    name: str, value: float | None
) -> float | None:
    if value is None:
        return None
    return _validate_non_negative_number(name, value)


def _validate_fraction(name: str, value: float) -> float:
    numeric_value = _validate_number(name, value)
    if numeric_value < 0 or numeric_value > 1:
        raise OperatingCostPressureValidationError(
            f"{name} must be between 0 and 1 inclusive"
        )
    return numeric_value


def _validate_number(name: str, value: float) -> float:
    if value is None:
        raise OperatingCostPressureValidationError(f"{name} is required")
    if isinstance(value, bool) or not isinstance(value, Real):
        raise OperatingCostPressureValidationError(f"{name} must be a number")
    numeric_value = float(value)
    if not math.isfinite(numeric_value):
        raise OperatingCostPressureValidationError(f"{name} must be finite")
    return numeric_value


def _validate_required_string(name: str, value: str) -> str:
    if value is None:
        raise OperatingCostPressureValidationError(f"{name} is required")
    if not isinstance(value, str):
        raise OperatingCostPressureValidationError(f"{name} must be a string")
    if not value.strip():
        raise OperatingCostPressureValidationError(f"{name} must be non-empty")
    return value


def _base_status_labels() -> list[str]:
    return [
        SCENARIO_ESTIMATE,
        NOT_CANON_NOT_MARKET_TRUTH,
        NOT_PROFITABILITY,
        SELECTED_COST_PRESSURE_ONLY,
        REVENUE_INPUTS_MISSING,
    ]


def _boundary_notes() -> list[str]:
    return [
        "Outputs are selected scenario operating-cost pressure only.",
        "Outputs are not total operating cost.",
        "Outputs are not canon and not market truth.",
        "Outputs do not calculate revenue, profitability, gross margin, ROI, "
        "payback, break-even, or economic viability.",
        "Outputs do not calculate fish revenue, basil revenue, crop revenue, "
        "or saleable_harvest_mass_kg.",
        "Outputs do not calculate buffer cost, water cost, labor cost, or "
        "backup-power cost in P2a.",
    ]


def _feed_inputs_supplied(**values: Any) -> bool:
    return any(value is not None for value in values.values())


def _power_inputs_supplied(**values: Any) -> bool:
    return any(value is not None for value in values.values())


def _dedupe(values: list[str]) -> list[str]:
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _clean_float(value: float) -> float:
    return round(value, 10)
