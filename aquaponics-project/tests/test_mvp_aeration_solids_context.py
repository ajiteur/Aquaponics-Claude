import unittest

from src.mvp_aeration_solids_context import (
    AERATION_CAPACITY_UNAVAILABLE,
    BACKUP_AERATION_POWER_CONTINUITY_MISSING,
    CLARIFIER_SETTLING_RETENTION_MISSING,
    DWC_ROOT_ZONE_AERATION_CONTEXT_MISSING,
    FISH_RESPIRATION_OXYGEN_DEMAND_UNAVAILABLE,
    MEASURED_DO_MISSING,
    OXYGEN_TRANSFER_ASSUMPTION_MISSING,
    SOLIDS_LOAD_COEFFICIENT_MISSING,
    SOLIDS_REMOVAL_CAPACITY_UNAVAILABLE,
    TOTAL_OXYGEN_DEMAND_UNAVAILABLE,
    AerationSolidsContextValidationError,
    build_aeration_solids_context,
)


class MvpAerationSolidsContextTests(unittest.TestCase):
    def test_default_context_emits_missing_aeration_and_solids_labels(self) -> None:
        result = build_aeration_solids_context()

        self.assertEqual(
            set(result),
            {
                "oxygen_context",
                "aeration_context",
                "dwc_root_zone_context",
                "solids_context",
                "status_labels",
                "boundary_notes",
            },
        )
        labels = set(result["status_labels"])
        self.assertIn(AERATION_CAPACITY_UNAVAILABLE, labels)
        self.assertIn(OXYGEN_TRANSFER_ASSUMPTION_MISSING, labels)
        self.assertIn(MEASURED_DO_MISSING, labels)
        self.assertIn(FISH_RESPIRATION_OXYGEN_DEMAND_UNAVAILABLE, labels)
        self.assertIn(TOTAL_OXYGEN_DEMAND_UNAVAILABLE, labels)
        self.assertIn(DWC_ROOT_ZONE_AERATION_CONTEXT_MISSING, labels)
        self.assertIn(SOLIDS_LOAD_COEFFICIENT_MISSING, labels)
        self.assertIn(SOLIDS_REMOVAL_CAPACITY_UNAVAILABLE, labels)
        self.assertIn(CLARIFIER_SETTLING_RETENTION_MISSING, labels)
        self.assertIn(BACKUP_AERATION_POWER_CONTINUITY_MISSING, labels)

    def test_measured_do_is_echoed_as_context_without_safe_unsafe_claim(self) -> None:
        result = build_aeration_solids_context(measured_do_mg_l=5.0)

        self.assertEqual(result["aeration_context"]["measured_do_mg_l"], 5.0)
        self.assertEqual(
            result["aeration_context"]["measured_do_basis"],
            "point_or_context_measurement_not_future_safety_proof",
        )
        self.assertNotIn(MEASURED_DO_MISSING, result["status_labels"])
        self.assertFalse(_contains_key(result, "safe"))
        self.assertFalse(_contains_key(result, "unsafe"))

    def test_nitrification_oxygen_demand_is_echoed_as_sub_load_context(self) -> None:
        result = build_aeration_solids_context(
            nitrification_oxygen_demand_g_day=134.5408
        )

        self.assertEqual(
            result["oxygen_context"]["nitrification_oxygen_demand_g_day"],
            134.5408,
        )
        self.assertEqual(
            result["oxygen_context"]["nitrification_oxygen_demand_basis"],
            "known nitrification-support sub-load only",
        )
        self.assertEqual(
            result["oxygen_context"]["total_oxygen_demand_status"], "not_calculated"
        )
        self.assertFalse(_contains_key(result, "total_oxygen_demand_g_day"))

    def test_dry_solids_potential_requires_feed_and_coefficient(self) -> None:
        without_coefficient = build_aeration_solids_context(feed_kg_day=1.0)
        without_feed = build_aeration_solids_context(dry_solids_coefficient=0.25)

        self.assertNotIn(
            "estimated_dry_solids_potential_kg_day",
            without_coefficient["solids_context"],
        )
        self.assertNotIn(
            "estimated_dry_solids_potential_kg_day", without_feed["solids_context"]
        )

    def test_dry_solids_potential_uses_feed_times_coefficient(self) -> None:
        result = build_aeration_solids_context(
            feed_kg_day=1.0, dry_solids_coefficient=0.25
        )

        self.assertAlmostEqual(
            result["solids_context"]["estimated_dry_solids_potential_kg_day"],
            0.25,
        )
        self.assertEqual(result["solids_context"]["dry_solids_coefficient"], 0.25)

    def test_dry_solids_output_is_labeled_with_boundaries(self) -> None:
        result = build_aeration_solids_context(
            feed_kg_day=1.0, dry_solids_coefficient=0.25
        )

        basis = result["solids_context"]["dry_solids_basis"]
        self.assertIn("provisional feed-linked dry-solids potential", basis)
        self.assertIn("not wet sludge", basis)
        self.assertIn("not TSS concentration", basis)
        self.assertIn("not solids-removal capacity", basis)

    def test_missing_coefficient_emits_solids_label(self) -> None:
        result = build_aeration_solids_context(feed_kg_day=1.0)

        self.assertIn(SOLIDS_LOAD_COEFFICIENT_MISSING, result["status_labels"])

    def test_missing_feed_with_coefficient_does_not_calculate_dry_solids(self) -> None:
        result = build_aeration_solids_context(dry_solids_coefficient=0.25)

        self.assertNotIn(
            "estimated_dry_solids_potential_kg_day", result["solids_context"]
        )
        self.assertIn(
            "feed_input_missing_for_dry_solids_potential",
            result["status_labels"],
        )

    def test_rejects_negative_measured_do(self) -> None:
        with self.assertRaisesRegex(
            AerationSolidsContextValidationError,
            "measured_do_mg_l must be non-negative",
        ):
            build_aeration_solids_context(measured_do_mg_l=-0.1)

    def test_rejects_invalid_dry_solids_coefficient(self) -> None:
        with self.assertRaisesRegex(
            AerationSolidsContextValidationError,
            "dry_solids_coefficient must be between 0 and 1 inclusive",
        ):
            build_aeration_solids_context(
                feed_kg_day=1.0, dry_solids_coefficient=1.01
            )

    def test_rejects_invalid_non_boolean_context_flags(self) -> None:
        with self.assertRaisesRegex(
            AerationSolidsContextValidationError,
            "aeration_capacity_context_available must be a boolean",
        ):
            build_aeration_solids_context(
                aeration_capacity_context_available="yes"  # type: ignore[arg-type]
            )

    def test_rejects_negative_nitrification_oxygen_and_feed(self) -> None:
        with self.assertRaisesRegex(
            AerationSolidsContextValidationError,
            "nitrification_oxygen_demand_g_day must be non-negative",
        ):
            build_aeration_solids_context(
                nitrification_oxygen_demand_g_day=-1.0
            )

        with self.assertRaisesRegex(
            AerationSolidsContextValidationError, "feed_kg_day must be non-negative"
        ):
            build_aeration_solids_context(
                feed_kg_day=-1.0, dry_solids_coefficient=0.25
            )

    def test_rejects_non_numeric_and_non_finite_numeric_inputs(self) -> None:
        with self.assertRaisesRegex(
            AerationSolidsContextValidationError, "measured_do_mg_l must be a number"
        ):
            build_aeration_solids_context(measured_do_mg_l=True)  # type: ignore[arg-type]

        with self.assertRaisesRegex(
            AerationSolidsContextValidationError,
            "dry_solids_coefficient must be finite",
        ):
            build_aeration_solids_context(dry_solids_coefficient=float("inf"))

    def test_output_does_not_imply_disallowed_claims(self) -> None:
        result = build_aeration_solids_context(
            nitrification_oxygen_demand_g_day=134.5408,
            measured_do_mg_l=5.0,
            feed_kg_day=1.0,
            dry_solids_coefficient=0.25,
        )

        for disallowed_key in DISALLOWED_OUTPUT_KEYS:
            self.assertFalse(_contains_key(result, disallowed_key), disallowed_key)

    def test_direct_helper_example(self) -> None:
        result = build_aeration_solids_context(
            nitrification_oxygen_demand_g_day=134.5408,
            feed_kg_day=1.0,
            dry_solids_coefficient=0.25,
            measured_do_mg_l=5.0,
        )

        self.assertEqual(
            result["oxygen_context"]["nitrification_oxygen_demand_g_day"],
            134.5408,
        )
        self.assertEqual(result["aeration_context"]["measured_do_mg_l"], 5.0)
        self.assertAlmostEqual(
            result["solids_context"]["estimated_dry_solids_potential_kg_day"],
            0.25,
        )
        for disallowed_key in DISALLOWED_OUTPUT_KEYS:
            self.assertFalse(_contains_key(result, disallowed_key), disallowed_key)


DISALLOWED_OUTPUT_KEYS = {
    "system_safe",
    "fish_safe",
    "safe",
    "unsafe",
    "aeration_capacity_sufficient",
    "oxygen_transfer_capacity",
    "total_oxygen_demand_g_day",
    "fish_respiration_oxygen_demand_g_day",
    "wet_sludge",
    "tss_mg_l",
    "solids_removal_capacity",
    "saleable_harvest_mass_kg",
    "feed_cost",
    "tank_suitability",
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
