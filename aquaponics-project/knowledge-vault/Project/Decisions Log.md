# Decisions Log

Newest first. Each entry gives the decision, why, and who made it.

## 2026-11-26

- **Shelve the farm go/no-go; build the strongest simulation for the Netherlands and India in parallel.** Why: if the simulation is strong, moving to a real farm is straightforward, and the engine should work across many markets. Decided by Ajit.
- **Run the P1 equipment research and hold the results for Batch 002.** Only values that fit an existing catalog slot are wired in (India polyhouse and shade-net life, India water price, NL basil seed). Everything else waits in `data/catalog/candidates_batch_002_v0.jsonl`. Asked by Ajit.
- **Use the MIDH 2025 Annexure V norms as the India national reference for protected structures, held for Batch 002.** NVPH tubular Rs 1000-1200/m2 and bamboo shade net Rs 450/m2 (plains) supersede the older 650-935 and 200-414 ranges, but the catalog values are not changed until Ajit approves. These are subsidy cost ceilings, not market prices. Telangana's 2025-26 state table could not be downloaded and stays a gap. Ajit supplied the PDF; Claude extracted it.
- **Approve Batch 002 as recommended.** Approved: nitrate water exchange of 1.5% per day (C1), NITR_0009 and NITR_0010 (D1), 12 corroborated equipment values (E1), and the MIDH 2025 norms as India structure prices: NVPH ₹1,000 to ₹1,200/m², bamboo shade net ₹450/m², labelled as subsidy ceilings (F1). Everything else stays a candidate or a sensitivity case. Approvals are recorded next to each value. Decided by Ajit (2026-11-26 01:33 Europe/Amsterdam).

## 2026-11-25

- **Model nitrate removal as water exchange plus a calibrated residual loss.** Water exchange uses UVI's 1.5 percent a day. Denitrification and solids N have no published rate, so one lumped loss fraction is calibrated to UVI's basil nitrate level and cross-checked against a peer-reviewed N budget. Candidate, pending Batch 002. Proposed by Claude; asked for by Ajit.
- **Approve batch 001 as recommended.** Accepted truths: NITR_0002, 0004, 0006; UE_0002, 0005, 0007, 0009, 0010; CD_0001 to 0003. Accepted the evidenced edges of the basil aquaponic pH scoring; the 6.2 to 6.9 band stays an assumption. Approved for scenario use only (not canon): Netherlands basil price and saleability, Karnataka basil price ₹100 to ₹250/kg, India saleability, Karnataka wage and electricity, and the catalog values except the EPS/XPS raft lives and two conflicting design rules. Everything else stays a candidate. Each approval is recorded next to its value. Decided by Ajit.
- **Apply the equipment inventory cross-check to the catalog.** Upgrade India fingerlings (Rs 4) and Dutch water to corroborated, flag nine shaky catalog values without changing them, and fill the India pump price with a candidate (Crompton 0.5 HP, Rs 13,400). Why: the 2026-11-25 equipment inventory agreed on most design rules but found failure data and rate mismatches. Asked by Ajit.
- **Research the remaining equipment in small batches.** The backlog is in `docs/equipment_research_backlog.md`. Run two or three researchers at a time to stay under the shared page-read limit. Proposed by Claude.
- **Start from cost of production, not market price.** Build a component library and a configurator that report cost per kg by component, with alternatives, before layering on logistics and market costs. Long-term goal: a worldwide database of components, fish and plants to find the configuration with the best output. Decided by Ajit.
- **Keep the component catalog outside canon for now.** It lives in `data/catalog/` as candidate inputs. Approved values move to `data/knowledge/business/` in a separate canon pass. Why: most prices are shop listings (tier 3) and need your approval first. Proposed by Claude, pending Ajit's review.
- **Use ₹65-180/kg as the India basil base price in the comparison.** Why: Ajit confirmed basil costs that much in Bangalore, matching ten Bengaluru B2B listings. The ₹600-1,000/kg study band is demoted to a sensitivity case. Formal approval of the value is pending in the approval batch.
- **Find the unit design with workable unit economics before the go/no-go.** Compare system type, scale, crop, labour model and location, then decide on the farm. Decided by Ajit.
- **Compare two locations side by side: the Netherlands and India.** For India, cover Karnataka, Tamil Nadu, Andhra Pradesh and Telangana. Decided by Ajit.
- **Use the raft surface as the nitrification capacity, and plant growth for nitrate uptake.** Replaces two placeholders (PR #6 and its follow-up). Values are candidates pending Ajit's review. Proposed by Claude.
- **Check reliability for every new learning.** Each new truth or manual input records its source tier, source gate, confidence with a reason, and corroboration, in canon and in the vault. Tier 3 or single-source items stay candidate. Why: we need to know how far each piece of knowledge can be trusted. Decided by Ajit.
- **Run work as parallel threads with a Gatekeeper.** One workstream per thread. The Gatekeeper reviews every PR and tags save points on main once Ajit merges. Decided by Ajit.
- **Accept the UVI basil crop-cycle values.** 8 plants/m², 28-day growing period, 2.0 kg/m² per harvest and related context, plus truths CROP_0001 to CROP_0007, are now accepted. Decided by Ajit.
- **Capture all learnings in Obsidian, split by trust level.** Truths (evidence-backed, one note each), simulation findings, decisions, inbox. Why: you use Obsidian as your local knowledge base. Decided by Ajit.
- **Fix the simulator, not a manual harvest value.** Basil harvest mass comes from a simulation calibrated to the UVI yield anchor, not from a hand-entered number. Why: the farm decision and the game both need a real prediction engine. Decided by Ajit.
- **Add a scenario-estimate mode to the rules.** Revenue and viability can be discussed only as labelled, sourced ranges. Why: the old rules blocked the farm go/no-go entirely. Proposed by Claude, approved by Ajit.
- **Move to a Claude-based repo.** `ajiteur/Aquaponics-Claude` is now the main repo, and the old `Aquaponics` repo is kept as upstream. A full copy is at `Documents\Aquaponics-Claude`. Canonical data is now tracked in git; before this it existed only on your PC. Decided by Ajit.
- **Restart the project with a goal.** Use the engine to decide on a real farm, with an original simulation game as the fallback. Decided by Ajit.

## Related Notes

- [[Project/Project|Project]]
