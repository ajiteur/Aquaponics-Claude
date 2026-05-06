"""Isolated P1.5 aeration and solids context helper."""

from __future__ import annotations

import math
from numbers import Real
from typing import Any


AERATION_CAPACITY_UNAVAILABLE = (
    "aeration_capacity_unavailable_without_equipment_and_transfer_basis"
)
OXYGEN_TRANSFER_ASSUMPTION_MISSING = "oxygen_transfer_assumption_missing"
MEASURED_DO_MISSING = "measured_do_missing"
FISH_RESPIRATION_OXYGEN_DEMAND_UNAVAILABLE = (
    "fish_respiration_oxygen_demand_unavailable"
)
TOTAL_OXYGEN_DEMAND_UNAVAILABLE = "total_oxygen_demand_unavailable"
DWC_ROOT_ZONE_AERATION_CONTEXT_MISSING = "dwc_root_zone_aeration_context_missing"
SOLIDS_LOAD_COEFFICIENT_MISSING = "solids_load_coefficient_missing"
FEED_INPUT_MISSING_FOR_DRY_SOLIDS_POTENTIAL = (
    "feed_input_missing_for_dry_solids_potential"
)
SOLIDS_TRANSLATION_PROVISIONAL = "solids_translation_provisional"
SOLIDS_REMOVAL_CAPACITY_UNAVAILABLE = (
    "solids_removal_capacity_unavailable_without_filter_design_inputs"
)
CLARIFIER_SETTLING_RETENTION_MISSING = "clarifier_settling_retention_missing"
BACKUP_AERATION_POWER_CONTINUITY_MISSING = (
    "backup_aeration_power_continuity_missing"
)


class AerationSolidsContextValidationError(ValueError):
    """Raised when P1.5 aeration or solids context inputs are invalid."""


