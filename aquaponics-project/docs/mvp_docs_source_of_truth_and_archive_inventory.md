# MVP Docs Source-of-Truth and Archive Inventory

## 1. Purpose

Create a docs-only inventory of the Aquaponics MVP documentation layer before
any operating manual, archive restructuring, file moves, deletes, or renames.

This is a review artifact only. It does not modify existing docs, configs,
canonical knowledge, ontology, runtime output, source, scripts, tests, or
project configuration.

## 2. Scope

In scope:

- tracked docs under `docs/**`
- tracked policy/config files under `configs/**`
- status-only review of the MVP integrity runner
- status-only review of the current Mode A/P1/P1.5/P2a MVP implementation and
  demo examples
- source-of-truth, supporting, superseded, archive-candidate, do-not-move, and
  manual-review classification

Out of scope:

- file moves, deletes, renames, or archive implementation
- edits to existing docs
- edits to `configs/**`
- edits to `data/knowledge/**`, `data/simulation/**`, `src/**`,
  `scripts/**`, `tests/**`, or configs
- code diffs or implementation recommendations
- inferred numeric values
- inferred or populated `saleable_harvest_mass_kg`
- promotion of scenario assumptions into canon

## 3. Inputs Reviewed

Commands and inventories reviewed:

- `python scripts/check_mvp_integrity.py`
- `git ls-files docs`
- `git ls-files configs`
- targeted text search across `docs`, `configs`, `src`, and `scripts`
- path-reference checks for tracked docs and configs

Current-state docs reviewed:

- `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- `docs/mvp_current_progress_map_update_spec.md`
- `docs/mvp_operating_cost_pressure_design.md`
- `docs/mvp_strategic_alignment_review_packet_for_pro.md`
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`

Policy/config files reviewed:

- `configs/allowlist.yaml`
- `configs/contradiction_policy.yaml`
- `configs/evidence_policy.yaml`
- `configs/first_slice_bridge_baselines.yaml`
- `configs/model_policy.yaml`
- `configs/promotion_policy.yaml`
- `configs/rejection_rules.yaml`
- `configs/source_registry.yaml`

Status-only implementation references reviewed:

- `scripts/check_mvp_integrity.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `scripts/example_mvp_mode_a_p1_water_quality_inputs.json`
- `scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json`
- `scripts/example_mvp_mode_a_p2a_operating_cost_inputs.json`
- `src/feed_waste_tan_loads.py`
- `src/mvp_tan_nh3_risk.py`
- `src/mvp_aeration_solids_context.py`
- `src/mvp_operating_cost_pressure.py`
- `src/mvp_mode_a_feed_load_report.py`

## 4. Integrity Snapshot Runner Result

The requested command was attempted first as:

```powershell
python scripts/check_mvp_integrity.py
```

The first sandboxed attempt failed because `python.exe` could not be accessed
by the system. The approved rerun outside that sandbox passed:

```text
MVP INTEGRITY SNAPSHOT - PASS
Mode: full
Commit: 20e016d
Compile: PASS
Tests: PASS
Demos: PASS
Expected values: PASS
Forbidden keys: NONE FOUND
Protected paths: CLEAN
Git status: clean
```

Latest verified demo values from the runner:

- TAN-N load: `29.44 g/day`
- O2 demand: `134.5408 g/day`
- alkalinity demand: `210.2016 g CaCO3/day`
- TAN-N concentration: `3.7743589743589743 mg/L`
- NH3-N: `0.026311377265059072 mg/L`
- NH3: `0.031949529536143155 mg/L`
- dry-solids potential: `0.25 kg/day`
- feed cost: `45.0 INR/day`
- power cost: `54.0 INR/day`
- selected cost-pressure subtotal: `99.0 INR/day`

Guardrails reported by the runner:

- no safety claims
- no revenue/profitability claims
- no total operating cost
- no `saleable_harvest_mass_kg`

## 5. Current MVP Truth Baseline

Current MVP spine:

- Mode A direct feed input remains the load-only base.
- P1 adds TAN-N concentration and NH3 chemistry context only with complete
  water-volume, time, pH, temperature, and freshwater inputs.
- P1.5 adds aeration and solids context without aeration adequacy, total oxygen
  demand, wet sludge, TSS, or solids-removal claims.
- P2a adds selected feed and electricity operating-cost pressure from explicit
  scenario/business inputs.

Current verified demo path:

1. Mode A load-only report.
2. P1 TAN-N/NH3 water-quality context report.
3. P1.5 aeration/solids context report.
4. P2a selected feed + electricity operating-cost pressure report.

Current blocked claims:

- no fish safety
- no system safety
- no aeration adequacy
- no total oxygen demand
- no solids-removal capacity
- no total operating cost
- no revenue
- no profitability
- no fish revenue
- no basil revenue
- no basil saleable harvest claim

Current basil boundary:

- `saleable_harvest_mass_kg` remains unresolved/null unless observed or
  explicitly reviewed.
- Standing biomass, daily gain, plant count, readiness labels, and feed/water
  outputs must not be used as saleable harvest mass.

## 6. Config/Policy Inventory

| path | title or inferred role | classification | current relevance | superseded by | stale reason | archive safety | external reuse risk | operating manual reference priority | notes |
|---|---|---|---|---|---|---|---|---|---|
| `configs/allowlist.yaml` | trusted-source domain tiers | `policy_or_config_reference` | Source trust filtering for research/evidence workflow. | none | none found | keep in place | low | medium | Policy reference, not MVP status truth. |
| `configs/contradiction_policy.yaml` | contradiction normalization and severity rules | `policy_or_config_reference` | Defines contradiction ticket behavior and no auto-promotion for severity 2+. | none | none found | keep in place | low | medium | Should be referenced by research/evidence review guidance. |
| `configs/evidence_policy.yaml` | evidence levels and confidence rules | `policy_or_config_reference` | Defines E0-E5 evidence scoring and confidence conditions. | none | none found | keep in place | low | medium | Operating manual should reference rather than duplicate. |
| `configs/first_slice_bridge_baselines.yaml` | tracked non-canonical bridge baseline config | `policy_or_config_reference` | Current durable source for `starter_tilapia_basil_system -> crop_system_type = architecture_dwc_raft`. | none | none found | do not move | medium | high | Referenced by bridge docs and `scripts/materialize_first_slice_bridge.py`. |
| `configs/model_policy.yaml` | model-use policy by research workflow stage | `policy_or_config_reference` | Guides discovery/filter/acquire/extract/review/merge/conflict-resolution automation. | none | model names may drift over time | manual review before external reuse | medium | low | Useful governance reference, not MVP demo truth. |
| `configs/promotion_policy.yaml` | candidate/provisional/accepted promotion gates | `policy_or_config_reference` | Prevents premature canon promotion and defines human gates. | none | none found | keep in place | low | medium | Important for future prompt library guardrails. |
| `configs/rejection_rules.yaml` | source rejection and metadata-only rules | `policy_or_config_reference` | Supports source filtering and paywall handling. | none | none found | keep in place | low | medium | Reference from research workflow, not MVP manual body text. |
| `configs/source_registry.yaml` | citable source registry | `policy_or_config_reference` | Tracks source IDs, trust status, and limitations. | none | registry completeness may drift | do not archive | medium | medium | Large policy/source reference; avoid copying into operating manual. |

## 7. Current Source-of-Truth Docs

Minimum current source-of-truth set:

| path | title or inferred role | classification | current relevance | superseded by | stale reason | archive safety | external reuse risk | operating manual reference priority | notes |
|---|---|---|---|---|---|---|---|---|---|
| `docs/mvp_current_truths_terminology_and_loophole_audit.md` | current MVP truth, terminology, guardrail, and freshness audit | `current_source_of_truth` | Primary current-state anchor for Mode A/P1/P1.5/P2a, latest demo values, blocked claims, and stale-doc handling. | none | none found | do not move | low | high | Treat as the top current MVP truth doc until replaced by a later current-state audit. |
| `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md` | four-level customer/advisor demo walkthrough | `current_source_of_truth` | Current demo script and explanation for load-only, P1, P1.5, and P2a. | none | none found | do not move | low | high | Operating manual should reference this for demo flow, not reprint all values. |
| `docs/mvp_current_progress_map_update_spec.md` | current progress-map update spec | `current_source_of_truth` | Current visual/progress framing showing P2a integration as built and revenue/profitability as future. | none | four-level walkthrough now exists, but spec remains aligned | do not move before visual/manual work | medium | medium | Source for progress map copy and guardrail chips. |
| `docs/business_layer_contract.md` | normative business-layer contract | `current_source_of_truth` | Business contract for later economics, null propagation, and required upstream fields. | none | current MVP demo intentionally does not satisfy full revenue/profit contract | do not move | medium | high | Do not use it to claim current revenue; use as boundary and future contract. |
| `docs/business_layer_plan.md` | phased business-layer plan | `current_source_of_truth` | Defines business-layer phases, placeholder policy, deferred paths, and non-goals. | none | some first-slice progress has advanced since creation | do not move | medium | medium | Reference for business guardrails; avoid duplicating phase tables in manual. |
| `docs/first_vertical_slice_choice.md` | chosen first business slice | `current_source_of_truth` | Establishes `basil bulk kg wholesale` as the first narrow business slice and names `saleable_harvest_mass_kg` as the bridge-required field. | none | first-slice proof remains incomplete | do not move | medium | medium | Important first-slice truth, but not a claim that revenue is implemented. |
| `docs/first_slice_adapter_saleable_harvest_null_status_design.md` | saleable harvest null-status design | `current_source_of_truth` | Current source for keeping `saleable_harvest_mass_kg: null` unresolved without observed or reviewed input. | none | none found | do not move | low | high | Key guardrail for avoiding basil revenue/saleability overclaim. |
| `docs/first_slice_harvest_saleability_runtime_output_alignment.md` | ontology-to-runtime/adapter alignment note | `current_source_of_truth` | Current source for keeping ontology labels qualitative and non-computational. | none | no implementation yet | do not move | medium | high | Reference from manual for saleability boundary; do not duplicate ontology label lists. |

## 8. Current Supporting Docs

| path | title or inferred role | classification | current relevance | superseded by | stale reason | archive safety | external reuse risk | operating manual reference priority | notes |
|---|---|---|---|---|---|---|---|---|---|
| `docs/automation_candidates.md` | automation-candidate register | `current_supporting` | Supports governance for repeated checks and helper decisions. | none | dated before integrity runner, but still directionally useful | keep in place | medium | low | Useful for prompt/library design, not MVP truth. |
| `docs/decision_rule_research_simulation_business_audit.md` | work-type decision rule | `do_not_move` | AGENTS-level reference for deciding research vs simulation vs business vs repo audit. | none | none found | do not move | low | high | Operating manual should link this directly. |
| `docs/first_slice_adapter_spec.md` | first-slice adapter prep spec | `current_supporting` | Defines thin adapter outputs and missing/deferred fields for `basil bulk kg wholesale`. | none | implementation may have moved ahead in scripts | do not move before adapter manual | medium | medium | Good reference for adapter boundary. |
| `docs/first_slice_architecture_runtime_plan.md` | architecture/runtime bridge planning | `current_supporting` | Supports `crop_system_type` bridge context. | bridge config and materialization docs for some details | earlier planning state | move only after reference check | medium | low | Useful history for why architecture context was added. |
| `docs/first_slice_assumption_review.md` | first-slice working assumption review | `current_supporting` | Flags constructed assumptions and keeps saleable mass null. | none | assumptions need review before external reuse | manual review before external reuse | high | low | Do not cite externally as final economics. |
| `docs/first_slice_basil_harvest_readiness_and_saleability_spec.md` | non-canon basil readiness/saleability reference spec | `current_supporting` | Supports saleability vocabulary and manual-review boundaries. | ontology/alignment docs for current implementation boundary | not current MVP demo status | do not move before saleability ref check | medium | medium | Keep non-canon wording; do not use as hard buyer grade. |
| `docs/first_slice_basil_harvest_saleability_promotion_candidate_map.md` | saleability promotion candidate map | `current_supporting` | Preserves do-not-promote and candidate classifications. | ontology apply/alignment docs for accepted labels | earlier review phase | move only after reference check | medium | low | Useful audit trail for why not all claims entered canon. |
| `docs/first_slice_bridge_design.md` | first-slice bridge design | `current_supporting` | Explains why `crop_system_type` is the first bridge and not a pricing selector. | materialization contract/config for operational source | some details implemented | move only after reference check | medium | medium | Reference for architecture-context boundary. |
| `docs/first_slice_bridge_materialization_contract.md` | bridge materialization contract | `current_supporting` | Defines `configs/first_slice_bridge_baselines.yaml` as tracked source and narrow materialization target. | none | none found | do not move before helper/manual docs | medium | medium | Important because config is referenced by script. |
| `docs/first_slice_bridge_regeneration_validation.md` | bridge regeneration validation record | `current_supporting` | Records that `crop_system_type` propagated through runtime validation. | none | validation snapshot may age | keep until next validation replaces it | medium | low | Useful history; not a current runtime source. |
| `docs/first_slice_bridge_tracked_source_decision.md` | bridge tracked-source decision | `current_supporting` | Justifies `configs/first_slice_bridge_baselines.yaml` as non-canonical tracked config. | none | decision implemented | move only after reference check | medium | low | Useful provenance for config ownership. |
| `docs/first_slice_cost_build_up_review.md` | cost build-up review | `current_supporting` | Supports first-slice cost assumption review. | none | may contain constructed working values | manual review before external reuse | high | low | Do not use as final cost truth. |
| `docs/first_slice_doc_consistency_sweep.md` | first-slice doc consistency sweep | `current_supporting` | Audits consistency across first-slice docs. | current inventory for MVP doc archive posture | older than this inventory | safe to archive later after reference update | medium | low | This inventory supersedes it for archive planning only. |
| `docs/first_slice_method_comparison.md` | first-slice method comparison | `current_supporting` | Compares methods and supporting docs for first-slice work. | none | may predate later bridge decisions | manual review before move | medium | low | Keep until operating manual references are settled. |
| `docs/first_slice_recurring_maintenance_plan.md` | recurring maintenance plan | `current_supporting` | Supports maintenance of first-slice docs/checks. | none | may need update after integrity runner | manual review before external reuse | medium | low | Supporting process note. |
| `docs/first_slice_repo_audit.md` | first-slice repo audit | `current_supporting` | Useful audit history for first-slice boundaries and references. | later targeted audits for specific topics | older snapshot | move only after reference check | medium | low | Heavily referenced by first-slice docs. |
| `docs/first_slice_reviewed_manual_harvest_value_approval_packet.md` | manual harvest value approval packet | `current_supporting` | Supports possible reviewed-manual path for non-null saleable mass. | none | no current approved non-null value | manual review before reuse | high | low | Do not imply saleable mass has been approved. |
| `docs/first_slice_reviewed_manual_run_note.md` | reviewed manual run note | `current_supporting` | Records reviewed manual run context. | none | review-run specific | manual review before reuse | high | low | History only unless explicitly refreshed. |
| `docs/first_slice_runtime_native_harvest_output_plan.md` | runtime-native harvest output plan | `current_supporting` | Future path for observed saleable harvest output. | null-status/alignment docs for current blocker handling | design not implemented | do not move before saleability ref check | medium | medium | Important future boundary but not current implementation truth. |
| `docs/first_slice_syntax_and_smoke_check.md` | first-slice syntax/smoke check record | `current_supporting` | Historical validation support for first-slice docs/configs. | integrity runner for MVP checks | narrower/older validation scope | safe to archive later after reference update | low | low | Keep until second archive pass checks references. |
| `docs/glossary_link_candidates_helper.md` | glossary link helper note | `current_supporting` | Supports vault/glossary maintenance, not current MVP truth. | none | outside current MVP path | safe to archive or relocate later | low | none | Low priority for operating manual. |
| `docs/layer_status_snapshot.md` | layer readiness snapshot | `needs_manual_review` | Broad layer status useful as context but not current MVP truth. | current MVP truth audit for MVP status | focused on older first vertical slice readiness | manual review before reuse | high | low | Risky externally because percentages are planning judgments. |
| `docs/mvp_operating_cost_pressure_design.md` | P2a/P2c operating-cost pressure design | `current_supporting` | Design provenance for P2a and future P2c; current implementation covers feed/electricity P2a only. | four-level walkthrough/current truth audit for current status | early sections say current MVP did not calculate cost before P2a implementation | do not move before references are updated | medium | medium | Use for design rules, not as current implementation status. |
| `docs/mvp_p1_5_aeration_solids_design.md` | P1.5 aeration/solids design | `current_supporting` | Design provenance for current P1.5 helper and report integration. | current truth audit for implementation state | implementation now exists | do not move before references are updated | medium | medium | Useful for boundary definitions. |
| `docs/mvp_p1_tan_concentration_nh3_risk_design.md` | P1 TAN/NH3 design | `current_supporting` | Design provenance for current P1 helper and report integration. | current truth audit for implementation state | implementation now exists | do not move before references are updated | medium | medium | Useful for load/concentration/NH3 separation. |
| `docs/mvp_tilapia_feed_research_ingestion_review.md` | Mode A tilapia feed research review | `current_supporting` | Evidence provenance supporting Mode A direct feed path. | current truth audit for current implementation state | older research ingestion state | move only after reference check | medium | low | Keep as research history, not current demo status. |
| `docs/runtime_field_inventory.md` | runtime field inventory | `current_supporting` | Supports runtime-to-business mapping and missing `saleable_harvest_mass_kg` blocker. | runtime-to-business audit for first-slice mapping | broader/older inventory | move only after reference check | medium | low | Good implementation reference, not MVP demo truth. |
| `docs/runtime_to_business_field_audit.md` | runtime-to-business field audit | `current_supporting` | Current first-slice mapping audit and saleable mass blocker documentation. | none | no adapter implementation in this note | do not move before adapter/manual work | medium | medium | Important reference for first-slice business boundary. |
| `docs/saleable_harvest_mass_bridge_decision.md` | saleable harvest mass bridge decision | `current_supporting` | Supports manual reviewed input or null bridge decision. | null-status design for current adapter wording | older than null-status design | move only after reference check | medium | medium | Use as bridge history; null-status design is sharper current anchor. |

## 9. Historical or Superseded Docs

| path | title or inferred role | classification | current relevance | superseded by | stale reason | archive safety | external reuse risk | operating manual reference priority | notes |
|---|---|---|---|---|---|---|---|---|---|
| `docs/first_slice_adapter_crop_system_type_plan.md` | crop-system-type adapter plan | `historical_superseded` | Earlier plan for `crop_system_type` handling. | bridge config/materialization docs and current runtime state | bridge path has advanced | archive candidate after reference check | medium | none | Keep until references are updated. |
| `docs/first_slice_basil_harvest_saleability_canon_apply_surface.md` | saleability canon apply surface | `historical_superseded` | Historical apply-surface decision for saleability vocabulary. | ontology apply result and runtime-output alignment note | ontology status moved on | archive candidate after reference check | medium | none | Do not use as current ontology state. |
| `docs/first_slice_basil_harvest_saleability_canonical_location_decision.md` | saleability canonical location decision | `historical_superseded` | Historical placement decision. | ontology apply result and alignment note | decision implemented/absorbed | archive candidate after reference check | medium | none | Keep as audit trail only. |
| `docs/first_slice_basil_harvest_saleability_minimal_vocabulary_design_plan.md` | saleability vocabulary design plan | `historical_superseded` | Earlier design for qualitative vocabulary. | ontology accepted qualitative entries and alignment note | design phase complete | archive candidate after reference check | medium | none | Do not cite as current vocabulary source. |
| `docs/first_slice_basil_harvest_saleability_vocabulary_ownership_apply_plan.md` | vocabulary ownership apply plan | `historical_superseded` | Historical apply plan. | ontology apply/alignment docs | apply phase complete | archive candidate after reference check | medium | none | Keep only for provenance. |
| `docs/first_slice_bridge_implementation_surface.md` | bridge implementation surface | `historical_superseded` | Earlier bridge implementation analysis. | materialization contract, regeneration validation, config | bridge implementation path chosen | archive candidate after reference check | medium | none | Do not use as current implementation instruction. |
| `docs/first_slice_bridge_persistence_decision.md` | bridge persistence decision | `historical_superseded` | Earlier persistence planning for bridge state. | tracked-source decision and config | tracked source selected | archive candidate after reference check | medium | none | Review references before moving. |
| `docs/first_slice_saleable_harvest_mass_plan.md` | saleable harvest mass plan | `historical_superseded` | Earlier plan for saleable mass handling. | null-status design and alignment note | sharper null-status boundary exists | archive candidate after reference check | high | none | High risk if reused to justify non-null mass. |
| `docs/first_slice_saleable_harvest_mass_run_path.md` | saleable harvest mass run path | `historical_superseded` | Earlier run-path note. | null-status design and runtime-output alignment note | current mass remains unresolved | archive candidate after reference check | high | none | Do not use externally unless labeled historical. |
| `docs/first_slice_working_input_pack.md` | first-slice working inputs | `historical_superseded` | Working input pack for early first-slice examples. | current null-status and assumption-review docs for boundaries | constructed inputs are not current truth | manual review before archive/reuse | high | none | Risky externally because it can look like approved economics. |
| `docs/knowledge_to_runtime_sync_plan.md` | knowledge-to-runtime sync plan | `needs_manual_review` | Older sync planning context. | current MVP and bridge docs for relevant current work | may predate bridge/config posture | manual review before move | medium | none | Check for hidden references before archive pass. |
| `docs/mvp_fish_feed_waste_tan_engine_design.md` | early MVP feed/waste/TAN design | `historical_superseded` | Origin design for Mode A load path. | current truth audit, implementation files, four-level walkthrough | implementation now exists and later layers were added | archive candidate only after reference/banner pass | high | low | Current truth audit already marks as historical. |
| `docs/mvp_mode_a_feed_load_customer_demo_walkthrough.md` | one-level Mode A demo walkthrough | `historical_superseded` | Historical first demo walkthrough. | four-level demo walkthrough | lacks P1/P1.5/P2a | archive candidate after historical banner | high | none | Risky externally because it under-represents current demo. |
| `docs/mvp_mode_a_feed_load_integration_surface_plan.md` | Mode A report integration plan | `historical_superseded` | Historical integration plan. | implemented report path and current truth audit | implementation exists | archive candidate after reference check | medium | none | Keep as provenance only. |
| `docs/mvp_mode_a_p1_p1_5_customer_demo_walkthrough.md` | three-level demo walkthrough | `historical_superseded` | Historical demo before P2a. | four-level demo walkthrough | lacks P2a selected cost-pressure layer | archive candidate after historical banner | high | none | High external reuse risk if mistaken as current demo. |
| `docs/mvp_strategic_alignment_review_packet_for_pro.md` | older strategic review packet | `historical_superseded` | Useful review history and Pro prompt material. | current truth audit and four-level walkthrough | contains older roadmap options before P1/P1.5/P2a completion | archive candidate after historical banner | high | low | Do not use as current roadmap status. |
| `docs/project_status_and_roadmap.md` | project status and roadmap | `needs_manual_review` | Broad project roadmap dated 2026-04-18. | current MVP truth audit for MVP status | predates current Mode A/P1/P1.5/P2a spine | manual review before external reuse | high | low | Keep in place until broad roadmap refresh. |
| `docs/repo_migration_plan.md` | repo migration plan | `needs_manual_review` | Migration history/planning context. | current repo contract and AGENTS rules | migration status unclear from this pass | manual review before archive | medium | none | Not MVP truth; check references before moving. |
| `docs/next_steps_backlog.md` | older next-steps backlog | `needs_manual_review` | Useful planning history but not current MVP operating truth. | current truth audit for MVP next action | backlog objective focused on earlier business vertical slice | manual review before external reuse | high | low | Needs refresh before being used as current roadmap. |

## 10. Archive Candidates

Best later archive candidates, after a second pass adds historical banners and
updates references:

- `docs/mvp_mode_a_feed_load_customer_demo_walkthrough.md`
- `docs/mvp_mode_a_p1_p1_5_customer_demo_walkthrough.md`
- `docs/mvp_mode_a_feed_load_integration_surface_plan.md`
- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_strategic_alignment_review_packet_for_pro.md`
- `docs/first_slice_basil_harvest_saleability_canon_apply_surface.md`
- `docs/first_slice_basil_harvest_saleability_canonical_location_decision.md`
- `docs/first_slice_basil_harvest_saleability_minimal_vocabulary_design_plan.md`
- `docs/first_slice_basil_harvest_saleability_vocabulary_ownership_apply_plan.md`
- `docs/first_slice_bridge_implementation_surface.md`
- `docs/first_slice_bridge_persistence_decision.md`
- `docs/first_slice_saleable_harvest_mass_plan.md`
- `docs/first_slice_saleable_harvest_mass_run_path.md`
- `docs/first_slice_working_input_pack.md`

