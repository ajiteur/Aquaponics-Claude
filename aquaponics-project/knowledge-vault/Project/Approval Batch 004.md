# Approval Batch 004

Open. When it's ready, reply "approve batch 004 as recommended", or list the item numbers you want changed. Approvals are then recorded next to each value (who, date, scope).

Opened: 2026-11-26, against `main` at `dc07134` (save-point-003). Rule used (AGENTS.md 6A, as in Batches 002 and 003): approve medium or high confidence items that are corroborated. For catalog prices, corroborated Tier 3 listings are approved for scenario use only, as in Batch 002 E1. Single-source, low-confidence, conflicting and fitted items stay candidates.

## A. Merge order

| # | PR | Recommendation |
|---|---|---|
| A1 | #31: basil density and light fixes, gravel beds counted as media volume (validation fixes) | **Merge first.** Tests, integrity and syncs pass, and it merges cleanly with main. |
| A2 | #32: the three component checkpoints (P1 gaps, missing categories, NL and India prices on every part) | **Merge second**, once its thread has stacked it on #31 (both edit the Findings and Decisions logs). With #31 combined, 244 tests pass. When it lands, the tracker reaches 16 of 16. |

## B. PR #31 (biology)

| # | Item | Recommendation |
|---|---|---|
| B1 | BYR_0005 (single-harvest basil yield in deep-flow, Tier 2, medium, corroborated) and NITR_0015 (trickling-filter TAN removal per m², Tier 2, medium, corroborated) | **Approve.** |
| B2 | BYR_0004 (low, single source), NITR_0013 (FAO media-bed sizing), NITR_0014 (SRAC 453 trickling-filter loading), NITR_0016 (raft surface nitrification), all single source | Keep as candidates. |
| B3 | The changed basil yield response (closed-canopy density, Knaus light re-derived) and the gravel-bed media-volume nitrification | Keep as candidates. They are fitted model changes. |
| B4 | Tickets UQ-015 and UQ-016 | Nothing to approve. |

## C. PR #32 (components)

| # | Item | Recommendation |
|---|---|---|
| C1 | The 5 new prices with medium confidence that are corroborated (Tier 3 listings): LED lights Lumatek Zeus 600 and SanLight EVO 4-120 (NL), the pH tester (NL), KOH pH base, and one India part | **Approve for scenario use.** Good enough for cost-per-kg ranges, not for a quote. |
| C2 | The other 22 new catalog entries (low confidence, single source or conflicting) and the 6 priced rows in `candidates_batch_004_v0.jsonl` | Keep as candidates. |
| C3 | The two NL backup generators now wired into the catalog | Nothing to do. They were approved in Batch 002 E1. |
| C4 | Telangana MIDH 2025-26 state rates | Still a gap. The site can't be downloaded from the cloud or from your PC. It needs an Indian network or a VPN. |

## Related Notes

- [[Project/Approval Batch 003|Approval Batch 003]]
- [[Project/Save Points|Save Points]]
- [[Project/Simulation Progress Tracker|Simulation Progress Tracker]]
