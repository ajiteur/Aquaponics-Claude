# First Slice Basil Harvest Saleability Canon Apply Surface

Status: `draft`

## Purpose

- Identify the smallest safe future canon apply surface for first-slice basil harvest-readiness and saleability work.
- Keep this as a review-first plan only.
- Separate evidence-backed concepts from runtime-output design, operator assumptions, and blocked items.
- Avoid proposing canonical diffs, schema shapes, runtime fields, or vocabulary designs in this pass.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- This pass reviews possible future canon touchpoints only.
- This pass does not modify `data/knowledge/**`, `data/simulation/**`, `src/**`, or `scripts/**`.
- `saleable_harvest_mass_kg` remains unresolved.
- `crop_system_type` remains context-only.
- Aroma remains manual-review only.
- Numeric harvest-height, leaf-count, stem-length, aroma-score, and buyer-tolerance thresholds remain blocked.

## Inputs Reviewed

Primary inputs:

- `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`
- `docs/first_slice_basil_harvest_saleability_promotion_candidate_map.md`

Supporting input:

- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`

Canonical files inspected for possible future touchpoints only:

- `data/knowledge/species/plants/basil.json`
- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/labor_models.json`
- `data/knowledge/models/plant_system_models.json`

Note:

- The active business canonical files are under `data/knowledge/business/**`; there is no inspected `data/knowledge/cost_models.json` or `data/knowledge/labor_models.json` at the repo root.

## Current Safe Promotion Candidates

Safest by evidence strength:

- young vegetative, leafy, non-woody, non-flowering harvest-readiness concept
- general marketability minimums for soundness, cleanliness, pest freedom, abnormal moisture, foreign smell/taste, and transportability
- freshness, turgidity, visible defect, chilling injury, and food-safety exclusion concepts as manual-review saleability screens
- product-form distinction between bulk-wholesale cut basil and RTU/RTE, live-root, potted, or bunch-specific forms

Safest by current repo fit:

- `data/knowledge/species/plants/basil.json` is the only existing canonical file with a plausible species-specific touchpoint.
- `data/knowledge/business/yield_to_revenue_rules.json` is a touchpoint for the business requirement `saleable_harvest_mass_kg`, but it is not the right place to define biology or manual saleability criteria.
- `data/knowledge/business/cost_models.json` and `data/knowledge/business/labor_models.json` have deferred basil packaging and harvest/pack placeholders, but the saleability evidence does not resolve their rates, drivers, or labor standards.
- `data/knowledge/models/plant_system_models.json` is about system architecture behavior, not basil saleability review.

## Recommended Smallest Future Canon Apply Surface

Recommendation for the next pass:

- No canon apply pass yet.

Reason:

- The strongest candidate concepts are real and evidence-backed, but the current canonical files do not have a clean existing vocabulary or structured location for harvest-readiness basis, saleability basis, product-form scope, or quality exclusion reasons.
- A notes-only edit to `data/knowledge/species/plants/basil.json` would be technically small, but it would hide manual saleability and product-form semantics inside a species profile instead of establishing the right canonical location.
- Editing `data/knowledge/business/yield_to_revenue_rules.json` would risk confusing a revenue input requirement with the biological, QA, and product-form basis for that input.

Smallest safe future apply surface after one more non-canon step:

- possible new canonical vocabulary location later, without designing it in this pass
- or a deliberately narrow `data/knowledge/species/plants/basil.json` apply only if the later scope is limited to species-specific qualitative harvest-readiness notes and explicitly excludes saleability vocabulary, product-form vocabulary, and runtime-output fields

## Candidate Canonical Touchpoints

| canonical touchpoint | possible future role | first-pass recommendation | blocker |
|---|---|---|---|
| `data/knowledge/species/plants/basil.json` | Species-specific qualitative harvest-readiness concept; possible chilling-to-marketability context. | Possible later touchpoint, but not first until location semantics are chosen. | No existing structured harvest-readiness or saleability section; notes-only edit may blur canon boundaries. |
| `data/knowledge/business/yield_to_revenue_rules.json` | Existing `rule_basil_bulk_kg` requires `saleable_harvest_mass_kg`. | Do not touch in the first canon apply pass. | Saleability criteria should not be embedded in a revenue translation rule; `saleable_harvest_mass_kg` remains unresolved. |
| `data/knowledge/business/cost_models.json` | Deferred basil packaging cost basis references saleable count or mass. | No change needed. | Evidence does not resolve packaging basis, rates, or cost drivers. |
| `data/knowledge/business/labor_models.json` | Deferred basil harvest/pack labor basis references saleable count or mass. | No change needed. | Evidence does not resolve labor standards, labor rates, or driver basis. |
| `data/knowledge/models/plant_system_models.json` | Architecture context and system behavior. | Do not touch in the first canon apply pass. | Basil saleability criteria are not architecture behavior rules; `crop_system_type` must remain context-only. |
| possible new canonical vocabulary location later | Harvest-readiness basis, saleability basis, product-form scope, and quality exclusion reason vocabulary. | Best likely future target, but not designed here. | Requires explicit vocabulary/schema decision before any apply pass. |
| no canon file yet | Preserve current review-only posture. | Recommended now. | Needed until the vocabulary/location decision is made. |

