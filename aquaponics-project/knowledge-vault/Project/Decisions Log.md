# Decisions Log

Newest first. Each entry gives the decision, why, and who made it.

## 2026-11-26: pH buffer (UQ-018)

- **Model pH from an alkalinity balance and a held dissolved CO2, opt-in per scenario.** Why: the old fixed drift had no buffer. CO2 is held, not modelled, because no CO2 transfer rate for rafts or media beds was found. Proposed by Claude, pending Ajit's review.
- **Credit no alkalinity returns by default (NH3 excretion, denitrification, plant nitrate uptake all 0), and report them as an upper-bound band.** Why: none is measured in aquaponics, and 0 is the conservative end (more base). The pH-free runs show the defaults drain alkalinity far faster than any real system, so the default needs your decision once UQ-019 has evidence. Proposed by Claude, pending Ajit's review.
- **Keep scoring validation with pH held at the published mean.** Why: the papers give no alkalinity, source water or base use, so a pH-free run is an assumption band, not a test. The pH-free runs are reported, not scored. Proposed by Claude.
- **File research that lived only in project files into the repo.** The equipment inventory report and notes, the P1 research notes, the research prompts and the farm viability inputs now sit in `data/sources/research_reports/`, `data/sources/research_prompts/`, `data/scenarios/`, `docs/` and `Learnings/`. Why: Ajit asked that every file and learning be in its proper folder. Asked by Ajit.

## 2026-11-26: Validation round 3

- **Hold pH at the published mean in validation runs.** Why: the daily pH drift has no alkalinity buffer, so an uncontrolled run drifts away from the pH the paper measured and changes the plant score. A real buffer model is ticket UQ-018. Proposed by Claude, pending Ajit's review.
- **Do not add a basil establishment lag.** Why: three raft studies show the first cut grows about as fast as later cuts; only UVI staggered planting shows a lag. UQ-016 closed as not supported. Proposed by Claude.
- **Score Knaus basil at the midpoint of its light band and report the two ends as sensitivity.** Why: the paper does not give the photoperiod, so both ends are bounds, not estimates. Proposed by Claude, pending Ajit's review.
- **Score Savidov fish against the report's stated 0.50 to 0.64 kg per fish, and keep Khater FCR reported but unscored.** Why: the 630 g point assumes no mortality; Khater's FCR is below every Tier 1 range and cannot be recomputed. Proposed by Claude, pending Ajit's review.

## 2026-11-26: Component checkpoints (P1 gaps, missing categories, NL and India on every part)

- **Fill empty catalog slots with new candidates, and hold the rest in `candidates_batch_004_v0.jsonl`.** Wired in: trough walls (NL cellular block, pine plank, hollow block; India concrete block), NL fingerlings, India basil seed, NL lettuce seed, NL K1 biofilter media, India expanded clay, and parts in the new categories. Held: a second NL tilapia feed (Lets-Grow), the German catfish farm model (context), a Crompton pump with no usable flow rating, and conflicting Bengaluru and out-of-date Hyderabad water tariffs. All pending Batch 004. Asked by Ajit.
- **Add the missing categories as opt-in add-ons, not into the base builds.** Lighting, monitoring, water treatment, backup power, harvest crates and propagation now have NL and India parts. The base builds stay as they were apart from the newly priced slots, so earlier results remain comparable. Why: most new parts have no sourced lifetime or count, so adding them by default would mix known and unknown costs. Proposed by Claude.
- **Size backup power on the chosen pumps and aeration, trough walls on the liner geometry, and one meter or kit per system.** Lights use the maker's stated coverage; hours per day are a user setting because no source gives them. Any count or hours a user sets goes in `component_overrides` and is their own assumption. Proposed by Claude.
- **A part role may be missing in one market only with a written reason.** Two are: heating in India (Indian polyhouses are not heated, HEAT_0009) and generators in India (the only listing looked like a placeholder). A test checks this. Proposed by Claude.
- **Telangana's 2025-26 protected-cultivation table stays a gap.** The state site refuses connections from both the cloud and Ajit's PC. It needs a download from an Indian network or VPN. Recorded by Claude.

## 2026-11-26: Basil and gravel-bed validation fixes

