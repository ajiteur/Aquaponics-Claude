# First Slice Architecture Runtime Plan

Status: `draft`

## Purpose

- Turn the current first-slice biological baseline into a clear runtime and scenario-planning note.
- Identify the smallest architecture-aware outputs that would materially improve the first slice next.
- Keep the result read-only and planning-focused without changing canon or simulation files.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- `architecture_dwc_raft` is the current first biological baseline only, not a canonical winner.
- The current first-slice economics view is used only as framing context.
- This note does not modify `data/knowledge/**`, runtime files, simulation files, or schemas.
- This note focuses on the smallest useful architecture-aware runtime additions, not a general simulation redesign.

## Current First Slice

- `basil bulk kg wholesale`

## Current First Biological Baseline

- `architecture_dwc_raft`
- Current status: `directionally_supported`
- Current meaning: best-supported first working biological baseline for the slice, not a permanent architecture winner

## Why DWC / Raft Is Being Used as the Current Baseline

- `docs/first_slice_method_comparison.md`
  - DWC or raft is the current best-supported method for the first slice
  - it is still held at `directionally_supported`, not `well_supported`
- `data/knowledge/models/plant_system_models.json`
  - raft is the high-buffer baseline
  - DWC or raft has lower short-term pump fragility than NFT
  - DWC or raft has high nitrification support when solids are removed upstream
  - `baseline_architecture_variant_id` is already `architecture_dwc_raft`
- `data/knowledge/species/plants/basil.json`
  - basil has repeated-cut stress and disease-risk notes
  - the current repo basil profile supports treating stable root-zone conditions and repeated-cut resilience as biologically meaningful
- `docs/runtime_to_business_field_audit.md`
  - `crop_system_type` is now present as a context field on the current basil path
  - the main business blocker remains missing `saleable_harvest_mass_kg`

## Minimum Runtime Fields or Outputs Needed Next

The smallest useful next additions are below. These are planning targets, not immediate schema changes.

### `must_have_next`

| Item | Why it matters next | Planning note |
|---|---|---|
| `crop_system_type` | Minimal architecture-aware bridge into the current business-facing field set. | The active first-slice path now carries `crop_system_type = architecture_dwc_raft` as a context field on the baseline scenario family. |
| One explicit basil DWC or raft scenario frame | Prevents architecture reasoning from staying purely abstract. | The chosen basil scenario should make the DWC or raft baseline explicit at scenario level, not only in later interpretation notes. |
| `saleable_harvest_mass_kg` or harvest output sufficient to roll it up | A real first-slice test still cannot happen without saleable harvested mass. | Direct output is simplest; explicit harvest-event output is acceptable if it cleanly supports adapter-side rollup. |
| Repeated-harvest framing | Basil method comparison is partly about repeated-cut suitability. | At minimum, emit enough harvest-cycle information to distinguish one-time standing biomass from repeated-cut output. |

### `important_but_deferred`

| Item | Why it matters | Why deferred now |
|---|---|---|
| `growing_area_m2` | Needed later for area-normalized labor, CAPEX, and productivity views. | Not required for the narrowest kg-based first slice. |
| `water_use_l` | Needed if NFT water-efficiency claims are later compared fairly. | Current slice is not reopening WUE-driven economics yet. |
| `supplement_input_records` | Useful later for operating-cost realism and stress interpretation. | Not required to prove the first thin bridge. |
| Explicit period bounds | Helpful for cleaner business reporting and repeated-run comparison. | Current adapter work can still use day-count framing first. |

### `needed_for_later_dwc_vs_nft_fair_comparison`

| Item | Why it matters later | Planning note |
|---|---|---|
| Same architecture identifier on paired scenarios | Required to compare DWC or raft and NFT without inference. | Use the same identifier pattern on both scenario families. |
| `growing_area_m2` or stable architecture capacity basis | Needed to compare throughput, density, and area-normalized burden fairly. | A fair DWC-vs-NFT comparison should not rely only on total kg. |
| Downtime or flow-interruption event output | Needed because NFT fragility is one of the strongest biology-to-business differences. | Keep event design minimal and architecture-relevant. |
| Maintenance or intervention event output | Needed to compare NFT unclogging burden against raft cleaning or aeration burden. | Event counts or simple rollups are enough at first. |
| `cull_or_unsaleable_mass_kg` | Needed to compare saleability, shrink, and quality loss fairly. | Especially important if cleanliness or root-zone stress is later compared between architectures. |

