# Tilapia feed-regime and stocking-input research pack for a first fish-feed-to-water-quality MVP

## Executive summary

The strongest first-pass conclusion is that **Mode A — direct `feed_kg_per_day` as a scenario input — is sufficient and safer for first implementation**. Multiple high-trust sources treat **daily feed input** as the core operational driver of waste generation, water-quality loading, and even system capacity. FAO’s Nile tilapia profile states that in recirculating systems the **maximum daily feed input is a better indicator of productivity and efficiency than final standing crop**, while aquaponic nitrogen reviews use feed rate and protein fraction directly to approximate TAN generation. citeturn6view1turn28view0

**Mode B — biomass-derived feeding — is supportable, but only as a second path**. It requires fish count, average fish weight, a stage/size-specific feeding-rate table, feed class or protein fraction, and regular re-weighing or other biomass updates. The same manuals that provide feeding tables also warn that they are only guidelines and shift with species, temperature, appetite, water quality, and management. citeturn15view0turn11view2turn6view0turn35view0

For **tilapia grow-out in tank/RAS/aquaponic contexts**, the most defensible starting assumptions are **context-split**, not universal:  
- feed rate declines strongly with fish size, roughly from **6–4% BW/day at 5–20 g** to **2–1.5% BW/day above 250 g** in intensive systems;  
- grow-out protein commonly sits around **30–32%** for adults, with **32%** used in the UVI DWC/raft aquaponic benchmark and broader tank/cage guidance spanning roughly **30–35%** depending on stage and production context;  
- **FCR around 1.4–1.8** is common in intensive tank culture, while aquaponic studies show context-dependent results from about **1.46–1.88** in NFT fingerlings and **0.9–1.4** in one integrated experimental system with high-energy feed;  
- **stocking density cannot be hard-coded** because aquaponic trials, commercial aquaponics, and intensive RAS operate at very different biomass levels and hardware intensities. citeturn37view0turn36view0turn21view0turn17view3turn11view2turn34view0turn19search11turn16view1turn6view1

For the MVP calculation chain, the strongest evidence-backed path is:

`feed_kg_per_day` + `feed_protein_fraction` → `PTAN_kg_per_day`  
then add `tank_or_system_water_volume`, `time basis`, `exchange / retention`, `biofilter conversion assumption`, `pH`, and `temperature` to estimate **TAN concentration** and **NH3 risk**. TAN alone is not enough for toxicity assessment; both Texas A&M aquaponics guidance and SRAC RAS guidance explicitly require **pH and temperature** to interpret ammonia toxicity. citeturn28view0turn30view0turn14view0

This pack supports the fish/feed/waste side of the MVP. It does **not** resolve basil saleable harvest output and should not be used to infer it. citeturn21view0turn28view0

## Evidence hierarchy and context split

### Evidence hierarchy

The most reliable evidence used here comes from:
- **FAO / AFFRIS Nile tilapia tables and species profile**, for protein requirements, feeding tables, and RAS production anchors. citeturn36view0turn37view0turn6view1
- **SRAC / NCRAC recirculating tank manuals**, for tank-culture feeding schedules, density anchors, feed conversion, ammonia from feed, and operational warnings. citeturn15view0turn17view3turn14view0turn29view0
- **WorldFish manuals and briefs**, for Nile tilapia protein ranges, cage/intensive grow-out feeding ranges, FCR interpretation, feed-management cautions, and water-quality links to feeding. citeturn4view3turn4view4turn11view2turn6view0
- **UVI aquaponic system documents**, for commercial aquaponic operating practice and daily-feed-input coupling to plant area. citeturn21view0turn21view2
- **Open-access aquaponic studies**, for aquaponics-specific stocking-density and feeding-schedule effects. citeturn8view0turn34view0turn35view0

Lower-priority evidence used only with caveats:
- **manufacturer feed specifications** via FAO compilation, used only to characterise commercial feed classes, not as universal biological defaults. citeturn11view3
- **historical feed-price tables** and extension examples, used only to show why feed cost must remain a scenario/business input. citeturn25search2turn23search2

### Context split notes