Archive safety notes:

- Do not move any file in this pass.
- Do not move high-reference historical docs until references are checked and
  either updated or intentionally left pointing to archive paths.
- Add a historical/superseded banner before moving externally risky docs.
- Treat saleability and economics working-input docs as higher-risk than
  ordinary design history because they can be misread as approved saleable mass
  or business assumptions.

## 11. Do-Not-Move Docs

Do not move these until an explicit archive-move pass updates or confirms
references:

| path | reason |
|---|---|
| `docs/mvp_current_truths_terminology_and_loophole_audit.md` | Primary current source-of-truth anchor. |
| `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md` | Current customer/advisor walkthrough. |
| `docs/mvp_current_progress_map_update_spec.md` | Current progress-map source. |
| `docs/business_layer_contract.md` | Normative business-layer contract and heavily referenced. |
| `docs/business_layer_plan.md` | Business-layer plan and referenced by MVP/current docs. |
| `docs/decision_rule_research_simulation_business_audit.md` | AGENTS decision-rule reference. |
| `docs/first_vertical_slice_choice.md` | Current first-slice choice. |
| `docs/first_slice_adapter_saleable_harvest_null_status_design.md` | Current saleable-harvest null-status boundary. |
| `docs/first_slice_harvest_saleability_runtime_output_alignment.md` | Current runtime/adapter saleability alignment. |
| `docs/first_slice_adapter_spec.md` | Current adapter prep reference. |
| `docs/runtime_to_business_field_audit.md` | Current first-slice runtime-to-business mapping audit. |
| `docs/mvp_operating_cost_pressure_design.md` | Referenced design provenance for P2a/P2c. |
| `docs/mvp_p1_tan_concentration_nh3_risk_design.md` | Referenced P1 design provenance. |
| `docs/mvp_p1_5_aeration_solids_design.md` | Referenced P1.5 design provenance. |

