# First Slice Basil Harvest Saleability Vocabulary Ownership Apply Plan

Status: `draft`

## Purpose

- Choose the exact future canonical vocabulary path for first-slice basil harvest-readiness and saleability.
- Define ownership boundaries for a later apply pass.
- Keep this pass review-first and non-canonical.
- Do not create the vocabulary file, vocabulary entries, schema content, runtime fields, or canonical diffs in this pass.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- Future vocabulary scope covers four concept groups only:
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
- `docs/first_slice_basil_harvest_saleability_canonical_location_decision.md`

Supporting input:

- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`

Canonical areas inspected for path and ownership fit:

- `data/knowledge/species/plants/`
- `data/knowledge/business/`
- `data/knowledge/models/`
- `data/knowledge/model_tickets/`
- `data/knowledge/evidence_maps/`
- existing repo ontology area:
  - `data/knowledge/ontology/`

## Recommended Future Canonical Vocabulary Path

Recommended future path:

- `data/knowledge/ontology/harvest_saleability.yaml`

Why this path:

- `data/knowledge/ontology/` already exists and is the closest existing repo area for canonical terms and semantic boundaries.
- A single focused file avoids spreading review vocabulary across species, business, model, ticket, and evidence-map files.
- The name is narrow enough for the current problem and broad enough to hold the four agreed concept groups without creating a folder hierarchy.
- YAML matches the existing files in `data/knowledge/ontology/`.

Not recommended:

- `data/knowledge/species/plants/basil.json` as the vocabulary owner.
- `data/knowledge/business/yield_to_revenue_rules.json` as the vocabulary owner.
- `data/knowledge/models/plant_system_models.json` as the vocabulary owner.
- `data/knowledge/evidence_maps/**` as the vocabulary owner.
- A broad new taxonomy folder.

## Ownership Boundary

The future file should own canonical review vocabulary boundaries only.

It should own:

- the names and meanings of accepted review-basis categories for harvest readiness
- the names and meanings of accepted review-basis categories for saleability
- the names and meanings of product-form scope categories relevant to harvest and saleability review
- the names and meanings of accepted quality-exclusion reason categories
- the manual-review boundary for sensory or QA-dependent concepts
- links or references to provenance support, without becoming an evidence map

It should not own:

- species-specific numeric biology parameters
- runtime output fields or adapter field names
- saleable mass values or methods for inferring them
- pricing, revenue, cost, labor, or penalty rates
- buyer-specific tolerance thresholds
- product prices or channel assumptions
- architecture behavior or `crop_system_type` semantics
- unresolved evidence questions

## What Belongs in the Future Vocabulary

The future vocabulary may eventually contain only qualitative, reusable review concepts for:

- harvest-readiness basis
- saleability basis
- product-form scope
- quality exclusion reasons
- manual-review-only markers where evidence supports a concept but not deterministic runtime logic
- provenance hooks to source-family labels and evidence-map records

This plan does not define the entries.

## What Must Stay Out

The future vocabulary must not contain:

- numeric harvest-height thresholds
- numeric leaf-count thresholds
- numeric stem-length thresholds
- aroma-score thresholds
- buyer tolerance percentages or defect thresholds
- inferred `saleable_harvest_mass_kg`
- gross, observed, rejected, or modeled mass field definitions as runtime-output design
- runtime-native field names or adapter contract fields
- price, cost, labor, CAPEX, or penalty-rate assumptions
- architecture-conditioned product-form selection
- any automatic rule that treats `crop_system_type` as a saleability selector
- evidence-map records as the semantic source of truth

## Relationship to Existing Canon Files

`data/knowledge/species/plants/basil.json`:

- should remain the species-specific fact profile
- may later reference or align with the vocabulary for basil-specific maturity and stress facts
- should not own the harvest-readiness or saleability vocabulary
- should not receive buyer/product-form or commercial acceptance semantics by default

`data/knowledge/business/yield_to_revenue_rules.json`:

- should remain a revenue translation rule file
- may later consume saleable output concepts after runtime or reviewed input exists
- should not define quality review terms
- should not resolve `saleable_harvest_mass_kg`

Other business files:

- pricing, channel, risk, cost, and labor files may later consume or reference vocabulary concepts
- they should not be the owner of harvest-readiness, saleability, product-form, or quality-exclusion terms
- risk and channel placeholders remain downstream consumers or TODO holders

`data/knowledge/models/**`:

- should remain for dynamic, biological, disease, architecture, or system-behavior models
- should not own manual QA vocabulary
- may later consume vocabulary concepts only if a separate model pass needs them

## Relationship to Model Tickets and Evidence Maps

`data/knowledge/model_tickets/**`:

- should hold unresolved blockers, open questions, and future work items
- should not contain accepted vocabulary entries
- appropriate ticket topics include buyer tolerances, aroma QA method, vocabulary shape, and runtime observation gaps

`data/knowledge/evidence_maps/**`:

- should provide provenance support and source traceability
- should not be the semantic home for saleability vocabulary
- may later link source-family evidence to vocabulary groups after a scoped apply pass

## Smallest Later Apply Pass Enabled

Smallest later apply pass:

- create `data/knowledge/ontology/harvest_saleability.yaml`
- keep it as an ownership scaffold only
- do not edit species, business, model, ticket, evidence-map, runtime, or script files in the same pass
- do not add vocabulary entries in that first scaffold pass
- include only enough metadata to identify ownership, status, source basis, and scope if the later apply pass explicitly approves metadata

This is intentionally smaller than adding accepted terms.

## Whether the Later Apply Should Create Scaffold Only or Include Minimal Groups

Recommendation:

- scaffold only

Reason:

- The exact path and ownership boundary can be made canonical before debating term shape.
- The source evidence supports the broad concept groups, but actual entries still need a scoped vocabulary-design pass.
- A scaffold-only pass minimizes risk of accidentally promoting thresholds, runtime fields, or buyer assumptions.
- Existing ontology files are lightweight, so a small scaffold fits the repo pattern.

Minimal vocabulary groups should wait for a separate explicit apply pass after the scaffold exists.

## Validation for the Later Apply Pass

For the later scaffold apply pass, run:

- `git --no-pager diff -- data/knowledge/ontology/harvest_saleability.yaml`
- `git status --short`
- a YAML parse check if the scaffold contains metadata
- a scoped changed-path check confirming no changes under:
  - `data/simulation/**`
  - `src/**`
  - `scripts/**`
- a protected-concept search in the scaffold diff for:
  - numeric height thresholds
  - leaf-count thresholds
  - stem-length thresholds
  - aroma-score thresholds
  - buyer tolerance percentages
  - inferred `saleable_harvest_mass_kg`
  - runtime-output field definitions
  - `crop_system_type` as selector logic

If the scaffold is intentionally empty, the YAML parse check may be skipped and the empty-file choice should be stated in the final report.

## Blockers

- Actual vocabulary entries are not designed yet.
- The scaffold metadata shape is not approved yet.
- `saleable_harvest_mass_kg` remains unresolved.
- Runtime output still does not provide observed saleable harvest mass.
- Buyer tolerances remain unsupported.
- Aroma remains manual-review only and lacks a standardized QA method.
- Product-form scope must remain separate from `crop_system_type`.

## Recommended Next Action

- Keep this plan as a docs-only future-apply plan.
- Do not apply canon yet.
- Next explicit apply pass, if approved, should create only `data/knowledge/ontology/harvest_saleability.yaml` as an ownership scaffold.
- After the scaffold exists, run a separate review-first vocabulary-design pass before adding any accepted vocabulary entries.
