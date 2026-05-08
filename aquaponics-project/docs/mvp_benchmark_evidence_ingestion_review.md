# MVP Benchmark Evidence Ingestion Review

## 1. Purpose

This document reviews the public benchmark mapping pack for
`uvi_like_tilapia_basil_dwc_raft_benchmark_v0` and decides how that evidence
should affect the benchmark fixture, seed-demo report language, expert-question
backlog, and dashboard readiness.

This is a review artifact only. It does not modify the benchmark JSON, the
seed-demo report, source code, canonical knowledge, runtime output, or tests.

## 2. Inputs reviewed

New research input reviewed:

- `data/sources/research_reports/markdown/Public Benchmark Mapping Pack for UVI-Like Tilapia Basil DWC Raft Benchmark.md`

The requested research path exists exactly. No alternate path was needed.

Current repo artifacts reviewed:

- `data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`
- `reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md`
- `docs/mvp_benchmark_scenario_dataset_design.md`
- `docs/mvp_seed_demo_report_design.md`
- `docs/mvp_unit_economics_data_contract.md`
- `docs/mvp_unit_economics_seed_goal_reset.md`
- `docs/mvp_expert_question_backlog_and_source_gap_plan.md`
- `docs/mvp_goal_drift_checklist.md`
- `docs/mvp_operating_manual_decision_playbook.md`

## 3. Research findings summary

The research pack concludes that the current fixture is partly benchmark-backed
and partly scaled scenario overlay.

Strong public/institutional anchors:

- UVI DWC/raft aquaponics architecture.
- 7,800 L fish-tank volume when the concentration scope is explicitly
  `fish_tank`.
- 32% protein tilapia feed.
- pH around 7.0 as an aquaponic compromise.
- Continuous recirculation and aeration.
- Dry-solids prior around 25% of feed on a dry basis.

Important limitations:

- `feed_kg_day = 1.0` does not map cleanly to the full public UVI commercial
  raft module unless a smaller module boundary or raft-area interpretation is
  declared.
- `effective_water_volume_l = 7800` is defensible only as fish-tank
  concentration scope, not total-system average.
- TAN/NH3 values are modelled concentration-context outputs, not observed UVI
  measurements and not safety proof.
- INR feed price, INR electricity price, and the 0.2 kW pump / 0.1 kW blower
  values are scenario overlays or scaled demo assumptions, not public UVI
  benchmark facts.
- Basil production context is benchmarkable, but basil saleable harvest mass
  remains blocked until observed or explicitly reviewed.

Research bottom line:

The fixture is credible enough for pre-customer seed-demo use only if described
as a public-evidence-inspired, scaled, scenario-augmented benchmark. It must not
be presented as a direct reproduction of the full UVI commercial system.

## 4. Current benchmark fixture impact

The current benchmark fixture already carries the most important top-level
guardrails:

- `customer_validated: false`
- `commercial_proof: false`
- `canon_status: not_canon`
- uncertainty labels for not customer validated, not canon, not commercial
  proof, not real-world operating proof, not total operating cost, and not
  profitability
- blocked/null fields for `saleable_harvest_mass_kg`, total cost scope,
  revenue-like outputs, profitability-like outputs, safety, aeration adequacy,
  and solids-removal capacity

The research does not require changing fixture values in this review pass.

Later fixture metadata should become more precise. The fixture currently marks
many fields broadly as `scenario_input`, `benchmark_assumption`, or source-gap
material. A later apply pass should add field-level evidence classes so the
fixture separates benchmark-backed technical anchors from benchmark-informed
scenario inputs, scaled engineering assumptions, non-benchmark business
overlays, modelled outputs, blocked fields, and expert-question candidates.

Recommended change classification:

| impact area | classification | reason |
|---|---|---|
| Add field-level evidence classes to fixture fields | `update_fixture_metadata_later` | Current fixture labels are correct but not specific enough for dashboard/report UI. |
| Keep current numeric fixture values unchanged | `no_change_needed` | Research supports review/metadata changes, not calculation changes. |
| Keep blocked/null fields unchanged | `no_change_needed` | Existing blocked field handling matches the research conclusion. |
| Treat module scope, raft area, and power scaling as unresolved | `expert_question_package` | Public evidence narrows the issue but does not fully define the intended module. |

