# First Slice Basil Harvest Saleability Promotion Candidate Map

Status: `draft`

## Purpose

- Map promotion candidates from `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`.
- Separate possible later canon candidates from provisional notes, operator assumptions, runtime-output design guidance, open questions, and do-not-promote items.
- Keep this as a review-first map only. It does not propose canonical diffs or schema shapes.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- This pass compares candidate claims against current canon touchpoints only.
- This pass does not modify `data/knowledge/**`, `data/simulation/**`, `src/**`, or `scripts/**`.
- `saleable_harvest_mass_kg` remains unresolved.
- `crop_system_type` remains context only.
- Aroma remains manual-review only.
- Modeled saleable mass is not treated as observed saleable mass.

## Inputs Reviewed

Primary input:

- `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md`

Supporting inputs:

- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`
- `docs/first_slice_runtime_native_harvest_output_plan.md`
- `docs/first_slice_saleable_harvest_mass_plan.md`
- `docs/runtime_to_business_field_audit.md`
- `docs/first_slice_adapter_spec.md`
- `docs/first_slice_repo_audit.md`
- `docs/decision_rule_research_simulation_business_audit.md`

Canon touchpoints inspected for comparison only:

- `data/knowledge/species/plants/basil.json`
- `data/knowledge/models/plant_system_models.json`
- `data/knowledge/business/yield_to_revenue_rules.json`
- `data/knowledge/business/cost_models.json`
- `data/knowledge/business/labor_models.json`

Durable source-family labels used below:

- EU general marketing standard baseline for fresh produce
- Basilico Genovese PDO proxy
- UC Davis basil/herb postharvest guidance
- Rutgers fresh-market basil guidance
- 2023 Frontiers basil postharvest review
- FDA fresh culinary herb food-safety/handling guidance
- UVI aquaponic basil repeated-cut findings
- first-slice runtime/business support docs listed above

## Current Repo Truth

- `data/knowledge/species/plants/basil.json` is a starter species profile. It already includes chilling sensitivity and marketability-loss language, plus successive-cutting, Pythium, and multi-harvest deficiency stress notes. It does not currently contain a harvest-readiness, saleability, product-form, or rejection-reason vocabulary.
- `data/knowledge/models/plant_system_models.json` contains architecture and system-behavior models. It does not currently define basil harvest-readiness or saleability rules.
- `data/knowledge/business/yield_to_revenue_rules.json` contains `rule_basil_bulk_kg`, which requires `saleable_harvest_mass_kg` for kg-based basil revenue. It also keeps architecture output-form review advisory through `crop_system_type`.
- `data/knowledge/business/cost_models.json` and `data/knowledge/business/labor_models.json` contain deferred basil packaging and harvest/pack labor placeholders that depend on a future sale-unit basis. They do not resolve saleable basil mass or quality-review rules.
- The supporting docs consistently treat `saleable_harvest_mass_kg` as missing or unresolved in runtime output, with a reviewed-manual override path available but still paused at `null`.
- Current runtime-facing docs treat `crop_system_type` as present and useful context only, not a selector that activates architecture-conditioned pricing, product-form, or saleability logic.

## Promotion Candidate Table

| candidate claim | source basis | current canon touchpoint | classification | rationale | promotion blocker, if any | recommended next action |
|---|---|---|---|---|---|---|
| Fresh bulk-wholesale basil should be young vegetative, leafy, non-woody material with flower heads absent. | Primary spec and research report; Basilico Genovese PDO proxy; Rutgers fresh-market basil guidance; UC Davis basil/herb postharvest guidance. | `data/knowledge/species/plants/basil.json` has no harvest-readiness rule. | `possible_later_canonical_candidate` | Adds a new qualitative harvest-readiness concept; does not conflict with current basil canon. | Needs an explicit later canon pass and a reviewed way to represent manual harvest-readiness criteria without numeric thresholds. | Carry forward as a later evidence-canon candidate; do not apply now. |
| General marketability baseline: sound, clean, practically pest-free, no abnormal moisture, no foreign smell/taste, and transportable. | Primary spec and research report; EU general marketing standard baseline and guidance. | `data/knowledge/business/yield_to_revenue_rules.json` requires saleable basil kg but does not define acceptance basis. | `possible_later_canonical_candidate` | Adds a qualitative acceptance basis that could strengthen the meaning of saleable kg. | Requires saleability/rejection vocabulary before canon promotion; buyer-specific tolerances remain absent. | Keep as a strong later candidate for minimum acceptance language only. |
| Freshness, turgidity, cultivar-appropriate color, low decay, and low visible damage are basil saleability basics. | Primary spec and research report; EU baseline; UC Davis basil/herb postharvest guidance; Rutgers fresh-market basil guidance. | `data/knowledge/species/plants/basil.json` has chilling marketability-loss notes but no general freshness/turgidity quality screen. | `possible_later_canonical_candidate` | Adds a new manual-review saleability screen; partly reinforces existing marketability-loss context. | Needs manual-review semantics and defect vocabulary; must not become visual-only auto-acceptance logic. | Candidate for later qualitative canon review, not runtime logic. |
| Visible rejection categories include serious wilting, yellowing, browning/blackening, decay, pest issues, mechanical damage, foreign matter, off-odour/off-taste, and contamination. | Primary spec and research report; EU baseline; UC Davis basil/herb postharvest guidance; Rutgers fresh-market basil guidance; FDA fresh culinary herb guidance. | Canon has optional `cull_or_unsaleable_mass_kg` in business rules but no reason vocabulary. | `possible_later_canonical_candidate` | Adds a rejection-reason concept that could make saleable mass more auditable. | Requires new controlled vocabulary before canon; no buyer tolerance percentages are supported. | Later vocabulary pass only after explicit `apply`; keep as grouped qualitative reasons now. |
| Chilling injury can make basil non-saleable or reduce marketability. | Primary spec and research report; UC Davis basil/herb postharvest guidance; 2023 Frontiers basil postharvest review. | `data/knowledge/species/plants/basil.json` already states chilling sensitivity, marketability loss, and severe injury thresholds. | `possible_later_canonical_candidate` | Strengthens existing basil stress canon by connecting chilling injury to saleability review. | Do not add a new numeric injury-score threshold in this pass. | Later canon pass could add a qualitative saleability linkage if a quality vocabulary exists. |
| Food-safety contamination, including floodwater contact, is an exclusion reason independent of appearance. | Primary spec and research report; FDA fresh culinary herb food-safety/handling guidance. | No current canon touchpoint for basil saleability exclusions. | `possible_later_canonical_candidate` | Adds a compliance/QA exclusion concept outside biological appearance. | Requires explicit scenario fact or QA input; cannot be inferred from plant state. | Keep as a later exclusion-vocabulary candidate; block runtime inference. |
| Bulk-wholesale cut basil should remain distinct from RTU/RTE retail-packed, live-root, potted, and bunch-specific product forms. | Primary spec and research report; FDA fresh culinary herb guidance; 2023 Frontiers basil postharvest review; Basilico Genovese PDO proxy. | `rule_basil_bulk_kg` and `rule_basil_bunches_optional` exist; `rule_architecture_output_form_context` remains advisory. | `possible_later_canonical_candidate` | Strengthens current product-scope separation without changing current business rules. | Requires product-form vocabulary before canon; must not turn `crop_system_type` into an automatic product-form selector. | Later product-form review only; keep first slice fixed as bulk kg wholesale. |
| Regrowth reserve after cutting matters for repeated-cut basil readiness. | Primary spec and research report; Rutgers fresh-market basil guidance; UVI aquaponic basil repeated-cut findings. | `basil.json` already notes successive-cutting stress and Pythium risk; `labor_models.json` notes repeated harvest may affect basil labor. | `provisional_spec_only` | Requires a repeated-cut context split; it is not a universal wholesale buyer-grade rule. | Needs repeated-cut operations vocabulary and stronger context handling. | Keep in docs until a repeated-cut operations/canon pass is explicitly requested. |
| Slight post-dispatch loss of freshness or turgidity may still be acceptable. | Primary spec and research report; EU general marketing standard baseline. | No matching current canon location. | `provisional_spec_only` | Useful nuance against zero-tolerance logic, but not enough to define a repo-wide acceptance threshold. | Needs buyer or receiving-language support before canon. | Keep as docs-only review nuance. |
| Aroma acceptability matters to culinary basil saleability. | Primary spec and research report; UC Davis basil/herb postharvest guidance; Basilico Genovese PDO proxy. | No current canon touchpoint for aroma. | `provisional_spec_only` | Important but manual-review only; not runtime-observable with current outputs. | No standardized repo QA method or numeric aroma threshold. | Keep manual-review only; block deterministic runtime scoring. |
| Aquaponic repeated-cut stress can reduce marketable share. | Primary spec and research report; UVI aquaponic basil repeated-cut findings. | `basil.json` already notes Pythium and nutrient-deficiency risks under successive cutting. | `runtime_output_design_only` | Existing canon covers the stress mode; the saleable-share implication belongs to future model/output design, not direct canon promotion. | No accepted penalty curve or modeled-saleable-mass basis. | Use only to justify keeping cut biomass separate from accepted saleable mass in future design. |
| Gross harvested, observed accepted, observed rejected, and modeled saleable mass should remain separate concepts. | Primary spec and research report; EU baseline; UC Davis; FDA; UVI; first-slice runtime/business support docs. | Current business canon only requires `saleable_harvest_mass_kg`; supporting docs say runtime does not emit it. | `runtime_output_design_only` | This is an epistemic/output-design distinction, not a biology or business-rate claim. | Requires an explicit later runtime or adapter apply pass; no canonical field names or schema shapes are proposed here. | Preserve the distinction in future design discussions; do not promote as canon in this pass. |
| `saleable_harvest_mass_kg` must not be inferred from standing biomass, daily gain, plant count, or modeled saleability. | Primary spec; runtime-native harvest output plan; saleable harvest mass plan; adapter spec; repo audit. | `rule_basil_bulk_kg` requires the field, while support docs mark it missing/unresolved. | `do_not_promote` | Prevents hidden aliasing between state, modeled estimate, and observed commercial acceptance. | Blocked until observed runtime harvest output or explicit reviewed human approval exists. | Keep `saleable_harvest_mass_kg` unresolved and nullable. |
| Numeric harvest-size proxies such as height, leaf count, stem length, or node count may help operations. | Primary spec and research report; Texas A&M and Utah/Arizona extension heuristics as summarized in the report. | No current canon touchpoint. | `operator_assumption_only` | Useful grower context but too production-context dependent for repo canon. | No context-robust threshold across greenhouse, hydroponic, aquaponic, and field systems. | Keep as operator notes only; never promote one universal numeric threshold from this pass. |
| Storage and handling bands can inform operations or later model context. | Primary spec and research report; UC Davis basil/herb postharvest guidance; 2023 Frontiers review; Rutgers fresh-market basil guidance. | `basil.json` already has growth-temperature and chilling-stress values, but no postharvest handling contract. | `operator_assumption_only` | Strong handling guidance, but not a buyer acceptance rule and not proof of observed saleability. | Needs a separate postharvest handling context if later promoted; must not overwrite growth-temperature context. | Keep as operator/model-context guidance only. |
| Generic buyer tolerance thresholds for minor yellowing, wilt, stem breakage, leaf-size mix, or stem-to-leaf ratio are not yet established. | Primary spec and research report; explicit absence of high-trust bulk-wholesale buyer tolerance evidence. | No current canon touchpoint. | `open_question` | The source set supports minimum quality concepts but not precise defect tolerances. | Needs high-trust buyer, receiver, or audited sales evidence. | Leave open and blocked until stronger evidence exists. |
| Hard numeric harvest-height, leaf-count, stem-length, aroma-score, or buyer-defect tolerance thresholds should become canon now. | Primary spec says not to promote these; research report says evidence is context-dependent or unresolved. | No current canon touchpoint. | `do_not_promote` | Would flatten context-dependent evidence into universal numbers. | Stronger evidence and explicit later apply scope would be required; current pass blocks it. | Do not promote. |

## Candidates That May Later Strengthen Canon

- Young vegetative, non-flowering, leafy, non-woody harvest-readiness concept.
- General marketability baseline for soundness, cleanliness, pest freedom, lack of abnormal moisture, lack of foreign smell/taste, and transportability.
- Freshness/turgidity and visible defect screens as manual-review saleability basics.
- Qualitative rejection or exclusion reason groups, including chilling injury and food-safety contamination.
- Product-form distinction for bulk-wholesale cut basil versus RTU/RTE, live-root, potted, and bunch-specific forms.

Any promotion of these items would require a separate explicit `apply` pass against `data/knowledge/**`, with vocabulary and context choices reviewed before editing.

## Candidates That Should Stay Provisional/Docs-Only

- Regrowth-reserve logic for repeated-cut basil until repeated-cut operation context is formalized.
- Aroma acceptability until a practical manual QA method is defined; it remains manual-review only.
- Slight transit-related freshness or turgidity loss until buyer or receiving-language evidence supports a reusable threshold.
- General buyer tolerance language for minor visible defects until stronger bulk-wholesale buyer evidence exists.

## Runtime-Output Design Candidates Only

- Separate gross harvested mass, observed accepted saleable mass, observed rejected mass, and modeled saleable mass conceptually.
- Keep quality state distinct from commercial acceptance state.
- Keep modeled saleable mass distinct from observed saleable mass.
- Keep `saleable_harvest_mass_kg` unresolved unless backed by observed runtime harvest output or explicit reviewed human approval.
- Treat rejection reasons and acceptance basis as future output-design or vocabulary work only, not as canonical schema changes in this map.

## Operator Assumptions Only

- Numeric harvest-size proxies such as height, leaf count, stem length, and node count.
- Storage and handling bands used for operations or later model context.
- Harvest time-of-day preferences.
- Buyer-specific tolerance assumptions not supported by the reviewed source set.

## Open Questions Before Promotion

- Which controlled vocabulary, if any, should represent harvest-readiness, saleability basis, and rejection reasons?
- Is there a high-trust bulk-wholesale basil buyer or receiver spec for minor yellowing, minor wilt, stem breakage, leaf-size mix, or stem-to-leaf ratio?
- Can aroma acceptability be standardized as a practical manual QA method without pretending it is runtime-observable?
- Which repeated-cut aquaponic stress signals are stable enough for a later modeled saleability adjustment without inventing penalty numbers?
- How should slight transit-related freshness loss be represented without turning it into either automatic acceptance or automatic rejection?

## Do-Not-Promote Items

- One universal numeric harvest-height threshold.
- One universal leaf-count, stem-length, or node-count threshold.
- Deterministic runtime saleability logic based on aroma.
- Direct inference of `saleable_harvest_mass_kg` from standing biomass, daily biomass gain, plant count, or modeled saleability.
- Visual-only auto-acceptance that ignores aroma, handling history, contamination, or buyer review.
- Storage-temperature guidance as a direct buyer-acceptance rule.
- Buyer-grade tolerance thresholds or percentages not supported by the reviewed report.
- `crop_system_type` as an automatic product-form, pricing, or saleability selector.

## Contradictions or Tensions Found

- No direct contradiction was found with current canonical files.
- `saleable_harvest_mass_kg` is a live business requirement in `yield_to_revenue_rules.json`, but current runtime/support docs mark it missing and unresolved. This is an integration blocker, not a canon contradiction.
- `basil.json` already contains chilling and repeated-cut stress notes. The spec would extend those into saleability review concepts, but current canon lacks the quality vocabulary needed to do that safely.
- `rule_architecture_output_form_context` keeps architecture context advisory. Any attempt to use `crop_system_type` as a saleability or product-form selector would conflict with current first-slice posture.
- Current cost and labor canon contain deferred basil packaging and harvest/pack placeholders. The saleability spec does not resolve their sale-unit or labor-standard TODOs.

## Spec-Classification Tensions, if Any

- The source research report's evidence-strength table uses stronger wording for several items, including aroma, regrowth reserve, storage/handling bands, chilling injury, product-form distinction, and aquaponic repeated-cut failure risk. The current spec downgrades several of these to provisional, operator-assumption, or design-only status. This map keeps the downgraded posture where promotion would require new vocabulary, runtime output, QA method, or context split.
- Aroma has meaningful source support, but the source set does not provide a repeatable numeric or runtime-observable standard. The map therefore keeps aroma as `provisional_spec_only` and manual-review only.
- Storage/handling evidence is strong for postharvest operations, but the spec correctly avoids treating it as a wholesale buyer-grade rule. The map keeps it as `operator_assumption_only`.
- Repeated-cut regrowth reserve is stronger in repeated-cut operations than in wholesale saleability. The map keeps it `provisional_spec_only` until repeated-cut context is represented explicitly.
- The source report proposes example field-name directions for future output design. This map treats those as conceptual design guidance only and does not propose final canonical field names or schema shapes.

## Recommended Next Action

- Keep this map as a docs-only review artifact.
- Do not promote anything into `data/knowledge/**` from this pass.
- Use a later explicit `apply` pass only if the target is scoped to one of:
  - qualitative harvest-readiness and saleability concepts
  - rejection/exclusion vocabulary
  - product-form scope vocabulary
  - qualitative chilling-to-saleability linkage
- Keep runtime-output separation work in runtime or adapter planning, not canonical biology or business files.
- Keep `saleable_harvest_mass_kg` unresolved until observed runtime harvest output or explicit reviewed human approval exists.
- Keep numeric thresholds, aroma scoring, buyer tolerances, and saleability penalties blocked until stronger evidence exists.
