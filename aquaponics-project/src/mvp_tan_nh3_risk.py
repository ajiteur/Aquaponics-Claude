"""Isolated P1 TAN-N concentration and NH3 chemistry helper."""

from __future__ import annotations

import math
from numbers import Real
from typing import Any


FISH_TANK_CONCENTRATION_SCOPE = "fish_tank"
NO_REMOVAL_ASSUMPTION = "upper_bound_no_removal"
KELVIN_OFFSET = 273.2
NH3_MOLECULAR_WEIGHT_CONVERSION = 17.0 / 14.0


class TanNh3RiskValidationError(ValueError):
    """Raised when P1 TAN concentration or NH3 chemistry inputs are invalid."""


def estimate_tan_n_concentration(
    *,
    tan_n_load_g_day: float,
    effective_water_volume_l: float,
    accumulation_period_day: float,
    concentration_scope: str,
) -> dict[str, Any]:
    """Estimate fish-tank TAN-N concentration from load, volume, and time basis.

    This first P1 helper supports only a fish-tank upper-bound/no-removal
    estimate. It does not calculate actual biofilter removal, system-average
    concentration, threshold comparisons, or safety labels.
    """

    validated_tan_n_load_g_day = _validate_non_negative_number(
        "tan_n_load_g_day", tan_n_load_g_day
    )
    validated_effective_water_volume_l = _validate_positive_number(
        "effective_water_volume_l", effective_water_volume_l
    )
    validated_accumulation_period_day = _validate_positive_number(
        "accumulation_period_day", accumulation_period_day
    )
    validated_concentration_scope = _validate_concentration_scope(concentration_scope)

    tan_n_load_g_period = (
        validated_tan_n_load_g_day * validated_accumulation_period_day
    )
    estimated_tan_n_mg_l = (
        tan_n_load_g_period * 1000.0 / validated_effective_water_volume_l
    )

    return {
        "estimated_tan_n_mg_l": estimated_tan_n_mg_l,
        "concentration_scope": validated_concentration_scope,
        "calculation_basis": {
            "concentration_basis": "TAN-N mg/L",
            "input_load_basis": "tan_n_load_g_day",
            "effective_water_volume_basis": "effective_water_volume_l",
            "time_basis": "accumulation_period_day",
            "assumption": NO_REMOVAL_ASSUMPTION,
            "assumption_note": (
                "Fish-tank upper-bound concentration estimate with no dilution, "
                "exchange, or biofilter removal calculated."
            ),
            "excluded_calculations": _excluded_calculations(),
        },
        "inputs": {
            "tan_n_load_g_day": validated_tan_n_load_g_day,
            "effective_water_volume_l": validated_effective_water_volume_l,
            "accumulation_period_day": validated_accumulation_period_day,
        },
    }


def calculate_unionized_nh3_chemistry(
    *,
    estimated_tan_n_mg_l: float,
    ph: float,
    water_temp_c: float,
    freshwater_assumption: bool,
) -> dict[str, Any]:
    """Calculate freshwater unionized NH3 chemistry from TAN-N, pH, and temperature.

    This returns chemistry estimates only. It does not compare against thresholds
    and does not emit safe/unsafe labels.
    """

    validated_tan_n_mg_l = _validate_non_negative_number(
        "estimated_tan_n_mg_l", estimated_tan_n_mg_l
    )
    validated_ph = _validate_ph(ph)
    validated_water_temp_c = _validate_water_temp_c(water_temp_c)
    if freshwater_assumption is not True:
        raise TanNh3RiskValidationError(
            "freshwater_assumption must be true for this first helper"
        )

    temperature_k = validated_water_temp_c + KELVIN_OFFSET
    pka = 0.0901821 + 2729.92 / temperature_k
    estimated_unionized_nh3_fraction = 1.0 / (10.0 ** (pka - validated_ph) + 1.0)
    estimated_nh3_n_mg_l = validated_tan_n_mg_l * estimated_unionized_nh3_fraction
    estimated_nh3_mg_l = estimated_nh3_n_mg_l * NH3_MOLECULAR_WEIGHT_CONVERSION

    return {
        "estimated_tan_n_mg_l": validated_tan_n_mg_l,
        "estimated_unionized_nh3_fraction": estimated_unionized_nh3_fraction,
        "estimated_nh3_n_mg_l": estimated_nh3_n_mg_l,
        "estimated_nh3_mg_l": estimated_nh3_mg_l,
        "calculation_basis": {
            "tan_concentration_basis": "TAN-N mg/L",
            "ph_basis": "freshwater pH",
            "temperature_basis": "water_temp_c",
            "freshwater_assumption": True,
            "temperature_k": temperature_k,
            "pka_formula": "0.0901821 + 2729.92 / temperature_k",
            "fraction_formula": "1 / (10 ** (pka - ph) + 1)",
            "nh3_n_basis": "unionized ammonia expressed as nitrogen",
            "nh3_basis": "unionized ammonia expressed as NH3 molecule",
            "nh3_conversion": "NH3-N to NH3 uses 17/14",
            "excluded_calculations": _excluded_calculations(),
        },
        "inputs": {
            "estimated_tan_n_mg_l": validated_tan_n_mg_l,
            "ph": validated_ph,
            "water_temp_c": validated_water_temp_c,
            "freshwater_assumption": True,
        },
    }


def _validate_concentration_scope(concentration_scope: str) -> str:
    if concentration_scope is None:
        raise TanNh3RiskValidationError("concentration_scope is required")
    if concentration_scope != FISH_TANK_CONCENTRATION_SCOPE:
        raise TanNh3RiskValidationError(
            "concentration_scope must be 'fish_tank' for this first helper"
        )
    return concentration_scope


def _validate_ph(value: float) -> float:
    numeric_value = _validate_number("ph", value)
    if numeric_value < 0 or numeric_value > 14:
        raise TanNh3RiskValidationError("ph must be between 0 and 14 inclusive")
    return numeric_value


def _validate_water_temp_c(value: float) -> float:
    numeric_value = _validate_number("water_temp_c", value)
    if numeric_value + KELVIN_OFFSET <= 0:
        raise TanNh3RiskValidationError(
            "water_temp_c produces an invalid Kelvin conversion"
        )
    return numeric_value


def _validate_non_negative_number(name: str, value: float) -> float:
    numeric_value = _validate_number(name, value)
    if numeric_value < 0:
        raise TanNh3RiskValidationError(f"{name} must be non-negative")
    return numeric_value


def _validate_positive_number(name: str, value: float) -> float:
    numeric_value = _validate_number(name, value)
    if numeric_value <= 0:
        raise TanNh3RiskValidationError(f"{name} must be positive")
    return numeric_value


def _validate_number(name: str, value: float) -> float:
    if value is None:
        raise TanNh3RiskValidationError(f"{name} is required")
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TanNh3RiskValidationError(f"{name} must be a number")
    numeric_value = float(value)
    if not math.isfinite(numeric_value):
        raise TanNh3RiskValidationError(f"{name} must be finite")
    return numeric_value


def _excluded_calculations() -> list[str]:
    return [
        "safety_threshold_comparison",
        "safe_or_unsafe_label",
        "biofilter_removal",
        "system_average_concentration",
        "feed_cost",
        "tank_suitability",
        "aeration_capacity",
        "mode_b_biomass_derived_feeding",
        "saleable_harvest_mass_kg",
    ]
