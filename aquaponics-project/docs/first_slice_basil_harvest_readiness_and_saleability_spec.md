# First Slice Basil Harvest Readiness And Saleability Spec

Status: `draft`

## Purpose

- Prepare the first repo-side harvest-readiness and saleability spec for `basil bulk kg wholesale`.
- Translate the current deep research report into a reviewable repo contract without promoting anything into canon yet.
- Keep `saleable_harvest_mass_kg` unresolved unless observed runtime output or explicit human approval exists.

## Ingestion Status

- The source research report is accepted as evidence for drafting this non-canonical spec, with caveats.
- Acceptance here means "usable for spec drafting"; it does not promote the report, this spec, or any threshold into `data/knowledge/**` canon.
- Numeric harvest-size heuristics, aroma assessment, buyer tolerance assumptions, and saleable-mass interpretation all remain subject to later review before any possible canon promotion.

## Scope

- Slice remains fixed as `basil bulk kg wholesale`.
- This note is a repo-side draft spec only.
- It does not modify canonical biology/model/business files, runtime files, scripts, or derived runtime outputs.
- It distinguishes:
  - observed harvest outcomes
  - modeled harvest outcomes
  - manual-review acceptance criteria
  - operator assumptions

## Research Basis Used

Primary research input:

- `data/sources/research_reports/markdown/Defensible First-Pass External Reference Standard for Harvest-Readiness and Saleability of Fresh Basil Sold as Basil Bulk Kg Wholesale.md`

Strongest source families preserved from that report:

- current EU general marketing-standard baseline for fresh produce
- Basilico Genovese PDO specification as a basil-specific formal proxy
- UC Davis basil and herb postharvest guidance
- Rutgers fresh-market basil guidance
- 2023 `Frontiers` basil postharvest review
- FDA fresh culinary herb food-safety/handling guidance
- UVI aquaponic basil repeated-cut findings

## Why This Spec Is Not Yet Canon

- This document is a docs-only disposition of one deep research report, not a canonical knowledge-file edit.
- The source set supports qualitative harvest-readiness and saleability screens more strongly than universal numeric thresholds.
- Harvest height, leaf count, stem length, and buyer-tolerance thresholds remain context-dependent and are not promoted here.
- Aroma remains important to basil saleability, but only as a manual-review criterion.
- `saleable_harvest_mass_kg` remains unresolved because the report supports separating gross, observed saleable, observed rejected, and modeled saleable mass rather than aliasing them.
- Any later canon promotion would require an explicit scoped pass against `data/knowledge/**`.

## What The Research Supports Strongly

The report supports these points strongly enough to guide a first repo-side spec:

- fresh basil for `basil bulk kg wholesale` should be treated as young vegetative, non-flowering material rather than mature or flowering biomass
- flower-head absence is a strong harvest-readiness cue
- saleability depends on both:
  - general produce marketability
  - basil-specific freshness and fragility
- the strongest first-pass acceptance baseline is:
  - sound
  - clean
  - practically free from pests and pest damage
  - free from abnormal external moisture
  - free from foreign smell or taste
  - able to withstand handling and arrive satisfactorily
- basil-specific saleability depends heavily on:
  - freshness
  - turgidity
  - colour retention
  - low decay
  - low visible damage
  - retained characteristic aroma
- rejection triggers strongly include:
  - rot or visible decay
  - meaningful pest presence or pest damage
  - serious wilting
  - yellowing, browning, or blackening beyond minor transit loss
  - chilling injury
  - foreign matter
  - off-odour or off-taste
  - food-safety disqualification such as floodwater contact
- the report strongly supports keeping gross harvested mass, observed saleable mass, observed rejected mass, and modeled saleable mass as separate concepts

## Evidence Disposition Table

Source traceability uses durable source-family labels from the research report path above, not copied citation tokens. A `canonical candidate` disposition means possible later promotion target after explicit review; it is not canon in this spec.

