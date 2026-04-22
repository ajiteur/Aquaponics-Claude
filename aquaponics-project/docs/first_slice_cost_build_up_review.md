# First Slice Cost Build-Up Review

Status: `draft`

## Purpose

- Review the current working cost build-up for the first slice.
- Judge whether the current example values for `variable_cost_per_saleable_kg` and `fixed_batch_cost` are acceptable for continued working use.
- Keep the result explicitly non-canonical.

## Scope

- Slice is fixed as `basil bulk kg wholesale`.
- Netherlands is the current first working benchmark for this pass only.
- This review covers only:
  - `variable_cost_per_saleable_kg`
  - `fixed_batch_cost`
- This review does not widen into India calculations, canonical business files, or schema redesign.

## Current First Slice

- `basil bulk kg wholesale`

## Current First Working Benchmark

- `netherlands`
- Status: `first_working_research_benchmark_only`

## Why `variable_cost_per_saleable_kg` and `fixed_batch_cost` Are the Two Weakest Assumptions

- `variable_cost_per_saleable_kg` is still a constructed working value in all three cases.
- The research pack gives Netherlands benchmark anchors for price, labour, electricity, packaging stance, and saleability, but it does not provide credible basil-kg conversion math for labour or electricity into per-saleable-kg operating cost.
- `fixed_batch_cost` is even weaker because it is not anchored to a reviewed period-cost scope yet; it currently exists to let the calculator emit a break-even result.
- Compared with price and saleability, these two fields are doing more interpretive work and have less direct source anchoring.

## Cost-Build-Up Review

### Conservative

| Assumption | Current value | Current status | Benchmark evidence that supports it | What is still constructed | What would tighten it |
|---|---:|---|---|---|---|
| `variable_cost_per_saleable_kg` | `6.8` | `working_assumption` | Netherlands benchmark labour `19.0 EUR/hour`, electricity `0.26 EUR/kWh`, packaging default `0.0 EUR/kg`, saleability `0.85`, and price band `7.0 EUR/kg` exist in the research pack. | The `6.8` value is not derived from a reviewed kg-level cost build-up; it is a constructed review-only unit-cost assumption. | One explicit reviewed Netherlands operating case that translates labour, energy, and other operating burden into saleable-kg cost on a stated basis. |
| `fixed_batch_cost` | `500.0` | `weak_assumption` | No direct benchmark evidence yet supports this exact batch fixed-cost value. | Entire value is constructed and held constant only to make break-even output comparable. | A reviewed fixed-cost scope for the example period with inclusion rules and a stated relation to the chosen basil wholesale slice. |

### Base

| Assumption | Current value | Current status | Benchmark evidence that supports it | What is still constructed | What would tighten it |
|---|---:|---|---|---|---|
| `variable_cost_per_saleable_kg` | `5.8` | `working_assumption` | Netherlands benchmark labour `17.5 EUR/hour`, electricity `0.25 EUR/kWh`, packaging default `0.0 EUR/kg`, saleability `0.90`, and price band `8.0 EUR/kg` exist in the research pack. | The `5.8` value is a constructed working number, not a direct conversion from labour or electricity benchmarks. | A reviewed base-case cost build-up using one stated operating assumption set. |
| `fixed_batch_cost` | `500.0` | `weak_assumption` | No direct benchmark evidence yet supports this exact batch fixed-cost value. | Entire value is constructed and held constant only to make break-even output comparable. | A reviewed example-period fixed-cost scope with explicit inclusions and exclusions. |

### Optimistic

| Assumption | Current value | Current status | Benchmark evidence that supports it | What is still constructed | What would tighten it |
|---|---:|---|---|---|---|
| `variable_cost_per_saleable_kg` | `5.0` | `working_assumption` | Netherlands benchmark labour `16.0 EUR/hour`, electricity `0.24 EUR/kWh`, packaging default `0.0 EUR/kg`, saleability `0.95`, and price band `9.0 EUR/kg` exist in the research pack. | The `5.0` value is a constructed working number, not a direct conversion from labour or electricity benchmarks. | A reviewed optimistic-case cost build-up using one stated operating assumption set. |
| `fixed_batch_cost` | `500.0` | `weak_assumption` | No direct benchmark evidence yet supports this exact batch fixed-cost value. | Entire value is constructed and held constant only to make break-even output comparable. | A reviewed example-period fixed-cost scope with explicit inclusions and exclusions. |

## Most Defensible Temporary Structure for This Pass

- The most defensible temporary structure is:
  - one explicit `variable_cost_per_saleable_kg`
  - plus one explicit `fixed_batch_cost`
- This is preferable to a harvested-kg component build-up right now because a component build-up would require unsupported precision.
- The research pack supports benchmark-level wage and electricity ranges, but it does not support a credible basil-kg conversion formula for direct labour or electricity burden in the current first-slice context.
- The correct current move is to keep the structure simple, explicit, and visibly provisional.

## Recommended Revised Working Values

- No numeric revision is recommended in this pass.

Current conclusion:

- conservative `variable_cost_per_saleable_kg = 6.8`
- base `variable_cost_per_saleable_kg = 5.8`
- optimistic `variable_cost_per_saleable_kg = 5.0`
- all cases `fixed_batch_cost = 500.0`

Why no numeric revision now:

- The review does not support tighter values without implying a false cost decomposition.
- The current numbers are acceptable for continued working use if they remain explicitly labeled as constructed example assumptions.

## Which of These Two Assumptions Currently Moves Break-Even Most?

- `variable_cost_per_saleable_kg`
- `fixed_batch_cost` matters linearly, but it is currently constant across all three cases.
- `variable_cost_per_saleable_kg` changes contribution margin directly and therefore moves break-even far more across the current example set.
- This is especially visible in the conservative case, where a very thin margin produces a very large break-even requirement.

## What Still Cannot Be Claimed

- That the current `variable_cost_per_saleable_kg` values are source-derived Netherlands basil cost facts.
- That `500.0` is a reviewed fixed-cost truth for any real period or facility.
- That benchmark labour and electricity rates have been credibly converted into basil-kg cost components.
- That the current example run is sufficient for canon promotion.
- That the Netherlands benchmark is canonical rather than the current first working benchmark only.

## Recommended Next Action After This Tightening Pass

- Keep the current example cost values for continued working use.
- Tighten provenance and explanation rather than forcing new numbers.
- Next, review one explicit Netherlands example cost build-up that can justify either:
  - a better direct `variable_cost_per_saleable_kg`, or
  - a credible harvested-kg component set
- Separately, define one reviewed example-period fixed-cost scope before trying to make break-even output more decision-ready.
