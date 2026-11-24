# Aeration Capacity and Solids Load Translation Research Pack for the Aquaponics MVP

## Executive summary

The strongest high-trust conclusion is that your current Mode A path can validly estimate **nitrification oxygen demand**, but it still does **not** estimate **total oxygen risk**. In authoritative RAS guidance, total oxygen demand is the sum of **fish respiration**, **oxygen demand from bacteria decomposing retained organic wastes and uneaten feed**, and **nitrification**. SRAC 451 gives a practical whole-system envelope of about **0.3 to 0.75 kg O₂ per kg feed added**, depending largely on whether solids are removed quickly and whether the biofilter is submerged. That makes nitrification oxygen demand an important sub-load, but not the entire aeration requirement. citeturn17view0turn10view0

For warmwater tilapia/RAS contexts, the strongest operating anchor remains **DO above 5 mg/L**, with SRAC 282 recommending **5.0–7.5 mg/L**, chronic growth/feed-conversion impacts below **3.5 mg/L**, and short-term survival at much lower values only under brief exposure. SRAC 452 independently recommends maintaining DO above **60% saturation or 5 ppm** for optimum warmwater fish growth, while also stating nitrifying bacteria become inefficient below **2 ppm**. WorldFish corroborates the warmwater tilapia view that DO should be **above 5 mg/L**, and not below **2 mg/L** in early morning monitoring. citeturn12view6turn8view2turn7view7

For the DWC/raft side, the evidence is also strong that **root-zone aeration cannot be treated as automatically covered by fish-tank aeration**. SRAC 454 states that long, deep flowing channels must be aerated with diffused air stones, SRAC 5007 recommends **one air stone per 10 square feet** in float beds, and the UVI commercial raft system used a **separate hydroponic blower** plus air stones through the raft channels; in that system, DO increased from **4.0 to 6.9 mg/L** as water passed through the hydroponic tanks. citeturn7view8turn8view0turn13view1

For solids, the strongest aquaponics-specific anchor is UVI’s rule that **at least 25% of feed becomes solid waste on a dry-weight basis**, with the wet sludge mass being much greater. UVI also states that solids should be removed before they enter the hydroponic component because they adhere to roots, create anaerobic zones, impair nutrient and water uptake, affect nitrifying bacteria, consume oxygen as they decompose, and produce ammonia. In UVI’s commercial-scale work, clarifier detention around **20 minutes** performed better than **9.5 minutes**, clarifier sludge was removed **three times daily**, and filter media were cleaned **once or twice weekly**. citeturn12view0turn12view1turn13view2turn22search9

Operationally, the strongest first-pass design implication is this: the MVP can move beyond “nitrification oxygen alone” by adding a **declared aeration-capacity basis**, a **provisional feed-based total oxygen envelope**, and **solids-removal context flags**, while continuing to emit warning labels whenever fish respiration, real transfer efficiency, DWC root-zone aeration, or solids-removal capacity are not actually specified. That approach stays evidence-backed without pretending to know more than the current inputs support. citeturn19view2turn19view1turn18view1turn17view0

## Evidence hierarchy and context splits

This pass starts from your uploaded **pumps and aeration**, **tilapia**, and **water chemistry** corroboration reports as prior synthesis, then re-checks the load-bearing claims against primary and near-primary sources. fileciteturn0file3 fileciteturn0file4 fileciteturn0file5

The highest-weight sources used here are SRAC publications hosted by university or official extension sites, the official UVI aquaponics pages and UVI commercial-system paper, the WorldFish water-quality brief, UF/IFAS hydroponic guidance, the Kentucky e-GRO root-disease guidance, and the peer-reviewed Ebeling–Timmons–Bisogni stoichiometry paper. Those sources cover, respectively, warmwater fish DO targets, nitrifier DO sensitivity, practical aeration/backup rules, DWC/raft aeration patterns, clarifier retention anchors, feed-to-solids translation, and the stoichiometric link between feed, TAN, oxygen demand, and alkalinity demand. citeturn8view2turn28view2turn13view1turn12view0turn23view0turn23view1turn10view0

