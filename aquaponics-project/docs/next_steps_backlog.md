# Next Steps Backlog

_Last updated: 2026-04-19_

Status: `draft`

## Purpose

Keep a practical backlog for choosing what to do next without fake precision.

This note is for current planning around one narrow first vertical slice. It is not a canonical contract and it should not be treated as a long-term roadmap by itself.

## Current Project Objective

Build one narrow, reviewable first vertical slice from runtime outputs to business interpretation.

For the current objective, the slice should stay small enough to review end-to-end:

- runtime outputs are mapped into the business contract
- one narrow pricing/cost/labor path is populated
- one first-pass business interpretation output becomes reviewable

## How to Use This Backlog

- Use `now / next / later / blocked / done` as the main decision system.
- Use the numeric priority only as a secondary aid inside the current objective.
- Re-rank tasks when the current objective changes.
- Prefer small tasks that unlock the vertical slice over broad cleanup or expansion work.

Important note:

- priority scoring only makes sense relative to the current objective
- do not use the score to create fake precision
- `Now / Next / Later` matters more than the numeric score

## Status Definitions

- `now`: should be worked on immediately because it directly advances or unblocks the current objective.
- `next`: not immediate, but likely to be the next useful task after the current `now` items.
- `later`: useful work, but not needed for the current narrow slice.
- `blocked`: should not move yet because another decision, audit, or artifact is missing.
- `done`: completed enough for the current objective and does not need active planning right now.

## Simple Prioritization Rule

`Priority = Objective impact + Blocker pressure + Uncertainty reduction - Effort`

Score definitions:

- `Objective impact`
  - `2` = directly advances the current objective
  - `1` = helpful but indirect
  - `0` = not relevant right now
- `Blocker pressure`
  - `2` = other important work is waiting on it
  - `1` = likely to matter soon
  - `0` = not blocking anything
- `Uncertainty reduction`
  - `2` = clears major confusion or prevents wrong decisions
  - `1` = clears some ambiguity
  - `0` = mostly already understood
- `Effort`
  - `2` = large / slow
  - `1` = medium
  - `0` = small / quick

Interpretation guidance:

- high priority: `3 to 6`
- medium priority: `1 to 2`
- low priority: `0 or below`

## Task-Type Definitions

- `research`: evidence review that decides structure, categories, or distinctions.
- `schema`: changes or clarifications to canonical file structure, fields, bases, or deferred rules.
- `integration`: mapping or adapter-facing work that connects runtime outputs to the business contract.
- `vault`: markdown note, glossary, explainer, or linking work in `knowledge-vault/**`.
- `policy`: geography, pricing basis, channel, or incentive assumptions that affect business interpretation.
- `simulation`: runtime or scenario-side work that changes what outputs exist or how they are produced.
- `automation`: local helper work for repeated low-judgment checks, extraction, or summarization.

## Main Backlog Table

