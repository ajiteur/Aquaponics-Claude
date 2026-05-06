# MVP P1.5 Aeration Capacity And Solids Load Design

## 1. Purpose

Define a docs-only P1.5 design plan for adding aeration-capacity context and
solids-load context to the Mode A/P1 MVP report path.

This plan keeps oxygen demand, oxygen transfer, measured dissolved oxygen,
solids production, solids removal, and safety interpretation separate. It does
not implement calculations and does not propose final code diffs.

## 2. Scope

In scope:

- P1.5 research translation for aeration capacity, oxygen-demand framing, DWC
  root-zone aeration, feed-linked solids, and solids-removal context.
- Classification of oxygen and solids concepts by implementation readiness.
- Warning labels and blocked claims for a later report extension.
- Recommended smallest future implementation surface.

Out of scope:

- Canonical biology/model/business edits.
- Ontology edits.
- Runtime or simulation-flow integration.
- Source, script, test, or existing-doc edits in this pass.
- Feed cost, tank suitability, Mode B, business profitability, or basil
  saleability implementation.

## 3. Inputs Reviewed

Primary P1.5 research input:

- `data/sources/research_reports/markdown/Aeration Capacity and Solids Load Translation Research Pack for the Aquaponics MVP.md`

Implemented MVP assets:

- `src/feed_waste_tan_loads.py`
- `src/mvp_tan_nh3_risk.py`
- `src/mvp_mode_a_feed_load_report.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `scripts/example_mvp_mode_a_p1_water_quality_inputs.json`
- `tests/test_feed_waste_tan_loads.py`
- `tests/test_mvp_tan_nh3_risk.py`
- `tests/test_mvp_mode_a_feed_load_report.py`
- `tests/test_build_mvp_mode_a_feed_load_report.py`

Supporting docs:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_tilapia_feed_research_ingestion_review.md`
- `docs/mvp_p1_tan_concentration_nh3_risk_design.md`
- `docs/mvp_mode_a_feed_load_customer_demo_walkthrough.md`
- `docs/mvp_strategic_alignment_review_packet_for_pro.md`

Missing inputs:

- None. The exact requested P1.5 research pack was present.

## 4. Current MVP/P1 Status

The current report path is Mode A direct feed input:

- required `feed_kg_day`
- required `protein_fraction`
- calculated `tan_n_load_kg_day`
- calculated `tan_n_load_g_day`
- calculated `oxygen_demand_g_day`
- calculated `alkalinity_demand_g_caco3_day`

The current P1 optional water-quality context can calculate only when the full
P1 input group is supplied:

- fish-tank upper-bound/no-removal `estimated_tan_n_mg_l`
- `estimated_unionized_nh3_fraction`
- `estimated_nh3_n_mg_l`
- `estimated_nh3_mg_l`

The current report still does not calculate:

- total oxygen demand
- fish respiration oxygen demand
- DWC/root-zone oxygen demand
- actual aeration capacity
- actual oxygen transfer
- solids load
- TSS concentration
- wet sludge
- solids-removal capacity
- biofilter removal
- fish safety or system safety

This P1.5 design should preserve the current P1 behavior. The existing
`oxygen_demand_g_day` remains nitrification-support oxygen demand only.

## 5. P1.5 Research Summary

The P1.5 research supports these implementation-relevant findings:

- Nitrification oxygen demand is valid but incomplete; it is not total oxygen
  demand.
- Total oxygen demand in RAS-like contexts includes fish respiration, organic
  waste and uneaten-feed decomposition, and nitrification.
- A practical feed-based total oxygen envelope of about `0.3-0.75 kg O2/kg feed`
  may be useful for scenario context, but it depends on solids retention and
  biofilter configuration and should not become canon.
- Warmwater tilapia operation uses dissolved-oxygen anchors around `5 mg/L` for
  normal operation, with chronic growth/feed-conversion concern below about
  `3.5 mg/L` and nitrifier inefficiency around `2 mg/L`. These are warning
  anchors only unless measured DO and threshold basis are explicit.
- Equipment nameplate power or blower presence is not oxygen-transfer capacity.
  Capacity comparisons need an oxygen-transfer basis such as SOTR/SAE,
  airflow-plus-diffuser context, oxygenation equipment, or measured site
  performance.
