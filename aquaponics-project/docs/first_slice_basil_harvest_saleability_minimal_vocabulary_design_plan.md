# First Slice Basil Harvest Saleability Minimal Vocabulary Design Plan

Status: `draft`

## Purpose

- Design the smallest safe first vocabulary-entry apply plan for `data/knowledge/ontology/harvest_saleability.yaml`.
- Keep this as a review-first design plan only.
- Do not edit the ontology file or any canonical file in this pass.
- Keep the plan limited to qualitative vocabulary design for `basil bulk kg wholesale`.

## Scope

- Future vocabulary groups considered:
  - harvest-readiness basis
  - saleability basis
  - product-form scope
  - quality exclusion reasons
- This pass does not modify `data/knowledge/**`, `data/simulation/**`, `src/**`, or `scripts/**`.
- `saleable_harvest_mass_kg` remains unresolved.
- `crop_system_type` remains context-only.
- Product-form scope remains separate from `crop_system_type`.
- Aroma remains manual-review only.
- Modeled saleable mass remains separate from observed saleable mass.
- Numeric harvest-height, leaf-count, stem-length, aroma-score, buyer-tolerance, shrink, penalty, and saleability-rate thresholds remain out of scope.

## Inputs Reviewed

Canonical scaffold:

- `data/knowledge/ontology/harvest_saleability.yaml`

Planning inputs:

- `docs/first_slice_basil_harvest_saleability_vocabulary_ownership_apply_plan.md`
- `docs/first_slice_basil_harvest_saleability_canonical_location_decision.md`
- `docs/first_slice_basil_harvest_saleability_canon_apply_surface.md`
- `docs/first_slice_basil_harvest_saleability_promotion_candidate_map.md`
- `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`

Supporting research input:

- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`

Source-family basis preserved from the reviewed inputs:

- EU general marketing standard baseline for fresh produce
- Basilico Genovese PDO proxy
- UC Davis basil/herb postharvest guidance
- Rutgers fresh-market basil guidance
- 2023 Frontiers basil postharvest review
- FDA fresh culinary herb food-safety/handling guidance
- UVI aquaponic basil repeated-cut findings

## Current Ontology Scaffold Status

- `git ls-files -- data/knowledge/ontology/harvest_saleability.yaml` confirms the scaffold is tracked.
- The scaffold status is `scaffold_draft`.
- The scaffold identifies the canonical owner as `data/knowledge/ontology/harvest_saleability.yaml`.
- The scaffold is still scaffold-only:
  - `accepted_vocabulary_entries_defined: false`
  - no accepted vocabulary groups are populated
  - no vocabulary entries are defined
  - no example terms are defined
- The scaffold preserves the required invariants:
  - `saleable_harvest_mass_kg` is unresolved
  - `crop_system_type` is context-only
  - aroma is manual-review only
  - product-form scope is separate from `crop_system_type`
  - modeled saleable mass is separate from observed saleable mass

## Minimal First Vocabulary Groups

The smallest useful first vocabulary-entry apply should add these four group containers and only the safest qualitative entries inside them:

- harvest-readiness basis
- saleability basis
- product-form scope
- quality exclusion reasons

The groups are already listed in the scaffold as future semantic homes. The later apply pass should keep them qualitative and review-oriented.

## Group-by-Group Design Boundaries

| group | purpose | allowed concept type | evidence support | must stay out | later apply readiness |
|---|---|---|---|---|---|
| harvest-readiness basis | Describe why fresh basil is considered ready to cut for the fixed slice. | Qualitative manual-review concepts such as vegetative maturity and absence of flowering. | Basilico Genovese PDO proxy; Rutgers fresh-market basil guidance; UC Davis herb guidance. | Numeric height, leaf-count, stem-length, node-count, or one universal cut-size trigger. | Ready for a later qualitative apply. |
| saleability basis | Describe the manual-review basis for treating fresh basil as saleable. | Qualitative minimum marketability and basil freshness concepts. | EU general marketing baseline; UC Davis basil/herb postharvest guidance; Rutgers handling/quality guidance. | Saleable mass fields, automated acceptance logic, buyer tolerance thresholds, storage-temperature acceptance rules. | Ready for a later qualitative apply. |
| product-form scope | Distinguish the target product form from adjacent forms. | Qualitative product-form scope concepts for bulk wholesale cut basil versus other forms. | FDA fresh culinary herb guidance; 2023 Frontiers review; Basilico Genovese PDO proxy. | `crop_system_type` selector logic, architecture-conditioned product-form logic, pricing or channel rules. | Ready for a later qualitative apply. |
| quality exclusion reasons | Describe qualitative reasons a lot may be excluded or rejected from the target sale form. | Qualitative manual-review exclusion categories. | EU baseline; UC Davis basil/herb postharvest guidance; FDA herb guidance; 2023 Frontiers review. | Defect percentages, buyer thresholds, shrink rates, penalty rates, runtime event schemas. | Ready for a later qualitative apply. |

## Candidate Qualitative Concepts for Later Apply

Candidate concepts are named descriptively here only. These are not final canonical IDs.

Harvest-readiness basis:

- non-flowering harvest stage
- young vegetative leafy material
- fresh culinary cut-basil context

Saleability basis:

- general marketability minimums
- freshness and turgidity
- cultivar-appropriate appearance and color as manual review
- characteristic aroma as manual-review only

Product-form scope:

- bulk wholesale cut basil as target scope
- RTU/RTE retail-packed herbs as out-of-scope adjacent forms
- live-root and potted basil as out-of-scope adjacent forms
- bunch-specific basil as a distinct adjacent form

Quality exclusion reasons:

- visible decay or rot
- serious wilting or loss of turgidity
- serious yellowing, browning, or blackening
- serious pest presence or pest damage
- serious mechanical damage
- foreign matter
- off-odour or off-taste
- chilling injury as manual-review exclusion
- food-safety contamination as QA/compliance exclusion

## Candidate Readiness Classifications

| candidate qualitative concept | classification | rationale |
|---|---|---|
| non-flowering harvest stage | `ready_for_first_vocabulary_apply` | Strong qualitative support and no need for numeric threshold. |
| young vegetative leafy material | `ready_for_first_vocabulary_apply` | Strong maturity concept support; keep non-numeric. |
| fresh culinary cut-basil context | `ready_for_first_vocabulary_apply` | Keeps the fixed slice and product context explicit. |
| general marketability minimums | `ready_for_first_vocabulary_apply` | Strong formal produce baseline; keep qualitative. |
| freshness and turgidity | `ready_for_first_vocabulary_apply` | Strong baseline for manual saleability review. |
| cultivar-appropriate appearance and color | `ready_for_first_vocabulary_apply` | Supported as manual review; no automated visual-only acceptance. |
| characteristic aroma | `keep_provisional` | Important for basil but must remain manual-review only; no scoring method yet. |
| bulk wholesale cut basil target scope | `ready_for_first_vocabulary_apply` | Strong product-form boundary for the first slice. |
| RTU/RTE retail-packed herbs as adjacent forms | `ready_for_first_vocabulary_apply` | Strong source support for product-form distinction. |
| live-root and potted basil as adjacent forms | `ready_for_first_vocabulary_apply` | Strong enough to prevent product-form mixing. |
| bunch-specific basil as adjacent form | `ready_for_first_vocabulary_apply` | Useful boundary; keep channel and packing assumptions out. |
| visible decay or rot | `ready_for_first_vocabulary_apply` | Strong exclusion concept. |
| serious wilting or loss of turgidity | `ready_for_first_vocabulary_apply` | Strong manual-review exclusion concept. |
| serious yellowing, browning, or blackening | `ready_for_first_vocabulary_apply` | Strong qualitative defect concept; no tolerance thresholds. |
| serious pest presence or pest damage | `ready_for_first_vocabulary_apply` | Strong marketability and defect basis. |
| serious mechanical damage | `ready_for_first_vocabulary_apply` | Strong defect and decay-risk basis. |
| foreign matter | `ready_for_first_vocabulary_apply` | Strong marketability and food-safety boundary. |
| off-odour or off-taste | `ready_for_first_vocabulary_apply` | Strong marketability boundary; sensory/manual review only. |
| chilling injury | `ready_for_first_vocabulary_apply` | Strong basil-specific exclusion concept; no injury-score threshold. |
| food-safety contamination | `ready_for_first_vocabulary_apply` | Strong QA/compliance exclusion concept; not inferable from appearance. |
| regrowth reserve after cutting | `keep_provisional` | Relevant to repeated-cut operations, but context split is not ready. |
| slight post-dispatch freshness/turgidity loss | `keep_provisional` | Useful nuance but not ready as accepted vocabulary without buyer/receiving language. |
| storage and handling band | `keep_provisional` | Operationally important but should not become a saleability acceptance term. |
| numeric harvest-size proxies | `blocked` | Height, leaf-count, stem-length, and node-count thresholds are context-dependent. |
| buyer defect tolerances | `blocked` | Current source set lacks high-trust bulk-wholesale tolerance thresholds. |
| aroma score threshold | `blocked` | No standardized QA scoring method exists. |
| inferred saleable mass | `blocked` | `saleable_harvest_mass_kg` remains unresolved and must not be inferred. |
| modeled saleable mass as observed saleable mass | `blocked` | Violates observed/modelled separation. |
| `crop_system_type` as product-form selector | `blocked` | Product-form scope must remain separate from system architecture context. |

## Concepts Blocked from First Vocabulary Apply

- one universal harvest-height threshold
- one universal leaf-count threshold
- one universal stem-length or node-count threshold
- numeric aroma score or aroma pass/fail threshold
- buyer tolerance percentages or defect thresholds
- shrink, penalty, or saleability-rate thresholds
- inferred `saleable_harvest_mass_kg`
- runtime output field names or adapter contract fields
- gross, observed, rejected, or modeled mass field definitions
- any rule that treats `crop_system_type` as a product-form, pricing, or saleability selector
- any concept that treats modeled saleable mass as observed saleable mass

## Recommended Next Apply Shape

Recommendation:

- group headers plus minimal qualitative entries

The later apply pass should add only:

- the four group containers
- a small set of qualitative entries classified above as `ready_for_first_vocabulary_apply`
- status and provenance metadata needed to show the entries are qualitative and review-based

The later apply pass should not add:

- entries classified as `keep_provisional`
- entries classified as `blocked`
- numeric thresholds
- runtime field definitions
- business calculation fields
- final consumer references in species, business, model, ticket, or evidence-map files

Canonical IDs are not finalized in this plan. If draft IDs are used in a later pre-apply review, they should be marked illustrative only until the apply scope is approved.

## Why This Apply Shape Is Safest

Group headers only would be safer in the narrowest mechanical sense, but it would not test whether the ontology can hold the already-reviewed qualitative concepts.

Group headers plus minimal qualitative entries is safer than a broader vocabulary apply because it:

- uses only concepts already marked as likely later canon candidates
- avoids all numeric thresholds and buyer-specific assumptions
- keeps aroma, regrowth reserve, storage/handling, and transit-loss nuance provisional
- does not touch species, business, model, ticket, evidence-map, runtime, or script files
- keeps `saleable_harvest_mass_kg` unresolved
- preserves the boundary between product form and `crop_system_type`
- preserves the boundary between modeled and observed saleable mass

## Validation for the Later Apply Pass

For a later approved vocabulary-entry apply pass, run:

- YAML parse check for `data/knowledge/ontology/harvest_saleability.yaml`
- `git --no-pager diff -- data/knowledge/ontology/harvest_saleability.yaml`
- `git status --short`
- changed-path check confirming no changes under:
  - `docs/**`
  - `data/simulation/**`
  - `src/**`
  - `scripts/**`
  - `data/knowledge/species/**`
  - `data/knowledge/business/**`
  - `data/knowledge/models/**`
  - `data/knowledge/model_tickets/**`
  - `data/knowledge/evidence_maps/**`
- protected-concept search in the ontology diff for:
  - numeric harvest-height thresholds
  - leaf-count thresholds
  - stem-length thresholds
  - aroma-score thresholds
  - buyer tolerance percentages
  - inferred `saleable_harvest_mass_kg`
  - runtime-output field definitions
  - `crop_system_type` selector logic
  - modeled saleable mass treated as observed saleable mass

Before committing the later apply, stage only `data/knowledge/ontology/harvest_saleability.yaml` and confirm that `git diff --cached --name-only --relative` shows only that path.

## Blockers

- Canonical IDs are not finalized.
- The exact vocabulary entry shape is not approved.
- `keep_provisional` concepts require separate review before entry creation.
- `blocked` concepts require stronger evidence or a separate runtime/business/model design decision.
- `saleable_harvest_mass_kg` remains unresolved.
- Runtime output still does not provide observed saleable harvest mass.

## Recommended Next Action

- Keep this plan as a docs-only review artifact.
- Next explicit apply pass should update only `data/knowledge/ontology/harvest_saleability.yaml`.
- That apply should add group headers plus the minimal qualitative entries marked `ready_for_first_vocabulary_apply`, with no numeric thresholds, runtime fields, business fields, or cross-file consumer edits.
