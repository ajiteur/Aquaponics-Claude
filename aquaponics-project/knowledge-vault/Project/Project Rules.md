# Project Rules

A plain-language summary of `aquaponics-project/AGENTS.md`. If they disagree, AGENTS.md wins.

## Goal

Build a thorough, evidence-first aquaponics knowledge and simulation engine. Use it to make predictions and decide whether a real farm is worth building. If a farm isn't viable, the same engine becomes the base for an original aquaponics simulation game.

## Where truth lives

- `data/knowledge/` is canonical: the source of truth.
- `data/simulation/` is derived: generated from canon and from simulation runs.
- This vault is the reading layer. It never overrides canon.
- [[Truths/Truths|Truths]] notes are generated from JSON. Don't edit them by hand; change the JSON and re-export.

## What can and can't be claimed

- No claims of fish safety, system safety, profitability, viability or validated harvest mass as fact.
- The one exception is a **scenario estimate**: you asked for it, every input is labelled with where it came from, nothing is invented, results are ranges, and it says "scenario estimate, not validated".
- Prices, wages and costs are never made up. Missing values stay missing.

## Evidence

- New evidence becomes a **candidate** truth first. It becomes **accepted** only after you approve it.
- When two facts disagree because their context differs (system, species, scale), keep both as a context split rather than calling it a contradiction.

## Working style

- Changes happen on a branch and arrive as a pull request for you to review.
- Small, scoped commits. Vault, canon and code changes go in separate commits.
- Every work session ends with a learning capture (below).

## Learning capture (end of every session)

1. New evidence goes into `data/knowledge/atomic_facts/` as candidate facts, then the truths export runs.
2. New simulation results go into the [[Learnings/Simulation Findings Log|Simulation Findings Log]].
3. Choices made go into the [[Project/Decisions Log|Decisions Log]].
4. Anything in the [[Inbox/Inbox|Inbox]] is sorted into the three above.

## Related Notes

- [[Project/Project|Project]]