The most important context splits are these. In **tank/RAS** contexts, fish safety and system stability dominate, so DO thresholds, backup capacity, response time, and gas transfer efficiency matter most. In **DWC/raft aquaponics**, the hydroponic component can also act as a treatment and re-aeration zone, but only if it is actually aerated and protected from solids loading. In **small aquaponics**, SRAC gives simple practical rules such as one air stone per 10 square feet of float bed and biofilter DO above 5 ppm. In **commercial aquaponics**, UVI provides the strongest operational pattern: separate fish and hydroponic blowers, ~20-minute clarifier detention, daily clarifier purging, weekly filter cleaning, and explicit power-backup practices. citeturn8view0turn8view1turn7view3turn28view0

## Threshold and capacity tables

**DO threshold table**

| Value or rule | Organism or process affected | Context | Confidence | Recommended use |
|---|---|---|---|---|
| **5.0–7.5 mg/L recommended** | Tilapia growth and production | Tank culture / warmwater RAS-like | High | Strong warmwater fish operating target for the MVP. SRAC 282 recommends this range and notes chronic effects below 3.5 mg/L. citeturn12view6turn12view7 |
| **Above 60% saturation or above 5 ppm** | Warmwater fish growth | General recirculating warmwater systems | High | Good generic RAS threshold if species-specific DO target is missing. citeturn8view2 |
| **Below 3.5 mg/L chronic** | Tilapia growth and feed conversion | Tank culture | High | Use as a growth-penalty anchor rather than an immediate-mortality trigger. citeturn12view6turn12view7 |
| **Below 2 mg/L** | Nitrifying bacteria efficiency | RAS biofilter | High | Strong nitrifier warning floor. This is the cleanest process-specific DO threshold in the source set. citeturn8view2turn8view3 |
| **More than 5 ppm** | Biofilter performance | Small-scale aquaponics | High | Use when a separate biofilter tank is present. citeturn8view1 |
| **Above 5 mg/L; early morning not below 2 mg/L** | Tilapia survival and feeding behaviour | Cage / pond monitoring brief | Medium | Good corroborating fish-behaviour anchor; use as supporting context, not as the sole warmwater RAS target. citeturn7view7 |
| **5 mg/L in nutrient solution** | Root-zone oxygenation | Small hydroponic lettuce systems | Medium | Reasonable hydroponic baseline proxy for oxygenated nutrient solution; not basil-specific and not aquaponics-specific. citeturn23view0 |
| **Saturated DO around 8 ppm reduces Pythium survival** | Root disease pressure | DWC hydroponic leafy-greens proxy | Medium | Useful disease-pressure anchor for DWC root zones; proxy evidence, not basil-specific canon. citeturn23view1 |

The threshold picture is consistent: use **5 mg/L** as the practical warmwater fish floor, **3.5 mg/L** as the chronic-growth warning for tilapia, and **2 mg/L** as the nitrifier inefficiency warning. Treat root-zone DO targets as a separate hydroponic/DWC layer, not as a by-product of fish-tank aeration. citeturn12view6turn8view2turn23view0turn23view1

**Aeration and oxygenation capacity guidance table**

