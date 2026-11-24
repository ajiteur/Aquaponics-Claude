# Corroboration report for aquaponics Layer 1 component library: Pumps and aeration

## Executive summary

This report consolidates **Tier 1–2** evidence on **pumps (recirculation/circulation)** and **aeration (oxygenation/degassing)** for **coupled aquaponics** and **closely related RAS**. It translates high‑trust guidance into **component-library-ready rules**, **numeric flow/exchange anchors**, **DO-related operational triggers**, **failure modes**, and **maintenance patterns** suitable for Layer 1 simulation. Primary Tier‑1 anchors come from **UVI (University of the Virgin Islands) aquaponics design guidance and commercial system documentation**, plus **SRAC** (Southern Regional Aquaculture Center) RAS/aquaponics manuals and an OSU-hosted SRAC aquaponics integration fact sheet. citeturn1view0turn13view0turn13view4turn11view0turn20view0

Across sources, the **pump’s system role** is consistently framed as: sustaining **stable hydraulic exchange** that rapidly removes wastes from fish tanks, moves water through treatment processes and plant units, and provides **mixing currents** that can be essential for even oxygen distribution (especially when oxygen is injected/added in concentrated streams). citeturn13view0turn11view0turn20view0turn13view4

The **aeration role** is consistently framed as: keeping **fish safe** and supporting **biofilter/nitrifier performance** by maintaining high dissolved oxygen and enabling **degassing** of CO₂ and other gases. SRAC specifies that DO should be maintained **above 60% saturation or above 5 mg/L** for optimum fish growth in most warmwater systems, that **nitrifiers become inefficient below 2 mg/L**, and that aeration must operate **continuously** in intensive systems. citeturn13view0

Practical circulation anchors are strong for UVI-style coupled systems: UVI lists a **rearing tank exchange rate target of ~1 hour** (noting their system average was **1.37 hours**) and clarifier **20 minutes**, while their commercial system page reports water pumped through each rearing tank at **25 gpm (100 L/min)** for a **full volume exchange every ~1:20 hours**. citeturn1view0turn20view0

Failure and safety modelling is well supported by explicit operational triggers: SRAC includes **alarm-style actions** such as **“Low dissolved oxygen (<5 mg/L): increase aeration; stop feeding until corrected”**, and fish behavioural indicators of oxygen problems (crowding at inflows/aerators, gulping at the surface). Both SRAC and UVI stress the need for **emergency aeration and backup power**, with UVI providing highly operational generator maintenance patterns (automatic transfer switch, monthly service, weekly exercise, phone alarm, mobile backup generator for key aeration). citeturn13view2turn13view1turn1view0

Energy/power anchors are available in UVI commercial-scale documentation, but not all of it is retrievable as first-party PDFs in this environment. Still, the accessible UVI commercial system report copy provides concrete motor ratings such as **pump ~0.37 kW (and also reported as 0.74 kW in an earlier trial)** and **blowers ~1.1 kW (fish) and 0.74 kW (plants)**. These values are best treated as **strong empirical anchors** but **split by system version (CA1 vs CA2)**. citeturn2view3turn2view1

## Evidence base and scope notes

Tier 1 sources used include: **UVI “Principles of aquaponics” page** (exchange rates, channel aeration vs exchange trade-off, power backup procedures), **UVI Commercial Aquaponic System (CAS) page** (per-tank pump flow and full-volume exchange timing), **SRAC 5007 Principles of Small-Scale Aquaponics** (pump placement, movement-of-water design notes, aeration density for DWC beds), and **SRAC 0452 Management of Recirculating Systems** (DO guidelines, nitrifier DO thresholds, continuous aeration requirement, fish behaviour indicators, and explicit management triggers). citeturn1view0turn20view0turn13view4turn13view0turn13view2

Tier 1 also includes an OSU-hosted SRAC aquaponics integration fact sheet, which gives UVI-specific operational numbers (e.g., total flow to four tanks, diffuser count, retention time, solids filtration cleaning frequency, and degassing tank role). citeturn11view0

