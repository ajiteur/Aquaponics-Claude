# MVP Prompt Library

## 1. Purpose

This library provides reusable prompt templates for Aquaponics MVP work so
ChatGPT, Codex, Deep Research, and Pro reviews can start from stable guardrails
instead of long one-off prompts.

This is a coordination document only. It is not a new operating manual, product
spec, canonical source, implementation plan, or approval to change files.

## 2. Relationship to the operating manual

Use `docs/mvp_operating_manual_decision_playbook.md` as the workflow anchor.
This library references that manual and the current truth docs instead of
duplicating their full content.

For current MVP state, cross-check:

- `docs/mvp_operating_manual_decision_playbook.md`
- `docs/mvp_docs_source_of_truth_and_archive_inventory.md`
- `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- `docs/mvp_current_progress_map_update_spec.md`

Implementation files may be inspected only to verify current state, commands,
field names, and boundaries. Inspection is not approval to edit them.

## 3. Before using any prompt: integrity snapshot workflow

Run an integrity snapshot before using any template for repo-grounded work.

Use quick mode for short planning, prompt handoff, current-state discussion, or
preflight checks:

```powershell
python scripts/check_mvp_integrity.py --quick
```

Use full mode before customer/advisor validation, Pro review, roadmap decisions,
implementation passes, report/demo integration, or external-facing demo use:

```powershell
python scripts/check_mvp_integrity.py --full
```

If the snapshot fails or looks surprising, stop. Do not weaken guardrails, skip
blocked-claim checks, or treat stale docs as current truth.

## 4. Current MVP baseline to preserve

- MVP spine: Mode A + P1 + P1.5 + P2a.
- Demo path:
  1. Mode A load-only.
  2. P1 TAN-N/NH3 context.
  3. P1.5 aeration/solids context.
  4. P2a selected feed + electricity operating-cost pressure.
- Current runner commands:
  - `python scripts/check_mvp_integrity.py --quick`
  - `python scripts/check_mvp_integrity.py --full`
- `saleable_harvest_mass_kg` remains unresolved/null unless observed or
  explicitly reviewed.
- No fish safety, system safety, revenue, profitability, total operating cost,
  or basil saleable harvest claims are allowed.
- P2a is selected operating-cost pressure from explicit feed and electricity
  inputs, not total operating cost.

## 5. Prompt template index

| Template | Primary tool | Typical output |
| --- | --- | --- |
| Strategic ChatGPT checkpoint | ChatGPT | Decision framing and next action |
| Current-truths / loophole audit | Codex or ChatGPT | Guardrail audit |
| Docs-only design pass | Codex | One scoped docs diff |
| Isolated helper implementation pass | Codex | Narrow helper and tests |
| Report integration pass | Codex | Report/demo integration diff |
| Demo walkthrough pass | Codex or ChatGPT | Demo script and wording |
| Customer/advisor validation plan | ChatGPT or Pro | Interview plan |
| Seed-demo dashboard/report design | ChatGPT or Codex | Visual/report design doc |
| Deep research request | Deep Research | Cited external evidence |
| Research ingestion review | Codex or ChatGPT | Promotion map or draft |
| Source-of-truth/archive inventory | Codex | Inventory and classifications |
| Obsidian pointer note | Codex | Minimal vault pointer note |
| Local helper/script creation pass | Codex | Script/helper and tests |
| Pro model strategic review | Pro | Ranked strategic review |
| Decision record / roadmap checkpoint | ChatGPT or Codex | Decision record |
| Archive-move pass, review-first then apply | Codex | Review map, then scoped moves |
| Prompt-library update pass | Codex | Library-only docs diff |

## 6. Tool routing: ChatGPT versus Codex versus Deep Research versus Pro

- ChatGPT: strategy, prompt drafting, checkpoint thinking, validation-plan
  shaping, and interpreting integrity snapshots.
- Codex: repo inspection, bounded edits, tests, validation commands, exact
  diffs, git status, and commits only when explicitly authorized.
- Deep Research: external evidence discovery, source comparison, geography or
  market research, and citation-backed research reports.
- Pro: high-stakes strategic synthesis, roadmap review, advisor/investor
  framing, and ranked next decisions after source docs and integrity results are
  available.

## 7. Template: strategic ChatGPT checkpoint

```text
You are helping with the Aquaponics MVP. Use the current integrity snapshot and
the operating manual as the baseline.

