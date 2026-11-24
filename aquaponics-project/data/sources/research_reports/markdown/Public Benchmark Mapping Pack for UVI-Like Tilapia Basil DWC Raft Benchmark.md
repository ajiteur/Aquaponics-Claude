# Public Benchmark Mapping Pack for UVI-Like Tilapia Basil DWC/Raft Benchmark

## Executive summary

The current `uvi_like_tilapia_basil_dwc_raft_benchmark_v0` is **partly benchmark-backed and partly scaled scenario overlay**. Its strongest public anchors are the **UVI DWC/raft system architecture**, **one rearing-tank volume of 7,800 L**, **32% crude-protein tilapia feed**, **pH around 7 as an aquaponic compromise**, **continuous recirculation/aeration**, and **a dry-solids prior of at least 25% of feed on a dry basis**. Those are all directly supported by UVI and SRAC/NMSU-style institutional sources. citeturn5view2turn11view0turn15view0turn11view4turn9view0

The biggest structural weakness is that the fixture is called “UVI-like” while its **`feed_kg_day = 1.0` does not map cleanly to the public UVI commercial module** unless a smaller raft area/module boundary is declared. UVI’s own raft design guidance is **60–100 g feed/m²/day**, and the UVI commercial raft area is **214 m²**, which implies roughly **12.8–21.4 kg feed/day** for the full raft area. Even one quarter of that raft area, **53.5 m²**, would imply roughly **3.2–5.35 kg/day** at the same design ratio. So `1.0 kg/day` is not a defensible “full UVI-like” feed benchmark as currently framed. citeturn15view0turn5view2turn11view0turn3view1

The current **`effective_water_volume_l = 7800`** is defensible **only because `concentration_scope = fish_tank`**. Public UVI sources show **7,800 L per rearing tank** but **110,000 L total system volume**. That means the benchmark’s concentration context is a **local fish-tank concentration proxy**, not a total-system average. This is a valid modelling choice, but it must be stated explicitly; otherwise it falsely looks like a total-system benchmark. citeturn5view2turn11view0

The chemistry context is directionally sound. UVI and SRAC/NMSU support **pH ≈ 7**, **warmwater tilapia around 27–29°C**, and **DO at or above 5 mg/L** as normal operating context. NMSU also shows that at **pH 7.0** and **28°C**, only a small fraction of TAN is in the toxic un-ionised form, so the current NH3-context outputs are chemically plausible as **modelled** values. They are still **not observed UVI measurements**, and therefore cannot be used as safety proof. citeturn15view0turn8view2turn9view0turn12view3

The weakest parts of the benchmark are the **business inputs** and some **scaled engineering inputs**. The current **feed price in INR**, **electricity price in INR**, and the specific **0.2 kW pump / 0.1 kW blower** values are **not public UVI benchmark anchors** from the retrieved institutional corpus. They are acceptable only as **scenario overlays** or **scaled demo assumptions**, not as public benchmark facts. citeturn5view2turn11view0

This means the benchmark is **credible enough for a pre-customer seed-demo** if it is described as a **public-evidence-inspired, scaled, scenario-augmented benchmark**, not as a direct reproduction of UVI operations. It is also suitable for technical advisor/investor conversations **only if the report clearly distinguishes** benchmark-backed assumptions, scenario assumptions, modelled outputs, and blocked claims such as basil saleability, profitability, total operating cost, or safety. citeturn15view0turn9view4turn12view1

## Evidence hierarchy

The strongest evidence in this pass comes from **UVI primary materials** describing the commercial aquaponic system and basil trials, because they directly match the target architecture: tilapia + basil + raft/DWC. The key sources are the current UVI CAS webpage, the UVI “Principles of aquaponics” page, and the UVI paper on tilapia and basil production. citeturn5view2turn15view0turn11view0