#### Pond
Pond systems are partly supported by natural productivity, so feeding rates, protein requirements, and FCRs from ponds do **not** transfer cleanly into tank/RAS/aquaponics. FAO and WorldFish both show pond and semi-intensive contexts using lower-protein or partially satiation-based feeding because fish obtain part of their nutrition from the pond biota. citeturn4view4turn17view1

#### Cage
Cage culture is closer to complete-feed dependence than ponds, but it still does not equal indoor RAS or aquaponics. WorldFish’s cage guidance still provides useful FCR, feed-class and feed-management evidence, while also warning that appetite changes with weather and water quality. citeturn11view2turn6view0

#### Tank
Tank culture evidence is directly relevant for the MVP. SRAC tank culture guidance links fish size to feeding rate, density, oxygen use, solids management, and carrying capacity. It also warns that high tank densities create severe vulnerability to power or aeration failure. citeturn15view0turn16view1turn15view2

#### RAS
RAS evidence is highly relevant for the feed-to-waste engine. FAO’s cultured-species profile explicitly treats **maximum daily feed input** as the better capacity indicator, gives RAS standing-crop ranges, and notes short retention times and daily make-up water exchange. SRAC also ties feeder management directly to biofilter load, DO shocks, and ammonia generation. citeturn6view1turn29view0turn14view0

#### Aquaponics
Aquaponics adds plant uptake and feed-to-plant coupling, but the nitrogen source still starts with feed. UVI’s basil DWC system explicitly frames nutrient balance around the ratio of **daily fish feed input to plant growing area**, while aquaponic nitrogen reviews express TAN generation directly as a function of feed rate and feed protein. citeturn21view0turn28view0

#### Nile tilapia versus generic tilapia
Many of the strongest nutrient requirement tables are **Nile tilapia-specific**, while SRAC tank culture guidance is written for tilapia more broadly. Because Nile tilapia is the predominant cultured tilapia species worldwide, Nile-specific nutrient tables are the best anchor. However, species/strain differences still matter operationally: in the UVI commercial aquaponic context, Nile and red tilapia were run at different stocking rates in the same system family. That means **species/strain should remain a scenario input whenever the claim is operational rather than purely nutritional**. citeturn18search0turn36view0turn21view0turn20search1

## Feeding-rate, protein, FCR, and stocking evidence

### Feeding-rate table by fish size or stage

| fish size or life stage | feeding rate basis | source | context | confidence | recommended use |
| --- | --- | --- | --- | --- | --- |
| Early fry 0–1 g | 30–10% BW/day, up to 8 feeds/day | FAO AFFRIS Table 28 citeturn37view0 | intensive tanks/ponds; hatchery phase | high | nursery/hatchery only; not a grow-out default |
| Fry 1–5 g | 10–6% BW/day, 4 feeds/day | FAO AFFRIS Table 28 citeturn37view0 | intensive cages/tanks/ponds | high | use only for fry scenarios |
| Fingerling 5–20 g | 6–4% BW/day | FAO AFFRIS Table 28 citeturn37view0 | intensive cages/tanks/ponds | high | strong stage-specific default candidate |
| Juvenile 20–100 g | 4–3% BW/day | FAO AFFRIS Table 28 citeturn37view0 | intensive cages/tanks/ponds | high | strong stage-specific default candidate |
| Grower 100–250 g | 3–2% BW/day | FAO AFFRIS Table 28 citeturn37view0 | intensive cages/tanks/ponds | high | strong grow-out default candidate |
| Larger grow-out >250 g | 2–1.5% BW/day | FAO AFFRIS Table 28 citeturn37view0 | intensive cages/tanks/ponds | high | strong finisher/default anchor |
| Generic warmwater food-fish grow-out | fingerlings 3–4% BW/day until about 113–227 g; then 2–3% BW/day to 454–907 g harvest | SRAC 0452 citeturn15view0turn15view1 | recirculating tank culture | medium-high | corroborating warmwater/tank baseline; useful when fish are weighed in pounds or grams |
| Intensive cage grow-out | 6–10% BW/day for fish under 100 g; 3–6% for 100–250 g; 1.5–3% for 300–800 g | WorldFish manual citeturn4view4 | intensive pond/cage grow-out | medium | corroboration only; do not flatten into RAS default |
| NFT aquaponic fingerlings | 4% BW/day, fed twice daily, 35% protein | MDPI NFT aquaponics study citeturn35view0 | NFT aquaponics, 13.5 g fingerlings at 6 kg/m³ | medium | aquaponics-specific operating point, not universal |
| UVI DWC/raft aquaponics | fed three times daily ad libitum; floating pellets, 32% protein | UVI tilapia–basil study citeturn21view0 | commercial DWC/raft aquaponics | medium-high | strong aquaponic operating benchmark, but ad libitum requires operator observation |

