# MVP Operating Manual and Decision Playbook

## 1. Purpose

This manual is the stable starting point for current Aquaponics MVP planning,
repo work, review sessions, and prompt handoffs.

Use it to answer:

- what the current MVP can and cannot claim
- which docs to read first
- which integrity check to run
- which tool or workflow to use next
- when to stop because a claim is blocked

This manual intentionally references current source-of-truth docs instead of
duplicating their full tables, demo output, source registry, or policies.

## 2. What This Manual Is And Is Not

This manual is:

- a compact operating and decision playbook
- a current-state starting point for ChatGPT, Codex, Pro, Deep Research, and
  human planning sessions
- workflow guidance for using existing docs, demo commands, and integrity
  checks
- a guardrail summary for avoiding unsafe MVP claims

This manual is not:

- canon
- a config policy file
- a product spec
- an implementation design spec
- a source registry
- a replacement for `AGENTS.md`
- permission to edit runtime, canon, ontology, scripts, source, tests, or
  configs

If this manual conflicts with current source docs, re-check the source docs and
update this manual only in a separate docs-only pass.

## 3. How To Use This Manual

Start here before any MVP roadmap, demo, prompt-library, validation, or
implementation discussion.

Use this order:

1. Run or review the integrity snapshot if current repo state matters.
2. Read the current MVP state and guardrails in this manual.
3. Follow links to the source-of-truth docs for detail.
4. Use the decision gates to choose review, research, design, implementation,
   validation, or stop.
5. Keep stale docs as history unless the inventory says they are current.

Do not use this manual to justify new calculations, revenue, profitability,
safety, total operating cost, or basil saleable harvest claims.

## 4. Current MVP State

Current MVP spine:

- Mode A direct feed input
- P1 TAN-N concentration and NH3 chemistry context
- P1.5 aeration and solids context
- P2a selected feed and electricity operating-cost pressure

Current implemented helpers:

- `src/feed_waste_tan_loads.py`
- `src/mvp_tan_nh3_risk.py`
- `src/mvp_aeration_solids_context.py`
- `src/mvp_operating_cost_pressure.py`
- `src/mvp_mode_a_feed_load_report.py`

Current demo runner:

- `scripts/build_mvp_mode_a_feed_load_report.py`

Current integrity runner:

- `scripts/check_mvp_integrity.py`

Current basil boundary:

- `saleable_harvest_mass_kg` remains unresolved/null unless observed runtime
  output or explicit reviewed manual input exists.
- No MVP feed, water-quality, aeration, solids, or cost-pressure output may
  infer basil saleable harvest mass.

## 5. Four-Level Demo Path

Run the four demo levels in this order when demonstrating the current MVP:

1. Mode A load-only:
   `python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json`
2. P1 TAN-N/NH3 context:
   `python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_water_quality_inputs.json`
3. P1.5 aeration/solids context:
   `python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json`
4. P2a selected feed + electricity operating-cost pressure:
   `python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p2a_operating_cost_inputs.json`

Use `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md` for the current
script, output values, and customer/advisor wording.

## 6. Integrity Snapshot Runner Workflow

Use quick mode when:

- checking before a short discussion or prompt handoff
- confirming demo values and guardrails quickly
- deciding whether a planning session can rely on current repo state

Command:

```powershell
python scripts/check_mvp_integrity.py --quick
```

Use full mode when:

- before customer/advisor validation
- before roadmap or Pro review
- before or after implementation work
- before treating demo output as current in external-facing material
- whenever quick mode fails or looks surprising

Command:

```powershell
python scripts/check_mvp_integrity.py --full
```

`PASS` means the runner found the expected current MVP state for its configured
checks. It does not prove field validation, fish safety, system safety,
profitability, revenue, total operating cost, or basil saleable output.

`FAIL` means stop and inspect the failing section before using the repo for a
roadmap, demo, prompt-library, or validation decision. Do not work around a
failure by weakening guardrails.

After running the snapshot, paste back:

- title line and mode
- commit
- compile/test/demo/expected-values result
- forbidden-key result
- protected-path result
- git status block
- latest demo values
- full failure text if any section fails

## 7. Current Terminology