Tier 2 evidence used here is limited to **institution-authored but third-party hosted** UVI commercial system report copies that provide energy/power and DO outcomes; where these are used, they are marked **“split by context”** or **“keep provisional”** depending on redundancy with first-party sources. citeturn2view3turn2view2

## Corroboration table

Each row below is a *candidate finding* for the component library (pumps and aeration). Where possible, quotes are kept ≤25 words.

| Normalised field name | Candidate value or rule | Source (URL or PDF title) | Source type | Trust tier | Direct quote / close paraphrase | Exact page / section | Context tags | Recommendation |
|---|---|---|---|---:|---|---|---|---|
| pump.role.hydraulic_exchange_benefit | High exchange quickly removes suspended solids and toxic metabolites from fish tanks | “Fish and Vegetable Production… 25 Years…” (UVI commercial system; hosted copy) `https://www.tag2grow.org/wp-content/uploads/2021/09/UVI-Aquaponics.pdf` citeturn2view1 | University programme report (hosted copy) | 2 | “A high water exchange rate quickly removed suspended solids and toxic waste metabolites…” citeturn2view1 | PDF p.4 (text excerpt) | Aquaponics; warmwater; commercial-scale | Split by context (UVI-specific but generalisable rule) |
| pump.role.system_recirculation | Pump returns treated water from sump/reservoir back to rearing tanks; sump location enables gravity returns | OSU-hosted SRAC aquaponics integration page `https://extension.okstate.edu/...aquaponics-integrating-fish-and-plant-culture` citeturn11view0 | University extension fact sheet | 1 | “Water collects in a reservoir (sump) and is returned to the rearing tank…” citeturn11view0 | System description | Aquaponics/RAS; warmwater; commercial-scale archetype | Promote to component library |
| pump.role.mixing_for_oxygen_distribution | Pump-driven currents are used to rapidly mix oxygenated/supersaturated water; mixing is critical | SRAC 0452 PDF `https://www.ncrac.org/files/inline-files/SRAC0452.pdf` citeturn13view0 | University extension (SRAC) | 1 | Supersaturated water should be “rapidly mixed… by currents… from the water pumping equipment.” citeturn13view0 | DO section, p.2 | RAS baseline; warmwater general | Promote |
| pump.design.location_sump | Place submersible pump/air-lift at sump bottom (lowest point); use gravity where possible | SRAC 5007 PDF `https://srac.msstate.edu/pdfs/Fact%20Sheets/5007%20Principles%20of%20Small-Scale%20Aquaponics.pdf` citeturn13view4 | University extension (SRAC) | 1 | “Pump… should be located at the lowest point… bottom of the sump… Gravity… lower the cost…” citeturn13view4 | “Movement of Water”, p.5 | Aquaponics; small-scale; general | Promote |
| pump.design.oversize_piping_for_clogging | Use oversized pipes when possible to reduce clogging risk | SRAC 5007 PDF citeturn13view4 | University extension (SRAC) | 1 | “Use oversized pipes to avoid any clogging that can occur.” citeturn13view4 | “Movement of Water”, p.5 | Aquaponics; small-scale | Promote |
| pump.flow.exchange_rate_rearing_target | Rearing tank exchange rate: 1 hour (UVI system 1.37 hours) | UVI “Aquaponic Systems” page `https://www.uvi.edu/.../aquaponic-systems/` citeturn1view0 | University programme webpage | 1 | “Rearing tank – **1 hour (UVI system – 1.37 hours)**.” citeturn1view0 | “Maintain adequate exchange rates” | Aquaponics; warmwater; commercial archetype | Promote (split by system version) |
| pump.flow.exchange_rate_clarifier_target | Clarifier exchange/retention: 20 minutes | UVI “Aquaponic Systems” page citeturn1view0 | University programme webpage | 1 | “Clarifier – **20 minutes**.” citeturn1view0 | “Maintain adequate exchange rates” | Aquaponics; warmwater | Promote |
| pump.flow.exchange_rate_dwc_rule | Deep flow channels exchange rate less important if aerated; if unaerated, require faster exchange | UVI “Aquaponic Systems” page citeturn1view0 | University programme webpage | 1 | “Deep flow… unimportant as long as they are aerated… Unaerated channels must have a faster exchange rate.” citeturn1view0 | “Maintain adequate exchange rates” | Aquaponics; DWC/raft; warmwater | Promote (core coupled trade-off rule) |
| pump.flow.rearing_tank_full_exchange | Pumped continuously at 25 gpm (100 L/min) per tank, full volume exchange every 1:20 hrs | UVI CAS page `https://www.uvi.edu/.../aquaponic-systems/application.html` citeturn20view0 | University programme webpage | 1 | “Water is pumped… **25 gallons/minute (100 l/min)**… full volume exchange every **1:20 hrs**.” citeturn20view0 | “UVI Commercial Aquaponic System (CAS)” | Aquaponics; warmwater; commercial-scale | Promote (strong numeric anchor) |
| pump.flow.total_flow_four_tanks | Total flow to four tanks 100 gpm; retention time 82 minutes; flow apportioning increases with fish growth | OSU-hosted SRAC aquaponics integration page citeturn11view0 | University extension fact sheet | 1 | “Flow rate to all four tanks is **100 gallons/minute**… average… **82 minutes**… higher flow as fish grow.” citeturn11view0 | Rearing unit description | Aquaponics; warmwater; commercial-scale | Promote |
| aeration.role.core | Adequate DO is required by fish and bacteria/biofilter; essential to operation | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “Supplying adequate… dissolved oxygen… to fish and… bacteria/biofilter… is essential…” citeturn13view0 | DO section, p.2 | RAS baseline; warmwater | Promote |
| aeration.DO.target_warmwater | Maintain DO above 60% saturation or above 5 mg/L for optimum fish growth (warmwater) | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “DO… maintained above **60 percent of saturation or above 5 ppm**…” citeturn13view0 | DO section, p.2 | RAS baseline; warmwater | Promote |
| aeration.DO.threshold_nitrifiers | Nitrifiers inefficient below 2 mg/L DO | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “Nitrifying bacteria become inefficient… below **2 ppm**.” citeturn13view0 | DO section, p.2 | RAS baseline | Promote (alarm boundary for nitrification) |
| aeration.ops.continuous_required | Aeration systems must operate continuously in intensive systems | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “Aeration systems must operate **continuously**…” citeturn13view0 | DO section, p.2 | RAS baseline; warmwater | Promote |
| aeration.ops.heavy_feeding_risk | At high feeding near harvest, oxygen demand may exceed system capacity; add aeration or reduce feeding | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | Oxygen demand may exceed aeration capacity; “supplemental aeration… or feeding… reduced.” citeturn13view0 | DO section, p.2 | RAS baseline; warmwater; high biomass | Promote |
| aeration.indicator.fish_behaviour_low_DO | Fish crowd around inflow/aerators or gulp at surface → check DO | SRAC 0452 Table 7 (fish observation) citeturn13view1 | University extension (SRAC) | 1 | “Crowding around water inflow/aerators… possible cause: **low oxygen**… check dissolved oxygen.” citeturn13view1 | Table 7, p.9 | RAS baseline; warmwater | Promote |
| aeration.alarm.DO_low_action | If DO <5 mg/L: increase aeration; stop feeding until corrected | SRAC 0452 Table 8 (water quality triggers) citeturn13view2 | University extension (SRAC) | 1 | “Low dissolved oxygen (**<5 ppm**)… **increase aeration**… **stop feeding** until corrected.” citeturn13view2 | Table 8, p.10 | RAS baseline; warmwater | Promote |
| aeration.alarm.CO2_high_action | If CO₂ >20 mg/L: add air stripping column or increase aeration | SRAC 0452 Table 8 citeturn13view2 | University extension (SRAC) | 1 | “High carbon dioxide (**above 20 ppm**)… add air stripping column… increase aeration.” citeturn13view2 | Table 8, p.10 | RAS baseline | Promote |
| aeration.failure.supersaturation_gas_bubble | Poor mixing can create zones of supersaturation → gas bubble disease; fry especially sensitive | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “Zones of supersaturation can cause gas bubble disease… Fry are particularly sensitive…” citeturn13view0 | DO section, p.2 | RAS baseline; life stage: fry | Promote (failure mode) |
| aeration.design.DWC_air_stone_density | DWC: place air stones in float bed ~1 per 10 sq ft | SRAC 5007 PDF citeturn13view3 | University extension (SRAC) | 1 | “Air stones… one for every **10 square feet**.” citeturn13view3 | DWC section, p.4 | Aquaponics; DWC/raft; small-scale | Promote (design anchor; split by scale) |
| aeration.design.biofilter_DO_target | Maintain DO >5 mg/L in biofilter tank | SRAC 5007 PDF citeturn13view4 | University extension (SRAC) | 1 | “DO… in the biofilter tank… maintained at more than **5 ppm**.” citeturn13view4 | Biofilter section, p.5 | Aquaponics; small-scale | Promote (conservative setpoint) |
| aeration.role.degassing_CO2 | Vigorous aeration vents CO₂ and prevents build-up | UVI commercial system report (hosted copy) citeturn2view1 | University programme report (hosted copy) | 2 | “Vigorous aeration vented carbon dioxide… and prevented its buildup.” citeturn2view1 | PDF p.4 excerpt | Aquaponics; warmwater; commercial-scale | Promote (mechanism); keep provisional on provenance |
| aeration.role.DWC_reaeration_mixing | Air stones in hydroponic tanks re‑aerate and mix water; expose water to nitrifying biofilm | UVI commercial system report (hosted copy) citeturn2view2 | University programme report (hosted copy) | 2 | Air stones “re‑aerated and mixed… exposing it to… nitrifying bacteria… on tank surface areas…” citeturn2view2 | PDF p.6 excerpt | Aquaponics; raft/DWC; warmwater | Promote; split by system type |
| DO.effect.hydroponic_passage | DO increased from 4.0 to 6.9 mg/L through hydroponic tanks (UVI trial) | UVI commercial system report (hosted copy) citeturn2view2 | University programme report (hosted copy) | 2 | “DO increased from **4.0 to 6.9 mg/L** on passage through the hydroponic tanks.” citeturn2view2 | PDF p.6 excerpt | Aquaponics; raft/DWC; warmwater | Keep provisional (trial-specific), but useful for simulation calibration |
| aeration.performance.rearing_DO_mean | Mean DO maintained at 6.2 mg/L in rearing tank (UVI trial) | UVI commercial system report (hosted copy) citeturn2view1 | University programme report (hosted copy) | 2 | “DO levels were maintained at a mean of **6.2 mg/L**…” citeturn2view1 | PDF p.4 excerpt | Aquaponics; warmwater; commercial-scale | Keep provisional (version-specific), but strong numeric anchor |
| aeration.design.rearing_diffusers_count | Rearing tanks “heavily aerated with 22 air diffusers” | OSU-hosted SRAC aquaponics integration page citeturn11view0 | University extension fact sheet | 1 | “Each circular rearing tank… heavily aerated with **22 air diffusers**.” citeturn11view0 | Rearing tank description | Aquaponics; warmwater; commercial-scale | Promote (design anchor) |
| aeration.role.degassing_tank | Degassing tank uses air diffusers to vent H₂S, methane, etc., before water reaches plants | OSU-hosted SRAC aquaponics integration page citeturn11view0 | University extension fact sheet | 1 | “Anaerobic… leads to… hydrogen sulfide… Therefore, a **degassing tank**… air diffusers vent the gasses…” citeturn11view0 | Solids/degassing discussion | Aquaponics; warmwater; commercial-scale | Promote |
| pump.failure.plant_risk_NFT | NFT: disruption in water flow can quickly cause wilting/death | OSU-hosted SRAC aquaponics integration page citeturn11view0 | University extension fact sheet | 1 | “With NFT, a disruption in water flow can lead quickly to **wilting and death**.” citeturn11view0 | NFT discussion | Aquaponics; greenhouse; flow-critical | Promote (simulation failure mode) |
| pump.failure.plant_risk_gravel | Reduced circulation + decomposition → anaerobic zones that impair/kill roots; flow disruption → rapid wilting | OSU-hosted SRAC aquaponics integration page citeturn11view0 | University extension fact sheet | 1 | “Reduction in water circulation… anaerobic zones… impair or kill plant roots… disruption… rapid… wilting.” citeturn11view0 | Gravel system drawbacks | Aquaponics; media beds; outdoor/greenhouse | Promote |
| maintenance.power_backup_generator | Install generator + automatic transfer switch; monthly service contract; weekly automatic exercise; phone alarm; mobile generator for key aeration | UVI “Aquaponic Systems” page citeturn1view0 | University programme webpage | 1 | “Install generator… monthly service contract… Schedule weekly… exercise… Install a phone alarm system… smaller mobile generator…” citeturn1view0 | “Ensure power backup” | Aquaponics; commercial | Promote (maintenance pattern) |
| maintenance.backup_components_design | Design with emergency aeration, backup power, and backup components | SRAC 0452 PDF citeturn12view1 | University extension (SRAC) | 1 | “Design the system with an emergency aeration system, back‑up power sources, and backup system components.” citeturn12view1 | Conclusion/p.10 text | RAS baseline | Promote |
| maintenance.monitoring_frequency_DO | Monitor DO closely before/after feeding; continuous feeding can reduce sharp DO drops | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “During… heavy feeding… DO should be monitored closely, particularly before and after feedings.” citeturn13view0 | DO section, p.2 | RAS baseline; warmwater | Promote |
| energy.anchor_pump_and_blowers_kW | Example UVI system: Pump 0.37 kW; blowers 1.1 kW (fish) and 0.74 kW (plants) | UVI commercial system report (hosted copy) citeturn2view3 | University programme report (hosted copy) | 2 | “Flow rate: 378 L/min, Pump: **0.37 kW**; Blowers: **1.1 kW** (fish) and **0.74 kW** (plants).” citeturn2view3 | PDF p.3 excerpt | Aquaponics; warmwater; commercial | Split by context (system version); keep provisional on provenance |
| energy.anchor_pump_kW_alt | Earlier UVI trial: 0.74 kW in-line pump moved 378 L/min | UVI commercial system report (hosted copy) citeturn2view1 | University programme report (hosted copy) | 2 | “A **0.74‑kW** in-line pump moved water… **378 L/min**…” citeturn2view1 | PDF p.4 excerpt | Aquaponics; warmwater | Contradiction ticket needed (power rating differs vs p.3) |
| monitoring.trigger_low_DO_fish_behaviour | Fish gather at surface and swim into aeration currents when oxygen-stressed | SRAC 0452 PDF citeturn13view0 | University extension (SRAC) | 1 | “Fish show signs… gathering at the surface and swimming into the current…” citeturn13view0 | DO section, p.2 | RAS baseline | Promote |
| monitoring.trigger_combined_DO_NH3_NO2_behaviour | “Lying at surface” / “crowding around inflow” can indicate low oxygen, high ammonia, or high nitrite—check these | SRAC 0452 Table 7 citeturn13view1 | University extension (SRAC) | 1 | These behaviours list “low oxygen” and “high ammonia or nitrite” as possible causes; check DO, ammonia, nitrite. citeturn13view1 | Table 7, p.9 | RAS baseline | Promote |
| pump.role.flow_diversion | Flow can be diverted: side-stream to hydroponics after solids removal; most water passes biofilter back to tank | OSU-hosted SRAC aquaponics integration page citeturn11view0 | University extension fact sheet | 1 | “A small side-stream flow may go to a hydroponic component… while most… passes through a biofilter…” citeturn11view0 | System configuration | Aquaponics; commercial design | Promote |