| Value or rule | Equipment or system context | Confidence | Recommended use |
|---|---|---|---|
| **Total O₂ demand = fish respiration + oxygen demand from breakdown of organic wastes/uneaten feed + nitrification** | General RAS | High | This is the core conceptual split the MVP should preserve. Do not equate nitrification oxygen demand with total oxygen demand. citeturn17view0 |
| **~0.3 kg O₂ per kg feed** | Non-submerged biofilters, solids removed quickly | High | Strong feed-based lower-envelope for rough total oxygen demand. Good for provisional context checks. citeturn17view0 |
| **Up to ~0.75 kg O₂ per kg feed** | Submerged biological filters, solids retained between backwashings | High | Strong feed-based upper-envelope for rough total oxygen demand when solids are retained longer. citeturn17view0 |
| **3 cfm air per lb daily feed ration** | Blown-air commercial growout | High | Practical airflow rule of thumb from SRAC 453; source also gives the metric equivalent of **187 lpm per kg feed/day**. Use as equipment-screening heuristic, not canon. citeturn28view2 |
| **4 cfm air per lb daily feed ration** | Airlift-based systems | High | Practical airlift rule of thumb; source also gives **249 lpm per kg feed/day**. Use when the scenario explicitly uses airlifts. citeturn28view2 |
| **Replace all oxygen in the system every 20–30 minutes at peak feeding** | Warmwater RAS under high loads | High | Strong operational capacity anchor for high-load RAS-like systems. citeturn8view7turn8view8 |
| **Backup response time under 20 minutes** | Large-scale RAS | High | Strong alarm/backup trigger. If backup capability is not declared, emit a separate risk warning. citeturn28view0turn28view1 |
| **SOTR = oxygen added in 1 hour under standard conditions; SAE = SOTR divided by horsepower** | Aerator performance rating | High | Best basis for comparing similar aerators, but not sufficient on its own for in-situ delivered oxygen. citeturn19view2turn19view1 |
| **Culture-tank air-stone diffusion in shallow tanks can be ≤40% oxygen absorption efficiency** | Common air stones in shallow tanks | High | Strong caution against pretending blower output equals oxygen transfer. citeturn18view2turn18view3 |
| **Properly designed pure-oxygen diffusion can exceed 90% absorption efficiency** | Oxygen injection systems | High | Use only when the scenario explicitly includes oxygenation equipment; not a default for simple aeration. citeturn18view2turn18view4 |
| **Atmospheric saturation in warm water rarely exceeds 8.75 mg/L; pure oxygen can increase saturation near 43 mg/L** | Warmwater oxygenation physics | High | Useful for interpreting why air-only systems cap out and why pure O₂ systems behave differently. citeturn18view4 |
| **Do not inject air deeper than about 5 feet** | Blown-air tank aeration | Medium to high | Practical gas-bubble-disease warning anchor in tank systems. citeturn28view2turn24view2 |

These anchors support a defensible MVP rule: **compare load against a declared capacity basis**, never against blower power alone. If the scenario only supplies “blower kW” or “air pump present”, capacity should remain unresolved and warning-only. citeturn19view1turn18view3turn28view2

**DWC and raft aeration guidance table**

| Value or rule | Raft or hydroponic context | Confidence | Recommended use |
|---|---|---|---|
| **Long, deep flowing channels must be aerated at intervals with diffused air through air stones** | SRAC aquaponics design guidance | High | Strong architecture rule for DWC/raft channels. citeturn7view8 |
| **One air stone per 10 square feet of float bed** | Small-scale raft systems | High | Strong small-scale spacing anchor. citeturn8view0 |
| **Hydroponic-channel exchange rate is unimportant as long as channels are aerated; unaerated channels need faster exchange** | UVI raft design guidance | High | Strong context split between aerated and unaerated DWC/raft. citeturn7view3 |
| **Separate hydroponic blower used** | UVI commercial raft system | High | Strong evidence that plant-side aeration is treated as its own subsystem, not assumed to be covered by fish-side aeration. citeturn7view5turn13view1 |
| **48 air stones per set of hydroponic tanks, spaced 1.22 m apart on the tank centreline** | UVI commercial raft system | High | Best commercial-scale DWC/raft geometry anchor in the current source set. citeturn13view0turn13view4 |
| **Water retained about 3 hours in hydroponic tanks** | UVI commercial raft system | High | Useful context variable for UVI-style demo assumptions. citeturn22search2turn13view2 |
| **DO increased from 4.0 to 6.9 mg/L through the hydroponic tanks** | UVI commercial raft system | High | Strong evidence that the raft component can actively re-aerate and mix water when designed that way. citeturn13view1 |
| **Roots need oxygen for healthy growth; sludge blocks flow and creates oxygen-poor zones** | Aquaponic hydroponic component | High | Strong biological reason to model separate root-zone oxygen risk. citeturn12view2turn7view8 |

The DWC/raft picture is unusually strong by aquaponics standards: there are both **simple small-scale rules** and a **commercial UVI reference pattern**. That makes DWC aeration one of the safer areas for initial scenario defaults as long as those defaults stay clearly labelled as **UVI-style** or **small-scale SRAC-style**, not universal. citeturn8view0turn13view1turn7view3

**Solids-load guidance table**

