# MVP Seed-Demo Dashboard/Report UI Design

## 1. Purpose

This document defines a docs-only dashboard/report UI design for the current
Aquaponics MVP seed-demo pathway.

The design goal is to show technical advisors, investors, aquaponics/RAS
experts, and future operator/customer reviewers what the current benchmark-backed
MVP calculates, what assumptions it uses, what is modelled, what is blocked, and
what data is needed next.

This is part of expert-reviewed benchmark readiness before prototype UI. It is
not polished dashboard implementation, commercial dashboard readiness, a
generated report, UI code, React component work, calculation work, benchmark JSON
work, canonical data work, runtime work, source work, test work, or Obsidian
work.

The UI must make uncertainty visible. Evidence class, readiness level, scope,
modelled-versus-observed status, business-overlay status, and blocked claims
must be displayed in the main interface, not hidden in footnotes.

## 2. Relationship to benchmark fixture, seed-demo report, and expert-question package

This design is downstream of the current benchmark fixture and seed-demo report:

- `data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json` is the
  benchmark fixture/design dataset.
- `reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md` is
  the current human-readable seed-demo report.
- `docs/mvp_benchmark_evidence_ingestion_review.md` defines the current
  evidence-class and guardrail posture.
- `docs/mvp_expert_question_package_for_benchmark_review.md` defines the
  expert-review questions that should stay visible before stronger UI work.
- `docs/mvp_expert_question_backlog_and_source_gap_plan.md` separates expert
  questions, later customer/operator questions, blocked data, and
  do-not-pursue-now items.

The benchmark fixture is public-evidence-inspired, scaled, and
scenario-augmented. It is not a direct UVI reproduction, not canon, not customer
validation, not commercial proof, and not real-world operating proof.

The dashboard/report UI should present the current report and fixture more
clearly. It must not change the fixture, report, data contract, business layer,
ontology, runtime path, scripts, tests, configs, or Obsidian notes.

## 3. Goal-drift checklist verdict

Verdict: CAUTION.

Reason: the goal-drift checklist treats seed-demo dashboard design as useful but
premature unless it is rewritten as a docs-only, review-first, guardrail-focused
design with no new calculations, no generated UI, and no commercial claims. This
pass meets that narrow condition.

Allowed continuation basis:

- docs-only design artifact
- review-first framing
- no implementation or prototype
- no new dashboard, report, slides, JSON, data, code, config, runtime,
  simulation, source, test, or Obsidian changes
- blocked claims and readiness labels are mandatory visible panels
- benchmark scenario assumptions remain scenario assumptions, not canon

Stop if a later pass would turn this into implementation, app/game expansion,
revenue/profitability work, hidden-guardrail polish, or a claim that benchmark
context proves safety, customer validation, commercial operation, real-world
operation, total operating cost, revenue, profitability, or saleable basil
harvest.

## 4. Target users and primary user story

Target users:

| user | primary need | UI emphasis |
|---|---|---|
| Technical investor/advisor | Understand whether the MVP is disciplined enough for expert-reviewed seed-demo discussion. | Current four-level spine, benchmark status, evidence labels, blocked claims, next data needed. |
| Aquaponics/RAS expert | Review system boundary, units, scope, water-quality interpretation, aeration/solids boundaries, and source gaps. | Fish-tank scope warnings, modelled-versus-observed labels, expert-question cards, assumption register. |
| Future operator/customer reviewer | Understand what data would be needed later from an actual unit and which current values are only scenario context. | Required observed records, readiness levels, blocked outputs, modelled labels, customer/operator data state. |

Primary user story:

As a reviewer, I can understand what the current MVP calculates, what
assumptions it uses, what is benchmark-backed, what is scenario-only, what is
modelled, what is blocked, and what data is needed next.

## 5. Dashboard/report information architecture

Recommended information architecture:

