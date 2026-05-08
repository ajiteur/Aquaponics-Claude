# MVP Goal-Drift Checklist

## 1. Purpose

Use this checklist before approving or writing future Aquaponics MVP tasks.

The checklist asks one question:

> Does the proposed next task advance the goal of proving whether one bounded
> tilapia + basil DWC/raft aquaponics unit can be measured, modeled, and
> evaluated for commercial unit economics using real measured data, explicit
> scenario data, or clearly labeled benchmark assumptions?

This is a lightweight coordination checklist. It is not a new operating
manual, product spec, roadmap, implementation plan, report, dashboard, or pitch
artifact.

## 2. Relationship to seed goal and current MVP state

Current pathway:

1. technical spine
2. seed-goal reset
3. unit-economics data contract
4. benchmark scenario dataset
5. seed-demo report
6. later expert/customer validation when accessible
7. later real-world unit-economics proof
8. later multi-species/app-game expansion

Current status:

| milestone | status |
| --- | --- |
| Technical spine | done enough |
| Seed-goal reset | done |
| Unit-economics data contract | done |
| Benchmark scenario design | done |
| Benchmark scenario fixture | done |
| Seed-demo benchmark report | done |
| Customer/operator validation | not yet available |
| Commercial proof | not yet available |
| Real-world operating proof | not yet available |

The current MVP supports pre-customer demo credibility. It does not yet support
customer validation, commercial proof, real-world operating proof, safety,
total operating cost, revenue, profitability, commercial operability, or known
basil saleable output.

## 3. When to use this checklist

Run this checklist before:

- new ChatGPT strategy decisions
- new Codex prompts
- implementation passes
- dashboard or report design
- Deep Research tasks
- Pro model reviews
- customer/advisor validation planning
- source-ingestion or benchmark-update work
- P2c, Mode B, or business-layer expansion
- app/game, UI, multi-species, or multi-crop expansion

Use it early, before a long prompt is written. If a task fails here, rewrite
the task instead of trying to add guardrails afterward.

## 4. PASS / CAUTION / FAIL meanings

| verdict | meaning | action |
| --- | --- | --- |
| PASS | The task directly advances the bounded unit-economics proof path and preserves blocked claims. | Proceed with a scoped prompt and validation commands. |
| CAUTION | The task may be useful, but timing, scope, evidence, or claim discipline needs tightening. | Rewrite as review-first, docs-only, or explicitly deferred work. |
| FAIL | The task violates a hard guardrail, skips the proof path, or creates misleading claims. | Do not proceed. Replace with a narrower task. |

## 5. Scoring criteria

Score each criterion from 0 to 2.

| score | meaning |
| --- | --- |
| 0 | Fails, is irrelevant, or creates drift risk. |
| 1 | Partially or indirectly helps, but needs tighter scope. |
| 2 | Strong and direct contribution to the seed goal. |

| criterion | score 0 | score 1 | score 2 |
| --- | --- | --- | --- |
| Seed-goal alignment | Does not advance bounded tilapia + basil unit-economics proof. | Indirectly related or useful later. | Directly advances the proof path. |
| Unit-economics data-contract value | Does not improve required fields, metadata, nulls, or provenance. | Mentions data needs but not contract-ready. | Clarifies or fills a data-contract gap. |
| Benchmark/report value | Does not improve benchmark or seed-demo clarity. | Helps presentation or review indirectly. | Improves benchmark fixture, source gaps, report clarity, or reviewer readiness. |
| Evidence basis | Invents values or uses weak/unclear evidence. | Uses plausible sources but needs review. | Uses real, explicit scenario, or clearly labeled benchmark evidence. |
| Claim discipline | Risks unsupported claims. | Guardrails are present but could be clearer. | Keeps blocked claims explicit and visible. |
| Timing | Pulls work forward before needed inputs exist. | Useful later, but not the next step. | Fits the current pathway and access constraints. |
| Validation value | Has no clear verification or review outcome. | Has some review value but weak validation. | Produces a clear check, artifact, or decision gate. |

Verdict thresholds:

| total score | default verdict |
| --- | --- |
| 11-14 | PASS, unless an automatic FAIL condition applies. |
| 6-10 | CAUTION, unless an automatic FAIL condition applies. |
| 0-5 | FAIL. |

## 6. Automatic FAIL conditions

Fail immediately if the proposed task would:

- infer, estimate, populate, or backfill `saleable_harvest_mass_kg`
- claim fish safety or system safety
- claim aeration adequacy
- claim total operating cost
- claim revenue or profitability
- claim commercial operability
- treat a benchmark scenario as customer validation
- treat a benchmark scenario as commercial proof
- treat a benchmark scenario as real-world operating proof
- promote scenario assumptions into canon
- expand to new fish or plants before first bounded-unit proof
- build an app/game layer before first bounded-unit proof
- modify protected canonical, runtime, simulation, source, script, test, config,
  or knowledge-vault files without explicit scope

If an automatic FAIL condition appears, do not rescue the task with a high
score. Rewrite the task.

## 7. CAUTION conditions

Use CAUTION when the task is plausible but not ready as written:

- useful, but not now
- presentation polish before data/report clarity
- extra biology module without a unit-economics connection
- dashboard work without explicit blocked-claim panels
- Deep Research not tied to a data-contract gap
- implementation before a review-first design when scope is uncertain
- P2c or Mode B work before missing evidence and validation questions are
  resolved
- customer validation work written as if customer access already exists

Recommended CAUTION response:

1. Narrow the task.
2. Make it review-first or docs-only if uncertainty is high.
3. Add blocked-claim language.
4. Add validation commands.
5. Re-score.

## 8. PASS conditions

PASS is appropriate when the task:

- advances unit-economics proof for one bounded tilapia + basil DWC/raft unit
- strengthens the data contract
- improves benchmark scenario or seed-demo report clarity
- reduces source gaps
- preserves blocked claims
- improves validation readiness
- keeps scenario assumptions separate from canon
- keeps benchmark evidence separate from customer/operator validation
- produces a clear decision, checklist, source plan, data artifact, or
  guarded report artifact

## 9. Reusable evaluation template

Use this format before approving a proposed task:

```text
Proposed task:
<one sentence>

Scores:
- seed-goal alignment: <0/1/2>
- unit-economics data-contract value: <0/1/2>
- benchmark/report value: <0/1/2>
- evidence basis: <0/1/2>
- claim discipline: <0/1/2>
- timing: <0/1/2>
- validation value: <0/1/2>

Goal-drift verdict: PASS / CAUTION / FAIL
Total score: <0-14>
Classification: <docs-only / research / report / data fixture / implementation / validation / expansion>
Reason: <short explanation>
Blocked-claims risk: <none / low / medium / high / automatic fail>
Recommended action: <proceed / rewrite / defer / stop>
```

If the task is allowed to proceed, the final prompt must still specify allowed
files, forbidden files, validation commands, commit status, and blocked claims.

## 10. Example evaluations

### Seed-demo dashboard design

| criterion | score |
| --- | --- |
| Seed-goal alignment | 1 |
| Unit-economics data-contract value | 1 |
| Benchmark/report value | 2 |
| Evidence basis | 1 |
| Claim discipline | 1 |
| Timing | 1 |
| Validation value | 1 |

Total score: 8

Verdict: CAUTION

Reason: A dashboard could help later presentation, but only after report
clarity and blocked-claim panels are stable.

Recommended action: Rewrite as docs-only dashboard design with explicit
guardrail panels, no new calculations, no generated UI, and no commercial
claims.

### P2c cost extension

| criterion | score |
| --- | --- |
| Seed-goal alignment | 1 |
| Unit-economics data-contract value | 2 |
| Benchmark/report value | 1 |
| Evidence basis | 1 |
| Claim discipline | 1 |
| Timing | 0 |
| Validation value | 1 |

Total score: 7

Verdict: CAUTION

Reason: More cost categories may matter, but the current report only supports
selected feed + electricity cost pressure. P2c can easily be mistaken for full
cost scope.

Recommended action: Do a review-first design or source-gap pass. Do not
implement P2c until selected categories, evidence, labels, and validation are
approved.

