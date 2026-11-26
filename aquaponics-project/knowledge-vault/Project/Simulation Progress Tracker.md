# Simulation Progress Tracker

Goal: make the simulation as strong as possible, for the Netherlands and India in parallel, and ready to extend to more markets. The farm go/no-go is shelved for now (Ajit, 2026-11-25).

Progress is counted as checkpoints done out of the total, with each checkpoint weighted equally. A checkpoint counts as done only when its work is merged on `main`. The Gatekeeper updates this note at every save point and PR review.

Last updated: 2026-11-26, after Approval Batch 002 (PRs #21 to #28). No checkpoint changed: Batch 002 moved part of sub-goals 2 and 4 forward (MIDH norms, 12 approved equipment values), but no checkpoint is complete yet.

## Overview

| Sub-goal | Progress | Done |
|---|---|---|
| 1. Accurate biology | `████████░░░░░░░░░░░░` 40% | 2 of 5 |
| 2. Complete components | `████████░░░░░░░░░░░░` 40% | 2 of 5 |
| 3. Swaps and trade-offs | `██████░░░░░░░░░░░░░░` 33% | 1 of 3 |
| 4. Multi-market | `██████░░░░░░░░░░░░░░` 33% | 1 of 3 |
| **All** | `███████░░░░░░░░░░░░░` **38%** | **6 of 16** |

## 1. Accurate biology

- [x] Nitrification model: biofilm capacity with TAN, pH, temperature and DO limits (candidate)
- [x] Nitrate removal: water exchange plus a calibrated residual loss (PR #21; the residual loss is a candidate)
- [ ] Heating and climate: water and air temperature, and the heating load per site (in review, PR #30)
- [ ] Fish growth and feed: tilapia growth to harvest, driving feed input (in review, PR #30)
- [ ] Validation against real farm data, not only calibration to UVI (in review, PR #30: 3 systems, 6 of 12 metrics fail after candidate fixes; UQ-015 open)

## 2. Complete components

- [x] Component catalog v1 and cost-per-kg configurator (PR #15)
- [x] Equipment inventory research (project files `equipment-inventory/`)
- [ ] Close the 8 P1 gaps from the inventory research
- [ ] Add the missing component categories
- [ ] Netherlands and India prices on every part

## 3. Swaps and trade-offs

- [x] Configurator v1: pick parts, get cost per kg by part
- [ ] Side-by-side alternatives for each component
- [ ] A trade-off report per swap (cost, output, water, risk)

## 4. Multi-market

- [x] Netherlands and four Indian states (Karnataka, Tamil Nadu, Andhra Pradesh, Telangana) as input sets
- [ ] Every price tagged with its market
- [ ] A test showing that adding a country needs data only, not code

## How to update

1. Tick a checkpoint when its PR merges, and note the PR.
2. Recount the bars: done / total per sub-goal, 20 characters wide, rounded down to whole characters.
3. New checkpoints can be added when Ajit agrees. Adding one lowers the percentage, which is expected.

## Related Notes

- [[Project/Save Points|Save Points]]
- [[Project/Status and Roadmap|Status and Roadmap]]
- [[Project/Feasibility Register|Feasibility Register]]
