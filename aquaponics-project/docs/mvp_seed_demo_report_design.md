# MVP Seed-Demo Report Design

## 1. Purpose

This document designs the future seed-demo report for the current Aquaponics
MVP. It is a strategic/report-design document only.

The report should show how the current Mode A + P1 + P1.5 + P2a technical
spine and the `uvi_like_tilapia_basil_dwc_raft_benchmark_v0` fixture support
pre-customer demo credibility.

This design does not generate the report, create a dashboard, create slides,
create a pitch deck, implement calculations, or promote benchmark assumptions
into canon.

## 2. Relationship to seed-goal reset, data contract, and benchmark fixture

The report design sits at step 4 of the current pathway:

1. unit-economics seed-goal reset
2. unit-economics data contract
3. benchmark scenario dataset
4. seed-demo report
5. later expert/customer validation when accessible

Use `docs/mvp_unit_economics_seed_goal_reset.md` for the seed objective,
`docs/mvp_unit_economics_data_contract.md` for field/readiness discipline, and
`docs/mvp_benchmark_scenario_dataset_design.md` plus
`data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json` for the
current benchmark fixture boundary.

The report must make clear that the benchmark fixture is mostly L1/L2
pre-customer evidence. It is not customer validation, commercial proof,
real-world operating proof, canon, safety proof, revenue proof, profitability
proof, total operating cost, or known basil saleable output.

## 3. Target audience

| audience | primary need | emphasis |
| --- | --- | --- |
| Technical investor/advisor | Understand whether the MVP is disciplined enough for seed review. | Pathway to unit-economics proof, current credibility, next data needed, and blocked claims. |
| Aquaponics/RAS expert | Check model boundaries and whether assumptions are visible. | Unit basis, water-quality scope, aeration/solids boundaries, source gaps, and non-safety language. |
| Future operator/customer reviewer | See what inputs would be needed later. | Required measured inputs, what the tool can calculate, what it cannot infer, and why customer/operator evidence is still needed. |

## 4. Core narrative

The report should follow this narrative:

1. The technical spine is built and passing integrity checks.
2. The seed goal is to evaluate one bounded tilapia + basil DWC/raft unit for
   future commercial unit economics using real, explicitly supplied scenario,
   or source-labeled benchmark data.
3. The UVI-like benchmark fixture demonstrates data structure and source-label
   discipline, not commercial proof.
4. The current MVP can show load, chemistry context, aeration/solids context,
   and selected feed + electricity cost pressure from explicit inputs.
5. The next real milestone is data-backed unit-economics evaluation after
   missing measured, source-backed, reviewed, or operator/customer inputs are
   supplied.

## 5. Recommended report structure

Recommended report order:

1. Front-page summary
2. System overview
3. Four-level MVP output table
4. Benchmark scenario summary
5. Assumption register
6. Source/data readiness panel
7. Current demo values
8. Unit-economics data contract summary
9. What this proves and does not prove
10. Blocked claims and guardrails
11. Next data needed
12. Validation and reproducibility appendix

The report should be concise enough for a first reviewer but structured enough
that every number and null has a visible status label.

## 6. Front-page summary design

The front page should contain:

- report title: `Aquaponics MVP Seed-Demo Report`
- scenario ID: `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`
- MVP spine: Mode A + P1 + P1.5 + P2a
- fixture status: `scenario_input`, `benchmark_assumption`, `not_canon`,
  `not_customer_validated`
- integrity snapshot status and commit hash from the report-generation run
- one-paragraph purpose statement
- one guardrail callout: selected cost pressure is not total operating cost,
  and benchmark fixture output is not commercial proof
- one next-milestone callout: collect or review the missing unit-economics
  inputs needed for real evaluation

The front page must not read like a pitch close. It should frame the report as
evidence discipline and next-data readiness.

## 7. System overview section

The system overview should use a simple bounded-unit flow:

| component | report role | do not claim |
| --- | --- | --- |
| Tilapia tank | Source of direct feed inputs and fish-tank TAN/NH3 context. | Fish safety, stocking adequacy, or harvest performance. |
| Solids filtration | Context for provisional dry-solids potential and future maintenance questions. | Solids-removal capacity or sludge design adequacy. |
| Biofilter/aeration | Context for nitrification oxygen demand and supplied DO context. | Aeration adequacy, oxygen-transfer sufficiency, or system safety. |
| DWC/raft basil bed | Plant production context for later unit-economics inputs. | Known saleable basil mass or revenue. |
| Data/report layer | Separates scenario inputs, benchmark assumptions, derived outputs, source gaps, and blocked fields. | Canonical truth or customer validation. |

Use a diagram only in a later generated report or dashboard pass. This design
does not create visuals.

## 8. Four-level MVP output section

The report should show the four levels as one table:

| level | role | key inputs | outputs to show | required boundary |
| --- | --- | --- | --- | --- |
| Mode A load-only | Converts direct feed and protein inputs into load context. | `feed_kg_day`, `protein_fraction` | TAN-N load, nitrification oxygen demand, alkalinity demand | No biomass-derived feeding or safety claim. |
| P1 TAN-N/NH3 context | Adds fish-tank concentration and chemistry context. | volume, period, scope, pH, temperature, freshwater basis | TAN-N concentration, NH3 fraction, NH3-N, NH3 | No toxicity or fish/system safety verdict. |
| P1.5 aeration/solids context | Adds supplied DO context and provisional dry-solids potential. | measured DO, dry-solids coefficient | DO context, dry-solids potential | No aeration adequacy or solids-removal capacity claim. |
| P2a selected feed + electricity cost pressure | Adds explicit selected cost-pressure inputs. | feed price, electricity tariff, pump/blower power records | feed cost, power kWh/day, power cost, selected subtotal | Not total operating cost, revenue, or profitability. |

## 9. Benchmark scenario section

The benchmark section should summarize:

- scenario ID: `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`
- architecture: tilapia + basil DWC/raft
- source basis: UVI-like architecture anchors, SRAC/FAO/extension/RAS guidance,
  present repo research packs, supplier price metadata gaps, and tariff metadata
  gaps
- scenario assumptions: explicit fixture values used for the current demo path
- readiness levels: mostly `L1_scenario_input` and source-planned
  `L2_benchmark_assumption_with_source`
- uncertainty labels: `not_customer_validated`, `not_canon`,
  `not_commercial_proof`, `not_real_world_operating_proof`,
  `not_total_operating_cost`, `not_profitability`
- source gaps: UVI-like exact mapping, supplier feed price metadata,
  electricity tariff metadata, labor/maintenance basis, and basil
  harvest/saleability basis

The section should say that the fixture is useful because it is explicit and
reproducible, not because it proves customer value or commercial operation.

## 10. Assumption register section

The report should include an assumption register with this column set:

| field | value or status | classification | readiness level | source basis | report treatment | notes |
| --- | --- | --- | --- | --- | --- | --- |

Rows should be grouped as:

- scenario input
- benchmark assumption
- source gap
- blocked until observed
- derived output

Minimum rows should include `feed_kg_day`, `protein_fraction`,
`effective_water_volume_l`, `accumulation_period_day`, `concentration_scope`,
`ph`, `water_temp_c`, `freshwater_assumption`, `measured_do_mg_l`,
`dry_solids_coefficient`, feed price, electricity price, pump/blower power
records, current expected outputs, and blocked/null fields.

Every row should answer whether the value is supplied, derived, source-backed,
missing, or blocked. The register must not collapse source gaps into
assumptions.

## 11. Source/data readiness panel

The source/data readiness panel should define:

| level | meaning | current report use |
| --- | --- | --- |
| `L0_blocked_or_unavailable` | Missing, unresolved, or blocked by guardrail. | Blocked outputs and source gaps. |
| `L1_scenario_input` | Explicit scenario value with no external-source claim. | Current demo fixture inputs and regression anchors. |
| `L2_benchmark_assumption_with_source` | Public, institutional, or supplier-backed benchmark value with metadata. | Source-reviewed benchmark assumptions after review. |
| `L3_measured_internal_or_pilot_data` | Internal measurement or pilot data. | Future internal/pilot update only. |
| `L4_observed_customer_or_operator_data` | Observed customer/operator data. | Not present in the current fixture. |
| `L5_reviewed_or_validated_commercial_data` | Reviewed commercial data suitable for scoped decision support. | Not present in the current fixture. |

The panel should explicitly state: the current fixture is mostly L1 plus
source-planned L2 context; it is not L4 or L5 validation.

## 12. Current demo values section

The report may show these current fixture/regression values:

| output | value | unit | report label |
| --- | --- | --- | --- |
| TAN-N load | 0.02944 | kg/day | derived fixture anchor |
| TAN-N load | 29.44 | g/day | derived fixture anchor |
| Nitrification oxygen demand | 134.5408 | g/day | nitrification sub-load only |
| Alkalinity demand | 210.2016 | g CaCO3/day | demand context only |
| TAN-N concentration | 3.7743589743589743 | mg/L | fish-tank context only |
| Unionized NH3 fraction | 0.006971085009084945 | fraction | chemistry context only |
| NH3-N | 0.026311377265059072 | mg/L | chemistry context only |
| NH3 | 0.031949529536143155 | mg/L | chemistry context only |
| Measured DO context | 5.0 | mg/L | supplied context only |
| Dry-solids potential | 0.25 | kg/day | provisional potential only |
| Scenario feed cost | 45.0 | INR/day | selected cost-pressure only |
| Scenario power kWh | 7.2 | kWh/day | selected power context |
| Scenario power cost | 54.0 | INR/day | selected cost-pressure only |
| Selected cost-pressure subtotal | 99.0 | INR/day | not total operating cost |

The report should not add calculations beyond current approved outputs.

## 13. Unit-economics data contract section

This section should summarize the future data contract without becoming the
contract itself:

- measured fields: future meter records, operator logs, harvest records,
  invoices, buyer/channel records, labor records, and reviewed manual inputs
- scenario inputs: explicit demo or what-if values with status labels
- benchmark assumptions: public/institutional/supplier-backed values with
  metadata
- derived fields: current load, chemistry context, solids potential, and
  selected cost-pressure outputs
- blocked-until-observed fields: basil saleable harvest mass, full revenue
  inputs, total cost scope, profitability outputs, commercial operability, and
  safety/adequacy claims

The section should make clear that unit-economics proof needs complete-enough
quantity, price, currency, date, geography, buyer/channel, labor, cost, and
status inputs before economic outputs can be designed.

## 14. What this proves and does not prove

What the report can credibly show:

- the current four-level technical spine runs and is integrity-checked
- the model separates load, concentration/chemistry context, aeration/solids
  context, and selected cost pressure
- the benchmark fixture is reproducible and source/status-labeled
- missing fields and blocked claims are visible instead of hidden
- the next data needed for unit-economics evaluation is concrete

What the report does not prove:

- customer validation
- commercial proof
- real-world operating proof
- fish safety or system safety
- aeration adequacy or solids-removal capacity
- total operating cost
- revenue, profitability, economic viability, or commercial operability
- known basil saleable harvest mass

## 15. Blocked claims and guardrails

The report must include a guardrail panel that blocks:

- fish safety claim
- system safety claim
- aeration adequacy claim
- solids-removal capacity claim
- total operating cost claim
- revenue claim
- profitability claim
- commercial operability claim
- known basil saleable harvest mass claim
- customer validation claim
- benchmark-as-canon claim
- benchmark-as-commercial-proof claim
- benchmark-as-real-world-operating-proof claim

`saleable_harvest_mass_kg` must remain unresolved/null unless a later approved
pass supplies observed runtime output or explicit reviewed manual input.

