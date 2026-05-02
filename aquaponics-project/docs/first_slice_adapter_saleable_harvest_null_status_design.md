# First Slice Adapter Saleable Harvest Null Status Design

Status: `draft`

## 1. Purpose

- Define how the first-slice adapter should represent unresolved `saleable_harvest_mass_kg` after the harvest/saleability ontology apply.
- Keep this as a review-first adapter design note for `basil bulk kg wholesale`.
- Preserve the current null/unresolved state until observed runtime harvest output or explicit reviewed manual input exists.
- Keep ontology labels qualitative and descriptive only.

## 2. Scope

- This pass is docs-only.
- This note does not modify canonical biology, model, business, ontology, runtime, script, or schema files.
- Runtime-native harvest output remains a separate later pass.
- Business-consumer behavior remains blocked until `saleable_harvest_mass_kg` has a reviewed non-null source.
- `crop_system_type` remains context-only.
- Product-form scope remains separate from `crop_system_type`.
- Aroma remains manual-review only.

## 3. Inputs Reviewed

Primary inputs:

- `docs/first_slice_harvest_saleability_runtime_output_alignment.md`
- `data/knowledge/ontology/harvest_saleability.yaml`

Supporting docs:

- `docs/first_slice_adapter_spec.md`
- `docs/runtime_to_business_field_audit.md`
- `docs/first_slice_saleable_harvest_mass_plan.md`
- `docs/first_slice_runtime_native_harvest_output_plan.md`
- `docs/first_slice_repo_audit.md`
- `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`
- `docs/first_slice_basil_harvest_saleability_minimal_vocabulary_design_plan.md`

Comparison-only files:

- `scripts/build_first_slice_adapter_payload.py`
- `scripts/example_first_slice_overrides.json`
- `scripts/example_first_slice_reviewed_manual_overrides.json`
- `scripts/example_first_slice_working_inputs.json`
- `data/knowledge/business/yield_to_revenue_rules.json`

## 4. Current Repo Truth

- `rule_basil_bulk_kg` in `data/knowledge/business/yield_to_revenue_rules.json` requires `saleable_harvest_mass_kg` for the active basil bulk kg revenue path.
- The current runtime-facing basil scenario output does not emit observed saleable harvest mass.
- Current runtime-facing files expose state and proxy information such as standing crop state, plant count, daily gain, chemistry, and energy; they do not provide a harvest rollup or observed acceptance result.
- The first-slice adapter currently emits `saleable_harvest_mass_kg` from explicit overrides only. The current example and reviewed-manual override files keep it as `null`.
- `saleable_harvest_mass_kg` must remain `null` and unresolved when no observed runtime output or explicit reviewed manual value exists.
- The harvest/saleability ontology is qualitative review vocabulary. It owns review labels and boundaries, not calculations.
- Ontology labels do not calculate saleable mass, revenue, shrink, penalties, saleability rates, or buyer acceptance.
- `crop_system_type` is architecture context only and must not become a product-form, pricing, saleability, or business selector.

## 5. Adapter Null-Status Design

Current adapter payload value:

```json
"saleable_harvest_mass_kg": null
```

Recommended unresolved meaning:

- `null` means no observed runtime saleable harvest mass and no approved reviewed-manual value were supplied for this run.
- The null state should be described as unresolved, not zero.
- The null state should remain visible to downstream review as a blocker for true basil bulk kg revenue calculation.
- The adapter may continue to classify the field as `missing` in metadata while the runtime source is absent.
- A later adapter pass may add a descriptive null-status or basis note, but that note must be metadata, not a numeric fallback and not a business calculation input.

Null must not mean:

- no basil was harvested
- no basil was saleable
- standing biomass is unavailable
- modeled saleability is zero
- the lot failed saleability review

## 6. Current Recommended Adapter Behavior

- Keep the top-level field present as `saleable_harvest_mass_kg: null`.
- Keep the adapter thin: flatten current runtime fields, carry fixed slice configuration, and preserve missing/deferred statuses.
- Keep existing override behavior: only an explicit reviewed override may provide a non-null value, and only after approval in a later pass.
- Do not infer from standing biomass, daily biomass gain, plant count, greenness, harvest-readiness labels, saleability labels, or product-form labels.
- Do not add ontology label arrays to current payloads in this pass.
- Do not add runtime-native harvest fields or business schema fields in this pass.

## 7. Possible Future Adapter Behavior

Possible later behavior should remain staged:

- First, add a descriptive adapter metadata note for the null state if an implementation pass explicitly approves the payload shape.
- Later, carry ontology labels only as review-context labels when there is a reviewed basis to attach them.
- Later still, consume runtime-native saleable harvest output if the runtime emits an explicit non-manual `saleable_harvest_mass_kg`.
- Business consumers should remain blocked until the mass field is backed by observed runtime harvest output or explicit reviewed manual input.

## 8. How Ontology Labels May Be Carried Later

Future adapter payloads may later carry these labels conceptually only:

- harvest-readiness basis labels, such as `non_flowering_harvest_stage`, `young_vegetative_leafy_material`, and `fresh_culinary_cut_basil_context`
- saleability basis labels, such as `general_marketability_minimums`, `freshness_and_turgidity`, and `cultivar_appropriate_appearance_and_color`
- product-form boundary labels, such as `bulk_wholesale_cut_basil_target_scope`, adjacent RTU/RTE retail-packed herb forms, live-root or potted basil forms, and bunch-specific basil as a distinct adjacent form
- quality exclusion reason labels, such as visible decay or rot, serious wilting, serious discoloration, pest damage, mechanical damage, foreign matter, off-odour or off-taste, chilling injury, and food-safety contamination

