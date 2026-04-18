# Business Layer Contract

## Boundary

This business layer is a canonical knowledge-layer contract for evaluating whether an aquaponics scenario is economically viable, not just biologically plausible.

In this pass:

- `data/knowledge/business/**` is canonical for business assumptions and business-facing translation rules.
- `data/simulation/**` remains derived runtime input, not business truth.
- Simulation outputs are treated as upstream observations to be consumed by the business layer later.
- Current simulation output shapes, including files such as `data/simulation/multi_day_summary.json`, are illustrative examples only and are not treated as a frozen long-term interface.
- No simulation logic, runtime sync logic, migration logic, or consumer integration is defined here.

## Purpose

The contract exists so later code can do four things cleanly:

1. translate biological/system outputs into saleable business quantities,
2. attach canonical pricing, cost, labor, CAPEX, and channel assumptions,
3. compute margins, payback, and scenario comparisons,
4. preserve uncertainty explicitly where business inputs are still missing.

## Versioning note

This pass keeps the current `0.1.0` version format provisionally. No repo-wide version-format convention was visible in the project materials reviewed for this cleanup pass.

## Canonical Business Inputs vs Derived Runtime Inputs

### Canonical business inputs

Canonical business inputs live under `data/knowledge/business/**` and include:

- price assumptions,
- channel behavior assumptions,
- variable cost rates,
- labor standards and labor rates,
- CAPEX assumptions,
- yield-to-revenue translation rules,
- risk penalty rules.

### Derived runtime inputs

Derived runtime inputs come from simulation/runtime outputs and later adapters. They are expected to describe what happened in a simulated scenario, not what the business layer believes to be true about the market or the business.

## Required upstream inputs from simulation

The fields below define the first-pass upstream contract. Exact file names and exact field names may differ in the current runtime output; these names are normative targets for later mapping, not a demand to change simulation now.

### Required now

#### Scenario identity and run framing

- `scenario_id`
- `run_id`
- `scenario_name`
- `time_basis`
  - expected values later: `daily`, `batch`, `multi_day_summary`, `scenario_rollup`
- `period_start_utc`
- `period_end_utc`

#### Plant production outputs

At least one crop-level record per crop present in a scenario:

- `crop_id`
- `crop_system_type`
- `growing_area_m2`
- `planting_count`
- `live_plant_count_end`
- `saleable_harvest_mass_kg`
- `cull_or_unsaleable_mass_kg`
- `harvest_event_count`
- `first_harvest_utc`
- `last_harvest_utc`

#### Fish production outputs

At least one fish-level record per fish cohort or scenario summary:

- `fish_species_id`
- `stocked_count`
- `live_count_end`
- `fish_biomass_kg_end`
- `harvested_fish_biomass_kg`
- `mortality_count`
- `mortality_biomass_kg`
- `feed_input_kg`

#### System operating outputs

- `energy_kwh`
- `water_use_l`
- `supplement_input_records` or equivalent aggregate records where available
- `observed_pH`
- `observed_tan_mg_l`
- `observed_unionized_nh3_mg_l`
- `observed_nitrate_mg_l`

#### Risk/event outputs

- `downtime_event_count`
- `disease_or_pathogen_event_records`
- `quality_risk_event_records`
- `out_of_range_event_records`

### Optional future extensions

These are not required for first integration, but the schemas are designed so they can be added later without redesign.

- `saleable_harvest_count` by sale unit, such as heads, bunches, or fish count
- `grade_mix` or `quality_class_mix`
- `harvested_fish_count`
- `average_saleable_unit_mass`
- `labor_hours_observed`
- `delivery_event_count`
- `channel_id`
- `adjustment_event_count`
- `order_count`
- `packing_material_usage`
- `seed_or_seedling_usage`
- `fingerling_purchase_count`
- `space_utilization_ratio`
- `equipment_runtime_hours`
- `cash-timing fields` such as invoiced vs paid date

## Required units

All business adapters should normalize upstream values into explicit units before using business-layer assumptions.

### Identity and time

- timestamps: ISO 8601 UTC
- durations: `day`, `month`, `year`, `cycle`, or explicit `hour`

### Biomass and counts

- fish biomass: `kg`
- plant harvest biomass: `kg`
- count units where relevant: `plant`, `head`, `bunch`, `fish`

### Area and volume

- growing area: `m2`
- fish water volume if later needed: `m3`

### Water quality and environment

- pH: dimensionless
- TAN: `mg/L`
- unionized NH3: `mg/L`
- nitrate: `mg/L`

### Operating inputs

- feed: `kg`
- energy: `kWh`
- water use upstream normalization target: `L`
- water cost-rate normalization target in canonical business assumptions may be `m3` after adapter conversion
- labor: `labor_hour`

### Money

- all money-bearing fields must include:
  - `currency_code`
  - `currency_date_basis`
  - explicit rate unit such as `currency_per_kg`, `currency_per_head`, `currency_per_m2`, `currency_per_labor_hour`, `currency_per_kWh`, `currency_per_day`, `currency_per_year`

## Output metrics

When upstream inputs or canonical business inputs are missing, outputs should emit `null` plus a missing-input explanation rather than an invented value.