When to use it: Before choosing <NEXT_DECISION>.
Purpose: Rank options without changing repo files.
Allowed file changes: None.
Inputs to inspect: integrity snapshot, docs/mvp_operating_manual_decision_playbook.md,
docs/mvp_current_truths_terminology_and_loophole_audit.md, <TARGET_DOC>.
Hard rules: Preserve Mode A + P1 + P1.5 + P2a; block <BLOCKED_CLAIMS>; do not infer
saleable_harvest_mass_kg; do not promote scenario assumptions into canon.
Validation requirements: Require quick or full integrity result from the requester.
Required output format: state summary, ranked options, recommended next action,
blocked claims, open questions.
Stop rules: Stop if current truth conflicts with the operating manual or if
implementation scope is requested before review-first design.
```

## 8. Template: current-truths / loophole audit

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: When current MVP truth, terminology, or stale-doc risk is uncertain.
Purpose: Audit current claims and loopholes without implementing changes.
Allowed file changes: <ALLOWED_FILES> only, or none for review-only.
Inputs to inspect: operating manual, current-truth audit, source-of-truth inventory,
demo walkthrough, progress map spec, and current integrity snapshot.
Hard rules: No canon promotion; no simulation integration; no safety, revenue,
profitability, total operating cost, or basil saleable harvest claim.
Validation requirements: Run <VALIDATION_COMMANDS>; include protected-path diff if
Codex is used.
Required output format: findings by severity, stale-doc notes, blocked claims,
recommended handling, touched files, validation, git status.
Stop rules: Stop before editing unless the user explicitly says apply.
```

## 9. Template: docs-only design pass

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: When a design needs to be clarified before code exists.
Purpose: Produce or update <DESIGN_DOC> without implementation.
Allowed file changes: <DESIGN_DOC> only.
Inputs to inspect: operating manual, current-truth audit, relevant source-of-truth docs,
and any user-provided design brief.
Hard rules: Do not modify src, scripts, tests, configs, data/knowledge,
data/simulation, ontology, or knowledge-vault files; block <BLOCKED_CLAIMS>.
Validation requirements: Run <VALIDATION_COMMANDS>; show exact diff and status.
Required output format: summary, touched files, exact diff, design summary,
validation results, git status, no commit.
Stop rules: Stop if the design requires new calculations, canon changes, runtime
integration, or ambiguous stable naming.
```

## 10. Template: isolated helper implementation pass

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: After a design doc approves one bounded helper.
Purpose: Implement <HELPER_FILE> with focused coverage in <TEST_FILE>.
Allowed file changes: <HELPER_FILE> and <TEST_FILE> only.
Inputs to inspect: <DESIGN_DOC>, operating manual, existing adjacent helper patterns,
and current integrity snapshot.
Hard rules: No report integration, simulation integration, canon edits, business edits,
or blocked claims; no invented numeric defaults.
Validation requirements: Run focused tests plus python scripts/check_mvp_integrity.py
--full unless the user scopes validation differently.
Required output format: summary, touched files, exact diff, tests, integrity result,
protected-path diff, git status, no commit unless explicitly authorized with
<COMMIT_MESSAGE>.
Stop rules: Stop if helper scope needs schema, runtime, or canon changes not listed.
```

