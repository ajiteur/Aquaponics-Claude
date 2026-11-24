# Corroboration report for aquaponics Layer 1 component library: Media bed vs DWC vs NFT

## Executive summary

Media beds, deep water culture (DWC/raft/DFT), and nutrient film technique (NFT) are repeatedly identified by Tier‑1 aquaponics references as the **most common plant-unit architectures**, but they differ sharply in **solids tolerance**, **oxygen delivery mechanism**, **hydraulic fragility**, and **crop fit**. SRAC‑454 (Rakocy/Masser/Losordo; UVI/Texas A&M/NCSU authorship) provides the most complete aquaponics-specific treatment of trade-offs across **gravel/media**, **raft**, and **NFT**, including explicit failure modes (e.g., *NFT flow interruption → rapid wilting/death*; *gravel clogging → anaerobic zones killing roots*), solids-mineralisation trade-offs, and design ratios anchored to fish feed input and/or media volumes. citeturn12view0turn13view0turn14view4turn15view1

For **commercial coupled aquaponics**, raft/DWC is consistently positioned as the **workhorse for leafy greens** thanks to its high water volume buffer, avoidance of channel clogging, and operational resilience to short pump disruptions (plants remain in water). citeturn16view0turn14view3 However, raft systems introduce **unique biotic failure modes** (roots exposed to aquaculture-associated organisms; tilapia fry/ostracods/tadpoles/snails damaging roots) requiring screens/agitation/biocontrol fish. citeturn16view0

**NFT** is consistently described as **water‑efficient and space‑efficient (can be mounted/stacked)** but **highly sensitive to solids and hydraulic interruptions**. Aquaponics sources emphasise the need to remove solids so they do not accumulate on roots, and highlight the architecture’s lower surface area/water volume relative to raft—often implying the need for a **separate biofilter**. citeturn17view0turn13view7turn10view1turn1view3 Peer‑reviewed open‑access hydroponics synthesis (including WUR authorship) additionally frames NFT as **vulnerable to pump/power failures** and **temperature fluctuations**, and notes constraints for **long‑cycle crops** and hot/high‑irradiance climates. citeturn25view0turn26view5turn27view0

**Media beds (gravel/sand/perlite media‑based systems)** are repeatedly characterised as **easy/low‑cost** and particularly suitable for **small-scale** operations, with the media providing plant anchorage and often serving as **combined mechanical + biological filtration**. citeturn9view0turn17view0 Their key downside is **solids accumulation → clogging → anaerobic zones**, which then drives maintenance requirements (cleaning, cultivation/turning, worm inoculation) and limits scaling. citeturn9view0turn17view0

Across all three, the most simulation-relevant “architecture levers” supported by high‑trust sources are: **solids loading rate and removal strategy**, **oxygen delivery strategy (aeration density/venturi/mixing/ebb–flow dewatering)**, **water volume buffering (temperature/nutrient swing damping)**, and **pump failure sensitivity**. citeturn17view0turn16view0turn25view0

## Sources and scope

This report prioritises Tier 1–2 sources only:

- **SRAC‑454 (OSU-hosted PDF)**: *Recirculating Aquaculture Tank Production Systems: Aquaponics—Integrating Fish and Plant Culture* (Rakocy/Masser/Losordo) — Tier 1 extension/manual. citeturn12view0  
- **SRAC‑5007 (Mississippi State / SRAC PDF)**: *Principles of Small‑Scale Aquaponics* — Tier 1 extension fact sheet focused on beginner/small systems; includes media bed, NFT, DWC definitions and key design anchors. citeturn9view0turn8view0  
- **UVI Aquaponic Systems page** (UVI AES): concise “rules of thumb” for biofiltration needs by plant architecture (raft vs NFT) and exchange-rate notes for deep flow channels. citeturn1view3  
- **Peer‑reviewed open‑access chapter with WUR authorship**: Maucieri et al. (2019) *Hydroponic Technologies* (in *Aquaponics Food Production Systems*, Springer Open Access) — Tier 2 (peer‑reviewed) hydroponic baseline with relevant NFT/DFT constraints and oxygen/temperature sensitivity. citeturn25view0turn26view0turn26view5turn27view0  

FAO Technical Paper 589 (Somerville et al., 2014) is preferred Tier 1, but the official FAO-hosted PDFs repeatedly timed out in this environment; therefore this report relies on SRAC/UVI/WUR for the core trade-off rules and uses FAO only for limited metadata-level confirmation that the three architectures are the “primary methods.” citeturn18search12

## Corroboration table