Non-doc do-not-move references:

- `configs/first_slice_bridge_baselines.yaml`
- `scripts/check_mvp_integrity.py`
- current MVP helper/report files under `src/**` and demo files under
  `scripts/**`

## 12. Needs-Manual-Review Docs

These should remain in place until a second pass reviews whether they need a
banner, rewrite, or archive move:

- `docs/layer_status_snapshot.md`
- `docs/next_steps_backlog.md`
- `docs/project_status_and_roadmap.md`
- `docs/repo_migration_plan.md`
- `docs/knowledge_to_runtime_sync_plan.md`
- `docs/first_slice_working_input_pack.md`
- `docs/first_slice_assumption_review.md`
- `docs/first_slice_cost_build_up_review.md`
- `docs/first_slice_reviewed_manual_harvest_value_approval_packet.md`
- `docs/first_slice_reviewed_manual_run_note.md`

Main reason:

- These docs can be useful history or planning context, but they should not be
  reused externally as current MVP status, current economics, current roadmap,
  or approved saleable-harvest evidence without review.

## 13. External Reuse Risk Notes

Highest external reuse risk:

- older one-level and three-level walkthroughs can make the MVP look less
  current than it is
- older strategic/roadmap docs can imply P1/P1.5/P2a are still unbuilt or that
  old next-step options are current
