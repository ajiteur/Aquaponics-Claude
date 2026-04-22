# First Slice Working Input Pack

Status: `draft`

## Purpose

- Define one narrow working calculation pack for the current first slice.
- Keep the calculation inputs explicit, reviewable, and outside canonical business files.
- Preserve the difference between research-benchmark inputs and canon.

## Scope

- Slice is fixed as `basil bulk kg wholesale`.
- This pass uses the Netherlands as the first working benchmark only.
- This pack supports only:
  - contribution margin per saleable kg
  - break-even saleable kg
  - required harvested kg from saleability rate
- This pack does not populate `pricing_models.json`, `cost_models.json`, or `labor_models.json`.

## Chosen Slice

- `basil bulk kg wholesale`

## Why the Netherlands Is Used as the First Working Benchmark for This Pass

- The current research pack treats the Netherlands as the cleanest research benchmark for the first working slice because basil wholesale price examples, greenhouse labour anchors, and non-household electricity benchmarks are better documented there than in India.
- This is a working-benchmark decision for this pass only.
- It does not promote Dutch values into canon.
- India remains relevant later, but it is kept out of the calculation script for now because the first-wholesale price stage is more ambiguous.

## Input Structure

The working JSON input should contain:

- a top-level `metadata` block
- a `cases` object with:
  - `conservative`
  - `base`
  - `optimistic`

Each case should support these fields:

- `price_per_saleable_kg`
- `variable_cost_per_saleable_kg`
- `variable_cost_per_harvested_kg`
- `direct_labor_cost_per_harvested_kg`
- `electricity_cost_per_harvested_kg`
- `packaging_handling_cost_per_harvested_kg`
- `other_variable_cost_per_harvested_kg`
- `saleability_rate`
- `fixed_batch_cost`
- `saleable_harvest_mass_kg`
- `provisional_inputs`
- `provenance`

The calculator accepts either:

- `variable_cost_per_saleable_kg` directly, or
- `variable_cost_per_harvested_kg`, or
- a full explicit set of harvested-kg component costs

## Conservative / Base / Optimistic Working Structure

These are the Netherlands-side working benchmark anchors for this pass.

| Case | price_per_saleable_kg | reference_labor_rate_per_hour | reference_electricity_rate_per_kwh | packaging_handling_cost_per_harvested_kg | saleability_rate |
|---|---:|---:|---:|---:|---:|
| conservative | `7.0 EUR/kg` | `19.0 EUR/hour` | `0.26 EUR/kWh` | `0.0 EUR/kg` | `0.85` |
| base | `8.0 EUR/kg` | `17.5 EUR/hour` | `0.25 EUR/kWh` | `0.0 EUR/kg` | `0.90` |
| optimistic | `9.0 EUR/kg` | `16.0 EUR/hour` | `0.24 EUR/kWh` | `0.0 EUR/kg` | `0.95` |

Important limitation:

- The labour and electricity figures above are benchmark rates, not yet direct unit-cost components.
- This pack does not invent `direct_labor_cost_per_harvested_kg` or `electricity_cost_per_harvested_kg` where the research pack has not established those conversions.

## Required Inputs

### Required now

- `price_per_saleable_kg`
- `saleability_rate`
- one of:
  - `variable_cost_per_saleable_kg`
  - `variable_cost_per_harvested_kg`
  - full explicit harvested-kg cost components

### Optional

- `fixed_batch_cost`
- `saleable_harvest_mass_kg`

## Input Provenance Notes

- `price_per_saleable_kg`
  - market level: Dutch importing wholesaler examples / operator haircut on that level
  - currency: `EUR`
  - tax treatment: not fully normalized in the current research pack
  - date basis: examples reported in a 2024 CBI report, based on March 2020 wholesaler examples
- `reference_labor_rate_per_hour`
  - market level: burdened Dutch greenhouse production labour benchmark
  - currency: `EUR`
  - tax/burden treatment: intended as burdened employer-side rate, not just wage floor
  - date basis: greenhouse CAO wage anchors from 1 July 2025 plus 2026 employer-contribution structure
- `reference_electricity_rate_per_kwh`
  - market level: non-household delivered electricity benchmark
  - currency: `EUR`
  - tax treatment: current research pack treats the Dutch benchmark as delivered total cost including VAT and tax
  - date basis: CBS 2024 H1 through 2025 H2 benchmark table
- `packaging_handling_cost_per_harvested_kg`
  - classification: bulk/non-retail default held at zero for first-slice working use
  - caveat: route-specific handling or packing burden may still need a later toggle
- `saleability_rate`
  - classification: operator assumption informed by postharvest handling science
  - not a canonical biological constant

## Which Inputs Are Provisional

- `price_per_saleable_kg`
  - provisional because the strongest Dutch wholesaler examples are older and need refresh
- `reference_labor_rate_per_hour`
  - provisional as a working benchmark, even though the underlying wage/burden evidence is relatively strong
- `reference_electricity_rate_per_kwh`
  - provisional as a working benchmark, even though the underlying official statistics are strong
- `packaging_handling_cost_per_harvested_kg`
  - provisional bulk-default exclusion, not a universal packaging truth

## Which Inputs Are Still Assumption-Driven

- `saleability_rate`
- any direct `variable_cost_per_saleable_kg`
- any direct `variable_cost_per_harvested_kg`
- any harvested-kg labour or electricity cost components
- `fixed_batch_cost`
- `saleable_harvest_mass_kg`

## Formula Definitions

Use these working definitions in the first-slice calculator:

```text
variable_cost_per_saleable_kg
  = direct input
  or variable_cost_per_harvested_kg / saleability_rate
  or (
      direct_labor_cost_per_harvested_kg
      + electricity_cost_per_harvested_kg
      + packaging_handling_cost_per_harvested_kg
      + other_variable_cost_per_harvested_kg
    ) / saleability_rate

contribution_margin_per_saleable_kg
  = price_per_saleable_kg - variable_cost_per_saleable_kg

break_even_saleable_kg
  = fixed_batch_cost / contribution_margin_per_saleable_kg
  only when fixed_batch_cost is supplied and contribution margin is positive

required_harvested_kg
  = 1 / saleability_rate
```

Interpretation of `required_harvested_kg`:

- harvested kilograms needed to realize one saleable kilogram under the chosen saleability rate

## Output Definitions

- `contribution_margin_per_saleable_kg`
  - price minus variable cost on a saleable-kg basis
- `break_even_saleable_kg`
  - saleable kilograms required to recover the supplied fixed batch cost
- `required_harvested_kg`
  - harvested kilograms needed to deliver one saleable kilogram

## What This Working Pack Does Not Prove Yet

- It does not prove that the Dutch benchmark should become canon.
- It does not prove a correct `saleable_harvest_mass_kg` for the first slice.
- It does not convert labour-rate or electricity-rate benchmarks into unit-cost components by itself.
- It does not prove a route-specific packaging burden.
- It does not validate channel fulfillment, delivery timing, or broader business viability.
- It does not settle India-vs-Netherlands canon or wider geography choice.

## Recommended Next Action After This Pass

- Add one reviewed Netherlands example input set with either:
  - explicit `variable_cost_per_saleable_kg`, or
  - explicit harvested-kg component costs
- keep `saleable_harvest_mass_kg` as reviewed manual input or `null`
- then run the calculator to produce one first reviewable Netherlands-side unit-economics output for the basil wholesale slice

Later comparison note:

- India can be added back as a second benchmark after the Dutch path is reviewable and the price-stage ambiguity is handled more explicitly.
