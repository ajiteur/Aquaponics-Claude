# Save Points

A save point is a known-good state of `main` that we can always go back to. The Gatekeeper declares it and tags it on `main` as `save-point-NNN`. Only Ajit merges PRs.

## Checklist

Every line must hold on `main` before a save point is tagged.

1. **Merged:** every PR meant for this save point is merged by Ajit, and the Gatekeeper reviewed each one.
2. **Tests green:** `python -m unittest discover -s tests` passes.
3. **Integrity:** `python scripts/check_mvp_integrity.py --quick` passes with protected paths clean. Use `--full` before a farm go/no-go or anything shown outside the project.
4. **Canon synced:** `python src/build_runtime_from_knowledge.py --dry-run` proposes no changes.
5. **Vault synced:** `python src/export_truths_to_vault.py --dry-run` shows 0 notes to write and 0 stale notes.
6. **Evidence:** no invented numbers. New values are `candidate` unless Ajit approved them, and each approval records who, date and scope.
7. **Reliability:** every truth or manual input added since the last save point records its source tier, source gate, confidence with a reason, and corroboration (AGENTS.md 6A). Tier 3 or single-source items are still `provisional`.
8. **Labels:** every business output says "scenario estimate, not validated". No blocked claim is stated as fact.
9. **Vault updated:** Status and Roadmap, Decisions Log, Simulation Findings Log and the [[Project/Feasibility Register|Feasibility Register]] reflect the merged work.
10. **Logged and tagged:** an entry is added below, then an annotated tag `save-point-NNN` is pushed on the `main` commit.

## PR review checks

The Gatekeeper checks every PR for these before giving a merge verdict:

- Tests and the integrity check pass on the PR head.
- No invented numbers. Each new value is canonical, approved by Ajit (who, date, scope), or marked candidate or pending.
- Each new truth or manual input has a reliability record: source tier, source gate, confidence with a reason, and corroboration.
- Context is kept (species, system type, scale, climate) rather than flattened into one number.
- Business outputs are labelled scenario estimates, and no blocked claim is stated as fact.
- Canon and runtime are in sync, and the vault export matches the JSON.
- The vault capture for the work is done: findings, decisions, status.
- The PR doesn't edit files that another open PR owns.

## Log

None yet. The first save point (`save-point-001`) is planned once PR #4 and PR #5 are merged.

## Related Notes

- [[Project/Feasibility Register|Feasibility Register]]
- [[Project/Decisions Log|Decisions Log]]
