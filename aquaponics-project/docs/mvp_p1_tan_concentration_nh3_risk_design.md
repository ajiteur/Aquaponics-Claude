# MVP P1 TAN Concentration and NH3 Risk Design

## 1. Purpose

Define a docs-only design plan for adding optional TAN-N concentration and
unionized NH3 risk interpretation to the Mode A MVP feed-load report path.

The design keeps three different questions separate:

- How much TAN-N load is produced?
- What estimated TAN-N concentration does that load imply in a named control
  volume?
- What estimated unionized NH3 risk follows only after pH, temperature, and
  threshold basis are explicit?

This pass does not implement calculations and does not propose final code diffs.

## 2. Scope

In scope:

- P1 research ingestion for tank volume, exchange, TAN concentration, and NH3
  risk.
- Optional concentration and NH3-risk design for the existing Mode A report
  path.
- Unit, scope, threshold-basis, and warning-label conventions.
- Recommended smallest future implementation surface.

Out of scope:

- Canonical biology/model/business edits.
- Ontology edits.
- Runtime or simulation-flow integration.
- Script, source, or test edits in this pass.
- Feed cost, tank suitability, Mode B, biofilter-removal, or basil saleability
  implementation.

## 3. Inputs Reviewed

Primary P1 research input:

- `data/sources/research_reports/markdown/Tank Volume, Exchange and TAN-to-NH3 Risk Research Pack.md`

Implemented MVP assets:

- `src/feed_waste_tan_loads.py`
- `src/mvp_mode_a_feed_load_report.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `tests/test_feed_waste_tan_loads.py`
- `tests/test_mvp_mode_a_feed_load_report.py`
- `tests/test_build_mvp_mode_a_feed_load_report.py`

Supporting docs:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_tilapia_feed_research_ingestion_review.md`
- `docs/mvp_mode_a_feed_load_integration_surface_plan.md`
- `docs/mvp_mode_a_feed_load_customer_demo_walkthrough.md`

## 4. Current Mode A Status

The current MVP Mode A path is valid and should remain load-only.

Current required inputs:

- `feed_kg_day`
- `protein_fraction`

Current calculated outputs:

- `tan_n_load_kg_day`
- `tan_n_load_g_day`
- `oxygen_demand_g_day`
- `alkalinity_demand_g_caco3_day`

Current boundaries:

- no TAN concentration
- no unionized NH3 toxicity
- no feed cost
- no tank suitability
- no biofilter removal
- no Mode B biomass-derived feeding
- no basil saleable output

The P1 layer should extend this report path only when explicit optional context
is supplied. It should not weaken the current missing-context labels.

## 5. P1 Research Summary

The P1 research supports these implementation-relevant findings:

- Load, concentration, and NH3 risk must stay separate.
- TAN-N load from feed is not already a TAN concentration.
- TAN concentration requires a named control volume and a time basis.
- Unionized NH3 risk cannot be estimated from TAN alone; it requires pH and
  water temperature.
- The safest concentration basis is TAN-N mg/L.
- The clean freshwater speciation path starts from TAN-N mg/L, estimates a
  unionized NH3 fraction, then estimates NH3-N mg/L.
- Optional conversion to NH3 mg/L should use the 17/14 molecular-weight factor
  only when the comparison threshold is stated as NH3 rather than NH3-N.
- Fish-tank exposure and whole-system average concentration are not equivalent.
- The UVI commercial raft system is the strongest demo benchmark for a
  tilapia + basil DWC/raft example, but its volumes and residence times are
  demo assumptions, not canon.
- No universal tank-volume, retention, exchange-rate, stocking-density, or
  biofilter-removal default is defensible.
- Biofilter conversion remains conditional on maturity, oxygen, alkalinity,
  pH, architecture, cleaning practice, and flow context.

## 6. Three-Stage Load/Concentration/NH3 Interpretation Chain

Stage 1: TAN-N load