- **Treat established cut-and-regrow basil as a closed canopy.** Above the UVI density (8 plants/m²), yield per m² stays flat instead of following a baby-leaf density curve. Why: UVI plants are already about 250 g each, and two raft trials at 20 to 23 plants/m² show no per-m² gain. The baby-leaf exponent stays as a sensitivity case. Proposed by Claude, pending Ajit's review.
- **Model gravel grow beds as media volume, not raft area.** Range 1.0 to 3.6 kg feed per m³ of gravel per day. The simulator default is the low end, which is conservative. Why: gravel is a different nitrifying surface from a raft, and the published validation case only fits near the upper end. Proposed by Claude, pending Ajit's review.
- **Fix the cause, not the result:** the remaining basil miss (young transplants) is a new ticket, UQ-016, not a tuned number. Proposed by Claude.

## 2026-11-26: Multi-market checkpoint

- **Tie every price to a market: region, currency and price year.** Retail listings take the year they were read, sourced documents take the year they state, and anything else is marked "not recorded" and flagged, never guessed. A build refuses a price in another currency. Why: the model has to generalise to many markets without mixing currencies or vintages. Proposed by Claude.
- **A new country is data only.** A test adds a stub third market from data and runs the configurator and the swaps on it with no code change. Proposed by Claude.

## 2026-11-26: Swaps checkpoint

- **Price other architectures from a sourced yield ratio against the raft, and only where a study gives a number.** NFT uses 0.83 to 0.95 of the raft yield. The media bed stays without a yield, because "not significantly different" is not a measured ratio. Batch 003 can accept parity as Ajit's own assumption. Proposed by Claude.
- **Compare swaps as patches on a base build, and show gaps next to each change.** A swap can change the architecture, the heating source or one part. A swap that opens a cost gap is flagged as not like-for-like rather than given a filled-in number. Why: Ajit wants game-like part choices, and an unpriced part must not look free. Proposed by Claude.
- **Model a heat pump as the same heat demand delivered with electricity.** Heat (kWh) is gas m³ × 8.63 to 8.79 kWh per m³, and electricity is heat ÷ a seasonal COP of 3.7 to 4.6. The heat-demand values themselves stay with the heating and climate thread. New values pending Batch 003. Proposed by Claude.

## 2026-11-26

- **Approve Batch 004 as recommended.** Approved: truths BYR_0005 and NITR_0015, and four corroborated Tier 3 prices for scenario use (Lumatek Zeus 600 and SanLight EVO 4-120 LEDs and the pH tester in the Netherlands, KOH pH base in India). Models and everything else stay candidates. Decided by Ajit (15:57 Europe/Amsterdam).

- **Approve Batch 003 as recommended.** Approved: heat pump COP and gas heat per m³ (NL), the India fan-pad polyhouse price, and truths CD_0011, CD_0012, HEAT_0002, HEAT_0004, HEAT_0005, HEAT_0009, FISH_0001 to FISH_0004, FISH_0006, FISH_0007, FISH_0009, BYR_0001 and BYR_0002. Models and everything else stay candidates. Media-bed yield parity (B8) was not chosen, so it stays a gap. Decided by Ajit (05:54 Europe/Amsterdam).

- **Fix the tilapia temperature curve and add basil density and light responses as candidates, and leave the gravel-bed nitrogen issue open.** Why: these were the two largest validation failures, and both now rest on measured, peer-reviewed curves. Both fixes leave the UVI anchor unchanged. Asked by the coordinator while Ajit was away; waiting on Ajit's review in Batch 003.
- **Validate against Knaus 2018, Savidov 2005 and Khater 2023, logging failures instead of retuning.** Why: no open source outside UVI gives a full coupled basil raft record, so each system checks different metrics. Recalibrating now would hide the failures before Ajit has seen them. Decided by Claude for the validation checkpoint; waiting on Ajit's review.
- **Make the new tilapia growth model opt-in per scenario and keep feed as a direct input.** Why: the MVP baseline is Mode A direct feed input, and the starter fixtures feed the P2a checks, so only the two basil raft crop-cycle scenarios switch to the new model. The SRAC size table is available as an option. Decided by Claude for the Fish growth and feed checkpoint; waiting on Ajit's review.
- **Model greenhouse heat demand with one calibrated loss coefficient, and hold every value for Batch 003.** Why: no source gives the cover-to-floor ratio or a basil heat demand. Calibrating to a published Dutch figure and checking against a second figure keeps the model tied to evidence. Solar utilisation can't be pinned down, so results are given as a range across its physical bounds (0 to 1). Decided by Claude for the Heating and climate checkpoint; waiting on Ajit's review.
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
