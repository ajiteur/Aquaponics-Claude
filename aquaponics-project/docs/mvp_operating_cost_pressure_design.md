# MVP Operating Cost Pressure Design

## 1. Purpose

Define a docs-only design plan for an MVP operating-cost pressure layer.

The layer should later calculate selected daily operating-cost pressures only
when explicit scenario or business inputs are supplied. It should not calculate
profitability, gross margin, ROI, payback, fish revenue, basil revenue, crop
revenue, or economic viability.

## 2. Scope

In scope:

- feed-cost pressure
- pump, blower, and aeration electricity-cost pressure
- alkalinity/buffer material cost pressure
- water replacement and optional discharge cost pressure
- filter-maintenance labor cost pressure
- backup-power cost context
- low/base/high/user-supplied sensitivity records
- future report section naming and boundary rules

Out of scope:

- canonical biology, model, business, or ontology edits
- runtime, source, script, or test edits
- implementation details or final code diffs
- revenue calculations
- profitability or viability outputs
- universal cost defaults
- basil saleable harvest mass inference

## 3. Inputs Reviewed

Operating-economics research input:

- `data/sources/research_reports/markdown/Operating Economics Input Research Pack for the Aquaponics MVP.md`

Implemented MVP assets:

- `src/feed_waste_tan_loads.py`
- `src/mvp_tan_nh3_risk.py`
- `src/mvp_aeration_solids_context.py`
- `src/mvp_mode_a_feed_load_report.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `scripts/example_mvp_mode_a_p1_water_quality_inputs.json`
- `scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json`

Supporting docs:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_p1_tan_concentration_nh3_risk_design.md`
- `docs/mvp_p1_5_aeration_solids_design.md`
- `docs/mvp_mode_a_p1_p1_5_customer_demo_walkthrough.md`
- `docs/mvp_strategic_alignment_review_packet_for_pro.md`
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`

## 4. Current MVP Status

The implemented MVP can currently report:

- direct `feed_kg_day`
- direct `protein_fraction`
- `tan_n_load_kg_day`
- `tan_n_load_g_day`
- `oxygen_demand_g_day`
- `alkalinity_demand_g_caco3_day`
- optional fish-tank upper-bound/no-removal `estimated_tan_n_mg_l`
- optional freshwater NH3 chemistry context
- optional aeration and solids context
- optional dry-solids potential with an explicit coefficient
- missing-context labels

The current MVP deliberately does not calculate:

- feed cost
- electricity cost
- buffer cost
- labor cost
- water cost
- revenue
- profitability
- gross margin
- ROI
- payback
- economic viability
- basil `saleable_harvest_mass_kg`

## 5. Operating-Economics Research Summary

The operating-economics research supports a cost-pressure layer as the safest
first economics layer.

Key findings:

- Feed is commonly a dominant cost driver in tilapia production, so feed-cost
  sensitivity is useful early.
- Public feed prices vary materially by geography, protein percentage, package
  size, supplier type, and date. They support scenario examples, not universal
  defaults.
- Electricity cost should use equipment power, runtime, and tariff. Measured kW
  is stronger than nameplate kW.
- Electricity tariffs require geography, date, tariff class, currency, tax
  treatment, and fixed/demand charge context.
- Alkalinity/buffer cost can bridge from the current CaCO3-equivalent
  alkalinity demand, but only when material identity, neutralising value,
  purity, and price are supplied.
- Water cost requires local supply tariff and replacement volume; discharge
  cost requires explicit effluent billing context.
- Maintenance labor should be task-based. UVI/NMSU-style clarifier purge and
  filter cleaning frequencies are useful structural examples, not universal
  labor rules.
- Backup power is operationally important, but the evidence supports requiring
  user-supplied backup-power cost inputs rather than defaulting costs.
- Profit, margin, ROI, payback, and viability remain blocked until explicit
  revenue inputs and fuller cost coverage exist.

## 6. Cost-Pressure Versus Profitability Boundary

The next economics layer should be `operating_cost_pressure`, not
profitability.

Allowed interpretation:

- "Given the cost inputs supplied, these categories create this selected daily
  operating-cost pressure."
- "This subtotal covers only supplied categories."
- "This is a scenario estimate, not market truth and not canon."

Blocked interpretation:

- "The system is profitable."
- "The system is economically viable."
- "Gross margin is known."
- "Revenue covers cost."
- "ROI or payback is known."

Design rule:

- Use `selected_operating_cost_pressure_subtotal` for the subtotal of supplied
  categories.
- Do not use `total_operating_cost` unless every required cost category is
  explicitly supplied and a later design pass approves that wording.

## 7. Operating-Cost Category Design

| Cost category | Required inputs | Required metadata | Formula candidate | Unit basis | Uncertainty notes | Classification |
| --- | --- | --- | --- | --- | --- | --- |
| feed cost | `feed_kg_day`, `feed_price_per_kg` | currency, date captured, geography, supplier type, package size, feed class, protein %, quoted unit basis, source reference | `daily_feed_cost = feed_kg_day * feed_price_per_kg` | kg/day, currency/kg, currency/day | prices vary by protein, supplier, region, and package size | `calculable_with_business_inputs` |
| pump/blower/aeration electricity cost | device records with `device_kw`, `runtime_h_day`, optional `load_fraction`, `electricity_price_per_kwh` | measured vs nameplate basis, device role, tariff class, geography, currency, date, tax/fixed/demand charge status | `kwh_day = sum(device_kw * runtime_h_day * load_fraction)`; `daily_electricity_cost = kwh_day * electricity_price_per_kwh` | kW, h/day, kWh/day, currency/kWh, currency/day | measured kW preferred; nameplate-only values should carry higher uncertainty | `calculable_with_business_inputs` |
| alkalinity/buffer cost | `alkalinity_demand_g_caco3_day`, buffer material record, effective neutralising value, price per kg | material identity, purity, neutralising value basis, package size, currency, date, source | `alkalinity_demand_caco3eq_kg_day = alkalinity_demand_g_caco3_day / 1000`; `required_material_kg_day = alkalinity_demand_caco3eq_kg_day / effective_neutralising_value`; `daily_buffer_cost = required_material_kg_day * price_per_kg` | g CaCO3/day, kg CaCO3-equivalent/day, kg material/day, currency/kg, currency/day | no one-kg-equals-one-kg-CaCO3 assumption without material record | `scenario_input_required` |
| water replacement / discharge cost | `replacement_m3_day`, `water_price_per_m3`, optional `discharge_m3_day`, optional `effluent_price_per_m3` | tariff provider, tariff class, geography, currency, date, metering basis, discharge billing basis | `daily_water_cost = replacement_m3_day * water_price_per_m3`; optional supply plus effluent formula | m3/day, currency/m3, currency/day | water and discharge costs are local and often billing-structure specific | `business_input_required` |
| filter-maintenance labor cost | maintenance task records, task hours, event frequency, burdened labor rate | task type, component, evidence/source basis, frequency basis, labor-rate basis, currency/date, whether owner labor is costed | `task_cost = task_hours_per_event * events_per_period * burdened_labor_rate`; daily normalize by period days when needed | hours/event, events/period, currency/hour, currency/period or day | source supports task structure, not universal task time or labor rate | `scenario_input_required` |
| backup-power cost context | backup technology, protected load list, runtime target, fuel or recharge price, test schedule, service cost | technology type, capacity/rating, fuel/recharge basis, service interval, reliability/alarm basis, currency/date | first pass should echo context and optionally calculate supplied test-run/fuel cost only when explicit | equipment-specific; currency/day or currency/period only with period basis | evidence supports need for backup power, not a universal backup cost | `customer_validation_required` |

## 8. Required Input Records And Metadata

Feed price record:

- `feed_price_per_kg`
- `currency_code`
- `currency_date_basis`
- `geography`
- `supplier_type`
- `supplier_or_quote_reference`
- `package_size_kg`
- `feed_class`
- `crude_protein_fraction`
- `quoted_unit_basis`
- `source_type`: quote, invoice, supplier listing, extension budget, or demo
  assumption
- `confidence`: high, medium, low, or customer supplied

Electricity tariff record:

- `electricity_price_per_kwh`
- `currency_code`
- `currency_date_basis`
- `geography`
- `tariff_class`
- `tax_inclusion_basis`
- `fixed_charge_basis`
- `demand_charge_basis`
- `source_type`
- `customer_tariff_reference`

Equipment power/runtime record:

- `device_id`
- `device_name`
- `device_role`
- `device_type`: pump, blower, aerator, controller, oxygenation, backup, or
  other
- `device_kw`
- `power_basis`: measured, nameplate, converted horsepower, or estimate
- `runtime_h_day`
- `load_fraction`
- `duty_cycle_basis`
- `backup_only`
- `protected_load`

Buffer material record:

- `buffer_material_name`
- `buffer_material_class`
- `purity_fraction`
- `effective_neutralising_value`
- `neutralising_value_basis`
- `price_per_kg`
- `currency_code`
- `currency_date_basis`
- `package_size_kg`
- `supplier_or_source_reference`

Water tariff record:

- `replacement_m3_day`
- `water_price_per_m3`
- `currency_code`
- `currency_date_basis`
- `geography`
- `metering_basis`
- optional `discharge_m3_day`
- optional `effluent_price_per_m3`
- optional `effluent_billing_basis`

Maintenance task/labor record:

- `task_id`
- `task_name`
- `component`
- `task_category`
- `task_hours_per_event`
- `events_per_period`
- `period_day_count`
- `burdened_labor_rate`
- `currency_code`
- `currency_date_basis`
- `frequency_basis`
- `labor_source`: customer supplied, advisor estimate, literature pattern, or
  demo assumption

Backup power record:

- `backup_technology_type`
- `protected_load_list`
- `backup_runtime_target_h`
- `fuel_consumption_basis` or `battery_capacity_basis`
- `fuel_or_recharge_price`
- `routine_test_run_schedule`
- `service_or_maintenance_cost`
- `service_period_day_count`
- `start_reliability_or_alarm_basis`
- `currency_code`
- `currency_date_basis`

## 9. Formula Candidates And Unit Basis

Formula candidates for later implementation:

| Formula | Required inputs | Output | Unit basis | Status |
| --- | --- | --- | --- | --- |
| `daily_feed_cost = feed_kg_day * feed_price_per_kg` | direct feed and explicit feed price | `daily_feed_cost_pressure` | currency/day | ready for P2a with business input |
| `kwh_day = sum(device_kw * runtime_h_day * load_fraction)` | explicit per-device power and runtime | `electricity_kwh_day` | kWh/day | ready for P2a with scenario input |
| `daily_electricity_cost = electricity_kwh_day * electricity_price_per_kwh` | kWh/day and tariff | `daily_electricity_cost_pressure` | currency/day | ready for P2a with business input |
| `alkalinity_demand_caco3eq_kg_day = alkalinity_demand_g_caco3_day / 1000` | existing alkalinity demand | intermediate | kg CaCO3-equivalent/day | ready as unit conversion |
| `required_material_kg_day = alkalinity_demand_caco3eq_kg_day / effective_neutralising_value` | buffer material record | intermediate | kg material/day | needs material basis |
| `daily_buffer_cost = required_material_kg_day * price_per_kg` | material requirement and price | `daily_buffer_cost_pressure` | currency/day | P2c candidate |
| `daily_water_cost = replacement_m3_day * water_price_per_m3` | replacement volume and tariff | `daily_water_cost_pressure` | currency/day | P2c candidate |
| `daily_water_and_effluent_cost = replacement_m3_day * supply_tariff + discharge_m3_day * effluent_tariff` | supply and discharge records | `daily_water_and_effluent_cost_pressure` | currency/day | later P2c with effluent basis |
| `task_cost_per_period = task_hours_per_event * events_per_period * burdened_labor_rate` | task and labor record | `task_cost_per_period` | currency/period | P2c candidate |
| `daily_task_cost_pressure = task_cost_per_period / period_day_count` | task period result | `daily_maintenance_labor_cost_pressure` | currency/day | P2c candidate |

All formulas should preserve currency and date metadata. Do not mix currencies
inside any subtotal unless an explicit exchange-rate record exists.

## 10. Uncertainty And Evidence-Quality Handling

Measured kW versus nameplate kW:

- Prefer measured kW.
- Allow nameplate kW only with `power_basis = nameplate` and an uncertainty
  label.
- Do not treat horsepower conversion as measured operating power.

Current quote versus historical benchmark:

- Current supplier quote or invoice can support a scenario base case.
- Historical extension-budget values can support schema and sensitivity
  scaffolding only.
- Label historical values as not current market truth.

Supplier price versus institutional budget:

- Supplier prices are useful for scenario costing when product metadata is
  preserved.
- Institutional budgets are useful for cost-category structure.
- Do not promote either to canon without a later business-input review.

Local tariff versus regional/national average:

- Use actual customer tariff when available.
- Use regional or national examples only as demo assumptions.
- Require tariff class and date for every tariff used in a report.

Customer-supplied labor time versus literature maintenance frequency:

- Customer-supplied task time is stronger for a specific scenario.
- Literature maintenance frequency can seed a task library pattern.
- Do not create universal labor hours or labor rates.

Currency handling:

- Every money-bearing input must include `currency_code`.
- Every price must include `currency_date_basis`.
- Cross-currency subtotals are blocked unless an exchange-rate basis is
  explicitly supplied.

## 11. Classification Table

| Item | Classification | Notes |
| --- | --- | --- |
| daily feed cost with explicit feed price | `calculable_with_business_inputs` | safest first cost-pressure output |
| feed price record | `business_input_required` | must carry currency, date, geography, feed class, protein, package, source |
| public feed-price examples | `scenario_input_required` | demo/sensitivity examples only, not canon |
| universal feed-price default | `blocked` | would create fake precision |
| per-device kWh/day from explicit power/runtime | `calculable_with_business_inputs` | use measured kW when possible |
| electricity tariff record | `business_input_required` | tariff class, geography, date, fixed/demand charges required |
| Dutch/EU electricity examples | `scenario_input_required` | reference-grade scenario examples, not universal defaults |
| universal electricity tariff | `blocked` | geography and tariff class vary too much |
| buffer material cost | `scenario_input_required` | requires chosen material and neutralising value |
| buffer material identity/purity/price | `business_input_required` | no generic one-to-one CaCO3 substitution |
| universal buffer cost | `blocked` | material chemistry and price are scenario-specific |
| water supply cost | `business_input_required` | local tariff and replacement volume required |
| discharge cost | `customer_validation_required` | include only when discharge billing applies |
| maintenance task cost | `scenario_input_required` | task frequency and hours must be explicit |
| labor rate | `business_input_required` | no universal labor-rate default |
| backup-power cost | `customer_validation_required` | technology and cost packaging are customer-specific |
| feed-cost sensitivity | `calculable_with_business_inputs` | low/base/high records can be useful before profitability |
| gross margin, ROI, payback, viability | `blocked` | requires revenue, complete cost coverage, and later approval |

## 12. Demo Assumptions Versus Scenario Inputs

Can be used as demo assumptions without becoming canon:

- Dutch/EU non-household electricity reference values when labelled with
  source, geography, tariff class, date, and demo status.
- Historical US extension-budget prices when labelled as historical planning
  benchmarks.
- Seller-side India or EU/UK feed-price examples when package, protein,
  supplier type, date, geography, and source are preserved.
- UVI/NMSU-style maintenance frequencies as task-library structure, not fixed
  labor hours.

Must remain user-supplied scenario or business inputs:

- actual feed price
- actual electricity tariff
- measured power draw
- actual runtime or duty cycle
- actual labor rate
- actual water tariff
- actual buffer material, purity, neutralising value, and price
- actual maintenance time
- actual backup-power fuel, recharge, service, or test-run cost

Blocked until explicit revenue inputs exist:

- fish revenue
- basil revenue
- crop revenue
- total revenue
- gross margin
- contribution margin
- ROI
- payback
- break-even
- profitability
- economic viability

## 13. Sensitivity Approach

Sensitivity records should be explicit inputs, not generated from hidden
defaults.

Recommended shape:

```text
sensitivity_cases:
  low:
    value: <number>
    unit: <rate unit>
    currency_code: <code>
    source_type: <source type>
    source_reference: <reference>
    metadata: <case-specific metadata>
  base:
    value: <number>
    unit: <rate unit>
    currency_code: <code>
    source_type: <source type>
    source_reference: <reference>
    metadata: <case-specific metadata>
  high:
    value: <number>
    unit: <rate unit>
    currency_code: <code>
    source_type: <source type>
    source_reference: <reference>
    metadata: <case-specific metadata>
  user_supplied:
    value: <number>
    unit: <rate unit>
    currency_code: <code>
    source_type: customer_supplied
    source_reference: <quote, invoice, tariff, or advisor note>
    metadata: <case-specific metadata>
