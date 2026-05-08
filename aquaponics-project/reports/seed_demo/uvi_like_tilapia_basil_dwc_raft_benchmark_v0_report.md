# Aquaponics MVP Seed-Demo Report

## 1. Title and front-page summary

Report artifact:
`reports/seed_demo/uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md`

Scenario ID:
`uvi_like_tilapia_basil_dwc_raft_benchmark_v0`

Scenario name:
UVI-like tilapia basil DWC raft benchmark v0

MVP spine:
Mode A + P1 + P1.5 + P2a

Integrity snapshot:
`python scripts/check_mvp_integrity.py --quick` passed at commit `9bee0fd`
during this report-generation pass.

First-page status:

- this is a pre-customer benchmark demo report
- the benchmark fixture is mostly `L1_scenario_input` plus source-planned
  `L2_benchmark_assumption_with_source`
- the fixture is not L4 observed customer/operator data
- the fixture is not L5 reviewed or validated commercial data
- the fixture is not customer validated
- the fixture is not canon
- the fixture is not commercial proof
- the fixture is not real-world operating proof

Purpose:
This report shows how the current MVP can turn explicit feed, water-quality,
aeration/solids, and selected cost-pressure inputs into a reproducible
pre-customer benchmark fixture. It also shows what remains missing or blocked
before one bounded tilapia + basil DWC/raft unit can be evaluated with real or
explicitly reviewed unit-economics data.

## 2. Executive summary

The current Aquaponics MVP has a four-level technical spine:

1. Mode A load-only
2. P1 TAN-N/NH3 context
3. P1.5 aeration/solids context
4. P2a selected feed + electricity cost pressure

The benchmark fixture provides source-labeled scenario inputs and current
expected outputs for the demo path. It is useful because it is explicit,
reproducible, and guarded. It is not useful as proof of field performance or
commercial operation.

The main result is a disciplined reportable structure: the current MVP can show
load, chemistry context, aeration/solids context, and selected operating-cost
pressure from explicit inputs while keeping missing data and blocked claims
visible.

## 3. Audience and intended use

| audience | intended use | report emphasis |
| --- | --- | --- |
| Technical investors/advisors | Decide whether the MVP is ready for a guarded seed-demo review. | Current technical spine, integrity status, benchmark fixture discipline, and next data needed. |
| Aquaponics/RAS experts | Review boundaries, units, source status, and missing inputs. | TAN/NH3 scope, DO context, solids boundary, cost-pressure boundary, and source gaps. |
| Future operator/customer reviewers | See what information would be needed from an actual unit later. | Measured inputs, explicit scenario inputs, fields blocked until observed or explicitly reviewed, and questions saved for later access. |

This report is a communication artifact for review. It is not a dashboard,
slide deck, pitch deck, runtime output, canonical knowledge file, or simulation
artifact.

## 4. What this report is and is not

This report is:

- a human-readable seed-demo report
- a pre-customer benchmark fixture summary
- a source-labeled scenario input and output walkthrough
- an assumption and readiness register
- a guardrail document for what remains blocked

This report is not:

- customer validation
- commercial proof
- real-world operating proof
- canon
- safety proof
- a full cost report
- a financial performance report
- a basil saleability result

## 5. System overview

| component | role in this report | boundary |
| --- | --- | --- |
| Tilapia tank | Provides the direct feed basis and fish-tank TAN/NH3 context. | The report does not make fish or system safety claims. |
| Solids filtration | Frames future solids handling and maintenance questions. | Dry-solids potential is not solids-removal capacity. |
| Biofilter/aeration | Provides context for nitrification oxygen demand and supplied DO context. | Device role, kW, and DO context do not establish aeration adequacy. |
| DWC/raft basil bed | Frames the plant-output side of the bounded unit. | Basil saleable output remains blocked until observed or explicitly reviewed. |
| Data/report layer | Separates scenario inputs, benchmark assumptions, derived outputs, source gaps, and blocked fields. | The fixture is not canon and not validation evidence. |

## 6. Current MVP technical spine