Rows below are **candidate component-library findings** (rules/anchors) suitable for Layer 1. “System type” uses: `MEDIA` (media bed / gravel / substrate), `DWC` (raft / deep flow technique), `NFT` (nutrient film technique), `CROSS` (applies to multiple).

| Normalized field name | Candidate value or rule | System type | Source | Source type | Trust tier | Direct quote / close paraphrase (≤25 words where possible) | Exact page / section | Context tags | Recommendation |
|---|---|---|---|---:|---:|---|---|---|---|
| plant_system.media.definition | Media bed holds media for plant roots; media can act as biofilter and solids filter | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Media supports… roots… and can act as a biofilter and solids filter.” citeturn9view0 | p.2 (Plant Unit) | aquaponics-specific; small-scale; general crops | Promote |
| plant_system.media.best_for_scale | Media beds are easy/inexpensive; good choice for small-scale systems | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Media beds are easy and inexpensive… good choice for small-scale systems.” citeturn9view0 | p.2 | aquaponics-specific; small-scale | Promote |
| plant_system.media.hydraulics.modes | Media beds operate as flood-and-drain cycles or continuous flow-through | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Beds… flooded and drained or water flows… continuously.” citeturn9view0 | p.2 | aquaponics-specific; small-scale | Promote |
| plant_system.media.hydraulics.water_level_rule | Water should rise to ~1 inch below top of media to limit algae/pests | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Water should rise to only 1 inch from the top of the media…” citeturn9view0 | p.2 | aquaponics-specific; small-scale | Promote |
| plant_system.media.solids_and_biofilt.tradeoff | Integrated filtration simplifies design but requires periodic media cleaning; otherwise clogging/anaerobic zones | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Manage and clean… periodically… otherwise… clogged and create anaerobic zones.” citeturn9view0 | p.2 | aquaponics-specific; small-scale | Promote |
| plant_system.media.maintenance.worms | Worms may be added to digest trapped solids in media | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Worms… added… to help digest solid material…” citeturn9view0 | p.2 | aquaponics-specific; small-scale | Promote (context: worm-enabled beds) |
| plant_system.media.depth_inches | Typical media bed depth ~6–12 inches; varies by root zone | MEDIA | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Most media beds are 6 to 12 inches deep.” citeturn9view0 | p.2 | aquaponics-specific; small-scale | Promote |
| plant_system.media.solids_failure_mode_anaerobic | Gravel/media clogging + reduced circulation + decomposition → anaerobic zones impair/kill roots | MEDIA | SRAC‑454 citeturn13view0 | University extension/manual PDF | 1 | “Reduction in water circulation… decomposition… anaerobic zones… impair or kill… roots.” citeturn13view0 | p.8 (Gravel negative aspects) | aquaponics-specific; small-scale | Promote |
| plant_system.media.failure_mode_flow_interrupt | Gravel retains little water if drained; flow disruption → rapid wilting | MEDIA | SRAC‑454 citeturn13view0 | University extension/manual PDF | 1 | “Gravel retains very little water… disruption… rapid onset… wilting.” citeturn13view0 | p.8 | aquaponics-specific; small-scale/outdoor | Promote |
| plant_system.media.crop_fit_trellised | Trellised crops (tomatoes/melons/peppers) work best on ground in media-based systems; Dutch bucket variant works | MEDIA | SRAC‑5007 citeturn8view0 | University extension PDF | 1 | “Trellised crops… work best… in media-based systems. Dutch bucket… can work well…” citeturn8view0 | p.6 (Plant Management) | aquaponics-specific; greenhouse; fruiting crops | Promote |
| plant_system.media.biofilter_integration_possible | Granular media (gravel/sand/perlite) can serve as sole biofilter but tends to clog; severe clogging can lead to ammonia production | MEDIA | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | Granular media “serve as the sole biofilter… tendency to clog… can actually produce ammonia…” citeturn17view0 | p.7 (Biofiltration) | aquaponics-specific; RAS-integrated | Promote (with warnings) |
| plant_system.media.solids_pre_treatment_trigger | If organic overloading causes clogging, add solids removal before media or reduce stocking/feeding | MEDIA | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | “Install… solids removal… before the media, or… decrease… stocking… feeding rates.” citeturn17view0 | p.7 | aquaponics-specific; management response | Promote |
| plant_system.media.design_ratio_volume | Reciprocating gravel systems: recommended volume ratio 1 ft³ fish tank : 2 ft³ pea gravel media; with this ratio, no solids removed; beds cultivated + red worms | MEDIA | SRAC‑454 citeturn16view0 | University extension/manual PDF | 1 | “1 cubed feet… to 2 cubed feet… pea gravel… recommended… no solids… cultivated… red worms…” citeturn16view0 | p.9 (Component ratios) | aquaponics-specific; small-scale; media beds | Promote (split: reciprocating gravel only) |
| plant_system.dwc.definition | DWC/raft/DFT: plants on floating/hanging support in 10–20 cm nutrient solution; in aquaponics can be up to 30 cm | DWC | Maucieri et al. (2019) citeturn26view0 | Peer-reviewed OA chapter PDF | 2 | “DFT… deep water… containers filled with 10–20 cm… In AP… up to…” citeturn26view0 | p.90 (4.3.1 DFT) | hydroponic baseline; AP-compatible | Promote (as depth anchor) |
| plant_system.dwc.management_cost_profile | DFT/DWC can minimise costs and management (simple tanks + rafts) | DWC | Maucieri et al. (2019) citeturn26view0 | Peer-reviewed OA chapter PDF | 2 | “System… interesting as it minimizes costs and management.” citeturn26view0 | p.90 | hydroponic baseline; indoor/greenhouse | Promote (baseline) |
| plant_system.dwc.best_for_leafy | Raft subsystem is ideal for leafy green (and other vegetables) | DWC | SRAC‑454 citeturn14view1 | University extension/manual PDF | 1 | “Raft… subsystem is ideal for… leafy green… vegetables.” citeturn14view1 | p.8 (Raft section) | aquaponics-specific; commercial-scale; leafy greens | Promote |
| plant_system.dwc.geometry_anchor_UVI | Example UVI raft tanks: 100 ft × 4 ft × 16 in; contain 12 in water; polystyrene rafts 8 ft × 4 ft × 1.5 in | DWC | SRAC‑454 citeturn14view1turn16view0 | University extension/manual PDF | 1 | Dimensions given for UVI raft tanks/rafts citeturn14view1turn16view0 | p.8 | aquaponics-specific; commercial-scale; leafy greens | Promote (as variant anchor) |
| plant_system.dwc.temperature_buffering | Raft sheets shield water from sunlight and maintain lower-than-ambient water temperature (beneficial in tropics) | DWC | SRAC‑454 citeturn14view3 | University extension/manual PDF | 1 | “Sheets… maintain lower than ambient water temperature…” citeturn14view3 | p.8 | aquaponics-specific; warm climates; root-zone temp | Promote |
| plant_system.dwc.pump_failure_resilience | Pump disruption does not cut plant water supply in raft the way it does in gravel/sand/NFT | DWC | SRAC‑454 citeturn14view3turn14view4 | University extension/manual PDF | 1 | “Disruption in pumping does not affect… water supply as in… NFT…” citeturn14view3turn14view4 | p.8 | aquaponics-specific; failure-mode | Promote |
| plant_system.dwc.oxygenation_design_anchor_small | DWC/float beds: air stones in float bed ~1 per 10 ft² | DWC | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Air stones… one for every 10 square feet.” citeturn9view0 | p.3 (DWC section) | aquaponics-specific; small-scale; leafy greens/herbs | Promote (split: small-scale) |
| plant_system.dwc.oxygenation_design_anchor_commercial | UVI raft tanks maintained DO ~80% saturation (6–7 mg/L) using air diffusers ~one every 4 ft along tank length | DWC | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | “DO… 6 to 7 mg/L… diffusers (one every 4 feet)… long axis.” citeturn17view0 | p.7 (Biofiltration/DO) | aquaponics-specific; commercial-scale | Promote (split: UVI-style) |
| plant_system.dwc.exchange_vs_aeration_rule | Deep flow channels: exchange rate “unimportant” if aerated; unaerated channels require faster exchange | DWC | UVI Aquaponic Systems citeturn1view3 | University programme webpage | 1 | “Deep flow… unimportant as long as… aerated… Unaerated… faster exchange.” citeturn1view3 | “Maintain adequate exchange rates” | aquaponics-specific; DWC; hydraulics/oxygen coupling | Promote |
| plant_system.dwc.biofilter_integration | In raft aquaponics, hydroponic component can provide adequate biofiltration; NFT has less surface area → separate biofilter | DWC / NFT | UVI Aquaponic Systems citeturn1view3 | University programme webpage | 1 | “Raft… adequate biofiltration… NFT… less surface area… separate biofilter…” citeturn1view3 | “Ensure adequate biofiltration” | aquaponics-specific; system design | Promote (split by architecture) |
| plant_system.dwc.solids_requirement_for_treatment | Raft provides nitrification if solids removed from flow before hydroponic component | DWC | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | “Raft… provides sufficient nitrification if solids are removed…” citeturn17view0 | p.7 | aquaponics-specific; solids sensitivity | Promote |
| plant_system.dwc.solids_risk_root_coating | Suspended solids entering plant unit can accumulate on roots creating anaerobic zones preventing oxygen‑dependent nutrient uptake | DWC / CROSS | SRAC‑454 citeturn15view0 | University extension/manual PDF | 1 | “Solids… may accumulate on… roots and create anaerobic zones…” citeturn15view0 | p.5 (Solids significance) | aquaponics-specific; root oxygen | Promote |
| plant_system.dwc.failure_mode_biotic_roots | Raft disadvantage: roots exposed to harmful organisms; tilapia fry can consume roots; ostracods consume root hairs | DWC | SRAC‑454 citeturn16view0 | University extension/manual PDF | 1 | “Tilapia fry… consume plant roots… ostracods… consume root hairs…” citeturn16view0 | p.8 | aquaponics-specific; biotic failure | Promote |
| plant_system.dwc.mitigation_biotic_roots | Mitigations: fine mesh screen; increased agitation; stock predator fish (e.g., redear sunfish) in hydro tanks | DWC | SRAC‑454 citeturn16view0 | University extension/manual PDF | 1 | “Fine mesh screen… increase water agitation… stock… fish… to prey…” citeturn16view0 | p.8 | aquaponics-specific; operational control | Promote |
| plant_system.nft.definition | NFT: narrow channels/troughs where roots see thin film of water delivering water/nutrients/oxygen | NFT | SRAC‑454 citeturn16view0turn15view6 | University extension/manual PDF | 1 | “Roots… exposed to a thin film… delivering water, nutrients and oxygen…” citeturn16view0turn15view6 | p.8 | aquaponics-specific; greenhouse | Promote |
| plant_system.nft.geometry_anchor_width | NFT troughs have been described as ~4–6 inches wide | NFT | SRAC‑454 citeturn16view0 | University extension/manual PDF | 1 | “Troughs (4 to 6 inches wide)….” citeturn16view0 | p.8 | aquaponics-specific | Promote |
| plant_system.nft.hydraulics_slope_rule | NFT channels should be sloped ~½ inch per 10 feet; generally <12 feet long | NFT | SRAC‑5007 citeturn9view0 | University extension PDF | 1 | “Sloped approximately ½ inch per 10 feet… generally less than 12 feet long.” citeturn9view0 | p.3 (NFT) | aquaponics-specific; small-scale | Promote |
| plant_system.nft.hydraulics_water_layer_cm | NFT nutrient solution layer ~1–2 cm (classic hydroponic) | NFT | Maucieri et al. (2019) citeturn27view5 | Peer-reviewed OA chapter PDF | 2 | “Troughs with a 1–2 cm layer of water.” citeturn27view5 | p.91 (4.3.2 NFT) | hydroponic baseline; greenhouse | Promote (baseline anchor) |
| plant_system.nft.biofilter_need_reasoning | NFT has much smaller water volume/surface area than raft; less area for nitrifier colonisation → separate biofilter may be needed | NFT | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | NFT “water volume and surface area… smaller… no… area… colonization…” citeturn17view0 | p.7 | aquaponics-specific | Promote (context-dependent “may”) |
| plant_system.nft.solids_must_remove | In NFT aquaponics, solids must be removed or they can accumulate and kill roots | NFT | SRAC‑454 citeturn16view0turn13view7 | University extension/manual PDF | 1 | “Solids must be removed so they do not accumulate and kill roots.” citeturn16view0turn13view7 | p.8 | aquaponics-specific; solids sensitivity high | Promote |
| plant_system.nft.failure_mode_flow_interrupt | NFT: disruption in water flow can quickly cause wilting and death | NFT | SRAC‑454 citeturn13view7turn16view0 | University extension/manual PDF | 1 | “Disruption… water flow can lead quickly to wilting and death.” citeturn13view7turn16view0 | p.8 | aquaponics-specific; high fragility | Promote |
| plant_system.nft.failure_mode_pump_dependency | NFT low water levels + no substrate makes it vulnerable to pump failure (clogging/power) | NFT | Maucieri et al. (2019) citeturn26view5 | Peer-reviewed OA chapter PDF | 2 | “Lack of substrate… low water levels makes… vulnerable… pump… clogging… power supply.” citeturn26view5 | p.91 | hydroponic baseline; failure mode | Promote |
| plant_system.nft.temperature_sensitivity | NFT temperature fluctuations in nutrient solution can cause plant stress followed by disease; high susceptibility to temp variation limits hot/high-irradiance contexts | NFT | Maucieri et al. (2019) citeturn26view5turn27view4 | Peer-reviewed OA chapter PDF | 2 | “Temperature fluctuations… plant stress… diseases… not suitable… high irradiation and temperature.” citeturn26view5turn27view4 | p.91–92 | hydroponic baseline; warm climates | Promote (split by climate) |
| plant_system.nft.crop_suitability_long_cycle_limit | NFT root system ageing/loss of function can prevent long-cycle crops (>4–5 months); constraints for long-cycle production | NFT | Maucieri et al. (2019) citeturn27view0 | Peer-reviewed OA chapter PDF | 2 | “Constraint… prevents… long-cycle crops (over 4–5 months).” citeturn27view0 | p.92 | hydroponic baseline; fruiting/long-cycle | Promote (as constraint) |
| plant_system.nft.oxygen_mechanism_and_risk | NFT film absorbs oxygen by diffusion, but dense roots/organic matter can block flow → anaerobic zones → inhibits nitrifiers → separate biofilter needed | NFT | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | “Thin film… absorbs oxygen… but dense roots… create anaerobic zones… necessitates… separate biofilter.” citeturn17view0 | p.7 | aquaponics-specific | Promote |
| plant_system.nft.microlines_not_recommended | Microtubes for water delivery (common in hydroponics) are not recommended in aquaponics because they will clog | NFT / MEDIA | SRAC‑454 + UVI citeturn13view7turn1view3 | University manual + university webpage | 1 | “Microtubes… not recommended because they will clog” / “Spaghetti tubes… will most likely clog.” citeturn13view7turn1view3 | p.8; UVI “Ensure good aeration” | aquaponics-specific; maintenance | Promote |
| plant_system.cross.solids_strategy_depends_on_organic_loading | High organic loading → highly efficient solids removal desirable (e.g., microscreen drum); low loading may allow minimal solids removal (more mineralisation) | CROSS | SRAC‑454 citeturn15view2 | University extension/manual PDF | 1 | “High organic loading… microscreen drum… Low organic loading… solids removal may be unnecessary…” citeturn15view2 | p.5 | aquaponics-specific; trade-off | Promote (modeled as strategy) |
| plant_system.cross.solids_mineralisation_tradeoff | Some solids can be beneficial via mineralisation; insufficient solids → more nutrient supplementation needed | CROSS | SRAC‑454 citeturn15view1 | University extension/manual PDF | 1 | “Mineralization supplies… nutrients… Without sufficient solids… more supplementation…” citeturn15view1 | p.5 | aquaponics-specific; nutrient balance | Promote |
| plant_system.dwc.nitrification_buffering_acclimation | In UVI raft system, after ~1 month acclimation, ammonia/nitrite monitoring not necessary (due to robust nitrification in raft surfaces) | DWC | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | “After… acclimation period of 1 month, it is not necessary to monitor ammonia and nitrite…” citeturn17view0 | p.7 | aquaponics-specific; commercial-style raft | Promote (simulation hook) |
| plant_system.cross.temperature_buffering_dwc_vs_nft | DWC holds heat better than NFT; NFT pipes tend to lose heat to environment | DWC / NFT | SRAC‑5007 citeturn8view0 | University extension PDF | 1 | “DWC systems hold onto heat better than NFT… pipes… give back heat…” citeturn8view0 | p.8 | aquaponics-specific; temperature context | Promote |
| plant_system.cross.crop_fit_leafy_vs_fruiting | Leafy greens/herbs perform well (lower nutrient needs); fruiting crops require additional nutrients; nutrient strategy differs by crop type | CROSS | SRAC‑5007 citeturn8view0 | University extension PDF | 1 | “Herbs and leafy greens perform well… Fruiting crops… require additional nutrients…” citeturn8view0 | p.6 | aquaponics-specific; crop suitability | Promote |
| plant_system.cross.nutrient_concentration_buffering | Raft holds ~75% system water volume; gravel/NFT hold minor volume → for same feed input, nutrient concentrations in gravel/NFT can be ~4× raft | DWC / NFT / MEDIA | SRAC‑454 citeturn13view1 | University extension/manual PDF | 1 | “75 percent… water… in… raft… nutrient concentrations nearly four times higher in gravel and NFT…” citeturn13view1 | p.10 | aquaponics-specific; system-level | Promote (simulation-important) |
| plant_system.cross.design_ratio_feeding_adjust_by_architecture | Gravel and NFT systems should use feeding rate ratio ~25% of recommended ratio for raft hydroponics (to avoid concentration extremes) | NFT / MEDIA | SRAC‑454 citeturn13view1 | University extension/manual PDF | 1 | “Gravel and NFT… feeding rate ratio… approximately 25 percent… raft…” citeturn13view1 | p.10 | aquaponics-specific; design ratio | Promote (key balancing rule) |
| plant_system.dwc.waste_treatment_capacity_feed_per_area | Raft waste treatment capacity equivalent to ~180 g fish feed per m² plant area/day (requires solids removed before raft) | DWC | SRAC‑454 citeturn17view0 | University extension/manual PDF | 1 | “Waste treatment capacity… equivalent to… 180 grams… per square meter…/day.” citeturn17view0 | p.7 | aquaponics-specific; sizing anchor | Promote (UVI-style raft) |

