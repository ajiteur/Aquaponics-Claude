# Aquaponics MVP Operating Manual

## Purpose

This note makes the current Aquaponics MVP operating manual visible in the
knowledge vault.

Use it as a pointer into the repo docs, not as the source of truth.

## Source-of-Truth Link

Repo source of truth:

- `docs/mvp_operating_manual_decision_playbook.md`

Supporting current-state references:

- `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- `docs/mvp_docs_source_of_truth_and_archive_inventory.md`
- `scripts/check_mvp_integrity.py`

## Current MVP Spine

- Mode A: direct feed input and load-only outputs.
- P1: TAN-N concentration and NH3 chemistry context.
- P1.5: aeration and solids context.
- P2a: selected feed and electricity operating-cost pressure.

## Integrity Check Commands

Quick check:

```powershell
python scripts/check_mvp_integrity.py --quick
```

Full check:

```powershell
python scripts/check_mvp_integrity.py --full
```

## What PASS Means

`PASS` means the runner found the expected current MVP state for its configured
checks.

It does not prove field validation, fish safety, system safety, profitability,
revenue, total operating cost, or basil saleable output.

## What FAIL Means

`FAIL` means stop and inspect the failing section before using the repo for a
roadmap, demo, prompt-library, validation, or external-facing decision.

Do not weaken guardrails to make a failure pass.

## Current Guardrails

Do not claim:

- fish or system safety
- aeration adequacy
- total operating cost
- revenue or profitability
- basil saleable harvest

Do not infer or populate `saleable_harvest_mass_kg` unless observed runtime
output or explicit reviewed manual input exists.

## Tool-Use Summary

- ChatGPT: strategy, prioritization, prompt drafting, roadmap decisions, and
  interpretation of integrity snapshots.
- Codex: repo inspection, file edits, implementation, tests, validation, diffs,
  and commits only when explicitly requested.
- Deep Research: external evidence, parameters, costs, source discovery, and
  source-trust comparisons.
- Pro: high-stakes synthesis, roadmap review, and strategic framing.

## Reminder

This Obsidian note is not the source of truth.

The repo doc is the source of truth:

- `docs/mvp_operating_manual_decision_playbook.md`

Do not update this note instead of updating the repo manual.

