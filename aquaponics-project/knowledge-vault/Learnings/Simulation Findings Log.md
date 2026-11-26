# Simulation Findings Log

What the simulation shows, newest first. These are **scenario estimates, not validated**: they describe the model, not the real world, and they are never truths.

## 2026-11-26: Validation fixes, basil density and light, tilapia temperature curve (scenario estimate, not validated)

Rerun of `python scripts/validate_published_systems.py` after two candidate fixes (pending Batch 003). The previous run is the entry below and is left as it was, so you can compare the two.

- **Tilapia temperature factor** now follows measured growth rates (Santos et al. 2013, three strains). At 22 °C it is 0.674 of the 28 to 30 °C rate (was 1/3). The old point read SRAC 283's "three times greater growth" as a daily rate, but that ratio applies to final weight over a grow-out, not to daily growth. Full rate runs to 33 °C, falling to 0.745 at 37 °C (Baras 2001).
- **Basil** per-plant growth now falls with planting density: yield per m² scales with density to the power 0.394, fitted to Ciriello 2021's raft trial. It also falls with daily light integral (DLI) below about 16.5 mol/m²/d (Dou 2018, Walters 2023). At the UVI anchor (8 plants/m², tropical light) nothing changes, by construction.

| Metric | Before | After |
|---|---|---|
| Knaus fish end biomass | −8% | −7% ✓ |
| Knaus FCR | +21% | +16% ✓ |
| Knaus TAN | +115% | +115% ✗ (gravel-bed N issue, left open) |
| Knaus NO3-N | −32% | −11% ✓ |
| Knaus basil per plant | +670% | +30% (DLI 4.8) to +441% (DLI 12.7) ✗ |
| Savidov basil per m² per year at its density | +286% | +68% ✗ |
| Savidov basil at UVI density (reference) | −3% | −3% ✓ |
| Savidov fish harvest weight | −38% | −25% (just over the bar) |
| Khater fish gain, mid / high table feed | −36% / −20% | −10% / 0% ✓ |
| Khater FCR | +166% | +84% ✗ |
| UVI grow-out, mid table at UVI temperatures | −34% | −24% |

- **6 of 12 metrics now fail, down from 7 of 11.** The Knaus basil metric is now two metrics, one for each DLI reading.
- **Basil is still too high.** Knaus's photoperiod isn't reported, so its DLI could be anywhere from 4.8 to 12.7, which is why the result spans +30 to +441 percent. Savidov's +68 percent may come from extrapolating a baby-leaf density trial down to 32 plants/m².
- **Khater's published FCR (0.92 to 1.20) sits below the Tier 1 range of 1.4 to 1.8**, so part of that gap may lie in the paper rather than the model.
- **No change in the crop-cycle scenarios:** they run at 28 °C, 8 plants/m² and no DLI set.

## 2026-11-26: Validation against three published systems beyond UVI (scenario estimate, not validated)

Run: `python scripts/validate_published_systems.py` (results in `data/simulation/results/published_system_validation.json`; observations in `data/knowledge/validation/published_system_observations.json`). A metric fails when the model is more than 25 percent off.

| System | Metric | Model | Published | Error |
|---|---|---|---|---|
| Knaus 2018, Rostock (tilapia, gravel beds, 70 days) | Fish end biomass | 17.8 kg | 19.45 kg | −8% ✓ |
| | FCR | 1.87 | 1.54 | +21% ✓ |
| | TAN mean | 0.45 mg/L | 0.21 | +115% ✗ |
| | NO3-N mean | 10.5 mg/L | 15.6 (SD 8.4) | −32% ✗ |
| | Basil fresh per plant | 124 g | 16.1 g | +670% ✗ |
| Savidov 2005, Alberta (tilapia + basil raft) | Basil per m² per year at 31.8 plants/m² | 99 kg | 25.7 kg | +286% ✗ |
| | Basil per m² per year at UVI density | 25.0 kg | 25.7 kg | −3% ✓ |
| | Fish harvest weight (24 weeks, 24.8 °C) | 392 g | about 630 g | −38% ✗ |
| Khater 2023, Egypt (tilapia + lettuce, 23.5 °C) | Fish gain per day (table feed, mid/high) | 0.68 / 0.84 g | 1.05 to 1.36 g | −36% / −20% |
| | FCR | 3.2 | 0.92 to 1.20 | +166% ✗ |