## Contradictions table

Most “conflicts” are **context splits**, not true contradictions—different scales, climates, and solids strategies.

| Field | Conflicting candidates | Sources | Why it conflicts | Recommended action |
|---|---|---|---|---|
| plant_system.dwc.oxygenation_density | Air stones ~1 per 10 ft² vs air diffusers ~1 per 4 ft (UVI commercial raft) | SRAC‑5007 vs SRAC‑454 citeturn9view0turn17view0 | Different aeration hardware and scale (small hobby vs UVI commercial). | Split by context: `dwc.small_scale_airstone_density` vs `dwc.UVI_diffuser_spacing`. |
| plant_system.dwc.depth | DWC depth “10–12 inches (6 inches workable)” vs DFT “10–20 cm; in AP up to 30 cm” vs UVI raft “12 inches of water” | SRAC‑5007 vs WUR OA chapter vs SRAC‑454 citeturn9view0turn26view0turn14view1 | Different conventions/units and system families; aquaponics often uses deeper rafts than some hydroponic DFT. | Harmonise into tolerated range + variants: `dwc.depth_cm = 15–30` with UVI anchor at ~30. |
| plant_system.solids_removal_strategy | “Solids must be removed before raft for nitrification” vs “low organic loading may allow minimal solids removal” vs gravel reciprocating design “no solids removed” | SRAC‑454 citeturn17view0turn15view2turn16view0 | Not a contradiction: it’s an organic-loading and design-ratio strategy axis (mineralisation vs clogging risk). | Model as strategy modes: `solids_removal.high_efficiency` vs `solids_removal.low/mineralisation`. |
| plant_system.nft.biofilter_requirement | “May require separate biofilter” vs “separate biofilter needed” | SRAC‑454 vs UVI citeturn17view0turn1view3 | “May” reflects system design ratios where plant unit still provides some nitrification; UVI warns surface area is lower in NFT. | Keep as conditional rule: `nft.requires_biofilter = true unless additional nitrifying area provided`. |

