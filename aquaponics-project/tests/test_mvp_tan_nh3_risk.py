import unittest

from src.mvp_tan_nh3_risk import (
    FISH_TANK_CONCENTRATION_SCOPE,
    NH3_MOLECULAR_WEIGHT_CONVERSION,
    TanNh3RiskValidationError,
    calculate_unionized_nh3_chemistry,
    estimate_tan_n_concentration,
)


class MvpTanNh3RiskTests(unittest.TestCase):
    def test_estimates_tan_n_concentration_from_load_volume_and_period(self) -> None:
        result = estimate_tan_n_concentration(
            tan_n_load_g_day=10.0,
            effective_water_volume_l=1000.0,
            accumulation_period_day=0.5,
            concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
        )

        self.assertAlmostEqual(result["estimated_tan_n_mg_l"], 5.0)
        self.assertEqual(result["concentration_scope"], FISH_TANK_CONCENTRATION_SCOPE)
        self.assertEqual(
            result["calculation_basis"]["concentration_basis"], "TAN-N mg/L"
        )
        self.assertEqual(
            result["calculation_basis"]["assumption"], "upper_bound_no_removal"
        )

    def test_estimates_example_tan_n_concentration(self) -> None:
        result = estimate_tan_n_concentration(
            tan_n_load_g_day=29.44,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
        )

        self.assertAlmostEqual(
            result["estimated_tan_n_mg_l"], 3.7743589743589743
        )

    def test_rejects_missing_or_invalid_volume(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "effective_water_volume_l is required"
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=29.44,
                effective_water_volume_l=None,  # type: ignore[arg-type]
                accumulation_period_day=1,
                concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
            )

        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "effective_water_volume_l must be positive"
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=29.44,
                effective_water_volume_l=0,
                accumulation_period_day=1,
                concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
            )

    def test_rejects_missing_or_invalid_accumulation_period(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "accumulation_period_day is required"
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=29.44,
                effective_water_volume_l=7800,
                accumulation_period_day=None,  # type: ignore[arg-type]
                concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
            )

        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "accumulation_period_day must be positive"
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=29.44,
                effective_water_volume_l=7800,
                accumulation_period_day=-1,
                concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
            )

    def test_rejects_unsupported_concentration_scope(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError,
            "concentration_scope must be 'fish_tank'",
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=29.44,
                effective_water_volume_l=7800,
                accumulation_period_day=1,
                concentration_scope="system_average",
            )

    def test_rejects_negative_tan_n_load(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "tan_n_load_g_day must be non-negative"
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=-0.1,
                effective_water_volume_l=7800,
                accumulation_period_day=1,
                concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
            )

    def test_calculates_nh3_fraction_with_known_ph_and_temperature(self) -> None:
        result = calculate_unionized_nh3_chemistry(
            estimated_tan_n_mg_l=3.7743589743589743,
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        self.assertAlmostEqual(
            result["estimated_unionized_nh3_fraction"], 0.00697108500908494
        )
        self.assertEqual(
            result["calculation_basis"]["fraction_formula"],
            "1 / (10 ** (pka - ph) + 1)",
        )

    def test_calculates_nh3_n_from_tan_n_concentration(self) -> None:
        result = calculate_unionized_nh3_chemistry(
            estimated_tan_n_mg_l=3.7743589743589743,
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        expected_nh3_n = (
            result["estimated_tan_n_mg_l"]
            * result["estimated_unionized_nh3_fraction"]
        )
        self.assertAlmostEqual(result["estimated_nh3_n_mg_l"], expected_nh3_n)

    def test_calculates_nh3_with_17_over_14_conversion(self) -> None:
        result = calculate_unionized_nh3_chemistry(
            estimated_tan_n_mg_l=3.7743589743589743,
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        self.assertAlmostEqual(
            result["estimated_nh3_mg_l"],
            result["estimated_nh3_n_mg_l"] * NH3_MOLECULAR_WEIGHT_CONVERSION,
        )

    def test_rejects_missing_ph_for_nh3_chemistry(self) -> None:
        with self.assertRaisesRegex(TanNh3RiskValidationError, "ph is required"):
            calculate_unionized_nh3_chemistry(
                estimated_tan_n_mg_l=3.7743589743589743,
                ph=None,  # type: ignore[arg-type]
                water_temp_c=28.0,
                freshwater_assumption=True,
            )

    def test_rejects_missing_temperature_for_nh3_chemistry(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "water_temp_c is required"
        ):
            calculate_unionized_nh3_chemistry(
                estimated_tan_n_mg_l=3.7743589743589743,
                ph=7.0,
                water_temp_c=None,  # type: ignore[arg-type]
                freshwater_assumption=True,
            )

    def test_requires_freshwater_assumption_for_first_helper(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError,
            "freshwater_assumption must be true for this first helper",
        ):
            calculate_unionized_nh3_chemistry(
                estimated_tan_n_mg_l=3.7743589743589743,
                ph=7.0,
                water_temp_c=28.0,
                freshwater_assumption=False,
            )

    def test_rejects_ph_outside_freshwater_calculation_range(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "ph must be between 0 and 14 inclusive"
        ):
            calculate_unionized_nh3_chemistry(
                estimated_tan_n_mg_l=3.7743589743589743,
                ph=14.1,
                water_temp_c=28.0,
                freshwater_assumption=True,
            )

    def test_rejects_temperature_with_invalid_kelvin_conversion(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError,
            "water_temp_c produces an invalid Kelvin conversion",
        ):
            calculate_unionized_nh3_chemistry(
                estimated_tan_n_mg_l=3.7743589743589743,
                ph=7.0,
                water_temp_c=-273.2,
                freshwater_assumption=True,
            )

    def test_rejects_non_numeric_and_non_finite_values(self) -> None:
        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "tan_n_load_g_day must be a number"
        ):
            estimate_tan_n_concentration(
                tan_n_load_g_day=True,  # type: ignore[arg-type]
                effective_water_volume_l=7800,
                accumulation_period_day=1,
                concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
            )

        with self.assertRaisesRegex(
            TanNh3RiskValidationError, "estimated_tan_n_mg_l must be finite"
        ):
            calculate_unionized_nh3_chemistry(
                estimated_tan_n_mg_l=float("inf"),
                ph=7.0,
                water_temp_c=28.0,
                freshwater_assumption=True,
            )

    def test_outputs_do_not_imply_disallowed_claims(self) -> None:
        concentration = estimate_tan_n_concentration(
            tan_n_load_g_day=29.44,
            effective_water_volume_l=7800,
            accumulation_period_day=1,
            concentration_scope=FISH_TANK_CONCENTRATION_SCOPE,
        )
        chemistry = calculate_unionized_nh3_chemistry(
            estimated_tan_n_mg_l=concentration["estimated_tan_n_mg_l"],
            ph=7.0,
            water_temp_c=28.0,
            freshwater_assumption=True,
        )

        combined = {"concentration": concentration, "chemistry": chemistry}
        for disallowed_key in {
            "safe",
            "unsafe",
            "profitability",
            "tank_suitability",
            "feed_cost",
            "biofilter_removal",
            "aeration_capacity",
            "saleable_harvest_mass_kg",
        }:
            self.assertFalse(_contains_key(combined, disallowed_key), disallowed_key)


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