The next strongest layer is **SRAC and university extension RAS/aquaponics materials**, used mainly to anchor operating ranges, DO thresholds, nitrification context, and general raft design logic. These include SRAC-454, SRAC-452, SRAC-5007, SRAC-282, and NMSU Circular 680. citeturn11view1turn9view0turn11view3turn8view0turn12view1

The weakest evidence in this pass is anything that would try to make the current **INR business inputs** or the **scaled power assumptions** look like institutional UVI benchmark facts. I did **not** find public UVI technical documents backing those exact business numbers, so they should remain scenario/business assumptions rather than benchmark anchors. citeturn5view2turn11view0

## UVI-like benchmark summary

Public UVI materials describe a **commercial raft aquaponic system** with **four rearing tanks of 7.8 m³ each**, **six hydroponic tanks of 11.356 m³ each**, **214 m² total plant growing area**, and **110,000 L total water volume**. The UVI CAS page also states that water is pumped through each rearing tank at **25 gpm / 100 L/min**, giving about **1:20 h full volume exchange**, while the UVI principles page lists a **1 h rearing-tank target** with the UVI system running at **1.37 h**, and a **20 min clarifier target**. citeturn5view2turn15view0turn11view0

For basil specifically, the UVI paper reports a commercial-scale outdoor tropical system using **floating pellets with 32% protein**, **basil at 8 plants/m²**, **28-day growth periods**, and repeated cutting at **15 cm** with regrowth. It also reports a **sustainable staggered basil mode** at about **99.6 g feed/day/m²**, while warning that batch basil eventually developed nutrient deficiencies and some harvest became unmarketable. citeturn11view0turn3view1turn3view3turn2view4

In short, the public benchmark is strongest for **system geometry**, **operating logic**, **feed protein**, **exchange**, **pH compromise**, **DO context**, and **basil cropping regime**. It is weak for **your current daily feed scalar**, **your current equipment power scalar**, and **your current business prices** unless those are explicitly declared to be scaled scenario overlays. citeturn5view2turn15view0turn11view0

## Context split notes

### UVI raft aquaponics

UVI’s public materials represent a **commercial-scale, warmwater, tropical, raft/DWC aquaponic system**. They are the closest public analogue to the current benchmark name and are therefore the primary frame for “UVI-like”. citeturn5view2turn15view0turn11view0

### DWC/raft aquaponics

For raft systems, UVI and SRAC both support a design logic centred on **feed input per unit plant area**, **root-zone aeration**, and **solids removal before the hydroponic component**. UVI explicitly states that in raft aquaponics adequate biofiltration occurs in the hydroponic component when the feeding-rate ratio is right, and SRAC gives raft-specific aeration and maintenance guidance. citeturn15view0turn11view3

### RAS/tank systems

SRAC RAS documents matter here because the benchmark produces **fish-tank TAN and DO context**, not just plant-side context. They support the logic that local fish-tank exchange, warmwater DO targets, pH, and backup aeration remain central even inside aquaponics. citeturn11view5turn9view0turn9view4

### Small aquaponics

Small-system SRAC guidance is useful for design heuristics, but it is **not** a direct benchmark for the UVI commercial module. It helps as a transfer source for things like air-stone density, daily maintenance tasks, and the fact that raft and NFT should be sized differently from media systems. citeturn11view3turn5view4

### Commercial aquaponics

The UVI benchmark is commercial-scale. Any scaled-down demo benchmark should be described as **commercial-benchmark-inspired** rather than “equivalent to UVI” unless module size, area, feed rate, and power scaling are made explicit. citeturn5view2turn15view0

## Benchmark mapping table