1. Front-page status and caution summary.
2. Benchmark scenario identity and framing.
3. Four-level MVP output path.
4. System-flow visual with scope boundaries.
5. Evidence-class and readiness legend.
6. Assumption register.
7. Scope-warning panel.
8. Modelled-versus-observed panel.
9. Business-overlay panel.
10. Blocked-claims and guardrail panel.
11. Expert-question panel.
12. Next-data-needed panel.
13. Dashboard state indicator.
14. Traceability/audit detail.
15. Validation checklist for a later prototype.

The front page should answer "what am I looking at?" and "what can this not
claim?" before showing detailed values.

## 6. Recommended layout

Use a restrained seed-demo report/dashboard layout, not a commercial operating
dashboard:

1. Header band: scenario name, scenario ID, MVP spine, current state badge, and
   CAUTION badge.
2. First row: summary cards for benchmark identity, output path, evidence
   ceiling, blocked claims, and next data needed.
3. Second row: four-level output panel and system-flow visual.
4. Third row: evidence/readiness legend and assumption-register preview.
5. Fourth row: guardrail panels for scope, modelled status, business overlays,
   and blocked claims.
6. Fifth row: expert-question cards and next-data checklist.
7. Appendix/detail: full traceability table, validation rules, and prototype
   implementation boundaries.

The interface should use explicit labels such as `modelled output not observed`,
`L1 scenario input`, `non-benchmark business overlay`, and `blocked until
observed or reviewed` beside values.

## 7. Front-page summary cards

Recommended cards:

| card | content | required warning |
|---|---|---|
| Scenario | `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`; tilapia + basil DWC/raft; version `v0`. | Public-evidence-inspired, scaled, scenario-augmented. |
| Current MVP path | Mode A + P1 + P1.5 + P2a. | Shows current approved output path only. |
| Evidence ceiling | Mostly L1 scenario input plus L2 source-planned benchmark context. | Not L4 observed customer/operator data or L5 reviewed commercial data. |
| Output status | Load, chemistry context, aeration/solids context, selected cost pressure. | Modelled/current-engine context unless explicitly labelled otherwise. |
| Blocked claims | Safety, adequacy, total cost, revenue, profitability, commercial operability, customer validation, saleable basil mass. | Must remain visually prominent. |
| Next data needed | Real records, reviewed crop saleability, labor/maintenance records, feed/electricity records, equipment metering, buyer/channel pricing, customer/operator validation. | Future data only, not inferred from benchmark fixture. |

The front page should not use launch, validated, profitable, safe, ready-to-run,
or commercial-operability language.

## 8. Benchmark scenario panel

The benchmark scenario panel should display:

| field | display |
|---|---|
| Scenario ID | `uvi_like_tilapia_basil_dwc_raft_benchmark_v0` |
| Scenario name | UVI-like tilapia basil DWC raft benchmark v0 |
| Architecture | `tilapia_basil_dwc_raft` |
| Fish/plant pair | tilapia + basil |
| MVP pathway | pre-customer Mode A + P1 + P1.5 + P2a seed-demo fixture |
| Framing | public-evidence-inspired, scaled, scenario-augmented |
| Evidence/readiness | mostly `L1_scenario_input`; source-planned `L2_benchmark_assumption_with_source` context |
| Direct UVI reproduction | false |
| Canon status | `not_canon` |
| Customer validation | false |
| Commercial proof | false |
| Real-world operating proof | false |

The panel should include a visible callout:

This scenario is useful because it is explicit and traceable. It is not a direct
copy of the full UVI commercial system and does not validate customer value,
commercial operation, or field performance.

## 9. Four-level MVP output panel

The output panel should show the current four-level path as one compact flow and
one detail table:

| level | role | values to display | required label |
|---|---|---|---|
| Mode A load-only | Direct feed and protein to waste/load context. | TAN-N load 29.44 g/day; nitrification oxygen demand 134.5408 g/day; alkalinity demand 210.2016 g CaCO3/day. | Modelled fixture output from supplied inputs; no biomass-derived feeding. |
| P1 TAN-N/NH3 context | Fish-tank concentration and NH3 chemistry context. | estimated fish-tank TAN-N 3.7743589743589743 mg/L; unionized NH3 fraction 0.006971085009084945; estimated NH3-N 0.026311377265059072 mg/L; estimated NH3 0.031949529536143155 mg/L. | Modelled fish-tank chemistry context; not observed UVI measurement; not fish-safety proof. |
| P1.5 aeration/solids context | Supplied DO context and dry-solids potential. | measured DO context 5.0 mg/L; dry-solids potential 0.25 kg/day; nitrification oxygen demand as sub-load. | DO context is not aeration adequacy; dry-solids potential is not removal capacity. |
| P2a selected cost pressure | Explicit selected feed and electricity cost-pressure overlay. | scenario feed cost 45.0 INR/day; scenario power cost 54.0 INR/day; selected cost-pressure subtotal 99.0 INR/day. | Non-benchmark business overlay; not total operating cost, revenue, or profitability. |

The panel should not add totals, ratios, margins, viability indicators, or
traffic-light health status.

## 10. System-flow visual

The system-flow visual should be a simple labelled flow, not a polished
commercial operations diagram:

`fish feed input -> tilapia tank -> solids filtration -> biofilter/aeration -> DWC/raft basil bed -> data/report layer`

Required visual labels:

| node | label | visible caveat |
|---|---|---|
| Fish feed input | Mode A direct input. | No biomass-derived feeding. |
| Tilapia tank | Fish-tank TAN/NH3 context. | Fish-tank scope only; no fish-safety claim. |
| Solids filtration | Solids handling context. | Dry-solids potential is not solids-removal capacity. |
| Biofilter/aeration | Nitrification oxygen demand and supplied DO context. | No aeration adequacy or system-safety claim. |
| DWC/raft basil bed | Basil production context. | No known saleable basil harvest mass. |
| Data/report layer | Evidence, readiness, assumptions, outputs, blocked claims. | Fixture/report layer, not canon or customer validation. |

If a future UI uses icons or a schematic, every node must keep its caveat
visible in the same viewport.

## 11. Evidence-class and readiness labels

Evidence classes to display:

| label | display meaning | current UI use |
|---|---|---|
| `benchmark_backed_core` | Strong public or institutional anchor for this fixture context. | Architecture, species context, freshwater and some technical anchors. |
| `benchmark_informed_scenario_input` | Plausible benchmark-context value still supplied as scenario input. | Concentration scope, timestep, temperature, DO context, nameplate basis. |
| `scaled_engineering_assumption` | Engineering value scaled or selected for this demo fixture. | 1.0 kg/day feed scalar, pump/blower kW, scenario power kWh/day. |
| `non_benchmark_business_overlay` | Price, tariff, or cost-pressure field not backed by public UVI benchmark evidence. | INR feed price, INR electricity price, selected cost-pressure outputs. |
| `modelled_output_not_observed` | Output generated from fixture inputs or current engine path. | TAN-N, NH3, oxygen demand, alkalinity demand, dry-solids potential, selected subtotal. |
| `blocked_until_observed_or_reviewed` | Field remains unavailable until observed data or explicit review exists. | Saleable basil mass, safety, revenue, profitability, total cost, commercial operability. |
| `expert_question_candidate` | Public evidence narrows the issue but does not safely resolve it. | Module scope, raft area, concentration display, pump/blower scaling, backup status, basil saleability standard. |

Readiness levels to display:

| level | meaning | current interpretation |
|---|---|---|
| L0 blocked/unavailable | Missing, unresolved, or blocked by guardrail. | Blocked claims, source gaps, saleable harvest mass. |
| L1 scenario input | Manually supplied scenario value with no external-source claim. | Current fixture inputs and regression anchors. |
| L2 benchmark assumption with source | Public, institutional, or supplier-backed benchmark value with metadata. | Source-reviewed or source-planned benchmark context only. |
| L3 measured internal/pilot data | Internal or pilot measurement, not customer/operator validation. | Future state; not present in current fixture. |
| L4 observed customer/operator data | Observed data from customer or operator setting. | Future state; not present in current fixture. |
| L5 reviewed/validated commercial data | Reviewed commercial data for scoped decision support. | Future state; not present in current fixture. |