### Batch outputs

Intended to answer: “Did this crop/fish cycle make sense economically?”

- `batch_revenue`
- `batch_variable_cost`
- `batch_direct_labor_cost`
- `batch_contribution_margin`
- `batch_risk_penalty_cost`
- `batch_risk_adjusted_margin`
- `batch_saleable_yield_kg`
- `batch_cull_rate_fraction`

### Daily outputs

Intended to answer: “What did today cost and what value was created or put at risk?”

- `daily_revenue_recognized`
- `daily_operating_cost`
- `daily_direct_labor_cost`
- `daily_risk_penalty_cost`
- `daily_contribution_margin`
- `daily_cash_cost`

### Monthly outputs

Intended to answer: “Is the system trending toward viability?”

- `monthly_revenue`
- `monthly_variable_cost`
- `monthly_direct_labor_cost`
- `monthly_risk_penalty_cost`
- `monthly_contribution_margin`
- `monthly_space_utilization`
- `monthly_channel_mix`

### Annualized outputs

Intended to answer: “If this operating pattern persisted, what would the business look like?”

- `annualized_revenue_run_rate`
- `annualized_variable_cost_run_rate`
- `annualized_direct_labor_cost_run_rate`
- `annualized_contribution_margin_run_rate`
- `annualized_risk_adjusted_margin_run_rate`
- `annualized_capex_recovery_requirement`
- `simple_payback_years`

### Scenario-comparison outputs

Intended to answer: “Which scenario is economically preferable, and why?”

- `scenario_revenue_delta`
- `scenario_margin_delta`
- `scenario_risk_adjusted_margin_delta`
- `scenario_payback_delta`
- `scenario_utilization_delta`
- `scenario_explanation_flags`

## Output cadence distinctions

### Batch

A crop or fish production cycle, or a defined repeated-harvest window.

### Daily

A single simulated day or normalized daily snapshot.

### Monthly

A rollup over calendar or simulated month periods.

### Annualized

A normalized run-rate view derived from shorter simulated periods. This is not the same as a real year of observed operation.

### Scenario comparison

A side-by-side comparison between two or more scenarios using the same accounting assumptions and compatible units.

## Internal decision support vs later user-facing presentation

### Internal decision support outputs

These are for model tuning, operator review, and scenario design:

- risk-adjusted margin
- missing-input flags
- null-propagation diagnostics
- decomposition of revenue vs culls vs mortality vs labor vs channel effects
- sensitivity to price, utilization, and loss assumptions

### Later user-facing outputs

These are acceptable later, but not the priority in this contract:

- simplified profitability scorecards
- payback summaries
- scenario ranking cards
- channel recommendation summaries
- “why this scenario is weaker/stronger” explanations

User-facing presentation should later be derived from the internal metrics above rather than becoming the primary accounting truth.

## Required business-layer connections

### Yield

The business layer must later connect to saleable harvest mass and, where available, saleable harvest counts. Raw biomass alone is not sufficient when products are sold as heads, bunches, or processed fish units.

### Mortality

Fish mortality and repeated-harvest plant losses must later reduce saleable output and may also increase effective cost per surviving unit.

### Harvest timing

Revenue recognition must later depend on harvest timing, because crop timing affects freshness, channel fit, and realized revenue window.

### Operating cost

Energy, feed, water, supplements, packaging, labor, and fulfillment costs must later be attached using canonical business assumptions rather than simulation-side placeholders.

### Utilization

Area, tank volume, or system occupancy utilization must later be made explicit. A biologically stable scenario may still be economically weak if infrastructure is underutilized.

### Risk

Risk must later be represented as explicit business penalties, downgrade effects, shrink, delay cost, recovery labor, or lost sales — not merely as biology warnings.

## Unresolved gaps and assumptions

The following gaps are intentionally left open instead of being guessed:

1. exact current runtime field names and nesting in `data/simulation/**`
2. geography, currency, and currency date basis
3. real market prices by product/channel/unit
4. real labor rates and burden assumptions
5. real CAPEX basis and useful life assumptions
6. saleable-vs-total yield separation in current runtime outputs
7. head-count/bunch-count availability for plant sales units
8. fish processing basis, such as live weight vs whole fish vs fillet yield
9. utilization definition, such as area occupancy, tank occupancy, or calendar throughput
10. channel-specific rejection, shrink, and payment-delay assumptions
11. how detailed risk/event outputs currently are in simulation
12. whether supplements, water, and packaging are already observable in runtime data or must be externalized later

## Deferred rule activation rule

If a rule or record depends on an optional future upstream field or on an unresolved schema choice, it should stay explicitly deferred with a simple marker such as `enabled_by_default: false` or `activation_status: "optional_future"` until the dependency is made canonical.

## Assumption handling rule

If a required business value is missing, downstream business logic should:

- keep the field in schema,
- emit `value: null`,
- emit an assumption flag,
- preserve the scenario as partially evaluable,
- avoid inventing certainty.

## Interface stability note

This document is normative for the business-layer boundary, but not a frozen runtime API.

The later integration phase should add a mapping/adaptor layer from actual runtime outputs into this contract without requiring immediate simulation-side changes.
