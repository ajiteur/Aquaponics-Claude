# MVP Fish Feed Waste TAN Engine Design

Status: `draft`

## 1. Purpose

- Define the smallest MVP-worthy fish-feed-to-waste-and-water-quality engine for a bounded tilapia + basil DWC/raft planning slice.
- Keep this pass review-first and docs-only.
- Separate physical daily load calculations from concentration, toxicity, sizing, and economics layers.
- Preserve the current basil saleable-output pause: `saleable_harvest_mass_kg` remains unresolved/null unless observed or explicitly reviewed.

## 2. Scope

In scope:

- tilapia feed input, feed-derived TAN-N load, solids-load framing, nitrification demand, oxygen demand, alkalinity demand, and warning labels
- DWC/raft baseline context for biofilter, solids filtration, aeration, pH stability, and plant nutrient context
- future implementation planning by candidate flow only
- seed-MVP demo outputs that show operational and business-planning value without pretending economics are complete

Out of scope:

- calculation implementation
- canonical biology/model/business edits
- runtime, script, ontology, or source-file edits
- harvest saleability logic
- greenhouse climate and crop saleability logic

## 3. Inputs Reviewed

Canonical repo inputs:

- `data/knowledge/models/nitrification_models.json`
- `data/knowledge/models/solids_models.json`
- `data/knowledge/models/pump_aeration_models.json`
- `data/knowledge/parameters/waterchemistry.json`
- `data/knowledge/species/fish/tilapia.json`

Context docs:

- `docs/first_slice_adapter_saleable_harvest_null_status_design.md`
- `docs/first_slice_architecture_runtime_plan.md`
- `docs/runtime_field_inventory.md`
- `docs/business_layer_plan.md`

Source and research inputs:

- `data/sources/research_reports/distilled/Distilled_Research_Pack_Aquaponics_L1.md`
- `data/sources/research_reports/markdown/Pumps and Aeration.md`
- `data/sources/research_reports/distilled/Pumps and Aeration.md`

Requested markdown paths not present:

- `data/sources/research_reports/markdown/Distilled_Research_Pack_Aquaponics_L1.md`
- `data/sources/research_reports/markdown/Biofilters and solids filters_Corroboration report for aquaponics Layer 1.md`
- `data/sources/research_reports/markdown/Water Chemistry and pH Management_Aquaponics Layer 1 Parameter Corroboration Report.md`
- `data/sources/research_reports/markdown/Tilapia Species Profile Corroboration Report for Aquaponics Layer 1.md`
- `data/sources/research_reports/markdown/Pumps and aeration_Corroboration report for aquaponics Layer 1 component library.md`

Closest available non-markdown evidence files were present under `data/sources/research_reports/raw/**` as PDFs. Their distilled findings are already reflected in the inspected canonical JSON and distilled markdown pack, so the missing markdown paths are non-blocking for this design pass.

## 4. Current Repo Truth

- The nitrification model already contains the feed-to-TAN formula, treated here as TAN-N or ammonia-N load:
  - `PTAN_kg_day = feed_kg_day * protein_fraction * 0.092`
- The nitrification model already contains stoichiometric demand coefficients:
  - oxygen demand: `4.57 g O2 / g TAN-N`
  - alkalinity demand: `7.14 g CaCO3 / g TAN-N`
- Biofilter sizing anchors are currently expressed as feed-loading ranges by media type:
  - fluidized sand: `16-32 kg feed / m3 media / day`
  - MBBR: `8-16 kg feed / m3 media / day`
  - bead biofilter: `16-32 kg feed / m3 media / day`, conditional on frequent washing