**Important operating caution:** feeding tables are **guidelines**, not hard defaults. SRAC states explicitly that its tables “should be used only as guidelines” and change with species and temperature. WorldFish and Texas A&M both note that feeding should be cut or adjusted when appetite drops or water quality worsens. citeturn15view0turn11view2turn6view0

### Feed protein table by feed class

| feed class | evidenced crude protein range | key source | context | confidence | recommended use |
| --- | --- | --- | --- | --- | --- |
| Pre-starter / first-feeding larvae | 45–50% requirement; commercial examples 40–45% | FAO nutrient requirement table; FAO commercial feed examples citeturn36view0turn11view3 | Nile tilapia larvae / commercial pre-starters | high for requirement; medium for product-class mapping | use only in hatchery path |
| Fry / starter | ~40% requirement; commercial starter examples often 30–40% | FAO nutrient requirement table; FAO commercial feed examples citeturn36view0turn11view3 | Nile tilapia fry / marketed starter feeds | high for requirement; medium for class mapping | strong nursery default candidate if fry path is ever modelled |
| Fingerling | 35–40% requirement; WorldFish reports 28–40% across authors; commercial examples around 31–40% | FAO and WorldFish citeturn36view0turn4view3turn11view3 | Nile tilapia fingerlings | high | strong fingerling protein band |
| Juvenile / pre-grower | 30–35% requirement | FAO nutrient requirement table citeturn36view0 | Nile tilapia juveniles 10–25 g | high | strong stage-specific default candidate |
| Grower / adult 25–200 g | 30–32% requirement; intensive tank feeds often 32–40%; WorldFish adult feed around 30% | FAO, SRAC, WorldFish citeturn36view0turn17view1turn11view2 | tank/RAS/aquaponic grow-out | high for requirement range; medium for exact commercial class | best first-pass grow-out protein anchor |
| Finisher / adult >200 g | 28–30% requirement; commercial finisher examples can range roughly 20–30% depending on brand and formulation | FAO nutrient requirement table and FAO commercial feed examples citeturn36view0turn11view3 | larger grow-out / finisher | medium-high | use as finisher band, not as a fixed default |
| Broodstock | 35–45% | FAO and WorldFish citeturn36view0turn4view3 | broodstock only | high | exclude from MVP grow-out defaults |
| General intensive aquaponic grow-out benchmark | 32% protein floating complete diet | UVI tilapia–basil and UVI update snippet citeturn21view0turn20search1 | DWC/raft commercial aquaponics | medium-high | strongest single aquaponic benchmark for MVP grow-out |

**Interpretation:** for a first grow-out-oriented MVP, **`feed_protein_fraction = 0.32` is a defensible scenario default candidate**, not canonical truth. It is well aligned with adult Nile tilapia requirement bands and with the UVI aquaponic operating benchmark. Fry and fingerling paths should use higher values and should not silently inherit the same default. citeturn36view0turn21view0turn11view2

### FCR guidance

| value or range | context | source | confidence | usable for first-pass defaults? |
| --- | --- | --- | --- | --- |
| 1.4:1–1.8:1 | common in tank culture of tilapia | SRAC 282 citeturn17view3 | high | yes, as a **scenario default candidate** for intensive tank/RAS grow-out |
| 1.5:1 estimate | warmwater recirculating schedule example at 84°F | SRAC 0452 citeturn15view0 | medium-high | yes, as a central planning assumption for demos |
| 1.5–2.0 | good indicator of effective feed use; >2 suggests poor feed use, wastage, high mortalities, or poor water quality | WorldFish cage brief citeturn11view2 | medium-high | yes, as an operating interpretation band |
| 1.46, 1.69, 1.88 | NFT aquaponics fingerlings at 3, 6, 9 kg/m³ respectively | MDPI NFT aquaponics study citeturn34view0 | medium | use only as aquaponics-specific context split |
| 0.9–1.4 | integrated aquaponics study using high-energy feed | Water 2019 study snippet citeturn19search11 | medium-low to medium | do not use as a generic default; too system-specific |

