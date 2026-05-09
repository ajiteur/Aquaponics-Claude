# AGENTS.md

This file defines safe operating rules for Codex and future agents working inside
`aquaponics-project/`.

## 1. Repo contract

- `data/knowledge/**` is canonical.
- `data/simulation/**` is derived runtime output.
- `docs/**` contains human-readable contracts, plans, and implementation notes.
- `knowledge-vault/**` is the human-readable navigation and note layer, not canonical machine truth.
- Do not modify `src/build_runtime_from_knowledge.py` unless explicitly instructed.
- Do not commit unless explicitly instructed.

## 1A. Decision-rule reference

- Use `docs/decision_rule_research_simulation_business_audit.md` when deciding whether a task should be handled as:
  - deep research / evidence review
  - simulation
  - business calculation
  - repo audit / compatibility check
- Use `docs/mvp_operating_manual_decision_playbook.md`,
  `docs/mvp_goal_drift_checklist.md`,
  `docs/mvp_current_truths_terminology_and_loophole_audit.md`, and
  `docs/mvp_prompt_library.md` for current MVP guardrails and prompt shaping.

## 1B. Current MVP house rules

Current MVP baseline:

- Mode A direct feed input.
- P1 TAN-N/NH3 context.
- P1.5 aeration/solids context.
- P2a selected feed + electricity operating-cost pressure.

Benchmark and seed-demo framing:

- Treat benchmark/seed-demo artifacts as public-evidence-inspired, scaled,
  scenario-augmented, and pre-customer unless a later approved source says
  otherwise.
- Do not treat benchmark scenarios as direct full-UVI reproduction, canon,
  customer validation, commercial proof, or real-world operating proof.
- If benchmark/seed-demo package artifacts are present, use them as current
  context only; do not make AGENTS.md depend on phase-specific report,
  prototype, fixture, or commit paths.

Non-negotiable blocked claims:

- Do not claim fish safety, system safety, aeration adequacy, oxygen-transfer
  capacity, total oxygen demand, solids-removal capacity, total operating cost,
  revenue, profitability, margin, ROI, payback, break-even, economic viability,
  commercial operability, customer validation, real-world operating proof, or
  known basil saleable harvest mass.

`saleable_harvest_mass_kg` rule:

- Do not infer, estimate, backfill, or populate `saleable_harvest_mass_kg`
  unless observed runtime output or explicitly reviewed manual input is
  approved for that scope.
- Do not infer it from standing biomass, daily gain, plant count,
  harvest-readiness labels, saleability labels, feed, water quality, solids,
  cost pressure, or benchmark basil context.

P2a cost-pressure boundary:

- P2a is selected feed + electricity operating-cost pressure only.
- It is not total operating cost, revenue, profitability, margin, economic
  viability, commercial operability, or commercial proof.

Terminology boundaries:

- TAN-N load is not concentration.
- TAN-N/NH3 chemistry context is not fish safety.
- Measured DO context is not aeration adequacy.
- Nitrification oxygen demand is not total oxygen demand or oxygen-transfer
  capacity.
- Dry-solids potential is not wet sludge, TSS, or solids-removal capacity.
- Fish-tank concentration scope is not whole-system average concentration.
- `crop_system_type` is context only; it must not activate saleability, pricing,
  buyer acceptance, product-form, or revenue logic by itself.

## 2. Global safety rules

- Prefer minimal diffs over broad rewrites.
- Do not touch unrelated files.
- Show diffs before any commit.
- If a file already satisfies the goal, report `no change needed`.
- Do not invent numeric values.
- Preserve meaningful context splits instead of flattening differences.
- Do not treat `data/simulation/**` as source-of-truth.
- Ignore `.obsidian/**` unless explicitly asked.
- Default mode is review-only or bounded edit with no commit.
- Commit only after explicit user instruction to commit.
- Staging must remain scoped; do not stage unrelated files.

## 2A. Path and shell discipline

- Assume the current working directory is the git repo root unless explicitly told otherwise.
- Use repo-relative paths only.
- Do not prepend `aquaponics-project/` when already operating from the repo root.
- Prefer exact file paths over guessed paths.
- If a referenced path is uncertain, stop and report the uncertainty instead of inventing one.
- If `rg` is unavailable, fall back to native shell search tools for the current environment rather than changing scope.

## 2B. Non-authoritative sources inside the repo

Unless explicitly asked, do not use these as proof of canonical requirements:

- `data/simulation/day_logs/**`
- `data/simulation/_sync_backups/**`
- temporary files
- debug logs
- generated patch files
- exported chat summaries
- copied temp review bundles
- `.obsidian/**`

These may be useful for diagnostics, but they are not canonical evidence.

## 2C. Cleanup-pass discipline

- In cleanup passes, prefer minimal edits over structural redesign.
- If a file or field already satisfies the goal, report `no change needed`.
- Do not broaden a cleanup pass into integration, migration, or schema redesign unless explicitly instructed.

## 3. Branching rules

- For branch-based experiments or risky automation, create a fresh branch first.
- Do not create a new branch for a simple review-only or bounded single-file edit unless explicitly asked.
- Use a separate branch for:
  - vault-linking experiments
  - business-layer cleanup passes
  - evidence/canon promotion passes
