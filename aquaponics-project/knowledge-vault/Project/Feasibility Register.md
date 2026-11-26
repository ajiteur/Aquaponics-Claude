# Feasibility Register

What the current evidence can support building now, and what is blocked and on what. Kept by the Gatekeeper. Hand-written, not generated.

Last reviewed: 2026-11-25 (against `main` after PRs #1 to #7)

Status key: **Buildable now** = canon and tests support it. **Buildable with labels** = allowed only as a labelled scenario estimate. **Blocked** = missing evidence or input; don't build it as fact.

## Buildable now

| Item | Why it's supported |
|---|---|
| Daily simulation with direct feed input (Mode A) | Current MVP baseline; integrity check and tests pass. |
| TAN-N load and NH3 fraction as chemistry context | Water-chemistry truths (pH and temperature drive NH3 share). Context only, not fish safety. |
| Aeration and dry-solids context (P1.5) | MVP baseline. Context only, not aeration adequacy or solids-removal capacity. |
| Basil grown to a 28-day harvest, calibrated to UVI | Accepted UVI facts: 8 plants/m², 28 days, 2.0 kg/m² batch and 1.8 kg/m² staggered per harvest (CROP_0001 to CROP_0004). Output is harvested cut mass, labelled scenario estimate. |
| Feed + electricity cost pressure (P2a) | MVP baseline. Selected costs only, not total operating cost. |
| Obsidian truths export, one note per truth, with a Reliability section | PRs #2 and #7; dry run matches the JSON. |

## Buildable with labels (scenario estimate, not validated)

| Item | Condition |
|---|---|
| Basil revenue range | Built (PRs #3 and #5). Price and saleability inputs are research-pack values still pending Ajit's approval, and the canonical `pricing_models.json` prices are all `todo`. Ranges only. |
| Biofilm nitrification capacity | Built in PR #6 as a candidate model: SRAC 454 raft capacity (E4, medium) with TAN, pH, temperature and DO limits. It runs about ten times above trickling-filter and RBC biofilm rates. That is the largest open question, so it waits for Ajit's review. |
| Basil score in coupled aquaponic loops | Built in PR #6 as a candidate: preferred pH 5.8 to 7.6. The 6.2 to 6.9 band is a low-confidence assumption, and above pH 7.6 there is no evidence. |
| Basil at UVI feed ratio (81.4 g/day/m²) | With the candidate nitrification model, TAN settles near 2 mg/L and basil reaches about 2.0 kg/m². That TAN is above the NMSU guidance of under 1 mg/L, so it is not a fish-safety result. |
| Unit economics example | The `variable_cost_per_saleable_kg` (6.8) and `fixed_batch_cost` (500.0) are constructed placeholders. Any output that uses them must say so. |

## Blocked

| Item | Blocked on |
|---|---|
| Fish-safe stocking or feed rate | Fish safety is a blocked claim (AGENTS.md 1B). The nitrification model is still a candidate, and nitrite and organic-carbon effects aren't modelled. |
| Nitrate balance and basil yield at low fish load | Uptake is growth-based and nitrate sinks are modelled (candidates). The residual loss is a fixed fraction calibrated at UVI's feed ratio; whether it holds at much lower feed is not known. |
| Feed-protein TAN | Both basil scenarios have feed protein set to null, so TAN per gram of feed uses the 30 mg/g scenario placeholder. |
| Standing basil biomass over time | `average_biomass_g` still grows at a fixed 4 g per plant per day. Only harvested cut mass is calibrated. |
| `saleable_harvest_mass_kg` | Needs observed output or a reviewed manual value approved by Ajit for that scope. The UVI papers don't quantify culled mass. |
| Revenue, margin, payback, break-even as fact | Blocked by AGENTS.md. Allowed only as labelled scenario estimates (AGENTS.md 1C). |
| Farm go/no-go for Ajit's site | Needs Ajit's inputs: location, scale, budget, energy and heating costs, local basil prices, labour. Farm inputs thread is gathering them. |
| CAPEX, labour, channel terms | All canonical records are `todo` with null values. |
| Batch basil at UVI scale without deficiencies | CROP_0006: UVI found batch production unsustainable with its fish output. |
| Lettuce and tilapia growth to harvest | Tilapia growth model is in review (PR #30). After the measured temperature curve it is within 10 to 25 percent at 23.5 to 25 °C (UQ-013, candidate fix). No lettuce crop-cycle calibration yet. |
| Basil yield at densities or light levels other than UVI's | Candidate density and DLI responses are in review (PR #30), but Savidov is still +68 percent and Knaus +30 to +441 percent (UQ-014). |

## Evidence notes from review

- The UVI yield values 2.0, 1.8 and 0.6 kg/m² are in the Basil corroboration report in the repo. The other UVI values (8 plants/m², 28 days, annual yields, 81.4 and 99.6 g/day/m² feed) came from a web read of the primary papers, which are not stored in the repo. Ajit approved them on 2026-11-24 (UTC).
- None of the 53 existing truths records a source tier, a confidence reason or corroboration yet. Their notes now show "not recorded" under Reliability. Backfilling those fields is a follow-up canon pass, with each fact staying as it is until then.
- The basil anchor conditions use one stated assumption: air temperature equals water temperature at the 26.5 °C midpoint. It is calibration only, not a measured value.

## Related Notes

- [[Project/Save Points|Save Points]]
- [[Project/Status and Roadmap|Status and Roadmap]]
