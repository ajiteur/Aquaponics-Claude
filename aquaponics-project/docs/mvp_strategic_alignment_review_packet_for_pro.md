# MVP Strategic Alignment Review Packet For Pro

## 1. Purpose

Prepare a concise source packet for a later Pro-model strategic review.

The packet should help answer:

- whether the work completed so far is strategically aligned with the seed-MVP
  goal
- whether the future roadmap is still the right priority path
- which next step should be pursued, deferred, or blocked
- which claims must remain off-limits until the required inputs exist

This is a review/preparation artifact only. It does not decide the roadmap and
does not propose code diffs.

## 2. Seed-MVP Goal

Build and validate an evidence-backed aquaponics planning engine that turns fish
feed into water-quality, biofilter, aeration, and business-risk insights for a
tilapia + basil DWC/raft system, while keeping basil saleable output unresolved
unless observed or explicitly reviewed.

Product thesis:

- Start from a driver operators understand: daily fish feed.
- Translate feed into TAN-N load, nitrification oxygen demand, and alkalinity
  demand.
- Add water-quality risk interpretation only when the missing physical context
  is supplied.
- Add aeration, solids, and business-risk interpretation as separate layers.
- Preserve explicit uncertainty instead of making premature safety,
  profitability, or basil-saleability claims.

## 3. Current Implementation Summary

Recent relevant commits visible in git log:

| Commit | Summary |
| --- | --- |
| `e7809d1` | Design MVP fish feed waste TAN engine. |
| `b098df0` | Add MVP feed to TAN load calculator. |
| `9b9d8fb` | Review tilapia feed research for MVP engine. |
| `78a37eb` | Plan Mode A feed load report integration. |
| `a567003` | Add Mode A feed load report builder. |
| `3135abe` | Add Mode A feed load demo runner. |
| `84bd1de` | Add Mode A feed load customer demo walkthrough. |
| `6694c86` | Design P1 TAN concentration and NH3 risk layer. |

Implemented assets inspected:

- `src/feed_waste_tan_loads.py`
- `src/mvp_mode_a_feed_load_report.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `tests/test_feed_waste_tan_loads.py`
- `tests/test_mvp_mode_a_feed_load_report.py`
- `tests/test_build_mvp_mode_a_feed_load_report.py`

Current Mode A calculation helper:

- requires direct `feed_kg_day`
- requires direct `protein_fraction`
- validates feed as numeric, finite, and non-negative
- validates protein fraction as numeric, finite, and between `0` and `1`
- calculates:
  - `tan_n_load_kg_day`
  - `tan_n_load_g_day`
  - `oxygen_demand_g_day`
  - `alkalinity_demand_g_caco3_day`
- explicitly excludes TAN concentration, unionized NH3 toxicity, feed cost,
  tank suitability, biomass-derived feeding, biofilter removal, and
  `saleable_harvest_mass_kg`

Current Mode A report builder:

- accepts required Mode A direct-feed inputs plus optional context-only fields
- calls the load helper
- returns stable sections:
  - `scenario_id`
  - `input_mode`
  - `inputs`
  - `optional_context`
  - `loads`
  - `calculation_basis`
  - `status_labels`
  - `boundary_notes`
- emits missing-context labels for concentration, NH3 risk, feed cost, tank
  suitability, biofilter removal, and basil saleable output

Current demo runner:

- reads explicit JSON from `--input`
- prints formatted deterministic JSON to stdout
- writes no files or runtime artifacts
- validates missing, invalid, or unsupported inputs

Current example input:

- `scenario_id = demo_mode_a_tilapia_basil_dwc`
- `input_mode = mode_a_direct_feed`
- `feed_kg_day = 1.0`
- `protein_fraction = 0.32`
- `feed_class = grow_out`
- `protein_basis = scenario_default_candidate_from_tilapia_feed_research`
- `architecture_context = tilapia_basil_dwc_raft`
- all supported context booleans set to `false`

Current example output load values:

- `tan_n_load_kg_day = 0.02944`
- `tan_n_load_g_day = 29.44`
- `oxygen_demand_g_day = 134.5408`
- `alkalinity_demand_g_caco3_day = 210.2016`

## 4. Current Docs/Research Summary

Design/review docs inspected:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_tilapia_feed_research_ingestion_review.md`
- `docs/mvp_mode_a_feed_load_integration_surface_plan.md`
- `docs/mvp_mode_a_feed_load_customer_demo_walkthrough.md`
- `docs/mvp_p1_tan_concentration_nh3_risk_design.md`