- Keep commits small and scoped.
- Do not mix:
  - vault note changes
  - business-layer schema changes
  - species/runtime/canonical knowledge changes
  in the same commit.

## 4. Evidence / canon agent rules

Use when reviewing corroboration PDFs, distilled packs, trust-policy files, and canonical repo files.

### Required workflow
1. Read current canonical files first.
2. Read the new evidence.
3. Normalize units and variable identity before comparing facts.
4. Preserve context tags such as:
   - system type
   - coupling mode
   - species
   - temperature regime
   - scale
   - architecture
5. Prefer `context_split` over contradiction when context differs.
6. If overlap still conflicts, draft a contradiction ticket rather than silently overwriting canon.
7. Stop before editing unless explicitly told `apply`.

### Do not
- Do not flatten context-dependent facts into one universal number.
- Do not promote derived runtime values back into canon.
- Do not change `src/build_runtime_from_knowledge.py` unless explicitly instructed.

## 5. Business-layer agent rules

Use for:
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `data/knowledge/business/**`

### Required workflow
1. Treat business files as canonical scaffolding, not live integration code.
2. Keep schemas simple and business-readable.
3. Prefer placeholder structures over invented numbers.
4. Keep deferred paths explicit and consistent.
5. Keep provenance repo-addressable where possible.
6. Keep `risk_penalty_models.json` draft until vocabularies are normalized.
7. If a field or file already satisfies the goal, report `no change needed`.
8. When a business field has an unresolved basis, mark it as a schema-choice TODO rather than hiding uncertainty inside a mixed field name or unit string.
9. Keep optional or deferred business paths explicit with a consistent activation pattern.
10. Reconcile contract-level required inputs against rule-level optional fields; do not silently promote optional fields to required.

### Do not
- Do not add runtime sync logic.
- Do not add migration code.
- Do not add consumer updates.
- Do not infer prices, wages, financing assumptions, or utilization from general knowledge.

## 6. Vault-linking agent rules

Use for `knowledge-vault/**/*.md` only.

### Required workflow
1. Touch markdown notes only.
2. Ignore `.obsidian/**`.
3. Find:
   - orphan notes
   - zero-outbound-link notes
   - obvious plain-text mentions of existing note titles
   - weak hub notes
4. Apply only minimal wikilink improvements.
5. Prefer hub-note links over many low-value cross-links.
6. Add at most 1 to 3 links per note in a single pass.
7. Show diffs only and stop without commit.

### Do not
- Do not rewrite prose unless needed to add a link.
- Do not auto-link ambiguous note titles.
- Do not touch business-layer files, code, or simulation files.
- If the exact wikilink already exists, report `no change needed`.
- Do not add duplicate `Related Notes` sections.

## 7. Automation ladder

Use this progression:

### Level 1 — review only
- audit files
- classify issues
- show diffs only

### Level 2 — bounded edit
- edit scoped files
- show exact diff
- stop without commit

### Level 3 — branch experiment
- create fresh branch
- run bounded automation
- show final diff
- stop without commit

### Level 4 — subagents (future)
Only introduce subagents after rules are stable and repeatable.

Candidate future subagents:
- evidence-canon reviewer
- business-layer cleanup reviewer
- vault-linking/navigation reviewer

## 8. Commit rules

Before commit:
- confirm scope
- confirm no unrelated files are staged
- confirm diff is readable
- confirm tests/checks relevant to that change have run
- commit only after explicit instruction

## 8A. Verification rules

- Run only the checks relevant to the scoped change.
- Prefer the smallest useful verification step.
- Do not expand verification scope unless a failure suggests it is necessary.
- If a required tool is unavailable in the environment, report that clearly instead of faking verification.
- For snapshot-based tests, update fixtures only when the approved canonical or generated output has intentionally changed.

## 8B. MVP verification pattern

For MVP tasks, prefer this three-step verification pattern unless the user gives
a narrower or broader validation set:

1. Integrity snapshot: usually `python scripts/check_mvp_integrity.py --quick`;
   use `--full` before major roadmap, external-facing, or implementation
   decisions.
2. Artifact-specific validation: run the focused test, JSON check, section
   audit, value audit, language audit, or static-prototype audit that matches
   the changed artifact.
3. Scope hygiene: show the relevant diff, protected-path diff or name-only
   check, `git status --short`, and `git diff --cached --name-only` before any
   commit.

A passing integrity snapshot means the configured checks passed. It does not
prove safety, validation, revenue, profitability, commercial operability,
real-world operation, or basil saleable harvest output.

## 9. Output style for agents

Unless told otherwise:
- start with a short state summary
- list touched files
- show exact diff
- show any verification run
- stop with `no commit`

## 10. Prompt compression rule

- Future prompts may rely on this AGENTS.md for stable repo guardrails, MVP
  blocked claims, benchmark framing, and standard verification posture.
- Prompts should still specify task-specific goal, allowed files, references,
  validation, stop rules, output format, and commit policy.
- Do not put one-off task instructions, phase percentages, commit hashes, exact
  demo values, exact benchmark values, seed-demo artifact paths, or transient
  milestone details into AGENTS.md.