## 11. Template: report integration pass

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: After an isolated helper exists and report exposure is approved.
Purpose: Integrate approved helper output into <REPORT_BUILDER_FILE> and
<DEMO_INPUT_FILE> if explicitly allowed.
Allowed file changes: <REPORT_BUILDER_FILE>, <DEMO_INPUT_FILE>, <TEST_FILE>, and
<TARGET_DOC> only if listed in <ALLOWED_FILES>.
Inputs to inspect: helper file, helper tests, design doc, demo walkthrough, integrity
runner, and current report builder.
Hard rules: Do not add new calculations outside the approved helper; preserve labels
as context or pressure; block <BLOCKED_CLAIMS>.
Validation requirements: Run report tests, relevant demo command, and full integrity.
Required output format: summary, touched files, exact diff, demo output summary,
validation results, protected-path diff, git status, no commit.
Stop rules: Stop if report wording would imply safety, total cost, revenue,
profitability, or saleable harvest.
```

## 12. Template: demo walkthrough pass

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: Before customer/advisor use or after approved report changes.
Purpose: Keep <TARGET_DOC> aligned with the current four-level demo.
Allowed file changes: <TARGET_DOC> only.
Inputs to inspect: operating manual, demo walkthrough, progress map spec, integrity
snapshot, and any approved demo outputs.
Hard rules: Do not modify implementation files; do not present context as safety,
adequacy, total cost, revenue, or profit.
Validation requirements: Run <VALIDATION_COMMANDS>, normally quick before docs-only
work and full before external-facing demo use.
Required output format: summary, touched files, exact diff, walkthrough summary,
blocked claims, validation, git status, no commit.
Stop rules: Stop if new demo levels, new calculations, or external claims are needed.
```

## 13. Template: customer/advisor validation plan

```text
Use this as a planning prompt, not an implementation prompt.

When to use it: Before interviews, walkthroughs, or advisor calls.
Purpose: Create a validation plan for the current MVP demo path.
Allowed file changes: None unless <TARGET_DOC> is explicitly allowed.
Inputs to inspect: operating manual, current demo walkthrough, integrity snapshot,
and <NEXT_DECISION>.
Hard rules: Questions must test usefulness and clarity, not prove safety, revenue,
profitability, field validation, or basil saleability.
Validation requirements: Require full integrity before external-facing use.
Required output format: audience, session flow, questions, feedback rubric,
blocked claims, decision criteria, next action.
Stop rules: Stop if the plan depends on claims outside Mode A + P1 + P1.5 + P2a.
```

## 14. Template: seed-demo dashboard/report design

```text
Use this for design only. Do not implement UI, scripts, or calculations.

When to use it: When shaping a seed-demo dashboard, report, or visual summary.
Purpose: Design how to present the current four-level MVP clearly.
Allowed file changes: <DESIGN_DOC> only.
Inputs to inspect: operating manual, progress map spec, demo walkthrough, current
truth audit, and integrity snapshot.
Hard rules: Use context/pressure wording; do not claim product readiness, safety,
revenue, profitability, total operating cost, or saleable basil output.
Validation requirements: Run <VALIDATION_COMMANDS> if Codex edits docs; otherwise
state the integrity snapshot used.
Required output format: layout summary, sections, labels, guardrail chips,
blocked claims, validation needs, next decision.
Stop rules: Stop before code, assets, dashboard implementation, or new metrics.
```

## 15. Template: deep research request

```text
Use Deep Research for external evidence only.

When to use it: When an MVP question needs outside sources before repo changes.
Purpose: Produce <RESEARCH_REPORT> with source-backed findings and uncertainty.
Allowed file changes: None.
Inputs to inspect: research question, operating manual guardrails, source-of-truth
inventory, and relevant policy constraints supplied by the requester.
Hard rules: Do not promote evidence into canon; do not infer blocked MVP claims;
separate geography, scale, species, system type, and evidence confidence.
Validation requirements: Cite sources, separate direct evidence from inference, and
flag contradictions or unresolved claims.
Required output format: executive summary, source table, findings, applicability,
uncertainties, blocked claims, repo-ingestion recommendations.
Stop rules: Stop if sources cannot support the requested precision or if the answer
would require invented numbers.
```