Research inputs inspected:

- `data/sources/research_reports/markdown/Tilapia feed-regime and stocking-input research pack for a first fish-feed-to-water-quality MVP.md`
- `data/sources/research_reports/markdown/Tank Volume, Exchange and TAN-to-NH3 Risk Research Pack.md`
- `data/sources/research_reports/markdown/Aeration Capacity and Solids Load Translation Research Pack for the Aquaponics MVP.md`

Supporting first-slice/business/architecture docs inspected:

- `docs/first_slice_runtime_native_harvest_output_plan.md`
- `docs/first_slice_adapter_saleable_harvest_null_status_design.md`
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `docs/first_slice_architecture_runtime_plan.md`
- `data/sources/research_reports/markdown/Architecture-Specific CAPEX Basis and Maintenance Driver Research Pack for Media Bed, DWC, and NFT Aquaponics.md`
- `data/sources/research_reports/markdown/Architecture-specific business drivers for media bed, DWC, and NFT in aquaponics.md`

Missing inputs:

- None of the requested exact research/doc paths were missing.

## 5. What Has Been Proven

Repo evidence supports these claims:

- Mode A direct feed input is implemented and tested.
- The load helper correctly calculates TAN-N load, nitrification oxygen demand,
  and alkalinity demand for direct feed and protein inputs.
- The report builder can wrap those load outputs in a stable report shape.
- The demo runner can read an explicit JSON input and print valid JSON to
  stdout without writing runtime artifacts.
- The current demo can explain why missing context blocks TAN concentration,
  NH3 risk, feed cost, tank suitability, biofilter removal, and basil
  saleability.
- The research stack supports Mode A as a safer first path than Mode B because
  daily feed and feed protein are direct load drivers.
- The P1 research supports a future three-stage load / concentration / NH3 risk
  chain.
- The P1.5 research supports a future aeration and solids layer, but not as a
  simple extension of nitrification oxygen alone.

Strategic proof level:

- The repo has a working evidence-backed feed-to-load slice.
- It has not yet proven water-quality safety, system safety, profitability, or
  saleable basil output.

## 6. What Has Not Been Proven

The current implementation does not prove or calculate:

- TAN concentration
- unionized NH3 risk
- fish safety
- whole-system safety
- biofilter removal
- total oxygen demand
- aeration adequacy
- DWC root-zone oxygen adequacy
- solids mass, wet sludge, TSS concentration, or solids-removal capacity
- feed cost
- tank suitability
- stocking-density suitability
- Mode B fish-biomass-derived feeding
- business profitability
- basil `saleable_harvest_mass_kg`
- basil revenue

The current demo also does not validate customer willingness or ability to
provide the next inputs: water volume, pH, temperature, flow/retention,
biofilter state, aeration capacity, solids-removal context, feed price, or
observed saleable harvest mass.

## 7. Current Assumptions And Constraints

Current strategic assumptions:

- Tilapia + basil is the first bounded slice.
- DWC/raft is the baseline architecture for the MVP demo.
- DWC/raft is directionally supported, not a permanent canonical winner.
- Mode A direct daily feed input is the first implementation path.
- `protein_fraction = 0.32` is a demo/scenario candidate, not canon.
- UVI-like volumes, flows, residence times, aeration patterns, and maintenance
  anchors are demo assumptions, not canon.
- Feed cost remains a scenario/business input.
- Basil saleable output remains unresolved/null unless observed or explicitly
  reviewed.
- No TAN concentration or NH3 safety claim exists until P1 is implemented with
  pH, temperature, volume, time basis, and threshold basis.
- No total oxygen or aeration adequacy claim exists until P1.5 is designed and
  implemented with capacity context.

Hard constraints to preserve:

- Do not infer `saleable_harvest_mass_kg`.
- Do not treat TAN-N load as TAN concentration.
- Do not model NH3 risk from TAN alone.
- Do not treat nitrification demand as actual biofilter removal.
- Do not treat nitrification oxygen demand as total oxygen demand.
- Do not treat oxygen demand as aeration capacity.
- Do not calculate feed cost without feed price.
- Do not claim system safety or profitability from the current demo.

## 8. Evidence Support Summary

Mode A support:

- The tilapia feed research supports direct daily feed input as the safest first
  implementation path.
- Feed amount plus protein fraction is the direct basis for TAN-N load.
- Mode B is supportable later but needs fish count, average weight, feeding-rate
  table, stage context, and biomass update logic.

P1 concentration/NH3 support:

- The tank-volume/TAN-to-NH3 research supports separating load, concentration,
  and NH3 risk.
- Concentration requires control volume, time basis, and scope.
- NH3 risk requires TAN-N concentration, pH, water temperature,
  freshwater/salinity assumption, and threshold basis.
- Fish-tank exposure and whole-system average are not equivalent.
- Recommended first P1 scope is fish-tank upper-bound/no-removal concentration.

P1.5 aeration/solids support:

- The aeration/solids research supports nitrification oxygen demand as a valid
  sub-load but not total oxygen risk.
- Total oxygen context must account for fish respiration and organic-waste
  decomposition in addition to nitrification.
- DWC/root-zone aeration is a separate subsystem; fish-tank aeration does not
  prove root-zone oxygen adequacy.
- Feed can support a provisional dry-solids potential estimate, but not wet
  sludge, TSS concentration, or removal capacity without more inputs.

Business and architecture support:

- Business-layer docs require explicit upstream saleable yield, feed, energy,
  risk, and event inputs before real economics.
- Architecture docs support DWC/raft as the first baseline and business-relevant
  architecture context, but not as a universal winner.
- Architecture business research supports treating DWC/raft, NFT, and media bed
  as different business archetypes rather than one generic plant subsystem.

Deferred evidence areas:

- feed price by geography/date/supplier
- saleable basil harvest mass
- actual biofilter removal efficiency
- total oxygen capacity
- fish respiration model
- solids-removal efficiency
- customer-specific operating practices

## 9. Roadmap Options For Pro Review

| Option | Upside | Risk | Dependency | Unlocks | Might overclaim | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| A. Implement isolated P1 TAN/NH3 chemistry helper now | Small, testable, evidence-backed next engineering step; keeps chemistry separate from report integration. | Could still feel abstract without report/demo integration. | P1 field names, freshwater basis, no-removal concentration policy. | Tested concentration/NH3 primitives. | Fish safety if thresholds are added too early. | Pursue now if Pro agrees P1 is the next layer. |
| B. Integrate P1 into Mode A report builder now | Makes current demo more useful by resolving one major missing-context label. | Higher surface area; risk of mixing concentration and risk wording into the report before helper contract is stable. | Option A or equivalent helper; report shape decisions. | A richer customer/advisor demo. | System safety, fish safety, daily average vs peak certainty. | Pursue later or immediately after A. |
| C. Design P1.5 aeration/solids layer before implementing P1 | Captures oxygen and solids risks that may matter more to operators than NH3 chemistry alone. | Delays the clean P1 chemistry implementation; could expand scope. | P1.5 design pass; capacity and solids terminology. | Better roadmap clarity for aeration/solids before code. | Total oxygen adequacy from nitrification demand. | Pursue now if Pro thinks operator value is oxygen/solids-first; otherwise pursue after A. |
| D. Implement P1.5 first | Directly addresses aeration and solids business-risk hooks. | Not ready: research exists, but no repo-side design doc or helper contract yet. | P1.5 design, capacity basis, solids-basis decisions. | Aeration/solids report layer. | Aeration capacity, total oxygen risk, TSS/removal certainty. | Block for now; design first. |
| E. Run customer/advisor demos before more implementation | Tests whether current uncertainty-forward demo is credible and which missing context users care about most. | Slower technical progress; feedback may be noisy from a minimal CLI output. | Demo walkthrough and current runner. | Prioritized next layer from real audience pull. | None if framed honestly. | Pursue now in parallel with Pro review. |
| F. Shift back to basil saleability/revenue | Reopens the business outcome that ultimately matters for basil revenue. | Still blocked by missing observed/reviewed saleable harvest mass; risks proxy inference. | Runtime-native saleable harvest output or explicit reviewed manual value. | Crop revenue path. | Saleable mass, revenue, shrink, buyer acceptance. | Block until observed/reviewed saleable mass exists. |
| G. Shift to business/feed-cost economics | Feed cost is a natural business hook from feed input. | Feed price is geography/date/supplier-specific; can become fake precision quickly. | Explicit feed price, currency, date basis, market level. | Basic scenario feed-cost sensitivity. | Profitability or canonical feed cost. | Pursue later as scenario-input economics, not canon. |

