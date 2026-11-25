# Status and Roadmap

Last updated: 2026-11-25

## Plan

1. **Get the repo running again.** Done 2026-11-25. All tests pass, and the project moved to the `Aquaponics-Claude` repo.
2. **First end-to-end basil prediction.** In progress. Basil can now be simulated to a harvest, calibrated to the UVI yield anchor (merged in PR #1, values accepted). A gross revenue range now exists: about €93 to €222 per m² per year, as a scenario estimate (PR #3). Costs come with step 3.
2a. **Find a unit design whose economics work.** In progress. First comparison of five designs in the Netherlands and India (labour + electricity only): in the Netherlands, hired basil labour must stay under about 0.22-0.49 h/kg, which no sourced basil system reaches yet; owner-operated or very lean large raceways are the candidates. India clears labour and power in every case but its price evidence is weak.
3. **Real-farm viability check.** Not started. Needs your inputs: location, scale, budget, energy and heating costs, local basil prices.
4. **The fork.** If viable, a pilot farm design spec. If not, an original aquaponics simulation game built on the same engine.

## Known weak spots in the engine

- The nitrification and TAN model is a placeholder and can't carry UVI-scale feed loads.
- The basil pH score uses hydroponic ranges, so it scores 0 across the whole aquaponic pH range.
- Standing plant biomass still grows at a fixed 4 g per plant per day. Only harvestable mass is calibrated.
- Two cost inputs in the unit-economics example (variable cost per kg, a €500 batch fixed cost) are constructed placeholders, not evidence.

## Related Notes

- [[Project/Project|Project]]
- [[Project/Decisions Log|Decisions Log]]