def build_aeration_solids_context(
    *,
    nitrification_oxygen_demand_g_day: float | None = None,
    measured_do_mg_l: float | None = None,
    feed_kg_day: float | None = None,
    dry_solids_coefficient: float | None = None,
    aeration_capacity_context_available: bool = False,
    oxygen_transfer_basis_available: bool = False,
    fish_respiration_context_available: bool = False,
    dwc_root_zone_aeration_context_available: bool = False,
    solids_removal_capacity_context_available: bool = False,
    clarifier_retention_context_available: bool = False,
    backup_aeration_power_continuity_available: bool = False,
) -> dict[str, Any]:
    """Build warning-only P1.5 aeration and solids context.

    This helper does not calculate total oxygen demand, fish respiration,
    aeration capacity, oxygen-transfer capacity, wet sludge, TSS concentration,
    solids-removal capacity, safety labels, or equipment adequacy.
    """

    validated_flags = {
        "aeration_capacity_context_available": _validate_flag(
            "aeration_capacity_context_available",
            aeration_capacity_context_available,
        ),
        "oxygen_transfer_basis_available": _validate_flag(
            "oxygen_transfer_basis_available", oxygen_transfer_basis_available
        ),
        "fish_respiration_context_available": _validate_flag(
            "fish_respiration_context_available", fish_respiration_context_available
        ),
        "dwc_root_zone_aeration_context_available": _validate_flag(
            "dwc_root_zone_aeration_context_available",
            dwc_root_zone_aeration_context_available,
        ),
        "solids_removal_capacity_context_available": _validate_flag(
            "solids_removal_capacity_context_available",
            solids_removal_capacity_context_available,
        ),
        "clarifier_retention_context_available": _validate_flag(
            "clarifier_retention_context_available",
            clarifier_retention_context_available,
        ),
        "backup_aeration_power_continuity_available": _validate_flag(
            "backup_aeration_power_continuity_available",
            backup_aeration_power_continuity_available,
        ),
    }
    validated_nitrification_oxygen_demand = _validate_optional_non_negative_number(
        "nitrification_oxygen_demand_g_day", nitrification_oxygen_demand_g_day
    )
    validated_measured_do = _validate_optional_non_negative_number(
        "measured_do_mg_l", measured_do_mg_l
    )
    validated_feed_kg_day = _validate_optional_non_negative_number(
        "feed_kg_day", feed_kg_day
    )
    validated_dry_solids_coefficient = _validate_optional_fraction(
        "dry_solids_coefficient", dry_solids_coefficient
    )

    solids_context = _build_solids_context(
        feed_kg_day=validated_feed_kg_day,
        dry_solids_coefficient=validated_dry_solids_coefficient,
        solids_removal_capacity_context_available=validated_flags[
            "solids_removal_capacity_context_available"
        ],
        clarifier_retention_context_available=validated_flags[
            "clarifier_retention_context_available"
        ],
    )
    status_labels = _build_status_labels(
        measured_do_mg_l=validated_measured_do,
        feed_kg_day=validated_feed_kg_day,
        dry_solids_coefficient=validated_dry_solids_coefficient,
        **validated_flags,
    )

    return {
        "oxygen_context": {
            "nitrification_oxygen_demand_g_day": (
                validated_nitrification_oxygen_demand
            ),
            "nitrification_oxygen_demand_basis": (
                "known nitrification-support sub-load only"
                if validated_nitrification_oxygen_demand is not None
                else "not_supplied"
            ),
            "fish_respiration_oxygen_demand_status": "not_calculated",
            "organic_waste_decomposition_oxygen_demand_status": "not_calculated",
            "total_oxygen_demand_status": "not_calculated",
        },
        "aeration_context": {
            "measured_do_mg_l": validated_measured_do,
            "measured_do_basis": (
                "point_or_context_measurement_not_future_safety_proof"
                if validated_measured_do is not None
                else "not_supplied"
            ),
            "aeration_capacity_context_available": validated_flags[
                "aeration_capacity_context_available"
            ],
            "oxygen_transfer_basis_available": validated_flags[
                "oxygen_transfer_basis_available"
            ],
            "aeration_capacity_status": "not_calculated",
            "oxygen_transfer_status": "not_calculated",
            "backup_aeration_power_continuity_available": validated_flags[
                "backup_aeration_power_continuity_available"
            ],
        },
        "dwc_root_zone_context": {
            "dwc_root_zone_aeration_context_available": validated_flags[
                "dwc_root_zone_aeration_context_available"
            ],
            "dwc_root_zone_basis": (
                "separate_from_fish_tank_aeration"
            ),
            "dwc_root_zone_oxygen_status": "not_calculated",
        },
        "solids_context": solids_context,
        "status_labels": status_labels,
        "boundary_notes": _boundary_notes(),
    }


def _build_solids_context(
    *,
    feed_kg_day: float | None,
    dry_solids_coefficient: float | None,
    solids_removal_capacity_context_available: bool,
    clarifier_retention_context_available: bool,
) -> dict[str, Any]:
    context: dict[str, Any] = {
        "feed_kg_day": feed_kg_day,
        "dry_solids_coefficient": dry_solids_coefficient,
        "dry_solids_basis": "not_calculated",
        "solids_removal_capacity_context_available": (
            solids_removal_capacity_context_available
        ),
        "clarifier_retention_context_available": clarifier_retention_context_available,
        "wet_sludge_status": "not_calculated",
        "tss_concentration_status": "not_calculated",
        "settleable_solids_split_status": "not_calculated",
        "solids_removal_status": "not_calculated",
    }
    if feed_kg_day is not None and dry_solids_coefficient is not None:
        context.update(
            {
                "estimated_dry_solids_potential_kg_day": (
                    feed_kg_day * dry_solids_coefficient
                ),
                "dry_solids_basis": (
                    "provisional feed-linked dry-solids potential; not wet "
                    "sludge, not TSS concentration, not settleable-solids split, "
                    "and not solids-removal capacity"
                ),
            }
        )
    return context