## 5. Current seed-demo report impact

The current seed-demo report already states that the fixture is pre-customer,
mostly L1/L2, not customer validated, not canon, not commercial proof, and not
real-world operating proof. It also blocks safety, aeration adequacy, total cost
scope, revenue-like outputs, profitability-like outputs, and basil saleable
harvest mass.

The research recommends a wording update later, not a report rewrite in this
pass. The report should make these distinctions more visible:

- "UVI-like" should be softened to "public-evidence-inspired, scaled,
  scenario-augmented benchmark" where external readers could otherwise infer a
  direct full-UVI reproduction.
- Fish-tank TAN/NH3 values should be called modelled concentration-context
  outputs, not observed UVI measurements.
- `effective_water_volume_l = 7800` should always be paired with
  `concentration_scope = fish_tank`.
- Feed price, electricity price, and selected cost-pressure subtotal should be
  called scenario business overlays, not public benchmark facts.
- Pump and blower kW values should be described as scaled nameplate assumptions
  needing expert review.

Recommended change classification:

| impact area | classification | reason |
|---|---|---|
| Add public-evidence-inspired/scaled/scenario-augmented language | `update_report_language_later` | Prevents direct-UVI reproduction overclaim. |
| Strengthen modelled-versus-observed wording | `update_report_language_later` | Prevents TAN/NH3 outputs from reading like observed UVI data. |
| Keep existing blocked-claim panels | `no_change_needed` | Current report already blocks the main forbidden claims. |
| Add dashboard-visible guardrail wording before UI work | `dashboard_guardrail_requirement` | UI could otherwise imply stronger evidence than the fixture supports. |

## 6. Benchmark-backed technical anchors

Use `benchmark_backed_core` later for fields that have the strongest public
benchmark support, while keeping them non-canon and fixture-specific:

- UVI DWC/raft architecture as the reference architecture.
- `protein_fraction = 0.32`.
- `effective_water_volume_l = 7800` only when paired with
  `concentration_scope = fish_tank`.
- `freshwater_assumption = true`.
- pH around 7.0 as aquaponic compromise.
- `dry_solids_coefficient = 0.25` as a generated dry-solids prior.
- 24 h/day pump and blower runtime as continuous-operation context.

These anchors support benchmark credibility. They do not prove safety,
commercial operation, or default design adequacy.

## 7. Benchmark-informed scenario assumptions

Use `benchmark_informed_scenario_input` later for fields that are plausible in
the UVI/SRAC context but remain supplied fixture choices:

- `accumulation_period_day = 1`.
- `concentration_scope = fish_tank`.
- `water_temp_c = 28.0`.
- `measured_do_mg_l = 5.0`.
- `feed_kg_day = 1.0`, if described as a smaller-module or raft-area scenario
  rather than a full-UVI feed benchmark.

These values can remain in the fixture, but language must avoid implying they
are direct observed UVI values.

## 8. Scaled engineering assumptions needing soft language

Use `scaled_engineering_assumption` later for engineering values that need
module-scope and scaling language:

- `demo_pump.device_kw = 0.2`.
- `demo_blower.device_kw = 0.1`.
- `power_basis = nameplate_kw`.
- derived `scenario_power_kwh_day`.
- derived `scenario_power_cost_per_day`.

Continuous runtime is benchmark-aligned, but the specific pump/blower kW values
are not direct full-UVI public benchmark values. They need expert-question
handling before dashboard UI presents them as anything stronger than scaled
demo assumptions.

## 9. Non-benchmark business overlays

Use `non_benchmark_business_overlay` later for business inputs and their
selected cost-pressure outputs:

- `feed_price_per_kg = 45.0 INR/kg`.
- `electricity_price_per_kwh = 7.5 INR/kWh`.
- `scenario_feed_cost_per_day = 45.0 INR/day`.
- `scenario_power_cost_per_day = 54.0 INR/day`.
- `selected_operating_cost_pressure_subtotal = 99.0 INR/day`.

These are acceptable as selected scenario cost-pressure fields. They are not
public benchmark facts, not total operating cost, not revenue, and not
profitability evidence.

## 10. Modelled versus observed wording requirements

Use these wording rules in later fixture/report updates:

| output area | required wording | forbidden implication |
|---|---|---|
| TAN-N concentration | "modelled fish-tank concentration context from fixture inputs" | Observed UVI TAN measurement or safety proof. |
| NH3 fraction / NH3-N / NH3 | "modelled chemistry context from TAN, pH, temperature, and freshwater assumptions" | Toxicity verdict, fish safety, or observed UVI chemistry. |
| Measured DO context | "supplied fixture DO context; benchmark-informed low-end operating context" | Aeration adequacy, oxygen-transfer capacity, or safety margin. |
| Dry-solids potential | "modelled dry-solids generation potential from supplied feed and coefficient" | Solids-removal capacity or captured-sludge volume. |
| Selected operating-cost pressure subtotal | "scenario feed plus electricity cost-pressure subtotal from supplied prices and nameplate power assumptions" | Total operating cost, commercial proof, profitability, or economic viability. |

## 11. Basil saleability handling

Basil production context is benchmarkable. The research supports UVI-like basil
production and harvest-regime context, but it does not support a known
saleable harvest quantity for this fixture.

Required handling:

- Keep `saleable_harvest_mass_kg` null/blocked unless observed or explicitly
  reviewed.
- Do not infer saleable output from basil production context, plant density,
  growth period, feed rate, gross harvest, or benchmark yield.
- Treat basil saleability as `blocked_until_observed_or_reviewed`.
- Save evidence-standard questions for the expert/customer package.

Recommended change classification:

| item | classification | reason |
|---|---|---|
| Keep basil saleable mass blocked | `no_change_needed` | Current fixture and report already enforce this. |
| Add clearer saleability evidence-class language later | `update_report_language_later` | Helps dashboard/report readers distinguish production context from saleable output. |
| Ask what observed/reviewed record is sufficient | `expert_question_package` | Public benchmark evidence does not answer the repo's non-null evidence rule. |

## 12. Field-level impact table