### Mode B biomass feeding

| criterion | score |
| --- | --- |
| Seed-goal alignment | 1 |
| Unit-economics data-contract value | 1 |
| Benchmark/report value | 0 |
| Evidence basis | 1 |
| Claim discipline | 1 |
| Timing | 0 |
| Validation value | 1 |

Total score: 5

Verdict: FAIL

Reason: Biomass-derived feeding is future-useful but premature as an
implementation pass. It would widen the technical model before the current
unit-economics proof path has real or reviewed inputs.

Recommended action: Defer. If needed, create only a review-first design note
after source gaps and customer/operator questions are clearer.

### New fish/plant expansion

| criterion | score |
| --- | --- |
| Seed-goal alignment | 0 |
| Unit-economics data-contract value | 0 |
| Benchmark/report value | 0 |
| Evidence basis | 0 |
| Claim discipline | 1 |
| Timing | 0 |
| Validation value | 0 |

Total score: 1

Verdict: FAIL

Reason: This is an automatic FAIL before the first bounded tilapia + basil unit
proof. It distracts from the current seed goal.

Recommended action: Stop. Preserve expansion ideas as deferred notes only after
real-world unit-economics proof work is underway.

### App/game prototype

| criterion | score |
| --- | --- |
| Seed-goal alignment | 0 |
| Unit-economics data-contract value | 0 |
| Benchmark/report value | 0 |
| Evidence basis | 0 |
| Claim discipline | 1 |
| Timing | 0 |
| Validation value | 0 |

Total score: 1

Verdict: FAIL

Reason: App/game work is an automatic FAIL before first bounded-unit proof. It
would shift effort from data, evidence, and validation readiness.

Recommended action: Stop. Revisit after the MVP has real-world unit-economics
evidence and reviewed product direction.

### Customer validation plan

| criterion | score |
| --- | --- |
| Seed-goal alignment | 2 |
| Unit-economics data-contract value | 1 |
| Benchmark/report value | 1 |
| Evidence basis | 1 |
| Claim discipline | 2 |
| Timing | 0 |
| Validation value | 2 |

Total score: 9

Verdict: CAUTION

Reason: Validation planning is aligned, but direct customer/operator access is
not yet available. The task must not imply validation has happened.

Recommended action: Create a future validation plan or question packet only.
Keep it blocked until access exists.

### Expert question backlog

| criterion | score |
| --- | --- |
| Seed-goal alignment | 2 |
| Unit-economics data-contract value | 2 |
| Benchmark/report value | 2 |
| Evidence basis | 1 |
| Claim discipline | 2 |
| Timing | 2 |
| Validation value | 2 |

Total score: 13

Verdict: PASS

Reason: A backlog tied to source gaps and data-contract blockers is directly
useful before customer access.

Recommended action: Proceed as docs-only or research-planning work. Tie every
question to a data-contract field, source gap, or blocked claim.

## 11. Recommended use cadence

Run this checklist:

- before every new strategy prompt
- before every Codex implementation prompt
- before every Deep Research request
- before every Pro review request
- before creating dashboard/report artifacts
- after any major source-of-truth doc changes
- before moving from design to implementation
- before proposing expansion beyond tilapia + basil DWC/raft

For quick decisions, use only the automatic FAIL list and total score. For
large tasks, include the full reusable evaluation template in the prompt.

## 12. Future automation or Skill option

This checklist may later become:

- a Codex prompt template: useful now, low overhead
- a script: useful only if prompts start repeating the same scoring mistakes
- a ChatGPT Skill: useful if strategy sessions need consistent triage
- an Obsidian pointer note: useful as a navigation link only, not source of
  truth

Recommended sequence:

1. Use this document manually for several decisions.
2. Add a prompt-library template if it proves stable.
3. Consider a script only after the scoring pattern is stable enough to test.
4. Add an Obsidian pointer only if navigation becomes a problem.

## 13. Recommended next action

Use this checklist before the next proposed task. The strongest near-term PASS
candidate is an expert/source question backlog tied to the benchmark fixture
source gaps, data-contract fields, and seed-demo report blockers.
