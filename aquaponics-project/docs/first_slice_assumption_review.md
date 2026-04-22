# First Slice Assumption Review

Status: `draft`

## Purpose

- Review the current working assumptions behind the first reviewable economics pass for the first slice.
- Separate source-anchored benchmark inputs from constructed working assumptions and missing operational outputs.
- Make clear what is safe for current working use versus what should remain outside canon.

## Scope

- Slice is fixed as `basil bulk kg wholesale`.
- Netherlands is used as the current first working benchmark for this pass only.
- This note reviews the current example working inputs, not canonical business files.
- This note does not widen into India calculations.

## Current First Slice

- `basil bulk kg wholesale`

## Current First Working Benchmark

- `netherlands`
- Status: `first_working_research_benchmark_only`

## Assumption Review Table

| Assumption | Current working value(s) | Source / origin | origin_type | classification | origin_note | Why it is currently reasonable or not | What would tighten it | Safe for current working use |
|---|---|---|---|---|---|---|---|---|
| `price_per_saleable_kg` | conservative `7.0`, base `8.0`, optimistic `9.0` | `scripts/example_first_slice_working_inputs.json`; benchmark anchored to the Netherlands price band in `data/sources/research_reports/markdown/First-slice basil wholesale economics input pack.md` | `research_pack` | `partly_anchored` | The current values match the research-pack Netherlands benchmark exactly, but the underlying wholesaler examples are older and explicitly provisional. | Reasonable for working review because the pack gives a clear Dutch wholesaler-level benchmark and the values are already framed as provisional rather than canonical. | A tighter Dutch first-wholesale price refresh with explicit transaction stage, tax treatment, and date normalization. | `yes`, for current working review only |
| `variable_cost_per_saleable_kg` | conservative `6.8`, base `5.8`, optimistic `5.0` | `scripts/example_first_slice_working_inputs.json` | `calculator_working_assumption` | `working_assumption` | Benchmark labour and electricity rates exist in the research pack, but these saleable-kg cost values are constructed example inputs rather than mechanically derived conversions. | Reasonable only as a review-first placeholder because the calculator needed one explicit saleable-kg cost to produce a first margin output and the repo explicitly avoids unsupported per-kg conversion precision. | One reviewed Netherlands example with explicit saleable-kg cost build-up or explicit harvested-kg components tied to a stated operating case. | `yes`, but only as a flagged working assumption |
| `fixed_batch_cost` | conservative `500.0`, base `500.0`, optimistic `500.0` | `scripts/example_first_slice_working_inputs.json` | `calculator_working_assumption` | `weak_assumption` | This is a constructed review-only constant used to make break-even saleable kg calculable across cases. | Reasonable only in the narrowest sense: it lets the calculator emit a break-even output, but it is the least anchored number in the pack. | A reviewed fixed-cost scope for the example period, with clear inclusion rules and relation to the chosen saleable-kg path. | `yes`, but only as a temporary calculation aid |
| `saleability_rate` | conservative `0.85`, base `0.90`, optimistic `0.95` | `scripts/example_first_slice_working_inputs.json`; benchmark anchored to the Netherlands saleability band in `data/sources/research_reports/markdown/First-slice basil wholesale economics input pack.md` | `research_pack` | `working_assumption` | The current values match the research-pack Netherlands saleability band exactly, but that band is explicitly an operator assumption informed by postharvest science rather than a measured wholesale-path constant. | Reasonable for current working use because the research pack is already explicit that saleability is assumption-driven and non-canonical. | Measured basil shrink/saleability observations for a defined Dutch wholesale path with basil-specific handling conditions. | `yes`, for current working review only |
| `saleable_harvest_mass_kg` | conservative `null`, base `null`, optimistic `null` | `scripts/example_first_slice_working_inputs.json`; current bridge decision and adapter prep docs | `missing_runtime_output` | `missing` | The current repo state explicitly keeps this field missing unless supplied as reviewed manual input. No current runtime harvest rollup exists. | Reasonable to leave null because the repo explicitly forbids deriving it from standing biomass or runtime proxies. | Reviewed manual first-slice input now, then later explicit runtime harvest-event output or adapter-side harvest rollup over real harvest observations. | `yes`, as `null`; not safe to invent |

## What Is Doing Most of the Work in the Current Break-Even Result?

- The break-even result is currently driven most by the gap between `price_per_saleable_kg` and `variable_cost_per_saleable_kg`.
- `fixed_batch_cost` matters linearly, but it is held constant across cases at `500.0`, so the break-even spread is mainly coming from the contribution-margin spread.
- In practical terms, the current example run is being shaped more by the constructed saleable-kg cost assumption than by the benchmark labour and electricity reference rates.

## Which Assumptions Are Most Fragile?

- `fixed_batch_cost`
  - weakest anchor in the current pack
- `variable_cost_per_saleable_kg`
  - necessary for the current example run, but still constructed rather than derived from an explicit operating-cost build-up
- `saleable_harvest_mass_kg`
  - still missing for realized-output interpretation, even though it is correctly left `null`

## Which Single Assumption Changes the Result Most If Moved Up or Down?

- `variable_cost_per_saleable_kg`
- In the current example structure, this is the most sensitive assumption because it sits directly against `price_per_saleable_kg` inside contribution margin.
- This is especially visible in the conservative case, where the margin is only `0.2` and the break-even output becomes very large.

## Recommended Next Tightening Order

1. Tighten `variable_cost_per_saleable_kg` with one explicit reviewed Netherlands cost build-up.
2. Tighten `fixed_batch_cost` with a clearly scoped example-period fixed-cost assumption.
3. Tighten `price_per_saleable_kg` with a refreshed Dutch first-wholesale price check.
4. Keep `saleability_rate` as an operator assumption until a path-specific shrink observation exists.
5. Keep `saleable_harvest_mass_kg` as reviewed manual input or `null` until harvest outputs improve.

## What Should Remain Outside Canon for Now

- the Netherlands first working benchmark itself
- all current example values in `scripts/example_first_slice_working_inputs.json`
- constructed `variable_cost_per_saleable_kg`
- constructed `fixed_batch_cost`
- the current saleability-rate band
- any future manual `saleable_harvest_mass_kg` used only for first-slice review

These are useful for first-slice working review, but they should not be promoted automatically into `data/knowledge/business/**`.
