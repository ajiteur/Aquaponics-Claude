# Simulation Progress Tracker

Goal: make the simulation as strong as possible, for the Netherlands and India in parallel, and ready to extend to more markets. The farm go/no-go is shelved for now (Ajit, 2026-11-25).

Progress is counted as checkpoints done out of the total, with each checkpoint weighted equally. A checkpoint counts as done only when its work is merged on `main`. The Gatekeeper updates this note at every save point and PR review.

Last updated: 2026-11-26, after Approval Batch 003. PR #28 now carries PRs #29 and #30, so these ticks hold once #28 merges.

## Overview

| Sub-goal | Progress | Done |
|---|---|---|
| 1. Accurate biology | `████████████████████` 100% | 5 of 5 |
| 2. Complete components | `████████░░░░░░░░░░░░` 40% | 2 of 5 |
| 3. Swaps and trade-offs | `████████████████████` 100% | 3 of 3 |
| 4. Multi-market | `████████████████████` 100% | 3 of 3 |
| **All** | `████████████████░░░░` **81%** | **13 of 16** |

Done does not mean validated: sub-goal 1's validation check still shows 6 of 12 metrics more than 25% off.

## 1. Accurate biology

- [x] Nitrification model: biofilm capacity with TAN, pH, temperature and DO limits (candidate)
- [x] Nitrate removal: water exchange plus a calibrated residual loss (PR #21; the residual loss is a candidate)
- [x] Heating and climate: water and air temperature, and the heating load per site (PR #30; model is a candidate)
- [x] Fish growth and feed: tilapia growth to harvest, driving feed input (PR #30; model is a candidate)
- [x] Validation against real farm data, not only calibration to UVI (PR #30, done as a check: 3 systems, 6 of 12 metrics fail after candidate fixes; UQ-015 open)

## 2. Complete components

- [x] Component catalog v1 and cost-per-kg configurator (PR #15)
- [x] Equipment inventory research (project files `equipment-inventory/`)
- [ ] Close the 8 P1 gaps from the inventory research (in review: 7 of 8 filled or recorded; Telangana state rates can't be downloaded)
- [ ] Add the missing component categories (in review: lighting, monitoring, water treatment, backup power, harvest, propagation; fish handling has no priced part)
- [ ] Netherlands and India prices on every part (in review: every role, two with a written reason; a test checks it)

## 3. Swaps and trade-offs

- [x] Configurator v1: pick parts, get cost per kg by part
- [x] Side-by-side alternatives for each component (PR #29, `compare_swaps.py`)
- [x] A trade-off report per swap (cost, output, water, risk) (PR #29, Learnings/Swap Trade-offs)

## 4. Multi-market

- [x] Netherlands and four Indian states (Karnataka, Tamil Nadu, Andhra Pradesh, Telangana) as input sets
- [x] Every price tagged with its market (PR #29; `audit_market_tags.py` has 14 open flags)
- [x] A test showing that adding a country needs data only, not code (PR #29)

## How to update

1. Tick a checkpoint when its PR merges, and note the PR.
2. Recount the bars: done / total per sub-goal, 20 characters wide, rounded down to whole characters.
3. New checkpoints can be added when Ajit agrees. Adding one lowers the percentage, which is expected.

## Related Notes

- [[Project/Save Points|Save Points]]
- [[Project/Status and Roadmap|Status and Roadmap]]
- [[Project/Feasibility Register|Feasibility Register]]