From repo evidence alone, the strongest priority paths are:

1. Pro review of A versus E/C sequencing.
2. If implementing next, add isolated P1 helper before report integration.
3. Run customer/advisor demo feedback in parallel.
4. Keep P1.5 as design-before-implementation.
5. Keep basil revenue and feed-cost economics deferred until their required
   inputs exist.

## 10. Fake-Precision And Strategic-Risk Traps

Key traps to flag for Pro:

- TAN-N load is not TAN concentration.
- TAN-N, TAN, NH3-N, and NH3 are different bases.
- Fish-tank exposure is not the same as whole-system average.
- Daily average is not the same as post-feeding peak.
- Nitrification oxygen demand is not total oxygen demand.
- Oxygen demand is not aeration capacity.
- Fish respiration is not modelled yet.
- DWC/root-zone aeration is not covered by fish-tank aeration.
- Gross dry-solids potential is not wet sludge.
- Gross dry-solids potential is not TSS concentration.
- Feed-linked solids potential is not solids-removal capacity.
- Nitrification demand is not actual biofilter removal.
- DWC/raft demo assumptions are not canon.
- UVI-like anchors are useful benchmark assumptions, not universal defaults.
- Feed cost must remain a scenario/business input, not a canonical biology
  value.
- Saleable harvest mass remains unresolved/null.
- Architecture context is not a pricing or saleability selector by itself.

Strategic-risk trap:

- Expanding too quickly from a credible load model into safety, capacity, or
  profitability claims could damage trust. The current repo's strongest
  strategic asset is disciplined boundary management.

## 11. Strategic Questions For Pro

Ask Pro to answer:

1. Is the current sequence strategically coherent for the seed-MVP goal?
2. Should the next technical pass be isolated P1 TAN/NH3 helper, P1 report
   integration, or P1.5 aeration/solids design?
3. Should customer/advisor demos happen before more implementation, in parallel,
   or after P1?
4. Is fish-tank upper-bound/no-removal concentration the right first P1 scope?
5. Should system-average concentration wait, or should it be implemented
   alongside fish-tank scope with strong warnings?
6. Is the current CLI/demo format enough for advisor feedback, or does it need a
   more readable report before demos?
7. Which missing-context label is most strategically important to resolve next:
   TAN concentration, NH3 risk, aeration capacity, solids context, feed cost, or
   crop saleable output?
8. Does P1.5 aeration/solids deserve a design pass before any more code?
9. Should feed-cost economics be delayed until customer inputs exist, or added
   as a scenario-only sensitivity layer?
10. Should basil saleability remain paused until observed/reviewed output, or is
    there a strategically valuable non-revenue crop-side demo to run first?
11. What claims should be forbidden in customer or investor demos until further
    evidence exists?
12. What would make this MVP compelling enough for seed-stage technical
    diligence without overbuilding?

## 12. Paste-Ready Pro Review Prompt

Use this prompt directly in Pro:

```text
You are reviewing strategic alignment for an aquaponics seed-MVP repo.

Seed-MVP goal:
Build and validate an evidence-backed aquaponics planning engine that turns fish
feed into water-quality, biofilter, aeration, and business-risk insights for a
tilapia + basil DWC/raft system, while keeping basil saleable output unresolved
unless observed or explicitly reviewed.

Current state:
- Mode A direct-feed path is implemented and tested.
- Inputs: feed_kg_day and protein_fraction.
- Outputs: tan_n_load_kg_day, tan_n_load_g_day, oxygen_demand_g_day,
  alkalinity_demand_g_caco3_day.
- Report builder wraps these in a stable report with inputs, optional_context,
  loads, calculation_basis, status_labels, and boundary_notes.
- Demo runner reads JSON and prints deterministic JSON to stdout.
- Current example uses feed_kg_day=1.0 and protein_fraction=0.32, yielding:
  tan_n_load_kg_day=0.02944, tan_n_load_g_day=29.44,
  oxygen_demand_g_day=134.5408, alkalinity_demand_g_caco3_day=210.2016.
- Current report explicitly does not calculate TAN concentration, NH3 toxicity,
  feed cost, tank suitability, biofilter removal, Mode B biomass-derived
  feeding, or basil saleable output.

Evidence summary:
- Tilapia feed research supports Mode A direct feed as the safest first
  implementation path. Mode B is supportable later but needs fish count,
  average weight, stage/size feeding-rate tables, and biomass updates.
- P1 tank-volume/TAN-to-NH3 research supports separate stages: load ->
  concentration -> NH3 risk. TAN concentration needs control volume and time
  basis. NH3 risk needs TAN-N concentration, pH, temperature,
  freshwater/salinity basis, and threshold unit basis.
- Recommended P1 first scope from current design is fish-tank upper-bound /
  no-removal concentration. System-average is useful but not equivalent to
  fish-tank exposure.
- P1.5 aeration/solids research supports nitrification oxygen as a valid
  sub-load but not total oxygen risk. Total oxygen also needs fish respiration
  and organic-waste decomposition. DWC/root-zone aeration is separate from
  fish-tank aeration. Feed can support provisional dry-solids potential, not wet
  sludge or TSS concentration.
- UVI-like values are useful demo assumptions for DWC/raft, not canon.
- Feed cost remains scenario/business input. Basil saleable_harvest_mass_kg
  remains unresolved/null unless observed or explicitly reviewed.

Decision needed:
Which next path best advances the seed-MVP without fake precision?

Options:
A. Implement isolated P1 TAN/NH3 chemistry helper now.
B. Integrate P1 into the Mode A report builder now.
C. Design P1.5 aeration/solids before implementing P1.
D. Implement P1.5 first.
E. Run customer/advisor demos before more implementation.
F. Shift back to basil saleability/revenue.
G. Shift to business/feed-cost economics.

Known traps:
- TAN-N load != TAN concentration.
- TAN-N, TAN, NH3-N, and NH3 need explicit unit basis.
- Fish-tank exposure != whole-system average.
- Daily average != post-feeding peak.
- Nitrification oxygen demand != total oxygen demand.
- Oxygen demand != aeration capacity.
- Fish respiration is not modelled yet.
- DWC root-zone aeration is not covered by fish-tank aeration.
- Dry-solids potential != wet sludge or TSS concentration.
- Nitrification demand != actual biofilter removal.
- Feed cost is scenario input, not canon.
- saleable_harvest_mass_kg remains unresolved/null.

Please evaluate:
1. Is the current path strategically coherent from repo evidence alone?
2. Which option should be pursued now, pursued later, or blocked?
3. Is fish-tank upper-bound/no-removal the right first P1 scope?
4. Should customer/advisor demos run before or alongside P1 implementation?
5. Does P1.5 aeration/solids need a design pass before code?
6. Which claims must remain forbidden in demos?
7. What minimum next artifact would most improve seed-MVP credibility?
```

## 13. Recommended Immediate Next Action Before Pro Review

Do not implement another layer before Pro review unless the decision is already
made.

Recommended immediate action:

- Paste the Section 12 prompt into Pro.
- Ask Pro to rank options A-G and identify the top false-precision risk.
- After Pro review, choose one narrow next pass:
  - P1 helper implementation,
  - P1 report integration,
  - P1.5 aeration/solids design,
  - or customer/advisor demo feedback synthesis.

Do not shift to basil revenue until `saleable_harvest_mass_kg` has an observed
or explicitly reviewed source. Do not shift to feed-cost economics unless feed
price is provided as an explicit scenario/business input.
