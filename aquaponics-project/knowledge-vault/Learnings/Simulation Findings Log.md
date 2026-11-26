# Simulation Findings Log

What the simulation shows, newest first. These are **scenario estimates, not validated**: they describe the model, not the real world, and they are never truths.

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
