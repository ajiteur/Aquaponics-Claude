# Status and Roadmap

Last updated: 2026-11-25

## Plan

1. **Get the repo running again.** Done 2026-11-25. All tests pass, and the project moved to the `Aquaponics-Claude` repo.
2. **First end-to-end basil prediction.** In progress. Basil can now be simulated to a harvest, calibrated to the UVI yield anchor (merged in PR #1, values accepted). A gross revenue range now exists: about €148 to €222 per m² per year, as a scenario estimate rerun after the nitrification fix (PR #6) and the nitrate uptake fix (PR #11). Costs come with step 3.
2a. **Find a unit design whose economics work.** In progress. First comparison of five designs in the Netherlands and India (labour + electricity only): in the Netherlands, hired basil labour must stay under about 0.25-0.50 h/kg, which no sourced basil system reaches yet; owner-operated or very lean large raceways are the candidates. In India at the Bangalore price (₹65-180/kg, confirmed by Ajit) wholesale basil barely covers labour and power, so India would need a higher-value channel or crop.
2b. **Component library and configurator.** First checkpoint in review: 25 sourced parts for the Netherlands and India, tilapia, basil and lettuce sizing, and a configurator that reports cost per kg by component, water, feed, energy and minimum area (see [[Project/How to Add Components|How to Add Components]]). First scenario estimate: basil cost per kg sits above the Dutch wholesale price band and overlaps the Bangalore band, before fish income is credited.
3. **Real-farm viability check.** Not started. Needs your inputs: location, scale, budget, energy and heating costs, local basil prices.
4. **The fork.** If viable, a pilot farm design spec. If not, an original aquaponics simulation game built on the same engine.

## Known weak spots in the engine

- ~~The nitrification and TAN model is a placeholder and can't carry UVI-scale feed loads.~~ Addressed in PR #6 (candidate, pending Ajit's review).
- ~~The basil pH score uses hydroponic ranges, so it scores 0 across the whole aquaponic pH range.~~ Addressed in PR #6 (candidate, pending Ajit's review).
- ~~Nitrate uptake is a placeholder that scales with the plant score.~~ Replaced with growth-based uptake in PR #11 (candidate).
- Nitrification and basil nitrate uptake now use sourced candidate models (PR #6 and follow-up), but nitrogen has no sink besides plant shoots, so nitrate builds up well above UVI's measured levels at UVI-scale feed.
- The raft nitrification capacity is about 10 times higher per m² than published biofilm rates; this needs a closer look.
- Standing plant biomass still grows at a fixed 4 g per plant per day. Only harvestable mass is calibrated.
- Two cost inputs in the unit-economics example (variable cost per kg, a €500 batch fixed cost) are constructed placeholders, not evidence.

## Related Notes

- [[Project/Project|Project]]
- [[Project/Decisions Log|Decisions Log]]
