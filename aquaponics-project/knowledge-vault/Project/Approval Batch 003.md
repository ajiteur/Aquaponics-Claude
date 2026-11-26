# Approval Batch 003

Open. When it's ready, reply "approve batch 003 as recommended", or list the item numbers you want changed. Approvals are then recorded next to each value (who, date, scope).

Opened: 2026-11-26, while Ajit is away. Rule used (AGENTS.md 6A): approve medium or high confidence items that Tier 1 or Tier 2 sources corroborate. Single-source, Tier 3, low-confidence, conflicting and calibrated items stay candidates.

## A. Merge order

Each PR is stacked on the one before it, so merge them in this order.

| # | PR | Recommendation |
|---|---|---|
| A1 | #28: record Approval Batch 002, save-point-002 entry | **Merge first.** Tag `save-point-002` on the merge commit. |
| A2 | #29: swaps checkpoint (`compare_swaps.py`, heat-pump heating source, NFT and media-bed alternatives) | **Merge second.** Re-reviewed at `c5e1042`: tests (204), integrity and syncs pass. |
| A3 | #30: heating and climate checkpoint (`heat_demand.py`, greenhouse heat models) | **Merge third.** Stacked on #29 at `45509ab`. With #28, #29 and #30 combined, tests, integrity and syncs pass. |

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

## Related Notes

- [[Project/Approval Batch 002|Approval Batch 002]]
- [[Project/Save Points|Save Points]]
- [[Project/Simulation Progress Tracker|Simulation Progress Tracker]]