| field name | current value | current interpretation | research finding | recommended evidence class | recommended wording | later apply-pass action | dashboard/report guardrail needed |
|---|---:|---|---|---|---|---|---|
| `architecture` | `tilapia_basil_dwc_raft` | Scenario identity and benchmark framing. | UVI DWC/raft is the closest public architecture anchor. | `benchmark_backed_core` | Public-evidence-inspired UVI/SRAC raft architecture. | `update_fixture_metadata_later` | State not direct full-UVI reproduction. |
| `fish_species` | tilapia | Scenario identity. | UVI benchmark matches tilapia context. | `benchmark_backed_core` | Tilapia context only. | `update_fixture_metadata_later` | No yield or safety implication. |
| `plant_species` | basil | Scenario identity. | UVI supports basil production context. | `benchmark_backed_core` | Basil production context, not saleable output. | `update_fixture_metadata_later` | Saleability remains blocked. |
| `feed_kg_day` | 1.0 kg/day | L1 scenario input. | Does not map cleanly to full UVI raft module without smaller module or raft area. | `scaled_engineering_assumption` plus `expert_question_candidate` | Scaled feed scenario; not full-UVI feed benchmark. | `update_fixture_metadata_later`; `expert_question_package` | Show missing module scope and raft area. |
| `protein_fraction` | 0.32 | L1 scenario input. | Strongly supported by UVI/SRAC tilapia feed context. | `benchmark_backed_core` | UVI/SRAC-backed feed-protein anchor for this fixture. | `update_fixture_metadata_later` | Still not canon/default feed value. |
| `effective_water_volume_l` | 7800 L | L1 scenario input. | Defensible only as UVI rearing-tank/fish-tank scope, not total system average. | `benchmark_backed_core` with scope condition | 7,800 L fish-tank concentration scope. | `update_fixture_metadata_later`; `update_report_language_later` | Always pair with `concentration_scope = fish_tank`. |
| `accumulation_period_day` | 1 day | L1 scenario input. | Daily basis is compatible with feed-ratio logic, but this is a modelling timestep. | `benchmark_informed_scenario_input` | One-day modelling timestep. | `update_fixture_metadata_later` | Do not call measured residence time. |
| `concentration_scope` | `fish_tank` | L1 scenario input. | Correct convention for 7,800 L; not total-system average. | `benchmark_informed_scenario_input` | Fish-tank local concentration scope. | `update_fixture_metadata_later`; `update_report_language_later` | UI must prevent whole-system interpretation. |
| `ph` | 7.0 | L1 scenario input. | Strong aquaponic compromise anchor. | `benchmark_backed_core` | Benchmark-backed pH context. | `update_fixture_metadata_later` | Chemistry context only. |
| `water_temp_c` | 28.0 C | L1 scenario input. | Warmwater tilapia context is supported, but this is still fixture-supplied. | `benchmark_informed_scenario_input` | Benchmark-informed temperature scenario. | `update_fixture_metadata_later` | No safety verdict. |
| `freshwater_assumption` | true | L1 scenario input. | UVI-compatible freshwater context. | `benchmark_backed_core` | Freshwater aquaponics context. | `update_fixture_metadata_later` | No broad system claim. |
| `measured_do_mg_l` | 5.0 mg/L | Supplied DO context. | Defensible low-end UVI/SRAC operating context, not proof of margin. | `benchmark_informed_scenario_input` | Supplied DO context, benchmark-informed. | `update_fixture_metadata_later`; `update_report_language_later` | Do not imply aeration adequacy. |
| `dry_solids_coefficient` | 0.25 | L1 scenario input. | Strong dry-solids generation prior. | `benchmark_backed_core` | Generated dry-solids prior, dry basis. | `update_fixture_metadata_later` | Not captured sludge or removal capacity. |
| `demo_pump.device_kw` | 0.2 kW | Nameplate scenario input. | Not a direct UVI full-system pump benchmark; needs scaling rationale. | `scaled_engineering_assumption`; `expert_question_candidate` | Scaled nameplate pump assumption. | `update_fixture_metadata_later`; `expert_question_package` | Show scaling uncertainty. |
| `demo_blower.device_kw` | 0.1 kW | Nameplate scenario input. | Not a direct UVI full-system blower benchmark; needs scaling rationale. | `scaled_engineering_assumption`; `expert_question_candidate` | Scaled nameplate blower assumption. | `update_fixture_metadata_later`; `expert_question_package` | Show scaling uncertainty. |
| pump/blower runtime | 24 h/day | Continuous runtime scenario. | Continuous operation is benchmark-aligned. | `benchmark_backed_core` for runtime mode | Continuous operation context. | `update_fixture_metadata_later` | Runtime mode does not prove capacity. |
| `power_basis` | `nameplate_kw` | Nameplate basis. | Acceptable as demo assumption; not measured consumption. | `benchmark_informed_scenario_input` | Nameplate power basis, not metered draw. | `update_fixture_metadata_later`; `update_report_language_later` | UI must show nameplate basis. |
| `feed_price_per_kg` | 45.0 INR/kg | Scenario cost input. | Not a public UVI benchmark fact. | `non_benchmark_business_overlay` | Scenario feed-price overlay. | `update_fixture_metadata_later`; `update_report_language_later` | Do not present as benchmark price. |
| `electricity_price_per_kwh` | 7.5 INR/kWh | Scenario tariff input. | Not a public UVI benchmark fact. | `non_benchmark_business_overlay` | Scenario electricity-price overlay. | `update_fixture_metadata_later`; `update_report_language_later` | Do not present as benchmark tariff. |
| `tan_n_load_*` | 0.02944 kg/day; 29.44 g/day | Derived regression anchor. | Modelled output from fixture feed/protein inputs. | `modelled_output_not_observed` | Modelled load output from fixture inputs. | `update_fixture_metadata_later`; `update_report_language_later` | Not observed UVI load. |
| `estimated_tan_n_mg_l` | 3.7743589743589743 mg/L | Derived fish-tank concentration context. | Modelled fish-tank context, not observed UVI measurement. | `modelled_output_not_observed` | Modelled fish-tank TAN-N context. | `update_fixture_metadata_later`; `update_report_language_later` | No safety claim. |
| `estimated_unionized_nh3_fraction` | 0.006971085009084945 | Derived chemistry context. | Chemically plausible modelled context, not observed. | `modelled_output_not_observed` | Modelled NH3 fraction context. | `update_fixture_metadata_later`; `update_report_language_later` | No toxicity verdict. |
| `estimated_nh3_n_mg_l` | 0.026311377265059072 mg/L | Derived chemistry context. | Modelled output, not observed. | `modelled_output_not_observed` | Modelled NH3-N context. | `update_fixture_metadata_later`; `update_report_language_later` | No fish safety claim. |
| `estimated_nh3_mg_l` | 0.031949529536143155 mg/L | Derived chemistry context. | Modelled output, not observed. | `modelled_output_not_observed` | Modelled NH3 context. | `update_fixture_metadata_later`; `update_report_language_later` | No system safety claim. |
| `oxygen_demand_g_day` | 134.5408 g/day | Derived nitrification sub-load. | Modelled demand context. | `modelled_output_not_observed` | Modelled nitrification oxygen-demand sub-load. | `update_fixture_metadata_later` | Not aeration capacity or adequacy. |
| `alkalinity_demand_g_caco3_day` | 210.2016 g/day | Derived demand context. | Modelled demand context. | `modelled_output_not_observed` | Modelled alkalinity demand context. | `update_fixture_metadata_later` | Not a dosing recommendation. |
| `estimated_dry_solids_potential_kg_day` | 0.25 kg/day | Derived solids potential. | Modelled generated dry-solids potential. | `modelled_output_not_observed` | Modelled dry-solids generation potential. | `update_fixture_metadata_later`; `update_report_language_later` | Not removal capacity. |
| `scenario_feed_cost_per_day` | 45.0 INR/day | Derived selected cost pressure. | Scenario business overlay. | `non_benchmark_business_overlay`; `modelled_output_not_observed` | Scenario feed cost-pressure output. | `update_fixture_metadata_later`; `update_report_language_later` | Not revenue/profitability or total cost. |
| `scenario_power_kwh_day` | 7.2 kWh/day | Derived from nameplate assumptions. | Derived from scaled nameplate assumptions. | `scaled_engineering_assumption`; `modelled_output_not_observed` | Scenario nameplate power context. | `update_fixture_metadata_later`; `update_report_language_later` | Not metered power. |
| `scenario_power_cost_per_day` | 54.0 INR/day | Derived selected cost pressure. | Scenario business overlay. | `non_benchmark_business_overlay`; `modelled_output_not_observed` | Scenario power cost-pressure output. | `update_fixture_metadata_later`; `update_report_language_later` | Not total cost. |
| `selected_operating_cost_pressure_subtotal` | 99.0 INR/day | Selected feed + electricity subtotal. | Internally consistent scenario subtotal, not public benchmark cost. | `non_benchmark_business_overlay`; `modelled_output_not_observed` | Selected scenario cost-pressure subtotal. | `update_fixture_metadata_later`; `update_report_language_later` | Not total operating cost. |
| `saleable_harvest_mass_kg` | null | Blocked field. | Basil production is benchmarkable, saleable mass is not known. | `blocked_until_observed_or_reviewed` | Blocked until observed or explicitly reviewed. | `no_change_needed`; later language can clarify | Do not infer from benchmark. |