- Input basis: direct `feed_kg_day` and `protein_fraction`.
- Output basis: `tan_n_load_kg_day` and `tan_n_load_g_day`.
- Interpretation: daily TAN-N / ammonia-N mass load.
- Boundary: not concentration, not toxicity, not removal.

Stage 2: estimated TAN-N concentration

- Input basis: Stage 1 load, effective water volume, time basis, concentration
  scope, and explicit exchange/removal assumption if used.
- Output basis: `estimated_tan_n_mg_l`.
- Interpretation: estimated TAN-N concentration in a named scope.
- Boundary: not unionized NH3 risk until pH and temperature are supplied.

Stage 3: estimated unionized NH3 risk

- Input basis: estimated TAN-N concentration, pH, water temperature,
  freshwater/salinity assumption, and explicit threshold unit basis.
- Output basis: `estimated_unionized_nh3_fraction`,
  `estimated_nh3_n_mg_l`, and optional `estimated_nh3_mg_l`.
- Interpretation: estimated unionized ammonia concentration and threshold
  comparison only when threshold basis is unambiguous.
- Boundary: not a claim that the system is safe, profitable, or adequately
  aerated.

## 7. Concentration Scopes

Supported concentration scopes:

| Scope | Meaning | Appropriate use | Key warning |
| --- | --- | --- | --- |
| `fish_tank` | Estimate concentration in the fish exposure control volume. | First risk-facing scope for tilapia NH3 interpretation. | Still not a post-feeding peak unless the time basis is peak-oriented. |
| `system_average` | Estimate concentration over total effective system volume. | Nutrient-context and slower whole-system planning. | Not equivalent to fish-tank exposure. |
| `both` | Emit fish-tank and system-average estimates side by side. | Later comparison/reporting mode. | Requires both volume bases and clear labels. |

Do not use total system volume as the denominator for fish exposure unless the
report explicitly says it is a system-average estimate and not fish-tank risk.

## 8. Recommended First Implementation Scope

Recommended first scope: `fish_tank` upper-bound/no-removal concentration.

Why this is safest:

- It is closest to fish exposure.
- It avoids pretending the full system is instantly mixed.
- It does not require claiming biofilter removal.
- It preserves the current boundary that nitrification demand is not actual
  conversion.
- It is easier to explain to customers and advisors than a mixed-loop model.

Recommended first-mode concentration basis:

```text
estimated_tan_n_mg_l =
  tan_n_load_g_period * 1000 / fish_tank_volume_l
```

If starting from `tan_n_load_g_day`:

```text
tan_n_load_g_period =
  tan_n_load_g_day * accumulation_period_hours / 24
```

This should be labelled as an upper-bound/no-removal estimate unless exchange
and removal assumptions are explicitly supplied. It should not be called actual
observed concentration or system safety.

## 9. Unit Conventions

Recommended field and unit conventions:

| Field | Unit | Meaning |
| --- | --- | --- |
| `tan_n_load_kg_day` | kg TAN-N/day | Feed-derived TAN-N load. |
| `tan_n_load_g_day` | g TAN-N/day | Feed-derived TAN-N load. |
| `estimated_tan_n_mg_l` | mg TAN-N/L | Estimated TAN-N concentration for a named scope. |
| `estimated_unionized_nh3_fraction` | dimensionless fraction | Fraction of TAN present as unionized NH3 under pH and temperature context. |
| `estimated_nh3_n_mg_l` | mg NH3-N/L | Estimated unionized ammonia expressed as nitrogen. |
| `estimated_nh3_mg_l` | mg NH3/L | Optional output only when an NH3-basis threshold or display need exists. |

Keep TAN-N as the concentration basis for the first implementation. Convert to
NH3 only after speciation and only when the threshold basis requires it.

## 10. Threshold-Basis Conventions

Every threshold comparison must carry an explicit basis:

| Threshold basis | Meaning | Use rule |
| --- | --- | --- |
| `NH3-N` | Unionized ammonia expressed as nitrogen. | Compare directly to `estimated_nh3_n_mg_l`. |
| `NH3` | Unionized ammonia expressed as NH3 molecule. | Compare to `estimated_nh3_mg_l`, or convert threshold to NH3-N using 14/17. |
| `TAN-N` | Total ammonia nitrogen concentration. | Use only for TAN concentration guidance, not unionized toxicity. |
| `ambiguous` | Source says ammonia without clear basis. | Block comparison until basis is reviewed. |

Do not compare a threshold to an output with a different basis unless the
conversion path is explicit and recorded.

## 11. Minimum Input Set For TAN-N Concentration

Minimum input set for an upper-bound/no-removal estimate:

- Stage 1 TAN-N load over a defined time period.
- `effective_water_volume_l`.
- `accumulation_period_hours` or equivalent time basis.
- `concentration_scope`: `fish_tank`, `system_average`, or `both`.
- Explicit declaration that the estimate is no-removal/no-dilution.

Minimum input set for any estimate using exchange, retention, or removal:

- Stage 1 TAN-N load over a defined time period.
- Named control volume.
- Effective volume for that scope.
- Timestep / accumulation period.
- Exchange or retention basis.
- Biofilter-removal assumption or biofilter state.
- Replacement or inflow TAN-N basis if exchange/dilution is non-zero.

If these inputs are missing, keep the report in warning-only mode.

## 12. Minimum Input Set For NH3 Risk

Minimum input set:

- `estimated_tan_n_mg_l`.
- `pH`.
- `water_temperature_c`.
- Freshwater/salinity assumption.
- Threshold unit basis: `NH3-N`, `NH3`, `TAN-N`, or `ambiguous`.

Recommended additional inputs before public-facing risk bands:

- threshold value
- exposure-duration basis
- fish life stage
- pH measurement quality or timestamp
- temperature measurement quality or timestamp
- whether the concentration is daily average or post-feeding peak

Without pH and water temperature, the report must not calculate NH3 risk.

## 13. Unionized NH3 Fraction Method

Recommended freshwater method:

```text
Tk = water_temperature_c + 273.2
pKa = 0.0901821 + 2729.92 / Tk
estimated_unionized_nh3_fraction = 1 / (10^(pKa - pH) + 1)
estimated_nh3_n_mg_l = estimated_tan_n_mg_l * estimated_unionized_nh3_fraction
```

Optional conversion:

```text
estimated_nh3_mg_l = estimated_nh3_n_mg_l * 17 / 14
```

Use the optional NH3 conversion only when a downstream threshold or display
explicitly uses NH3 rather than NH3-N.

Unit caveats:

- The formula is for freshwater / zero or dilute salinity.
- Salinity requires correction or a blocked warning.
- TAN-N should not be converted directly to "TAN as NH3" without speciation.
- Ambiguous ammonia thresholds should block comparison.

## 14. UVI-Like Demo Benchmark Assumptions

The UVI-like values may be used later as a named demo preset. They must not be
promoted to canon and must not become universal defaults.

Candidate UVI-like demo assumptions:

| Field | Demo value | Use |
| --- | ---: | --- |
| `fish_tank_volume_l` | `7800` | Fish-tank concentration scope. |
| `total_system_volume_l` | `111196` | System-average scope. |
| `recirculation_flow_l_min` | `378` | Flow/retention context. |
| `rearing_tank_retention_h` | `1.37` | Fish-tank retention context. |
| `clarifier_retention_min` | `19-20` | Clarifier context. |
| `dwc_raft_retention_h` | `3` | Plant-trough retention context. |

Optional UVI-like context:

- weekly partial replacement around 5 percent only when explicitly labelled
  UVI-like
- freshwater assumption
- pH compromise around 7.0 as a demo scenario assumption, not a universal target

These values are useful for customer/advisor demos because they show fish tank
and whole-system average are not the same exposure basis.

## 15. Warning Labels And Blocked Claims

Recommended P1 warning labels:

| Label | Trigger |
| --- | --- |
| `tan_concentration_unavailable_missing_control_volume` | TAN-N load exists but no effective volume is supplied. |
| `tan_concentration_unavailable_missing_time_basis` | TAN-N load exists but no accumulation period is supplied. |
| `tan_concentration_scope_missing_or_ambiguous` | Scope is absent or not one of `fish_tank`, `system_average`, or `both`. |
| `tan_concentration_upper_bound_no_removal` | Concentration is estimated with no exchange/removal. |
| `biofilter_removal_assumption_missing` | Removal is needed for a non-upper-bound estimate but not supplied. |
| `nh3_risk_unavailable_missing_ph` | TAN-N concentration exists but pH is missing. |
| `nh3_risk_unavailable_missing_temperature` | TAN-N concentration exists but temperature is missing. |
| `nh3_fraction_blocked_missing_freshwater_or_salinity_basis` | pH and temperature exist but salinity/freshwater basis is not explicit. |
| `threshold_unit_basis_mismatch` | Threshold and output bases differ without explicit conversion. |
| `threshold_unit_basis_ambiguous_blocked` | Threshold says ammonia but does not state TAN-N, NH3-N, or NH3. |
| `system_average_not_equivalent_to_fish_tank_exposure` | System-average scope is used for fish-risk discussion. |
| `daily_average_not_equivalent_to_post_feeding_peak` | Daily average is used where peak exposure could matter. |
| `saleable_harvest_mass_unresolved` | Basil saleable output is not observed or explicitly reviewed. |

Blocked claims:

- system is safe
- fish are safe from NH3
- tank is suitable
- biofilter removes the load
- aeration capacity is adequate
- feed cost is known
- profitability is known
- basil saleable harvest mass is known

## 16. Missing-Context Labels That Can Become Calculated Outputs

These current missing-context areas can become calculated outputs after enough
inputs exist:

| Current area | Future calculated output |
| --- | --- |
| TAN concentration unavailable | `estimated_tan_n_mg_l` with a named concentration scope. |
| NH3 risk unavailable | `estimated_unionized_nh3_fraction`, `estimated_nh3_n_mg_l`, optional `estimated_nh3_mg_l`. |
| Fish-tank volume missing | fish-tank estimate once `fish_tank_volume_l` and time basis exist. |
| System volume missing | system-average estimate once `total_system_volume_l` and time basis exist. |
| Retention unknown | `estimated_rearing_tank_retention_h`, `estimated_clarifier_retention_min`, or `estimated_dwc_raft_retention_h` when volume and flow are supplied. |

These outputs should remain estimates, not observations.

## 17. Missing-Context Labels That Should Remain Warnings

These should remain warnings even when some inputs exist:

- actual biofilter removal efficiency unknown
- actual post-feeding peak transient unknown
- actual nitrifying biofilm condition unknown
- pH measurement quality unknown
- salinity correction unknown
- threshold unit basis mismatch
- whole-system average not equivalent to fish-tank exposure
- daily average not equivalent to post-feeding peak
- aeration demand not equivalent to aeration capacity
- basil saleable output unresolved

These are not just missing fields. They are epistemic boundaries that protect
the report from overstating system safety.

## 18. Safe First Implementation Options

| Option | Description | Value | Risk | Readiness |
| --- | --- | ---: | --- | --- |
| Upper-bound no-removal fish-tank estimate | Estimate `estimated_tan_n_mg_l` from TAN-N load, fish-tank volume, and time basis. | 9 | low | ready after field naming |
| Fish-tank scope only | Emit concentration and NH3 risk only for fish-tank scope. | 9 | low | recommended first scope |
| System-average scope only | Estimate over total system volume. | 5 | medium | useful later but can mislead fish-risk interpretation |
| Both scopes | Emit fish-tank and system-average side by side. | 8 | medium | needs more report design |
| Warning-only mode | Keep current labels when required inputs are absent. | 8 | low | already aligned with current MVP |

Recommended sequence:

1. Add warning-only field support for missing P1 inputs.
2. Add fish-tank upper-bound/no-removal concentration.
3. Add NH3 fraction and NH3-N only when pH, temperature, and freshwater basis
   are explicit.
