# Approval Batch 003

Open. When it's ready, reply "approve batch 003 as recommended", or list the item numbers you want changed. Approvals are then recorded next to each value (who, date, scope).

Opened: 2026-11-26, while Ajit is away. Rule used (AGENTS.md 6A): approve medium or high confidence items that Tier 1 or Tier 2 sources corroborate. Single-source, Tier 3, low-confidence, conflicting and calibrated items stay candidates.

## A. Merge order

Each PR is stacked on the one before it, so merge them in this order.

| # | PR | Recommendation |
|---|---|---|
| A1 | #28: record Approval Batch 002, save-point-002 entry | **Merge first.** Tag `save-point-002` on the merge commit. |
| A2 | #29: swaps checkpoint (`compare_swaps.py`, heat-pump heating source, NFT and media-bed alternatives) | **Merge second.** Re-reviewed at `c5e1042`: tests (204), integrity and syncs pass. |
| A3 | #30: heating and climate checkpoint, plus the fish growth and feed checkpoint (`heat_demand.py`, `fish_growth.py`) | **Merge third.** Stacked on #29, re-reviewed at `a3a4892`. It now also carries the validation checkpoint and its first fixes. The fish model is opt-in, and only the two basil raft crop cycles use it; their yields move by under 0.1% (1.440 to 1.441 kg/m²). With #28, #29 and #30 combined, tests, integrity and syncs pass. |

## B. Values from PR #29 (swaps)

| # | Item | Recommendation |
|---|---|---|
| B1 | `heat_pump_seasonal_cop` NL 3.7 to 4.6 and `gas_heat_kwh_per_m3` NL 8.63 to 8.79 (Tier 2, medium, corroborated) | **Approve for scenario use.** |
| B2 | Truths CD_0011 (heat pump COP) and CD_0012 (gas heat per m³) | **Approve.** |
| B3 | Component `heating_heat_pump_air_water_nl`, €26.55 to €33.88/m² | Keep as candidate. Conflicting sources, lifetime unknown. |
| B5 | Basil yield in NFT relative to DWC, 0.83 to 0.95 (Blunk 2023, Pasch 2021) | Keep as candidate. Low confidence, the sources conflict on size. |
| B6 | Component `nft_channel_upvc_100x80_nl`, €16.75 to €18.61/m | Keep as candidate. Tier 3, single source. |
| B7 | Component `media_expanded_clay_nl`, €188 to €440/m³ | Keep as candidate. Three Tier 3 listings agree, but the rule needs Tier 1 or 2; lifetime unknown. |
| B8 | Media-bed basil yield relative to DWC: no number found (Knaus 2020 says not significantly different, but its table couldn't be read) | **Your call.** Option: use 1.0 (parity) as your own labelled assumption, scenario use only. If you say nothing, it stays a gap and media-bed swaps show no yield. |
| B4 | Component `structure_polyhouse_fan_pad_in`, ₹1,500 to ₹1,800/m² | **Approve the price for scenario use** (it is the MIDH 2025 norm approved in Batch 002 F1). Lifetime and power stay missing. |

## C. Values from PR #30 (heating and climate)

| # | Item | Recommendation |
|---|---|---|
| C1 | HEAT_0002 (Bengaluru IMD normals), HEAT_0004 (cover U-values and screen factor), HEAT_0005 (31.65 MJ per m³ a.e.), HEAT_0009 (Indian NVPH have no heating) | **Approve.** Tier 1, corroborated. |
| C2 | HEAT_0001 (De Bilt KNMI normals) | Keep as candidate. Official and high confidence, but single source; a second source (another KNMI station or Eurostat) would clear it. |
| C3 | HEAT_0006 (boiler 84 to 92%, 1999), HEAT_0003 and HEAT_0010 (Tier 3) | Keep as candidates. Low confidence. |
| C4 | HEAT_0007 (KEMA calibration point) and ticket UQ-012 (KEMA 2009 vs 2012, about 2x apart) | Keep as candidate until UQ-012 is resolved. |
| C5 | HEAT_0008 (no published Dutch basil heat demand) | Keep as candidate. Single source. |
| C6 | The greenhouse heat demand model | Keep as candidate. It is calibrated to the conflicting KEMA point. |

## D. Values from PR #30 (fish growth and feed)

| # | Item | Recommendation |
|---|---|---|
| D1 | FISH_0001 (FCR 1.4 to 1.8, UVI 1.7), FISH_0002 (SRAC 282 feeding table), FISH_0003 (no feeding below 17 °C), FISH_0004 (growth at the optimum), FISH_0006 (UVI growth benchmark), FISH_0007 (UVI 32% protein pellet) | **Approve.** Tier 1 or 2, medium or high, corroborated. |
| D2 | FISH_0005 (optimum 27 to 29 °C; sources conflict) | Keep as candidate. |
| D3 | FISH_0008 (no thermal growth coefficient found; Tier 3) | Keep as candidate. |
| D4 | The tilapia growth and feed model, with temperature factors now taken from Santos 2013 measured growth (0.674 at 22 °C) and Baras 2001 above the optimum | Keep as candidate. It is a new model, revised after one validation run. |

## E. Values from PR #30 (validation against published systems)

| # | Item | Recommendation |
|---|---|---|
| E1 | Published-system observations: Knaus 2018 (Tier 2, medium), Savidov 2005 (Tier 1, low), Khater 2023 (Tier 2, medium) | Keep as candidates. Each is single source. They are used only as comparison targets, so they don't need to be approved to be useful. |
| E2 | Tickets UQ-013 to UQ-015 | Nothing to approve. They record the gaps the validation found: 7 of 11 metrics are more than 25% off (fish growth is too slow below 27 °C, basil yield doesn't respond to density or light, and the N balance is off for gravel beds). |

## F. Validation fixes (PR #30)

| # | Item | Recommendation |
|---|---|---|
| F1 | FISH_0009 (Santos 2013 growth by temperature), BYR_0001 (density trial), BYR_0002 (light response) | **Approve.** Tier 2, medium, corroborated. |
| F2 | BYR_0003 (low light, single source) | Keep as candidate. |
| F3 | The basil yield response model (density exponent 0.394 from Ciriello 2021; DLI points from Dou 2018 and Walters 2023) | Keep as candidate. It is a fitted model; it is 1.0 at the UVI anchor, so the existing results don't change. |
| F4 | Validation after the fixes: 6 of 12 metrics more than 25% off (was 7 of 11). UQ-013 and UQ-014 are fixes in review; UQ-015 (gravel-bed N balance) stays open. | Nothing to approve. |

## Related Notes

- [[Project/Approval Batch 002|Approval Batch 002]]
- [[Project/Save Points|Save Points]]
- [[Project/Simulation Progress Tracker|Simulation Progress Tracker]]