- Solids models currently provide clarifier HRT and settler TSS capture anchors, not a canonical feed-to-solid-waste mass fraction.
- Pump and aeration models currently provide turnover targets, DO thresholds, CO2 action logic, backup/maintenance patterns, and provisional pump-power anchors.
- Water chemistry parameters currently provide pH target ranges, TAN guidance, unionized NH3 action thresholds, nitrification pH inhibition thresholds, and alkalinity target guidance.
- The tilapia profile currently provides preferred temperature and pH ranges, minimum dissolved oxygen, unionized NH3 sensitivity, and aquaponics validation benchmarks.
- Runtime-facing files already contain fish biomass, daily feed, pH, TAN, unionized NH3, nitrate, dissolved oxygen, and alkalinity fields in some scenario/day-log families, but these runtime artifacts are derived outputs and are not canonical truth.
- Existing runtime code has simplified feed/TAN/concentration behavior, but this design pass does not validate, edit, or promote it.
- `saleable_harvest_mass_kg` remains unresolved/null and must not be inferred from standing plant biomass, daily plant gain, or plant count.

## 5. Minimal Fish-Feed-To-Waste-And-Water-Quality Calculation Chain

Minimum daily chain:

1. fish biomass, if using biomass-derived feeding
2. feed input, either supplied directly or derived from biomass and feeding rate
3. feed protein fraction
4. feed-driven solid-waste load, only when a solids fraction or direct solids-load input exists
5. TAN-N or ammonia-N production load from feed and protein fraction
6. nitrification conversion demand from TAN-N load
7. oxygen demand from TAN-N load
8. alkalinity demand from TAN-N load
9. TAN/NH3 risk interpretation only when concentration and pH/temperature context exist
10. biofilter, solids, aeration, and pH stability warning labels
11. business-risk interpretation hooks without calculating costs unless business inputs are supplied

Minimum directly calculable load outputs when `feed_kg_day` and `protein_fraction` are known:

- `feed_kg_day`
- `tan_n_load_kg_day`
- `tan_n_load_g_day`
- `nitrification_oxygen_demand_g_o2_day`
- `nitrification_alkalinity_demand_g_caco3_day`

Conditionally calculable outputs:

- `solid_waste_load_g_day` only with a supplied solids fraction or direct solids load
- `biofilter_feed_loading_status` only with biofilter media type and media volume
- `tan_mg_l` only with explicit water volume, time basis, dilution/exchange, and removal assumptions
- `unionized_nh3_mg_l` only from observed value or from TAN concentration plus pH and temperature

## 6. Load Versus Concentration Boundary

Physical load calculations answer:

- how much feed enters the system per day
- how much TAN-N or ammonia-N is produced per day
- how much oxygen and alkalinity nitrification demands per day
- how much solid-waste load must be handled per day, if a solids-load fraction or direct solids input exists

Concentration and risk calculations answer:

- what concentration accumulates in the fish tank or system water
- whether TAN guidance is exceeded
- whether unionized NH3 is risky for tilapia
- whether pH, DO, alkalinity, and biofilter capacity make the load unsafe

Boundary rules:

- TAN-N load may be calculated from feed and protein fraction.
- TAN concentration must not be calculated unless water volume, dilution/exchange, removal, and time basis are explicit.
- NH3 toxicity must not be modeled from TAN alone; it requires pH and temperature context or an observed unionized NH3 value.
- DO risk must not be inferred from oxygen demand alone unless aeration capacity or observed DO is supplied.
- Tank-volume suitability must not be asserted unless tank volume, stocking density, and water-quality assumptions are supplied.

Terminology rule:

- `tan_n_load_*` and the feed-to-TAN formula represent TAN-N or ammonia-N mass load.
- `tan_mg_l` is a concentration and requires volume/time/removal context.
- `unionized_nh3_mg_l` is the fish-toxicity driver and must come from observation or from TAN concentration plus pH and temperature.

## 7. Two Input Modes: Direct Feed Input Versus Biomass-Derived Feed Input

### Mode A: direct feed input

Required input:

- `feed_kg_day`

Use when the scenario or operator already knows the daily ration.

Advantages:

- smallest path to TAN, oxygen, and alkalinity load
- avoids choosing a fish-stage feeding-rate curve prematurely
- useful for customer/advisor demos where the operator can provide current feed rate

### Mode B: biomass-derived feed input

Required inputs:

- `fish_biomass_kg`
- `feeding_rate_fraction_body_weight_day`

Design formula:

```text
feed_kg_day = fish_biomass_kg * feeding_rate_fraction_body_weight_day
```

Use only when fish biomass and a reviewed feeding-rate basis are both supplied.

If `fish_biomass_kg` is not supplied directly, it may be calculated only when both of these scenario inputs are supplied:

- `fish_count`
- `average_fish_weight_g`

Do not:

- derive feed amount from fish count alone
- choose a feeding rate without fish size/stage context
- treat feeding-rate defaults as canon before deep research or explicit scenario input supports them

## 8. Recommended First Implementation Mode

The safest first implementation mode is Mode A:

- require direct `feed_kg_day` as scenario input
- require supplied `protein_fraction`
- calculate load-only outputs first:
  - `tan_n_load_kg_day`
  - `tan_n_load_g_day`
  - `nitrification_oxygen_demand_g_o2_day`
  - `nitrification_alkalinity_demand_g_caco3_day`
- emit warning labels for missing concentration, NH3 toxicity, biofilter, solids, aeration, and economics context

Mode A should not calculate:

- TAN concentration
- unionized NH3 toxicity
- biofilter removal
- feed cost
- tank suitability
- crop saleable output

Mode B should wait until fish biomass and feeding-rate evidence by size/stage are supplied or researched.

## 9. Evidence-Backed Formulas And Parameters

| item | expression or parameter | classification | implementation readiness |
|---|---|---|---|
| Feed to TAN-N or ammonia-N load | `tan_n_load_kg_day = feed_kg_day * protein_fraction * 0.092` | first-pass design formula | ready when feed and protein fraction are supplied |
| TAN-N kg to g | `tan_n_load_g_day = tan_n_load_kg_day * 1000` | first-pass design formula | ready |
| Nitrification oxygen demand | `o2_demand_g_day = tan_n_load_g_day * 4.57` | first-pass design formula | ready when TAN-N load is known |
| Nitrification alkalinity demand | `alkalinity_demand_g_caco3_day = tan_n_load_g_day * 7.14` | first-pass design formula | ready when TAN-N load is known |
| Biomass-derived feed input | `feed_kg_day = fish_biomass_kg * feeding_rate_fraction_body_weight_day` | scenario input formula | ready only when feeding rate is supplied |
| Solids load from feed | `solid_waste_load_g_day = feed_kg_day * 1000 * solid_waste_fraction_of_feed` | open calibration item | not ready as default; usable only with supplied fraction |
| Biofilter feed loading | `feed_kg_day / biofilter_media_m3` compared to media range | operational warning threshold | ready only when media type and media volume are supplied |
| TAN concentration equivalent | load-to-volume/time/removal calculation | open calibration item | blocked until volume, exchange, time, and removal basis exist |
| Unionized NH3 risk | observed or computed NH3 compared to thresholds | operational warning threshold | ready only when observed NH3 or TAN+pH+temperature are supplied |
| Feed cost | `feed_kg_day * feed_cost_per_kg` | business input | blocked until explicit feed cost is supplied |

## 10. Scenario Inputs Versus Canonical Defaults

Canonical defaults currently suitable as design anchors:

- feed-to-TAN coefficient: `0.092`
- nitrification oxygen demand coefficient: `4.57 g O2 / g TAN-N`
- nitrification alkalinity demand coefficient: `7.14 g CaCO3 / g TAN-N`
- pH compromise and tolerable ranges
- pH inhibition ladder for nitrification
- TAN operational guidance as concentration context, not load context
- unionized NH3 warning/action thresholds
- DO setpoint and low-DO action thresholds
- biofilter feed-loading ranges by media type
- clarifier HRT and settler capture anchors

Scenario inputs required for the first load-only engine:

- `feed_kg_day`, or `fish_biomass_kg` plus `feeding_rate_fraction_body_weight_day`
- `protein_fraction`
- optional direct `solid_waste_load_g_day` or `solid_waste_fraction_of_feed`

Scenario inputs required for concentration/risk layer:

- tank or system water volume
- retention/exchange rate
- time basis
- pH
- temperature
- observed or computed TAN concentration
- observed or computed unionized NH3
- dissolved oxygen or aeration capacity
- alkalinity concentration or buffering state

Business inputs required for economics:

- feed cost per kg
- electricity cost per kWh
- buffer/supplement cost basis
- labor/callout cost basis for interventions
- risk-penalty interpretation rules

## 11. Input Dependency Matrix

| value | unit | dependency classification | required for |
|---|---|---|---|
| `fish_count` | count | scenario input required if biomass is not supplied | Mode B biomass derivation only with average fish weight |
| `average_fish_weight_g` | g/fish | scenario input required if biomass is not supplied | Mode B biomass derivation only with fish count |
| `fish_biomass_kg` | kg fish biomass | scenario input required | Mode B feed derivation, stocking context |
| `feed_kg_day` | kg feed/day | scenario input required or implementation-derived value | Mode A direct load chain; all downstream load outputs |
| `feeding_rate_fraction_body_weight_day` | fraction/day | scenario input required; deep-research gap for defaults | Mode B feed derivation |
| `protein_fraction` | fraction of feed | scenario input required; deep-research gap for defaults by feed class | TAN-N load |
| `solid_waste_fraction_of_feed` | fraction of feed | deep-research gap or scenario input required | solids load |
| `solid_waste_load_g_day` | g/day | scenario input required or implementation-derived value | solids filtration load |
| `tan_n_load_kg_day` | kg TAN-N/day | implementation-derived value | nitrification load |
| `tan_n_load_g_day` | g TAN-N/day | implementation-derived value | oxygen and alkalinity demand |
| `o2_demand_g_day` | g O2/day | implementation-derived value | aeration demand context |
| `alkalinity_demand_g_caco3_day` | g CaCO3/day | implementation-derived value | pH/alkalinity stability context |
| `water_volume_l` or `system_volume_l` | L | scenario input required | concentration layer |
| `retention_or_exchange_rate` | time or volume/time | scenario input required | concentration and dilution/removal layer |
| `pH` | pH | canonical threshold available; observed/scenario value required | NH3 risk, pH stability, nitrification warning |
| `temperature_c` | C | canonical tilapia range available; observed/scenario value required | NH3 fraction and fish health context |
| `tan_mg_l` | mg/L | observed/scenario value or implementation-derived with volume/time basis | TAN concentration guidance |
| `unionized_nh3_mg_l` | mg/L NH3 | observed/scenario value or implementation-derived from TAN+pH+temperature | fish health risk |
| `dissolved_oxygen_mg_l` | mg/L | canonical thresholds available; observed/scenario value required | fish, nitrifier, and aeration warning |
| `alkalinity_mg_l_as_caco3` | mg/L as CaCO3 | canonical threshold available; observed/scenario value required | buffering warning |
| `biofilter_media_type` | label | scenario/customer-discovery input | biofilter capacity warning |
| `biofilter_media_m3` | m3 | scenario/customer-discovery input | feed-loading capacity warning |
| `aeration_capacity` | equipment-specific | scenario/customer-discovery input; deep-research gap for general defaults | DO capacity interpretation |
| `feed_cost_per_kg` | currency/kg | business input required; customer-discovery input | feed cost economics |
| `crop_system_type` | label | canonical/context available in current slice | architecture-aware interpretation only |
| `saleable_harvest_mass_kg` | kg | unresolved/null | out of scope; do not infer |

## 12. Missing Inputs Requiring Deep Research

Highest-priority gaps before stronger defaults:

- feed protein percentage by feed class for tilapia grow-out and starter/stage contexts
- feeding rate by fish size, stage, water temperature, and management target
- feed-to-solid-waste fraction or defensible solids-load model
- minimum fish size or stocking stage for the MVP scenario framing
- stocking-density bands for tilapia in DWC/raft aquaponics or RAS-like coupled systems
- aeration capacity translation from demand to equipment sizing, including oxygen transfer efficiency or blower/diffuser curves