**Interpretation:**  
- For the MVP, **`expected_fcr = 1.5–1.8`** is well-supported enough for scenario work in tank/RAS-like grow-out. citeturn17view3turn15view0  
- FCR should remain a **scenario input or validated assumption**, not a hard-coded canon value, because it shifts with density, feed composition, fish size, environment, and survival. citeturn34view0turn35view0turn19search10

### Stocking-density and tank-volume guidance

| guidance | fish size/stage context | source | confidence | use in MVP |
| --- | --- | --- | --- | --- |
| ~30 kg/m³ baseline maximum in highly aerated systems; some operators 60–72 kg/m³ | generic tilapia tank culture | SRAC 282 citeturn16view1 | high | use as a **warning anchor**, not a universal default |
| 60–120 kg/m³ with supplemental oxygen and good solids control | intensive tank/RAS | SRAC 282 and FAO species profile citeturn16view1turn6view1 | high | use only when strong aeration/oxygenation and filtration assumptions are explicit |
| production levels in recirculating systems 60–120 kg/m³ or more | RAS | FAO Nile tilapia profile citeturn6view1 | high | RAS capacity anchor; not small aquaponic default |
| replace 100% of tank water every 90–120 min in flow-through designs | flow-through tanks | SRAC 282 citeturn16view0 | high | useful only if modelling flow-through analogues |
| RAS retention time around one hour; 5–10% of system volume replaced daily | recirculating systems | FAO Nile tilapia profile citeturn6view1 | high | strong system-volume / dilution anchor |
| UVI CAS total volume 110,000 L; four 7,800 L rearing tanks; full tank exchange every 1:20 h; 50 g to 900 g over 24 weeks | commercial DWC/raft aquaponics | UVI CAS page citeturn21view2 | high | strong aquaponic benchmark |
| Nile tilapia fingerlings stocked at 77 fish/m³ and fed 32% protein, three times daily ad libitum | commercial DWC/raft aquaponics | UVI tilapia–basil paper and UVI update snippet citeturn21view0turn20search1 | medium-high | useful benchmark, but not universal |
| 3, 6, 9 kg/m³ tested; 6 kg/m³ recommended as balance in NFT fingerling aquaponics | NFT aquaponics, fingerlings | MDPI NFT study citeturn34view0 | medium | strong small-system NFT context split |
| 150, 300, 450 fish/m³ tested; lower density gave better fish growth and lower FCR | aquaponic fingerling study with lettuce | Aquaculture and Fisheries 2022 abstract citeturn8view0 | medium | corroborates “higher density worsens fish performance” in aquaponics |

**Interpretation:** stocking density must remain a **scenario input** with context tags such as `small_aquaponics_fingerlings`, `commercial_dwc_raft`, or `intensive_ras_with_supplemental_oxygen`. The evidence is strong that density depends on stage, hardware, oxygenation, and whether the objective is fish growth, plant nutrient supply, or both. citeturn34view0turn8view0turn16view1turn6view1

## Inputs needed for Mode A, Mode B, TAN concentration, and NH3 risk

### Inputs needed for biomass-derived feeding

The evidence-backed minimum inputs for **Mode B** are:

- `fish_count`
- `average_fish_weight_g`
- `fish_biomass_kg`
- `feeding_rate_fraction_per_day`
- `feed_protein_fraction`
- `feed_class`
- ideally `water_temperature`
- ideally `feeding_frequency_per_day`
- ideally periodic re-weighing / resampling of biomass

SRAC provides the direct operational method: sample fish, estimate total biomass, then calculate the new daily feed rate from the relevant **percent body weight consumed per day**. citeturn15view3

A defensible derived chain is:

- `fish_biomass_kg = fish_count × average_fish_weight_g / 1000`
- `feed_kg_per_day = fish_biomass_kg × feeding_rate_fraction_per_day`

