# Simulation Findings Log

What the simulation shows, newest first. These are **scenario estimates, not validated**: they describe the model, not the real world, and they are never truths.

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