| current fixture field | current fixture value | unit | closest public benchmark value/range | source | source date or publication date if available | context | confidence | recommended classification | recommended fixture treatment | notes |
|---|---:|---|---|---|---|---|---|---|---|---|
| `feed_kg_day` | 1.0 | kg/day | UVI raft design: **60–100 g feed/m²/day**; with **214 m²** that implies **12.8–21.4 kg/day** for the full UVI raft area. One quarter area (**53.5 m²**) implies **3.2–5.35 kg/day**. | UVI principles; UVI basil paper citeturn15view0turn11view0 | current UVI webpage; basil paper based on 2002 trials, published 2004 citeturn17search7 | commercial raft aquaponics | high | `scenario_input_ok` | `keep_but_soften_language` | `1.0 kg/day` is **not** a full-UVI feed benchmark. It only maps to roughly **10–16.7 m²** of raft area at the UVI design ratio. |
| `protein_fraction` | 0.32 | fraction | **32% protein** floating pellets | UVI basil paper; SRAC-5007 citeturn11view0turn5view4 | 2004 paper / current SRAC PDF | tilapia aquaponics | high | `strong_benchmark_anchor` | `keep_as_is` | One of the cleanest benchmark-backed inputs in the fixture. |
| `effective_water_volume_l` | 7800 | L | **7,800 L per rearing tank**; **110,000 L total system volume** | UVI CAS page; UVI basil paper citeturn5view2turn11view0 | current UVI webpage / 2004 paper | commercial UVI system | high | `strong_benchmark_anchor` | `keep_as_is` | Strong only because the fixture already says `concentration_scope = fish_tank`. |
| `accumulation_period_day` | 1 | day | Daily feed input / daily feed ratio is the standard public design basis | UVI principles; SRAC-454 citeturn15view0turn5view1 | current UVI webpage / 2006 SRAC | modelling timestep | medium | `scenario_input_ok` | `keep_but_soften_language` | This is a modelling timestep, not a measured UVI residence time. |
| `concentration_scope` | `fish_tank` | categorical | Public UVI anchors support local rearing-tank exchange and volume, but total system volume is much larger | UVI CAS page; UVI principles citeturn5view2turn15view0 | current UVI webpages | fish-exposure scope choice | medium | `scenario_input_ok` | `keep_but_soften_language` | Defensible, but it must be stated as a **scope convention** rather than a measured system-average benchmark. |
| `pH` | 7.0 | pH units | UVI recommends **pH 7.0** as aquaponic compromise; basil trials averaged **7.4** and **7.1** with ranges **7.0–7.6** and **6.9–7.3** | UVI principles; UVI basil paper; NMSU corroboration citeturn15view0turn2view0turn12view1 | current UVI webpage / 2004 paper / NMSU current PDF | aquaponic compromise pH | high | `strong_benchmark_anchor` | `keep_as_is` | Good benchmark value, but not the only defensible one. |
| `water_temp_c` | 28.0 | °C | Tilapia tank optimum **27–29°C** | SRAC-282 citeturn8view2 | current SRAC PDF | warmwater tilapia tank/RAS | high | `scenario_input_ok` | `keep_but_soften_language` | Strong species/production anchor, but not a direct measured UVI basil-trial mean in the retrieved lines. |
| `freshwater_assumption` | true | boolean | UVI system used **rainwater** and cultured tilapia in freshwater aquaponics | UVI basil paper citeturn16view0 | 2004 paper, 2002 trials | freshwater aquaponics | high | `strong_benchmark_anchor` | `keep_as_is` | This is a clean UVI-compatible assumption. |
| `measured_do_mg_l` | 5.0 | mg/L | UVI principle: maintain **DO ≥5 mg/L** in fish tank and around roots; basil trial rearing tanks observed **4.0–5.0 mg/L**; SRAC warmwater optimum **>5 mg/L** | UVI principles; UVI basil paper; SRAC-452 citeturn15view0turn2view2turn9view0 | current UVI webpage / 2004 paper / current SRAC PDF | warmwater raft aquaponics | high | `strong_benchmark_anchor` | `keep_but_soften_language` | Best interpreted as a **threshold-edge / low-end operating context**, not as proof of safe margin. |
| `dry_solids_coefficient` | 0.25 | dry-mass fraction of feed | UVI principle: **at least 25% of feed becomes solid waste, dry basis** | UVI principles citeturn15view0 | current UVI webpage | solids-generation prior | high | `strong_benchmark_anchor` | `keep_as_is` | Good benchmark prior for **generated dry solids**, not for captured sludge or disposal volume. |
| `feed_price_per_kg` | 45 | INR/kg | No public UVI technical benchmark retrieved for this value | no matching benchmark source found in retrieved UVI/SRAC corpus citeturn5view2turn11view0 | n/a | business overlay | low | `scenario_input_ok` | `keep_but_soften_language` | Acceptable as a scenario price, but not as a public benchmark fact. Requires metadata if shown externally. |
| `electricity_price_per_kwh` | 7.5 | INR/kWh | No public UVI technical benchmark retrieved for this value | no matching benchmark source found in retrieved UVI/SRAC corpus citeturn5view2turn11view0 | n/a | business overlay | low | `scenario_input_ok` | `keep_but_soften_language` | Same issue as feed price: scenario input, not benchmark anchor. |
| `pump_kw` | 0.2 | kW | UVI basil paper used **½-hp pump** ≈ **0.37 kW** for the full commercial loop | UVI basil paper citeturn11view0 | 2004 paper | whole-system nameplate | medium | `expert_question_candidate` | `relabel_as_expert_question` | Plausible only as a scaled module assumption; not a direct UVI benchmark value. |
| `pump_hours_day` | 24 | h/day | UVI pumps water **continuously** | UVI CAS page; SRAC-452 continuous aeration/operation logic citeturn5view2turn9view0 | current UVI webpage / current SRAC PDF | continuous recirculation | high | `strong_benchmark_anchor` | `keep_as_is` | Strong as an operating-mode anchor. |
| `pump_power_basis` | `nameplate` | categorical | Public UVI docs report motor **ratings** rather than measured kWh draw | UVI basil paper; UVI CAS page citeturn11view0turn5view2 | 2004 / current webpage | equipment-metadata basis | medium | `scenario_input_ok` | `keep_but_soften_language` | Fine for a demo assumption, but do not imply measured consumption. |
| `blower_kw` | 0.1 | kW | UVI basil paper used separate **1-hp blowers** for fish and hydroponic tanks, i.e. ≈ **0.746 kW each** for the full commercial loop | UVI basil paper citeturn11view0 | 2004 paper | whole-system nameplate | medium | `expert_question_candidate` | `relabel_as_expert_question` | Much smaller than the retrieved whole-UVI-system anchor; needs explicit module scaling rationale. |
| `blower_hours_day` | 24 | h/day | Continuous aeration is required in intensive warmwater systems | SRAC-452; UVI continuous DO/aeration logic citeturn9view0turn15view0 | current SRAC PDF / UVI webpage | aeration runtime | high | `strong_benchmark_anchor` | `keep_as_is` | Strong operating-mode anchor. |
| `blower_power_basis` | `nameplate` | categorical | Public UVI docs report blower motor rating rather than measured draw | UVI basil paper citeturn11view0 | 2004 paper | equipment-metadata basis | medium | `scenario_input_ok` | `keep_but_soften_language` | Same caveat as pump power basis. |