| Value or rule | Solids context | Confidence | Recommended use |
|---|---|---|---|
| **At least 25% of feed becomes solid waste on a dry-weight basis** | UVI aquaponics design rule | High for a practical aquaponic anchor | Best first-pass aquaponics solids coefficient in the source set; use as a provisional gross dry-solids potential, not as wet sludge or TSS concentration. citeturn12view0 |
| **Wet sludge mass is much greater** | Sludge handling | High | Strong caution against using dry-solids coefficients as wet-sludge mass. citeturn12view0 |
| **Waste solids classes: settleable, suspended, floatable, dissolved; settleable and suspended are the main RAS concern** | General RAS solids ontology | High | Good canonical category set for the business and warning layers. citeturn17view0 |
| **Settleable solids settle within about 1 hour under still conditions** | Clarification / settling behaviour | High | Strong definitional anchor for settler logic; not a complete sizing rule. citeturn17view0 |
| **Fecal solids and uneaten feed consume DO and generate ammonia if left in the system** | Organic loading | High | Strong reason to keep solids-removal state tied to both oxygen and TAN/NH₃ warning layers. citeturn17view0 |
| **Remove solids before hydroponics; solids on roots create anaerobic zones, impair uptake, affect nitrifiers, consume oxygen, and produce ammonia** | Aquaponic hydroponic component | High | Strong aquaponics-specific hazard statement. citeturn12view1turn12view2 |
| **In the UVI system, clarifiers removed about half of removed solids and filter tanks removed the other half** | UVI settleable vs suspended split | Medium to high | Useful context-specific split for a UVI-style scenario; do not promote as a universal solids fraction. citeturn14view2 |

**Solids-removal guidance table**

| Value or rule | Subsystem or maintenance context | Confidence | Recommended use |
|---|---|---|---|
| **Treat effluent first to reduce settleable and suspended solids, then remove ammonia/nitrate in a biofilter** | General aquaponic treatment sequence | High | Strong sequencing rule for the conceptual model. citeturn6search4turn6search5 |
| **Clarifier detention around 20 minutes** | UVI commercial aquaponics | High | Strong UVI-style clarifier anchor. citeturn7view3turn22search2 |
| **9.5-minute clarifier detention underperformed compared with longer retention; UVI moved to ~19 minutes** | UVI commercial trial evidence | High | Strong operational justification for not using a very short detention assumption. citeturn7view5turn22search9 |
| **Clarifier sludge removed three times daily** | UVI commercial maintenance | High | Strong maintenance-frequency anchor for UVI-style demos. citeturn7view5turn13view2 |
| **Filter tanks drained and orchard netting washed once or twice weekly** | UVI suspended-solids polishing | High | Strong maintenance-frequency anchor for UVI-style polishing filters. citeturn12view4 |
| **Filter-cleaning frequency changes nitrate behaviour because retained solids increase denitrification** | UVI operational trade-off | High | Strong evidence that solids removal affects nutrient chemistry, not just cleanliness. citeturn13view2 |
| **Anaerobic solids at the bottom of hydroponic tanks should be removed** | UVI DWC/raft maintenance | High | Strong root-zone maintenance warning. citeturn13view2 |
| **Clarifier, mechanical filter, or swirl separator may all be used; settleable solids should be removed as rapidly as possible** | General RAS removal options | High | Strong process-class guidance; insufficient for universal efficiency defaults. citeturn17view0 |

## Interpretation and translation rules

The cleanest oxygen interpretation for the MVP is to keep **three distinct layers**. First, the already-implemented **nitrification oxygen demand**. Second, a **rough total system oxygen-demand envelope** derived from feed and solids-retention context. Third, a **capacity layer** based on declared aeration or oxygenation equipment. SRAC 451 is explicit that total system oxygen demand is the sum of fish respiration, organic-waste decomposition, and nitrification; it also gives the practical feed-based envelope of **0.3–0.75 kg O₂ per kg feed** depending on solids retention and biofilter configuration. citeturn17view0

The nitrification sub-load itself can be anchored strongly. Ebeling, Timmons, and Bisogni state that **TAN-N production can be estimated as** `feed × protein_fraction × 0.092`, and also restate the commonly used nitrification stoichiometry of about **4.57 g O₂** and **7.14 g alkalinity as CaCO₃** per **1 g ammonia-nitrogen converted**. That makes a defensible nitrification oxygen formula for the design layer: `nitrification_oxygen_demand_kg_day = feed_kg_day × protein_fraction × 0.092 × 4.57`. citeturn10view0