## 16. Template: research ingestion review

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: After <RESEARCH_REPORT> exists and before any canon or docs update.
Purpose: Classify what can be used, deferred, or blocked.
Allowed file changes: None for review-first; <TARGET_DOC> only if the user later
says apply.
Inputs to inspect: <RESEARCH_REPORT>, operating manual, current-truth audit, relevant
source-of-truth docs, and any named policy docs.
Hard rules: No canon promotion without explicit approval; preserve context splits;
do not infer saleable_harvest_mass_kg or business outcomes.
Validation requirements: Run <VALIDATION_COMMANDS> only if files change; otherwise
report review evidence.
Required output format: candidate map, do-not-promote list, contradictions, open
questions, recommended next action.
Stop rules: Stop before editing unless the user explicitly says apply and lists files.
```

## 17. Template: source-of-truth/archive inventory

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: When docs may be stale, duplicated, superseded, or risky to reuse.
Purpose: Classify source-of-truth, supporting, superseded, archive-candidate,
do-not-move, and manual-review docs.
Allowed file changes: <TARGET_DOC> only, or none for review-only.
Inputs to inspect: operating manual, existing inventory, current-truth audit, named
docs in scope, and current integrity snapshot.
Hard rules: Do not move, delete, rename, or archive files in inventory passes; do not
treat stale docs as current truth without cross-checking the manual/current audit.
Validation requirements: Run <VALIDATION_COMMANDS>; include diff and status if edited.
Required output format: classification table, stale reason, archive safety,
external reuse risk, recommended handling, no commit.
Stop rules: Stop before archive moves; require a separate archive-move pass.
```

