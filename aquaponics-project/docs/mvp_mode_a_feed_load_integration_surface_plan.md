# MVP Mode A Feed Load Integration Surface Plan

## Purpose

Define the smallest safe surface for using the existing Mode A
fish-feed-to-TAN-N load helper in an MVP demo/report without changing the
simulation runtime schema, business revenue logic, or basil harvest saleability
logic.

This is a review-first planning note only. It does not propose final code diffs
and does not implement integration.

## Scope

In scope:

- Confirm the current Mode A helper and tests.
- Identify where explicit demo inputs should come from.
- Define report fields for load-only outputs.
- Define missing-context status labels for values that must not be calculated
  yet.
- Compare candidate integration locations.
- Recommend the smallest future implementation pass.

Out of scope for this pass:

- Modifying `data/knowledge/**`, `data/simulation/**`, `src/**`, `scripts/**`,
  or tests.
- Runtime schema redesign.
- TAN concentration calculation.
- Unionized NH3 toxicity calculation.
- Feed cost calculation.
- Tank suitability calculation.
- Mode B biomass-derived feeding.
- Biofilter removal or actual conversion modeling.
- Basil harvest or saleability logic.

## Inputs reviewed

Primary inputs:

- `docs/mvp_fish_feed_waste_tan_engine_design.md`
- `docs/mvp_tilapia_feed_research_ingestion_review.md`
- `src/feed_waste_tan_loads.py`
- `tests/test_feed_waste_tan_loads.py`

Comparison-only inputs:

- `src/simulate_day.py`
- `src/simulate_n_days.py`
- `scripts/build_first_slice_adapter_payload.py`
- `scripts/calculate_first_slice_unit_economics.py`
- `scripts/validate_first_slice_inputs.py`
- `src/**`, `scripts/**`, and `tests/**` file inventory and report/output
  search results

Current commit context:

- The Mode A load-only helper exists in the repo and was committed as
  `b098df0 Add MVP feed to TAN load calculator`.

## Current helper status

The helper exists at `src/feed_waste_tan_loads.py`.

The targeted test file exists at `tests/test_feed_waste_tan_loads.py`.

The helper is Mode A load-only:

- It requires direct `feed_kg_day`.
- It requires direct `protein_fraction`.
- It calculates `tan_n_load_kg_day`.
- It calculates `tan_n_load_g_day`.
- It calculates `oxygen_demand_g_day`.
- It calculates `alkalinity_demand_g_caco3_day`.
- It returns calculation-basis metadata.

The helper intentionally does not implement:

- TAN concentration.
- Unionized NH3 toxicity.
- Feed cost.
- Tank suitability.
- Mode B biomass-derived feeding.
- Biofilter removal or actual nitrification conversion.
- Basil saleability logic.
- `saleable_harvest_mass_kg` inference or population.

The helper treats the calculated nitrogen load as TAN-N / ammonia-N load, not
unionized NH3.

## Proposed demo input surface

For the next demo/report layer, inputs should come from an explicit,
non-canonical scenario/report input object supplied by the caller. That object
can later be provided by a small CLI, a test fixture, or a notebook-style demo,
but it should not be read from canonical knowledge files and should not require
writing to `data/simulation/**`.

Required Mode A inputs:

| Field | Unit | Required | Role |
| --- | --- | --- | --- |
| `scenario_id` | string | yes | Human-readable demo/report identifier. |
| `input_mode` | enum/string | yes | Must be `mode_a_direct_feed`. |
| `feed_kg_day` | kg feed/day | yes | Direct feed input passed to the helper. |
| `protein_fraction` | fraction 0 to 1 | yes | Direct protein fraction passed to the helper. |

Optional context-only demo inputs:

| Field | Unit | Role |
| --- | --- | --- |
| `scenario_label` | string | Display label only. |
| `feed_class` | string | Descriptive feed class; not a canonical default. |
| `protein_fraction_basis` | string | Source or assumption note, such as feed label or demo assumption. |
| `feeding_frequency_per_day` | count/day | Display context only. |
| `expected_fcr_band` | ratio | Demo assumption only; must not calculate feed or growth in Mode A. |
| `system_architecture` | string | Architecture context such as DWC/raft; not a permanent canonical winner. |
| `crop_context` | string | Optional basil context only; no saleable output inference. |

Optional fields that may support status labels only:

| Field | Unit | Current use |
| --- | --- | --- |
| `system_water_volume_l` | L | If absent, report that concentration is not calculated. |
| `time_basis` | string | If absent, report that concentration/time interpretation is incomplete. |
| `exchange_or_retention_basis` | string | If absent, report that dilution/removal context is incomplete. |
| `pH` | pH units | If absent, report that NH3 risk is not calculated. |
| `water_temperature_c` | C | If absent, report that NH3 risk is not calculated. |
| `feed_price_per_kg` | currency/kg | If absent, report that feed cost is not calculated. |
| `tank_volume_l` | L | If absent, report that tank suitability is not calculated. |
| `stocking_density_kg_m3` | kg/m3 | If absent, report that tank suitability is not calculated. |
| `biofilter_capacity_basis` | string | If absent, report that biofilter capacity/removal is not calculated. |

The implementation should use `feed_kg_day` as the internal field name because
that is the helper API. A later CLI may accept `feed_kg_per_day` as an alias
only if it normalizes explicitly to `feed_kg_day` before calling the helper.

## Proposed report output surface

The report should echo the direct input basis and return only physical loads
plus status labels for missing layers.

Required report fields:

| Field | Unit | Source |
| --- | --- | --- |
| `scenario_id` | string | Input echo. |
| `input_mode` | string | Must be `mode_a_direct_feed`. |
| `feed_kg_day` | kg feed/day | Helper input echo. |
| `protein_fraction` | fraction 0 to 1 | Helper input echo. |
| `tan_n_load_kg_day` | kg TAN-N/day | Helper output. |
| `tan_n_load_g_day` | g TAN-N/day | Helper output. |
| `oxygen_demand_g_day` | g O2/day | Helper output for nitrification oxygen demand. |
| `alkalinity_demand_g_caco3_day` | g CaCO3/day | Helper output for alkalinity demand. |
| `calculation_basis` | object | Helper metadata plus report-level boundaries. |
| `status_labels` | array/string list | Missing-context labels. |

Optional report display aliases may be added later, but the smallest pass should
keep the helper output keys unchanged to avoid remapping errors.

The report must not emit:

- `tan_mg_l` or `tan_mg_L` derived from feed.
- `unionized_nh3_mg_l` or `unionized_nh3_mg_L` derived from TAN.
- Feed cost derived from feed amount.
- Tank-size suitability.
- Fish biomass-derived feed.
- Biofilter removal amount or actual conversion rate.
- `saleable_harvest_mass_kg` derived from plant biomass, plant gain, plant
  count, or any other proxy.

## Missing-context status labels

Recommended labels for the first report layer:

| Label | Trigger | Meaning |
| --- | --- | --- |
| `tan_concentration_not_calculated_missing_volume_time_exchange_or_removal` | Water volume, time basis, exchange/retention, or removal basis is absent. | TAN-N load is available, but mg/L concentration is not calculated. |
| `nh3_risk_not_calculated_missing_ph_or_temperature` | pH or temperature is absent. | Unionized NH3 risk is not calculated from TAN alone. |
| `feed_cost_not_calculated_missing_feed_price` | Feed price is absent. | Feed cost and feed-cost economics are not calculated. |
| `tank_suitability_not_calculated_missing_volume_or_stocking_density` | Tank volume or stocking density is absent. | Tank-size suitability is not asserted. |
| `biofilter_removal_not_calculated_missing_capacity_or_state` | Biofilter capacity/state is absent. | Nitrification demand is not treated as actual biofilter removal. |
| `basil_saleable_output_unresolved` | No observed or explicitly reviewed saleable output is provided. | Basil `saleable_harvest_mass_kg` remains unresolved/null. |

