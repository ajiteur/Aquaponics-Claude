# MVP Tilapia Feed Research Ingestion Review

Status: `draft`

## 1. Purpose

- Review the new tilapia feed-regime and stocking-input research pack against the MVP fish/feed/waste/TAN engine plan.
- Confirm whether the committed Mode A helper at `b098df0` remains aligned with the evidence.
- Classify research findings for later repo use without promoting values into canon.

## 2. Scope

- This is a docs-only ingestion review.
- It does not modify canonical biology, model, business, runtime, script, or helper files.
- It does not propose final implementation diffs.
- Basil `saleable_harvest_mass_kg` remains unresolved/null unless observed or explicitly reviewed.

## 3. Inputs Reviewed

Primary new research input:

- `data/sources/research_reports/markdown/Tilapia feed-regime and stocking-input research pack for a first fish-feed-to-water-quality MVP.md`

Existing project inputs:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `src/feed_waste_tan_loads.py`
- `tests/test_feed_waste_tan_loads.py`

Supporting inputs:

- `data/knowledge/species/fish/tilapia.json`
- `data/knowledge/models/nitrification_models.json`
- `data/knowledge/models/solids_models.json`
- `data/knowledge/models/pump_aeration_models.json`
- `data/knowledge/parameters/waterchemistry.json`
- `docs/first_slice_repo_audit.md`
- `docs/first_slice_runtime_native_harvest_output_plan.md`
- commit `b098df0` (`Add MVP feed to TAN load calculator`)

## 4. Current Mode A Implementation Status

The committed helper implements Mode A only:

- direct `feed_kg_day`
- supplied `protein_fraction`
- `tan_n_load_kg_day = feed_kg_day * protein_fraction * 0.092`
- `tan_n_load_g_day = tan_n_load_kg_day * 1000`
- `oxygen_demand_g_day = tan_n_load_g_day * 4.57`
- `alkalinity_demand_g_caco3_day = tan_n_load_g_day * 7.14`

The helper validates:

- `feed_kg_day` is required, finite, numeric, and non-negative
- `protein_fraction` is required, finite, numeric, and between `0` and `1` inclusive

The helper explicitly excludes:

- TAN concentration
- unionized NH3 toxicity
- feed cost
- tank suitability
- biomass-derived feeding
- biofilter removal
- `saleable_harvest_mass_kg`

## 5. New Research Summary

The research pack supports these conclusions:

- Mode A direct daily feed input is the safest first implementation path.
- Feed input and feed protein fraction are the strongest direct drivers for first-pass TAN-N or ammonia-N load.
- Mode B biomass-derived feeding is supportable later, but requires fish count, average fish weight, fish biomass, stage/size-specific feeding rate, feed class/protein, and biomass updates.
- A grow-out `feed_protein_fraction = 0.32` is a defensible scenario default candidate, especially for a DWC/raft aquaponic grow-out demo, but not canonical truth.
- FCR around `1.5-1.8` is a scenario assumption band for intensive tank/RAS-like grow-out, not a load-only helper input and not canon.
- Stocking density remains context-dependent and must be scenario/customer input.
- Feed cost remains business/scenario input because available feed-price evidence is geography-, date-, and market-level dependent.
- NH3 risk requires TAN plus pH and temperature; TAN alone is not a toxicity model.
- TAN concentration and NH3 risk require water volume, time basis, exchange/retention, biofilter assumptions, pH, and temperature.

## 6. Alignment With Current Implementation

Alignment verdict: `aligned`.

The new research validates the current Mode A implementation because:

- it treats direct daily feed input as the safest first driver
- it supports feed plus protein fraction as the TAN-N production basis
- it keeps concentration and NH3 risk separate from load-only calculations
- it keeps Mode B as a later secondary path
- it keeps feed cost, stocking density, and tank suitability out of the load-only helper

No current Mode A code or tests appear inconsistent with the new research.

Naming note:

- The research pack often uses `feed_kg_per_day`.
- The implemented helper uses `feed_kg_day`.
- These are semantically aligned daily-feed fields. A later integration pass can decide whether to preserve helper naming, add adapter aliases, or normalize scenario input naming.