A useful inference follows from those two source families. If feed contains **35% protein**, nitrification alone is about **0.15 kg O₂ per kg feed**; SRAC 451’s total system envelope of **0.3–0.75 kg O₂ per kg feed** therefore implies that fish respiration plus organic-waste breakdown are materially important and should not be hand-waved away. That inference is strong enough for design logic, but it is still an inference and should be labelled as such in internal notes. citeturn10view0turn17view0

For equipment translation, the best first-pass basis is **oxygen-transfer basis first, airflow basis second, power draw last**. SRAC 3700 defines **SOTR** and **SAE**, but warns that aerators transfer less oxygen under real operating conditions than under standard test conditions, so those ratings are best used to compare similar aerators rather than as direct design capacity. SRAC 451 reinforces the caution by noting that common air stones in shallow tanks can have oxygen absorption efficiencies of **not greater than 40%**, while properly designed pure-oxygen systems can exceed **90%** absorption efficiency. citeturn19view2turn19view1turn18view3

That is why the following shortcuts are unsafe. Do **not** treat **nitrification oxygen demand** as **total oxygen demand**. Do **not** treat **blower litres per minute** as **delivered oxygen** without diffuser depth and transfer assumptions. Do **not** treat **fish-tank DO** as proof that DWC roots are well oxygenated. Do **not** turn **feed-based solids coefficients** into **TSS concentration** without volume, flow, detention, and removal-efficiency inputs. And do **not** assume high solids retention is neutral just because it may increase mineralisation; UVI showed that retained solids also increase denitrification, gas generation, and root-zone anaerobic risk. citeturn17view0turn18view1turn13view2

For solids translation, the safest first pass is to calculate only **gross dry solid-waste potential**, not concentration and not wet sludge. UVI’s “at least 25% of feed as dry solids” is the best aquaponics-specific anchor for that. By contrast, TSS concentration, settleable-versus-suspended split, and actual solids-removal capacity all depend on clarification time, hydraulics, filter type, purge schedule, and where in the system the solids are allowed to accumulate. UVI’s own system demonstrates this sensitivity: clarifier detention time, clarifier purge frequency, filter-cleaning frequency, and even bottom solids in hydroponic tanks all mattered materially. citeturn12view0turn14view2turn13view2

## MVP guidance

**Warning-label recommendations**

- `warning_total_oxygen_demand_partial` — emit whenever the report shows nitrification oxygen demand but fish respiration and solids/BOD oxygen demand are not modelled. SRAC 451 makes this separation explicit. citeturn17view0  
- `warning_aeration_capacity_basis_missing` — emit whenever capacity is described only as “blower present”, “air pump present”, or “kW installed”, with no transfer basis such as SOTR, airflow-plus-diffuser-depth, or validated site performance. citeturn19view2turn19view1turn18view3  
- `warning_fish_tank_do_below_operating_target` — trigger below **5 mg/L** for warmwater tilapia/RAS operation; escalate if chronic or repeated. citeturn12view6turn8view2turn7view7  
- `warning_tilapia_growth_penalty_do` — trigger when DO is persistently below **3.5 mg/L**. citeturn12view6turn12view7  
- `warning_biofilter_do_low` — trigger below **2 mg/L** at the nitrification component, or below **5 mg/L** where a small-system biofilter tank is explicitly modelled. citeturn8view2turn8view1  
- `warning_root_zone_aeration_unverified` — emit for DWC/raft whenever separate hydroponic aeration is not declared. citeturn7view8turn7view3turn13view1  
- `warning_solids_translation_provisional` — emit whenever solids are estimated directly from feed using the UVI 25% dry-waste anchor. citeturn12view0  
- `warning_solids_removal_context_missing` — emit whenever clarifier detention, filter type, or purge/cleaning schedule are missing. citeturn13view2turn17view0  
- `warning_backup_aeration_missing` — emit when no generator, oxygen reserve, backup blower, or explicit response-time plan is declared. citeturn28view0turn7view3  
- `warning_feed_spike_oxygen_risk` — emit around heavy feeding if DO is not observed before and after feeding, because SRAC 452 notes that respiration rises sharply after feeding. citeturn24view1

**Demo input candidates**

