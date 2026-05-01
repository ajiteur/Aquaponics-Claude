# First Slice Basil Harvest Saleability Canonical Location Decision

Status: `draft`

## Purpose

- Decide where first-slice basil harvest-readiness and saleability concepts should eventually live canonically.
- Keep this as a review-first location decision only.
- Do not design vocabulary entries, schema fields, runtime fields, or canonical diffs in this pass.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- Concepts reviewed:
  - harvest-readiness basis
  - saleability basis
  - product-form scope
  - quality exclusion reasons
- This pass does not modify `data/knowledge/**`, `data/simulation/**`, `src/**`, or `scripts/**`.
- `saleable_harvest_mass_kg` remains unresolved.
- `crop_system_type` remains context-only.
- Aroma remains manual-review only.
- Numeric harvest-height, leaf-count, stem-length, aroma-score, and buyer-tolerance thresholds remain blocked.

## Inputs Reviewed

Primary inputs:

- `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`
- `docs/first_slice_basil_harvest_saleability_promotion_candidate_map.md`
- `docs/first_slice_basil_harvest_saleability_canon_apply_surface.md`

Supporting input:

- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`

Canonical areas inspected for location fit only:

- `data/knowledge/species/plants/`
- `data/knowledge/business/`
- `data/knowledge/models/`
- `data/knowledge/model_tickets/`
- `data/knowledge/evidence_maps/`

## Candidate Canonical Homes

- Existing basil species profile:
  - `data/knowledge/species/plants/basil.json`
- Existing business files:
  - especially `data/knowledge/business/yield_to_revenue_rules.json`
  - related but not primary: pricing, channel, risk, cost, and labor files
- Existing model files:
  - especially `data/knowledge/models/plant_system_models.json`
  - related disease/climate models only where dynamic stress modeling is in scope
- Future new canonical vocabulary file:
  - best candidate class for harvest-readiness basis, saleability basis, product-form scope, and quality exclusion reasons
  - exact path and schema are intentionally not designed here
- Open questions or model tickets:
  - `data/knowledge/model_tickets/**`
- Evidence maps:
  - `data/knowledge/evidence_maps/**`
- Docs only:
  - current spec, promotion map, and apply-surface notes

## Evaluation by Concept Group

| concept group | best eventual semantic home | supporting canonical home | not a good primary home | reason |
|---|---|---|---|---|
| harvest-readiness basis | Future new canonical vocabulary file | `data/knowledge/species/plants/basil.json` | business rules | Needs reusable review terms; basil profile can carry species-specific maturity support but should not define the whole review vocabulary. |
| saleability basis | Future new canonical vocabulary file | business files may later reference it | `basil.json` alone | Saleability mixes produce quality, QA review, product scope, and commercial acceptance. |
| product-form scope | Future new canonical vocabulary file | business rules may later consume the product-form distinction | `crop_system_type` or plant-system models | Product form is not the same as architecture or crop system type. |
| quality exclusion reasons | Future new canonical vocabulary file | evidence maps for provenance; tickets for unresolved tolerances | yield-to-revenue rules | Rejection reasons are controlled review terms, not revenue translation logic. |
| unresolved thresholds and buyer tolerances | model tickets or docs only | evidence maps for provenance | canonical vocabulary now | Evidence is insufficient for numeric tolerance vocabularies or thresholds. |

## Candidate-Home Rating Table

Ratings are decision aids only; they are not evidence-strength scores.

| candidate home | fit | risk | boundary clarity | evidence/provenance fit | location decision |
|---|---:|---|---|---|---|
| `data/knowledge/species/plants/basil.json` | 6 | medium | mixed | medium | Good supporting home for species-specific maturity and stress facts; not sufficient for saleability vocabulary. |
| `data/knowledge/business/yield_to_revenue_rules.json` | 3 | high | poor | weak | Business consumer of saleable mass only; should not define QA or biology criteria. |
| Other `data/knowledge/business/**` files | 4 | medium | mixed | weak | Useful later for pricing, channel, risk, cost, or labor consumers; not the semantic home. |
| `data/knowledge/models/plant_system_models.json` | 2 | high | poor | weak | Architecture behavior model; saleability review terms do not belong here. |
| Other `data/knowledge/models/**` files | 3 | medium | mixed | weak | May model disease or postharvest dynamics later, but not the vocabulary home. |
| Future new canonical vocabulary file | 9 | medium | clear | strong | Best semantic home, provided a later pass chooses path and shape explicitly. |
| `data/knowledge/model_tickets/**` | 5 | low | clear | medium | Good for blockers and open questions, not for accepted vocabulary. |
| `data/knowledge/evidence_maps/**` | 6 | low | clear | strong | Good provenance support, not the semantic home for saleability terms. |
| Docs only | 7 | low | clear | medium | Best current non-canon holding location until the vocabulary path is chosen and applied. |

## Recommended Canonical Location Strategy

Use a split-location strategy.

Recommended strategy:

- Future new canonical vocabulary location as the primary semantic home for:
  - harvest-readiness basis
  - saleability basis
  - product-form scope
  - quality exclusion reasons
- `data/knowledge/species/plants/basil.json` as a supporting home for species-specific facts only:
  - young vegetative/non-flowering maturity support
  - chilling sensitivity and saleability relevance
  - repeated-cut stress context already present in the profile
- Business files as consumers only:
  - they may later reference saleability or product-form concepts once canonical vocabulary exists
  - they should not define the concepts
- `data/knowledge/model_tickets/**` for unresolved thresholds, buyer tolerances, aroma QA, and vocabulary-design blockers.
- `data/knowledge/evidence_maps/**` for source traceability and provenance only.
- Docs remain the holding layer until a future apply pass is explicitly requested.

## Split-Location Strategy, if Recommended

Split-location strategy is recommended because the concept groups cross repo layers:

- Harvest-readiness basis has species-specific biological content, but the review terms should be reusable.
- Saleability basis combines biological condition, postharvest handling, manual QA, and commercial acceptance.
- Product-form scope is a product/market distinction, not a species trait or architecture field.
- Quality exclusion reasons are manual-review categories that may support business, runtime, and evidence traceability later.

Boundary rule:

- Species profile supports facts.
- Vocabulary owns review terms.
- Business files consume accepted saleable outputs.
- Runtime output records observations or modeled estimates.
- Evidence maps support provenance.
- Tickets hold unresolved blockers.

## Why Not Only `basil.json`

- `basil.json` is species-specific and can support young vegetative/non-flowering maturity and chilling sensitivity.
- It is not sufficient for product-form scope because bulk wholesale, RTU/RTE, live-root, potted, and bunch-specific forms are product and channel distinctions.
- It is not sufficient for saleability basis because acceptance depends on manual QA, handling history, contamination status, and buyer context.
- It is not sufficient for quality exclusion reasons because those should be controlled review terms reusable across future crops and products.
- Putting all saleability semantics into `basil.json` would blur species facts with commercial acceptance logic.

## Why Not Only `yield_to_revenue_rules.json`

- `yield_to_revenue_rules.json` currently defines revenue translation requirements, including `rule_basil_bulk_kg`.
- It should not define what makes basil saleable, because that would mix input semantics with revenue calculation.
- It cannot resolve `saleable_harvest_mass_kg`; runtime output or reviewed human input is still required.
- It is not the right place for harvest-readiness basis, product-form scope, or quality exclusion vocabularies.
- Editing it first would risk treating business requirements as proof of biological or QA truth.

## What Remains Docs-Only

- Current spec, promotion map, and apply-surface reasoning.
- Regrowth reserve for repeated-cut basil until operations context is formalized.
- Slight post-dispatch freshness/turgidity nuance.
- Aroma acceptability as manual-review guidance.
- Storage and handling bands as operator/model-context guidance.
- Buyer tolerance discussion for minor yellowing, wilt, stem breakage, leaf-size mix, or stem-to-leaf ratio.

## What Remains Runtime-Output Design Only

- Separation of gross harvested, observed accepted saleable, observed rejected, and modeled saleable mass.
- Any future runtime or adapter field for saleability basis, harvest-readiness basis, quality exclusion reasons, or acceptance confidence.
- Any adapter-side rollup from explicit harvest observations.
- Any non-manual runtime source for `saleable_harvest_mass_kg`.
- Any modeled saleability or marketable-share adjustment.

## Blockers Before Vocabulary Design

- Choose the exact canonical vocabulary path in a later apply-scoped plan.
- Decide whether the vocabulary is crop-specific, product-form-specific, or shared with crop/product qualifiers.
- Decide how provenance will link to evidence maps without making evidence maps the semantic home.
- Decide how open buyer tolerances and aroma QA blockers will be represented outside accepted vocabulary.
- Keep `saleable_harvest_mass_kg` unresolved until observed runtime harvest output or explicit reviewed human approval exists.
- Keep `crop_system_type` context-only and separate from product-form scope.

## Minimum Viable Future Apply Path

Minimum viable future apply path enabled by this decision:

1. Create a tightly scoped future apply plan for a new canonical vocabulary location.
2. In that later plan, define only the location and ownership boundary first.
3. After explicit approval, add the smallest accepted qualitative vocabulary groups without numeric thresholds or runtime fields.
4. Add only source/provenance references needed to connect the vocabulary to the reviewed basil source families.
5. Leave business, runtime, model, cost, and labor files untouched until consumers need the vocabulary.

This pass does not design those entries.

## Recommended Next Action

- Keep this decision doc as non-canonical guidance.
- Do not apply canon yet.
- Next non-canon step: draft a narrow vocabulary-ownership apply plan that chooses the exact future path and ownership boundary, still without adding terms.
- After that, request an explicit `apply` pass before creating any canonical vocabulary file or editing any existing canonical file.