- DWC/raft root-zone aeration is a separate subsystem; fish-tank aeration does
  not prove plant-channel oxygen support.
- Feed can support a provisional gross dry-solids potential estimate. The
  strongest aquaponics anchor is at least `25%` of feed as dry solid waste, but
  wet sludge, TSS concentration, and removal capacity require more inputs.
- UVI-like clarifier detention, purge frequency, filter cleaning, raft
  air-stone geometry, and separate hydroponic blower patterns are useful demo
  assumptions, not universal defaults or canon.

## 6. Oxygen-Demand Concept Separation

Oxygen concepts to keep separate:

| Concept | Meaning | Current/future interpretation |
| --- | --- | --- |
| nitrification oxygen demand | Oxygen needed to support conversion of TAN-N to nitrate. | Already calculated as `oxygen_demand_g_day`; not actual biofilter removal. |
| fish respiration oxygen demand | Oxygen consumed by fish metabolism, feeding response, and growth. | Not calculated yet; needs fish biomass/size, temperature, feeding state, or a reviewed model. |
| organic-waste/decomposition oxygen demand | Oxygen consumed as retained feces and uneaten feed decompose. | Not calculated yet; needs solids load, retention, decomposition/BOD basis, or a feed-based envelope. |
| DWC/root-zone oxygen demand | Oxygen needed in raft channels/root zones for root health and disease pressure management. | Separate plant-side context; not covered by fish-tank aeration. |
| total oxygen demand | Fish respiration plus organic-waste/decomposition oxygen plus nitrification and any other declared loads. | Not calculated now; a feed-based envelope could be a provisional scenario context later. |
| aeration/oxygen-transfer capacity | Delivered oxygen support from actual equipment and operating conditions. | Not calculated now; requires transfer basis, device context, and continuity assumptions. |

Naming rule:

- Keep `oxygen_demand_g_day` as nitrification-support oxygen demand unless a
  later implementation introduces an explicit `total_oxygen_demand_*` field.

## 7. Oxygen Concept Classification

| Oxygen concept | Classification | Rationale |
| --- | --- | --- |
| nitrification oxygen demand | `calculable_now` | Already derived from TAN-N load using `4.57 g O2/g TAN-N`. |
| fish respiration oxygen demand | `blocked` | Needs a reviewed fish-respiration model and fish biomass/size/temperature context. |
| organic-waste/decomposition oxygen demand | `blocked` | Needs solids retention, uneaten feed, decomposition/BOD basis, or a reviewed feed-envelope implementation. |
| DWC/root-zone oxygen demand | `warning_only` | Evidence supports separate context warnings, but not a basil-specific oxygen-demand formula. |
| total oxygen demand | `blocked` | Cannot be calculated from nitrification oxygen alone. Could become scenario-envelope output later. |
| measured DO context | `scenario_input_required` | A measured value can support warning labels only with measurement location, timing, and threshold basis. |
| aeration/oxygen-transfer capacity | `scenario_input_required` | Requires equipment and transfer basis; blower/pump presence alone is insufficient. |
| backup aeration/power continuity | `scenario_input_required` | Required for resilience context; absence should remain a warning, not a safety calculation. |

## 8. Aeration-Capacity Context Requirements

Minimum context before any aeration-capacity comparison:

- measured DO value, if using observed DO context
- measurement location: fish tank, biofilter, DWC/raft channel, or other
- measurement timing: daily average, early morning, post-feeding, or point
  observation
- aeration device type: air pump, blower, airlift, pure oxygen, venturi, or
  other
- pump/blower capacity basis: airflow, pressure/depth, SOTR, SAE, or vendor
  curve
- oxygen-transfer basis: standard rating, in-situ derating, diffuser depth,
  diffuser layout, oxygen source, or measured site performance
- diffuser/air-stone assumptions: count, spacing, depth, and serviced area
- backup aeration or power-continuity basis: generator, backup blower, oxygen
  reserve, alarm, response time, or none
- loop scope: fish tank, biofilter, DWC/raft root zone, or whole system

Do not compare demand against:

- equipment nameplate power alone
- "air pump present" alone
- "blower present" alone
- fish-tank DO as proof of future safety
- fish-loop aeration as proof of DWC/root-zone aeration