## Fish/feed benchmark anchors

The strongest public fish/feed anchors for this benchmark are:

- **Tilapia feed protein**: UVI basil trials used **32% protein floating pellets**, which supports `protein_fraction = 0.32` directly. citeturn11view0
- **Fish cohort cadence**: UVI CAS states fingerlings are stocked at about **50 g** and reared **24 weeks to 900 g**, with one tank harvested every **6 weeks**. citeturn5view2
- **Basil-specific feed-to-area ratio**: UVI principles recommend **60–100 g feed/m²/day** for raft hydroponics, and the basil trial reports **81.4 g/day/m²** in batch mode and **99.6 g/day/m²** in staggered mode, with the staggered mode deemed sustainable. citeturn15view0turn3view3turn4search1
- **Stocking context**: In the basil paper, Nile tilapia fingerlings were stocked at **77 fish/m³**, averaged **70 g**, and were fed **three times daily ad libitum**. citeturn11view0

What this means for the current fixture is straightforward: `feed_kg_day = 1.0` is **too low to serve as a direct full-UVI commercial benchmark**, and probably too low even for a one-tank + quarter-raft interpretation, unless the benchmark is explicitly meant to represent a much smaller plant area than the public UVI module. citeturn15view0turn11view0

## Water-quality and volume anchors