## Component-library-ready fields

A compact, implementation-ready “Layer 1” structure (values are conservative defaults; add variants per context).

### Canonical system records

| Field | MEDIA (media bed / gravel) | DWC (raft / DFT) | NFT |
|---|---|---|---|
| component.key | `plant_system.media_bed` | `plant_system.dwc_raft` | `plant_system.nft` |
| core definition | Media-filled bed supports roots; can provide solids + biofiltration citeturn9view0turn17view0 | Floating/hanging support in deeper nutrient solution (often 15–30 cm aquaponics) citeturn26view0turn14view1 | Narrow troughs; thin film of water along channel; low water volume citeturn16view0turn27view5 |
| best suited for | Beginners/small-scale; trellised/ground crops and Dutch bucket variants citeturn9view0turn8view0 | Leafy greens and herbs; commercial staggered harvest; good in warm climates (shading) citeturn14view1turn14view3 | Leafy greens/herbs; space-efficient/stackable; avoid long-cycle/hot high-irradiance contexts unless mitigated citeturn16view0turn27view0turn27view4 |
| hydraulic requirement highlights | Flood-and-drain or continuous; maintain waterline below top media; risk flow disruption → wilting citeturn9view0turn13view0 | High volume buffer; pumping interruption less immediately harmful to plant water supply citeturn14view3turn14view4 | Strong pump dependence; slope constraints; flow interruption → rapid plant death citeturn9view0turn13view7turn26view5 |
| oxygen delivery mechanism | Ebb–flow dewatering exposes nitrifiers to atmospheric oxygen citeturn17view0 | Requires active aeration to maintain root DO; examples: air stones 1/10 ft² or diffusers 1/4 ft citeturn9view0turn17view0 | Film absorbs oxygen by diffusion; roots/organic matter can block flow causing anaerobic zones citeturn17view0 |
| solids sensitivity | Medium–high: media captures solids; must be cleaned/cultivated; clogging → anaerobic zones; can produce ammonia if overloaded citeturn9view0turn17view0 | Medium: solids on roots can create anaerobic zones; typically remove solids before raft for stable nitrification citeturn15view0turn17view0 | High: solids must be removed; microtubes clog; root mats can clog channels and drive anaerobic zones citeturn16view0turn13view7turn17view0 |
| root-zone temperature sensitivity | Moderate (not strongly quantified in core sources) | Lower swing risk; rafts shade and can lower water temperature in tropics citeturn14view3 | High sensitivity to temperature swings; WUR OA notes temperature fluctuations → stress/disease; not suitable in hot/high irradiation environments citeturn26view5turn27view4 |
| crop-duration suitability | Supports long-cycle + trellised crops (best fit among the three) citeturn8view0 | Suits staggered short-cycle crops; larger net pots possible for bigger plants citeturn14view1 | Long-cycle limitation (>4–5 months) due to root system ageing; mitigate with special multi-layer designs (context) citeturn27view0turn27view4 |
| common failure modes | Media clogging; anaerobic zones; labour-intensive cleaning; flow disruption → wilting citeturn9view0turn13view0 | Biotic root damage (tilapia fry/ostracods/tadpoles/snails); aeration failure; solids root-coating anaerobiosis citeturn16view0turn15view0 | Pump/power failure; solids clogging; temperature-induced stress/disease; microtube clogging citeturn13view7turn26view5 |
| maintenance pattern anchors | Periodic cleaning; optional worms; cultivate/stir between crops; heavy substrate handling citeturn9view0turn16view0 | Clean/handle rafts without drying biofilm; manage screens/agitation; maintain aeration devices citeturn9view0turn16view0 | Frequent inspection/cleaning of manifolds/outlets; avoid microtubes; keep holes large to reduce cleaning citeturn13view7turn1view3 |