## 18. Template: Obsidian pointer note

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: When the vault needs a minimal pointer to current MVP docs.
Purpose: Update or create a small navigation note without changing canonical truth.
Allowed file changes: Markdown files listed in <ALLOWED_FILES> under
knowledge-vault/** only; never .obsidian/**.
Inputs to inspect: operating manual, source-of-truth inventory, target vault note,
and current-truth audit.
Hard rules: Do not edit docs, src, scripts, tests, configs, data/knowledge,
data/simulation, or ontology files; add minimal links only.
Validation requirements: Show exact diff and git status.
Required output format: summary, touched files, exact diff, link summary,
validation, git status, no commit.
Stop rules: Stop if note title/link target is ambiguous or if more than minimal
pointer text is needed.
```

## 19. Template: local helper/script creation pass

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: When a local coordination or validation helper is approved.
Purpose: Create <HELPER_FILE> and <TEST_FILE> as a narrow local utility.
Allowed file changes: <HELPER_FILE> and <TEST_FILE> only.
Inputs to inspect: operating manual, current helper/script patterns, current truth
audit, and the approved design or task brief.
Hard rules: No canonical knowledge edits, runtime edits, simulation integration,
business logic, or blocked claims; keep output compact and command-backed.
Validation requirements: Run focused tests, <VALIDATION_COMMANDS>, and full integrity
when helper affects MVP validation.
Required output format: summary, touched files, exact diff, command output summary,
protected-path diff, git status, no commit unless explicitly approved with
<COMMIT_MESSAGE>.
Stop rules: Stop if the helper needs broad repo traversal, schema changes, or
unstated protected paths.
```

## 20. Template: Pro model strategic review

```text
Use Pro for strategic synthesis after current facts are assembled.

When to use it: Before a major roadmap, advisor, or investor-facing decision.
Purpose: Review <NEXT_DECISION> against current MVP truth and constraints.
Allowed file changes: None.
Inputs to inspect: full integrity snapshot, operating manual, current-truth audit,
demo walkthrough, progress map spec, and any candidate options.
Hard rules: Do not invent metrics, costs, revenue, safety, profitability, or basil
saleability; keep P2a as selected cost pressure only.
Validation requirements: Require full integrity result and list any missing evidence.
Required output format: current baseline, ranked options, risks, blocked claims,
recommended decision, what would change the recommendation.
Stop rules: Stop if inputs are stale, missing, or conflict with the operating manual.
```

## 21. Template: decision record / roadmap checkpoint

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: After a decision is made and needs a durable record.
Purpose: Record <NEXT_DECISION>, rationale, constraints, and follow-up.
Allowed file changes: <TARGET_DOC> only.
Inputs to inspect: operating manual, current-truth audit, source-of-truth inventory,
integrity snapshot, and decision evidence supplied by the user.
Hard rules: Do not convert roadmap intent into implemented status; do not authorize
canon, runtime, simulation, or business changes unless explicitly decided.
Validation requirements: Run <VALIDATION_COMMANDS>; show exact diff and status.
Required output format: summary, touched files, exact diff, decision summary,
deferred items, validation, git status, no commit.
Stop rules: Stop if the decision is not explicit or if the record would assert
unapproved implementation.
```

## 22. Template: archive-move pass, review-first then apply

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: Only after an inventory identifies archive candidates and the user
asks for archive review.
Purpose: Review archive moves first; apply only after explicit approval.
Allowed file changes: Review phase none; apply phase only files listed in
<ALLOWED_FILES> and only the approved moves/reference edits.
Inputs to inspect: source-of-truth inventory, operating manual, current-truth audit,
git references to candidate files, and current integrity snapshot.
Hard rules: Do not move source-of-truth, configs, canonical data, runtime,
simulation, src, scripts, tests, ontology, or vault files unless explicitly allowed.
Validation requirements: Review phase shows move plan only; apply phase runs
<VALIDATION_COMMANDS>, exact diff/status, and protected-path checks.
Required output format: review map, risk notes, proposed move list, stop point;
after apply, touched files, exact diff, validation, git status, no commit.
Stop rules: Stop after review unless the user explicitly says apply.
```

## 23. Template: prompt-library update pass

```text
You are operating from the Aquaponics-project git repo root. Follow AGENTS.md.

When to use it: When this library needs a narrow update.
Purpose: Update reusable templates without creating task-specific prompts.
Allowed file changes: docs/mvp_prompt_library.md only.
Inputs to inspect: operating manual, current-truth audit, source-of-truth inventory,
demo walkthrough, progress map spec, and current integrity snapshot.
Hard rules: Do not modify existing source docs, configs, data/knowledge,
data/simulation, src, scripts, tests, ontology, or knowledge-vault; block
<BLOCKED_CLAIMS>.
Validation requirements: Run python scripts/check_mvp_integrity.py --quick,
git diff for this file, git status, and protected-path diff.
Required output format: summary, touched files, exact diff, template index summary,
tool routing summary, forbidden patterns summary, checklist summary, validation,
git status, no commit.
Stop rules: Stop if the request becomes a new operating manual, product spec, or
implementation plan.
```

## 24. Forbidden prompt patterns

Generated prompts must never allow:

- Inferring, estimating, backfilling, or populating `saleable_harvest_mass_kg`
  from biomass, plant count, growth, readiness, feed, water, solids, or cost
  outputs.
- Fish safety, system safety, aeration adequacy, oxygen capacity, or future
  safety claims.
- Revenue, profitability, margin, ROI, payback, break-even, viability, or total
  operating cost claims.
- Treating selected P2a cost pressure as total operating cost.
- Promoting scenario inputs, demo values, research findings, or assumptions into
  canon without explicit approval.
- Simulation integration, runtime integration, business consumer updates, or
  schema migration unless explicitly approved.
- Broad implementation before review-first design when scope is uncertain.
- Using stale docs as current truth without cross-checking the operating manual
  and current-truth audit.
- Editing protected paths through vague wording such as "clean up related files"
  or "make whatever changes are needed."

## 25. Prompt quality checklist

Before sending a prompt, verify it:

- States the current MVP baseline: Mode A + P1 + P1.5 + P2a.
- Names allowed files with exact paths or `<ALLOWED_FILES>`.
- Names forbidden paths: configs, `data/knowledge`, `data/simulation`, `src`,
  scripts, tests, ontology, and knowledge-vault when not in scope.
- Includes hard rules for blocked claims.
- Includes validation commands in `<VALIDATION_COMMANDS>`.
- Includes stop rules for ambiguous scope, failed integrity, or canon/runtime
  pressure.
- Includes required output format.
- Says whether commit is allowed; default is no commit.
- Says whether docs, source, canon, runtime, scripts, tests, configs, and vault
  files may change.
- Keeps `saleable_harvest_mass_kg`, safety, revenue, profitability, and total
  operating cost guarded.

## 26. Recommended next action

Use this library for the next strategic checkpoint or bounded Codex pass only
after an integrity snapshot. For uncertain work, start with a review-first
template and require explicit allowed files before any apply pass.