These labels are explanatory report statuses, not automated pass/fail logic.

## Candidate integration locations

The helper can technically be called from multiple surfaces, but most of them
would mix load-only planning with existing runtime or business assumptions.

Candidate locations:

- Scenario/report generator: a narrow report builder that accepts explicit Mode
  A scenario inputs and emits load-only report output.
- Simulation day flow: the existing `src/simulate_day.py` daily runtime update.
- First-slice adapter: the existing basil business adapter payload builder.
- Separate MVP demo script: a one-off CLI-style wrapper around the helper.
- No integration yet: keep only the helper and tests.

## Integration location rating table

| Candidate location | Value | Risk | Readiness | Likely future touched files | Validation requirements | Stop rules |
| --- | ---: | --- | --- | --- | --- | --- |
| Scenario/report generator | 9 | low | ready now | New `src/mvp_mode_a_feed_load_report.py`; new `tests/test_mvp_mode_a_feed_load_report.py`; optional explicit demo input file only if approved. | Import check, targeted report-builder tests, direct calculation check, forbidden-output assertions, protected-path diff check. | Stop if it requires `data/simulation/**`, runtime schema changes, business revenue logic, Mode B, concentration, NH3 toxicity, feed cost, tank suitability, or basil saleability logic. |
| Simulation day flow | 5 | high | blocked | `src/simulate_day.py`, `src/simulate_n_days.py`, runtime-output tests/fixtures. | Full simulation regression tests plus runtime-output review. | Stop because current flow derives feed from biomass, calculates concentration-style TAN updates, models removal, writes runtime output, and includes feed cost. |
| First-slice adapter | 3 | medium | blocked | `scripts/build_first_slice_adapter_payload.py`, adapter examples/tests. | Adapter payload snapshot checks and saleability null-status checks. | Stop because the adapter is scoped to basil business payload alignment and must keep `saleable_harvest_mass_kg` unresolved/null. |
| Separate MVP demo script | 8 | low | needs design | New `scripts/build_mvp_mode_a_feed_load_report.py` only if scripts are explicitly approved; tests or fixture if approved. | CLI smoke test, JSON output check, forbidden-output assertions, protected-path diff check. | Stop if script placement requires modifying existing scripts, generated runtime output, or canonical/demo assumptions without explicit approval. |
| No integration yet | 2 | low | ready now | None. | Existing helper tests only. | Stop if MVP demo/report output is required. |

## Recommended integration location

Use a scenario/report generator that is separate from the simulation day flow.

The safest future call site is a new pure report-builder function that accepts
an explicit Mode A input dictionary, calls `calculate_feed_waste_tan_loads()`,
and returns a report dictionary with load outputs and missing-context labels.

Recommended future surface:

- New report helper: `src/mvp_mode_a_feed_load_report.py`
- New targeted tests: `tests/test_mvp_mode_a_feed_load_report.py`

An optional CLI wrapper or example input file can come later if explicitly
approved. The first implementation should prove the report contract in pure
Python before adding command-line behavior or file placement decisions.

## Why not integrate elsewhere yet

Do not integrate into `src/simulate_day.py` yet because that file currently:

- Derives feed from fish biomass and feed-rate percentage.
- Calculates TAN as an mg/L equivalent using water volume.
- Applies effective nitrification/removal.
- Updates water-state runtime output.
- Estimates unionized NH3 by scaling from old TAN.
- Calculates daily feed cost from economics inputs.

Those behaviors are outside the Mode A load-only boundary and would require a
broader runtime redesign to align with the new helper.