## 16. Next data needed

The next-data section should separate public/source work from later
customer/operator work:

| data need | status | why it matters |
| --- | --- | --- |
| Real fish output | later | Required for fish quantity and future revenue inputs. |
| Real basil observed saleable output | blocked until observed/reviewed | Required before basil saleable mass or basil revenue can be non-null. |
| Real labor/maintenance records | later | Required before labor and full cost scope can be evaluated. |
| Real feed/electricity/tariff inputs | next or later | Needed to replace scenario prices with source-backed or measured prices. |
| Real buyer/channel pricing | later | Required before revenue fields can be used. |
| Real customer/operator validation | blocked until access exists | Needed before real-world fit or commercial claims can be tested. |

The report should also list source-review tasks that can be done before
customer access, especially benchmark source review and supplier/tariff
metadata review.

## 17. Recommended visuals and report components

Recommended future components:

- current progress roadmap
- system flow diagram
- four-level output table
- benchmark scenario assumption table
- assumption register
- data readiness panel
- guardrail panel
- next-milestone panel

Visuals should be restrained and evidence-focused. Avoid dashboard-like
optimization visuals, investor pitch graphics, or charts implying commercial
performance before data exists.

## 18. Allowed report language

Allowed phrasing:

- "pre-customer benchmark fixture"
- "source-labeled scenario input"
- "current four-level MVP spine"
- "selected feed and electricity cost pressure"
- "not total operating cost"
- "not customer validated"
- "not canon"
- "not commercial proof"
- "not real-world operating proof"
- "blocked until observed or reviewed"
- "data needed before unit-economics evaluation"

Preferred claim pattern:

`This report shows what the current MVP can calculate from explicit inputs and
which inputs remain missing before unit-economics evaluation.`

## 19. Forbidden report language

Forbidden phrasing or implications:

- "validated by customers"
- "commercially proven"
- "real-world proven"
- "safe for fish"
- "system is safe"
- "aeration is adequate"
- "total operating cost"
- "revenue"
- "profit"
- "profitable"
- "economic viability"
- "commercially operable"
- "known saleable basil harvest"
- "canonical default"
- "UVI benchmark proves this unit"
- "selected operating-cost pressure equals full operating cost"

These words may appear only inside explicit forbidden/blocked sections, not as
positive report claims.

## 20. Future generated report guidance

Recommended future generated report location:

`reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md`

Do not create that report in this design pass.

Future generation guidance:

- read the benchmark fixture as fixture input, not canon
- include the integrity snapshot command and result
- include source/readiness labels beside every value
- preserve current expected outputs as fixture anchors unless an approved pass
  updates them
- keep generated report outputs out of `data/simulation/**` unless a later
  explicitly approved runtime-output pass says otherwise
- keep blocked claims in a visible section
- do not add new calculations in the report generator
- do not generate slides, dashboards, or pitch copy unless a later pass
  explicitly requests that artifact

## 21. Validation checks for later report implementation

A later report-generation or dashboard-design pass should validate:

- `python scripts/check_mvp_integrity.py --quick`
- `python scripts/check_mvp_integrity.py --full` before external-facing use
- `python -m json.tool data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`
- generated report contains the scenario ID and integrity snapshot commit
- generated report labels fixture values as scenario/benchmark, not canon
- generated report keeps selected cost pressure separate from total operating
  cost
- generated report keeps `saleable_harvest_mass_kg` null/blocked unless a later
  observed or reviewed input is explicitly approved
- generated report contains no positive safety, adequacy, revenue,
  profitability, total-cost, commercial-operability, customer-validation, or
  real-world-proof claims
- protected paths stay clean unless the later pass explicitly widens scope

## 22. Recommended next action

Run a docs-only seed-demo report generation spec pass, or a review-first source
completion pass for the benchmark fixture, before creating the actual generated
report. The next pass should decide the exact report artifact boundary and
validation commands without adding calculations or commercial claims.
