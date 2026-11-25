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
7. **Labels:** every business output says "scenario estimate, not validated". No blocked claim is stated as fact.
8. **Vault updated:** Status and Roadmap, Decisions Log, Simulation Findings Log and the [[Project/Feasibility Register|Feasibility Register]] reflect the merged work.
9. **Logged and tagged:** an entry is added below, then an annotated tag `save-point-NNN` is pushed on the `main` commit.

## Log

None yet. The first save point (`save-point-001`) is planned once PR #2 is merged.

## Related Notes

- [[Project/Feasibility Register|Feasibility Register]]
- [[Project/Decisions Log|Decisions Log]]
