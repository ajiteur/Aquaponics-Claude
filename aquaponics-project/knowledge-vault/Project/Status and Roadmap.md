# Status and Roadmap

Last updated: 2026-11-26

## Plan

1. **Get the repo running again.** Done 2026-11-25. All tests pass, and the project moved to the `Aquaponics-Claude` repo.
2. **First end-to-end basil prediction.** In progress. Basil can now be simulated to a harvest, calibrated to the UVI yield anchor (merged in PR #1, values accepted). A gross revenue range now exists: about €111 to €222 per m² per year, as a scenario estimate rerun after the nitrification fix (PR #6), the nitrate uptake fix (PR #11) and nitrate removal. The high end needs fish feed sized to the UVI ratio. Costs come with step 3.
2a. **Find a unit design whose economics work.** In progress. First comparison of five designs in the Netherlands and India (labour + electricity only): in the Netherlands, hired basil labour must stay under about 0.25-0.50 h/kg, which no sourced basil system reaches yet; owner-operated or very lean large raceways are the candidates. In India at the Bangalore price (₹65-180/kg, confirmed by Ajit) wholesale basil barely covers labour and power, so India would need a higher-value channel or crop.
2b. **Component library and configurator.** First checkpoint in review: 25 sourced parts for the Netherlands and India, tilapia, basil and lettuce sizing, and a configurator that reports cost per kg by component, water, feed, energy and minimum area (see [[Project/How to Add Components|How to Add Components]]). First scenario estimate: basil cost per kg sits above the Dutch wholesale price band and overlaps the Bangalore band, before fish income is credited. Component checkpoints in review (2026-11-26): every part role now has a Netherlands and an India price (or a written reason), and lighting, monitoring, water treatment, backup power, harvest crates and propagation exist as add-ons. Most new parts lack a sourced lifetime, and Telangana's state rates can't be downloaded.
3. **Real-farm viability check.** Not started. Needs your inputs: location, scale, budget, energy and heating costs, local basil prices.
4. **The fork.** If viable, a pilot farm design spec. If not, an original aquaponics simulation game built on the same engine.

## Known weak spots in the engine

- ~~The nitrification and TAN model is a placeholder and can't carry UVI-scale feed loads.~~ Addressed in PR #6 (candidate, pending Ajit's review).
- ~~The basil pH score uses hydroponic ranges, so it scores 0 across the whole aquaponic pH range.~~ Addressed in PR #6 (candidate, pending Ajit's review).
- ~~Nitrate uptake is a placeholder that scales with the plant score.~~ Replaced with growth-based uptake in PR #11 (candidate).
- ~~Nitrogen has no sink besides plant shoots, so nitrate builds up well above UVI's level.~~ Water exchange and a calibrated residual loss added (candidate, Batch 002). The residual loss is calibrated to one site, so it is low confidence.
- The raft nitrification capacity is about 10 times higher per m² than published biofilm rates; this needs a closer look.
- ~~Heating cost uses a transferred pepper figure (21-30 m³ gas/m²).~~ A climate-driven heat demand model for the Netherlands and Karnataka now exists (candidate, Batch 003). Basil at 24 to 26 °C comes out at about 67 to 88 m³ gas/m²/yr with a night screen. The calibration point conflicts with an older KEMA figure (UQ-012), and Karnataka fan-pad cooling (about ₹157 to ₹389 per m² a year) rests on one low-confidence energy figure.
- ~~Fish growth is feed / FCR x fish score x 0.8 (placeholder).~~ A sourced feed, FCR and temperature model is in (candidate, Batch 003), opt-in for the basil raft scenarios. Its 22 to 27 °C slope may be too steep; no thermal growth coefficient was found.
- Validation against three published systems: 3 of 12 metrics fail after the second round of candidate fixes (closed-canopy basil density, corrected Knaus light, gravel beds as media volume; UQ-014 and UQ-015 in review). Still open: basil grown from young transplants (UQ-016), Savidov fish weight (−25%) and Khater FCR (+84%, which may lie in the paper).
- Standing plant biomass still grows at a fixed 4 g per plant per day. Only harvestable mass is calibrated.
- Two cost inputs in the unit-economics example (variable cost per kg, a €500 batch fixed cost) are constructed placeholders, not evidence.

## Related Notes

- [[Project/Project|Project]]
- [[Project/Decisions Log|Decisions Log]]