These gaps do not block this design pass. They affect whether the first implementation can ship with defaults or must require scenario inputs.

## 13. Missing Inputs That Can Remain Scenario/Customer Inputs

Inputs that can remain explicit scenario or customer/advisor inputs for the MVP:

- feed cost per kg
- direct `feed_kg_day`
- fish biomass
- fish tank volume
- system water volume
- retention/exchange rate
- biofilter media type and volume
- aeration equipment/capacity
- current pH, temperature, TAN, unionized NH3, DO, and alkalinity
- stocking density or fish count and average weight

This is acceptable because the first MVP can demonstrate sensitivity and planning value without pretending that every design choice is canonical.

## 14. Timing Classification For Unresolved Inputs

| unresolved item | classification | timing |
|---|---|---|
| feed cost per kg | business input; customer-discovery input | needed before economics layer; can remain scenario input for now |
| feed protein percentage by feed class | deep-research gap or scenario input | needed before first implementation if TAN load uses defaults; can remain scenario input for now |
| feeding rate by fish size/stage | deep-research gap or scenario input | needed before Mode B; not needed for Mode A direct feed input |
| fish minimum size / stocking stage | deep-research gap; customer-discovery input | needed before customer/advisor demo if using a prefilled example |
| fish tank volume | scenario/customer input | needed before concentration/risk layer and tank suitability claims |
| stocking density | deep-research gap or scenario/customer input | needed before sizing/tank suitability and advisor demo |
| water volume / system volume | scenario/customer input | needed before concentration/risk layer |
| retention / exchange rate | scenario/customer input | needed before concentration/risk layer |
| biofilter media volume | scenario/customer input | needed before biofilter capacity warning |
| aeration capacity | scenario/customer input; deep-research gap for defaults | needed before aeration capacity and economics layers |
| feed-to-solids fraction | deep-research gap or scenario input | needed before calculated solids mass; feed can still serve as load driver |
| pH and temperature | scenario/observed input; canonical thresholds available | needed before NH3 toxicity interpretation |
| alkalinity concentration | scenario/observed input; canonical threshold available | needed before pH stability warning |

Missing feed cost, tank size, and stocking density are not blockers for this design pass. They may become blockers for later economics, concentration, sizing, or advisor-demo layers.

## 15. Risk And Warning Interpretation

Direct calculations should remain separate from warning labels.

Directly calculable load values:

- `feed_kg_day`
- `tan_n_load_kg_day`
- `tan_n_load_g_day`
- `o2_demand_g_day`
- `alkalinity_demand_g_caco3_day`

Warning labels that require extra context:

- `tan_concentration_context_missing`
- `nh3_toxicity_context_missing`
- `biofilter_capacity_unknown`
- `biofilter_feed_loading_warning`
- `solids_load_unknown`
- `solids_filtration_warning`
- `aeration_capacity_unknown`
- `low_do_warning`
- `nitrifier_do_inhibition_warning`
- `pH_compromise_warning`
- `nitrification_pH_inhibition_warning`
- `alkalinity_buffering_warning`
- `feed_cost_missing_for_economics`

Risk interpretation rules:

- TAN-N load alone is a biofilter and water-quality pressure indicator, not a toxicity conclusion.
- TAN concentration is an operational water-quality indicator only when volume/time/removal context exists.
- Unionized NH3 is the toxicity driver for fish and requires pH and temperature context if not directly observed.
- DO warnings should use observed DO or explicit aeration capacity, not oxygen demand alone.
- pH and alkalinity warnings should indicate stability risk and nitrification support, not direct business cost.

## 16. Connections To Biofilter, Solids, Aeration, pH, And Plant Nutrient Context

Fish health:

- feed load drives TAN-N load and oxygen demand
- observed or computed unionized NH3 drives fish safety warnings
- DO and temperature frame growth and stress risk

Biofilter sizing/load:

- TAN-N load defines nitrification conversion demand, not actual removal
- feed loading can be compared to media-specific feed capacity only when media volume and type are supplied
- actual biofilter conversion/removal requires explicit capacity, maturity, flow, pH, DO, temperature, and alkalinity context
- pH, DO, temperature, and alkalinity should later affect nitrification capacity or warning severity

Solids filtration load:

- feed rate is the driver for solids pressure
- actual solids mass requires a solids fraction or direct solids-load input
- clarifier HRT and settler type can later drive capture and carryover warnings

Aeration/DO risk:

- nitrification oxygen demand is calculable from TAN-N load
- fish and biofilter DO thresholds are already available as warning anchors
- capacity risk requires observed DO or aeration equipment/capacity inputs

pH/alkalinity stability:

- nitrification alkalinity demand is calculable from TAN-N load
- pH stability warning requires alkalinity concentration and pH context
- low pH can inhibit nitrification even if feed/TAN formulas are otherwise valid

Plant nutrient availability context:

- nitrification output supports nitrate availability context for DWC/raft plants
- this engine should expose nutrient-load context only, not basil saleable yield
- plant-side pH tradeoffs should be warning context, not harvest-saleability logic

Architecture-aware business interpretation:

- DWC/raft context affects aeration, buffering, hydraulic resilience, and solids-management interpretation
- `crop_system_type` should remain a context field, not a pricing or saleability selector
- business-risk hooks should describe potential cost drivers such as backup power, solids maintenance, oxygen capacity, and pH buffering without calculating cost unless business inputs exist

## 17. Business And Seed-MVP Relevance

The engine is seed-MVP relevant because it can show a defensible operating chain:

- if daily feed increases, TAN-N load increases
- higher TAN-N load raises biofilter, oxygen, and alkalinity demand
- weak biofilter, solids removal, aeration, pH, or alkalinity context raises operational warnings
- those warnings connect to business-risk hooks such as intervention labor, feed curtailment, buffer/supplement use, backup power, and equipment sizing

Economics should remain honest:

- feed cost is not calculated without explicit feed cost per kg
- electricity/aeration cost is not calculated without power and electricity inputs
- saleable basil output remains unresolved/null
- business interpretation can show "value at risk" categories before it has dollarized penalties

## 18. Customer/Advisor Demo Output Enabled By This Engine

Useful MVP demo outputs:

- daily feed-to-TAN load card
- nitrification oxygen and alkalinity demand card
- missing-context checklist for concentration and NH3 toxicity
- biofilter load warning when media type/volume are supplied
- solids-filtration pressure warning when solids inputs are supplied
- DO/aeration warning if observed DO or capacity context is supplied
- pH/alkalinity stability warning
- DWC/raft operational-risk summary
- business-risk hook summary:
  - feed input cost needs feed price
  - aeration risk needs equipment/power data
  - pH control risk needs buffer/supplement inputs
  - saleable crop output remains unresolved

This is useful in a seed conversation because it demonstrates causal modeling and disciplined uncertainty instead of a black-box yield or revenue claim.

## 19. What Remains Out Of Scope

- basil `saleable_harvest_mass_kg` inference
- standing plant biomass to saleable mass conversion
- daily plant gain to saleable mass conversion
- plant count to saleable mass conversion
- greenhouse climate or disease-trigger logic
- customer-specific profitability claims
- feed-cost calculation without feed cost input
- tank-size or stocking-density suitability claims without tank volume and stocking-density evidence
- TAN concentration without water volume, time, dilution, and removal basis
- NH3 toxicity from TAN alone
- bacteria producing TAN; fish/feed produce TAN load, nitrifiers convert TAN
- final implementation diffs

## 20. Smallest Future Implementation Surface

Smallest future implementation flow:

1. Add an isolated feed-load calculator that accepts scenario inputs and canonical coefficients.
2. Emit load-only outputs first:
   - feed kg/day
   - TAN-N kg/day and g/day
   - O2 demand g/day
   - CaCO3 alkalinity demand g/day
   - context-missing warning labels