| level | role | current input basis | current output basis | boundary |
| --- | --- | --- | --- | --- |
| Mode A load-only | Converts direct feed and protein inputs into load context. | `feed_kg_day`, `protein_fraction` | TAN-N load, nitrification oxygen demand, alkalinity demand | Does not infer feed from biomass. |
| P1 TAN-N/NH3 context | Adds fish-tank concentration and chemistry context. | water volume, accumulation period, scope, pH, temperature, freshwater assumption | TAN-N concentration, unionized NH3 fraction, NH3-N, NH3 | Context only; no safety verdict. |
| P1.5 aeration/solids context | Adds supplied DO context and provisional dry-solids potential. | measured DO context, dry-solids coefficient | DO context, nitrification oxygen demand as sub-load, dry-solids potential | No adequacy or capacity claim. |
| P2a selected feed + electricity cost pressure | Adds explicit selected cost-pressure inputs. | feed price, electricity tariff, pump/blower power records | feed cost, power kWh/day, power cost, selected subtotal | Selected pressure only; not full cost scope. |

## 7. Benchmark scenario summary

| field | value |
| --- | --- |
| Scenario ID | `uvi_like_tilapia_basil_dwc_raft_benchmark_v0` |
| Scenario version | `v0` |
| Architecture | `tilapia_basil_dwc_raft` |
| Fish species | tilapia |
| Plant species | basil |
| Created for | pre-customer Mode A + P1 + P1.5 + P2a seed-demo fixture |
| Customer validated | false |
| Commercial proof | false |
| Canon status | `not_canon` |

Source basis in the fixture:

- UVI-like DWC/raft architecture anchors: `source_gap`
- SRAC/FAO/extension/RAS guidance: `source_gap`
- tilapia feed-regime and stocking research: repo research pack present
- tank volume, exchange, and TAN-to-NH3 research: repo research pack present
- aeration and solids-load research: repo research pack present
- operating economics input research: repo research pack present
- supplier feed-price metadata: `source_gap`
- electricity tariff metadata: `source_gap`

Readiness and uncertainty labels:

- `scenario_input`
- `benchmark_assumption`
- `not_customer_validated`
- `not_canon`
- `not_commercial_proof`
- `not_real_world_operating_proof`
- `not_total_operating_cost`
- `not_profitability`

## 8. Assumption register

### Scenario inputs

| field | value or status | classification | readiness level | source basis | report treatment | notes |
| --- | --- | --- | --- | --- | --- | --- |
| `input_mode` | `mode_a_direct_feed` | scenario input, required | L1 | benchmark fixture | input | Current demo path only. |
| `feed_kg_day` | 1.0 kg/day | scenario input, required | L1 | benchmark fixture | input | Not a feed recommendation. |
| `protein_fraction` | 0.32 | scenario input, required | L1 | benchmark fixture | input | Not a canonical protein value. |
| `feed_class` | `grow_out` | scenario input, optional | L1 | benchmark fixture | context | Context only. |
| `effective_water_volume_l` | 7800 L | scenario input, required | L1 | benchmark fixture | input | Fish-tank concentration context. |
| `accumulation_period_day` | 1 day | scenario input, required | L1 | benchmark fixture | input | Time basis only. |
| `concentration_scope` | `fish_tank` | scenario input, required | L1 | benchmark fixture | input | Prevents whole-system ambiguity. |
| `ph` | 7.0 | scenario input, required | L1 | benchmark fixture | input | Chemistry context only. |
| `water_temp_c` | 28.0 deg C | scenario input, required | L1 | benchmark fixture | input | Chemistry context only. |
| `freshwater_assumption` | true | scenario input, required | L1 | benchmark fixture | input | Explicit salinity boundary. |
| `measured_do_mg_l` | 5.0 mg/L | scenario input, required | L1 | benchmark fixture | context | DO context only. |
| `dry_solids_coefficient` | 0.25 | scenario input, required | L1 | benchmark fixture | input | Fixture coefficient, not canon. |
| `feed_price_per_kg` | 45.0 INR/kg | scenario input, required | L1 | benchmark fixture | selected cost-pressure input | Supplier metadata remains a source gap. |
| `electricity_price_per_kwh` | 7.5 INR/kWh | scenario input, required | L1 | benchmark fixture | selected cost-pressure input | Tariff metadata remains a source gap. |
| `demo_pump` | 0.2 kW, 24 h/day, load fraction 1.0 | scenario input, required | L1 | benchmark fixture | power record | `nameplate_kw` basis. |
| `demo_blower` | 0.1 kW, 24 h/day, load fraction 1.0 | scenario input, required | L1 | benchmark fixture | power record | `nameplate_kw` basis. |