```

Sensitivity labels:

- `scenario_estimate`
- `not_market_truth`
- `not_canon`
- `not_profitability`
- `partial_cost_pressure_only`

Feed and electricity are the best first sensitivity categories because they are
decision-useful and easy to parameterize from explicit inputs.

## 14. Proposed Future Report Sections

Future report section names:

- `operating_cost_pressure`
- `cost_inputs`
- `cost_basis`
- `cost_status_labels`
- `cost_boundary_notes`

Candidate `operating_cost_pressure` shape:

```text
operating_cost_pressure:
  currency_code: <code or null>
  time_basis: daily
  supplied_categories:
    - feed
    - electricity
  selected_operating_cost_pressure_subtotal: <number or null>
  category_costs:
    feed:
      daily_feed_cost_pressure: <number or null>
      status: calculated | missing_input | blocked
    electricity:
      electricity_kwh_day: <number or null>
      daily_electricity_cost_pressure: <number or null>
      status: calculated | missing_input | blocked
    buffer:
      daily_buffer_cost_pressure: <number or null>
      status: calculated | missing_input | blocked
    water:
      daily_water_cost_pressure: <number or null>
      status: calculated | missing_input | blocked
    maintenance_labor:
      daily_maintenance_labor_cost_pressure: <number or null>
      status: calculated | missing_input | blocked
    backup_power:
      daily_backup_power_cost_pressure: <number or null>
      status: context_only | calculated | missing_input | blocked
