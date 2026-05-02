"""Mode A feed-to-TAN-N load calculator for the MVP aquaponics engine."""

from __future__ import annotations

import math
from numbers import Real
from typing import Any


FEED_TO_TAN_N_FACTOR = 0.092
OXYGEN_DEMAND_G_PER_G_TAN_N = 4.57
ALKALINITY_DEMAND_G_CACO3_PER_G_TAN_N = 7.14


class FeedWasteTanLoadValidationError(ValueError):
    """Raised when Mode A feed/TAN load inputs are missing or out of range."""


def calculate_feed_waste_tan_loads(feed_kg_day: float, protein_fraction: float) -> dict[str, Any]:
    """Calculate load-only feed/TAN-N demands from direct daily feed input.

    This intentionally does not calculate TAN concentration, unionized NH3 toxicity,
    feed cost, tank suitability, biomass-derived feeding, or biofilter removal.
    """

    validated_feed_kg_day = _validate_non_negative_number("feed_kg_day", feed_kg_day)
    validated_protein_fraction = _validate_fraction("protein_fraction", protein_fraction)

    tan_n_load_kg_day = validated_feed_kg_day * validated_protein_fraction * FEED_TO_TAN_N_FACTOR
    tan_n_load_g_day = tan_n_load_kg_day * 1000.0
    oxygen_demand_g_day = tan_n_load_g_day * OXYGEN_DEMAND_G_PER_G_TAN_N
    alkalinity_demand_g_caco3_day = (
        tan_n_load_g_day * ALKALINITY_DEMAND_G_CACO3_PER_G_TAN_N
    )

    return {
        "feed_kg_day": validated_feed_kg_day,
        "protein_fraction": validated_protein_fraction,
        "tan_n_load_kg_day": tan_n_load_kg_day,
        "tan_n_load_g_day": tan_n_load_g_day,
        "oxygen_demand_g_day": oxygen_demand_g_day,
        "alkalinity_demand_g_caco3_day": alkalinity_demand_g_caco3_day,
        "calculation_basis": {
            "input_mode": "mode_a_direct_feed",
            "tan_load_basis": "TAN-N/ammonia-N load, not unionized NH3",
            "feed_to_tan_n_factor": FEED_TO_TAN_N_FACTOR,
            "oxygen_demand_g_per_g_tan_n": OXYGEN_DEMAND_G_PER_G_TAN_N,
            "alkalinity_demand_g_caco3_per_g_tan_n": (
                ALKALINITY_DEMAND_G_CACO3_PER_G_TAN_N
            ),
            "excluded_calculations": [
                "tan_concentration",
                "unionized_nh3_toxicity",
                "feed_cost",
                "tank_suitability",
                "biomass_derived_feeding",
                "biofilter_removal",
                "saleable_harvest_mass_kg",
            ],
        },
    }


def _validate_non_negative_number(name: str, value: float) -> float:
    numeric_value = _validate_number(name, value)
    if numeric_value < 0:
        raise FeedWasteTanLoadValidationError(f"{name} must be non-negative")
    return numeric_value


def _validate_fraction(name: str, value: float) -> float:
    numeric_value = _validate_number(name, value)
    if numeric_value < 0 or numeric_value > 1:
        raise FeedWasteTanLoadValidationError(f"{name} must be between 0 and 1 inclusive")
    return numeric_value


def _validate_number(name: str, value: float) -> float:
    if value is None:
        raise FeedWasteTanLoadValidationError(f"{name} is required")
    if isinstance(value, bool) or not isinstance(value, Real):
        raise FeedWasteTanLoadValidationError(f"{name} must be a number")
    numeric_value = float(value)
    if not math.isfinite(numeric_value):
        raise FeedWasteTanLoadValidationError(f"{name} must be finite")
    return numeric_value
