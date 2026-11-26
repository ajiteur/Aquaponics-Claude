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
9. **Vault updated:** Status and Roadmap, Decisions Log, Simulation Findings Log, the [[Project/Feasibility Register|Feasibility Register]] and the [[Project/Simulation Progress Tracker|Simulation Progress Tracker]] reflect the merged work.
10. **Logged and tagged:** an entry is added below, then an annotated tag `save-point-NNN` is pushed on the `main` commit.

## PR review checks

The Gatekeeper checks every PR for these before giving a merge verdict:

- Tests and the integrity check pass on the PR head.
- No invented numbers. Each new value is canonical, approved by Ajit (who, date, scope), or marked candidate or pending.
- Each new truth or manual input has a reliability record: source tier, source gate, confidence with a reason, and corroboration.
- Context is kept (species, system type, scale, climate) rather than flattened into one number.
- Business outputs are labelled scenario estimates, and no blocked claim is stated as fact.
- Canon and runtime are in sync, and the vault export matches the JSON.
- The vault capture for the work is done: findings, decisions, status, and any checkpoint ticked in the Simulation Progress Tracker.
- The PR doesn't edit files that another open PR owns.

## Log

### save-point-002 (2026-11-26)

- **Commit:** the merge commit of PR #28 on `main`, after PRs #20 to #28 and Approval Batch 002.
- **What it holds:**
  - Nitrate sinks: water exchange (approved) and a calibrated residual loss (candidate). Nitrate holds near 43 mg/L at the UVI feed ratio.
  - The P1 equipment research (51 candidates, 12 approved for scenario use) and the MIDH 2025 India structure norms.
  - The Simulation Progress Tracker (6 of 16 checkpoints).
- **Checks:** to be confirmed on the merge commit: tests, `check_mvp_integrity.py --quick`, runtime sync dry run and vault export dry run.
- **Open at this point:** the residual nitrate loss and 39 equipment values stay candidates; heating, fish growth and validation are not modelled; state subsidy top-ups are not read.

### save-point-001 (2026-11-25)

- **Commit:** `07ce825` on `main`, after PRs #1 to #19 and Approval Batch 001.
- **What it holds:**
  - Basil grown to a 28-day harvest, calibrated to UVI.
  - A candidate biofilm nitrification model and growth-based basil nitrate uptake.
  - Basil aquaponic pH scoring (evidenced edges accepted).
  - The basil gross revenue range, now with approved inputs.
  - The unit design comparison for the Netherlands and the Indian states.
  - The component catalog and cost-per-kg configurator.
  - The local runner (`run.bat`).
  - Obsidian truths with reliability fields, and the Gatekeeper rules.
- **Checks:** 189 tests OK. `check_mvp_integrity.py --full` PASS, protected paths clean. Runtime sync dry run: no changes. Vault export dry run: 0 to write, 0 stale.
- **Open at this point:**
  - Batch 002 items: TN, AP and TG basil prices, the all-India band, the sensitivity locations, the NL lettuce price, the EPS/XPS raft lives and two conflicting design rules.
  - 13 older truths have no reliability record yet.
  - The nitrate balance has no sinks besides plant uptake, so it runs to about 161 to 180 mg/L at the UVI feed ratio.
  - Standing biomass is still a placeholder.
  - Fish revenue, heating, CAPEX and logistics are not in the cost lines.

## Related Notes

- [[Project/Feasibility Register|Feasibility Register]]
- [[Project/Decisions Log|Decisions Log]]
