# MVP Current Truths, Terminology, and Loophole Audit

## 1. Purpose

Capture the current MVP truth before choosing the next roadmap direction. This
note audits the implemented Mode A/P1/P1.5/P2a spine, terminology, demo
outputs, guardrails, protected-path status, stale documentation, and remaining
loopholes.

This is a current-state audit only. It is not canon, not a product spec, and
not an implementation plan.

## 2. Scope

In scope:

- current helper/report/demo state
- current demo output values
- terminology and blocked-claim boundaries
- documentation freshness
- scenario-versus-canon boundaries
- readiness for customer/advisor validation or seed-demo dashboard/report
  design

Out of scope:

- new calculations
- canonical biology/model/business edits
- ontology edits
- runtime edits
- source, script, test, Obsidian, or knowledge-vault edits
- revenue, profitability, safety, adequacy, or viability claims

## 3. Inputs reviewed

Implemented demo assets:

- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `scripts/example_mvp_mode_a_p1_water_quality_inputs.json`
- `scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json`
- `scripts/example_mvp_mode_a_p2a_operating_cost_inputs.json`

Implemented helpers:

- `src/feed_waste_tan_loads.py`
- `src/mvp_tan_nh3_risk.py`
- `src/mvp_aeration_solids_context.py`
- `src/mvp_operating_cost_pressure.py`
- `src/mvp_mode_a_feed_load_report.py`

Tests:

- `tests/test_feed_waste_tan_loads.py`
- `tests/test_mvp_tan_nh3_risk.py`
- `tests/test_mvp_aeration_solids_context.py`
- `tests/test_mvp_operating_cost_pressure.py`
- `tests/test_mvp_mode_a_feed_load_report.py`
- `tests/test_build_mvp_mode_a_feed_load_report.py`

