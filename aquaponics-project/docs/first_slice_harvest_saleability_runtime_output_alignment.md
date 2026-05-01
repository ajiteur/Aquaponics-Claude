# First Slice Harvest Saleability Runtime Output Alignment

Status: `draft`

## Purpose

- Align future runtime-output or adapter-output design with the accepted qualitative entries in `data/knowledge/ontology/harvest_saleability.yaml`.
- Keep this pass review-first and docs-only.
- Preserve the fixed slice: `basil bulk kg wholesale`.
- Do not implement runtime fields, adapter fields, schema fields, business logic, or ontology changes in this pass.

## Scope

- Read-only ontology input: `data/knowledge/ontology/harvest_saleability.yaml`.
- Runtime and adapter scope is limited to future design alignment.
- `saleable_harvest_mass_kg` remains unresolved.
- `crop_system_type` remains context-only.
- Product-form scope remains separate from `crop_system_type`.
- Aroma remains manual-review only and is not deterministic saleability logic.
- Ontology labels may be discussed only as future basis, reason, product-form boundary, or manual/QA review labels.

## Inputs Reviewed

- `data/knowledge/ontology/harvest_saleability.yaml`
- `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`
- `docs/first_slice_basil_harvest_saleability_promotion_candidate_map.md`
- `docs/first_slice_basil_harvest_saleability_canon_apply_surface.md`
- `docs/first_slice_basil_harvest_saleability_canonical_location_decision.md`
- `docs/first_slice_basil_harvest_saleability_vocabulary_ownership_apply_plan.md`
- `docs/first_slice_basil_harvest_saleability_minimal_vocabulary_design_plan.md`
- `docs/first_slice_runtime_native_harvest_output_plan.md`
- `docs/first_slice_saleable_harvest_mass_plan.md`
- `docs/runtime_to_business_field_audit.md`
- `docs/first_slice_adapter_spec.md`
- `docs/first_slice_repo_audit.md`

## Current Ontology Status

- The ontology status is `draft_with_accepted_qualitative_entries`.
- `accepted_vocabulary_entries_defined: true`.
- Four ontology groups are present:
  - `harvest_readiness_basis`
  - `saleability_basis`
  - `product_form_scope`
  - `quality_exclusion_reasons`
- The entries are qualitative vocabulary entries with `status: accepted_qualitative`.
- The ontology still excludes runtime fields, prices, costs, labor assumptions, penalty rates, inferred saleable mass, crop-system architecture behavior, and buyer tolerance thresholds.

## Runtime-Output Concepts And Epistemic States

| concept | intended epistemic state | alignment rule |
|---|---|---|
| `gross_harvest_mass_kg` | observed or explicitly reported total harvested basil mass before saleability exclusion | Must not be treated as saleable mass. |
| `observed_saleable_harvest_mass_kg` | mass accepted as saleable after human review, QA review, or receiving acceptance | May later carry saleability-basis labels, but only when acceptance is reviewed or observed. |
| `observed_rejected_harvest_mass_kg` | mass explicitly rejected or downgraded out of the target sale form | May later carry quality-exclusion reason labels. |
| `modeled_saleable_harvest_mass_kg` | estimated saleable mass from a model | Must remain separate from observed accepted mass and business-required saleable mass. |
| `saleable_harvest_mass_kg` | current first-slice required business input, still unresolved | Must remain null/unresolved unless backed by observed runtime output or explicit reviewed manual input. |

## How Ontology Labels May Be Used Later

- `harvest_readiness_basis` entries may later be referenced as basis labels explaining why a reviewed crop was considered ready to cut.
- `saleability_basis` entries may later be referenced as basis labels explaining why reviewed basil was considered saleable.
- `product_form_scope` entries may later be referenced as product-form boundary labels for `basil bulk kg wholesale` and adjacent out-of-scope forms.
- `quality_exclusion_reasons` entries may later be referenced as reason labels for observed rejection, downgrade, or exclusion.
- Ontology labels are not pass/fail logic by themselves.
- Ontology labels must not compute mass, revenue, saleability rate, shrink, price, cost, labor, penalties, or buyer acceptance.
- Ontology labels must not make `crop_system_type` a saleability, pricing, product-form, or business selector.

## What Remains Manual/QA Review Only