| Task | Type | Why now | What it unlocks | Objective impact | Blocker pressure | Uncertainty reduction | Effort | Priority | Status | Definition of done | Artifact path | Notes / blockers |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
| Phase 1 runtime-to-business field audit | integration | The current contract is defined, but runtime coverage is still not mapped explicitly. | Shows which required-now fields already exist, are derivable, or are missing. | 2 | 2 | 2 | 1 | 5 | now | One read-only matrix of required-now contract fields vs current runtime outputs, with present/derivable/missing status. | `docs/runtime_to_business_field_audit.md` | Best current blocker-clearing task. |
| Choose first direct-mass slice | policy | The slice must be narrow before pricing/cost/labor can be populated cleanly. | Prevents diffuse data gathering and keeps the first path reviewable. | 2 | 2 | 2 | 0 | 6 | now | One explicit first slice chosen, such as basil bulk kg wholesale or tilapia kg wholesale. | `docs/first_vertical_slice_choice.md` | Should be chosen before broader channel or output-form work. |
| Populate one narrow pricing/cost/labor path | schema | The business layer cannot emit a non-null first interpretation until one path is populated. | Enables the first end-to-end business calculation path. | 2 | 2 | 1 | 1 | 4 | now | One narrow path has non-null pricing, cost, and labor assumptions with clear basis notes. | `data/knowledge/business/pricing_models.json` | Depends on choosing the first slice first. |
| Tighten first-slice working assumptions | research | The first example run now works, but the weakest assumptions are still constructed working values. | Makes the first reviewable output more defensible before anything is promoted toward business-layer canon. | 2 | 2 | 2 | 1 | 5 | next | One reviewed assumption note exists and at least the first-slice variable-cost and fixed-cost basis are tightened beyond purely constructed example values. | `docs/first_slice_assumption_review.md` | Keep this review-first and non-canonical. |
| First reviewable business interpretation output | integration | The project objective is not complete until there is one reviewable output path. | Creates the first vertical-slice artifact for review. | 2 | 1 | 1 | 1 | 3 | next | One example interpretation output can be produced with nulls only where still explicitly unresolved. | `docs/business_layer_contract.md` | Depends on the audit and one populated business path. |
| Runtime/business missing-field matrix generation helper | automation | The Phase 1 audit is likely to be repeated and benefits from stable extraction. | Speeds later re-audits as the contract or runtime changes. | 1 | 1 | 1 | 1 | 2 | next | A helper can generate the matrix candidate from the contract and runtime files for review. | `docs/automation_candidates.md` | Keep hybrid if judgment on derivable vs missing remains high. |
| Output-form and channel-fit deep research | research | Important for broader plant pricing, but the narrow direct-mass slice can avoid most of it at first. | Makes later lettuce-head, basil-bunch, and architecture-aware plant channels safer. | 1 | 1 | 2 | 2 | 2 | next | Reviewed guidance exists for output form and channel-fit expansion beyond the narrow first slice. | `data/knowledge/business/yield_to_revenue_rules.json` | Useful soon, but not the first bottleneck if the slice is direct-mass. |
| First local Python helper for repeated low-judgment repo checks | automation | Repo checks are repeating, but they do not directly create the first slice. | Saves time on JSON checks, diff summaries, and placeholder scans. | 1 | 0 | 1 | 1 | 1 | next | One small helper exists for at least one repeated low-judgment check. | `docs/automation_candidates.md` | Good sidecar task, not the main slice blocker. |
| India policy and incentive research | policy | Valuable for later real-world business interpretation, but not necessary for the first narrow slice. | Better geography-specific pricing and incentive assumptions later. | 1 | 0 | 1 | 2 | 0 | later | One scoped research note exists with sources, limits, and explicit non-canonical assumptions. | `docs/project_status_and_roadmap.md` | Do after the first slice unless geography becomes immediate. |
| Vault first-meaningful-mention cleanup follow-ups | vault | Nice for navigation quality, but not part of the vertical slice objective. | Better vault readability and reuse. | 0 | 0 | 0 | 1 | -1 | later | Remaining high-value vault notes are linked without clutter. | `knowledge-vault/` | Keep separate from business integration work. |
| Broader risk-penalty activation | schema | Risk structure exists, but active penalties are intentionally deferred and not needed for the first narrow slice. | Later risk-adjusted margin outputs. | 1 | 1 | 2 | 2 | 2 | blocked | Penalty vocabularies, event detail, and first active rule basis are clear enough to promote one path. | `data/knowledge/business/risk_penalty_models.json` | Blocked by event detail and penalty-basis decisions. |
| Wider channel expansion | schema | More channels are useful later, but they complicate the first slice too early. | Multi-channel comparisons and richer pricing paths. | 1 | 0 | 1 | 2 | 0 | later | More channel records and product/channel combinations are populated with real assumptions. | `data/knowledge/business/channel_assumptions.json` | Keep narrow until one path works end-to-end. |
| Create geography benchmark-pack structure | research | A reusable Netherlands/India benchmark-pack structure could help later cross-geo review, but it does not unblock the current slice now. | Cleaner storage and comparison of later geography-specific working packs without pushing them into canon too early. | 1 | 0 | 1 | 2 | 0 | later | One non-canonical benchmark-pack structure exists for later Netherlands and India working packs, clearly separated from business canon. | `data/sources/research_reports/markdown/` | Later only; do not build the folder structure during the current first-slice push. |
| Business-layer foundation scaffold and contract creation | schema | This baseline already exists and should not consume active planning time. | Makes the current first-slice work possible. | 1 | 0 | 0 | 0 | 1 | done | Contract, plan, and initial business JSON files exist and have been reviewed as usable scaffolding. | `docs/business_layer_contract.md` | Revisit only if a later integration step exposes a structural gap. |

## Current Recommendation

Work the next three items in this order:

1. Run the runtime-to-business field audit.
2. Choose one first populated slice, preferably a narrow direct-mass path.
3. Populate one narrow pricing/cost/labor path for that slice.

After that:

4. Produce one first reviewable business interpretation output
5. only then widen into output-form/channel-fit research, broader risk activation, or more channels

## Notes and Cautions

- Do not let useful side work displace the first vertical slice.
- If a task depends on unresolved sale-unit or channel-fit logic, it is probably not the right first slice.
- Keep research, schema cleanup, and vault work from mixing into one execution pass unless the dependency is real.
- A blocked task is not low-value; it just should not drive the queue yet.