## Contradictions table

| Field | Conflicting candidates | Sources | Reason for difference | Recommended action |
|---|---|---|---|---|
| Fish tank exchange/turnover target | “Rearing tank – 1 hour” vs UVI system “1.37 hours” vs CAS page “full volume exchange every 1:20 hrs” vs UVI trial “0.8 h” | UVI principles page citeturn1view0 vs UVI CAS page citeturn20view0 vs UVI commercial report copy citeturn2view1 | Different system versions and operating regimes (CA1 vs CA2), and “recommended” vs “observed”. | **Split by context**: store a *design target* (≈1 h) and *observed examples* (0.8–1.37 h). |
| Total flow to tanks | OSU page: flow rate to four tanks 100 gpm vs CAS page: 25 gpm per tank | OSU aquaponics integration citeturn11view0 vs UVI CAS citeturn20view0 | Not a true contradiction: 25 gpm per tank × 4 tanks = 100 gpm total. | **No contradiction ticket**; normalise to per-tank and total. |
| Pump power rating in “UVI commercial” examples | Pump 0.37 kW vs 0.74 kW (both paired with ~378 L/min) | UVI report copy (p.3 vs p.4 excerpts) citeturn2view3turn2view1 | Likely different pumps across trials/versions (CA2 vs CA1), different measurement conventions, or reporting of nameplate vs measured draw. | **Split by system version**; open a **contradiction ticket** if your library requires a single power anchor. |
| DO setpoints vs “minimums” | DO >5 mg/L recommended for fish growth vs nitrifier inefficiency below 2 mg/L | SRAC 0452 DO guidance citeturn13view0 | These are different constructs: operational setpoint for growth/safety vs lower bound for nitrification. | **Promote both** as separate fields: `do_setpoint` and `do_min_nitrification`. |
| “Channel exchange rate” importance in DWC | DWC exchange “unimportant as long as aerated” vs general emphasis on exchange for waste removal | UVI principles page citeturn1view0 vs UVI/OSU emphasis on removing wastes from fish tanks via exchange/flow citeturn11view0turn20view0 | DWC channels can rely on aeration for root oxygenation; fish tanks still require turnover to export wastes to treatment. | **Split by subsystem**: fish tank turnover vs plant channel aeration/exchange trade-off. |