## Best excerpts to ingest into a local pipeline

Short excerpts with suggested field keys (quotes kept short).

- `plant_system.nft.failure_mode_flow_interrupt`: “With NFT, a disruption in water flow can lead quickly to wilting and death.” citeturn13view7  
- `plant_system.media.solids_failure_mode_anaerobic`: “Clogging… reduction in water circulation… leads to… anaerobic zones that impair or kill plant roots.” citeturn13view0  
- `plant_system.dwc.temperature_buffering`: “Sheets… maintain lower than ambient water temperature…” citeturn14view3  
- `plant_system.dwc.pump_failure_resilience`: “A disruption in pumping does not affect the plant’s water supply as in… NFT…” citeturn14view3turn14view4  
- `plant_system.dwc.best_for_leafy`: “Raft… subsystem is ideal for… leafy green… vegetables.” citeturn14view1  
- `plant_system.dwc.failure_mode_biotic_roots`: “If tilapia fry gain access… they consume plant roots…” citeturn16view0  
- `plant_system.nft.solids_must_remove`: “Solids must be removed so they do not accumulate and kill roots.” citeturn16view0turn13view7  
- `plant_system.nft.pump_dependency_peer_reviewed`: “Lack of substrate… low water levels makes… NFT vulnerable… pump… clogging… power supply.” citeturn26view5  
- `plant_system.nft.temperature_sensitivity_peer_reviewed`: “Temperature fluctuations… cause plant stress followed by diseases.” citeturn26view5  
- `plant_system.dwc.depth_cm_anchor`: “DFT… containers filled with 10–20 cm… In AP this can be up…” citeturn26view0  
- `plant_system.cross.nutrient_concentration_buffering`: “Nutrient concentrations nearly four times higher in gravel and NFT… than in raft…” citeturn13view1  
- `plant_system.cross.biofiltration_by_architecture`: “Raft… adequate biofiltration… NFT… separate biofilter is needed.” citeturn1view3  