4. Add system-average or `both` only after report wording makes the exposure
   distinction unmistakable.

## 19. Recommended Smallest P1 Implementation Surface

Smallest future implementation surface:

- New helper module, for example `src/mvp_tan_nh3_risk.py`.
- Extend `src/mvp_mode_a_feed_load_report.py` to call the helper only when P1
  optional inputs are supplied.
- Add targeted tests for the new helper.
- Extend report-builder tests for calculated and warning-only paths.
- Extend the demo runner accepted input fields only after the report builder
  supports them.
- Extend `scripts/example_mvp_mode_a_feed_load_inputs.json` with named
  UVI-like demo assumptions only if the implementation pass explicitly approves
  that example update.

Do not integrate into `src/simulate_day.py` yet. Do not modify runtime outputs
or `data/simulation/**`.

Candidate future files:

- `src/mvp_tan_nh3_risk.py`
- `src/mvp_mode_a_feed_load_report.py`
- `scripts/build_mvp_mode_a_feed_load_report.py`
- `scripts/example_mvp_mode_a_feed_load_inputs.json`
- `tests/test_mvp_tan_nh3_risk.py`
- `tests/test_mvp_mode_a_feed_load_report.py`
- `tests/test_build_mvp_mode_a_feed_load_report.py`

## 20. Validation Plan For Later Implementation

Later implementation validation should check:

- Existing Mode A load-only tests still pass.
- No concentration output appears without control volume and time basis.
- No NH3 output appears without TAN-N concentration, pH, temperature, and
  freshwater/salinity basis.
- Fish-tank and system-average scopes are labelled separately.
- System-average output carries a warning when used without fish-tank exposure.
- Daily average output carries a warning when post-feeding peak could matter.
- No biofilter removal is calculated unless a later pass explicitly approves a
  removal model.
- Threshold comparisons block on ambiguous ammonia basis.
- NH3-N to NH3 conversion uses 17/14 only when required.
- UVI-like values are labelled demo assumptions, not canon.
- No feed cost, tank suitability, Mode B, or basil saleable output appears.
- `src/simulate_day.py` remains untouched.
- Protected-path git checks show no unintended edits.

Suggested command checks for a future implementation pass:

- Python compile check for modified files.
- Targeted unit tests for load helper, report builder, P1 helper, and demo
  runner.
- Direct demo command with and without P1 context.
- `git --no-pager diff --name-only -- data/knowledge data/simulation docs`
- `git --no-pager diff --name-only -- src/simulate_day.py`
- `git status --short`

## 21. What Remains Out Of Scope

Out of scope for P1:

- actual biofilter removal
- actual post-feeding peak transient
- actual plant-side nitrification contribution
- actual aeration capacity
- feed cost
- tank suitability
- stocking-density suitability
- Mode B biomass-derived feeding
- feed-rate defaults by fish stage
- basil saleable harvest mass
- basil revenue or profitability
- runtime simulation-flow integration

## 22. Blockers

No blockers for this docs-only design pass.

Blockers for implementation unless resolved in the next pass:

- final P1 input field names
- exact report output section names for concentration and NH3 risk
- threshold comparison policy and threshold value source
- whether first implementation emits only fish-tank scope or also allows
  system-average behind explicit scope input
- how to represent no-removal versus removal-assumption modes

These are design choices, not reasons to edit canon.

## 23. Recommended Next Action

Run a tightly scoped P1 implementation pass that adds a new helper for
fish-tank upper-bound/no-removal TAN-N concentration and freshwater NH3-N
estimation.

Keep the implementation optional in the Mode A report path:

- if P1 inputs are absent, keep current missing-context labels
- if fish-tank volume and time basis exist, calculate fish-tank
  `estimated_tan_n_mg_l`
- if pH, temperature, and freshwater basis exist, calculate
  `estimated_unionized_nh3_fraction` and `estimated_nh3_n_mg_l`
- keep all safety, profitability, biofilter-removal, tank-suitability, and
  basil-saleability claims blocked