- Harvest-readiness labels such as non-flowering harvest stage and young vegetative leafy material.
- Saleability labels such as general marketability minimums, freshness and turgidity, and cultivar-appropriate appearance and color.
- Quality-exclusion labels, including visible decay or rot, wilting, discoloration, pest damage, mechanical damage, foreign matter, off-odour or off-taste, chilling injury, and food-safety contamination.
- Product-form boundary labels where runtime cannot determine product form from crop architecture alone.
- Aroma-related interpretation remains manual-review only. Positive aroma acceptability is not an accepted deterministic vocabulary entry.

## What Must Not Be Inferred

- Do not infer `saleable_harvest_mass_kg` from standing biomass.
- Do not infer it from daily biomass gain.
- Do not infer it from plant count.
- Do not infer it from modeled saleability.
- Do not infer observed saleable mass from `gross_harvest_mass_kg`.
- Do not infer observed saleable mass from `modeled_saleable_harvest_mass_kg`.
- Do not infer product form, pricing path, saleability status, or buyer acceptance from `crop_system_type`.
- Do not infer rejection reasons from visual greenness, harvest readiness, or model state alone.

## Candidate Implementation Surface Comparison

| candidate surface | value | risk | readiness | likely future touched files or flow | stop rules |
|---|---:|---|---|---|---|
| Runtime-native harvest output path | 8 | high | needs design | Future runtime-facing basil harvest output flow; exact producer path must be approved before any edit. | Stop if output would infer saleable mass from standing biomass, daily gain, plant count, or modeled saleability. Stop if a broad harvest-event framework is required for the first slice. |
| Adapter payload/null-status path | 8 | low | needs design | First-slice adapter payload flow, likely around `scripts/build_first_slice_adapter_payload.py` and generated adapter payload examples in a later explicit apply. | Stop if labels become schema-wide business selectors, pricing inputs, or mass calculations. Stop if ontology entries would need to change again. |
| Reviewed-manual input path | 7 | medium | needs design | Existing reviewed-manual override flow for `saleable_harvest_mass_kg`; later run-scoped review input and provenance packet. | Stop if a manual value is hidden as runtime-native truth. Stop if no reviewed non-null value exists. |
| Business consumer path | 4 | high | blocked | Future business consumer flow only after observed or reviewed saleable mass exists. | Stop if ontology labels are used to calculate revenue, rates, shrink, penalties, or buyer acceptance. |
| No implementation yet | 5 | low | ready now | Docs-only alignment; no code, runtime, adapter, ontology, or business file changes. | Stop if the next request tries to combine design, runtime changes, and business consumer changes in one pass. |

## Recommended Smallest Future Implementation Surface

The smallest future implementation surface should be the adapter payload/null-status path, not runtime-native harvest output and not business consumption.

Recommended future shape by flow only:

- keep `saleable_harvest_mass_kg` null when no observed or reviewed value exists
- allow a later adapter design to attach ontology labels only as basis, reason, product-form boundary, or manual/QA review labels
- keep the adapter thin and descriptive
- do not calculate saleable mass from ontology labels
- do not require any ontology entry changes

Runtime-native harvest output remains the stronger long-term target, but it should wait until explicit harvest observations or direct saleable harvest output are designed.

## What Is Still Blocked

- Non-null `saleable_harvest_mass_kg` remains blocked until observed runtime harvest output or explicit reviewed manual input exists.
- `gross_harvest_mass_kg`, `observed_saleable_harvest_mass_kg`, `observed_rejected_harvest_mass_kg`, and `modeled_saleable_harvest_mass_kg` remain design concepts only until a later explicit runtime or adapter schema pass.
- Buyer tolerance percentages, numeric harvest-size thresholds, aroma scores, shrink rates, penalty rates, and saleability-rate thresholds remain blocked.
- Business consumption of ontology labels remains blocked.
- Runtime-native harvest output remains blocked until the producer path and source semantics are approved.

## Recommended Next Action

- Keep this alignment note as a docs-only artifact.
- If implementation is requested next, start with a narrow adapter payload/null-status design pass that references existing ontology labels without changing ontology entries.
- Keep runtime-native harvest output as a later separate pass.
- Keep business consumer changes blocked until `saleable_harvest_mass_kg` is backed by observed runtime output or explicit reviewed manual input.