## Component-library-ready fields

The following are **suggested canonical fields** for a Layer 1 component library, populated only with **strongest corroborated values** (or marked unspecified where Tier 1–2 sources here do not provide a number).

### Pump component

| Field key | Recommended default / anchor | Notes / source basis |
|---|---|---|
| `pump.function.primary` | Maintain recirculation/turnover and hydraulic stability; deliver water through filters/plant units and back to fish tanks | SRAC/OSU/UVI describe recirculation loop architecture and exchange importance. citeturn11view0turn20view0turn13view4 |
| `pump.location.recommended` | Place main pump at sump bottom (lowest point) | SRAC 5007. citeturn13view4 |
| `pump.design.gravity_preference` | Use gravity where possible to reduce water movement cost | SRAC 5007. citeturn13view4 |
| `pump.design.piping_clogging_mitigation` | Oversize pipes when possible to reduce clogging risk | SRAC 5007. citeturn13view4 |
| `pump.turnover_target.rearing_tank` | **~1 hour** baseline design target (store observed examples separately) | UVI principles page provides target and observed 1.37 h. citeturn1view0 |
| `pump.turnover_observed.rearing_tank_examples` | **0.8 h**, **1.37 h**, **~1:20 h** | UVI documents multiple operating points; encode as examples rather than one truth. citeturn2view1turn1view0turn20view0 |
| `pump.flow_anchor.per_tank` | **25 gpm (100 L/min)** per rearing tank (UVI CAS) | Strong, first-party numeric anchor. citeturn20view0 |
| `pump.flow_anchor.system_total` | **100 gpm** to four rearing tanks (UVI-derived commercial configuration) | OSU SRAC aquaponics integration. citeturn11view0 |
| `pump.energy.anchor_power_draw` | **Unspecified (Tier‑1)**; **0.37 kW / 0.74 kW** provisional examples | Only accessible as a hosted report copy; treat as version-specific; do not hardcode as universal. citeturn2view3turn2view1 |
| `pump.failure.plant_impact_NFT` | Flow disruption in NFT can rapidly cause wilting/death | OSU-hosted SRAC integration. citeturn11view0 |

