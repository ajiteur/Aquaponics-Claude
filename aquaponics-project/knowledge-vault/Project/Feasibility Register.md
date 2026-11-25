# Feasibility Register

What the current evidence can support building now, and what is blocked and on what. Kept by the Gatekeeper. Hand-written, not generated.

Last reviewed: 2026-11-24 (against `main` at PR #1, with PR #2 open)

Status key: **Buildable now** = canon and tests support it. **Buildable with labels** = allowed only as a labelled scenario estimate. **Blocked** = missing evidence or input; don't build it as fact.

## Buildable now

| Item | Why it's supported |
|---|---|
| Daily simulation with direct feed input (Mode A) | Current MVP baseline; integrity check and tests pass. |
| TAN-N load and NH3 fraction as chemistry context | Water-chemistry truths (pH and temperature drive NH3 share). Context only, not fish safety. |
| Aeration and dry-solids context (P1.5) | MVP baseline. Context only, not aeration adequacy or solids-removal capacity. |
| Basil grown to a 28-day harvest, calibrated to UVI | Accepted UVI facts: 8 plants/m², 28 days, 2.0 kg/m² batch and 1.8 kg/m² staggered per harvest (CROP_0001 to CROP_0004). Output is harvested cut mass, labelled scenario estimate. |
| Feed + electricity cost pressure (P2a) | MVP baseline. Selected costs only, not total operating cost. |
| Obsidian truths export, one note per truth | PR #2; dry run matches the JSON. |

## Buildable with labels (scenario estimate, not validated)

| Item | Condition |
|---|---|
| Basil revenue range | Only with price and saleability cases that are canonical, reviewed, or supplied by Ajit, each labelled with its origin. Ranges only. The canonical `pricing_models.json` prices are all still `todo`. |
| Basil at UVI feed ratio (81.4 g/day/m²) | Runs, but the result is not a valid operating point until nitrification is fixed (TAN about 14 mg/L, NH3 about 1.1 mg/L in the run). |
| Unit economics example | The `variable_cost_per_saleable_kg` (6.8) and `fixed_batch_cost` (500.0) are constructed placeholders. Any output that uses them must say so. |

## Blocked

| Item | Blocked on |
|---|---|
| Fish-safe stocking or feed rate at a given biofilter size | Nitrification and TAN model is a placeholder (no biofilter capacity). Evidence: Biofilters corroboration report; model work in the nitrification thread. |
| Basil growth response to pH | Basil pH score uses hydroponic ranges and scores 0 from pH 6.9 to 7.6, though UVI grew basil well at pH 7.4. Needs a context-split decision (aquaponic vs hydroponic). |
| Standing basil biomass over time | `average_biomass_g` still grows at a fixed 4 g per plant per day. Only harvested cut mass is calibrated. |
| `saleable_harvest_mass_kg` | Needs observed output or a reviewed manual value approved by Ajit for that scope. The UVI papers don't quantify culled mass. |
| Revenue, margin, payback, break-even as fact | Blocked by AGENTS.md. Allowed only as labelled scenario estimates (AGENTS.md 1C). |
| Farm go/no-go for Ajit's site | Needs Ajit's inputs: location, scale, budget, energy and heating costs, local basil prices, labour. Farm inputs thread is gathering them. |
| CAPEX, labour, channel terms | All canonical records are `todo` with null values. |
| Batch basil at UVI scale without deficiencies | CROP_0006: UVI found batch production unsustainable with its fish output. |
| Lettuce and tilapia growth to harvest | No crop-cycle or growth calibration yet beyond the starter profiles. |

## Evidence notes from review

- The UVI yield values 2.0, 1.8 and 0.6 kg/m² are in the Basil corroboration report in the repo. The other UVI values (8 plants/m², 28 days, annual yields, 81.4 and 99.6 g/day/m² feed) came from a web read of the primary papers, which are not stored in the repo. Ajit approved them on 2026-11-24 (UTC).
- None of the 53 existing truths records a source tier, a confidence reason or corroboration yet. Their notes now show "not recorded" under Reliability. Backfilling those fields is a follow-up canon pass, with each fact staying as it is until then.
- The basil anchor conditions use one stated assumption: air temperature equals water temperature at the 26.5 °C midpoint. It is calibration only, not a measured value.

## Related Notes

- [[Project/Save Points|Save Points]]
- [[Project/Status and Roadmap|Status and Roadmap]]