Label-carrying rules:

- labels must be descriptive review context only
- labels must not be automatic pass/fail logic
- labels must not convert `crop_system_type` into product-form scope
- labels must not turn aroma into deterministic runtime logic
- labels must not imply an observed saleable mass exists

## 9. What Must Not Be Inferred

Do not infer or calculate:

- `saleable_harvest_mass_kg` from standing biomass
- `saleable_harvest_mass_kg` from daily biomass gain
- `saleable_harvest_mass_kg` from plant count
- observed saleable mass from gross harvested mass
- observed saleable mass from modeled saleable mass
- revenue from ontology labels
- shrink from ontology labels
- penalty rates from ontology labels
- saleability rates from ontology labels
- buyer acceptance from ontology labels
- product form, pricing path, saleability status, or buyer acceptance from `crop_system_type`
- aroma pass/fail status from runtime fields or ontology labels

## 10. Candidate Adapter Approaches

| adapter approach | value | risk | readiness | current judgment |
|---|---:|---|---|---|
| Keep only `saleable_harvest_mass_kg: null` | 8 | low | ready now | Best current behavior. It preserves the required field, keeps the blocker visible, and avoids unsupported inference. |
| Add a descriptive null-status or basis note later | 8 | low | needs design | Good smallest future adapter enhancement if metadata shape is approved. It should describe why the value is null without changing the business field or schema. |
| Add future ontology-label arrays later | 6 | medium | needs design | Useful as review context after label placement is designed. Risk is misuse as pass/fail, pricing, shrink, or acceptance logic. |
| Wait for runtime-native harvest output | 9 | medium | blocked | Strongest long-term solution, but unavailable now because runtime does not emit observed saleable harvest mass. This should stay separate from the adapter null-status pass. |

## 11. Recommended Smallest Future Adapter Implementation Surface

The smallest safe future adapter implementation surface is a metadata-only null-status enhancement around the existing adapter payload, not a new top-level business field and not a schema-wide ontology-label integration.

Recommended future surface:

- keep `saleable_harvest_mass_kg` as the existing top-level business field
- keep its value `null` when no observed or reviewed value exists
- add one descriptive metadata note only if a later implementation pass approves the payload shape
- keep ontology labels out of calculations and out of business consumer logic
- do not require ontology, runtime, canonical business, or schema changes

## 12. Later Implementation Candidate Files

A later explicitly approved implementation pass might touch only a narrow set such as:

- `scripts/build_first_slice_adapter_payload.py`
- `scripts/example_first_slice_overrides.json`
- `scripts/example_first_slice_reviewed_manual_overrides.json`
- generated first-slice adapter payload examples or fixtures, if a later pass creates or refreshes them
- a follow-up docs note describing the implemented adapter payload shape

Files that should remain out of that later adapter implementation unless separately approved:

- `data/knowledge/**`
- `data/simulation/**` as source-of-truth
- `src/**`
- ontology files
- runtime producers
- canonical business rules

## 13. Validation for a Later Implementation Pass

Later validation should confirm:

- payload JSON still contains `saleable_harvest_mass_kg`
- absent observed or reviewed input still emits `saleable_harvest_mass_kg: null`
- a null-status note, if added, is metadata-only and does not become a business input
- no ontology label is used to compute mass, revenue, shrink, penalties, buyer acceptance, or saleability rate
- `crop_system_type` remains context-only
- product-form labels remain separate from `crop_system_type`
- aroma remains manual-review only
- modeled saleable mass is not treated as observed saleable mass
- generated examples or fixtures match the approved payload shape
- changed-path checks show no edits under `data/knowledge/**`, `data/simulation/**`, `src/**`, or unapproved runtime/script surfaces

Minimum command checks for a later adapter implementation pass should include:

- `git --no-pager diff -- scripts/build_first_slice_adapter_payload.py`
- `git --no-pager diff --name-only -- data/knowledge data/simulation src`
- `git --no-pager diff --name-only -- scripts`
- `git status --short`
- a payload-generation command using the current first-slice scenario and null override file, if the runtime artifact is present

## 14. Blockers

- Runtime output still does not provide observed saleable harvest mass.
- No approved non-null reviewed-manual `saleable_harvest_mass_kg` value is currently present in the inspected examples.
- Runtime-native harvest output is blocked until a separate bounded runtime pass defines the producer path and source semantics.
- Business consumption is blocked until `saleable_harvest_mass_kg` is backed by observed runtime output or explicit reviewed manual input.
- Ontology-label arrays need separate adapter payload-shape design before implementation.

## 15. Recommended Next Action

- Keep current adapter behavior as `saleable_harvest_mass_kg: null` when no reviewed value exists.
- Treat the null as unresolved and review-blocking, not zero and not failed saleability.
- If implementation is requested next, start with the smallest metadata-only null-status enhancement in the adapter payload.
- Keep future ontology-label carrying conceptual until a later pass explicitly approves the adapter payload shape.
- Keep runtime-native harvest output as a separate later pass.