The cleanest additional demo inputs are: measured or assumed **fish-tank DO mg/L**; a declared **aeration-capacity basis** such as SOTR/SAE, airflow per unit, or an explicitly approximate rule-of-thumb airflow basis; a boolean for **separate DWC/raft aeration present**; simple DWC geometry such as **air-stone count or spacing**; **clarifier retention time**; **clarifier purge frequency**; **filter-cleaning frequency**; and **backup-aeration present or absent**. These all have direct support in SRAC and UVI sources. citeturn28view2turn13view1turn13view2turn28view0

If you want one step beyond that, the next most useful inputs are **fish biomass or stocking density**, because that moves the model closer to resolved fish respiration rather than feed-only inference. WorldFish’s tilapia oxygen-limitation work is helpful here because it explicitly ties oxygen demand to routine metabolism, feeding metabolism, and biosynthesis, and ties oxygen supply to body size and gill surface area. citeturn11view0

**Scenario-default candidates**

Strong default candidates for a first report layer are: **tilapia warmwater DO target >5 mg/L**; **tilapia chronic-growth warning below 3.5 mg/L**; **nitrifier inefficiency warning below 2 mg/L**; **small-scale float-bed air-stone density of one per 10 square feet**; and **UVI-style clarifier detention around 20 minutes**. Those anchors are better supported than most other candidate defaults in this topic area. citeturn12view6turn8view2turn8view0turn7view3

Provisional scenario-default candidates are: **gross dry solid-waste potential = 0.25 × feed**; **UVI-style clarifier purge three times daily**; **UVI-style filter cleaning once or twice weekly**; and **commercial raft air-stone spacing around 1.22 m** where the scenario is explicitly “UVI-like raft”. These are useful, but they should not be promoted to universal canon. citeturn12view0turn13view2turn13view0

**Customer-validation inputs**

The values that most need customer, operator, or advisor validation are: actual **aeration/oxygenation equipment capacity**, real **diffuser depth and arrangement**, whether the system uses **air only or pure oxygen**, whether DWC/raft tanks have **separate blowers**, whether solids are removed **quickly or intentionally retained for mineralisation**, and whether backup capability can actually restore aeration within the response window. These are the variables most likely to make a superficially similar system behave very differently. citeturn18view1turn28view0turn13view2

**Do-not-use-yet findings**

Do not yet promote any universal conversion from **blower airflow or blower wattage to delivered oxygen**. Do not promote any universal conversion from **feed added to TSS concentration**. Do not promote a universal **settleable-versus-suspended solids split** beyond clearly tagged system-specific evidence such as UVI’s clarifier/filter split. And do not pretend there is a basil-specific DWC root-zone DO threshold in the current evidence pack; the strongest root-zone DO numbers here are hydroponic leafy-greens proxies. citeturn19view1turn18view3turn14view2turn23view1

## Open questions

The most important unresolved item is a **first-pass tilapia fish-respiration model** suitable for the MVP. The current evidence is strong enough to say fish respiration matters and varies with size, feeding, and temperature, but this pass does not yet produce a simple, high-confidence coefficient that should be hard-coded. WorldFish’s model points the right direction, but a reviewable first-pass implementation basis still needs its own evidence pass. citeturn11view0

A second unresolved item is how to **derate nameplate airflow or SOTR into site-usable oxygen delivery** for specific shallow-tank, raft-channel, or diffuser layouts. The sources are clear that standard ratings and real operating transfer differ materially, but they do not give a single safe universal derating factor for aquaponic use. citeturn19view1turn18view3

A third unresolved item is the lack of a strong **basil-specific DWC root-zone oxygen or disease threshold**. The current root-zone oxygen disease guidance is strong as hydroponic leafy-greens evidence, but still a proxy for basil. citeturn23view1

A fourth unresolved item is **cross-context solids-removal efficiency by component type**. The current source set strongly supports clarifier detention, solids-removal urgency, and maintenance patterns, but not a universal efficiency table for swirl separators, radial-flow settlers, clarifiers, and polishing filters across all aquaponic scales. citeturn17view0turn13view2

## Recommended next repo-side use and direct answers

The next Codex design pass should preserve four explicit distinctions: **nitrification oxygen demand**, **total oxygen-demand envelope**, **declared aeration-capacity basis**, and **solids-removal context**. It should also preserve a separate DWC flag for **root-zone aeration present or unverified**. That keeps the system honest: you can show stronger insight than “missing context everywhere”, but you still do not imply that total fish-side oxygen safety has been calculated when only part of the chain is known. citeturn17view0turn13view1turn19view1

