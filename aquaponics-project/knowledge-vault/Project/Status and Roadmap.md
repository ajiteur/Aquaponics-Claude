# Status and Roadmap

Last updated: 2026-11-25

## Plan

1. **Get the repo running again.** Done 2026-11-25. All tests pass, and the project moved to the `Aquaponics-Claude` repo.
2. **First end-to-end basil prediction.** In progress. Basil can now be simulated to a harvest, calibrated to the UVI yield anchor (merged in PR #1, values accepted). A gross revenue range now exists: about €148 to €222 per m² per year, as a scenario estimate (PR #3; updated after the nitrate uptake fix). Costs come with step 3.
3. **Real-farm viability check.** Not started. Needs your inputs: location, scale, budget, energy and heating costs, local basil prices.
4. **The fork.** If viable, a pilot farm design spec. If not, an original aquaponics simulation game built on the same engine.

## Known weak spots in the engine

- Nitrification and basil nitrate uptake now use sourced candidate models (PR #6 and follow-up), but nitrogen has no sink besides plant shoots, so nitrate builds up well above UVI's measured levels at UVI-scale feed.
- The raft nitrification capacity is about 10 times higher per m² than published biofilm rates; this needs a closer look.
- Standing plant biomass still grows at a fixed 4 g per plant per day. Only harvestable mass is calibrated.
- Two cost inputs in the unit-economics example (variable cost per kg, a €500 batch fixed cost) are constructed placeholders, not evidence.

## Related Notes

- [[Project/Project|Project]]
- [[Project/Decisions Log|Decisions Log]]