Supporting docs present:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_tilapia_feed_research_ingestion_review.md`
- `docs/mvp_p1_tan_concentration_nh3_risk_design.md`
- `docs/mvp_p1_5_aeration_solids_design.md`
- `docs/mvp_operating_cost_pressure_design.md`
- `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- `docs/mvp_current_progress_map_update_spec.md`
- `docs/mvp_strategic_alignment_review_packet_for_pro.md`
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`

Knowledge-vault/Obsidian context inspected read-only:

- `knowledge-vault/Learnings/Simulation Learnings.md`
- nearby matching MVP/aquaponics/simulation/business notes by filename search

## 4. Current expected MVP state

Current completed layers:

1. Mode A direct feed input
2. TAN-N load calculator
3. nitrification oxygen-demand calculator
4. alkalinity-demand calculator
5. Mode A report builder
6. JSON demo runner
7. P1 TAN-N concentration + NH3 chemistry helper
8. P1 report/demo integration
9. P1.5 aeration/solids context helper
10. P1.5 report/demo integration
11. P2a operating-cost pressure helper
12. P2a report/demo integration
13. four-level customer/advisor walkthrough
14. current progress-map update spec

Current demo levels:

1. Mode A load-only report
2. P1 TAN-N/NH3 water-quality context report
3. P1.5 aeration/solids context report
4. P2a selected operating-cost pressure report

## 5. Git and commit-state audit

Initial `git status --short` before creating this note was clean.

Recent relevant commits visible in `git log --oneline -12`:

- `3e4ae43 Add four-level MVP customer demo walkthrough`
- `32a6456 Update MVP progress map spec`
- `dde4053 Integrate P2a operating cost pressure into Mode A report`
- `e9f0ad1 Add P2a operating cost pressure helper`
- `6fb53d9 Design MVP operating cost pressure layer`
- `c9eadec Add Mode A P1 P1.5 customer demo walkthrough`
- `c8c5297 Integrate P1.5 aeration solids context into Mode A report`
- `0f516f0 Add P1.5 aeration and solids context helper`
- `02ac4b9 Design P1.5 aeration and solids context layer`
- `0be1494 Integrate P1 TAN NH3 context into Mode A report`
- `688c016 Add P1 TAN concentration and NH3 chemistry helper`
- `06888a7 Prepare strategic alignment packet for Pro review`

Commit-state finding:

- `clear`: the expected current-state docs and P2a integration appear committed
  before this audit pass.

## 6. Demo-command audit

All four demo commands ran successfully:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json
```

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_water_quality_inputs.json
```

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json
```

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p2a_operating_cost_inputs.json
```

Demo-level truth:

- Demo 1 prints load-only report fields and missing-context labels.
- Demo 2 adds `water_quality_context`.
- Demo 3 adds `aeration_solids_context`.
- Demo 4 adds `operating_cost_pressure`.

## 7. Test and validation audit

Validation commands run:

```powershell
python -m py_compile src/feed_waste_tan_loads.py src/mvp_tan_nh3_risk.py src/mvp_aeration_solids_context.py src/mvp_operating_cost_pressure.py src/mvp_mode_a_feed_load_report.py scripts/build_mvp_mode_a_feed_load_report.py
```

```powershell
python -m unittest tests.test_feed_waste_tan_loads tests.test_mvp_tan_nh3_risk tests.test_mvp_aeration_solids_context tests.test_mvp_operating_cost_pressure tests.test_mvp_mode_a_feed_load_report tests.test_build_mvp_mode_a_feed_load_report
```

Results:

- `py_compile`: passed
- `unittest`: passed, `112` tests run

Validation finding:

- `clear`: helper, report-builder, and demo-runner tests cover the current
  Mode A/P1/P1.5/P2a demo path.

## 8. Current MVP spine

Mode A:

- starts from explicit `feed_kg_day`
- uses explicit `protein_fraction`
- calculates load-only TAN-N, oxygen demand, and alkalinity demand

P1:

- adds optional fish-tank upper-bound/no-removal TAN-N concentration
- adds optional unionized NH3 chemistry context
- requires explicit water volume, time basis, pH, temperature, and freshwater
  assumption

P1.5:

- adds optional aeration and solids context
- echoes nitrification oxygen demand as a sub-load
- echoes measured DO as context
- estimates dry-solids potential only with explicit coefficient

P2a:

- adds optional feed and equipment-electricity operating-cost pressure
- requires explicit scenario/business price and tariff metadata
- calculates selected operating-cost pressure subtotal only when supplied money
  outputs share one currency

## 9. Current terminology

| Term | Current meaning |
| --- | --- |
| Mode A direct feed input | Scenario supplies `feed_kg_day` directly; no biomass-derived feeding. |
| TAN-N load | Ammonia nitrogen load from feed/protein in kg/day or g/day; not concentration. |
| TAN-N concentration | Estimated mg TAN-N/L only when water volume and time basis are supplied. |
| NH3 fraction | Dimensionless unionized ammonia fraction from pH and temperature. |
| NH3-N | Unionized ammonia expressed as nitrogen, mg NH3-N/L. |
| NH3 | Unionized ammonia molecule concentration, mg NH3/L, converted from NH3-N by `17/14`. |
| Nitrification oxygen demand | Oxygen demand associated with nitrifying TAN-N; not total oxygen demand. |
| Measured DO context | A point/context dissolved oxygen measurement; not safety proof. |
| Dry-solids potential | Provisional feed-linked dry-solids estimate; not wet sludge, TSS, or removal capacity. |
| Scenario feed cost | Feed cost calculated only from explicit feed price metadata. |
| Scenario power cost | Equipment electricity cost calculated only from explicit equipment and tariff metadata. |
| Selected operating-cost pressure | Supplied-category cost-pressure context; not total operating cost. |
| Selected operating-cost pressure subtotal | Sum of supplied calculable money categories only when currencies match. |

## 10. Layer-by-layer current truth

Mode A load-only calculates:

- `tan_n_load_kg_day`
- `tan_n_load_g_day`
- `oxygen_demand_g_day`
- `alkalinity_demand_g_caco3_day`

Mode A load-only does not claim:

- TAN concentration
- unionized NH3 toxicity
- feed cost
- tank suitability
- Mode B feeding
- biofilter removal
- aeration capacity
- crop saleability
- `saleable_harvest_mass_kg`

P1 water-quality chemistry context calculates:

- `estimated_tan_n_mg_l`
- `estimated_unionized_nh3_fraction`
- `estimated_nh3_n_mg_l`
- `estimated_nh3_mg_l`

P1 does not claim:

- safe/unsafe threshold status
- fish safety
- system safety
- actual biofilter removal
- post-feeding transient peak exposure
- system-average concentration

P1.5 aeration/solids context calculates or echoes:

- nitrification oxygen demand as a known sub-load
- measured DO as context when supplied
- provisional dry-solids potential when feed and coefficient are supplied

P1.5 does not claim:

- total oxygen demand
- fish respiration oxygen demand
- organic-waste decomposition oxygen demand
- aeration capacity
- oxygen-transfer capacity
- aeration adequacy
- wet sludge
- TSS concentration
- settleable-solids split
- solids-removal capacity

P2a feed/electricity cost pressure calculates:

- `scenario_feed_cost_per_day`
- per-device `device_kwh_day`
- `scenario_power_kwh_day`
- `scenario_power_cost_per_day`
- `selected_operating_cost_pressure_subtotal`

P2a does not claim:

- total operating cost
- feed/electricity market truth
- canon prices
- buffer cost
- water cost
- labor cost
- backup-power cost
- fish revenue
- basil revenue
- crop revenue
- margin
- ROI
- payback
- break-even
- profitability
- economic viability

## 11. Latest demo values

Values from the current demo commands:

| Output | Current value |
| --- | --- |
| TAN-N load | `0.02944 kg/day` |
| TAN-N load | `29.44 g/day` |
| Nitrification oxygen demand | `134.5408 g/day` |
| Alkalinity demand | `210.2016 g CaCO3/day` |
| Estimated TAN-N concentration | `3.7743589743589743 mg TAN-N/L` |
| Estimated unionized NH3 fraction | `0.006971085009084945` |
| Estimated NH3-N concentration | `0.026311377265059072 mg NH3-N/L` |
| Estimated NH3 concentration | `0.031949529536143155 mg NH3/L` |
| Measured DO | `5.0 mg/L` |
| Dry-solids potential | `0.25 kg/day` |
| Scenario feed cost | `45.0 INR/day` |
| Pump power use | `4.8 kWh/day` |
| Blower power use | `2.4 kWh/day` |
| Scenario power use | `7.2 kWh/day` |
| Scenario power cost | `54.0 INR/day` |
| Selected operating-cost pressure subtotal | `99.0 INR/day` |

## 12. Guardrails and blocked claims

The current MVP must not claim:

- fish safety
- system safety
- aeration adequacy
- total oxygen demand
- solids-removal capacity
- total operating cost
- profitability
- revenue
- margin
- ROI
- payback
- break-even
- economic viability
- basil saleable harvest mass

Current naming and labels mostly support these guardrails. P2a uses selected
operating-cost-pressure language rather than total-cost or profit language.

## 13. Protected-path audit

Protected-path diff checks:

- `git --no-pager diff --name-only -- data/knowledge data/simulation src scripts tests`
- `git --no-pager diff --name-only -- src/simulate_day.py`

Current audit result:

- `clear`: no protected files changed in this pass.
- `clear`: `src/simulate_day.py` was not modified.
- `clear`: no `knowledge-vault/**` or `.obsidian/**` files were modified.

## 14. Documentation freshness audit

Current-facing docs:

| Doc | Freshness classification | Notes |
| --- | --- | --- |
| `docs/mvp_current_progress_map_update_spec.md` | `clear` | Treats P2a report integration as completed and points to four-demo walkthrough. |
| `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md` | `clear` | Current four-level customer/advisor walkthrough. |
| `docs/mvp_operating_cost_pressure_design.md` | `clear` | Historical design source for P2a/P2c; still useful as design context. |
| `docs/mvp_p1_tan_concentration_nh3_risk_design.md` | `clear` | Historical design source for P1; implementation exists. |
| `docs/mvp_p1_5_aeration_solids_design.md` | `clear` | Historical design source for P1.5; implementation exists. |

Historical docs that should not be treated as current roadmap status:

| Doc | Freshness classification | Notes |
| --- | --- | --- |
| `docs/mvp_strategic_alignment_review_packet_for_pro.md` | `minor_stale_historical_doc` | Contains older roadmap options before P1/P1.5/P2a completion. Keep as historical review packet. |
| `docs/mvp_mode_a_feed_load_customer_demo_walkthrough.md` | `minor_stale_historical_doc` | One-level demo walkthrough; superseded by four-level walkthrough. |
| `docs/mvp_mode_a_p1_p1_5_customer_demo_walkthrough.md` | `minor_stale_historical_doc` | Three-level walkthrough; superseded by four-level walkthrough. |
| `docs/mvp_fish_feed_waste_tan_engine_design.md` | `minor_stale_historical_doc` | Early design doc; useful as origin history, not current state. |
| `docs/mvp_mode_a_feed_load_integration_surface_plan.md` | `minor_stale_historical_doc` | Integration planning doc; implementation now exists. |
| `docs/mvp_tilapia_feed_research_ingestion_review.md` | `minor_stale_historical_doc` | Research ingestion context remains useful; not current implementation state. |

Freshness finding:

- `clear`: current-facing docs exist and are committed.
- `minor_stale_historical_doc`: older roadmap/design/walkthrough docs should be
  cited as historical unless a later cleanup pass explicitly updates their
  headers.

## 15. Scenario-versus-canon audit

Current scenario inputs, not canon:

- feed price
- electricity price
- tariff date/geography/class/source
- equipment power records
- dry-solids coefficient
- water volume in demo examples
- pH/temperature in demo examples
- measured DO in demo examples

Current canon-protection boundaries:

- no feed price promoted to canon
- no electricity price promoted to canon
- no dry-solids coefficient promoted to canon
- no UVI-like or demo values promoted to canon
- no business revenue rule changed in this pass

Finding:

- `clear`: scenario/demo values are labeled and used as explicit inputs, not
  canonical defaults.

## 16. Biological and engineering boundary audit

Current boundaries:

- TAN-N load is not TAN-N concentration.
- TAN-N concentration requires effective water volume and time basis.
- NH3 chemistry requires pH and temperature.
- P1 estimates fish-tank upper-bound/no-removal context, not safety.
- nitrification oxygen demand is not aeration capacity.
- nitrification oxygen demand is not total oxygen demand.
- nitrification oxygen demand is not biofilter removal.
- measured DO is context, not future safety proof.
- dry-solids potential is not wet sludge.
- dry-solids potential is not TSS.
- dry-solids potential is not solids-removal capacity.
- selected operating-cost pressure is not total operating cost.

Finding:

- `clear`: current helper/report/test names preserve the major engineering
  boundaries.

## 17. Basil saleability boundary audit

Current boundaries:

- no MVP feed/water/solids/cost output populates `saleable_harvest_mass_kg`
- basil revenue is not calculated
- crop revenue is not calculated
- plant biomass, plant count, or daily gain are not used as saleable harvest
  mass
- `saleable_harvest_mass_kg` remains unresolved unless observed or explicitly
  reviewed

Supporting observation:

- The current MVP report keeps `saleable_harvest_mass_kg` in excluded
  calculations or boundary notes, not as a numeric output.

Finding:

- `clear`: basil saleability remains blocked correctly.

## 18. Findings table

| Finding | Classification | Evidence | Recommended handling |
| --- | --- | --- | --- |
| Four-level demo path exists and runs. | `clear` | All four demo commands succeeded. | Proceed to validation/demo packaging. |
| Unit tests pass. | `clear` | `112` tests passed. | Keep current scope. |
| Protected paths unchanged. | `clear` | Protected diff checks empty. | No cleanup needed. |
| P2a naming avoids total-cost/profit claims. | `clear` | `operating_cost_pressure`, selected subtotal labels, no total operating cost output. | Keep terminology. |
| Older roadmap docs contain earlier next-build states. | `minor_stale_historical_doc` | Stale-doc scan found older P1/P1.5/P2a planning language. | Treat as historical; avoid using them as current-facing status. |
| Knowledge-vault Simulation Learnings note is older and runtime-derived. | `minor_stale_historical_doc` | It references older simulation reports and viability/NH3 bands. | Sync later with current MVP guardrails; do not use as current truth. |
| Current four-level walkthrough is demo-ready but not field-validated. | `clear` | Walkthrough exists and values are command-backed. | Run customer/advisor validation before expanding model layers. |
| P2c cost categories are not implemented. | `blocked` | Current P2a only includes feed and electricity. | Defer until customer/advisor validation confirms value. |
| Mode B biomass-derived feeding is not implemented. | `blocked` | Current input mode remains Mode A direct feed. | Keep future work. |
| Revenue/profitability not implemented. | `blocked` | No explicit revenue inputs; basil saleability unresolved. | Keep blocked. |

## 19. Loopholes or gaps found

Loopholes controlled by current design:

- P2a could be mistaken for total operating cost; current labels and notes
  explicitly block this.
- P1 TAN-N concentration could be mistaken for safety; current output does not
  compare to thresholds.
- measured DO could be mistaken for aeration adequacy; current P1.5 text blocks
  this.
- dry-solids potential could be mistaken for TSS, wet sludge, or filter
  performance; current labels block this.

Remaining gaps:

- `needs_doc_update`: if older docs are reused externally, add a short
  "historical/superseded" banner in a future cleanup pass. Do not do this in
  the current single-file audit pass.
- `blocked`: no customer/advisor validation evidence yet.
- `blocked`: no seed-demo dashboard/report design yet.
- `blocked`: no P2c buffer/water/maintenance cost-pressure helper yet.
- `blocked`: no Mode B biomass-derived feeding yet.
- `blocked`: no runtime-native harvest output for observed saleable harvest
  mass.
- `blocked`: no revenue/profitability until explicit revenue and
  complete-enough cost inputs exist.

No immediate `needs_code_fix` or `needs_test_update` findings were found.

## 20. What is ready for seed-demo presentation

Ready for a controlled seed-demo/customer-advisor presentation:

- four demo commands
- four-level walkthrough
- current progress-map spec
- explicit load, water-quality, aeration/solids, and selected-cost-pressure
  values
- missing-context and blocked-claim labels
- guardrail language around no safety, no adequacy, no revenue, no
  profitability, and no basil saleability claims

Presentation caveat:

- This is ready as a transparent MVP planning-engine demo, not as field
  validation or an operational recommendation.

## 21. What remains future work

Future work:

- customer/advisor validation
- seed-demo dashboard/report design
- P2c buffer/water/maintenance cost pressure
- Mode B biomass-derived feeding
- runtime-native harvest output for observed/reviewed saleable harvest mass
- fish revenue only with explicit fish harvest and sale-price inputs
- basil revenue only after observed/reviewed saleable harvest mass
- profitability only after explicit revenue and complete-enough cost inputs

Recommended priority order:

1. Customer/advisor validation batch.
2. Seed-demo dashboard/report design if users understand and value the current
   four-level output.
3. P2c only if selected operating-cost pressure is validated as useful.
4. Mode B only if operators cannot reliably provide direct feed input or need
   planning from stock count and average weight.

## 22. Obsidian sync recommendation

Do not modify Obsidian or knowledge-vault files in this pass.

Recommended later sync:

- Add or update a knowledge-vault note summarizing the current four-level MVP
  spine.
- Mark `knowledge-vault/Learnings/Simulation Learnings.md` as older
  simulation-derived context, not current MVP truth.
- Add links from relevant water-quality, aeration, solids, and business notes
  to the current four-level walkthrough and this audit.
- Preserve the boundary that `data/simulation/**` and knowledge-vault notes are
  not canonical machine truth.

## 23. Go / no-go verdict

Go for customer/advisor validation.

Reason:

- The current four-level path runs.
- Tests pass.
- The key terminology and guardrails are in place.
- Current output is useful enough for structured feedback.

No-go for revenue/profitability.

Reason:

- explicit revenue inputs are not present
- total operating cost is not present
- basil saleable harvest mass remains unresolved

Conditional go for seed-demo dashboard/report design.

Condition:

- Start only as a presentation layer for existing outputs and blocked-claim
  labels. Do not add new calculations or claims.

## 24. Recommended next action

Run a small customer/advisor validation batch using the four-level demo and
capture:

- which outputs are credible
- which labels are confusing
- which inputs operators can provide
- whether selected operating-cost pressure is valuable enough to justify P2c
- whether a dashboard/report view would help users understand the current
  output

Do not proceed to revenue, profitability, Mode B, or P2c until validation
feedback indicates those are the right next layer.
