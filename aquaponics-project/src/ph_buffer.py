"""Carbonate alkalinity buffer and pH for the daily simulation (UQ-018, candidate).

Replaces the fixed pH drift (0.01 pH per mg/L TAN nitrified) with a daily alkalinity
balance and a carbonate-equilibrium pH solve. The model record (candidate, pending
review) is "carbonate_alkalinity_buffer" in data/knowledge/models/water_chemistry_models.json.

    dAlk = - 7.05 x TAN-N nitrified            (Ebeling et al. 2006, Eq. 14)
           + excretion credit x TAN-N nitrified (default 0; charge-balance option 3.57)
           + 3.57 x share x residual N loss      (denitrification return; default share 0)
           + k_plant x 3.57 x NO3-N taken up     (plant uptake return; default 0)
           + exchange x (Alk_source - Alk)
           + base dose (as CaCO3)

Dissolved CO2 is held at the level implied by the starting pH and alkalinity, unless
the scenario gives co2_mg_L. pH comes from the charge balance with Plummer & Busenberg
(1982) constants. Concentrations, no activity correction.

Opt-in: a scenario turns it on with water_chemistry.model = "carbonate_alkalinity_buffer".
All outputs are scenario estimates, not validated.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNTIME_MODEL_PATH = PROJECT_ROOT / "data" / "simulation" / "models" / "water_chemistry_models.json"
MODEL_ID = "carbonate_alkalinity_buffer"
MG_CACO3_PER_MMOL_EQ = 50.04
CO2_MG_PER_MMOL = 44.01
G_CACO3_PER_G_N_PER_EQ_MOL = 50.04 / 14.007  # 3.57: 1 eq per mol N as g CaCO3 per g N


def load_model(path: Path = RUNTIME_MODEL_PATH) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    for record in data["records"]:
        if record.get("model_id") == MODEL_ID:
            return record
    raise KeyError(f"{MODEL_ID} not found in {path}")


def _log_k(coeffs: list[float], temp_c: float) -> float:
    a, b, c, d, e = coeffs
    t = temp_c + 273.15
    return a + b * t + c / t + d * math.log10(t) + e / t ** 2


def pk1(temp_c: float, model: dict) -> float:
    return -_log_k(model["coefficients"]["carbonic_acid_constants"]["log_k1_vs_T_K"], temp_c)


def pk2(temp_c: float, model: dict) -> float:
    return -_log_k(model["coefficients"]["carbonic_acid_constants"]["log_k2_vs_T_K"], temp_c)


def _alk_from(h: float, co2_mol: float, k1: float, k2: float, kw: float) -> float:
    hco3 = k1 * co2_mol / h
    return hco3 + 2 * k2 * hco3 / h + kw / h - h


def ph_from_alkalinity(alk_mg_l: float, co2_mg_l: float, temp_c: float, model: dict) -> float:
    """Solve the carbonate charge balance for pH (eq/L alkalinity, mol/L CO2*)."""
    k1, k2 = 10 ** -pk1(temp_c, model), 10 ** -pk2(temp_c, model)
    kw = 10 ** -model["coefficients"]["water_ion_product_pKw_25C"]["value"]
    alk = alk_mg_l / MG_CACO3_PER_MMOL_EQ / 1000.0
    co2 = max(co2_mg_l, 1e-6) / CO2_MG_PER_MMOL / 1000.0
    lo, hi = 3.0, 11.0  # pH bounds; alkalinity falls as pH falls
    for _ in range(80):
        mid = (lo + hi) / 2
        if _alk_from(10 ** -mid, co2, k1, k2, kw) > alk:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def co2_from_ph(ph: float, alk_mg_l: float, temp_c: float, model: dict) -> float:
    """Dissolved CO2* (mg/L) implied by a pH and alkalinity."""
    k1, k2 = 10 ** -pk1(temp_c, model), 10 ** -pk2(temp_c, model)
    kw = 10 ** -model["coefficients"]["water_ion_product_pKw_25C"]["value"]
    h = 10 ** -ph
    alk = alk_mg_l / MG_CACO3_PER_MMOL_EQ / 1000.0
    hco3 = (alk - kw / h + h) / (1 + 2 * k2 / h)
    return max(hco3 * h / k1, 0.0) * CO2_MG_PER_MMOL * 1000.0


def alkalinity_for_ph(ph: float, co2_mg_l: float, temp_c: float, model: dict) -> float:
    k1, k2 = 10 ** -pk1(temp_c, model), 10 ** -pk2(temp_c, model)
    kw = 10 ** -model["coefficients"]["water_ion_product_pKw_25C"]["value"]
    co2 = co2_mg_l / CO2_MG_PER_MMOL / 1000.0
    return _alk_from(10 ** -ph, co2, k1, k2, kw) * 1000.0 * MG_CACO3_PER_MMOL_EQ


def _setting(cfg: dict, model: dict, key: str, coeff: str) -> float:
    if cfg.get(key) is not None:
        return float(cfg[key])
    return float(model["coefficients"][coeff]["simulation_default"])


def step_day(
    *,
    water: dict,
    cfg: dict,
    temp_c: float,
    tan_nitrified_mg_l: float,
    residual_n_loss_mg_l: float,
    plant_no3_uptake_mg_l: float,
    exchange_fraction: float,
    target_ph: float | None,
    model: dict,
) -> dict:
    """Advance alkalinity one day and return the new pH and the terms used."""
    c = model["coefficients"]
    alk = water.get("alkalinity_mg_L_as_CaCO3")
    if alk is None:
        raise ValueError("carbonate_alkalinity_buffer needs water_state.alkalinity_mg_L_as_CaCO3")
    co2 = water.get("dissolved_co2_mg_L")
    if co2 is None:
        co2 = cfg.get("co2_mg_L")
    if co2 is None:
        co2 = co2_from_ph(water["pH"], alk, temp_c, model)
    source_alk = cfg.get("source_water_alkalinity_mg_L_as_CaCO3")
    if source_alk is None:
        raise ValueError("carbonate_alkalinity_buffer needs water_chemistry.source_water_alkalinity_mg_L_as_CaCO3")

    nit = c["nitrification_alkalinity_g_CaCO3_per_g_N"]["value"]
    credit = _setting(cfg, model, "nh3_excretion_credit_g_CaCO3_per_g_N", "fish_nh3_excretion_alkalinity_credit_g_CaCO3_per_g_N")
    denit_share = _setting(cfg, model, "denitrified_share_of_residual_n_loss", "denitrified_share_of_residual_n_loss")
    plant_eq = _setting(cfg, model, "plant_uptake_return_eq_per_mol_N", "plant_nitrate_uptake_alkalinity_return_eq_per_mol_N")
    denit = c["denitrification_alkalinity_return_g_CaCO3_per_g_N"]["value"]

    terms = {
        "nitrification": -nit * tan_nitrified_mg_l,
        "nh3_excretion_credit": credit * tan_nitrified_mg_l,
        "denitrification_return": denit * denit_share * residual_n_loss_mg_l,
        "plant_uptake_return": plant_eq * G_CACO3_PER_G_N_PER_EQ_MOL * plant_no3_uptake_mg_l,
        "water_exchange": exchange_fraction * (source_alk - alk),
    }
    alk_new = max(alk + sum(terms.values()), 0.0)

    dose_caco3 = 0.0
    base_g_per_m3 = {}
    if target_ph is not None and ph_from_alkalinity(alk_new, co2, temp_c, model) < target_ph:
        need = alkalinity_for_ph(target_ph, co2, temp_c, model) - alk_new
        cap = _setting(cfg, model, "max_base_dose_mg_L_as_CaCO3_per_day", "max_base_dose_mg_L_as_CaCO3_per_day")
        dose_caco3 = max(0.0, min(need, cap))
        mix = cfg.get("base_mix") or {"KOH": 0.5, "Ca(OH)2": 0.5}
        eqv = c["base_alkalinity_g_CaCO3_per_g"]["values"]
        for base, share in mix.items():
            base_g_per_m3[base] = round(dose_caco3 * share / eqv[base], 4)  # mg/L = g/m3
        alk_new += dose_caco3
    terms["base_dose"] = dose_caco3

    ph = ph_from_alkalinity(alk_new, co2, temp_c, model)
    return {
        "model_basis": "carbonate_alkalinity_buffer_candidate",
        "alkalinity_mg_L_as_CaCO3": alk_new,
        "dissolved_co2_mg_L": co2,
        "pH": ph,
        "terms_mg_L_as_CaCO3": {k: round(v, 4) for k, v in terms.items()},
        "base_dose_g_per_m3": base_g_per_m3,
    }
