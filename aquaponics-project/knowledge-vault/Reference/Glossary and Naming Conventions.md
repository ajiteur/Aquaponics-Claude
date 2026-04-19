# Glossary and Naming Conventions

- Status: `draft`
- Scope: Human-facing terminology guide for vault notes, reviews, plans, and repo discussions.
- Canonical sources still win: `data/knowledge/**` and normative docs such as `docs/business_layer_contract.md` and `docs/decision_rule_research_simulation_business_audit.md`.
- Per-entry `grounding` labels describe how well a definition is grounded in the current project.
- Those labels do not make this glossary note itself canonical.

## Purpose

- Keep terminology consistent across research, simulation, business, and repo-audit work.
- Reduce avoidable naming drift between vault notes and canonical repo files.
- Make uncertainty explicit when a term exists in the repo but is not yet fully normalized.

## How to Use This Glossary

- Prefer the term and spelling used here when writing notes, reviews, or plans.
- When a machine field exists, quote the exact field name in backticks.
- If this note conflicts with canonical JSON or a normative doc, the canonical source wins.
- Grounding labels used here:
  - `grounding: repo_grounded` = definition is grounded clearly in current repo docs, canonical files, or repeated repo usage.
  - `grounding: provisional` = term is in use, but scope or normalization is still evolving.
  - `grounding: todo` = useful requested term, but not yet cleanly defined in the current repo state.

## Core Project Terms

### Canonical

- grounding: `repo_grounded`
- Definition: Source-of-truth material the project intends to preserve and review deliberately.
- Use in this project: Usually `data/knowledge/**`; some docs are also normative for boundaries and contracts.
- Do not confuse with: `knowledge-vault/**` notes or `data/simulation/**` outputs.
- Example or note: `data/knowledge/business/**` is canonical scaffolding even when records are still draft.

### Derived

- grounding: `repo_grounded`
- Definition: Output produced from canonical inputs or runtime processes rather than treated as source truth.
- Use in this project: `data/simulation/**` is derived runtime output; some generated vault summaries are also derived.
- Do not confuse with: `canonical`.
- Example or note: Species files under `data/simulation/**` remain derived until an explicit migration says otherwise.

### Deferred

- grounding: `repo_grounded`
- Definition: Intentionally present in schema, but not active yet because inputs, evidence, or basis choices are still unresolved.
- Use in this project: Common in business-layer records and rules that use `enabled_by_default: false` and `activation_status: "optional_future"`.
- Do not confuse with: Missing, forgotten, or rejected work.
- Example or note: Architecture-aware output-form review in the business layer is currently deferred.

### Provisional

- grounding: `repo_grounded`
- Definition: Reviewable and useful, but not stable enough to treat as final.
- Use in this project: Docs use this for items that are directionally supported but still need later normalization or promotion review.
- Do not confuse with: `accepted` or `todo`.
- Example or note: A rule can be structurally useful but still provisional if the evidence is context-sensitive.

### Accepted

- grounding: `repo_grounded`
- Definition: Reviewed strongly enough for current scoped canon.
- Use in this project: Seen most clearly in accepted atomic truths and warnings.
- Do not confuse with: `draft` or `provisional`.
- Example or note: Water-chemistry atomic truths marked `accepted` are safe anchors for terminology.

### Schema-Choice TODO

- grounding: `repo_grounded`
- Definition: Explicit marker that a field exists, but the canonical basis or representation is not settled yet.
- Use in this project: Common in business JSON as `schema_choice_status: "todo"` with a matching note.
- Do not confuse with: A missing field or a runtime bug.
- Example or note: Choosing whether NFT CAPEX scales by `growing_area_m2` or `channel_length_m`.

## Research / Simulation / Business / Repo-Audit Terms

### Research / Evidence Review

- grounding: `repo_grounded`
- Definition: Repo work that decides what structure, distinction, or rule should exist based on sources and canon discipline.
- Use in this project: Best for architecture differences, units, basis choices, context splits, and canon decisions.
- Do not confuse with: `simulation` or `repo audit`.
- Example or note: Deciding whether architecture must be first-class in CAPEX, labor, yield, and risk models.

### Simulation

- grounding: `repo_grounded`
- Definition: Dynamic modeling of what happens inside a chosen scenario over time.
- Use in this project: Event counts, yield continuity, downtime severity, and mitigation value belong here.
- Do not confuse with: `business calculation`.
- Example or note: Estimating how often NFT flow interruption causes lost output in one scenario.