| criterion | evidence basis | evidence strength | observation mode | proposed repo use | recommended disposition | notes / limits |
|---|---|---|---|---|---|---|
| non-flowering harvest stage | Basilico Genovese PDO proxy; Rutgers fresh-market basil guidance; report harvest-readiness synthesis | `strong` | `manual_review` | harvest-readiness criterion | `canonical candidate` possible later promotion only; not canon | Strong concept support; do not convert into one numeric threshold. |
| young vegetative material | Basilico Genovese PDO proxy; UC Davis basil/herb postharvest guidance; EU general marketing standard | `medium_to_strong` | `manual_review` | harvest-readiness criterion | `canonical candidate` possible later promotion only; not canon | Keep as concept only; avoid one universal height, leaf-count, or stem-length rule. |
| numeric size proxy such as height, leaf count, or stem length | Texas A&M and Utah/Arizona extension heuristics as summarized in the report | `weak_to_medium` | `manual_review` | grower context note only | `operator assumption` | Useful operationally, but too context-dependent for canon or hard runtime logic. |
| regrowth reserve after cutting | Rutgers fresh-market basil guidance; UVI aquaponic basil repeated-cut findings | `medium` | `manual_review` | repeated-cut harvest protocol | `provisional spec candidate` | Relevant for repeated-cut context, not a universal wholesale buyer-grade rule. |
| general marketability baseline: sound, clean, pest-free, transportable | EU general marketing standard; EU explanatory guidance summarized in the report | `strong` | `manual_review` | wholesale acceptance baseline | `canonical candidate` possible later promotion only; not canon | Strongest formal minimum-quality baseline in the source set. |
| freshness and turgidity | EU general marketing standard; UC Davis basil/herb postharvest guidance | `strong` | `manual_review` | wholesale acceptance baseline | `canonical candidate` possible later promotion only; not canon | Allows judgment; do not reduce to one automated proxy. |
| characteristic aroma acceptability | UC Davis basil/herb postharvest guidance; Basilico Genovese PDO proxy | `medium` | `manual_review_only` | wholesale acceptance criterion | `provisional spec candidate` | Important, but manual-review only and not currently suitable for deterministic runtime logic. |
| visible defect screen: yellowing, wilting, decay, insect damage, serious mechanical injury | UC Davis basil/herb postharvest guidance; Rutgers fresh-market basil guidance | `strong` | `manual_review` | exclusion or rejection reasons | `canonical candidate` possible later promotion only; not canon | Strong basis for qualitative rejection categories, not buyer-specific tolerance percentages. |
| slight post-dispatch loss of freshness/turgidity may still be acceptable | EU general marketing standard | `strong` | `manual_review` | acceptance nuance | `provisional spec candidate` | Supports avoiding zero-tolerance logic for minor transit softness. |
| chilling injury as rejection basis | UC Davis basil/herb postharvest guidance; Frontiers basil postharvest review | `strong` | `manual_review` | exclusion or rejection reasons | `canonical candidate` possible later promotion only; not canon | Strong concept support; do not canonize one numeric injury score threshold yet. |
| storage and handling band for basil | UC Davis basil/herb postharvest guidance; Frontiers basil postharvest review; Rutgers fresh-market basil guidance | `strong` | `assumption_only` | postharvest handling reference | `operator assumption` | Useful for handling and model context, not a wholesale grade by itself. |
| food-safety contamination exclusion | FDA fresh culinary herb guidance | `strong` | `manual_review` | exclusion reason | `canonical candidate` possible later promotion only; not canon | Cannot be inferred from crop appearance alone. |
| product-form distinction between bulk wholesale and RTU/RTE/live-root/potted basil | FDA fresh culinary herb guidance; Frontiers basil postharvest review; Basilico Genovese PDO proxy product-form context | `strong` | `config_or_manual_review` | scope guard | `canonical candidate` possible later promotion only; not canon | Prevents mixing product forms in later runtime or adapter logic. |
| aquaponic repeated-cut failure risk affecting marketable share | UVI aquaponic basil repeated-cut findings | `medium` | `modeled_or_manual_review` | future runtime/output design | `provisional spec candidate` | Strongly supports separating cut biomass from accepted saleable mass. |
| explicit separation of gross, observed saleable, observed rejected, and modeled saleable mass | EU general marketing standard; UC Davis basil/herb postharvest guidance; FDA fresh culinary herb guidance; UVI aquaponic basil repeated-cut findings; report repo-design conclusion | `strong` | `schema_or_output_contract` | future runtime/output naming | `provisional spec candidate` | Repo-design conclusion; do not silently alias these fields. |

## Recommended Classifications

### `canonical candidate`

These are possible later canon-promotion targets, but are **not canon and not promoted now**:

- non-flowering harvest stage
- young vegetative harvest-readiness concept
- general marketability baseline for soundness, cleanliness, pest/damage freedom, transportability, and no foreign smell/taste
- freshness and turgidity as saleability basics
- visible defect and exclusion categories for decay, serious damage, pest issues, wilting, yellowing, chilling injury, foreign matter, and food-safety contamination
- product-form distinction:
  - bulk wholesale cut basil
  - not RTU/RTE retail-packed basil
  - not live-root or potted basil

### `provisional spec candidate`

- regrowth-reserve logic for repeated-cut basil
- aroma acceptability as a manual-review criterion
- acceptance nuance for slight post-dispatch freshness loss
- aquaponic repeated-cut failure-risk concepts that can reduce marketable share
- explicit separation of:
  - `gross_harvest_mass_kg`
  - `observed_saleable_harvest_mass_kg`
  - `observed_rejected_harvest_mass_kg`
  - `modeled_saleable_harvest_mass_kg`

### `operator assumption`

- numeric size proxies such as height, leaf count, or stem length
- storage and handling bands used operationally or in later models
- harvest time-of-day preferences
- buyer-specific tolerance assumptions not present in the reviewed source set

### `open question`

- generic bulk-wholesale basil buyer tolerances for minor yellowing, stem breakage, stem-to-leaf ratio, or minor wilt
- numeric aroma grading that is reliable enough for repeatable QA or runtime use
- context-robust numeric harvest-stage thresholds across greenhouse, hydroponic, aquaponic, and field systems
- how to standardize repeated-cut saleability review in aquaponic basil without inventing numeric penalties

### `do not use yet`

- one hard numeric harvest-height threshold as repo canon
- one hard leaf-count threshold as repo canon
- one hard stem-length threshold as repo canon
- deterministic runtime saleability logic based on aroma
- direct inference of saleable mass from:
  - standing biomass
  - daily biomass gain
  - plant count
- visual-only auto-acceptance logic that ignores aroma, handling history, or contamination status
- buyer-grade tolerance thresholds or percentages not actually supported by the reviewed report

## First-Pass Repo Spec

### Harvest-Readiness Criteria

For the current repo-side first pass, basil is harvest-ready for `basil bulk kg wholesale` when all of the following are true:

- product context is fresh cut culinary basil for bulk wholesale
- plant material is young vegetative rather than mature or flowering
- flower heads are absent
- harvested material is leafy and non-woody enough for fresh culinary use

Additional repeated-cut readiness considerations:

- cutting practice should preserve acceptable regrowth where repeated harvest is intended
- repeated-cut readiness should remain a context flag, not a wholesale buyer-grade rule by itself

What should remain out of canon in this section:

- one universal cut height
- one universal leaf-count threshold
- one universal node-count rule for all contexts

### At-Harvest Selection Criteria

At-harvest selection should favor material that is:

- visibly fresh
- adequately turgid
- appropriately coloured for the cultivar/context
- free of visible decay
- free of serious insect damage
- free of serious mechanical damage
- free of flower heads

At-harvest selection should also preserve:

- harvest practices that avoid rough handling
- repeated-cut practices that do not strip regrowth reserves indiscriminately

Observation mode:

- `manual_review`

### Saleability / Wholesale Acceptance Criteria

For this first-pass repo spec, a lot should only be treated as saleable for `basil bulk kg wholesale` when it clears both:

1. the general marketability screen
2. the basil-specific culinary-herb screen

General marketability screen:

- sound
- clean
- practically free from pests
- practically free from pest damage affecting usability
- free from abnormal external moisture
- free from foreign smell or taste
- able to withstand transport and arrive in satisfactory condition

Basil-specific culinary-herb screen:

- retains fresh appearance
- retains acceptable turgidity
- does not show important yellowing, blackening, browning, or decay
- does not show important visible mechanical injury
- retains characteristic culinary aroma

Important nuance:

- slight transit-related loss of freshness or turgidity may still be acceptable
- that nuance should remain a human-review judgment, not a hard automated pass/fail rule

### Rejection / Exclusion Criteria

For the current first-pass repo spec, rejection or exclusion reasons should include:

- rot
- visible decay
- serious wilting
- serious yellowing
- serious browning or blackening
- chilling injury that materially harms edibility or acceptance
- serious pest presence
- serious pest damage
- serious mechanical damage
- foreign matter
- off-odour or off-taste
- food-safety contamination
- other manual reject reason

