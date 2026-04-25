# First Slice Method Comparison

Status: `draft`

## Purpose

- Lock the current first working economics view as the comparison frame for grow-method review.
- Compare `architecture_nft`, `architecture_dwc_raft`, and `architecture_media_bed` only in the context of the current first slice.
- Make clear what the repo can already support versus what still needs targeted deep research.

## Scope

- Slice is fixed as `basil bulk kg wholesale`.
- Netherlands is the current first working benchmark only; it is a comparison frame, not canon.
- This note does not reopen the current working economics values.
- This note does not modify `data/knowledge/**`, runtime files, simulation files, or schemas.
- Canonical repo files and repo docs are the primary support; the architecture-specific research pack is supporting evidence for business interpretation.

## Locked First Working Economics View

The current comparison frame is:

- `docs/first_vertical_slice_choice.md`
  - first slice remains `basil bulk kg wholesale`
- `docs/first_slice_working_input_pack.md`
  - Netherlands remains the current first working benchmark only
  - working price band is `7.0 / 8.0 / 9.0 EUR per saleable kg`
  - working saleability band is `0.85 / 0.90 / 0.95`
- `docs/first_slice_cost_build_up_review.md`
  - `variable_cost_per_saleable_kg = 6.8 / 5.8 / 5.0` remains a constructed working assumption
  - `fixed_batch_cost = 500.0` remains a weak working assumption
  - `variable_cost_per_saleable_kg` currently moves break-even more than `fixed_batch_cost`
- `docs/first_slice_assumption_review.md`
  - `saleable_harvest_mass_kg` remains missing and must not be invented from standing biomass or runtime proxies

Implication for this comparison:

- the first-slice frame is currently sensitive to hidden labor, maintenance, sanitation, and saleability losses
- a method is better positioned for the first slice if it is more likely to preserve clean, repeatable basil output without adding fragile or labor-heavy burdens that the current working economics view does not price precisely yet

## Current First Slice

- `basil bulk kg wholesale`

## Methods Compared

- `architecture_nft`
- `architecture_dwc_raft`
- `architecture_media_bed`

## Comparison Criteria

| Criterion | Why it matters for this slice |
|---|---|
| basil yield potential | First-slice output is sold by bulk harvested kg, so weak yield fit can erase already-thin contribution margin. |
| repeated-harvest suitability | Basil often uses repeated cutting, so harvest-cycle stress matters to long-run saleable output quality. |
| saleability / quality risk | The current economics view depends on saleable kilograms, not standing biomass. |
| labor burden | The current cost build-up review says variable cost is still the most sensitive break-even driver. |
| maintenance burden | Extra cleaning, unclogging, or reset work can quietly raise cost even before rates are canonized. |
| outage / flow fragility | Acute crop-loss risk matters when the slice is still margin-sensitive and harvest mass is missing upstream. |
| water-quality fragility | The repo already treats architecture-specific solids, buffering, and nitrification differences as business-relevant. |
| cleanliness / post-harvest handling fit | Bulk basil wholesale still benefits from clean, repeatable harvest handling even without bunch logic. |
| fit with current first-slice economics threshold | The best current method is the one least likely to demand hidden cost or shrink assumptions just to make the first reviewable slice work. |

## Method-by-Method Review

### `architecture_dwc_raft`

Summary:

- commercial archetype strength: `well_supported`
- first-slice suitability: `favorable`
- evidence confidence: `directionally_supported`

What repo evidence supports it:

- `data/knowledge/models/plant_system_models.json`
  - raft is the high-buffer baseline
  - short-term pump fragility is lower than NFT because of water buffering
  - nitrification support is high if solids are removed upstream
- `data/knowledge/business/yield_to_revenue_rules.json`
  - DWC or raft is the advisory architecture context most associated with cleaner leafy or herb handling
- `data/knowledge/business/labor_models.json`
  - raft harvest and changeover burden is explicitly kept separate because it is expected to be lower than media beds for quick crops
  - inspection burden is present, but not framed as high-frequency unclogging in the way NFT is
- `data/knowledge/business/cost_models.json`
  - raft cleaning and foam replacement are recognized as real architecture-specific costs, but not the dominant clogging/unclogging profile used for NFT