```

`cost_inputs` should echo the explicit records used. `cost_basis` should state
formula and unit basis. `cost_status_labels` should name missing categories and
blocked claims. `cost_boundary_notes` should explain that this is selected
operating-cost pressure only.

## 15. Output Naming Rules

Use:

- `daily_feed_cost_pressure`
- `electricity_kwh_day`
- `daily_electricity_cost_pressure`
- `daily_buffer_cost_pressure`
- `daily_water_cost_pressure`
- `daily_water_and_effluent_cost_pressure`
- `daily_maintenance_labor_cost_pressure`
- `daily_backup_power_cost_pressure`
- `selected_operating_cost_pressure_subtotal`

Do not use in the first implementation:

- `total_operating_cost`
- `profit`
- `profitability`
- `gross_margin`
- `contribution_margin`
- `ROI`
- `payback`
- `economic_viability`

Only consider `total_operating_cost` later if all required operating-cost
categories are explicitly supplied, currency/date bases are compatible, and a
later design pass approves the wording.

## 16. Blocked Economic Claims

Blocked claims:

- fish revenue is known
- basil revenue is known
- crop revenue is known
- `saleable_harvest_mass_kg` is known
- profitability is known
- gross margin is known
- contribution margin is known
- ROI is known
- payback is known
- break-even is known
- economic viability is known
- all operating costs are known
- a scenario is bankable or fundable from these cost-pressure outputs alone

Reason:

- Revenue inputs are absent.
- Basil saleable output remains unresolved unless observed or explicitly
  reviewed.
- Cost categories are partial unless every required category has explicit
  inputs.
- Scenario/demo assumptions are not canon.

## 17. Recommended Smallest Implementation Surface

Smallest future implementation surface:

- Add an isolated helper first, for example
  `src/mvp_operating_cost_pressure.py`.
- Add targeted helper tests, for example
  `tests/test_mvp_operating_cost_pressure.py`.
- Start with feed and electricity only.
- Accept explicit input records and return a plain dict with:
  - `operating_cost_pressure`
  - `cost_inputs`
  - `cost_basis`
  - `cost_status_labels`
  - `cost_boundary_notes`
- Add one optional example input later only after helper behavior is validated.
- Integrate into `src/mvp_mode_a_feed_load_report.py` later, not in the first
  helper pass.
- Do not integrate into `src/simulate_day.py`.
- Do not modify `data/knowledge/**`, `data/simulation/**`, or canonical
  business files in the first implementation pass.

## 18. Recommended Phased Implementation Path

P2a: feed cost plus electricity cost helper

- Implement isolated helper only.
- Inputs:
  - `feed_kg_day`
  - feed price record
  - equipment power/runtime records
  - electricity tariff record
- Outputs:
  - `daily_feed_cost_pressure`
  - `electricity_kwh_day`
  - `daily_electricity_cost_pressure`
  - `selected_operating_cost_pressure_subtotal`
  - status and boundary labels
- Keep all revenue and profitability blocked.

P2b: optional report integration

- Extend the Mode A/P1/P1.5 report only after P2a tests pass.
- Keep the cost section optional.
- Add cost outputs only when explicit cost inputs are supplied.
- Keep existing water-quality and aeration/solids behavior unchanged.

P2c: buffer, water, and maintenance helper extensions

- Add buffer material costing from CaCO3-equivalent alkalinity demand only when
  material and neutralising value records exist.
- Add water replacement and optional discharge costs only with tariff records.
- Add task-based maintenance labor cost only with task hours, event frequency,
  period, and labor-rate records.
- Keep backup power as context-only unless cost inputs are explicit.

## 19. Validation Plan For Later Implementation

Later implementation validation should check:

- no cost output appears without explicit price/tariff/labor/material inputs
- `daily_feed_cost_pressure` uses only supplied `feed_kg_day` and
  `feed_price_per_kg`
- electricity kWh uses explicit per-device power, runtime, and load fraction
- measured kW and nameplate kW are labelled differently
- currency code and currency date basis are present for every money-bearing
  input
- cross-currency subtotals are blocked without exchange-rate basis
- `selected_operating_cost_pressure_subtotal` includes only supplied,
  compatible categories
- `total_operating_cost` does not appear in the first implementation
- no revenue, profit, margin, ROI, payback, or viability fields appear
- no basil `saleable_harvest_mass_kg` is inferred or populated
- existing Mode A, P1, and P1.5 tests still pass
- `src/simulate_day.py` remains untouched
- protected-path git checks show no unintended edits

Suggested later command checks:

- Python compile check for modified Python files
- targeted operating-cost helper unit tests
- existing Mode A/P1/P1.5 unit tests
- direct demo/report check if report integration is included
- `git --no-pager diff --name-only -- data/knowledge data/simulation docs`
- `git --no-pager diff --name-only -- src/simulate_day.py`
- `git status --short`

## 20. What Remains Out Of Scope

Out of scope for this design:

- implementation
- canonical business input promotion
- revenue
- profitability
- gross margin
- contribution margin
- ROI
- payback
- break-even
- economic viability
- fish revenue
- basil revenue
- crop revenue
- universal feed-price defaults
- universal electricity-price defaults
- universal labor-rate defaults
- universal buffer-cost defaults
- runtime or simulation integration
- generated runtime artifacts
- saleable basil harvest mass inference

## 21. Blockers

No blockers for this docs-only design pass.

Potential blockers for later implementation:

- final helper field names
- report integration shape for optional cost sections
- currency compatibility policy
- whether first helper supports sensitivity cases or only a single base case
- how to represent fixed and demand charges
- how to represent nameplate-power uncertainty
- whether buffer costing waits until a reviewed neutralising-value record shape
  is approved
- whether backup-power cost remains context-only in P2a

Blocked until explicit revenue inputs exist:

- profit
- gross margin
- ROI
- payback
- fish revenue
- basil revenue
- crop revenue
- viability claims

## 22. Recommended Next Action

Keep this document as the operating-cost pressure design artifact.

Recommended next repo-side pass:

- implement P2a as an isolated helper for feed cost and electricity cost
  pressure only, or
- run a short field-naming review if cost input record names need to be settled
  first.

Do not modify canonical business files, runtime files, scripts, or simulation
flow for the first implementation pass. Do not calculate profitability or
revenue. Keep basil `saleable_harvest_mass_kg` unresolved unless observed or
explicitly reviewed.