Where it fails:
- **Fish grow too slowly below 27 °C.** This shows up in three systems (Savidov at 24.8 °C, Khater at 23.5 °C, and UVI's winters) but not at 26.3 °C (Knaus, −8 percent). The straight-line temperature factor between 22 and 27 °C is the likely cause. Ticket UQ-013.
- **Basil yield does not respond to plant density or light.** It matches Savidov per m² only if the UVI density is assumed. At Savidov's real density, or under Knaus's dim autumn light, it is far too high. Ticket UQ-014.
- **The nitrogen balance is off for a small gravel-bed system.** TAN is too high (gravel is counted as raft area) and nitrate too low (the UVI-calibrated loss is probably too strong at low feed). Ticket UQ-015.
- **What held up:** fish growth at a near-optimal 26 °C, and basil yield per m² at the UVI density in a second raft system.
- Caveats: Savidov's yield period and fish harvest weight are derived, the report is low confidence, and Knaus mixed basil with mint and parsley.

## 2026-11-26: Fish growth and feed, tilapia (scenario estimate, not validated)

Run: `python src/fish_growth.py` (UVI check) and `src/simulate_crop_cycle.py`, 28 days, on both basil raft scenarios. Fish gain is now feed x temperature factor / FCR 1.7, replacing the placeholder feed / FCR x fish score x 0.8. All new values are candidates pending Batch 003.

- **Feeding at the SRAC 282 table brackets UVI's measured growth.** Starting from UVI's 79 g fish at UVI's 24 to 29 °C, the mid table rate gives 537 g after 24 weeks, the low rate 283 g and the high rate 1,021 g. UVI measured 814 g. At a steady 28 °C, the mid rate gives 721 g (11 percent low). UVI fed to satiation, which seems to sit in the upper half of the table.
- **The temperature curve may be too harsh at 24 °C.** It gives 60 percent of full growth at 24 °C, but UVI reported only a "slight growth depression" in its 24 °C winter. The straight line from 22 to 27 °C is an assumption between sourced points, and a measured thermal growth coefficient would settle it.
- **In the crop-cycle scenarios fish grow from 80 g to 94.3 g in 28 days (was 92.8 g).** Feed is still the scenario's 1 percent of body weight a day (Mode A input). Basil yield and revenue barely move.
- **Feeding the UVI feed-ratio fish at the table rate (about 2.25 percent) would overload the raft.** TAN climbs to about 94 mg/L in 28 days. So at table feeding the same raft carries only about 45 percent of that stock. This is a sensitivity run only; the committed scenarios keep 1 percent.

## 2026-11-26: Heating and climate, NL glasshouse and Karnataka polyhouse (scenario estimate, not validated)

Run: `python src/heat_demand.py` (results in `data/simulation/results/greenhouse_heat_demand.json`). An hourly heat balance on a mean day per month from KNMI De Bilt and IMD Bengaluru 1991-2020 normals. The loss coefficient is calibrated to KEMA 2012's Venlo radish figure. All values are candidates pending Batch 003.

| Netherlands glasshouse setpoint | Heat demand (m³ gas eq. per m² per year) | Gas (m³/m²/yr) | Gas cost (€/m²/yr) |
|---|---|---|---|
| 10 °C, basil chilling floor only | 13 to 17 | 15 to 21 | 20 to 30 |
| 24 °C day and night, with night screen | 61 to 64 | 67 to 76 | 89 to 111 |
| 26 °C day and night, with night screen | 71 to 74 | 77 to 88 | 103 to 128 |
| 26 °C day and night, no screen | 89 to 102 | 97 to 122 | 130 to 177 |

- **Heating basil to its preferred 26 °C in a Dutch glasshouse would cost about €100 to €130 per m² per year in gas with a night screen, and more without one.** The basil gross revenue scenario was €154 to €222 per m² per year (UVI feed-ratio case), so heat alone would take roughly half or more. These are scenario estimates; total operating cost is not claimed.
- **The model checks out against a second KEMA figure (cold pot plant, 15/13 °C, screened) to within 3 to 6 percent.** It overshoots a chrysanthemum figure by 25 to 40 percent, but that one is probably lit and may be gas use, not heat demand.
- **The basil cases are an extrapolation.** The model is calibrated between 8 and 15 °C, and no published Dutch basil heat demand exists. Lit tomato uses about 32 m³/m² and warm Phalaenopsis 50 to 90, so basil at 24 to 26 °C landing at 61 to 88 sits where a warm crop would.
- **The biggest open uncertainty is KEMA's own radish number.** KEMA 2009 gives about 5.4 m³/m² for the same setpoints, against 12.0 in 2012. If 2009 is right, every Dutch figure here roughly halves (ticket UQ-012).
- **Karnataka needs no heating at 10 to 15 °C setpoints on mean nights.** Holding 24 to 26 °C at night would take about 74 to 252 kWh of heat per m² per year. Record lows went below basil's 10 °C chilling line in November to February, so cold-night protection may matter (low confidence: tertiary source).
- **Karnataka cooling is the larger question.** Outdoor air is above basil's preferred 27.5 °C for about 2,300 hours a year and above its tolerated 31 °C for about 600. Fan-pad cooling would use about 46 to 55 kWh per m² per year if run every day (low confidence: one North-West India source). At Karnataka's Batch 001 power rate (₹3.45 to ₹7.10 per kWh, low confidence, fixed charges excluded) that is about ₹157 to ₹389 per m² per year.

## 2026-11-26: Swaps checkpoint, NFT yield and Dutch NFT and media prices (scenario estimate, not validated)

Run: `run.bat swaps_basil_nl` and `run.bat swaps_basil_karnataka` again, after adding a sourced NFT-to-raft basil yield ratio of 0.83 to 0.95 (Blunk 2023, Pasch 2021) and Dutch prices for NFT channels (€16.75 to €18.61 per m) and expanded clay (€188 to €440 per m³). All are candidates pending Batch 003.

- **NFT now has a cost per kg: NL €4.42 / 5.89 / 7.73, Karnataka ₹50.81 / 72.37 / 99.00** (low / mid / high), against €10.04 and ₹133.49 mid for the raft. That is still not like-for-like (*). Channel metres per m² aren't sourced, so the channels are unpriced, and in NL the separate biofilter NFT needs has no price. Most of the drop comes from fish feed at 25% of the raft rate (SRAC 454, low confidence) and no raft aeration, so this is the least reliable swap in the table.
- **Media bed still has no cost per kg.** Knaus 2020 found no significant weight difference between gravel, raft and grow pipes, but its numbers sit in a table image that couldn't be read. A non-significant difference isn't turned into a ratio. With clay media the NL media bed costs €130 per m² per year mid, against €243 for the raft, before the clay's lifetime and the bed container, which are both gaps.

## 2026-11-26: Swaps checkpoint, side-by-side part swaps (scenario estimate, not validated)

Run: `run.bat swaps_basil_nl` and `run.bat swaps_basil_karnataka` (`scripts/compare_swaps.py`). Base: 100 m² tilapia + basil DWC raft, owner labour, mid case. Each row is the change against the base. A (*) means the swap opens cost gaps, so some of its costs are left out and the change is not like-for-like. New values are candidates pending Batch 003.

| Swap | NL change per kg basil (base €10.04) | Karnataka change per kg basil (base ₹133.49) |
|---|---|---|
| Media bed instead of raft (*) | n/a (no sourced yield); −€116 per m² per yr, −42 m³ water, −13,800 kWh | n/a; −₹1,676 per m² per yr, −42 m³ water |
| NFT instead of raft (*) | n/a (no sourced yield or channel layout) | n/a (same) |
| Air-water heat pump instead of gas boiler (*) | −€2.04 (+12,500 kWh, gas to zero); heat pump life not sourced | not applicable (no heating) |
| Heating off | −€3.44 (yield kept at the heated value, so this is an upper bound on heating cost) | not applicable |
| New IBC instead of used IBC | +€0.06 | — |
| EPS instead of XPS rafts | −€0.03 | — |
| Fan-and-pad polyhouse (*) | — | −₹9.67, but only because its life and power are not sourced |
| Shade net instead of polyhouse | — | −₹0.97 |
| FRP 750 L tanks instead of PVC 5,000 L | — | +₹11.35 |
| 90 m³ cement RAS tank instead of PVC | — | +₹5.89 |

- **In the Netherlands, heating is the biggest swap lever.** A heat pump at a seasonal COP of 3.7 to 4.6 roughly halves the heating line at current CBS gas and power prices, before its build cost (life not sourced).
- **Media bed and NFT can't be priced per kg yet.** With no sourced yield for basil in those systems, only cost per m² is shown. Fish feed falls to 25% of the raft rate (SRAC 454 factor, low confidence), which drives the drop in electricity and water.
- **In Karnataka, tank choice matters more than structure choice** among the parts priced so far. PVC biofloc tanks remain the cheapest per kg.
- **The Karnataka base is now ₹109.68 / 133.49 / 159.43 per kg** (low / mid / high), up from earlier runs because the MIDH 2025 polyhouse norm (Batch 002, F1) replaced the older range.

## 2026-11-26: Equipment P1 research, Batch 002 candidates (scenario estimate, not validated)

- Karnataka basil DWC configurator, mid case: INR 110.25 to 130.78 per kg of plant output (low to high case moves from 91.65-130.41 to 106.95-156.78). Why: polyhouse life (10-12 yr) and an India water price are now counted instead of left out as gaps. The water price is Chennai's commercial tariff (Rs 99-163/m3) used as a proxy, because no current Bengaluru tariff was found.
- Netherlands basil DWC: unchanged at EUR 8.27 / 10.04 / 12.21 per kg. The basil seed price added (EUR 0.0005-0.002 per seed) is too small to move it.
- All new values are candidates pending Batch 002 approval.

## 2026-11-25: Nitrate removal added (water exchange and filter-tank losses)

Run: `src/simulate_crop_cycle.py`, 28 days, both basil raft scenarios, with UVI-style solids handling assumed. Scenario estimate, not validated. New values are candidates pending Batch 002.

| Scenario | Nitrate-N (mg/L) over 28 days | Basil kg/m² | € per m² per year (cons. / base / opt.) |
|---|---|---:|---|
| Starter fixture (8 kg fish) | 41 → 21 (was 42 → 38) | 1.44 (was 1.91) | 111 / 135 / 160 |
| UVI feed ratio | 42 → 43 (was 45 → 161) | 1.99 | 154 / 187 / 222 |

- **At the UVI feed ratio, nitrate now holds near UVI's measured 42 mg/L** instead of building up to about 161. This is by construction: the residual loss is calibrated to that anchor.
- **About 73 percent of nitrified N is lost to denitrification and solids** in the calibration, roughly 42 percent of feed N. A peer-reviewed tilapia aquaponics N budget (Yang and Kim 2020) found 45 to 50 percent lost by denitrification, so the size looks plausible.
- **Water exchange at 1.5 percent a day (UVI) removes only a small share.** On its own it would leave nitrate far too high.
- **The starter fixture is now nitrate-limited again** (1.44 kg/m²). With only about a tenth of UVI's feed per m², the same loss fraction leaves too little nitrate for 90 plants. This again says to size fish feed to about 80 g per m² per day.

## 2026-11-25: Cost of production per kg from the component configurator

Run: `scripts/configure_system.py` (or `run.bat configure_basil_dwc_nl` / `configure_basil_dwc_karnataka`) on the candidate catalog in `data/catalog/`. Scenario estimate, not validated. Tilapia + basil DWC raft, 100 m² grow area, sized from UVI rules (80 g feed per m² per day, 160 kg fish per m³ tank per year). Counts build cost spread over each part's life, electricity, feed, fingerlings, seeds, water, heating and labour. Logistics, packaging, land and financing are not included. Fish are a co-product and are not credited.

| Build | Labour | € or ₹ per kg basil (low / mid / high cost) | per kg of basil + fish |
|---|---|---|---|
| Netherlands, glasshouse, heated | owner, not costed (830 h/yr needed) | €8.3 / 10.0 / 12.2 | €4.7 / 5.8 / 7.2 |
| Netherlands | hired, lean (Hawaii) | €9.6 / 11.5 / 13.9 | €5.4 / 6.6 / 8.2 |
| Netherlands | hired, UVI intensity | €17.6 / 20.6 / 24.0 | €9.9 / 11.9 / 14.2 |
| Karnataka, polyhouse | owner, not costed | ₹89 / 108 / 128 | ₹50 / 62 / 75 |
| Karnataka | hired, UVI intensity | ₹134 / 154 / 176 | ₹75 / 89 / 104 |

- **Feed is the biggest line** (about 40% in NL, 52% in Karnataka) because fish feed is charged to basil and the fish aren't credited. Crediting fish sales is the next lever.
- **NL heating is the second line** (about 34%), from a transferred sweet-pepper gas range, so it is the least reliable big number.
- **Air pumps matter:** small piston air pumps (NL) cost 17% of the total in electricity; one oversized 1.5 kW blower (India) costs 27%. A right-sized regenerative blower is the obvious alternative to source.
- **Build cost is small per kg** (under €0.70/kg in NL) once spread over 10-20 year lives, but several prices are still missing (trough walls, India pump, polyhouse life).
- **Next to the candidate price bands (comparison only, not a margin):** the NL cost range sits above the €7-9/kg wholesale band even owner-run; the Karnataka range overlaps the ₹65-180/kg Bangalore band. Fish income and logistics are not in yet.
- Simulator cross-check: the sized 100 m² system harvests about 2.0 kg/m² per cut at TAN about 2.3 mg/L, close to the catalog yield (1.9). The simulator runs at tropical water temperature in both regions.
- Gaps: NL fingerling and seed prices, India pump price, water price and seed price, structure lifetime in India, labour by task.

## 2026-11-25: Unit design comparison rerun after PR #11

Rerun of `scripts/compare_unit_configurations.py` after the nitrate-uptake fix (PR #11). Scenario estimate, not validated. The simulated UVI-ratio basil yield is now 2.00 kg/m² per harvest, so the top of the basil yield range is 26.0 kg/m² per year (was 25.9). The starter fixture now simulates 1.91 kg/m² per harvest (was 0.77).

- **Only the high and mid cases move, by under 1%.** Netherlands owner-run: €111 to €207 per m² per year (was €111 to €206). Karnataka owner-run at Ajit's price: ₹1,097 to ₹5,766.
- The break-even labour intensity in the Netherlands is unchanged at about 0.25 to 0.50 h per kg.
- Current numbers live in `docs/unit_configuration_economics_review.md`. The two entries below keep their original numbers as history.

## 2026-11-25: Karnataka rerun at Ajit's Bangalore price

Run: `scripts/compare_unit_configurations.py`, Karnataka basil price set to ₹100-250/kg (Ajit's local read, depends on processed, fresh or organic; agrees with the ₹65-180 listings). Scenario estimate, not validated. Headroom = revenue minus labour and electricity.

- **Owner-run basil: ₹1,100 to ₹5,740 per m² per year** (about €10 to €52), up about 50% from the listing price, but still well below the Dutch owner-run case (€111 to €206).
- **Hired staff at UVI or Purdue labour intensity: about break-even in the low case** (₹-70 to ₹-20), ₹2,000 to ₹4,700 in the mid and high cases.
- Where a unit lands in the band depends on grade (fresh, processed, organic). A defined grade and buyer would settle it.

## 2026-11-25: Which unit design clears labour and electricity (Netherlands vs India)

Run: `scripts/compare_unit_configurations.py` on `data/scenarios/unit_configuration_candidates_v0.json`. Scenario estimate, not validated. **Headroom** = revenue minus labour and electricity per m² per year; it still has to pay heating, CAPEX, consumables and any uncosted owner time. Review: `docs/unit_configuration_economics_review.md`.

Basil yield: 23.4 to 25.9 kg/m² per year (UVI canon to simulated UVI feed ratio). Tropical yields; Dutch winter is not in the range.

| Design | NL € per m²/yr (low / mid / high) | India ₹ per m²/yr at the demoted study band (low / mid / high) |
|---|---|---|
| A. UVI-style DWC basil, hired, UVI labour (0.56-0.62 h/kg) | -166 / -105 / -38 | 8,913 / 14,946 / 22,113 |
| B. Large raceway DWC basil, hired, Hawaii-farm labour per m² (0.08-0.09 h/kg) | 72 / 120 / 174 | 10,015 / 16,071 / 23,214 |
| C. Basil farm at Purdue labour per kg (0.53-0.65 h/kg) | -177 / -98 / -13 | 8,862 / 15,153 / 22,520 |
| D. Large raceway DWC lettuce, Flemish auction price | -42 / -19 / 6 | no India lettuce price |
| E. Owner-operated DWC basil | 111 / 156 / 206 | 10,195 / 16,221 / 23,335 |

- **Netherlands: hired basil labour must stay under about 0.25-0.50 h per harvested kg.** Every sourced basil labour figure (0.53-0.65 h/kg) is above that. Only design B clears, and it borrows a lettuce farm's labour per m².
- **Scale and a simple raceway layout cut labour per m² about sevenfold** (UVI 214 m² vs Hawaii about 1,142 m²). Processing and packing was 44% of Hawaii's hours.
- **Owner-operated NL leaves €111-206 per m² per year** for heating, CAPEX and owner pay (about €7.6 to €19 per owner hour in the low and mid cases).
- **Wholesale lettuce doesn't work** at Low Countries auction prices. Basil earns about 4 to 11 times more revenue per m².
- **India base price is now ₹65-180/kg** (Bangalore level, confirmed by Ajit, matching ten Bengaluru B2B listings). At that price, owner-run basil leaves only about ₹180-4,070 per m² per year (about €2-37), less than the Dutch owner-run case. Hired staff at UVI or Purdue labour intensity lose money in the low case. By state, owner-run in the low case: Karnataka ₹441, Tamil Nadu ₹76, Andhra Pradesh ₹725, Telangana ₹289 per m².
- **The old ₹600-1,000/kg study band is demoted** to a sensitivity case. At that band everything cleared (about €81-213 per m²), which shows how much India depends on price.
- The India table above uses the demoted band; see `docs/unit_configuration_economics_review.md` for base-price numbers.
- Biggest gaps: basil harvest and pack hours per kg, Dutch heating demand, build cost per m².

Related truths: [[Truths/Business/Business|Business]] and [[Truths/Operations/Operations|Operations]] (UE_0001 to UE_0011, candidates).

## 2026-11-25: New nitrification and nitrate uptake models (PR #6 and PR #11)

Run: `src/simulate_crop_cycle.py`, 28 days, both basil raft scenarios, with the raft (11.25 m²) as the only nitrifying surface. All new model values are candidates. This **supersedes the revenue rerun entry below** for current numbers. Details and source reliability: [[Learnings/Nitrification Model Findings|Nitrification Model Findings]].

| Scenario | TAN (mg/L) | NH3 (mg/L) | Nitrate (mg/L) | Basil kg/m² | € per m² per year (cons. / base / opt.) |
|---|---|---|---|---:|---|
| Starter fixture (8 kg fish) | about 0.2 | about 0.0015 | 42 to 38 | 1.91 (was 1.21) | 148 / 179 / 213 |
| UVI feed ratio | 1.9 to 2.3 (was about 14) | about 0.015 (was about 1.1) | 45 to 161 | 2.00 | 155 / 187 / 222 |

- **The UVI-scale fish load is now a valid operating point for ammonia.** The raft runs at about 58 percent of its modelled capacity.
- **TAN of about 2 mg/L is above the NMSU guidance of TAN under 1 ppm**, but NH3 stays low at pH 6.9.
- **The old nitrate uptake placeholder was about 7 times too high.** Growth-based uptake is about 0.6 mg/L per day for 90 plants in 6,000 L. The starter case is no longer nitrate-limited, so its yield rises to 1.91 kg/m².
- **Nitrate now builds up to about 161 mg/L in the UVI case; UVI measured about 42.** The model has no nitrogen sinks besides plant shoots: no water exchange, sludge removal, denitrification or root uptake. That is the next gap to close.

## 2026-11-25: Basil revenue range rerun after the nitrification and pH fix

The 28-day basil runs were regenerated after PR #6 (nitrification model and basil pH scoring fix), and the revenue range was rebuilt from them. This **supersedes the two entries below** for current numbers. Same price and saleability inputs as before, still pending your approval.

| Scenario | Harvest kg/m² | Water state over the run | € per m² per year (cons. / base / opt.) |
|---|---:|---|---|
| Starter fixture | 0.77 (was 1.21) | TAN max about 0.22 mg/L, nitrate falls to about 5.7 mg/L | 60 / 72 / 86 |
| UVI feed ratio | 1.99 (was 2.00) | TAN max about 2.3 mg/L, NH3 max about 0.016 mg/L, nitrate stays near 41 to 44 mg/L | 154 / 187 / 222 |

- **Range: about €60 to €222 per m² per year gross.**
- **The UVI feed-ratio case now holds water quality in a normal-looking range** (TAN about 2.3 mg/L, close to the UVI trial mean of 2.2), so 2.0 kg/m² is no longer just a plant-side ceiling. This is context, not a fish-safety assessment.
- **The starter fixture is more nitrate-limited than before.** It has too little fish feed for its 90 plants. The 11.25 m² system grosses about €670 to €970 a year at that yield.
- **Takeaway:** feed per m² of grow area drives basil output. A real design should size fish feed to the UVI ratio, about 80 to 100 g per m² per day.

## 2026-11-25: Basil gross revenue range

Run: `scripts/build_basil_revenue_range.py` on the two 28-day basil results (PR #3). Gross revenue only, with no costs, margin or profit. 13 crops per year (UVI staggered trial). Prices are €7, €8 and €9/kg (provisional Dutch wholesale examples). Saleability is 85%, 90% and 95% (provisional assumptions).

| Scenario | Harvest kg/m² | € per m² per year (cons. / base / opt.) |
|---|---:|---|
| Starter fixture (nitrate-limited) | 1.21 | 93 / 113 / 134 |
| UVI feed ratio (TAN up to about 14 mg/L, NH3 about 1.2 mg/L) | 2.00 | 155 / 187 / 222 |

- **Range: about €93 to €222 per m² per year gross.** Treat the top end as a plant-side ceiling until the nitrification model can carry that feed load.
- The 11.25 m² starter system grosses about €1,050 to €1,500 a year at its current yield.
- Biggest unknowns: today's real prices, saleability, and every cost line. The Farm inputs work covers these.

## 2026-11-25: Basil grown to a full 28-day harvest

Run: `src/simulate_crop_cycle.py` on the `basil_raft_crop_cycle` scenarios (PR #1). Basil cut-mass growth is calibrated to the UVI anchor: 8 plants/m², 28 days, 2.0 kg/m² per harvest.

- **Starter fixture (8 kg tilapia, 90 basil plants, 11.25 m²): about 1.2 kg/m² per harvest.** The basil runs short of nitrate, which falls from 42 to about 15 mg/L by day 27. Feed per m² is about a tenth of what UVI used.
- **Fish scaled to the UVI feed ratio: 2.0 kg/m².** Water quality collapses, though: TAN about 14 mg/L, NH3 about 1.1 mg/L. The placeholder nitrification model can't remove that load, so this isn't a valid operating point.
- **Bug found:** before this run, basil was never nitrate-limited because of a mismatched field name. Earlier basil runs were too optimistic.
- **Model gap:** the basil pH score is 0 at any pH from 6.9 to 7.6, the normal aquaponic range, because it uses hydroponic ranges. UVI grew basil well at pH 7.4.

Related truths: [[Truths/Biology/Biology|Biology]] (CROP_0002 to CROP_0004), [[Truths/Operations/Operations|Operations]] (CROP_0006, CROP_0007).

## Related Notes

- [[Learnings/Simulation Learnings|Simulation Learnings]] (older generated summary)
- [[Project/Project|Project]]