- `data/sources/research_reports/markdown/Architecture-specific business drivers for media bed, DWC, and NFT in aquaponics.md`
  - DWC or raft is described as the clearest commercial aquaponics archetype for leafy greens and herbs
  - it is less outage-sensitive than NFT and better aligned with fast harvest and standardized plant handling
- `data/knowledge/species/plants/basil.json`
  - basil has repeated-cut stress and disease-risk notes, so buffered and more stable plant-side conditions are favorable for protecting saleable output

What is still uncertain:

- basil-specific yield superiority over NFT is not strongly established in canonical repo files
- architecture-specific spoilage or shrink percentages for basil wholesale are not available
- the current runtime path now carries `crop_system_type` as context, but it still does not emit `saleable_harvest_mass_kg`, so the current runtime-to-business bridge cannot yet prove a raft-specific realized output path

Current signal for the first slice:

- `favorable`
- DWC or raft has the strongest repo support as the commercial herb or leafy archetype that best balances standardized handling, lower short-term fragility, and manageable labor burden under the locked first-slice economics frame

### `architecture_nft`

Summary:

- commercial archetype strength: `directionally_supported`
- first-slice suitability: `mixed`
- evidence confidence: `directionally_supported`

What repo evidence supports it:

- `data/knowledge/models/plant_system_models.json`
  - NFT is explicitly modeled as low-buffer and very high fragility under pump disruption
  - solids-carryover penalties escalate through channel blockage and root-loss risk
  - nitrification support is low and separate biofiltration is often required
- `data/knowledge/business/yield_to_revenue_rules.json`
  - NFT remains an advisory candidate for standardized leafy or herb handling
- `data/knowledge/business/labor_models.json`
  - NFT harvest labor is kept separate because sanitation and reset burden can matter
  - NFT inspection and intervention notes explicitly point to unclogging and flow-check burden
- `data/knowledge/business/cost_models.json`
  - NFT-specific sanitation and unclogging or filter-service cost buckets already exist as architecture-specific placeholders
- `data/sources/research_reports/markdown/Architecture-specific business drivers for media bed, DWC, and NFT in aquaponics.md`
  - NFT is space-efficient and can suit lighter-rooted crops and some herbs
  - channels can be easier to clean than foam rafts
  - the same pack also says NFT is the most failure-sensitive architecture and depends on cleaner water and uninterrupted flow

What is still uncertain:

- the repo does not support a strong basil-specific commercial yield advantage for NFT over DWC or raft
- architecture-specific saleability loss from clogging, interruption, or uneven performance is not quantified
- the economic value of NFT space efficiency is not captured cleanly in the current first-slice frame because `growing_area_m2` and architecture-specific CAPEX or labor rates remain unresolved

Current signal for the first slice:

- `mixed`
- NFT has plausible herb-handling and sanitation advantages, but the repo support is stronger for its fragility, water-cleanliness dependence, and intervention burden than for a clear first-slice basil wholesale advantage

### `architecture_media_bed`

Summary:

- commercial archetype strength: `directionally_supported`
- first-slice suitability: `unfavorable`
- evidence confidence: `well_supported`

What repo evidence supports it:

- `data/knowledge/models/plant_system_models.json`
  - media beds are flexible and can integrate solids and nitrification support
  - the same file also models clogging, anaerobic-zone escalation, and high fragility if beds are drained
  - buffering is lower than raft
- `data/knowledge/business/yield_to_revenue_rules.json`
  - media-bed output-form context is already advisory toward mixed-crop or fruiting interpretation rather than a clean standardized leafy or herb path
- `data/knowledge/business/labor_models.json`
  - media beds carry separate harvest/changeover and inspection/intervention placeholders because extra root clean-out, media handling, and clogging checks are expected
- `data/knowledge/business/cost_models.json`
  - media-bed changeover cleaning and gravel or media washing already exist as separate architecture cost buckets
- `data/sources/research_reports/markdown/Architecture-specific business drivers for media bed, DWC, and NFT in aquaponics.md`
  - media beds are described as operationally flexible but better aligned with mixed-crop, smaller-scale, or direct-market models than with highly standardized high-throughput leafy lines
  - the same pack says heavier cleaning, root or solids clogging risk, and tedious crop turns are meaningful business penalties
