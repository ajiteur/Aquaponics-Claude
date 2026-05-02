import unittest

from src.feed_waste_tan_loads import (
    FeedWasteTanLoadValidationError,
    calculate_feed_waste_tan_loads,
)


class FeedWasteTanLoadsTests(unittest.TestCase):
    def test_calculates_mode_a_load_outputs(self) -> None:
        result = calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction=0.32)

        self.assertEqual(result["feed_kg_day"], 1.0)
        self.assertEqual(result["protein_fraction"], 0.32)
        self.assertAlmostEqual(result["tan_n_load_kg_day"], 0.02944)
        self.assertAlmostEqual(result["tan_n_load_g_day"], 29.44)
        self.assertAlmostEqual(result["oxygen_demand_g_day"], 134.5408)
        self.assertAlmostEqual(result["alkalinity_demand_g_caco3_day"], 210.2016)
        self.assertEqual(result["calculation_basis"]["input_mode"], "mode_a_direct_feed")
        self.assertEqual(
            result["calculation_basis"]["tan_load_basis"],
            "TAN-N/ammonia-N load, not unionized NH3",
        )

    def test_calculation_basis_excludes_forbidden_outputs(self) -> None:
        result = calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction=0.32)

        excluded = set(result["calculation_basis"]["excluded_calculations"])
        self.assertIn("tan_concentration", excluded)
        self.assertIn("unionized_nh3_toxicity", excluded)
        self.assertIn("feed_cost", excluded)
        self.assertIn("tank_suitability", excluded)
        self.assertIn("biomass_derived_feeding", excluded)
        self.assertIn("biofilter_removal", excluded)
        self.assertIn("saleable_harvest_mass_kg", excluded)
        self.assertNotIn("tan_mg_l", result)
        self.assertNotIn("unionized_nh3_mg_l", result)
        self.assertNotIn("feed_cost", result)
        self.assertNotIn("saleable_harvest_mass_kg", result)

    def test_allows_zero_feed_and_boundary_protein_fractions(self) -> None:
        zero_feed = calculate_feed_waste_tan_loads(feed_kg_day=0, protein_fraction=1)
        self.assertEqual(zero_feed["tan_n_load_kg_day"], 0.0)

        zero_protein = calculate_feed_waste_tan_loads(feed_kg_day=1, protein_fraction=0)
        self.assertEqual(zero_protein["tan_n_load_kg_day"], 0.0)

    def test_rejects_missing_inputs(self) -> None:
        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "feed_kg_day is required"):
            calculate_feed_waste_tan_loads(feed_kg_day=None, protein_fraction=0.32)  # type: ignore[arg-type]

        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "protein_fraction is required"):
            calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction=None)  # type: ignore[arg-type]

    def test_rejects_negative_feed(self) -> None:
        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "feed_kg_day must be non-negative"):
            calculate_feed_waste_tan_loads(feed_kg_day=-0.1, protein_fraction=0.32)

    def test_rejects_protein_fraction_outside_zero_to_one(self) -> None:
        with self.assertRaisesRegex(
            FeedWasteTanLoadValidationError,
            "protein_fraction must be between 0 and 1 inclusive",
        ):
            calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction=-0.01)

        with self.assertRaisesRegex(
            FeedWasteTanLoadValidationError,
            "protein_fraction must be between 0 and 1 inclusive",
        ):
            calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction=1.01)

    def test_rejects_non_numeric_inputs(self) -> None:
        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "feed_kg_day must be a number"):
            calculate_feed_waste_tan_loads(feed_kg_day=True, protein_fraction=0.32)  # type: ignore[arg-type]

        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "protein_fraction must be a number"):
            calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction="0.32")  # type: ignore[arg-type]

    def test_rejects_non_finite_inputs(self) -> None:
        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "feed_kg_day must be finite"):
            calculate_feed_waste_tan_loads(feed_kg_day=float("inf"), protein_fraction=0.32)

        with self.assertRaisesRegex(FeedWasteTanLoadValidationError, "protein_fraction must be finite"):
            calculate_feed_waste_tan_loads(feed_kg_day=1.0, protein_fraction=float("nan"))


if __name__ == "__main__":
    unittest.main()
