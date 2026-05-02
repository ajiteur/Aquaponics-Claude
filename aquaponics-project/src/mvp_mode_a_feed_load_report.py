"""Mode A load-only report builder for the MVP aquaponics feed engine."""

from __future__ import annotations

from typing import Any

from src.feed_waste_tan_loads import (
    FeedWasteTanLoadValidationError,
    calculate_feed_waste_tan_loads,
)


INPUT_MODE = "mode_a_direct_feed"

TAN_CONCENTRATION_UNAVAILABLE = (
    "tan_concentration_unavailable_without_volume_time_exchange_or_removal"
)
NH3_RISK_UNAVAILABLE = "nh3_risk_unavailable_without_ph_and_temperature"
FEED_COST_UNAVAILABLE = "feed_cost_unavailable_without_feed_price"
TANK_SUITABILITY_UNAVAILABLE = (
    "tank_suitability_unavailable_without_volume_and_stocking_density"
)
BIOFILTER_REMOVAL_UNAVAILABLE = (
    "biofilter_removal_unavailable_without_capacity_and_conversion_assumption"
)
BASIL_SALEABLE_OUTPUT_UNRESOLVED = (
    "basil_saleable_output_unresolved_without_observed_or_reviewed_value"
)


class ModeAFeedLoadReportValidationError(ValueError):
    """Raised when a Mode A feed-load report input is invalid."""


def build_mode_a_feed_load_report(
    *,
    scenario_id: str | None = None,
    input_mode: str | None = None,
    feed_kg_day: float | None = None,
    protein_fraction: float | None = None,
    feed_class: Any | None = None,
    protein_basis: Any | None = None,
    feeding_frequency_per_day: Any | None = None,
    fcr_band: Any | None = None,
    architecture_context: Any | None = None,
    water_volume_context_available: Any = False,
    time_basis_context_available: Any = False,
    exchange_or_retention_context_available: Any = False,
    ph_context_available: Any = False,
    temperature_context_available: Any = False,
    feed_price_context_available: Any = False,
    tank_volume_context_available: Any = False,
    stocking_density_context_available: Any = False,
    biofilter_capacity_context_available: Any = False,
) -> dict[str, Any]:
    """Build a load-only Mode A report from explicit direct-feed inputs."""

    validated_scenario_id = _validate_required_string("scenario_id", scenario_id)
    validated_input_mode = _validate_input_mode(input_mode)

    try:
        load_result = calculate_feed_waste_tan_loads(
            feed_kg_day=feed_kg_day, protein_fraction=protein_fraction
        )
    except FeedWasteTanLoadValidationError as exc:
        raise ModeAFeedLoadReportValidationError(str(exc)) from exc

    optional_context = {
        "feed_class": feed_class,
        "protein_basis": protein_basis,
        "feeding_frequency_per_day": feeding_frequency_per_day,
        "fcr_band": fcr_band,
        "architecture_context": architecture_context,
        "water_volume_context_available": water_volume_context_available,
        "time_basis_context_available": time_basis_context_available,
        "exchange_or_retention_context_available": (
            exchange_or_retention_context_available
        ),
        "ph_context_available": ph_context_available,
        "temperature_context_available": temperature_context_available,
        "feed_price_context_available": feed_price_context_available,
        "tank_volume_context_available": tank_volume_context_available,
        "stocking_density_context_available": stocking_density_context_available,
        "biofilter_capacity_context_available": biofilter_capacity_context_available,
    }

    return {
        "scenario_id": validated_scenario_id,
        "input_mode": validated_input_mode,
        "inputs": {
            "feed_kg_day": load_result["feed_kg_day"],
            "protein_fraction": load_result["protein_fraction"],
        },
        "optional_context": optional_context,
        "loads": {
            "tan_n_load_kg_day": load_result["tan_n_load_kg_day"],
            "tan_n_load_g_day": load_result["tan_n_load_g_day"],
            "oxygen_demand_g_day": load_result["oxygen_demand_g_day"],
            "alkalinity_demand_g_caco3_day": (
                load_result["alkalinity_demand_g_caco3_day"]
            ),
        },
        "calculation_basis": _build_calculation_basis(load_result),
        "status_labels": _build_status_labels(
            water_volume_context_available=water_volume_context_available,
            time_basis_context_available=time_basis_context_available,
            exchange_or_retention_context_available=(
                exchange_or_retention_context_available
            ),
            ph_context_available=ph_context_available,
            temperature_context_available=temperature_context_available,
            feed_price_context_available=feed_price_context_available,
            tank_volume_context_available=tank_volume_context_available,
            stocking_density_context_available=stocking_density_context_available,
            biofilter_capacity_context_available=biofilter_capacity_context_available,
        ),
        "boundary_notes": [
            "Report labels do not calculate TAN concentration.",
            "Report labels do not calculate unionized NH3 toxicity.",
            "Report labels do not calculate feed cost.",
            "Report labels do not calculate tank suitability.",
            "Report labels do not calculate biofilter removal.",
            (
                "Report labels do not calculate mass, revenue, shrink, penalties, "
                "buyer acceptance, or saleability rates."
            ),
            "Report labels do not calculate or populate saleable_harvest_mass_kg.",
        ],
    }