## What Should Remain Docs-Only

- The current promotion map and spec classifications.
- Regrowth-reserve logic for repeated-cut basil until repeated-cut operations context is explicitly represented.
- Slight post-dispatch freshness or turgidity nuance until buyer or receiving-language evidence supports reusable treatment.
- Aroma acceptability as manual-review guidance only.
- Storage and handling bands as operator/model-context guidance, not buyer acceptance rules.
- Buyer tolerance discussion for minor yellowing, wilt, stem breakage, leaf-size mix, or stem-to-leaf ratio.

## What Is Runtime-Output Design Only

- Separating gross harvested mass, observed accepted saleable mass, observed rejected mass, and modeled saleable mass.
- Keeping modeled saleable mass distinct from observed saleable mass.
- Any future field for saleability basis, harvest-readiness basis, quality exclusion reasons, or acceptance confidence.
- Any adapter or runtime path that supplies `saleable_harvest_mass_kg`.
- Any rollup from explicit harvest observations.

These are not canon apply targets in the first pass.

## What Remains Blocked

- `saleable_harvest_mass_kg` remains blocked until observed runtime harvest output or explicit reviewed human approval exists.
- Canonical saleability or rejection vocabulary remains blocked until a canonical location and shape are chosen.
- Product-form vocabulary remains blocked until a location is chosen and the scope is separated from `crop_system_type`.
- Numeric harvest-stage thresholds remain blocked because the evidence is context-dependent.
- Buyer tolerance thresholds remain blocked until high-trust buyer, receiver, or audited sales evidence exists.
- Aroma scoring remains blocked until a practical manual QA method exists; deterministic runtime aroma scoring remains blocked.
- Saleability penalties or modeled marketable-share fractions remain blocked until stronger evidence and runtime/model design exist.

## Whether Runtime-Output Design Should Precede Canon Changes

- Runtime-output design should precede any canon change that tries to define or consume saleable mass fields.
- Runtime-output design should precede any attempt to distinguish observed saleable mass from modeled saleable mass in canonical business logic.
- Runtime-output design does not need to precede a purely qualitative harvest-readiness canon note, but that notes-only apply is not recommended as the next step because it would not solve the missing vocabulary/location problem.
- The next required step before canon is a non-canon vocabulary/location decision, not a runtime implementation.

## Out-of-Scope Items for First Canon Apply Pass

- Any change to `data/knowledge/**` in this pass.
- Any proposed canonical diff.
- Any new runtime field or schema field.
- Any new canonical schema or vocabulary design.
- Any edit to `data/simulation/**`, `src/**`, or `scripts/**`.
- Any inference of `saleable_harvest_mass_kg`.
- Any use of `crop_system_type` as a product-form, pricing, or saleability selector.
- Any numeric harvest-height, leaf-count, stem-length, aroma-score, or buyer-tolerance threshold.
- Any conversion of runtime-output design ideas into biology, model, or business canon.

## Suggested Validation for a Later Apply Pass

For a later approved canon apply pass, run only checks relevant to the touched files:

- inspect the exact diff for the touched `data/knowledge/**` file or files
- confirm no `data/simulation/**`, `src/**`, or `scripts/**` files changed unless separately approved
- parse any edited JSON canonical files with a JSON validator
- search the diff for blocked terms or concepts such as numeric height thresholds, leaf-count thresholds, stem-length thresholds, aroma scores, buyer tolerance percentages, and inferred `saleable_harvest_mass_kg`
- confirm `saleable_harvest_mass_kg` remains unresolved unless the later apply scope explicitly includes observed runtime harvest output or reviewed human approval
- confirm `crop_system_type` remains context-only
- confirm source paths and durable source-family labels are preserved without copied chat citation tokens

## Recommended Next Action

- Do not run a canon apply pass yet.
- Create one non-canon decision note or update the promotion map later to choose the canonical location for:
  - harvest-readiness basis
  - saleability basis
  - product-form scope
  - quality exclusion reasons
- After that location decision, run a tightly scoped future apply pass only if it can touch one clear canonical target and avoid runtime-output design, numeric thresholds, buyer tolerance thresholds, and inferred saleable mass.