## 13. Evidence-class system for later fixture/report updates

| evidence class | meaning | allowed use |
|---|---|---|
| `benchmark_backed_core` | Strong public/institutional anchor for this fixture context. | Fixture/report metadata only; not canon. |
| `benchmark_informed_scenario_input` | Plausible value informed by benchmark context but still supplied as a scenario input. | Demo scenario with visible status label. |
| `scaled_engineering_assumption` | Engineering input scaled or selected for the demo module. | Demo scenario only, with scaling caveat. |
| `non_benchmark_business_overlay` | Price, tariff, or cost-pressure field not backed by public UVI benchmark evidence. | Scenario cost-pressure only. |
| `modelled_output_not_observed` | Output generated from fixture inputs or current engine path. | Explain model structure; do not treat as observed data. |
| `blocked_until_observed_or_reviewed` | Field must stay null/blocked until observed or explicitly reviewed. | Guardrail and future data planning only. |
| `expert_question_candidate` | Public evidence narrows the issue but does not safely resolve it. | Expert/advisor package, not automatic fixture promotion. |

## 14. Expert-question package candidates

Prepare a short expert package before dashboard/report UI work tries to present
the fixture as a coherent module:

1. What exact module scale does `feed_kg_day = 1.0` represent under UVI-like
   feed-to-area logic?
2. What raft growing area should be paired with the 1.0 kg/day feed scenario?
3. Is the intended module one UVI fish tank with proportional raft area, a
   smaller demo unit, or another scoped module?