## 9. DWC/Root-Zone Aeration Context

DWC/raft should have its own context fields and warnings.

Candidate future context inputs:

- `dwc_root_zone_aeration_present`
- `dwc_aeration_device_type`
- `dwc_air_stone_count`
- `dwc_air_stone_spacing_m`
- `dwc_float_bed_area_m2`
- `dwc_channel_retention_h`
- `dwc_measured_do_mg_l`
- `dwc_measurement_location`
- `dwc_solids_carryover_context`

Safe interpretation:

- DWC/raft channels may re-aerate water when designed with separate aeration.
- DWC/raft channels may become root-zone oxygen and solids-risk areas when
  unaerated or when solids carry over.
- Fish-tank DO and fish-side aeration do not resolve DWC/root-zone oxygen
  context.
- Hydroponic leafy-greens root-zone DO anchors can support warning context, but
  should not become basil-specific canon in this pass.

## 10. Solids-Load Concept Separation

Solids concepts to keep separate:

| Concept | Meaning | Current/future interpretation |
| --- | --- | --- |
| feed-linked dry-solids potential | Gross dry solid-waste mass implied by feed input and a dry-solids coefficient. | Can be a provisional estimate only with an explicit coefficient or named demo assumption. |
| uneaten-feed fraction | Portion of feed not consumed and entering the waste stream. | Scenario/operator input; not known from feed rate alone. |
| settleable solids | Solids that settle under still conditions and can load clarifiers/settlers. | Needs solids split or direct observation; not the same as total dry solids. |
| suspended solids / TSS | Solids remaining suspended in water as concentration. | Needs water volume, sampling basis, flow, removal, and measurement or model. |
| wet sludge | Removed sludge mass including water. | Not derivable from dry-solids potential without moisture/sludge handling basis. |
| solids-removal capacity | Ability of clarifiers, swirl separators, radial-flow settlers, filters, or purge schedules to remove solids. | Needs filter design, retention, flow, maintenance, and efficiency assumptions. |

## 11. Solids Concept Classification

| Solids concept | Classification | Rationale |
| --- | --- | --- |
| direct solids load supplied by scenario | `calculable_now` | A later helper could echo/normalize a supplied dry-solids load without inferring it from feed. |
| feed-linked dry-solids potential | `scenario_input_required` | Can be estimated from feed only if `dry_solids_fraction_of_feed` is supplied or explicitly set as a named UVI-like demo assumption. |
| UVI-like `0.25 * feed` dry-solids potential | `warning_only` | Useful demo assumption, but should carry `provisional` and `not canon` labels. |
| uneaten-feed fraction | `scenario_input_required` | Depends on feeding management and fish behavior. |
| settleable solids | `blocked` | Needs split, observation, or settler-specific evidence. |
| suspended solids / TSS | `blocked` | Requires concentration, sampling, volume, flow, and removal context. |
| wet sludge | `blocked` | Dry solids cannot be converted to wet sludge without moisture/sludge basis. |
| solids-removal capacity | `scenario_input_required` | Needs filter type, flow, retention, purge/cleaning schedule, and efficiency basis. |
| solids carryover to DWC/root zone | `warning_only` | Can warn when removal context is missing; should not quantify without inputs. |

Feed can support only one cautious first solids estimate:

- `provisional_dry_solids_potential_kg_day = feed_kg_day * dry_solids_fraction_of_feed`

That estimate should be emitted only when the coefficient is explicitly
supplied or when the scenario clearly opts into a named UVI-like demo
assumption. It must not be presented as wet sludge, TSS concentration,
settleable-solids load, or removal-capacity evidence.

## 12. Solids-Removal Context Requirements

Minimum context before claiming solids-removal capacity:

- filter or separator type
- target solids class: settleable, suspended/TSS, floatable, or mixed
- flow rate through the component
- component volume or geometry
- clarifier/settling retention time
- purge frequency and method
- filter-cleaning frequency
- solids-retention/mineralization strategy
- estimated or measured removal efficiency
- downstream carryover location, especially DWC/root zone
- whether retained solids are allowed to decompose in system

Safe UVI-like demo assumptions, if explicitly labelled:

- clarifier detention around `20 minutes`
- clarifier purge around `three times daily`
- polishing/filter cleaning around `once or twice weekly`
- separate DWC/root-zone aeration and maintenance context

These should not become universal defaults.

## 13. Warning Labels And Blocked Claims

Recommended future P1.5 warning labels:

| Label | Trigger |
| --- | --- |
| `aeration_capacity_unavailable` | Oxygen demand exists but no usable aeration or oxygen-transfer capacity basis is supplied. |
| `oxygen_transfer_assumption_missing` | Equipment is supplied but transfer basis, diffuser depth/layout, SOTR/SAE, or in-situ derating is missing. |
| `measured_do_missing` | No measured DO value is supplied for the relevant loop. |
| `measured_do_not_future_safety` | Measured DO exists but should not be treated as proof of future safety. |
| `fish_respiration_oxygen_demand_unavailable` | Fish respiration is not modelled or supplied. |
| `organic_waste_oxygen_demand_unavailable` | Waste/decomposition oxygen demand is not modelled or supplied. |
| `total_oxygen_demand_unavailable` | Only nitrification oxygen demand is available. |
| `nitrification_oxygen_not_total_oxygen` | Report shows nitrification oxygen demand without total oxygen context. |
| `dwc_root_zone_aeration_context_missing` | DWC/raft context exists but plant-side aeration is not declared. |
| `solids_load_coefficient_missing` | Feed is known but no solids coefficient or direct solids load is supplied. |
| `solids_translation_provisional` | A feed-linked dry-solids estimate is emitted from a scenario/demo coefficient. |
| `solids_removal_capacity_unavailable` | Solids load/context exists but filter/removal capacity inputs are missing. |
| `clarifier_settling_retention_missing` | Clarifier/settler context exists but retention time is missing. |
| `backup_aeration_power_continuity_missing` | No backup aeration, power, oxygen reserve, alarm, or response-time plan is declared. |

Blocked claims:

- fish are safe
- system is safe
- aeration capacity is adequate
- oxygen transfer is adequate
- tank is suitable
- measured DO proves future safety
- DWC/root-zone oxygen is covered by fish-tank aeration
- biofilter removes the load
- wet sludge mass is known from dry-solids potential
- TSS concentration is known from dry-solids potential
- solids-removal capacity is known without filter design inputs
- feed cost is known
- profitability is known
- basil saleable harvest mass is known

## 14. Safe First Implementation Options

| Option | Description | Value | Risk | Readiness |
| --- | --- | ---: | --- | --- |
| Warning-only aeration context | Add labels for missing total oxygen, fish respiration, transfer basis, measured DO, DWC aeration, and backup continuity. | 8 | low | ready after field naming |
| Measured-DO context labels only | Accept measured DO plus location/timing/threshold basis and emit context labels without safety claims. | 7 | medium | needs threshold-basis wording |
| Feed-linked provisional dry-solids potential | Estimate gross dry-solids potential from feed only when coefficient is supplied or a named UVI-like demo assumption is explicit. | 8 | medium | needs coefficient provenance label |
| No equipment capacity comparison yet | Keep aeration capacity unresolved unless transfer basis and scope are explicit. | 9 | low | ready |
| Feed-based total oxygen envelope | Use `0.3-0.75 kg O2/kg feed` as a scenario-context envelope. | 6 | medium | needs careful wording and solids-retention context |

Recommended first implementation option:

- Add warning-only P1.5 context labels first.
- Optionally add feed-linked provisional dry-solids potential only when
  `dry_solids_fraction_of_feed` is explicitly supplied or the scenario names a
  UVI-like demo assumption.
- Do not compare oxygen demand to equipment capacity in the first P1.5 pass.
- Do not emit safe/unsafe or adequacy labels.

## 15. Recommended Smallest P1.5 Implementation Surface

Smallest future implementation surface:

- Add a new isolated helper, for example `src/mvp_aeration_solids_context.py`,
  for warning-label logic and optional feed-linked dry-solids potential.
- Extend `src/mvp_mode_a_feed_load_report.py` only after the helper contract is
  tested.
- Extend `scripts/build_mvp_mode_a_feed_load_report.py` only to pass through
  approved optional P1.5 inputs.