### Aeration component

| Field key | Recommended default / anchor | Notes / source basis |
|---|---|---|
| `aeration.function.primary` | Maintain DO for fish + nitrifiers; support degassing (CO₂, other gases) | SRAC and UVI/OSU describe DO needs and degassing roles. citeturn13view0turn11view0turn2view1 |
| `do.setpoint.fish_tank_warmwater` | **≥5 mg/L** (or ≥60% saturation) | SRAC 0452. citeturn13view0 |
| `do.min.nitrification_efficiency` | **2 mg/L** (below this nitrifiers inefficient) | SRAC 0452. citeturn13view0 |
| `do.alarm.low` | **<5 mg/L** triggers action | SRAC Table 8. citeturn13view2 |
| `do.alarm.actions_low` | Increase aeration; stop feeding until corrected | SRAC Table 8. citeturn13view2 |
| `co2.alarm.high` | **>20 mg/L** CO₂ triggers management | SRAC Table 8. citeturn13view2 |
| `aeration.ops.continuous` | Aeration must run continuously in intensive systems | SRAC 0452. citeturn13view0 |
| `aeration.design.DWC_air_stone_density_smallscale` | **1 air stone per 10 ft²** of float bed | SRAC 5007 (small-scale guidance). citeturn13view3 |
| `aeration.design.rearing_diffusers_UVI_example` | **22 air diffusers per rearing tank** | OSU SRAC integration (UVI example). citeturn11view0 |
| `aeration.failure.supersaturation` | Poor mixing can create supersaturation zones → gas bubble disease (fry sensitive) | SRAC 0452. citeturn13view0 |
| `power_backup.requirement` | Provide emergency aeration + backup power + backup components | SRAC 0452 and UVI guidance. citeturn12view1turn1view0 |
| `power_backup.maintenance_UVI_pattern` | Monthly generator service; weekly automatic exercise; phone alarm; mobile generator for key aeration | UVI “Ensure power backup”. citeturn1view0 |