The UI should show the current evidence ceiling as L1/L2. L3 through L5 should
appear in the legend as future states, not as current evidence.

## 12. Assumption register UI

The assumption register should use this column set:

| field | value/status | evidence class | readiness level | source basis | report treatment | notes |
|---|---|---|---|---|---|---|

Required row groups:

- scenario identity
- scenario inputs
- benchmark-backed or benchmark-informed assumptions
- scaled engineering assumptions
- non-benchmark business overlays
- modelled outputs
- blocked or null fields
- expert-question candidates

Minimum visible rows:

| field | value/status | evidence class | readiness | treatment |
|---|---|---|---|---|
| `feed_kg_day` | 1.0 kg/day | scaled engineering assumption; expert-question candidate | L1 | scaled scenario input |
| `protein_fraction` | 0.32 | benchmark-backed core | L1/L2 context | technical anchor, not canon |
| `effective_water_volume_l` | 7800 L | benchmark-backed core with fish-tank scope | L1/L2 context | fish-tank concentration scope |
| `concentration_scope` | `fish_tank` | benchmark-informed scenario input | L1 | scope convention |
| `measured_do_mg_l` | 5.0 mg/L | benchmark-informed scenario input | L1 | supplied DO context |
| `feed_price_per_kg` | 45.0 INR/kg | non-benchmark business overlay | L1 | selected cost-pressure input |
| `electricity_price_per_kwh` | 7.5 INR/kWh | non-benchmark business overlay | L1 | selected cost-pressure input |
| `demo_pump` | 0.2 kW, 24 h/day, nameplate basis | scaled engineering assumption; expert-question candidate | L1 | nameplate power record |
| `demo_blower` | 0.1 kW, 24 h/day, nameplate basis | scaled engineering assumption; expert-question candidate | L1 | nameplate power record |
| `saleable_harvest_mass_kg` | null/unresolved | blocked until observed or reviewed | L0 | blocked, not zero |

The register should support filtering by evidence class and readiness level, but
the default view should not hide blocked rows.

## 13. Scope-warning UI

The scope-warning UI should be a persistent panel near the benchmark scenario
and P1 output sections.

Required warnings:

- Fish-tank scope: the current TAN/NH3 concentration context is fish-tank
  scoped.
- Not total system volume: `effective_water_volume_l = 7800` must not be shown
  as whole-system volume.
- Not whole-system average: current concentration display is not a
  whole-system average concentration.
- Module boundary unresolved: the fixture does not yet resolve whether the
  bounded unit is a full UVI system, one fish tank plus proportional raft area,
  a smaller demo module, or another scoped unit.
- Raft area implied by 1 kg/day feed unresolved: `feed_kg_day = 1.0` must not
  imply a full-UVI raft area or saleable basil output.

The UI should keep these warnings visible whenever a reviewer sees water-quality
values, feed scalar, system-flow visual, or plant-side context.

## 14. Modelled-versus-observed UI

The UI should separate current-engine modelled outputs from observed data:

| group | current status | required UI label |
|---|---|---|
| TAN-N load and oxygen/alkalinity demand | Modelled from supplied feed/protein inputs. | Modelled fixture output, not observed UVI load. |
| Fish-tank TAN/NH3 values | Modelled current-engine chemistry context. | Modelled fish-tank context, not observed UVI measurement. |
| DO context | Supplied fixture DO context. | Supplied context only, not aeration adequacy. |
| Dry-solids potential | Modelled generation potential from supplied feed and coefficient. | Potential only, not captured sludge or removal capacity. |
| Selected cost pressure | Derived from scenario feed price, tariff, and nameplate power assumptions. | Scenario business overlay, not total operating cost. |

No card should use health, safe, unsafe, adequate, viable, validated, or
operable as an output state.

## 15. Business-overlay UI

Business-overlay fields should be grouped separately from benchmark technical
fields:

| field | display | required warning |
|---|---|---|
| Scenario feed price | 45.0 INR/kg; scenario feed cost 45.0 INR/day. | Non-benchmark business overlay; not public UVI benchmark fact. |
| Scenario electricity price | 7.5 INR/kWh; scenario power cost 54.0 INR/day. | Non-benchmark business overlay; not tariff validation. |
| Scenario power kWh/day | 7.2 kWh/day. | Nameplate power context, not metered power. |
| Selected cost-pressure subtotal | 99.0 INR/day. | Selected feed plus electricity pressure only; not total operating cost. |

The UI must not calculate or imply revenue, gross margin, profit, ROI, payback,
break-even, economic viability, or complete cost scope.

## 16. Blocked-claims and guardrail panel

The blocked-claims panel should be visible on the front page and repeated in
detail view. It should use locked guardrail cards or equivalent high-visibility
components.

Required blocked claims:

- no fish safety claim
- no system safety claim
- no aeration adequacy claim
- no solids-removal capacity claim
- no total operating cost claim
- no revenue claim
- no profitability claim
- no commercial operability claim
- no customer validation claim
- no known basil saleable harvest mass

The panel should also state that the benchmark scenario is not canon, not direct
UVI reproduction, not commercial proof, and not real-world operating proof.

Blocked claims are not optional help text. They are core UI content.

## 17. Expert-question panel

The expert-question panel should show high-priority review questions as cards:

| question area | required card prompt | why visible |
|---|---|---|
| Module scope | What exact module boundary does this fixture represent? | Prevents direct-UVI reproduction or hidden scale claims. |
| Raft area implied by 1 kg/day feed | What raft growing area, if any, should be paired with `feed_kg_day = 1.0`? | Prevents plant-output or saleability inference. |
| Fish-tank versus total-system display | Should future reports show only fish-tank context or a separate total-system context? | Prevents concentration-scope confusion. |
| Pump/blower scaling | How should pump and blower nameplate values be scaled or labelled? | Prevents scenario power from looking measured or benchmark-proven. |
| Backup aeration/power status | What backup status records are needed before reliability-adjacent wording is allowed? | Prevents hidden safety or resilience claims. |
| Basil saleability evidence standard | What observed or reviewed basil handling/buyer evidence is enough before `saleable_harvest_mass_kg` can become non-null? | Prevents proxy-based saleable-harvest inference. |

Card states should be `open`, `answered in later review`, or `blocked until
observed/customer/operator data`. This design does not create canonical
open-question tickets.

## 18. Next-data-needed panel

The next-data-needed panel should be a checklist with status and reason:

| data needed | current status | unlocks later |
|---|---|---|
| Real fish output | unavailable | Fish-output review and later fish economics only after explicit quantity/status/price records. |
| Observed/reviewed basil saleable output | blocked | Non-null `saleable_harvest_mass_kg` only after observed or explicitly reviewed evidence. |
| Labor/maintenance records | source gap | Broader cost-scope design after task, cadence, and cost basis are explicit. |
| Feed/electricity records | scenario/source gap | Stronger source-backed cost-pressure labels after dated supplier/tariff metadata. |
| Equipment metering | unavailable | Future measured power context; current values remain nameplate/scenario. |
| Buyer/channel pricing | unavailable | Future revenue inputs only with quantity, price, currency, date, geography, channel, and status. |
| Later customer/operator validation | unavailable | Customer/operator feedback, not available from the benchmark fixture. |

The checklist should not present unavailable data as a defect in the current
demo. It should present them as explicit gates before stronger claims.

## 19. Dashboard states

The UI should support these states:

| state | when shown | allowed display | disallowed display |
|---|---|---|---|
| Benchmark demo state | Current state. | L1/L2 scenario and benchmark context, modelled outputs, blocked claims, expert questions. | L3-L5 evidence labels, observed/customer wording, safety or economics claims. |
| Expert-review state | After expert answers are recorded in a later approved artifact. | Answered question cards and revised wording recommendations. | Canon promotion or hidden unresolved fields. |
| Future measured-data state | After real internal/pilot or operator records exist in a later approved path. | L3/L4 measured/observed labels where supported. | Mixing measured and scenario values without labels. |
| Blocked/revenue-unavailable state | Current and future until explicit saleable quantity and sale records exist. | Null/blocked revenue, saleability, profitability, and total-cost cards. | Any inferred revenue, profit, total operating cost, or saleable basil mass. |