## Starter simulation hooks for media bed vs DWC vs NFT

Hooks are phrased as simulation-ready rules; each is backed by at least one Tier 1–2 source.

1) **Pump failure fragility by architecture**  
If `pump_state=OFF`, then:
- NFT: plant water stress rises **rapidly** (wilting/death). citeturn13view7turn26view5  
- Media/gravel: water stress rises quickly if beds drain; raft buffered (plants still in water). citeturn13view0turn14view3  

2) **Solids carryover penalty model**  
If `suspended_solids_inflow_to_plants` exceeds a threshold:
- Increase probability of **root-zone anaerobic events** (solids coat roots) and reduce nutrient uptake. citeturn15view0  
- For NFT specifically: increase probability of **root clogging/channel blockage** and “roots die” events unless solids removal is enabled. citeturn16view0turn17view0  

3) **Media bed “clogging → anaerobic zones” state machine**  
Accumulate `media_solids_load` over time; when above a limit, set `media_clogged=true`, then:
- Reduce effective circulation and increase anaerobic zone probability; apply root mortality penalty until `media_cleaned` event occurs. citeturn9view0turn13view0  

4) **Architecture-driven nitrification capacity adjustment**  
- Raft: allow substantial nitrification surface area on raft undersides/walls; after `system_age > ~1 month` reduce ammonia/nitrite monitoring burden (or increase stability margin). citeturn17view0  
- NFT: reduce nitrification surface area; default `separate_biofilter_required=true` unless extra media is provided. citeturn17view0turn1view3  

