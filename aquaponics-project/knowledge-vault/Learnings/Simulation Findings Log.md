# Simulation Findings Log

What the simulation shows, newest first. These are **scenario estimates, not validated**: they describe the model, not the real world, and they are never truths.

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