Current default state: benchmark demo state with blocked/revenue-unavailable
cards visible.

## 20. Visual component recommendations

Recommended components:

- KPI cards for current approved values, each with evidence-class chip and
  readiness badge.
- Output flow for Mode A -> P1 -> P1.5 -> P2a.
- System-flow visual for feed/tank/solids/biofilter-aeration/raft/report layer.
- Assumption table with filterable evidence-class and readiness columns.
- Evidence-class chips using the exact class labels from the fixture/report
  posture.
- Readiness badges for L0 through L5.
- Locked guardrail cards for blocked claims.
- Expert-question cards with open/answered/blocked state.
- Next-data checklist with required record type and later decision unlocked.
- Traceability links or field references from each displayed value to fixture
  field, report row, evidence class, readiness level, and status.

Use quiet report/dashboard styling. Avoid a product-marketing landing page,
commercial control-room styling, green success-only status, or visuals that make
scenario values feel observed.

## 21. Above-the-fold versus detail/appendix content

Above the fold:

- scenario ID and benchmark framing
- CAUTION state
- Mode A + P1 + P1.5 + P2a path
- evidence ceiling: mostly L1/L2, not L4/L5
- direct warnings: not direct UVI reproduction, not customer validation, not
  commercial proof, not real-world operating proof
- summary cards for current outputs
- blocked-claims panel
- fish-tank scope warning
- modelled-versus-observed warning

Detail/appendix:

- full assumption register
- full evidence-class legend
- readiness definitions
- field-by-field traceability
- source-gap list
- expert-question detail
- future data checklist
- validation checklist for prototype implementation
- language rules and forbidden wording

Blocked claims must appear above the fold and in detail view.

## 22. Traceability and auditability

Each displayed value should trace to:

| displayed item | trace fields |
|---|---|
| Scenario identity | fixture path, `scenario_identity`, scenario ID, version, architecture, fish/plant pair, status labels. |
| Current output value | fixture expected output field, report row, current integrity snapshot value, evidence class, readiness level. |
| Assumption | fixture field, source basis, evidence class, readiness level, scenario/benchmark/modelled/blocked status. |
| Scope warning | fixture concentration scope, fish-tank volume label, expert-question card if unresolved. |
| Business overlay | feed price/tariff/power-basis field, non-benchmark business overlay label, selected-scope warning. |
| Blocked field | blocked/null field name, L0 readiness, source needed, forbidden claim. |

Prototype traceability requirement:

- every KPI card has a source field reference
- every table row has evidence class and readiness level
- every modelled value says modelled, current-engine, or fixture output
- every scenario price says scenario, currency, and selected-scope
- every blocked field shows why it is blocked and what evidence would change it
- `saleable_harvest_mass_kg` remains null/unresolved unless a later approved
  observed or explicitly reviewed source exists

## 23. Language rules

Allowed language:

- benchmark fixture
- public-evidence-inspired
- scaled
- scenario-augmented
- pre-customer seed-demo context
- modelled current-engine context
- selected operating-cost pressure
- non-benchmark business overlay
- blocked until observed or reviewed
- expert-question candidate
- next data needed

Required caution language:

- not a direct UVI reproduction
- not canon
- not customer validation
- not commercial proof
- not real-world operating proof
- not observed UVI measurement
- not fish-safety proof
- not system-safety proof
- not aeration adequacy
- not solids-removal capacity
- not total operating cost
- not revenue
- not profitability
- no known basil saleable harvest mass

Forbidden or high-risk UI language:

- safe, unsafe, adequate, viable, profitable, investable, validated, proven,
  commercial-ready, field-proven, customer-validated, operator-validated