5) **Water volume buffering and nutrient concentration swings**  
Represent system nutrient concentration swing amplitude inversely with `hydroponic_water_volume_fraction`. Raft ≈ high buffering; gravel/NFT ≈ low buffering; encode SRAC estimate of ~4× concentration difference scenario as calibration guidance. citeturn13view1  

6) **Root-zone oxygen requirement (DWC/DFT)**  
If `DWC_root_DO < 4–5 mg/L`, apply nutrient uptake penalty/deficiency risk (hydroponic baseline); optionally tighten under warm water conditions. citeturn26view0turn26view7  

7) **Climate mismatch penalty (NFT hot/high irradiance)**  
If `climate_heat_index` high and `NFT` chosen, increase plant stress/disease risk due to solution temperature fluctuations; reduce suitability score. citeturn26view5turn27view4  

8) **Raft-specific biotic intrusion events**  
If `fish_fry_intrusion=true` or `zooplankton_bloom=true`, apply raft root damage/stunting unless `mesh_screen` and/or `agitation` mitigation is enabled. citeturn16view0  

## Recommended component variants to add

These variants are chosen because they map directly to corroborated trade-offs and can drive meaningful gameplay and simulation branching.

Media bed variants  
- `media_bed.flood_and_drain_bell_siphon` (ebb–flow oxygenation; periodic solids capture; clogging risk) citeturn9view0turn17view0  
- `media_bed.continuous_flow` (simpler hydraulics; potentially different clogging dynamics; still requires periodic cleaning) citeturn9view0  
- `media_bed.worm_inoculated` (adds solids digestion capacity; reduces clogging rate) citeturn9view0turn16view0  
- `media_bed.reciprocating_gravel_ratio_SRA454` (encode 1 ft³ fish : 2 ft³ gravel; “no solids removed” mode) citeturn16view0  