What could be implemented next, on the evidence now in hand, is a report layer that compares **nitrification O₂ demand** against a declared capacity basis, plus a **rough total oxygen envelope** based on `0.3–0.75 kg O₂/kg feed`, clearly tagged as feed-based and solids-context-dependent. What should remain warning-only is anything requiring real transfer efficiency or fish-respiration resolution that the scenario does not supply. What must remain scenario input for now includes real equipment capacity, backup status, solids-removal pattern, and whether the DWC component has separate aeration. citeturn17view0turn28view2turn28view0

1. **Minimum input set needed to compare nitrification oxygen demand against aeration context**  
   At minimum: `feed_kg_day`, `protein_fraction` or `TAN_N_load`, a declared **aeration-capacity basis** such as SOTR or airflow-based heuristic, and enough context to know whether that basis is continuous and applicable to the fish loop or plant loop. Without a real capacity basis, the comparison should remain warning-only. citeturn10view0turn19view2turn19view1

2. **Minimum input set needed to estimate total oxygen-risk context for tilapia**  
   At minimum: a total-oxygen approach needs the existing feed inputs **plus** either a fish-respiration model input set or a provisional feed-based total oxygen envelope, a measured or target **DO**, a declared **aeration/oxygenation capacity basis**, and basic solids-retention context. If you want a more resolved fish-risk view, add fish biomass or stocking density and temperature. citeturn17view0turn11view0turn12view6

3. **Strongest DWC and raft aeration anchors for a tilapia plus basil demo**  
   The strongest anchors are: **aerate long deep channels**, **one air stone per 10 square feet** in small float beds, and the **UVI commercial pattern** of separate hydroponic aeration with **48 air stones per set of hydroponic tanks spaced 1.22 m apart**, where DO rose from **4.0 to 6.9 mg/L** through the raft tanks. citeturn7view8turn8view0turn13view1

4. **Safest first solids-load estimate from feed, if any**  
   Yes: a cautious first-pass estimate is `provisional_dry_solid_waste_potential_kg_day = 0.25 × feed_kg_day`, explicitly labelled as **dry solid waste potential**, not wet sludge, not TSS, and not a concentration estimate. citeturn12view0

5. **Which solids-removal values can be used as demo assumptions without becoming canon**  
   The safest demo assumptions are **UVI-style** ones: clarifier detention around **20 minutes**, clarifier purge **three times daily**, filter cleaning **once or twice weekly**, and a note that slower solids removal increases mineralisation but also shifts nitrate and gas behaviour. These should stay tagged as UVI-like operating assumptions, not universal defaults. citeturn7view3turn13view2

6. **Which aeration and solids values must remain user-supplied scenario inputs**  
   Actual **equipment capacity**, real **transfer basis**, diffuser depth and layout, whether **pure oxygen** is used, whether there is **separate DWC aeration**, the real **solids-removal subsystem**, purge schedule, and backup power or backup air capability should all remain scenario inputs. citeturn18view3turn28view0turn13view1turn13view2

7. **What warning labels should the MVP report emit when aeration or solids context is missing**  
   At minimum: `warning_total_oxygen_demand_partial`, `warning_aeration_capacity_basis_missing`, `warning_root_zone_aeration_unverified`, `warning_solids_translation_provisional`, `warning_solids_removal_context_missing`, `warning_backup_aeration_missing`, and `warning_feed_spike_oxygen_risk`. Those are directly justified by the source set. citeturn17view0turn19view1turn13view2turn28view0turn24view1

8. **What the next Codex design pass should do with this research**  
   Use it to define a **separate oxygen-capacity context layer** and a **separate solids-context layer** around the existing load model. Promote only the well-supported anchors: warmwater fish DO target, nitrifier DO floor, DWC/raft aeration required, UVI-style clarifier detention, and the provisional dry-solids coefficient. Keep fish-respiration resolution, real transfer efficiency, and concentration-level solids modelling explicitly unresolved unless the scenario supplies the missing inputs. citeturn12view6turn8view2turn7view8turn7view3turn12view0