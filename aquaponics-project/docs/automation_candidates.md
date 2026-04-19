# Automation Candidates

_Last updated: 2026-04-19_

Status: `draft`

## Purpose

Keep a practical register of repeated Codex or agent tasks and decide which ones should:

- stay manual,
- stay agent-assisted,
- move to a hybrid workflow,
- or be replaced by a local Python helper.

This document is a planning note, not a canonical contract.

## How to use this document

- Start here when a task has been repeated enough that the current manual pattern feels wasteful.
- Treat repetition counts as working estimates from recent repo work, not telemetry.
- Prefer review-first decisions over automation-by-default.
- Update this note when a task is repeated again or when a helper script is added.

Working definitions:

- `repeated task`: the same task shape has been done multiple times with only small input changes.
- `structured input`: the task starts from files, fields, paths, headings, or patterns that are already explicit.
- `predictable output`: the output format is stable enough that the result shape is known in advance.
- `automatically verifiable`: success can be checked by parsing, schema validation, exact-match checks, counts, or other deterministic tests.
- `low-judgment task`: the task is mostly extraction, checking, transformation, or formatting.
- `high-judgment task`: the task depends on evidence weighing, policy choice, canon judgment, ranking, or context splitting.
- `hybrid workflow`: Python extracts, checks, or generates candidates, then Codex does the final wording, review, or decision.
- `automation candidate`: a repeated task that is structured enough to review for scripting.
- `local Python helper`: a small repo-local script used for repeated extraction, checking, summarization, or matrix generation.
- `review-first workflow`: Codex reviews manually first, confirms the stable pattern, then recommends or builds automation.
- `failure risk if automated badly`: the cost of a bad automation result, such as silent wrong edits, missed contradictions, or misleading reports.

## Decision Rule: Agent vs Local Python vs Hybrid

Keep as agent/Codex work when:

- interpretation is high
- evidence is mixed
- context splitting matters
- policy or canon judgment is required
- failure would be subtle and hard to detect automatically

Prefer local Python when:

- extraction, checking, or transformation is repetitive
- input and output pattern is stable
- success can be checked automatically
- failure is easy to detect and recover from

Prefer hybrid when:

- Python can extract, check, or generate candidates
- Codex should still do final wording, ranking, or judgment
- the task has structured inputs but non-trivial review logic

Short rule:

- if the task is repeated and checkable, automate
- if the task is repeated but still needs interpretation, use hybrid
- if the task still depends on canon judgment, keep it agent-first

## Repetition Thresholds

- Repeated `3` times: review for automation candidate.
- Repeated `5` times: build a script unless judgment is clearly high.
- If the task is destructive or edit-heavy, require a review-first workflow even after the threshold is met.
- If the task touches canonical knowledge and wrong output would be hard to detect, prefer hybrid over full automation.

## Automation-Candidate Table

| Task name | Current method | Repetition count | Typical inputs | Typical outputs | Automatically verifiable? | Judgment level | Failure risk if automated badly | Best form | Recommendation | Trigger to automate | Notes |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| JSON validity checks | Codex + shell | 5+ | scoped JSON paths | pass/fail list | yes | low | low | local Python helper | build local Python soon | already past 5 | Stable parse check; good first helper. |
| Scoped git diff summaries | Codex + git | 5+ | scoped paths | compact diff summary | partly | low | low | local Python helper | build local Python soon | already past 5 | Good for repeated review passes and closure checks. |
| Duplicate `Related Notes` detection | Codex review | 3+ | vault markdown notes | duplicate-section report | yes | low | low | local Python helper | build local Python soon | already past 3 | Deterministic markdown hygiene check. |
| Glossary anchor existence checks | Codex review | 3+ | glossary note, candidate anchors | missing-anchor report | yes | low | low | local Python helper | build local Python soon | already past 3 | Good preflight check before vault-linking passes. |
| First-mention link detection | Codex review | 4+ | vault markdown notes, target terms | candidate first mentions | partly | medium | medium | hybrid workflow | keep hybrid | repeated 5 with stable rules | Regex can find candidates, but clutter judgment still matters. |
| Vault link hygiene review | Codex review | 4+ | vault markdown notes | suggested minimal links | no | medium | medium | hybrid workflow | keep hybrid | repeated 5 with stable lint rules | Script can flag likely misses; Codex should approve edits. |
| Runtime/business field inventory | Codex + shell | 3+ | contract doc, JSON files, runtime files | field lists and overlaps | yes | low_to_medium | low | local Python helper | build local Python soon | already past 3 | Strong fit for extraction and comparison. |
| Missing-field matrix generation | Codex review | 2-3 | contract fields, runtime outputs | matrix of present/derivable/missing fields | mostly | medium | medium | hybrid workflow | keep hybrid | repeated 3 with fixed matrix format | Python should build the matrix; Codex should interpret blockers. |
| Repeated status/classification memos | Codex review | 4+ | scoped files and review question | status lines and blockers | no | high | medium | agent/Codex first | keep agent/Codex first | only automate if classification rubric becomes fixed | Output wording is stable; judgment is not. |
| Business JSON placeholder scanning | Codex + shell | 4+ | business JSON files | counts of `null`, `todo`, deferred rules | yes | low | low | local Python helper | build local Python soon | already past 5 | Good closure-check helper for the business layer. |
| Research-to-schema candidate extraction | Codex review | 3+ | research markdown, target schema files | candidate fields, bases, tasks, warnings | partly | high | high | hybrid workflow | keep hybrid | only automate extraction, not final recommendation | Python can pull basis/task phrases; Codex should classify. |

## Current Recommendations

### Build local Python soon

- JSON validity checks
- scoped git diff summaries
- duplicate `Related Notes` detection
- glossary anchor existence checks
- runtime/business field inventory
- business JSON placeholder scanning

### Keep hybrid

- first-mention link detection
- vault link hygiene review
- missing-field matrix generation
- research-to-schema candidate extraction

### Keep agent/Codex first

- repeated status/classification memos
- any review that ends in `stable_enough_for_now` vs `needs_follow_up_before_integration`
- any task where the answer depends on evidence quality rather than file shape

## Not Suitable for Full Automation Yet

- contradiction resolution
- context-split vs contradiction judgment
- evidence-to-canon promotion decisions
- business-layer schema decisions where basis or driver choice is unresolved

These are still high-judgment tasks. Python may help collect inputs, but final decisions should remain review-first.

## Notes and Cautions

- Do not automate a task just because it is annoying; automate it when the pattern is stable.
- Prefer scripts that check or generate candidates before scripts that edit canonical files directly.
- If a task can silently produce plausible but wrong output, do not move it straight to full automation.
- For canonical knowledge work, extraction is easier to automate than judgment.
- If a helper becomes important to repeated review passes, keep its inputs path-scoped and its output easy to diff.