## Best excerpts to ingest into a local pipeline

Short, high-signal excerpts mapped to suggested field keys.

- `pump.location.recommended`: “A… submersible water pump should be located… **bottom of the sump**… Gravity… lower the cost…” citeturn13view4  
- `pump.turnover_target.rearing_tank`: “Rearing tank – **1 hour (UVI system – 1.37 hours)**.” citeturn1view0  
- `pump.flow_anchor.per_tank`: “Water is pumped… **25 gallons/minute (100 l/min)**… full volume exchange every **1:20 hrs**.” citeturn20view0  
- `aeration.do_setpoint_warmwater`: “DO… maintained… above **60 percent of saturation or above 5 ppm**…” citeturn13view0  
- `aeration.do_min_nitrifiers`: “Nitrifying bacteria become inefficient… below **2 ppm**.” citeturn13view0  
- `aeration.ops_continuous`: “Aeration systems must operate **continuously**…” citeturn13view0  
- `alarm.DO_low_actions`: “Low dissolved oxygen (**less than 5 ppm**)… **increase aeration**… **stop feeding** until corrected.” citeturn13view2  
- `alarm.CO2_high_actions`: “High carbon dioxide (**above 20 ppm**)… add air stripping column… increase aeration.” citeturn13view2  
- `indicator.low_DO_behaviour`: “Crowding around water inflow/aerators… possible cause: **low oxygen**… check dissolved oxygen…” citeturn13view1  
- `failure.supersaturation_zones`: “Zones of supersaturation can cause gas bubble disease… Fry are particularly sensitive…” citeturn13view0  
- `DWC.air_stone_density`: “Air stones… **one for every 10 square feet**.” citeturn13view3  
- `power_backup.UVI_generator_procedure`: “Install generator… **monthly service**… **weekly** automatic… exercise… **phone alarm**… mobile generator…” citeturn1view0  
- `failure.NFT_flow_disruption`: “With NFT, a disruption in water flow can lead quickly to **wilting and death**.” citeturn11view0  

