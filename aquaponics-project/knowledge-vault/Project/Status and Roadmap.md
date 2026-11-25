# Status and Roadmap

Last updated: 2026-11-25

## Plan

1. **Get the repo running again.** Done 2026-11-25. All tests pass, and the project moved to the `Aquaponics-Claude` repo.
2. **First end-to-end basil prediction.** In progress. Basil can now be simulated to a harvest, calibrated to the UVI yield anchor (merged in PR #1, values accepted). A gross revenue range now exists: about €60 to €222 per m² per year, as a scenario estimate. It was rerun after the nitrification fix, and the high end needs fish feed sized to the UVI ratio. Costs come with step 3.
3. **Real-farm viability check.** Not started. Needs your inputs: location, scale, budget, energy and heating costs, local basil prices.
4. **The fork.** If viable, a pilot farm design spec. If not, an original aquaponics simulation game built on the same engine.

## Known weak spots in the engine

- ~~The nitrification and TAN model is a placeholder and can't carry UVI-scale feed loads.~~ Addressed in PR #6 (candidate, pending Ajit's review). The UVI feed-ratio run now holds TAN around 2.3 mg/L.
- ~~The basil pH score uses hydroponic ranges, so it scores 0 across the whole aquaponic pH range.~~ Addressed in PR #6 (candidate, pending Ajit's review).
- Nitrate uptake is a placeholder that scales with the plant score. That's why the starter basil fell to 0.77 kg/m² once PR #6 raised the basil plant score.
- Standing plant biomass still grows at a fixed 4 g per plant per day. Only harvestable mass is calibrated.
- Two cost inputs in the unit-economics example (variable cost per kg, a €500 batch fixed cost) are constructed placeholders, not evidence.

## Related Notes

- [[Project/Project|Project]]
- [[Project/Decisions Log|Decisions Log]]