## 7. Load-Only Helper Boundary Audit

Boundary audit result: `passes`.

The helper remains correctly load-only:

- no TAN concentration calculation
- no unionized NH3 toxicity calculation
- no feed cost calculation
- no tank suitability calculation
- no Mode B biomass-derived feeding
- no biofilter removal or conversion claim
- no basil saleability logic
- no inferred or populated `saleable_harvest_mass_kg`

The helper also keeps nitrification demand distinct from actual biofilter removal.

## 8. Classification Table

| research finding | classification | repo interpretation |
|---|---|---|
| Mode A direct feed input is sufficient and safer for first implementation | `supports_current_implementation` | Validates the committed helper and should remain the first MVP path. |
| Feed plus protein fraction drives TAN-N load | `supports_current_implementation` | Matches the helper formula. |
| `feed_protein_fraction = 0.32` for grow-out | `scenario_default_candidate` | Useful configurable demo default, not canon and not hard-coded into helper. |
| FCR band `1.5-1.8` | `scenario_default_candidate` | Useful for planning/demo assumptions, not used by Mode A load-only helper. |
| Stage-specific feeding-rate bands | `later_mode_b_candidate` | Use only when designing biomass-derived feeding. |
| Stocking density context bands | `scenario_input_required` | Keep context-tagged; do not hard-code a universal default. |
| Feed cost evidence | `business_input_only` | Keep geography/date/supplier-specific. |
| NH3 risk requires TAN, pH, and temperature | `later_concentration_or_nh3_candidate` | Supports later risk design; current helper should not model toxicity. |
| Concentration layer needs volume, time, exchange, and biofilter assumptions | `later_concentration_or_nh3_candidate` | Required before TAN concentration implementation. |
| Customer actual feed practice and measurement reliability | `customer_validation_required` | Validate before customer-facing claims. |
| One universal stocking-density default | `do_not_use_yet` | Too context-dependent. |
| One universal feed protein value for all stages | `do_not_use_yet` | Stage-specific only. |
| One universal FCR across pond, cage, RAS, and aquaponics | `do_not_use_yet` | Context-dependent. |
| Any conversion from fish feed/biomass to basil saleable output | `do_not_use_yet` | Out of scope; saleable basil output remains unresolved. |

## 9. Scenario-Default Candidates

Use only as configurable, non-canonical assumptions:

- `feed_protein_fraction = 0.32` for a grow-out DWC/raft demo scenario
- `expected_fcr_band = 1.5-1.8` for intensive tank/RAS-like grow-out planning
- stage-specific grow-out feeding-rate bands for later Mode B design:
  - `100-250 g`: about `0.02-0.03` body weight/day
  - `>250 g`: about `0.015-0.02` body weight/day
- qualitative rule that multiple smaller feedings reduce load spikes

These should not be embedded in `src/feed_waste_tan_loads.py`.

## 10. Demo-Input Candidates

Good demo inputs for a configurable scenario/report layer:

- `feed_kg_day` or display alias `feed_kg_per_day`
- `protein_fraction`, optionally defaulted to `0.32` for a grow-out demo
- `feed_class`
- `feeding_frequency_per_day`
- optional `expected_fcr_band`
- scenario label such as `commercial_dwc_raft_growout_demo`

For a richer demo, but not for the current helper:

- `system_water_volume`
- `pH`
- `water_temperature`
- `biofilter_state`
- `exchange_or_retention_anchor`
- preferably `DO`

## 11. Scenario Inputs Required

Inputs that must remain explicit scenario inputs:

- actual `feed_kg_day`
- actual `protein_fraction` if known from the feed label
- `fish_count`
- `average_fish_weight_g`
- `fish_biomass_kg`
- `feeding_rate_fraction_per_day`
- `stocking_density`
- `tank_volume`
- `system_volume`
- `water_exchange_rate` or `retention_time`
- `biofilter_conversion_efficiency` or capacity assumption
- `pH`
- `temperature`
- `DO`
- `alkalinity`

These should not be promoted to canon by this ingestion review.

## 12. Customer-Validation Inputs

Customer/advisor discovery should validate:

- actual daily feed measurement availability
- feed label protein availability
- feed class stability over time
- actual feeding regime: fixed ration, ad libitum, fasting cycle, or sensor/feeder based
- whether fish are weighed often enough to support Mode B
- species/strain: Nile, red, hybrid, or generic tilapia
- tank and system volume
- aeration, oxygenation, and backup-power posture
- biofilter maturity/state
- whether water-quality measurements are reliable enough for pH/NH3/DO claims

## 13. Later Mode B Candidates

Mode B is supportable later but should remain unimplemented in the current helper.

Candidate Mode B chain:

```text
fish_biomass_kg = fish_count * average_fish_weight_g / 1000
feed_kg_day = fish_biomass_kg * feeding_rate_fraction_per_day
```

Mode B needs:

- fish count
- average fish weight
- size/stage-specific feeding-rate table
- feed class/protein fraction
- temperature/appetite adjustment policy
- periodic biomass updates

The new research supports Mode B as a later design pass, not as a required current MVP helper feature.

## 14. Later Concentration/NH3 Candidates

A later TAN concentration and NH3 risk layer needs:

- `feed_kg_day`
- `protein_fraction`
- `tank_water_volume_m3` or `system_water_volume_m3`
- timestep or accumulation period
- exchange rate or retention time
- biofilter conversion/capacity assumption
- pH
- temperature
- preferably DO
- preferably alkalinity

Rules to preserve:

- TAN concentration must not be calculated from load alone.
- NH3 toxicity must not be modeled from TAN alone.
- Biofilter demand must not be treated as actual conversion/removal without capacity and operating context.

## 15. Business-Input-Only Findings

Business-only or scenario/business inputs:

- feed price per kg
- feed class and supplier/market level
- currency
- date basis
- geography
- feed wastage/spoilage assumptions
- labor cost for feeding, monitoring, and interventions
- energy cost for aeration or circulation

The new research supports feed as a dominant operating-cost category, but it does not provide a current canonical feed-cost value.

## 16. Do-Not-Use-Yet Findings

Do not use yet:

- one universal stocking-density default
- one universal FCR default across pond, cage, RAS, and aquaponics
- one universal protein fraction for all life stages
- feed-cost canon
- Mode B as a required current helper path
- TAN concentration without volume/time/exchange/removal context
- NH3 toxicity from TAN alone
- actual biofilter removal from nitrification demand alone
- any conversion from fish feed, fish biomass, standing plant biomass, daily plant gain, or plant count into basil `saleable_harvest_mass_kg`

## 17. Recommended Next Repo-Side Pass

Recommended next pass: `Mode A scenario/report integration surface plan`.

Why this should come before implementation:

- the helper is already implemented and validated
- the research validates Mode A, but scenario input naming and report output shape still need design
- demo defaults such as `protein_fraction = 0.32` should be placed deliberately as configurable assumptions, not helper constants
- concentration/NH3, Mode B, and feed-cost economics each require additional input contracts

Recommended order:

1. Mode A scenario/report integration surface plan
2. Mode A integration implementation
3. TAN concentration/NH3 risk design
4. Mode B design
5. feed-cost economics design

## 18. Blockers

No blockers for this docs-only ingestion review.

Blockers for later work:

- Mode A integration needs a designed scenario/report input surface.
- TAN concentration/NH3 risk needs volume, time basis, exchange/retention, biofilter assumptions, pH, and temperature.
- Mode B needs fish count, average fish weight, feeding-rate table choice, and biomass update rules.
- Feed-cost economics needs explicit feed cost, geography, currency, date basis, and market level.
- Basil saleable output remains unresolved/null and blocks crop revenue interpretation until observed or explicitly reviewed.

## 19. Recommended Next Action

- Keep the committed Mode A helper load-only.
- Use the new research to support a Mode A scenario/report integration surface plan.
- Allow `feed_protein_fraction = 0.32` and FCR `1.5-1.8` only as configurable demo/scenario assumptions.
- Keep stocking density and feed cost as scenario/customer/business inputs.
- Keep Mode B, TAN concentration/NH3 risk, and feed-cost economics as separate later passes.
- Keep basil `saleable_harvest_mass_kg` unresolved/null.