## Starter simulation hooks for pump and aeration effects

These hooks are intended to translate the corroborated rules into **minimal functional dynamics** for Layer 1 simulation. They deliberately use the *observed/target exchange rate anchors and DO thresholds* rather than overfitting to any single facility.

### Pump-driven hydraulics

A simple, simulation-ready representation is to treat each major vessel (rearing tank, clarifier, hydroponic tank) as a well-mixed volume with **turnover time** τ and flow Q:  
- Use UVI anchors for τ in commercial coupled systems: **~1 hour** nominal, with observed values **~0.8–1.37 hours** and CAS example **~1:20 hours**. citeturn1view0turn20view0turn2view1  
- Implement **pump off / pump degraded** as an immediate change in τ (τ → ∞ for off, τ increases for degraded), which then delays export of TAN/CO₂ and solids from rearing tanks and delays delivery of oxygenated/treated water. The UVI narrative explicitly links high exchange to quick removal of wastes. citeturn2view1turn11view0  

A minimal “hydraulic stability” metric can be:  
- `exchange_rate = 1/τ`  
- When `exchange_rate` falls below a configured threshold (e.g., below the nominal **1-hour target**), trigger risk escalations: increasing local TAN/NO₂ and decreasing uniformity of DO distribution. citeturn1view0turn13view0  