That chain is directly implied by SRAC’s biomass-based feed calculations and by FAO/WorldFish feeding tables expressed as percent of body weight per day. citeturn15view3turn37view0

### Inputs needed for TAN concentration and NH3 risk

The minimum evidence-backed inputs are:

- `feed_kg_per_day`
- `feed_protein_fraction`
- `tank_water_volume_m3` and/or `system_water_volume_m3`
- `accumulation_period` or modelling timestep
- `exchange_rate` or `retention_time`
- `biofilter_conversion_assumption` or `nitrification_capacity`
- `pH`
- `water_temperature`
- preferably `dissolved_oxygen`
- preferably `alkalinity`

The most defensible first-pass TAN generation relation in aquaponics is:

- `PTAN_kg_per_day = feed_kg_per_day × feed_protein_fraction × 0.092`

This comes directly from the aquaponic nitrogen review citing Ebeling and Timmons. citeturn28view0

Texas A&M aquaponics guidance is explicit that **TAN alone reveals nothing about toxicity**; **pH and temperature must also be known** to calculate unionised ammonia. It also notes that unionised ammonia can spike quickly after feeding in limited-volume systems. citeturn30view0

### Practical interpretation for the engine

#### What Mode A needs
Mode A can run with:
- `feed_kg_per_day`
- `feed_protein_fraction` or `feed_class`
- `system_water_volume`
- `time basis`
- `pH`
- `temperature`
- `biofilter_state`
- `exchange / retention`
- optional `DO` and `alkalinity`

That is enough to estimate:
- TAN production rate
- simple TAN accumulation risk
- NH3 risk band
- biofilter oxygen / alkalinity demand warnings
- feed-linked aeration warnings

This is why Mode A is the best first implementation path. citeturn28view0turn30view0turn14view0turn6view1

#### What Mode B adds
Mode B adds the fish-biomass estimation layer and requires:
- a valid size/stage feed table
- operator or scenario choice of feeding regime
- ongoing fish biomass updates
- temperature / appetite adjustment logic
- stronger validation against real farm practice

That makes it useful, but less safe as the very first path. citeturn15view0turn11view2turn35view0

### Feed-management findings that matter to the engine

- **Poor feeding response is an alarm**. SRAC says a sudden reduction in feeding response should trigger immediate checks of system and water quality. citeturn29view0
- **Multiple feedings reduce acute load spikes**. SRAC states that multiple feedings spread the waste load on the biofilter and help prevent sudden DO decreases. citeturn29view0
- **Feeding and water quality are tightly linked**. WorldFish advises restricting or stopping feed when appetite is poor or water quality declines. Texas A&M notes unionised ammonia can rise quickly after feeding in small-volume aquaponics. citeturn11view2turn30view0
- **Temperature changes feed intake**. WorldFish notes that low temperature reduces feeding and high temperature can reduce DO and worsen mortality risk. citeturn6view0

## What can be used now, what must stay configurable, and what belongs in the economics layer

### Scenario-default candidates

#### strong_default_candidate
- `input_mode = direct_feed_kg_per_day` for first implementation. citeturn6view1turn28view0
- `ptan_formula = feed × protein × 0.092`. citeturn28view0
- `nh3_requires = TAN + pH + temperature`. citeturn30view0turn14view0
- `multiple_small_feedings_reduce_load_spikes = true` as a qualitative rule. citeturn29view0

#### scenario_default_candidate
- `feed_protein_fraction = 0.32` for market-stage grow-out in intensive tank/RAS/aquaponic contexts, with override expected. citeturn36view0turn21view0turn11view2
- `expected_fcr_band = 1.5–1.8` for intensive grow-out planning. citeturn17view3turn15view0
- `feeding_rate_band_above_250g = 0.015–0.02` BW/day. citeturn37view0
- `feeding_rate_band_100_to_250g = 0.02–0.03` BW/day. citeturn37view0

#### operator_input_required
- actual `feed_kg_per_day`
- actual `fish_count`
- actual `average_fish_weight_g`
- actual `stocking_density`
- `tank_volume` and `system_volume`
- `feed_class`
- `feed_protein_fraction` if known from label
- `pH`, `temperature`, `DO`
- `feeding_frequency`
- `biofilter_status`
- `water_exchange` / `retention_time`