Do not integrate into the first-slice adapter yet because that adapter is
currently focused on basil business payload alignment. Adding fish/feed loads
there would mix separate concerns and could obscure the rule that basil
`saleable_harvest_mass_kg` remains unresolved/null unless observed or explicitly
reviewed.

Do not start with a standalone script if a pure report-builder function can
prove the contract first. A script can wrap the report builder later.

Do not leave the helper unintegrated if the next milestone needs an MVP
demo/report, because a report surface is the smallest useful way to show the
engine spine without changing runtime.

## Smallest future implementation pass

Recommended smallest future pass:

1. Add a new pure report builder in `src/mvp_mode_a_feed_load_report.py`.
2. Accept a caller-supplied Mode A scenario object with `scenario_id`,
   `input_mode`, `feed_kg_day`, and `protein_fraction`.
3. Validate `input_mode == "mode_a_direct_feed"` before calling the helper.
4. Call `calculate_feed_waste_tan_loads(feed_kg_day, protein_fraction)`.
5. Return a report dictionary containing input echoes, helper load outputs,
   calculation basis, and missing-context status labels.
6. Add targeted tests in `tests/test_mvp_mode_a_feed_load_report.py`.

The first implementation pass should not add a CLI, write output files, modify
runtime scenarios, or create canonical defaults.

## Validation plan for future implementation

Future implementation validation should include:

- Syntax/import check for the new report helper and existing load helper.
- Targeted tests for the new report builder.
- Existing `tests/test_feed_waste_tan_loads.py`.
- Direct calculation check for `feed_kg_day = 1.0` and
  `protein_fraction = 0.32`.
- Assertion that output includes:
  - `tan_n_load_kg_day`
  - `tan_n_load_g_day`
  - `oxygen_demand_g_day`
  - `alkalinity_demand_g_caco3_day`
  - `status_labels`
- Assertion that output excludes:
  - TAN concentration fields.
  - Unionized NH3 fields.
  - Feed cost fields.
  - Tank suitability fields.
  - Mode B biomass-derived feed fields.
  - Biofilter removal fields.
  - `saleable_harvest_mass_kg` inferred values.
- Assertion that missing-context labels are present when volume/time/exchange,
  pH/temperature, feed price, tank volume/stocking density, and biofilter
  capacity/state are absent.
- Git checks proving no changes under `data/knowledge/**`,
  `data/simulation/**`, existing runtime files, scripts, or harvest/business
  saleability logic.

## Out of scope

The integration plan does not include:

- Calculating TAN concentration.
- Calculating unionized NH3 fraction or toxicity.
- Calculating feed cost.
- Calculating tank suitability.
- Implementing Mode B.
- Modeling actual biofilter conversion/removal.
- Promoting feed protein, FCR, feeding-rate bands, stocking density, or feed
  cost into canon.
- Treating DWC/raft as a permanent canonical winner.
- Using plant standing biomass, plant daily gain, or plant count as saleable
  harvest mass.
- Populating `saleable_harvest_mass_kg`.
- Runtime schema redesign or generated simulation output changes.

## Blockers

No blocker exists for this docs-only planning pass.

For the next implementation pass, the main non-blocker design decision is
whether to stop at a pure report-builder function or also approve a CLI wrapper
and example input file. The pure report-builder function is sufficient for the
first implementation.

Runtime integration remains blocked until a later pass explicitly redesigns the
relationship between load-only TAN-N outputs, existing mg/L runtime fields,
biofilter conversion, and water-state updates.

## Recommended next action

Run a tightly scoped implementation pass for the scenario/report generator:

- Create `src/mvp_mode_a_feed_load_report.py`.
- Create `tests/test_mvp_mode_a_feed_load_report.py`.
- Reuse `calculate_feed_waste_tan_loads()` unchanged.
- Keep all outputs load-only.
- Emit missing-context status labels instead of calculating concentration,
  NH3 toxicity, feed cost, tank suitability, or saleable basil output.