Recommended review mode:

- `manual_review`

These reasons are suitable for later `quality_exclusion_reasons` vocabulary work, but not for canonical schema changes in this pass.

### Repeated-Cut Basil Considerations

Repeated-cut basil should be handled explicitly because the report supports both:

- repeated-cut regrowth potential
- repeated-cut saleability risk

Repo-side implications:

- repeated-cut harvest readiness is not identical to one-time harvest readiness
- biomass available to cut is not the same thing as accepted saleable wholesale mass
- repeated-cut aquaponic stressors such as nutrient deficiency or disease pressure can reduce saleable share without changing the basic product form

This supports later separation between:

- available harvested mass
- observed accepted saleable mass
- observed rejected mass
- modeled saleable mass

## Naming Distinction For Harvest Mass Fields

The repo should preserve the following naming distinction:

- `gross_harvest_mass_kg`
  - all harvested basil mass entering post-cut handling before saleability exclusion
- `observed_saleable_harvest_mass_kg`
  - mass actually accepted as saleable after human review, QA, or receiving acceptance
- `observed_rejected_harvest_mass_kg`
  - mass explicitly rejected or downgraded out of the target sale form
- `modeled_saleable_harvest_mass_kg`
  - estimated saleable mass derived from a model, not from direct observed acceptance
- current unresolved `saleable_harvest_mass_kg`
  - must remain unresolved unless it is explicitly backed by:
    - observed runtime output, or
    - explicit human-reviewed manual input

Important rule:

- do not silently alias `saleable_harvest_mass_kg` to gross mass
- do not silently alias it to modeled saleable mass
- do not silently alias it to standing biomass

## What This Implies For Future Runtime Output Design

The research report implies that future runtime output should separate epistemic states clearly.

Smallest safe later output pattern:

- one field for gross harvested mass:
  - `gross_harvest_mass_kg`
- one field for observed accepted saleable mass when direct review exists:
  - `observed_saleable_harvest_mass_kg`
- one field for observed rejected mass when direct review exists:
  - `observed_rejected_harvest_mass_kg`
- one field for modeled saleable mass when a quality model is used:
  - `modeled_saleable_harvest_mass_kg`
- one explicit basis field for how acceptance was determined:
  - example: `saleability_basis`
- one explicit readiness basis field for why the crop was cut:
  - example: `harvest_readiness_basis`
- one explicit rejection-reason field or list:
  - example: `quality_exclusion_reasons`

Design implication:

- quality state and commercial acceptance state should be separable
- manual review, modeled output, and observed acceptance should not collapse into one ambiguous `saleable_harvest_mass_kg`

## What Should Not Become Runtime Logic Yet

- do not add one hard numeric height threshold
- do not add one hard leaf-count threshold
- do not add deterministic aroma scoring logic
- do not infer saleability from standing biomass, daily biomass gain, or plant count
- do not treat non-flowering status alone as proof of saleability
- do not auto-accept basil based only on visual greenness
- do not convert storage-temperature guidance into a direct buyer-acceptance rule
- do not encode buyer-specific minor-defect tolerances that the report does not actually support
- do not treat reviewed manual override values as runtime-native observations

## Open Questions Before Canon Promotion

- What buyer-grade tolerance language, if any, can support bulk-wholesale basil defect tolerances beyond the current minimum-quality baseline?
- Is there a high-trust reviewed buyer or receiver spec for:
  - minor yellowing
  - minor wilt
  - stem breakage
  - leaf-size heterogeneity
  - stem-to-leaf ratio
- Can aroma acceptability be standardized in a practical QA method without pretending it is runtime-observable?
- Which repeated-cut aquaponic stress signals are stable enough to inform later modeled saleability adjustment without inventing unsupported penalties?
- How should the repo represent slight transit-related freshness loss without confusing it with rejection?

## Recommended Next Action

- Keep this note as a non-canonical first-pass repo spec.
- Use it to guide later review of harvest-output field naming and saleability-review vocabulary.
- Keep `saleable_harvest_mass_kg` unresolved unless a later pass provides:
  - observed runtime harvest output, or
  - explicit human-reviewed manual approval for a specific run
- Do not promote numeric harvest-size thresholds, aroma thresholds, or buyer-specific defect tolerances into canon until stronger reviewed evidence exists.