### Benchmark assumptions

| field | value or status | classification | readiness level | source basis | report treatment | notes |
| --- | --- | --- | --- | --- | --- | --- |
| Scenario architecture | `tilapia_basil_dwc_raft` | scenario input, benchmark assumption | L1 | scenario identity | framing | UVI-like in role, not exact UVI replication proof. |
| Fish species | tilapia | scenario input, benchmark assumption | L1 | scenario identity | framing | Species context only. |
| Plant species | basil | scenario input, benchmark assumption | L1 | scenario identity | framing | Output remains unresolved. |
| Research pack references | present for feed, TAN/NH3, aeration/solids, operating economics | benchmark assumption with source planning | L2 | fixture source basis | source context | Used for source planning, not validation. |

### Source gaps

| field | value or status | classification | readiness level | source basis | report treatment | notes |
| --- | --- | --- | --- | --- | --- | --- |
| UVI-like exact mapping | `source_gap` | source gap | L0 | fixture source basis | gap | Needs source review before benchmark values are upgraded. |
| SRAC/FAO/extension/RAS guidance mapping | `source_gap` | source gap | L0 | fixture source basis | gap | Use only as support after review. |
| Supplier feed-price metadata | `source_gap` | source gap | L0 | fixture source basis | gap | Current feed price is fixture input. |
| Electricity tariff metadata | `source_gap` | source gap | L0 | fixture source basis | gap | Current tariff is fixture input. |
| Labor and maintenance basis | `source_gap` | source gap | L0 | fixture source gaps | gap | Not included in current selected pressure. |
| Basil harvest and saleability basis | blocked until observed | blocked until observed | L0 | fixture source gaps | blocked | Needs observed or explicitly reviewed evidence. |

### Blocked-until-observed fields

| field | value or status | classification | readiness level | source basis | report treatment | notes |
| --- | --- | --- | --- | --- | --- | --- |
| `saleable_harvest_mass_kg` | null | blocked until observed | L0 | observed runtime output or explicit reviewed manual input required | blocked | Null means unresolved, not zero. |
| `fish_revenue` | null | blocked until observed | L0 | explicit sale set required | blocked | No sale set is supplied. |
| `basil_revenue` | null | blocked until observed | L0 | explicit saleable quantity and sale set required | blocked | Saleable quantity is absent. |
| `total_operating_cost` | null | blocked until observed | L0 | complete cost scope required | blocked | Selected pressure is not complete cost scope. |
| `profitability` | null | blocked until observed | L0 | complete economic scope required | blocked | No economic result is supplied. |
| `commercial_operability` | null | blocked until observed | L0 | customer/operator or reviewed commercial evidence required | blocked | Benchmark scenarios cannot prove operation. |
| `fish_safety` | null | blocked until observed | L0 | safety design and review required | blocked | Chemistry context is not a verdict. |
| `system_safety` | null | blocked until observed | L0 | safety design and review required | blocked | Benchmark context is not assurance. |
| `aeration_adequacy` | null | blocked until observed | L0 | oxygen-transfer capacity and review required | blocked | Device kW and DO context are not capacity proof. |
| `solids_removal_capacity` | null | blocked until observed | L0 | filter/clarifier performance evidence required | blocked | Dry-solids potential is not removal capacity. |

### Derived outputs

| field | value or status | classification | readiness level | source basis | report treatment | notes |
| --- | --- | --- | --- | --- | --- | --- |
| `tan_n_load_kg_day` | 0.02944 kg/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Fixture anchor only. |
| `tan_n_load_g_day` | 29.44 g/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Fixture anchor only. |
| `oxygen_demand_g_day` | 134.5408 g/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Nitrification sub-load only. |
| `alkalinity_demand_g_caco3_day` | 210.2016 g CaCO3/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Demand context only. |
| `estimated_tan_n_mg_l` | 3.7743589743589743 mg/L | derived, regression anchor | L1 | benchmark fixture expected output | output | Fish-tank context only. |
| `estimated_unionized_nh3_fraction` | 0.006971085009084945 | derived, regression anchor | L1 | benchmark fixture expected output | output | Chemistry context only. |
| `estimated_nh3_n_mg_l` | 0.026311377265059072 mg/L | derived, regression anchor | L1 | benchmark fixture expected output | output | Chemistry context only. |
| `estimated_nh3_mg_l` | 0.031949529536143155 mg/L | derived, regression anchor | L1 | benchmark fixture expected output | output | Chemistry context only. |
| `estimated_dry_solids_potential_kg_day` | 0.25 kg/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Potential only. |
| `scenario_feed_cost_per_day` | 45.0 INR/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Selected cost-pressure only. |
| `scenario_power_kwh_day` | 7.2 kWh/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Power context only. |
| `scenario_power_cost_per_day` | 54.0 INR/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Selected cost-pressure only. |
| `selected_operating_cost_pressure_subtotal` | 99.0 INR/day | derived, regression anchor | L1 | benchmark fixture expected output | output | Not full cost scope. |