3. Add optional checks only when inputs exist:
   - biofilter feed loading
   - solids load
   - observed DO warning
   - pH/alkalinity warning
   - NH3 warning from observed NH3 or TAN+pH+temperature
4. Keep generated outputs clearly marked as scenario/runtime outputs, not canon.
5. Keep business hooks descriptive until business inputs are supplied.

Candidate file/flow surface for a later approved implementation pass:

- `src/simulate_day.py` or a new narrow helper module consumed by it
- `src/simulate_n_days.py` only if output summaries need new fields
- scenario input/config files only if a later pass explicitly approves scenario inputs
- generated runtime outputs under `data/simulation/**` only as derived artifacts
- optional docs update documenting the implemented payload/output shape

Do not touch `src/build_runtime_from_knowledge.py` unless explicitly instructed.

## 21. Validation For A Later Implementation Pass

Later validation should confirm:

- load-only calculations work with Mode A direct `feed_kg_day`
- Mode B derives feed only when fish biomass and feeding rate are both supplied
- feed-to-TAN uses `feed_kg_day * protein_fraction * 0.092`
- O2 and alkalinity demands use the canonical coefficients
- no TAN concentration is emitted without explicit volume/time/removal basis
- no NH3 toxicity label is emitted from TAN alone
- no feed cost is emitted without `feed_cost_per_kg`
- no tank-size suitability claim is emitted without volume and stocking-density inputs
- `saleable_harvest_mass_kg` remains null/unresolved and untouched
- no canonical files are changed unless a later pass explicitly requests canon work
- generated runtime diffs are expected only in approved derived-output paths

Suggested later command checks:

- targeted unit or smoke test for the feed-load calculator
- `git --no-pager diff --name-only -- data/knowledge`
- `git --no-pager diff --name-only -- data/simulation`
- `git --no-pager diff --name-only -- src scripts`
- `git status --short`

## 22. Deep-Research Queue To Accelerate MVP

Ready-to-run research topics:

1. Tilapia feed-class and feeding-rate defaults for a DWC/raft aquaponics MVP:
   - feed protein ranges by fish stage
   - feeding rate as percent body weight by fish size/stage
   - minimum defensible stocking stage for a demo scenario
2. Feed-to-solids and solids-removal sizing for small commercial tilapia aquaponics:
   - feed-to-settleable/TSS load fractions
   - clarifier/radial-flow sizing implications
   - carryover warning thresholds for DWC/raft
3. Aeration capacity and oxygen-transfer defaults for DWC/raft aquaponics:
   - oxygen transfer efficiency or blower/diffuser rules
   - translating O2 demand into equipment capacity
   - energy and backup-power assumptions suitable for business hooks

These should be research outputs or evidence memos first, not direct canon promotion.

## 23. Blockers

Not blockers for this design pass:

- missing feed cost per kg
- missing tank size
- missing stocking density
- missing water volume
- missing feed-class protein default

Potential blockers for later layers:

- concentration/risk layer is blocked without water volume, time basis, dilution/exchange, and removal semantics
- NH3 toxicity layer is blocked without pH and temperature context or observed unionized NH3
- biofilter capacity warning is blocked without media type and media volume
- solids mass calculation is blocked without a direct solids input or feed-to-solids fraction
- feed-cost economics are blocked without feed cost per kg
- tank suitability is blocked without tank volume, stocking density, and water-quality assumptions
- advisor-demo defaults are weaker until feed class, feeding rate, stocking stage, and density are researched or supplied

## 24. Recommended Next Action

- Keep this note as a docs-only design artifact.
- For the first implementation, prefer Mode A direct `feed_kg_day` plus supplied `protein_fraction`.
- Implement load-only outputs before concentration or toxicity outputs.
- Add warning labels for missing concentration, NH3, biofilter, solids, aeration, and economics context instead of inventing missing inputs.
- Send the feed-class/feeding-rate and feed-to-solids topics to deep research before choosing default coefficients.
- Keep basil saleable harvest mass unresolved/null until a separate observed or explicitly reviewed saleability pass approves otherwise.