### Business Calculation

- grounding: `repo_grounded`
- Definition: Economic interpretation of scenario outputs using business-layer assumptions.
- Use in this project: Revenue translation, cost allocation, contribution margin, payback, and risk-penalty framing.
- Do not confuse with: Live market truth or biology-only warnings.
- Example or note: Translating saleable yield and labor into a scenario margin.

### Repo Audit

- grounding: `repo_grounded`
- Definition: Compatibility check of what current files, fields, tests, and consumers can safely support right now.
- Use in this project: Read-only safety review for schema changes, deletions, aliases, and test impact.
- Do not confuse with: Biological truth or business truth.
- Example or note: Checking whether a field can safely change shape without breaking current readers.

### Context Split

- grounding: `repo_grounded`
- Definition: Keep two claims separate because their context differs enough that flattening them would mislead.
- Use in this project: Important for architecture, species, scale, temperature regime, channel, and system-type differences.
- Do not confuse with: `contradiction`.
- Example or note: A small-scale NFT lettuce result can stay a context split instead of becoming a universal profitability rule.

### Contradiction

- grounding: `repo_grounded`
- Definition: Unresolved conflict between overlapping claims after context has been normalized as far as possible.
- Use in this project: Log contradictions instead of silently overwriting canon.
- Do not confuse with: `context split` or ordinary uncertainty.
- Example or note: `knowledge-vault/Learnings/contradictions_log.md` is the current vault note for unresolved issues and open questions.

## Business-Layer Terms

### architecture_variant_id

- grounding: `provisional`
- Definition: Machine-readable ID for a named architecture variant, such as `architecture_media_bed`.
- Use in this project: Keeps architecture-specific CAPEX, labor, output-form review, and risk taxonomy separate.
- Do not confuse with: Component IDs such as `media_bed` or upstream field names such as `crop_system_type`.
- Example or note: Current draft variants are `architecture_media_bed`, `architecture_dwc_raft`, and `architecture_nft`.

### crop_system_type

- grounding: `repo_grounded`
- Definition: Normative upstream field name for the crop-side growing system used in business mapping.
- Use in this project: Required crop-level field in `docs/business_layer_contract.md`.
- Do not confuse with: `architecture_variant_id` or a component note title.
- Example or note: A later mapping layer may translate runtime grow-system labels into this field.

### Output Form