#### customer_validation_required
- whether the system behaves like **small NFT aquaponics**, **commercial DWC/raft aquaponics**, or **intensive RAS**
- species/strain used: Nile, red, hybrid, or generic tilapia
- actual feeding practice: ad libitum, fixed ration, fasting cycle, or sensor/feeder based
- target fish size and harvest cadence
- whether feed label protein is known and stable over time
- aeration / oxygenation / backup power provisions

#### do_not_use_yet
- one universal stocking-density default
- one universal FCR default across pond, cage, RAS, and aquaponics
- one universal feed protein default for all stages
- feed-cost canon
- any conversion from fish standing biomass to basil saleable output

### Values that must remain scenario inputs

These should **not** be embedded as canonical biological truths yet:
- `stocking_density`
- `feeding_rate_fraction_per_day`
- `feed_class`
- `feed_protein_fraction` beyond stage-specific default suggestions
- `fcr`
- `biofilter_conversion_efficiency`
- `uneaten_feed_fraction`
- `water_exchange_rate`
- `system_volume`
- `fish_mortality_rate`

The evidence is strong that these change with stage, system type, hardware, and management. citeturn15view0turn16view1turn34view0turn35view0

### What can be used before first implementation

Use now:
- Mode A direct feed input path
- stage-based protein defaults
- PTAN generation from feed and protein
- NH3 risk only when pH and temperature are present
- qualitative rules linking feeding to DO/biofilter load
- density warning bands split by context

These are well supported and sufficient for a first demo without pretending to know saleable basil output. citeturn28view0turn30view0turn29view0turn6view1

### What can wait for the economics layer

- local feed price
- local labour cost of feeding
- equipment depreciation related to feeding or aeration
- channel-specific fish pricing
- customer-specific feed procurement assumptions

These are business inputs, not biology defaults. citeturn11view2turn25search2turn23search2

### What can wait for customer or discovery validation

- whether customers want Mode B at launch
- which feed classes they routinely buy
- whether they can actually supply reliable biomass estimates
- what level of density warning granularity is credible for customer-facing outputs
- whether culture is run at satiation, fixed ration, or fasting cycles

## Feed-cost evidence, clearly separated from biology

### Feed-cost evidence

| source | geography | date basis | market level | product class | usable only as scenario/business input? |
| --- | --- | --- | --- | --- | --- |
| WorldFish cage-feeding brief says feed contributes about 60% of total operating cost | Ghana/Nigeria-oriented brief, but framed as general cage guidance | 2022 publication | operating-cost share, not price per kg | commercial tilapia feed | yes citeturn11view2 |
| WorldFish manual says feed is the main operating cost and can exceed half of farmgate price/gross revenue in intensive aquaculture | Africa-focused Nile tilapia manual | 2023 publication | operating-cost share, not price per kg | intensive aquaculture feed | yes citeturn4view0 |
| Texas A&M aquaponics fish-selection quick fact cites a typical 32% fish feed at about USD 485/ton in bulk or USD 15–18 per 40 lb bag, but uses it as a nitrate-cost comparison example rather than a tilapia feed market study | United States | publication era ~2020 | bulk / bagged extension example | 32% fish feed | yes, illustration only citeturn23search2 |
| FAO historical commercial feed table for the Philippines shows indicative tilapia starter/grower/finisher feed prices around roughly USD 0.47–0.56/kg, with USD 1 = PHP 26 stated in the table | Philippines | historical; clearly not current | indicative feed-table pricing | starter/grower/finisher | yes, historical only citeturn25search2 |

### Feed-cost conclusion

There is **not enough current, high-confidence, RAS/aquaponics-specific feed-price evidence** in the high-trust literature gathered here to justify a canonical feed-cost number. Feed cost should remain a **scenario/business input** tied to geography, date, supplier class, and feed class. What *is* strongly supported is that feed is usually one of the dominant operating costs and should be separated cleanly from biology defaults. citeturn11view2turn4view0turn23search2turn25search2

## Direct answers, open questions, and recommended next repo-side use

### Direct answers to the key implementation questions