## 9. Source/data readiness panel

| readiness level | definition | current fixture use |
| --- | --- | --- |
| `L0_blocked_or_unavailable` | Missing, unresolved, or blocked by guardrail. | Source gaps and blocked/null fields. |
| `L1_scenario_input` | Manually supplied scenario value with no external-source claim. | Current fixture inputs and expected output anchors. |
| `L2_benchmark_assumption_with_source` | Public, institutional, or supplier-backed benchmark value with metadata. | Source-planned research-pack context after review. |
| `L3_measured_internal_or_pilot_data` | Internal measurement or pilot data, not customer/operator validated. | Not present in the current fixture. |
| `L4_observed_customer_or_operator_data` | Observed data from a customer or operator setting. | Not present in the current fixture. |
| `L5_reviewed_or_validated_commercial_data` | Reviewed commercial data suitable for scoped decision support. | Not present in the current fixture. |

The current fixture is mostly L1 with source-planned L2 context. It does not
contain L4 or L5 evidence.

## 10. Four-level output table with current fixture values

| level | output | value | unit | report label |
| --- | --- | --- | --- | --- |
| Mode A | `tan_n_load_kg_day` | 0.02944 | kg/day | derived fixture anchor |
| Mode A | `tan_n_load_g_day` | 29.44 | g/day | derived fixture anchor |
| Mode A | `oxygen_demand_g_day` | 134.5408 | g/day | nitrification sub-load only |
| Mode A | `alkalinity_demand_g_caco3_day` | 210.2016 | g CaCO3/day | demand context only |
| P1 | `estimated_tan_n_mg_l` | 3.7743589743589743 | mg/L | fish-tank context only |
| P1 | `estimated_unionized_nh3_fraction` | 0.006971085009084945 | fraction | chemistry context only |
| P1 | `estimated_nh3_n_mg_l` | 0.026311377265059072 | mg/L | chemistry context only |
| P1 | `estimated_nh3_mg_l` | 0.031949529536143155 | mg/L | chemistry context only |
| P1.5 | `measured_do_mg_l` | 5.0 | mg/L | supplied context only |
| P1.5 | `estimated_dry_solids_potential_kg_day` | 0.25 | kg/day | provisional potential only |
| P2a | `scenario_feed_cost_per_day` | 45.0 | INR/day | selected operating-cost pressure only |
| P2a | `scenario_power_kwh_day` | 7.2 | kWh/day | selected power context |
| P2a | `scenario_power_cost_per_day` | 54.0 | INR/day | selected operating-cost pressure only |
| P2a | `selected_operating_cost_pressure_subtotal` | 99.0 | INR/day | selected operating-cost pressure only |

These values are copied from the benchmark fixture expected outputs. This
report does not calculate new values.

## 11. Unit-economics data contract summary

The future unit-economics data contract separates:

- measured fields: future meter records, operator logs, harvest records, labor
  records, invoices, buyer/channel records, and explicitly reviewed manual
  inputs
- scenario inputs: explicit fixture values such as feed, protein fraction,
  water volume, pH, temperature, DO context, feed price, tariff, and device
  power records
- benchmark assumptions: public, institutional, or supplier-backed values after
  source review
- derived fields: the current load, chemistry context, dry-solids potential,
  and selected operating-cost pressure outputs
- blocked-until-observed fields: saleable basil mass, complete sale sets,
  complete cost scope, economic outputs, operational claims, and safety or
  adequacy claims

The contract requires explicit quantity, price, currency, date, geography,
buyer/channel, labor, cost, and status inputs before later economic evaluation
can be designed.