- first-slice working inputs and cost reviews can look like approved economics
  unless clearly labeled as review-only
- saleable-harvest plans can be misread as authority to populate
  `saleable_harvest_mass_kg`

Reusable externally with low risk if framed correctly:

- `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- `docs/mvp_current_progress_map_update_spec.md`

Reusable only as internal references:

- policy/config files
- historical design docs
- first-slice saleability/bridge docs
- implementation and demo scripts

## 14. Recommended Future Docs Structure

Recommended future structure by role, not by immediate move command:

- current MVP truth:
  - current status/terminology audit
  - current four-level walkthrough
  - current progress-map spec
- operating manual:
  - short playbook that links to source docs and commands
  - no copied source tables unless necessary
- design provenance:
  - P1, P1.5, P2a, Mode A, and first-slice design history
- policy/config references:
  - keep machine-readable configs under `configs/**`
  - reference them from docs instead of duplicating them
- archive/history:
  - older walkthroughs
  - superseded implementation plans
  - older strategic packets and roadmap snapshots

Do not create the archive structure or move files in this pass.

## 15. Whether an Operating Manual Is Still Needed

Yes. This inventory does not replace an operating manual.

Reason:

- The inventory classifies docs and archive risk.
- It does not give a runnable operator/advisor workflow.
- It does not provide a stable daily command sequence, demo checklist, or
  decision playbook.
- It does not decide when to run integrity checks, when to use current docs,
  when to stop before revenue/profit claims, or how to select the next pass.

The operating manual should be short and reference-heavy.

## 16. What the Operating Manual Should Reference

The operating manual should reference, not duplicate:

- current MVP truth:
  - `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- demo flow:
  - `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- current visual/progress framing:
  - `docs/mvp_current_progress_map_update_spec.md`
- integrity check:
  - `scripts/check_mvp_integrity.py`
- work-type routing:
  - `docs/decision_rule_research_simulation_business_audit.md`
- business boundary:
  - `docs/business_layer_contract.md`
  - `docs/business_layer_plan.md`
- saleable-harvest null boundary:
  - `docs/first_slice_adapter_saleable_harvest_null_status_design.md`
  - `docs/first_slice_harvest_saleability_runtime_output_alignment.md`
- policy/config:
  - `configs/evidence_policy.yaml`
  - `configs/promotion_policy.yaml`
  - `configs/contradiction_policy.yaml`
  - `configs/rejection_rules.yaml`
  - `configs/source_registry.yaml`
  - `configs/first_slice_bridge_baselines.yaml`

The operating manual should not duplicate:

- long source-registry entries
- full evidence/promotion policies
- full demo JSON payloads
- historical design tables
- stale roadmap options
- saleability vocabulary lists unless a later manual section needs a short
  pointer

## 17. Recommended Archive-Move Strategy for a Later Pass

Later archive strategy:

1. Add historical/superseded banners to the highest-risk docs first.
2. Re-run path-reference checks for all archive candidates.
3. Split candidates into:
   - safe to move after reference updates
   - keep in place because current docs reference them
   - manual review before move
4. Move only a small batch per pass.
5. After each move, run focused reference checks and the MVP integrity snapshot.
6. Do not move policy/config files in the archive pass unless a separate config
   restructure is explicitly approved.
7. Do not move current source-of-truth docs until a replacement current-source
   bundle exists and references have been updated.

No exact `git mv` commands are proposed in this inventory.

## 18. Recommended Next Action

Recommended next action:

- Create a short operating manual / decision playbook that references the
  current source-of-truth docs above and uses the integrity runner as the
  pre-demo/pre-roadmap sanity check.

Recommended prompt-library references:

- Use this inventory for doc-selection and archive-risk prompts.
- Use `docs/mvp_current_truths_terminology_and_loophole_audit.md` for current
  MVP guardrails.
- Use `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md` for demo
  prompts.
- Use `docs/decision_rule_research_simulation_business_audit.md` for
  work-type routing prompts.
- Use policy/config files as references, not pasted policy text.
- Use null-status/saleability alignment docs for prompts that mention
  `saleable_harvest_mass_kg`.

Stop rules for the next pass:

- stop if operating-manual scope tries to move archive candidates
- stop if a prompt tries to infer basil saleable mass
- stop if a prompt turns P2a into total operating cost or profitability
- stop if a prompt uses historical docs as current status without checking this
  inventory and the current truth audit