### Aeration and dissolved oxygen dynamics

Represent DO as a balance between **oxygen transfer** and **oxygen demand**:

- Use SRAC operating doctrine to encode thresholds:  
  - `DO_target` for warmwater fish growth: **≥5 mg/L** (or ≥60% saturation). citeturn13view0  
  - `DO_min_nitrification`: **2 mg/L** (below this nitrifiers become inefficient). citeturn13view0  
  - `DO_alarm_low`: **<5 mg/L** triggers “increase aeration; stop feeding until corrected”. citeturn13view2  

- Model nitrification as DO-limited:  
  - If `DO < 2 mg/L`, scale nitrification capacity down sharply (e.g., linear or Hill-type drop), reflecting “inefficient” nitrifiers. citeturn13view0  

- Encode behavioural warning signals as observables:  
  - If `DO` is low, fish may crowd around inflows/aerators or gulp at the surface; in simulation these behaviours can be emitted as warning events before mortality. citeturn13view1turn13view0  

### Interaction between circulation and aeration

Two interaction hooks are directly supported:

- **Mixing requirement for oxygen delivery:** when oxygen is injected or concentrated oxygenated flow enters the tank, SRAC stresses rapid mixing by currents from pumping equipment. Therefore, effective oxygen transfer to the bulk tank can be modelled as reduced when the pump/mixing is degraded. citeturn13view0  
- **DWC aeration vs exchange trade-off:** UVI states deep flow channels are “unimportant as long as they are aerated,” but unaerated channels require faster exchange. This can be encoded as:  
  - If `DWC_aeration = on`, relax minimum channel exchange constraint;  
  - If `DWC_aeration = off`, enforce a stricter channel turnover requirement to prevent root-zone hypoxia. citeturn1view0  

### Failure mode library

Implement these discrete events with strong trigger logic:

- `power_failure`: immediately sets `pump_state=off` and `aeration_state=off` unless protected by backup power; hazard increases rapidly because SRAC requires continuous aeration and UVI explicitly requires generator-backed continuity. citeturn13view0turn1view0  
- `pump_failure_flow_disruption_NFT`: if NFT is present and pump off, trigger rapid “plant water stress” progression, consistent with “wilting and death” language. citeturn11view0  
- `supersaturation_zone_risk`: if oxygen injection is high and mixing is low, increase gas bubble disease risk (especially for fry). citeturn13view0  

### Maintenance and operational scheduling primitives

Use UVI’s operational patterns as schedulable tasks:

- `generator_weekly_exercise` and `generator_monthly_service` as preventive maintenance events to reduce probability of backup failure; `phone_alarm_system` as a monitoring primitive that reduces detection delay. citeturn1view0  
- `DO_monitoring_before_after_feeding` as a routine schedule, with increased risk weighting during heavy feeding periods. citeturn13view0