The cleanest volume anchors are all public and direct:

- **One fish rearing tank**: **7,800 L**. citeturn5view2turn11view0
- **Total system volume**: **110,000 L**. citeturn5view2turn11view0
- **Six hydroponic tanks**: **11,356 L each** and **214 m² total plant area**. citeturn5view2turn11view0
- **Rearing-tank exchange**: public UVI target **1 h**, actual UVI system **1.37 h**; CAS page reports **100 L/min** for about **1:20 h** full exchange per rearing tank. citeturn15view0turn5view2
- **Hydroponic retention**: UVI basil paper reports about **3 h average retention time** in hydroponic tanks. citeturn11view0
- **Clarifier anchor**: UVI principles recommend **20 min**. citeturn15view0

This makes `effective_water_volume_l = 7800` defensible **only** as a fish-tank concentration context. If someone instead interpreted the benchmark as a full-system concentration using the public UVI **110,000 L** volume, the same daily TAN-N load would be far lower before removal. So the benchmark must state that it is using a **fish-tank local concentration proxy**, not a total-system average. citeturn5view2turn15view0

## TAN/NH3 interpretation anchors

The public benchmark sources strongly support the **methodology** for interpreting TAN/NH3, even when they do not support every exact fixture scalar.

NMSU explicitly states that test kits measure **TAN**, that the toxic fraction depends on **pH and temperature**, and that to determine toxic ammonia you multiply TAN by the table factor for the observed pH and temperature. In the same NMSU table, at **pH 7.0** and **28°C**, the factor is about **0.697%**, which is consistent with the current model producing a very small NH3-N fraction from the benchmark’s estimated TAN-N. citeturn11view4turn12view3

That means the current benchmark’s TAN/NH3 chemistry is **directionally coherent**, but it is still **modelled** rather than observed. UVI’s basil trial reported actual operating **total-ammonia-N** ranges of **1.1–2.4 mg/L** in staggered culture and **1.6–2.9 mg/L** in batch culture. By contrast, the benchmark’s current **estimated TAN-N ≈ 3.77 mg/L** is a one-day, fish-tank-scope model output using the fixture’s own load assumptions. So it should be described as a **calculated concentration context**, not as a UVI-observed benchmark value. citeturn2view0turn11view4

The public ammonia-risk sources also make clear that **higher pH and higher temperature increase the toxic fraction**, and that TAN by itself does not prove toxicity. That is why the current benchmark should continue to display **TAN/TAN-N**, **NH3 fraction context**, and **explicit unit labels**, but must avoid implying proved fish safety. citeturn11view4turn8view4turn9view0

## Aeration/solids anchors

For aeration, the strongest public anchors are:

- UVI principles: **DO of 5 mg/L or higher** should be maintained in the fish rearing tank and around plant roots. citeturn15view0
- UVI basil trial: rearing-tank DO during basil fell to **4.0–5.0 mg/L**; earlier lettuce trials were **5.0–6.0 mg/L**. citeturn2view2
- SRAC-452: warmwater systems should generally be kept **above 5 mg/L**, nitrifiers become inefficient **below 2 mg/L**, and aeration systems must run **continuously**. citeturn9view0

For solids, UVI principles say **at least 25% of feed becomes solid waste on a dry basis**, and those solids should be **removed before the hydroponic component** because they foul roots, create anaerobic zones, consume oxygen, and generate ammonia. UVI’s basil paper shows the practical removal routine: settleable solids removed from clarifiers **three times daily**, orchard-netting filter tanks drained **twice weekly**, and screens cleaned **daily**. citeturn15view0turn11view0