| term | current meaning |
|---|---|
| Mode A direct feed input | Scenario supplies `feed_kg_day` directly; no biomass-derived feeding. |
| TAN-N load | Ammonia nitrogen load from feed/protein in kg/day or g/day; not concentration. |
| TAN-N concentration | Estimated mg TAN-N/L only when water volume and time basis are supplied. |
| NH3 fraction | Dimensionless unionized ammonia fraction from pH and temperature. |
| NH3-N | Unionized ammonia expressed as nitrogen, mg NH3-N/L. |
| NH3 | Unionized ammonia molecule concentration, mg NH3/L, converted from NH3-N by `17/14`. |
| nitrification oxygen demand | Oxygen demand associated with nitrifying TAN-N; not total oxygen demand or aeration capacity. |
| measured DO context | Point/context dissolved oxygen measurement; not future safety proof. |
| dry-solids potential | Provisional feed-linked dry-solids estimate; not wet sludge, TSS, or removal capacity. |
| scenario feed cost | Feed cost calculated only from explicit feed price metadata. |
| scenario power cost | Equipment electricity cost calculated only from explicit equipment and tariff metadata. |
| selected operating-cost pressure subtotal | Sum of supplied calculable money categories only when currencies match; not total operating cost. |

## 8. Guardrails And Forbidden Claims

Do not claim:

- fish safety
- system safety
- aeration adequacy
- total oxygen demand
- solids-removal capacity
- total operating cost
- revenue
- profitability
- margin, ROI, payback, break-even, or economic viability
- basil saleable harvest mass

Do not infer:

- `saleable_harvest_mass_kg` from standing biomass, daily gain, plant count,
  harvest-readiness labels, saleability labels, or feed/water/cost outputs
- product form, pricing path, saleability status, buyer acceptance, or aroma
  pass/fail status from `crop_system_type`
- total cost from P2a selected cost pressure
- safety from TAN-N concentration, NH3 chemistry, or measured DO

Scenario/demo values are explicit inputs or outputs for the demo path. They are
not canon and must not become default business, biology, or model assumptions.

## 9. Source-Of-Truth Docs

Read these first for current MVP work:

- `docs/mvp_docs_source_of_truth_and_archive_inventory.md`
- `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- `docs/mvp_current_progress_map_update_spec.md`
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `docs/first_vertical_slice_choice.md`
- `docs/first_slice_adapter_saleable_harvest_null_status_design.md`
- `docs/first_slice_harvest_saleability_runtime_output_alignment.md`

Use the inventory to decide whether another doc is current, supporting,
historical, superseded, an archive candidate, do-not-move, or needs manual
review.

## 10. Config/Policy References

Config files are governance and policy references. This manual is workflow and
decision guidance.

Reference these when needed, but do not duplicate or edit them during ordinary
manual or prompt-library work:

- `configs/allowlist.yaml`: trusted-source domain tiers
- `configs/contradiction_policy.yaml`: contradiction normalization and ticket
  rules
- `configs/evidence_policy.yaml`: evidence levels and confidence rules
- `configs/first_slice_bridge_baselines.yaml`: tracked non-canonical bridge
  baseline for `crop_system_type`
- `configs/model_policy.yaml`: model-use policy by workflow stage
- `configs/promotion_policy.yaml`: candidate/provisional/accepted promotion
  gates
- `configs/rejection_rules.yaml`: source rejection and metadata-only rules
- `configs/source_registry.yaml`: citable source registry

Do not treat configs as prose docs to archive or rewrite unless a separate
config-governance pass explicitly approves that work.

## 11. Historical And Stale-Doc Handling

Older docs can be useful history. They should not be used as current truth
unless cross-checked against:

- this manual
- `docs/mvp_docs_source_of_truth_and_archive_inventory.md`
- `docs/mvp_current_truths_terminology_and_loophole_audit.md`

High-risk stale-doc categories:

- older one-level or three-level walkthroughs
- older roadmap or strategic review packets
- first-slice working-input and cost notes
- saleable-harvest planning notes that predate the current null-status boundary

Archive moves require a separate explicit archive pass. Do not move, delete,
rename, or archive files during ordinary MVP planning, manual, prompt-library,
or design passes.

## 12. Decision Gates

Validate with customers/advisors when:

- the integrity snapshot passes
- the current four-level walkthrough is enough for structured feedback
- the goal is to learn which outputs, labels, and inputs are credible or useful

Design first when:

- a new layer changes terminology, output shape, source-of-truth boundaries, or
  user-facing claims
- the work touches P2c, Mode B, seed-demo dashboard/report shape, harvest
  output, revenue, profitability, or business-consumer behavior

Implement only when:

- the design surface is narrow
- allowed files are explicit
- helper behavior and report integration boundaries are clear
- relevant tests or integrity checks are identified

Use deep research when:

- external evidence, cost inputs, parameter ranges, source trust, or
  context-dependent distinctions are needed
- a value might be promoted toward canon, provisional business assumptions, or
  reusable model structure

Use Pro when:

- strategic priority, roadmap sequencing, investor/advisor framing, or
  high-stakes synthesis needs a second strong review
- current options are plausible but tradeoffs are hard to rank

Stop when:

- a request needs fish/system safety, revenue, profitability, total operating
  cost, or basil saleable harvest claims that the current repo cannot support
- `saleable_harvest_mass_kg` would be inferred from proxies
- historical docs conflict with current truth
- implementation scope would touch protected files without explicit approval

## 13. Next-Step Decision Rules

If users value selected cost pressure most, consider a P2c design pass for
buffer, water, maintenance, or backup-power cost pressure. Do not implement
P2c before design.

If users value oxygen/solids most, deepen P1.5 design before adding new
outputs. Keep total oxygen demand, aeration capacity, and solids removal
blocked until required inputs and evidence are explicit.

If users need easier input setup, design a seed-demo dashboard or report view
around existing outputs and guardrails. Do not add calculations just to make
the dashboard look complete.

If users ask for biomass planning, design Mode B separately. Do not mix biomass
derived feeding into Mode A.

If users ask for revenue or profit, keep it blocked unless explicit revenue
inputs, complete-enough cost inputs, and an observed or reviewed non-null
saleable harvest source exist.

If users ask for basil saleability, use the null-status and runtime-output
alignment docs. Keep `saleable_harvest_mass_kg` null unless observed or
explicitly reviewed.

## 14. ChatGPT, Codex, Deep Research, And Pro Usage Rules

Use ChatGPT for:

- strategy and prioritization
- prompt drafting
- roadmap choices
- interpreting integrity snapshots
- deciding which source docs to read next

Use Codex for:

- repo inspection
- bounded file edits
- implementation
- validation commands
- tests
- diffs, git status, and commits when explicitly requested

Use Deep Research for:

- external evidence review
- source discovery
- parameter, cost, and policy research
- source-trust comparisons
- geography- or market-specific inputs

Use Pro for:

- high-stakes strategic synthesis
- roadmap review
- investor/advisor framing
- ranking plausible next moves after source docs and integrity results are
  available

## 15. Codex Workflow Rules

Default to review-first design before broad implementation.

Prefer this implementation sequence for MVP layers:

1. docs-only design or review map
2. isolated helper
3. helper tests
4. optional report integration
5. report/demo tests
6. walkthrough or manual update
7. full integrity snapshot

Do not integrate with simulation unless explicitly approved.

Do not modify `data/knowledge/**`, `data/simulation/**`, ontology files,
runtime files, `src/**`, `scripts/**`, `tests/**`, or configs unless the user
explicitly authorizes that scope.

Run `python scripts/check_mvp_integrity.py --full` before major roadmap
decisions, after implementation work, and before external-facing demo use.

Report:

- touched files
- exact diff or no-index diff summary for new untracked docs
- integrity snapshot result
- protected-path diff result
- git status
- no commit unless explicitly instructed

## 16. Definitions Of Done

Design doc done:

- scope and non-goals are explicit
- source docs and implementation references are named
- allowed and blocked claims are clear
- recommended smallest future surface is stated
- no implementation or protected-file edits occurred

Helper done:

- helper has a narrow responsibility
- inputs and outputs are explicit
- forbidden claims remain excluded
- focused tests pass
- full integrity snapshot passes when relevant

Report integration done:

- helper is called only under approved input conditions
- missing-context labels remain visible
- demo JSON remains deterministic
- focused tests and full integrity snapshot pass

Demo walkthrough done:

- commands are listed
- actual output values are current
- plain-language explanation blocks unsafe claims
- customer/advisor discovery questions are included or referenced

Validation plan done:

- target audience is named
- questions are scoped to feedback, not proof of safety or profit
- current demo path and guardrails are referenced
- capture format for feedback is clear

Archive inventory done:

- current source-of-truth docs are identified
- stale, superseded, historical, do-not-move, and manual-review docs are
  separated
- no move, delete, rename, or archive commands are proposed
- protected paths remain unchanged

## 17. Recommended Immediate Next Actions

Recommended next actions:

1. Build a reusable prompt library that references this manual, the inventory,
   the current-truth audit, and the four-level walkthrough.
2. Create a seed-demo dashboard/report design that presents existing outputs
   and guardrails without adding calculations.
3. Create a customer/advisor validation plan for the four-level demo.
4. Keep revenue, profitability, total operating cost, and basil saleable output
   blocked until explicit inputs and reviewed saleable harvest evidence exist.

Do not start archive moves, P2c implementation, Mode B implementation, revenue
work, or saleable-harvest population from this manual alone.

