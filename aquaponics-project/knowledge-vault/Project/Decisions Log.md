# Decisions Log

Newest first. Each entry gives the decision, why, and who made it.

## 2026-11-25

- **Find the unit design with workable unit economics before the go/no-go.** Compare system type, scale, crop, labour model and location, then decide on the farm. Decided by Ajit.
- **Compare two locations side by side: the Netherlands and India.** For India, cover Karnataka, Tamil Nadu, Andhra Pradesh and Telangana. Decided by Ajit.
- **Record reliability with every new value.** Each value gets a source tier, a confidence level and the reason for it, in canon and in the vault. Decided by Ajit.
- **Accept the UVI basil crop-cycle values.** 8 plants/m², 28-day growing period, 2.0 kg/m² per harvest and related context, plus truths CROP_0001 to CROP_0007, are now accepted. Decided by Ajit.
- **Capture all learnings in Obsidian, split by trust level.** Truths (evidence-backed, one note each), simulation findings, decisions, inbox. Why: you use Obsidian as your local knowledge base. Decided by Ajit.
- **Fix the simulator, not a manual harvest value.** Basil harvest mass comes from a simulation calibrated to the UVI yield anchor, not from a hand-entered number. Why: the farm decision and the game both need a real prediction engine. Decided by Ajit.
- **Add a scenario-estimate mode to the rules.** Revenue and viability can be discussed only as labelled, sourced ranges. Why: the old rules blocked the farm go/no-go entirely. Proposed by Claude, approved by Ajit.
- **Move to a Claude-based repo.** `ajiteur/Aquaponics-Claude` is now the main repo, and the old `Aquaponics` repo is kept as upstream. A full copy is at `Documents\Aquaponics-Claude`. Canonical data is now tracked in git; before this it existed only on your PC. Decided by Ajit.
- **Restart the project with a goal.** Use the engine to decide on a real farm, with an original simulation game as the fallback. Decided by Ajit.

## Related Notes

- [[Project/Project|Project]]