This makes the current `dry_solids_coefficient = 0.25` a **good benchmark-backed generation prior**, but not a proof of actual solids capture, sludge disposal volume, or plant-root cleanliness. It should remain explicitly labelled as **dry-solids potential**, not “solids removed”. citeturn15view0turn11view0

## Operating-cost benchmark anchors

The public technical benchmark is **not** a public cost benchmark.

The retrieved UVI technical sources give **equipment ratings** and system design context, but they do **not** provide the current benchmark’s **45 INR/kg feed price** or **7.5 INR/kWh electricity price**. So those business inputs should be shown as **scenario cost overlays**, not as public benchmark values. citeturn5view2turn11view0

By contrast, the equipment-power side does have benchmark context: the UVI basil paper reports a **½-hp pump** and separate **1-hp blowers** for the fish and hydroponic tanks in the full commercial system. That means the current **0.2 kW pump** and **0.1 kW blower** cannot be presented as direct UVI benchmark values; at best they are **scaled nameplate assumptions** for a smaller demo module. citeturn11view0

The current **99 INR/day feed + power subtotal** is therefore best described as an **internally consistent scenario subtotal** computed from the fixture’s business inputs, not as a public benchmark operating cost. citeturn5view2turn11view0

## Basil production and saleability context

Public UVI evidence is strong enough to benchmark **basil production context**, but **not** strong enough to benchmark `saleable_harvest_mass_kg` for your seed demo.

What can be benchmarked from UVI:

- Basil can be produced successfully in the UVI raft system. citeturn11view0
- The 2002 UVI basil trials used **8 plants/m²**, **28-day growth periods**, repeated cutting at **15 cm**, and regrowth. citeturn3view1
- Later UVI variety work used **16 plants/m²** and harvests every **21–28 days** before blooming, showing that density and cycle length are cultivar/management-dependent rather than canonical. citeturn20view0
- Staggered production in the UVI system was more agronomically sustainable than batch production at similar overall yield scale. citeturn4search1turn2view4

What **cannot** be promoted as known saleable output:

- The UVI paper explicitly says that in batch culture, nutrient deficiencies eventually rendered **much of the harvest unmarketable**. citeturn2view4
- It also reports mortality and root disease issues after repeated cutting, including **Pythium** and survival loss. citeturn3view3turn2view5

So the correct benchmark interpretation is: **the UVI evidence supports basil biological production and harvest regime**, but it does **not** support a clean repo claim that the benchmark knows saleable basil mass. That should remain **blocked until observed or manually reviewed**. citeturn2view4turn3view3

## Source gaps

The most important source gaps are structural, not numerical.

- The benchmark does **not declare the intended module boundary**: full UVI commercial system, one fish tank + proportional raft area, or some other scaled module. Without that, `feed_kg_day`, `pump_kw`, and `blower_kw` cannot be honestly called “UVI-like”. citeturn5view2turn15view0
- The benchmark does **not declare raft growing area**. Because UVI design uses feed/day per m² plant area, plant area is missing from the most important public sizing logic. citeturn15view0turn4search1
- The benchmark does **not provide fish biomass/stocking context**, so the feed rate cannot be compared to UVI cohorts except very indirectly. citeturn5view2turn11view0
- The business inputs have **no public benchmark provenance** in the retrieved corpus. citeturn5view2turn11view0
- The benchmark has no public anchor for **backup power/aeration status**, which matters if the report risks implying reliability or resilience. UVI and SRAC both emphasise backup systems. citeturn15view0turn9view4

## Expert question candidates

The following are the best candidates for expert/advisor review before promoting the benchmark much further:

- If `feed_kg_day = 1.0`, **what exact raft area** is this benchmark claiming to represent under UVI-like feed-to-area logic? citeturn15view0turn4search1
- Is the benchmark intended to represent **one UVI fish tank plus one quarter of the raft area**, or a completely different scaled module? Public UVI hardware and operating intensities differ a lot depending on that answer. citeturn5view2turn11view0
- How should **pump and blower nameplate power** be scaled from full-system UVI equipment to the current demo module? citeturn11view0
- Should the default concentration view stay **fish-tank local** or should the report also show a **total-system diluted context** for honesty? Public UVI system volume makes that difference material. citeturn5view2turn11view0
- Should `dry_solids_coefficient` remain a **generated-solids prior only**, with captured-sludge estimates blocked until removal design is specified? UVI sources support that caution. citeturn15view0turn11view0

## Customer/operator questions for later

These are not blockers for a seed demo, but they are needed later for operator realism:

- Actual **daily feed delivery profile** and seasonal variation.
- Actual **measured pump/blower power draw**, not just nameplate.
- Actual **DO logging location and time basis**.
- Actual **clarifier purge and filter-cleaning burden**.
- Actual **backup aeration/power practice**.
- Actual **basil rejection / saleability outcomes** after harvest handling. citeturn11view0turn15view0turn9view4

## Recommended updates to benchmark fixture classification

Without proposing diffs, the fixture should conceptually be read in four classes:

- **Benchmark-backed core**: `protein_fraction`, `effective_water_volume_l` with fish-tank scope, `freshwater_assumption`, `dry_solids_coefficient`, `pump_hours_day`, `blower_hours_day`, and pH near 7.0. citeturn5view2turn15view0turn11view0
- **Benchmark-informed scenario inputs**: `water_temp_c`, `measured_do_mg_l`, `accumulation_period_day`, `concentration_scope`. citeturn8view2turn9view0turn12view3
- **Scaled engineering assumptions needing soft language**: `feed_kg_day`, `pump_kw`, `blower_kw`, and any totals derived from their scaling. citeturn15view0turn11view0
- **Non-benchmark business overlays**: `feed_price_per_kg`, `electricity_price_per_kwh`, and the resulting selected cost-pressure subtotal. citeturn5view2turn11view0

## Recommended updates to seed-demo report language

Use language like this:

- “**Public-evidence-inspired benchmark scenario** anchored to UVI/SRAC aquaponics and RAS references.” citeturn15view0turn9view0
- “**Scaled benchmark-style technical scenario**, not a direct reproduction of the full UVI commercial system.” citeturn5view2turn15view0
- “Fish-tank TAN/NH3 figures are **modelled concentration context outputs**, not observed farm measurements.” citeturn11view4turn2view0
- “Feed price, electricity price, and selected cost subtotal are **scenario business assumptions**, not public benchmark facts.” citeturn5view2turn11view0
- “Basil saleable output remains **blocked until observed or manually reviewed**.” citeturn2view4turn3view3

Avoid language like:

- “This reproduces the UVI system.”
- “This benchmark proves safety.”
- “This benchmark proves profitability.”
- “This benchmark proves saleable basil output.” citeturn15view0turn9view4turn2view4

## Recommended language for advisor/investor conversations

A defensible short form is:

> “We have a public-benchmark-mapped demo scenario inspired by UVI’s tilapia + raft aquaponics work. Core hydraulic, feed-protein, pH, DO, and solids assumptions are institution-backed. Some business and equipment values are still scenario overlays, clearly marked as such. The tool demonstrates model structure and benchmark alignment, not customer validation, farm safety, profitability, or known saleable basil output.” citeturn5view2turn15view0turn9view4turn2view4

## Claims to avoid

Do **not** describe this benchmark as any of the following:

- customer validation
- commercial proof
- real-world operating proof
- safety proof
- revenue proof
- profitability proof
- total operating cost proof
- proof of tank suitability
- proof of system resilience
- proof of basil saleable harvest mass citeturn9view4turn2view4turn15view0

## Open questions

The main open questions are:

- What exact **module scale** does the benchmark intend to represent?
- What **plant area** is implicitly coupled to `feed_kg_day = 1.0`?
- Should the benchmark visually show both **fish-tank** and **whole-system** concentration contexts?
- How should **equipment power** be scaled from public UVI hardware to the current demo fixture?
- Should the current DO line be shown as **measured low-end context**, **target minimum**, or both?
- What metadata will later distinguish **benchmark-backed** from **scenario-only** cost inputs? citeturn5view2turn15view0turn9view0

## Recommended next repo-side use

The next Codex pass should use this research to do four things conceptually:

- add **benchmark classification metadata** to every fixture field
- separate **benchmark-backed technical anchors** from **scenario business overlays**
- make **modelled versus observed** wording explicit in the seed-demo report path
- keep **basil saleability blocked** until future observed/reviewed data exists citeturn2view4turn15view0turn11view4

It would also be worth preparing a short **expert-question package** focused on module scope, plant area, and power scaling before any dashboard UI implies that the current fixture represents a direct UVI module. citeturn5view2turn11view0

## Direct answers

**Which current benchmark fixture values are best supported?**  
Best supported are `protein_fraction = 0.32`, `effective_water_volume_l = 7800` **when explicitly fish-tank scoped**, `freshwater_assumption = true`, pH around `7.0`, `dry_solids_coefficient = 0.25`, and the assumption of continuous pump/blower runtime. `measured_do_mg_l = 5.0` is also defensible as a low-end UVI/SRAC operating anchor. citeturn11view0turn5view2turn15view0turn9view0

**Which current benchmark fixture values should remain scenario inputs?**  
`feed_kg_day = 1.0`, `accumulation_period_day = 1`, `concentration_scope = fish_tank`, `water_temp_c = 28.0`, the specific `pump_kw` and `blower_kw` values, and the two price inputs should remain scenario inputs. Some are benchmark-informed; others are simply overlays. citeturn15view0turn11view0

**Which values should be marked `source_gap`?**  
The biggest `source_gap` is not one scalar but the **missing module definition** tying feed/day to raft area and scaled equipment. If a public-facing report keeps the current INR feed/electricity values without provenance, those also become benchmark `source_gap`s. Any implied saleable basil output would be a `source_gap` or blocked claim. citeturn15view0turn2view4

**Which values require expert review?**  
Expert review is most needed for `feed_kg_day` as a UVI-like scaling claim, `pump_kw`, `blower_kw`, and the intended mapping between fish-tank volume and raft area. citeturn15view0turn11view0

**Which values require customer/operator observed data later?**  
Actual feed schedule, measured power draw, DO time-series, backup status, solids removal performance, and any basil saleability or rejection data require later operator observation. citeturn11view0turn9view4turn2view4

**Is the current UVI-like benchmark scenario credible enough for a pre-customer seed-demo report?**  
Yes, **conditionally**. It is credible if presented as a **UVI-inspired, scaled, scenario-augmented technical benchmark**, not as a direct reproduction of UVI operations. citeturn5view2turn15view0

**Is it credible enough for technical investor/advisor conversations if properly caveated?**  
Yes. It is credible for conversations about **model structure**, **evidence mapping**, and **what is intentionally blocked**, but not for claims of market proof, safety, profitability, or customer validation. citeturn9view4turn2view4

**What should be changed before using it externally?**  
Make module scope explicit, label business inputs as scenario overlays, label TAN/NH3 outputs as modelled rather than observed, and keep basil saleability blocked. citeturn5view2turn11view4turn2view4

**What should be changed before creating a dashboard/report UI?**  
Add visible distinctions for **benchmark-backed**, **scenario assumption**, **modelled output**, and **blocked claim**. Also add a clear note that `effective_water_volume_l = 7800` is a fish-tank scope, not a total-system value. citeturn5view2turn11view4

**What should the next Codex pass be?**  
The next pass should formalise **fixture evidence classes**, **scope metadata**, **report phrasing rules**, and **blocked-claim discipline** before spending design effort on polished dashboards. citeturn15view0turn9view4turn2view4