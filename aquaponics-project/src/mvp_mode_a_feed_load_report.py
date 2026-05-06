"""Mode A report builder for the MVP aquaponics feed engine."""

from __future__ import annotations

from typing import Any

from src.feed_waste_tan_loads import (
    FeedWasteTanLoadValidationError,
    calculate_feed_waste_tan_loads,
)
from src.mvp_tan_nh3_risk import (
    NO_REMOVAL_ASSUMPTION,
    TanNh3RiskValidationError,
    calculate_unionized_nh3_chemistry,
    estimate_tan_n_concentration,
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
P1_WATER_QUALITY_INPUT_FIELDS = (
    "effective_water_volume_l",
    "accumulation_period_day",
    "concentration_scope",
    "ph",
    "water_temp_c",
    "freshwater_assumption",
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
    effective_water_volume_l: float | None = None,
    accumulation_period_day: float | None = None,
    concentration_scope: str | None = None,
    ph: float | None = None,
    water_temp_c: float | None = None,
    freshwater_assumption: bool | None = None,
) -> dict[str, Any]:
    """Build a Mode A report from explicit direct-feed inputs."""

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

    water_quality_context = _build_water_quality_context(
        tan_n_load_g_day=load_result["tan_n_load_g_day"],
        effective_water_volume_l=effective_water_volume_l,
        accumulation_period_day=accumulation_period_day,
        concentration_scope=concentration_scope,
        ph=ph,
        water_temp_c=water_temp_c,
        freshwater_assumption=freshwater_assumption,
    )
    has_water_quality_context = water_quality_context is not None

    report = {
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
        "calculation_basis": _build_calculation_basis(
            load_result, has_water_quality_context=has_water_quality_context
        ),
        "status_labels": _build_status_labels(
            has_water_quality_context=has_water_quality_context,
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
        "boundary_notes": _build_boundary_notes(
            has_water_quality_context=has_water_quality_context
        ),
    }
    if water_quality_context is not None:
        report["water_quality_context"] = water_quality_context
    return report


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


def _build_calculation_basis(
    load_result: dict[str, Any], *, has_water_quality_context: bool
) -> dict[str, Any]:
    helper_basis = load_result["calculation_basis"]
    excluded_calculations = [
        "unionized_nh3_toxicity",
        "threshold_comparison",
        "feed_cost",
        "tank_suitability",
        "biomass_derived_feeding",
        "biofilter_removal",
        "aeration_capacity",
        "crop_saleability",
        "saleable_harvest_mass_kg",
    ]
    if not has_water_quality_context:
        excluded_calculations.insert(0, "tan_concentration")

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
        "excluded_calculations": excluded_calculations,
        "calculation_limits": [
            "No feed-cost calculation.",
            "No tank-suitability calculation.",
            "No crop saleability calculation.",
        ],
    }


def _build_status_labels(
    *,
    has_water_quality_context: bool,
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

    if not has_water_quality_context and not (
        _is_explicitly_true(water_volume_context_available)
        and _is_explicitly_true(time_basis_context_available)
        and _is_explicitly_true(exchange_or_retention_context_available)
    ):
        labels.append(TAN_CONCENTRATION_UNAVAILABLE)

    if not has_water_quality_context and not (
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


def _build_water_quality_context(
    *,
    tan_n_load_g_day: float,
    effective_water_volume_l: float | None,
    accumulation_period_day: float | None,
    concentration_scope: str | None,
    ph: float | None,
    water_temp_c: float | None,
    freshwater_assumption: bool | None,
) -> dict[str, Any] | None:
    p1_inputs = {
        "effective_water_volume_l": effective_water_volume_l,
        "accumulation_period_day": accumulation_period_day,
        "concentration_scope": concentration_scope,
        "ph": ph,
        "water_temp_c": water_temp_c,
        "freshwater_assumption": freshwater_assumption,
    }
    supplied_fields = [
        field for field, value in p1_inputs.items() if value is not None
    ]
    if not supplied_fields:
        return None

    missing_fields = [
        field for field, value in p1_inputs.items() if value is None
    ]
    if missing_fields:
        raise ModeAFeedLoadReportValidationError(
            "partial P1 water-quality input group; missing field(s): "
            + ", ".join(missing_fields)
        )

    try:
        concentration = estimate_tan_n_concentration(
            tan_n_load_g_day=tan_n_load_g_day,
            effective_water_volume_l=effective_water_volume_l,
            accumulation_period_day=accumulation_period_day,
            concentration_scope=concentration_scope,
        )
        chemistry = calculate_unionized_nh3_chemistry(
            estimated_tan_n_mg_l=concentration["estimated_tan_n_mg_l"],
            ph=ph,
            water_temp_c=water_temp_c,
            freshwater_assumption=freshwater_assumption,
        )
    except TanNh3RiskValidationError as exc:
        raise ModeAFeedLoadReportValidationError(str(exc)) from exc

    return {
        "concentration_scope": concentration["concentration_scope"],
        "concentration_assumption": NO_REMOVAL_ASSUMPTION,
        "effective_water_volume_l": concentration["inputs"][
            "effective_water_volume_l"
        ],
        "accumulation_period_day": concentration["inputs"][
            "accumulation_period_day"
        ],
        "ph": chemistry["inputs"]["ph"],
        "water_temp_c": chemistry["inputs"]["water_temp_c"],
        "freshwater_assumption": chemistry["inputs"]["freshwater_assumption"],
        "estimated_tan_n_mg_l": concentration["estimated_tan_n_mg_l"],
        "estimated_unionized_nh3_fraction": (
            chemistry["estimated_unionized_nh3_fraction"]
        ),
        "estimated_nh3_n_mg_l": chemistry["estimated_nh3_n_mg_l"],
        "estimated_nh3_mg_l": chemistry["estimated_nh3_mg_l"],
        "unit_basis": {
            "estimated_tan_n_mg_l": "mg TAN-N/L",
            "estimated_unionized_nh3_fraction": "dimensionless fraction",
            "estimated_nh3_n_mg_l": "mg NH3-N/L",
            "estimated_nh3_mg_l": "mg NH3/L",
            "effective_water_volume_l": "L",
            "accumulation_period_day": "day",
            "ph": "freshwater pH",
            "water_temp_c": "degrees C",
        },
    }


def _build_boundary_notes(*, has_water_quality_context: bool) -> list[str]:
    if has_water_quality_context:
        water_quality_note = (
            "Water-quality context estimates TAN-N concentration and NH3 "
            "chemistry only when complete P1 inputs are supplied."
        )
    else:
        water_quality_note = "Report labels do not calculate TAN concentration."

    return [
        water_quality_note,
        "Report labels do not calculate unionized NH3 toxicity.",
        "Report labels do not calculate feed cost.",
        "Report labels do not calculate tank suitability.",
        "Report labels do not calculate biofilter removal.",
        "Report labels do not calculate aeration capacity.",
        (
            "Report labels do not calculate mass, revenue, shrink, penalties, "
            "buyer acceptance, or saleability rates."
        ),
        "Report labels do not calculate or populate saleable_harvest_mass_kg.",
    ]