## Which Gaps Block a Real Architecture-Aware First-Slice Test Today

- `crop_system_type` is now present on the current basil runtime path, but architecture-conditioned business behavior remains deferred.
- No runtime-facing `saleable_harvest_mass_kg` exists today.
- Current runtime outputs are state snapshots and day-log assessments, not harvest rollups.
- Repeated-cut basil is biologically important, but current runtime outputs do not yet make harvest cycles explicit enough for an architecture-aware first-slice test.
- No runtime-facing `growing_area_m2` or equivalent stable plant-side basis exists yet.
- Current basil scenario framing does not yet give a clean paired DWC-or-raft baseline versus NFT comparison path.

## What a Minimal First DWC / Raft Basil Scenario Should Provide

The minimal first DWC or raft basil scenario does not need full architecture-aware support everywhere. It should provide:

1. One explicit basil scenario artifact whose plant side is clearly tagged as `architecture_dwc_raft`.
2. `crop_id = plant_basil`.
3. `crop_system_type = architecture_dwc_raft` carried explicitly as the current first bridge context field.
4. The existing chemistry, plant-state, and energy fields already used by the thin adapter path.
5. One explicit harvest-ready output path:
   - direct `saleable_harvest_mass_kg`, or
   - harvest-event output sufficient to roll up `saleable_harvest_mass_kg`.
6. Enough repeated-harvest framing to distinguish a repeated-cut basil run from a single standing-biomass snapshot.
7. Scenario-level framing for the DWC or raft conditions that matter biologically:
   - plant-side water-buffered architecture
   - plant-side aeration dependence
   - whether solids are removed upstream before the raft or DWC component

If dedicated fields are not introduced immediately, the last item can remain explicit in scenario framing or notes first, but the architecture identifier itself should not remain implicit.

## What a Later Fair NFT Comparison Would Require

A fair later DWC-vs-NFT comparison should require all of the following:

1. The same basil cultivar or cultivar group.
2. The same fish-side nutrient source or loading regime.
3. The same greenhouse or climate context.
4. The same harvest regime:
   - same period length
   - same repeated-cut schedule or cut-count rule
5. The same core reported outputs:
   - `saleable_harvest_mass_kg`
   - `cull_or_unsaleable_mass_kg`
   - `harvest_event_count`
   - harvest timing or cut-cycle framing
   - `energy_kwh`
   - `water_use_l`
6. The same area or capacity basis:
   - `growing_area_m2`, or
   - one clearly mapped architecture capacity basis that can be normalized later
7. Architecture-relevant event signals:
   - flow interruption or outage events
   - clogging or intervention burden
   - maintenance-cleaning burden

Without those controls, a later DWC-vs-NFT comparison would still be informative, but not fair enough to move the current baseline beyond `directionally_supported`.

## What Should Remain Deferred for Now

- architecture-conditioned pricing or revenue-selection rules
- numeric architecture penalties or hard profitability multipliers
- full event-vocabulary redesign for every failure mode
- media-bed revisit for the current first slice
- WUE-driven reopening of the first-slice baseline before a comparable saleable-output path exists
- broader architecture-aware business interpretation beyond the thin first bridge

## Smallest Viable Runtime/Business Bridge Before Full Architecture-Aware Support

The smallest viable bridge is:

1. Keep using the basil `scenario_snapshot` family as the primary adapter source.
2. Keep only one architecture-aware bridge field active:
   - `crop_system_type`
3. Keep that field set explicitly to `architecture_dwc_raft` on the chosen basil baseline scenario.
4. Keep `product_id = basil`, `channel_id = channel_wholesale`, and the current working economics view unchanged.
5. Keep `saleable_harvest_mass_kg` as:
   - a reviewed manual bridge input, or
   - `null`
   until runtime harvest output exists.
6. Keep architecture-conditioned revenue rules inactive until runtime outputs can support them explicitly.

This gives the repo one real architecture-aware hook without forcing full architecture-aware support everywhere else first.

## Recommended Next Action

- Keep the explicit basil baseline scenario whose plant side is tagged as `architecture_dwc_raft`.
- Keep `crop_system_type = architecture_dwc_raft` stable as the current context bridge.
- Prioritize one harvest-ready output path next:
  - direct `saleable_harvest_mass_kg`, or
  - harvest-event output that can roll up to it cleanly
- Leave `growing_area_m2`, `water_use_l`, and paired NFT comparison work for the next layer after the first DWC or raft baseline path is real.