- `data/knowledge/species/plants/basil.json`
  - basil repeated-cut stress and disease pressure make it undesirable to add extra avoidable handling or root-zone instability without a strong compensating business case

What is still uncertain:

- the repo does not prove media beds cannot produce basil profitably
- one crop-specific context split in the architecture research pack suggests gravel can perform well on some basil growth measures, but not as a commercial basil wholesale economics proof
- architecture-specific saleability loss for media-grown basil is not quantified

Current signal for the first slice:

- `unfavorable`
- media beds remain commercially meaningful as a different archetype, but the repo support points away from them for a first reviewable `basil bulk kg wholesale` slice because the current economics frame is sensitive to labor, cleaning, and standardization burdens

## Current Best-Supported Method for the First Slice

- `architecture_dwc_raft`

Judgment:

- first-slice suitability: `favorable`
- evidence confidence: `directionally_supported`

Why this is the current best-supported choice:

- It is the strongest repo-supported commercial archetype for leafy greens and herbs in aquaponics.
- It aligns better than media beds with standardized, cleaner plant handling.
- It avoids the strongest outage and unclogging fragility associated with NFT.
- Under the locked first working economics view, that combination is more defensible than either media-bed flexibility or NFT space efficiency.

Important limit:

- This is not yet a canonical winner for basil in the abstract.
- It is the current best-supported first-slice comparison baseline under the repo's present economics frame and evidence quality.

## What the Repo Can Already Say Confidently

- `well_supported`: architecture should remain a first-class business distinction rather than a flattened plant-subsystem label.
- `well_supported`: DWC or raft is the strongest commercial aquaponics archetype in the repo for leafy or herb programs.
- `well_supported`: NFT carries the highest acute flow-interruption fragility and cleaner-water dependence.
- `well_supported`: media beds carry the heaviest changeover and cleaning burden for short-cycle or standardized crop programs.
- `directionally_supported`: for the current `basil bulk kg wholesale` slice, DWC or raft is better positioned than NFT or media bed.
- `well_supported`: the current runtime path now provides `crop_system_type` as context, but still does not provide `saleable_harvest_mass_kg`, so the method comparison is still partly an evidence-layer judgment rather than a realized business-output test.

## What Remains Too Uncertain

- `too_uncertain`: a definitive basil-specific fresh-mass or saleable-mass advantage between DWC or raft and NFT
- `too_uncertain`: architecture-specific basil shrink, quality-loss, or saleability percentages
- `too_uncertain`: architecture-specific labor-hour and maintenance-rate benchmarks credible enough for canon promotion
- `too_uncertain`: whether the current basil runtime scenario should later support architecture-conditioned business interpretation beyond the current baseline context, because `crop_system_type` is still only a context field and not a pricing or revenue driver

## Targeted Deep-Research Questions Only If Needed

1. For repeated-cut aquaponic basil sold by bulk kg, is there a reviewed commercial or near-commercial comparison of saleable harvested mass across DWC or raft versus NFT?
2. For basil specifically, how much of the architecture difference shows up in post-harvest cleanliness, shrink, or discard rather than raw standing biomass?
3. Which architecture-specific operating burden matters more in practice for basil wholesale lines: raft cleaning and foam replacement, or NFT unclogging and flow-check intervention?
4. Does media-bed basil have any reviewed commercial wholesale path that overcomes the extra changeover and cleanliness burden strongly enough to compete with DWC or raft for a first proof slice?

## Recommended Next Action

- Keep the current first-slice economics view locked as the comparison frame.
- Use `architecture_dwc_raft` as the current best-supported comparison baseline for the first slice.
- Do not promote that preference into canon yet.
- Do not widen the first slice into architecture-conditioned revenue rules yet, because `crop_system_type` remains context only and `saleable_harvest_mass_kg` is still missing upstream.
- If the project needs a narrower method decision before canon promotion, run one targeted DWC-versus-NFT basil research pass focused only on repeated-harvest saleable kg, labor burden, and saleability or shrink implications.