#### Is Mode A, direct `feed_kg_per_day`, sufficient for first implementation?
**Yes.** It is the safest and best-supported first path. Daily feed input is the most direct measurable driver of TAN generation and an important system-capacity indicator in RAS and aquaponics. citeturn6view1turn28view0

#### Is Mode B, biomass-derived feeding, sufficiently supported for first implementation?
**Yes, but only as a secondary path.** It is sufficiently supported only if the scenario also supplies fish biomass, stage/size class, feeding-rate table selection, and regular biomass updates. Without those, it becomes too assumption-heavy. citeturn15view3turn15view0turn35view0

#### Which values are needed before concentration/NH3 risk can be implemented?
At minimum:
- `feed_kg_per_day`
- `feed_protein_fraction`
- `system_or_tank_volume`
- `timestep / accumulation period`
- `exchange_rate` or `retention_time`
- `biofilter_conversion_assumption`
- `pH`
- `temperature`

Preferably add:
- `DO`
- `alkalinity`

That is because TAN production is feed-linked, while NH3 toxicity depends on TAN plus pH and temperature. citeturn28view0turn30view0turn14view0

#### Which values are needed before feed-cost economics can be implemented?
At minimum:
- local `feed_price_per_kg`
- `feed_class`
- `protein_fraction`
- `market level / pack size`
- `currency`
- `date basis`
- geography
- any wastage/shrink assumption if feed spoilage or fines are modelled

None of these should be pulled from biological defaults. citeturn23search2turn25search2turn11view2

#### What should be customer-validated before seed-demo claims?
- actual feeding regime
- actual fish biomass and density
- actual system volume
- actual pH/temperature measurement practice
- actual aeration/backup capability
- actual feed label protein
- actual biofilter maturity/state

These variables materially change water-quality risk and cannot safely be assumed away in customer claims. citeturn29view0turn30view0turn16view1turn14view0

#### What is the safest minimum viable input set for a first demo?
The safest minimum viable set is:
- `feed_kg_per_day`
- `feed_protein_fraction` or `feed_class`
- `system_water_volume`
- `pH`
- `water_temperature`
- `biofilter_state`
- `basic_exchange_or_retention_anchor`
- preferably `DO`

This supports TAN generation, NH3 warning logic, and biofilter/aeration warning labels without having to infer fish biomass. citeturn28view0turn30view0turn6view1

#### Which values should never be hard-coded as canon yet?
- stocking density
- FCR
- feeding-rate schedule
- feed cost
- protein fraction outside stage-specific default bands
- biofilter conversion efficiency
- uneaten-feed fraction
- survival/mortality rate

These all vary too much by context. citeturn15view0turn16view1turn34view0turn35view0

### Recommended next repo-side use

In a later design or Codex pass, the safest use of this research would be:

- treat **Mode A** as the MVP baseline input path;
- allow **Mode B** only as an advanced path with explicit stage and biomass inputs;
- store feeding-rate guidance as **context-split tables**, not one master value;
- store feed protein as **stage/class bands** with a grow-out scenario default candidate near **32%**;
- store FCR as a **scenario assumption band**, not a canon constant;
- require `pH` and `temperature` before surfacing any NH3 risk label;
- keep `stocking_density` and `feed_cost` explicitly configurable;
- keep basil saleable output unresolved unless observed or manually reviewed.

All of those uses are strongly aligned with the evidence gathered here. citeturn36view0turn21view0turn17view3turn28view0turn30view0

### Open questions and limitations

The main unresolved items are:

- A good **first-pass solids-load coefficient** tied to feed mass, digestibility, and uneaten feed fraction; this pass did not gather enough high-confidence tilapia/RAS-specific solids-partition evidence to recommend one coefficient.
- A better **aquaponics-specific grow-out FCR range** for commercial DWC/raft tilapia rather than fingerling-focused research systems.
- More direct evidence for **species/strain-conditioned feeding** differences beyond Nile-versus-generic tilapia and UVI’s Nile-versus-red operational split.
- Better current, region-specific **commercial feed cost** evidence suitable for later business inputs.
- Customer discovery on whether operators can reliably supply `feed_kg_per_day` and/or biomass estimates.

Those are the main blockers before expanding from first-pass biology/loading logic into richer operational and economic modelling.