- Add a new optional demo input file rather than modifying the existing
  load-only or P1 example inputs.
- Add targeted tests for:
  - load-only report unchanged
  - P1 report unchanged
  - P1.5 warning-only context
  - partial P1.5 input validation
  - optional dry-solids potential with explicit coefficient
  - no disallowed safety, cost, suitability, removal, or saleability outputs

Candidate future files:

- `src/mvp_aeration_solids_context.py`
- `src/mvp_mode_a_feed_load_report.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json`
- `tests/test_mvp_aeration_solids_context.py`
- `tests/test_mvp_mode_a_feed_load_report.py`
- `tests/test_build_mvp_mode_a_feed_load_report.py`

Do not integrate into `src/simulate_day.py` yet. Do not modify runtime outputs
or `data/simulation/**`.

## 16. Validation Plan For Later Implementation

Later implementation validation should check:

- Existing Mode A load-only tests still pass.
- Existing P1 TAN/NH3 helper and report tests still pass.
- `oxygen_demand_g_day` remains nitrification-support oxygen demand.
- No total oxygen demand is emitted from nitrification oxygen alone.
- No aeration-capacity comparison is emitted without transfer basis and scope.
- No measured DO value is treated as proof of future safety.
- DWC/root-zone aeration context remains separate from fish-tank aeration.
- No wet sludge or TSS concentration is calculated from dry-solids potential.
- No solids-removal capacity is claimed without filter design inputs.
- No feed cost, tank suitability, Mode B, biofilter removal, safe/unsafe label,
  or basil saleable output appears.
- UVI-like values remain labelled as demo assumptions, not canon.
- `src/simulate_day.py` remains untouched.
- Protected-path git checks show no unintended edits.

Suggested command checks for a future implementation pass:

- Python compile check for modified Python files.
- Targeted unit tests for load helper, P1 helper, report builder, demo runner,
  and any new P1.5 helper.
- Direct demo command for load-only, P1, and P1.5 examples.
- `git --no-pager diff --name-only -- data/knowledge data/simulation docs`
- `git --no-pager diff --name-only -- src/simulate_day.py`
- `git status --short`

## 17. What Remains Out Of Scope

Out of scope for P1.5:

- fish safety claims
- system safety claims
- threshold pass/fail logic
- total oxygen demand from nitrification oxygen alone
- fish respiration model implementation
- organic-waste/decomposition oxygen model implementation
- actual aeration or oxygen-transfer capacity
- equipment sizing or adequacy claims
- DWC/root-zone oxygen adequacy claims
- wet sludge estimates
- TSS concentration estimates
- solids-removal capacity
- biofilter removal
- feed cost
- tank suitability
- Mode B biomass-derived feeding
- basil saleable harvest mass
- basil revenue or profitability
- runtime simulation-flow integration

## 18. Blockers

No blockers for this docs-only design pass.

Blockers for later implementation unless resolved in that pass:

- final P1.5 input field names
- whether a first implementation is warning-only or also emits dry-solids
  potential
- whether `0.25 * feed_kg_day` may be used only as a named UVI-like demo
  assumption or must be user-supplied as `dry_solids_fraction_of_feed`
- measured DO field basis: location, timing, threshold basis, and measurement
  quality
- aeration-capacity field basis: SOTR, SAE, airflow, oxygenation equipment,
  diffuser layout, in-situ derating, or observed performance
- fish-respiration model evidence
- organic-waste/decomposition oxygen-demand evidence
- solids-removal capacity evidence by filter type and maintenance pattern

These are design and scenario-input issues, not reasons to edit canon.

## 19. Recommended Next Action

Keep this note as the P1.5 design artifact.

Recommended next repo-side pass:

- Implement the smallest warning-only P1.5 context helper, or
- run a short review pass to decide whether dry-solids potential should require
  a user-supplied coefficient or may use a named UVI-like demo coefficient.

If implementation comes next, keep it isolated:

- do not modify `src/simulate_day.py`
- do not modify canonical files
- do not calculate safe/unsafe labels
- do not compare against thresholds
- do not calculate feed cost, tank suitability, biofilter removal, wet sludge,
  TSS concentration, or basil saleable output
