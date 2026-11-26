# Approval Batch 002

Open. Items are added as they come in. When it's ready, reply "approve batch 002 as recommended", or list the item numbers you want changed. Approvals are then recorded next to each value (who, date, scope).

Opened: 2026-11-26, against `main` at `6198b51` (save-point-001 is `07ce825`).

Rule used for the recommendations (AGENTS.md 6A): approve items with medium or high confidence that Tier 1 or Tier 2 sources corroborate. Single-source, Tier 3, low-confidence and calibrated items stay candidates. The simulation uses candidates anyway, so keeping one as a candidate doesn't stop any work.

## A. Pull requests to merge

| # | Item | Recommendation |
|---|---|---|
| A0 | PRs #21, #23, #24 and #25 | Merged. |
| A1 | PR #21 (merged): nitrate removal by water exchange and a calibrated residual loss | **Merge.** Tests, the full integrity check, and the canon and vault syncs pass, and it merges cleanly with main. At the UVI feed ratio, nitrate now holds near 43 mg/L instead of climbing to about 161. That match is by construction, since the loss is calibrated to UVI's 42 mg/L, so it is not a validation. The starter fixture becomes nitrate-limited again (about 21 mg/L by day 28) and harvests 1.44 kg/m² instead of 1.91. Small follow-up: the unit-design inputs' bias note still cites 1.91. |

| A2 | PR #26: MIDH 2025 protected-cultivation norms as candidates | **Merge.** Tests, the integrity check and the canon sync pass, and it merges cleanly. Catalog values aren't changed until F1 is approved. |

## B. Scenario inputs (scenario estimates only, never canon)

| # | Item | Recommendation |
|---|---|---|
| B1 | Basil prices for Tamil Nadu, Andhra Pradesh and Telangana, and the all-India band (₹600 to ₹1,000, one 2025 Andhra study) | **Keep as candidates.** No state-level evidence, and Bangalore evidence puts real prices about 2.5 to 10 times lower. |
| B2 | Sensitivity locations: the ₹600 to ₹1,000 study band and the Bengaluru listings at ₹65 to ₹180 | Keep as sensitivity cases. They aren't base inputs, so they don't need approval. |
| B3 | Netherlands lettuce auction price (Flemish VBT weekly prices, configuration C) | Keep as candidate. Single source, low confidence. |

## C. Candidate model values in canon

| # | Item | Recommendation |
|---|---|---|
| C1 | Nitrate sinks: water exchange 1.5% of volume per day (PR #21) | **Approve.** Tier 1 and corroborated (NITR_0009). |
| C2 | Nitrate sinks: residual loss of 0.735 of nitrified N, calibrated to UVI's basil nitrate mean (PR #21) | **Keep as candidate.** It's a fitted value that runs through two other candidate models. Its size agrees with an independent N budget (Yang and Kim), but that only makes it plausible. |
| C3 | Catalog: EPS/XPS raft lifetimes, `media_bed_depth_m`, `raft_air_share_of_fish_air` (carried over from batch 001) | Keep as candidates until a durability source and a design check resolve the conflicts. |

## D. Candidate truths

| # | Truths | Recommendation |
|---|---|---|
| D1 | NITR_0009, NITR_0010 (medium, Tier 1, corroborated) | **Approve.** |
| D2 | NITR_0011 (low, single source), NITR_0012 (medium, single Tier 2 source) | Keep as candidates. |

## E. P1 equipment research (PR #25, 51 candidates)

| # | Item | Recommendation |
|---|---|---|
| E1 | The 12 candidates with medium or high confidence that are corroborated: India Tier 1 structure lives, the NHB tubular shade net norm (₹710 to ₹816/m²) and rooftop solar support (₹18,000 to ₹30,000/kWp); the Bangalore water price rise; NL backup power (generators €649 to €706, LiFePO4 batteries €510 to €882) | **Approve for scenario use.** |
| E2 | The other 39 (single-source, low-confidence or conflicting, including the NL trough walls and heating) | Keep as candidates. |

## F. MIDH 2025 norms (PR #26)

| # | Item | Recommendation |
|---|---|---|
| F1 | Use the MIDH 2025 norms (Tier 1, official) as the India reference for protected structures, replacing the older catalog ranges: naturally ventilated polyhouse ₹650 to ₹935/m² becomes ₹1,000 to ₹1,200, bamboo shade net ₹200 to ₹414/m² becomes ₹450 | **Approve for scenario use**, labelled as subsidy cost ceilings, not market prices. |
| F2 | The 50% central subsidy | Keep as a sensitivity case (with and without the subsidy), not a base input. Eligibility isn't known yet, and state top-ups aren't read. |

## Related Notes

- [[Project/Approval Batch 001|Approval Batch 001]]
- [[Project/Save Points|Save Points]]
- [[Project/Feasibility Register|Feasibility Register]]