- total cost, revenue, margin, ROI, payback, break-even, economics result
- known saleable harvest, inferred saleable harvest, expected sales
- direct UVI reproduction, UVI equivalent, UVI validated

## 24. Prototype implementation boundaries

A later prototype implementation pass may proceed only as a separate approved
task. This design does not propose code diffs.

Prototype boundaries:

- read existing benchmark/report artifacts only after explicit approval
- do not modify benchmark JSON unless a later fixture-update pass is approved
- do not modify the seed-demo report unless a later report-update pass is
  approved
- do not modify `data/knowledge/**`, ontology files, evidence maps, model
  tickets, runtime files, `src/**`, `scripts/**`, `tests/**`, `configs/**`,
  `data/simulation/**`, reports, generated artifacts, or Obsidian notes
- do not implement new calculations
- do not add revenue, profitability, safety, total-cost, commercial-operability,
  or saleable-harvest logic
- do not hide caveats behind footnotes or help text

Stop a later prototype if the design needs new values, new calculations, changed
fixture fields, report rewrites, code changes, or protected data changes before
the scope is explicitly approved.

## 25. Dashboard prototype readiness verdict

Verdict: CAUTION.

The design is ready as a review document for expert-reviewed benchmark readiness
before prototype UI. It is not ready for polished dashboard implementation or
commercial dashboard readiness.

Required conditions before prototype implementation:

1. Confirm the prototype is presentation-only and uses existing approved values.
2. Keep evidence-class chips, readiness badges, modelled-versus-observed labels,
   fish-tank scope warnings, business-overlay labels, and blocked-claim panels
   visible by default.
3. Confirm no benchmark JSON, seed-demo report, canonical files, runtime files,
   source files, scripts, tests, configs, reports, generated data, simulation
   files, or Obsidian notes are changed unless separately approved.
4. Run integrity and protected-path checks before and after implementation.
5. Stop if any UI wording implies safety, aeration adequacy, solids-removal
   capacity, total operating cost, revenue, profitability, commercial
   operability, customer validation, real-world operating proof, or saleable
   basil harvest.

## 26. Validation checks for later implementation

A later dashboard/report prototype should be checked for:

- scenario ID displayed exactly
- benchmark framing displayed as public-evidence-inspired, scaled, and
  scenario-augmented
- direct-UVI reproduction warning visible
- Mode A, P1, P1.5, and P2a output groups present
- each displayed value has evidence class and readiness level
- current evidence ceiling shown as L1/L2, not L4/L5
- fish-tank concentration scope visible beside TAN/NH3 values
- modelled-versus-observed labels visible beside TAN/NH3, oxygen demand,
  alkalinity demand, dry-solids potential, and selected subtotal
- business overlays labelled as scenario inputs and non-benchmark business
  overlays
- selected cost-pressure subtotal labelled as not total operating cost
- blocked-claims panel visible above the fold
- expert-question cards visible for module scope, raft area, concentration
  display, pump/blower scaling, backup aeration/power, and basil saleability
- next-data-needed checklist visible
- no inferred `saleable_harvest_mass_kg`
- no safety, adequacy, revenue, profitability, total-cost, commercial
  operability, customer-validation, or real-world operating-proof language
- no hidden footnote-only caveats
- mobile/compact view still shows state, evidence/readiness, scope, modelled
  status, and blocked claims before or with values
- audit view can trace each value to fixture field, report section, evidence
  class, readiness level, and status

## 27. Recommended next action

Recommended next action: review this design with an aquaponics/RAS expert or
technical advisor before any prototype UI implementation.

The review should focus on whether the visible guardrail panels, fish-tank scope
warnings, modelled-versus-observed labels, business-overlay labels, and
expert-question cards are enough to prevent overclaiming while still making the
current MVP understandable.

After review, the smallest later implementation path would be a read-only
prototype surface that displays existing benchmark/report values with visible
evidence and blocked-claim labels. That later pass should be separately scoped
and should stop before any new calculations, data edits, report generation,
canonical promotion, or business/revenue/profitability work.