- grounding: `provisional`
- Definition: Business-layer description of the saleable product representation used for revenue translation.
- Use in this project: Deferred yield-to-revenue rules use output-form language to keep mass, bunch, head, or live-root handling separate.
- Do not confuse with: Crop identity, packaging detail, or final channel pricing.
- See also: [[#Channel-Fit|channel-fit]], [[#Business Calculation|business calculation]].

### Live-Root

- grounding: `provisional`
- Definition: Output-form concept where a plant is sold with living roots still attached.
- Use in this project: Useful for deferred business interpretation of certain leafy-crop handling paths without making channel logic canonical.
- Do not confuse with: `whole head` or mass-only harvest handling.
- See also: [[#Output Form|output form]], [[#Channel-Fit|channel-fit]].

### Whole Head

- grounding: `provisional`
- Definition: Saleable whole-head plant form handled as an intact head rather than only as bulk mass.
- Use in this project: Useful for lettuce-style revenue interpretation where head-based handling matters.
- Do not confuse with: Mass-only output handling or `live-root`.
- See also: [[#Output Form|output form]], [[#Lettuce|lettuce]].

### Herb Clippings

- grounding: `provisional`
- Definition: Harvested clipped herb biomass sold without an intact root system.
- Use in this project: Useful for herb-side output-form review where repeated clipping differs from whole-plant sale assumptions.
- Do not confuse with: `live-root` plants or whole-head handling.
- See also: [[#Output Form|output form]], [[#Basil|basil]].

### Channel-Fit

- grounding: `provisional`
- Definition: Shorthand for how well a crop and output form fit a target sales channel's handling and merchandising needs.
- Use in this project: Mentioned in deferred output-form review and activation notes, but not yet normalized as a canonical rule.
- Do not confuse with: NFT channel geometry or hydraulic flow path.
- See also: [[#Output Form|output form]], [[#crop_system_type|crop_system_type]].

### allocation_scope

- grounding: `repo_grounded`
- Definition: Cost-model field that says where a cost is applied in business translation.
- Use in this project: Current values include `direct_to_crop_batch` and `shared_system_cost`.
- Do not confuse with: `cost_category`, `driver_key`, or CAPEX grouping.
- See also: [[#Shared System Cost|shared system cost]], [[#Shared System CAPEX|Shared System CAPEX]].

### Shared System Cost

- grounding: `repo_grounded`
- Definition: Operating cost allocated at whole-system level rather than to one crop batch.
- Use in this project: Appears as `allocation_scope: "shared_system_cost"` in business cost models.
- Do not confuse with: [[#Shared System CAPEX|shared system CAPEX]], which is capital rather than operating cost.
- See also: [[#allocation_scope|allocation_scope]].

### Contribution Margin

- grounding: `provisional`
- Definition: Revenue minus direct or variable business costs for the scoped product or scenario.
- Use in this project: Useful target metric once yield, labor, and operating-cost rules are translated into economics.
- Do not confuse with: Gross revenue, net profit, or payback.
- See also: [[#Business Calculation|business calculation]], [[#Payback|payback]].

### Payback

- grounding: `repo_grounded`
- Definition: Recovery of included CAPEX from later cash contribution over time.
- Use in this project: CAPEX records already use `include_in_payback_default`; the exact payback method is still scenario-dependent.
- Do not confuse with: Contribution margin, ROI, or IRR.
- See also: [[#Contribution Margin|contribution margin]], [[#Shared System CAPEX|Shared System CAPEX]].

### Grow-Unit Basis

- grounding: `provisional`
- Definition: Glossary shorthand for a sizing basis tied to grow-side physical units.
- Use in this project: Useful when comparing architecture-specific bases such as `growing_area_m2`, `media_volume_m3`, `water_surface_area_m2`, `channel_length_m`, or `planting_site_count`.
- Do not confuse with: `supporting-system basis`.
- Example or note: NFT CAPEX by `channel_length_m` is a grow-unit basis choice.

### Supporting-System Basis

- grounding: `provisional`
- Definition: Glossary shorthand for a sizing basis tied to shared support infrastructure rather than one grow unit.
- Use in this project: Useful for pumps, solids removal, biofiltration, backup power, and fish-side infrastructure.
- Do not confuse with: `grow-unit basis`.
- Example or note: `system`, `design_flow_m3_per_hour`, and `design_feed_load_kg_per_day` are supporting-system basis candidates.

### Shared System CAPEX

- grounding: `provisional`
- Definition: Human shorthand for CAPEX that belongs to the whole system rather than one crop line or one architecture bundle.
- Use in this project: Applies to items such as greenhouse structure, water treatment, fish system, controls, and hydraulics.
- Do not confuse with: [[#Shared System Cost|shared system cost]], which is an operating-cost concept.
- Example or note: `capex_greenhouse_structure` is shared system CAPEX; `capex_nft_bundle` is architecture-bundle CAPEX.

## Water Chemistry and Biology Terms

### TAN

- grounding: `repo_grounded`
- Definition: Total Ammonia Nitrogen, the combined amount of NH3 and NH4+ in water.
- Use in this project: Business contract expects `observed_tan_mg_l`; accepted atomic truths note that common ammonia test kits measure TAN.
- Do not confuse with: `unionized ammonia / NH3`, which is the more toxic fraction.
- Deeper explainer: [[Reference/Explainers/TAN|TAN explainer]].
- See also: [[#Unionized Ammonia / NH3|NH3]], [[#NH4+|NH4+]], [[#pH|pH]], [[#Nitrification|Nitrification]].

### NH4+

- grounding: `repo_grounded`
- Definition: Ionized ammonium form within total ammonia in water.
- Use in this project: Appears in atomic-truth language contrasting NH4+ with the more toxic NH3 fraction.
- Do not confuse with: [[#Unionized Ammonia / NH3|NH3]] or [[#TAN|TAN]] as a combined measure.
- See also: [[#TAN|TAN]], [[#Unionized Ammonia / NH3|NH3]], [[#pH|pH]].

### Unionized Ammonia / NH3

- grounding: `repo_grounded`
- Definition: The un-ionized toxic ammonia form present within TAN; toxicity rises with pH and temperature.
- Use in this project: Business contract expects `observed_unionized_nh3_mg_l`; tilapia canon includes NH3 warning and critical values.
- Do not confuse with: TAN as a whole or NH4+.
- Deeper explainer: [[Reference/Explainers/Unionized Ammonia NH3|Unionized Ammonia / NH3 explainer]].
- See also: [[#TAN|TAN]], [[#NH4+|NH4+]], [[#pH|pH]], [[#Tilapia|Tilapia]], [[#Nitrification|Nitrification]].

### Dissolved Oxygen / DO

- grounding: `repo_grounded`
- Definition: Oxygen dissolved in water and available to fish, plant roots, and nitrifying microbes.
- Use in this project: Appears in species thresholds, DWC root-zone guidance, and sensor notes.
- Do not confuse with: Aeration equipment; aeration is one way to maintain DO.
- See also: [[#Nitrification|Nitrification]], [[#DWC / Raft|DWC / Raft]], [[#Biofilter|biofilter]], [[#Tilapia|Tilapia]].

### Temperature

- grounding: `repo_grounded`
- Definition: Core water-quality and biological-control variable affecting fish, microbes, and plant response.
- Use in this project: Affects fish tolerance, plant performance, nitrification, and NH3 toxicity across species notes, chemistry reasoning, and simulation inputs.
- Do not confuse with: Ambient air temperature only or a single species-specific optimum.
- See also: [[#pH|pH]], [[#TAN|TAN]], [[#Unionized Ammonia / NH3|NH3]], [[#Nitrification|Nitrification]], [[#Tilapia|Tilapia]].

### pH

- grounding: `repo_grounded`
- Definition: Measure of acidity or alkalinity in water.
- Use in this project: Cross-domain control variable for fish tolerance, plant nutrient availability, and ammonia toxicity.
- Do not confuse with: Nutrient concentration, alkalinity, or EC.
- Deeper explainer: [[Reference/Explainers/pH|pH explainer]].
- See also: [[#TAN|TAN]], [[#Unionized Ammonia / NH3|NH3]], [[#NH4+|NH4+]], [[#Alkalinity|alkalinity]], [[#Nitrification|Nitrification]].

### Alkalinity

- grounding: `provisional`
- Definition: Water's buffering capacity against acid addition rather than the same thing as pH.
- Use in this project: Matters for pH stability as nitrification consumes buffering capacity and appears in stoichiometry-oriented treatment notes.
- Do not confuse with: `pH`; alkalinity is buffering capacity, not the current acidity reading.
- See also: [[#pH|pH]], [[#Nitrification|Nitrification]].

### CO2

- grounding: `provisional`
- Definition: Dissolved carbon dioxide relevant to fish-water quality and gas balance.
- Use in this project: Useful when reasoning about aeration, degassing, and overall water-gas balance, even though it is not yet normalized as a main repo field.
- Do not confuse with: Dissolved oxygen or alkalinity.
- See also: [[#Dissolved Oxygen / DO|DO]], [[#pH|pH]], [[#Temperature|temperature]].

### EC

- grounding: `todo`
- Definition: Electrical conductivity, often used as a shorthand proxy for dissolved ion concentration.
- Use in this project: Useful term to recognize, but not yet normalized as a core field or control target in the current repo state.
- Do not confuse with: Nutrient-specific concentration or pH.
- See also: [[#pH|pH]], [[#nitrate-N|nitrate-N]].

### nitrate-N

- grounding: `provisional`
- Definition: Nitrate expressed as nitrogen only, not as the full nitrate ion mass.
- Use in this project: Appears in basil aquaponics anchors, while other repo fields use plain nitrate wording such as `observed_nitrate_mg_l`.
- Do not confuse with: Generic `nitrate` wording; unit interpretation can change materially.
- Example or note: Preserve exact field names. Do not hand-convert `nitrate-N` and `nitrate` in prose without saying so.

### Nitrite

- grounding: `repo_grounded`
- Definition: Intermediate nitrogen form in nitrification that sits between ammonia and nitrate in the conversion chain.
- Use in this project: Shows up in water-loop and biofilter reasoning as a monitored conversion state rather than a final plant-available form.
- Do not confuse with: `nitrate-N` or [[#TAN|TAN]].
- See also: [[#TAN|TAN]], [[#NH4+|NH4+]], [[#Nitrification|Nitrification]], [[#Biofilter|Biofilter]].

### Nitrification

- grounding: `repo_grounded`
- Definition: Microbial conversion of ammonia toward nitrate, with hydrogen ions released so pH tends to fall.
- Use in this project: Core water-treatment concept for biofilters, media beds, fish-water chemistry, and oxygen demand.
- Do not confuse with: Solids removal; related but different process.
- Deeper explainer: [[Reference/Explainers/Nitrification|Nitrification explainer]].
- See also: [[#TAN|TAN]], [[#NH4+|NH4+]], [[#Unionized Ammonia / NH3|NH3]], [[#Dissolved Oxygen / DO|DO]], [[#Biofilter|biofilter]], [[#pH|pH]].

## Architecture Terms

### Biofilter

- grounding: `repo_grounded`
- Definition: Water-treatment component that provides surface area for nitrifying microbes.
- Use in this project: Exists as a component note and shows up in architecture/business discussion through `separate_biofilter_required`.
- Do not confuse with: A [[#Media Bed|media bed]] that may add some treatment surface, or a [[#Solids Filter|solids filter]] that removes particles.
- See also: [[#Nitrification|Nitrification]], [[#Dissolved Oxygen / DO|DO]], [[#Media Bed|Media Bed]].

### Clarifier

- grounding: `provisional`
- Definition: Solids-separation or settling stage used before downstream treatment or grow stages.
- Use in this project: Useful treatment term where upstream solids removal matters before biofilters, DWC, NFT, or other cleaner-water-dependent stages.
- Do not confuse with: [[#Biofilter|biofilter]], which is for biological conversion rather than primary settling.
- See also: [[#Solids Filter|Solids Filter]], [[#Biofilter|Biofilter]].

### HRT

- grounding: `provisional`
- Definition: Hydraulic retention time, meaning how long water remains in a treatment or grow volume.
- Use in this project: Useful shorthand for practical treatment sizing and flow interpretation even though it is not yet a normalized core business field.
- Do not confuse with: Pump runtime or turnover count by itself.
- See also: [[#Clarifier|clarifier]], [[#Biofilter|biofilter]].

### Solids Filter

- grounding: `provisional`
- Definition: Treatment stage that removes suspended or settleable solids before downstream plant or biofilter stages.
- Use in this project: Appears in architecture-aware business scaffolding through `solids_filter_required` and solids-removal operating cost categories.
- Do not confuse with: [[#Biofilter|biofilter]], which is for biological conversion rather than primary solids capture.
- See also: [[#Biofilter|Biofilter]], [[#Media Bed|Media Bed]], [[#DWC / Raft|DWC / Raft]], [[#NFT|NFT]].

### Media Bed

- grounding: `repo_grounded`
- Definition: Grow bed that uses solid media for plant support and can add biofiltration surface area.
- Use in this project: Treated as an architecture with mixed-crop flexibility, integrated treatment potential, and clogging/cleaning burden.
- Do not confuse with: A standalone biofilter or a generic plant subsystem.
- Example or note: Current component note uses `component_id: media_bed`; business layer also uses `architecture_media_bed`.
- See also: [[#Biofilter|biofilter]], [[#Solids Filter|solids filter]], [[#DWC / Raft|DWC / Raft]], [[#NFT|NFT]].

### DWC / Raft

- grounding: `repo_grounded`
- Definition: Deep water culture plant bed using rafts over deeper water.
- Use in this project: Current research treats it as the clearest commercial leafy-greens archetype and the high-buffer baseline.
- Do not confuse with: `NFT` or hydroponics in general.
- Example or note: Current component note uses `dwc_raft_bed`; business layer uses `architecture_dwc_raft`.
- See also: [[#Dissolved Oxygen / DO|DO]], [[#Biofilter|biofilter]], [[#Solids Filter|solids filter]], [[#Media Bed|Media Bed]], [[#NFT|NFT]].

### NFT

- grounding: `repo_grounded`
- Definition: Nutrient film technique channel carrying a thin flowing water layer for lighter-rooted crops.
- Use in this project: Treated as a high-density, cleaner-water, high-fragility architecture with strong flow sensitivity.
- Do not confuse with: `DWC / raft` or generic channel irrigation.
- Example or note: Current component note uses `nft_channel`; business layer uses `architecture_nft`.
- See also: [[#Solids Filter|solids filter]], [[#Biofilter|biofilter]], [[#DWC / Raft|DWC / Raft]], [[#Media Bed|Media Bed]].

## Species Reference Terms

### Tilapia

- grounding: `repo_grounded`
- Definition: Current starter-profile fish species, stored as `fish_tilapia` and represented by Nile tilapia in the repo.
- Use in this project: Current fish-side economics and water-quality reference language centers on tilapia.
- Do not confuse with: `koi` or a generic fish placeholder.
- Example or note: `data/knowledge/species/fish/tilapia.json` is the current canonical species profile.

### Koi

- grounding: `todo`
- Definition: Requested glossary term, but not a cleanly defined canonical species profile in the current repo state.
- Use in this project: Mention only as a future fish-profile candidate unless canon is added.
- Do not confuse with: `tilapia`, which is the fish species currently used in active business files.
- Example or note: No canonical `data/knowledge/species/fish/koi.json` was found in this pass.

### Lettuce

- grounding: `repo_grounded`
- Definition: Current starter-profile leafy crop `plant_lettuce`.
- Use in this project: Major reference crop for architecture comparison, pH and nitrate interpretation, and head-based business rules.
- Do not confuse with: A generic leafy-greens bucket.
- Example or note: Current business rules already distinguish lettuce head-based and mass-based interpretation.

### Basil

- grounding: `repo_grounded`
- Definition: Current starter-profile herb crop `plant_basil`.
- Use in this project: Major herb reference crop for repeated harvest, bunch-vs-kg sales logic, and disease or decline risk.
- Do not confuse with: A generic herb placeholder.
- Example or note: Current business rules keep basil kg and bunch paths separate.

## Naming Conventions

- Prefer exact machine names in backticks: `crop_system_type`, `architecture_variant_id`, `observed_tan_mg_l`.
- In standalone notes or at first meaningful use, prefer expanded term plus abbreviation when helpful: `Total Ammonia Nitrogen (TAN)`.
- Prefer snake_case for machine fields and IDs; use normal prose for human-facing terms.
- Use the plain-language term first when helpful, then the exact ID if needed: `media bed` -> `architecture_media_bed` or `media_bed`.
- Keep layer words explicit: say `canonical knowledge`, `derived simulation output`, `vault note`, or `repo audit` instead of just `data`.
- Preserve unit suffixes in field names exactly as stored: `growing_area_m2`, `channel_length_m`, `observed_unionized_nh3_mg_l`.
- Preserve context instead of flattening it. If architecture, scale, crop, or temperature regime changes the meaning, say so.
- Use `schema-choice TODO` when basis is unresolved; do not hide uncertainty inside a vague mixed field name.
- Use `DWC / raft` in prose unless the exact machine term is required, such as `architecture_dwc_raft` or `dwc_raft_bed`.
- Preserve exact nitrate wording from the source field: `nitrate_mg_L`, `observed_nitrate_mg_l`, and `nitrateN` are not automatically interchangeable.

## Current Working Decisions

- These are current drafting and review directions, not permanent machine-schema claims.
- `crop_system_type` and `architecture_variant_id`: not one-to-one. Use `crop_system_type` as the upstream/runtime-facing field, use `architecture_variant_id` as the business/review taxonomy layer, and allow a later mapping table to connect them.
- `grow-unit basis` and `supporting-system basis`: keep them as formal glossary/review terms now, but do not promote them to machine-schema fields yet.
- Nitrate naming: normalize later through a controlled pass, but do not flatten `nitrate-N` and `nitrate` casually before that pass; preserve exact source wording meanwhile.
- `koi`: keep as glossary `todo` and do not include it in first-draft scope yet.
- `accepted` vs `provisional`: `accepted` means the meaning is stable enough that unresolved details do not materially change interpretation; `provisional` means the direction is useful, but basis, normalization, context split, or activation still materially affects meaning.

## Open Terminology Questions

- Should `crop_system_type` and `architecture_variant_id` be formally mapped one-to-one, or can one architecture contain multiple crop-system values?
- Should `grow-unit basis` and `supporting-system basis` become formal repo terms, or remain glossary shorthand only?
- Should nitrate naming be normalized to one canonical machine pattern across species, business, and chemistry files?
- Should `koi` become a canonical species profile in the first-draft scope, or remain outside the current starter profile set?
- When should `provisional` vs `accepted` be used in business-layer review, rather than mainly in evidence and atomic-truth review flow?