DWC/raft variants  
- `dwc_raft.small_scale_airstone_density` (1 air stone/10 ft²) citeturn9view0  
- `dwc_raft.UVI_diffuser_spacing` (diffusers ~1 per 4 ft; target DO 6–7 mg/L) citeturn17view0  
- `dwc_raft.aerated_channels_exchange_relaxed` vs `dwc_raft.unaerated_exchange_strict` citeturn1view3  
- `dwc_raft.biotic_intrusion_protected` (mesh screen + agitation) vs `dwc_raft.biotic_intrusion_unprotected` citeturn16view0  

NFT variants  
- `nft.standard_manifold_large_holes` (avoid microtubes; reduce clogging frequency) citeturn13view7  
- `nft.with_fine_solids_removal` (required in aquaponics to prevent root kill) citeturn16view0turn15view2  
- `nft.vertical_stack` (space efficiency; introduces maintenance/harvest access penalty) citeturn16view0  
- `nft.hot_climate_penalty` (temperature swing vulnerability) citeturn26view5turn27view4  
- `nft.long_cycle_restricted` (constraint on long-cycle crops >4–5 months) citeturn27view0  

Cross-system “strategy” variants (important for coupled aquaponics balancing)  
- `solids_strategy.high_efficiency_removal` (e.g., microscreen drum filter; high organic loading) citeturn15view2  
- `solids_strategy.low_removal_mineralisation` (accept some solids for mineralisation; increases clogging/anaerobic management burden) citeturn15view1turn15view2  
- `feeding_ratio.architecture_adjusted` (raft baseline vs gravel/NFT ≈ 25% of raft) citeturn13view1turn16view0