def _validate_required_string(name: str, value: str | None) -> str:
    if value is None:
        raise ModeAFeedLoadReportValidationError(f"{name} is required")
    if not isinstance(value, str):
        raise ModeAFeedLoadReportValidationError(f"{name} must be a string")
    if not value.strip():
        raise ModeAFeedLoadReportValidationError(f"{name} must be non-empty")
    return value


def _validate_input_mode(input_mode: str | None) -> str:
    if input_mode is None:
        raise ModeAFeedLoadReportValidationError("input_mode is required")
    if input_mode != INPUT_MODE:
        raise ModeAFeedLoadReportValidationError(
            f"input_mode must be {INPUT_MODE!r}"
        )
    return input_mode


def _build_calculation_basis(load_result: dict[str, Any]) -> dict[str, Any]:
    helper_basis = load_result["calculation_basis"]
    return {
        "input_mode": INPUT_MODE,
        "input_basis": "Mode A direct-feed input",
        "tan_load_basis": "TAN-N/ammonia-N load, not TAN concentration",
        "oxygen_demand_basis": (
            "Nitrification-support oxygen demand, not confirmed biofilter removal"
        ),
        "alkalinity_demand_basis": (
            "Nitrification-support CaCO3 alkalinity demand, not confirmed "
            "biofilter removal"
        ),
        "feed_to_tan_n_factor": helper_basis["feed_to_tan_n_factor"],
        "oxygen_demand_g_per_g_tan_n": (
            helper_basis["oxygen_demand_g_per_g_tan_n"]
        ),
        "alkalinity_demand_g_caco3_per_g_tan_n": (
            helper_basis["alkalinity_demand_g_caco3_per_g_tan_n"]
        ),
        "excluded_calculations": [
            "tan_concentration",
            "unionized_nh3_toxicity",
            "feed_cost",
            "tank_suitability",
            "biomass_derived_feeding",
            "biofilter_removal",
            "crop_saleability",
            "saleable_harvest_mass_kg",
        ],
        "calculation_limits": [
            "No feed-cost calculation.",
            "No tank-suitability calculation.",
            "No crop saleability calculation.",
        ],
    }


def _build_status_labels(
    *,
    water_volume_context_available: Any,
    time_basis_context_available: Any,
    exchange_or_retention_context_available: Any,
    ph_context_available: Any,
    temperature_context_available: Any,
    feed_price_context_available: Any,
    tank_volume_context_available: Any,
    stocking_density_context_available: Any,
    biofilter_capacity_context_available: Any,
) -> list[str]:
    labels: list[str] = []

    if not (
        _is_explicitly_true(water_volume_context_available)
        and _is_explicitly_true(time_basis_context_available)
        and _is_explicitly_true(exchange_or_retention_context_available)
    ):
        labels.append(TAN_CONCENTRATION_UNAVAILABLE)

    if not (
        _is_explicitly_true(ph_context_available)
        and _is_explicitly_true(temperature_context_available)
    ):
        labels.append(NH3_RISK_UNAVAILABLE)

    if not _is_explicitly_true(feed_price_context_available):
        labels.append(FEED_COST_UNAVAILABLE)

    if not (
        _is_explicitly_true(tank_volume_context_available)
        and _is_explicitly_true(stocking_density_context_available)
    ):
        labels.append(TANK_SUITABILITY_UNAVAILABLE)

    if not _is_explicitly_true(biofilter_capacity_context_available):
        labels.append(BIOFILTER_REMOVAL_UNAVAILABLE)

    labels.append(BASIL_SALEABLE_OUTPUT_UNRESOLVED)
    return labels


def _is_explicitly_true(value: Any) -> bool:
    return value is True