## 12. What this proves

This report can credibly show:

- the Mode A + P1 + P1.5 + P2a technical spine is present and passes the quick
  integrity snapshot
- the current demo path has reproducible fixture inputs and expected outputs
- the benchmark fixture keeps scenario inputs, benchmark assumptions, source
  gaps, derived outputs, and blocked fields separate
- selected feed and electricity pressure can be reported from supplied inputs
  while preserving the selected-scope label
- the next data needed for later unit-economics evaluation is concrete

## 13. What this does not prove

This report does not prove:

- customer validation
- commercial proof
- real-world operating proof
- fish safety
- system safety
- aeration adequacy
- solids-removal capacity
- total operating cost
- revenue
- profitability
- economic viability
- commercial operability
- known basil saleable harvest mass
- canon/default assumptions

## 14. Blocked claims and guardrails

The benchmark fixture blocks these fields or claims:

- `saleable_harvest_mass_kg`
- `total_operating_cost`
- `fish_revenue`
- `basil_revenue`
- `crop_revenue`
- `profitability`
- `gross_margin`
- `roi`
- `payback`
- `break_even`
- `economic_viability`
- `commercial_operability`
- `fish_safety`
- `system_safety`
- `aeration_adequacy`
- `solids_removal_capacity`

Guardrail interpretation:

- null means unresolved, not zero
- selected operating-cost pressure is not full cost scope
- chemistry context is not a safety verdict
- measured DO context is not aeration adequacy
- dry-solids potential is not solids-removal capacity
- benchmark assumptions are not canon
- benchmark fixture outputs are not customer validation, commercial proof, or
  real-world operating proof

## 15. Next data needed

| next data | current status | why it is needed |
| --- | --- | --- |
| Real fish output | later | Needed for later fish quantity records. |
| Real basil observed saleable output | blocked until observed or explicitly reviewed | Needed before `saleable_harvest_mass_kg` can become non-null. |
| Real labor/maintenance | later | Needed before complete labor and maintenance scope can be evaluated. |
| Real feed/electricity/tariff inputs | next or later | Needed to replace fixture prices with source-backed, measured, or reviewed inputs. |
| Real buyer/channel pricing | later | Needed before any later sale-price use. |
| Real customer/operator validation | blocked until access exists | Needed before real-world fit can be tested. |

## 16. Source gaps and expert/customer questions

Current source gaps:

- exact UVI-like source mapping for this bounded tilapia + basil DWC/raft
  fixture
- supplier feed-price metadata
- electricity tariff metadata
- labor and maintenance basis
- basil harvest and saleability basis

Expert/customer question candidates:

- Which public UVI, SRAC, FAO, or extension benchmark is closest to this
  bounded tilapia + basil DWC/raft fixture?
- Which source should be accepted for local feed price metadata?
- Which source should be accepted for local electricity tariff metadata?
- Should equipment power use nameplate, metered, duty-cycle adjusted, or
  supplier-estimated basis in the first seed-demo report?
- What observed basil handling or buyer review record is sufficient before a
  saleability quantity can become non-null?
- Which labor and maintenance activities must be tracked before any complete
  cost scope is designed?

## 17. Recommended next milestone

Recommended next milestone:
review and fill the source plan for
`uvi_like_tilapia_basil_dwc_raft_benchmark_v0` without changing canon or adding
new calculations.

The next useful artifact is a review-first source completion pass that
identifies which fixture inputs can be upgraded from scenario input to
source-backed benchmark assumption and which fields must remain blocked.

## 18. Appendix: validation and reproducibility notes

Commands used before creating this report:

- `python scripts/check_mvp_integrity.py --quick`
- `python -m json.tool data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`

Integrity snapshot result:

- mode: quick
- commit: `9bee0fd`
- demos: PASS
- expected values: PASS
- forbidden keys: NONE FOUND
- protected paths: CLEAN

Fixture parse result:

- `python -m json.tool data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json`
  passed outside the sandbox after the sandbox Python launcher failed to run
  `json.tool`

Report generation notes:

- all output values in this report were copied from the benchmark fixture
- no new calculations were performed
- no benchmark JSON, docs, source files, scripts, tests, configs, protected
  data, runtime files, simulation outputs, slides, dashboards, or pitch decks
  were created or modified