4. Should the report show only fish-tank concentration context, or also show a
   separately labelled total-system dilution context in a later design?
5. How should pump and blower nameplate power be scaled from public UVI
   equipment to this fixture?
6. What backup power or backup aeration status must be collected before any
   reliability-adjacent language is allowed?
7. What observed or explicitly reviewed basil handling/buyer evidence is
   sufficient before `saleable_harvest_mass_kg` can become non-null?

Recommended change classification:

| package item | classification | timing |
|---|---|---|
| Module scope and raft-area questions | `expert_question_package` | Before dashboard UI. |
| Power-scaling questions | `expert_question_package` | Before dashboard UI or P2c extension. |
| Concentration-scope presentation question | `expert_question_package` | Before expanded report/dashboard design. |
| Basil saleability evidence question | `expert_question_package` | Before any output/revenue contract update. |

## 15. Dashboard readiness verdict

Dashboard readiness verdict:

`caution_update_metadata_and_language_first`

Reason:

The fixture is credible enough for pre-customer seed-demo use when described as
public-evidence-inspired, scaled, and scenario-augmented. It is not ready for a
polished dashboard that could visually imply direct UVI reproduction, safety,
profitability, known basil saleability, or real-world operating proof.

Minimum blockers to clear before dashboard work:

1. Add field-level evidence-class metadata to the benchmark fixture in a later
   approved apply pass.
2. Update seed-demo report language to distinguish benchmark-backed anchors,
   scenario inputs, scaled engineering assumptions, non-benchmark business
   overlays, modelled outputs, and blocked fields.
3. Prepare the expert-question package around module scope, raft area,
   concentration scope, and power scaling.
4. Require dashboard panels for evidence class, readiness level, modelled versus
   observed status, fish-tank concentration scope, and blocked claims.

If dashboard work begins before those blockers are cleared, it should remain a
review-first design artifact only.

## 16. Recommended later apply-pass scope

Recommended phased scope:

### Phase 1: benchmark fixture metadata/classification update

Allowed future scope, only if explicitly approved:

- update `data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`
  field metadata
- add evidence classes from this review
- add module-scope and raft-area source-gap fields
- preserve all current numeric values unless a separate approved value-change
  review exists
- keep `saleable_harvest_mass_kg` null/blocked

### Phase 2: seed-demo report language update

Allowed future scope, only if explicitly approved:

- update `reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md`
- add public-evidence-inspired, scaled, scenario-augmented wording
- clarify modelled versus observed outputs
- clarify fish-tank concentration scope
- clarify scenario business overlays
- preserve blocked-claim panels

### Phase 3: expert-question package

Allowed future scope, only if explicitly approved:

- create a docs-only expert-question package
- focus on module scope, raft area, power scaling, concentration presentation,
  backup status, and basil saleability evidence
- do not modify canonical open-question tickets unless a later pass explicitly
  allows it

### Phase 4: dashboard/report UI design only after guardrails are visible

Allowed future scope, only if explicitly approved:

- create a review-first dashboard/report UI design doc
- require visible evidence-class, readiness, scope, modelled-output, and blocked
  claim panels
- do not create a dashboard implementation until a later implementation pass is
  explicitly approved

## 17. Blocked claims and guardrails

This review does not allow any of these claims:

- customer validation
- commercial proof
- real-world operating proof
- system safety
- fish safety
- aeration adequacy
- solids-removal capacity
- total operating cost
- revenue
- profitability
- economic viability
- commercial operability
- known basil saleable harvest mass
- canon/default assumptions
- direct reproduction of the full UVI commercial system

Guardrail interpretation:

- Benchmark-backed core fields are still fixture/report evidence, not canon.
- Scenario inputs remain scenario inputs until a later approved source-backed
  update changes their status.
- Modelled outputs are not observed UVI measurements.
- Selected cost-pressure is not total cost scope.
- Basil production context is not known saleable basil mass.
- Dashboard visuals must not imply stronger evidence than the field metadata
  supports.

## 18. Recommended next action

Run a later review-first apply pass for Phase 1 only: add field-level evidence
classes and scope metadata to
`data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`, preserving
the existing fixture values and blocked/null fields. After that, run a separate
Phase 2 report-language update pass before any dashboard/report UI design work.
