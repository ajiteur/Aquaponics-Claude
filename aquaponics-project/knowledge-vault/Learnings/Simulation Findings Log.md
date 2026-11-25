# Simulation Findings Log

What the simulation shows, newest first. These are **scenario estimates, not validated**: they describe the model, not the real world, and they are never truths.

## 2026-11-25: New nitrification and nitrate uptake models (PR #6)

Run: `src/simulate_crop_cycle.py`, 28 days, both basil raft scenarios, with the raft (11.25 m²) as the only nitrifying surface. All new model values are candidates. Details and source reliability: [[Learnings/Nitrification Model Findings|Nitrification Model Findings]].

| Scenario | TAN (mg/L) | NH3 (mg/L) | Nitrate (mg/L) | Basil kg/m² | € per m² per year (cons. / base / opt.) |
|---|---|---|---|---:|---|
| Starter fixture (8 kg fish) | about 0.2 | about 0.0015 | 42 to 38 | 1.91 (was 1.21) | 148 / 179 / 213 |
| UVI feed ratio | 1.9 to 2.3 (was about 14) | about 0.015 (was about 1.1) | 45 to 161 | 2.00 | 155 / 187 / 222 |

- **The UVI-scale fish load is now a valid operating point for ammonia.** The raft runs at about 58 percent of its modelled capacity.
- **TAN of about 2 mg/L is above the NMSU guidance of TAN under 1 ppm**, but NH3 stays low at pH 6.9.
- **The old nitrate uptake placeholder was about 7 times too high.** Growth-based uptake is about 0.6 mg/L per day for 90 plants in 6,000 L. The starter case is no longer nitrate-limited, so its yield rises to 1.91 kg/m².
- **Nitrate now builds up to about 161 mg/L in the UVI case; UVI measured about 42.** The model has no nitrogen sinks besides plant shoots: no water exchange, sludge removal, denitrification or root uptake. That is the next gap to close.

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