def _build_status_labels(
    *,
    measured_do_mg_l: float | None,
    feed_kg_day: float | None,
    dry_solids_coefficient: float | None,
    aeration_capacity_context_available: bool,
    oxygen_transfer_basis_available: bool,
    fish_respiration_context_available: bool,
    dwc_root_zone_aeration_context_available: bool,
    solids_removal_capacity_context_available: bool,
    clarifier_retention_context_available: bool,
    backup_aeration_power_continuity_available: bool,
) -> list[str]:
    labels: list[str] = []

    if not (
        aeration_capacity_context_available and oxygen_transfer_basis_available
    ):
        labels.append(AERATION_CAPACITY_UNAVAILABLE)
    if not oxygen_transfer_basis_available:
        labels.append(OXYGEN_TRANSFER_ASSUMPTION_MISSING)
    if measured_do_mg_l is None:
        labels.append(MEASURED_DO_MISSING)
    if not fish_respiration_context_available:
        labels.append(FISH_RESPIRATION_OXYGEN_DEMAND_UNAVAILABLE)

    labels.append(TOTAL_OXYGEN_DEMAND_UNAVAILABLE)

    if not dwc_root_zone_aeration_context_available:
        labels.append(DWC_ROOT_ZONE_AERATION_CONTEXT_MISSING)

    if feed_kg_day is not None and dry_solids_coefficient is None:
        labels.append(SOLIDS_LOAD_COEFFICIENT_MISSING)
    elif feed_kg_day is None and dry_solids_coefficient is not None:
        labels.append(FEED_INPUT_MISSING_FOR_DRY_SOLIDS_POTENTIAL)
    elif feed_kg_day is None and dry_solids_coefficient is None:
        labels.append(SOLIDS_LOAD_COEFFICIENT_MISSING)
    else:
        labels.append(SOLIDS_TRANSLATION_PROVISIONAL)

    if not solids_removal_capacity_context_available:
        labels.append(SOLIDS_REMOVAL_CAPACITY_UNAVAILABLE)
    if not clarifier_retention_context_available:
        labels.append(CLARIFIER_SETTLING_RETENTION_MISSING)
    if not backup_aeration_power_continuity_available:
        labels.append(BACKUP_AERATION_POWER_CONTINUITY_MISSING)
    return labels


def _boundary_notes() -> list[str]:
    return [
        "Nitrification oxygen demand is not total oxygen demand.",
        "Measured DO is a point/context measurement, not future safety proof.",
        "Oxygen demand is not aeration capacity.",
        (
            "Equipment capacity is not oxygen-transfer capacity unless transfer "
            "assumptions exist."
        ),
        "Fish respiration oxygen demand is not calculated.",
        "DWC/root-zone aeration is separate from fish-tank aeration.",
        "Dry-solids potential is not wet sludge.",
        "Dry-solids potential is not TSS concentration.",
        "Dry-solids potential is not solids-removal capacity.",
        (
            "No feed cost, tank suitability, fish safety, system safety, or "
            "basil saleable output is calculated."
        ),
    ]


def _validate_flag(name: str, value: bool) -> bool:
    if not isinstance(value, bool):
        raise AerationSolidsContextValidationError(f"{name} must be a boolean")
    return value


def _validate_optional_fraction(name: str, value: float | None) -> float | None:
    if value is None:
        return None
    numeric_value = _validate_number(name, value)
    if numeric_value < 0 or numeric_value > 1:
        raise AerationSolidsContextValidationError(
            f"{name} must be between 0 and 1 inclusive"
        )
    return numeric_value


def _validate_optional_non_negative_number(
    name: str, value: float | None
) -> float | None:
    if value is None:
        return None
    numeric_value = _validate_number(name, value)
    if numeric_value < 0:
        raise AerationSolidsContextValidationError(f"{name} must be non-negative")
    return numeric_value


def _validate_number(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise AerationSolidsContextValidationError(f"{name} must be a number")
    numeric_value = float(value)
    if not math.isfinite(numeric_value):
        raise AerationSolidsContextValidationError(f"{name} must be finite")
    return numeric_value
