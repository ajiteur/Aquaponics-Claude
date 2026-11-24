# Corroboration report for aquaponics Layer 1 component and process library: Greenhouse climate control and disease-trigger variables

## Executive summary

Greenhouse climate control variables that most reliably translate into **Layer‑1 simulation hooks** for aquaponics/hydroponics are: **air temperature (day/night), nutrient-solution/root-zone temperature, relative humidity (RH), vapour pressure deficit (VPD), leaf wetness duration, and canopy airflow/mixing**. Tier‑1 university sources repeatedly tie these variables to **lettuce quality failures (bolting and tipburn)** and to **high-impact greenhouse diseases (basil downy mildew, Botrytis blight, lettuce downy mildew)**. citeturn12view1turn12view2turn14view0turn3view4turn12view5turn13view4turn13view3

For **lettuce (hydroponic/CEA baseline)**, high-trust setpoints cluster around **~24 °C day** and **~18–19 °C night** and emphasise that exceeding these values increases quality risk, especially bolting under prolonged heat and/or large fluctuations. citeturn12view1turn12view4 Cornell CEA additionally specifies an operational **RH band of ~50–70%** and a **nutrient solution temperature ceiling of ~25 °C** (with a cited optimum of **24 °C air & 24 °C water** for dry‑weight production in a floating system). citeturn12view1turn4view2

For **humidity/airflow**, Cornell CEA identifies RH as a primary lever because **high RH reduces transpiration**, which reduces **nutrient transport** and **leaf cooling**, while also encouraging diseases such as **Botrytis and mildew**. citeturn12view2 Tipburn (lettuce) is strongly framed as an **environment-driven Ca-transport failure**: the lettuce head creates a **humid micro-environment** by blocking airflow, reducing transpiration and Ca delivery to young leaves. citeturn14view0

For **leaf wetness and disease triggers**, several Tier‑1 extension sources provide simulation-grade numeric thresholds. Basil downy mildew needs **≥4 h leaf wetness for infection** and **>7.5 h night RH >95% for sporulation**, with pathogen development bounded between **~11.7–25 °C** (53–77 °F) and an optimum near **20 °C** (68 °F). citeturn3view4 Botrytis blight on greenhouse crops is favoured by **8–12 h moisture film**, **RH ≥93%**, and **~12.8–18.3 °C** (55–65 °F). citeturn12view5 Lettuce downy mildew epidemiology includes a clear trigger: **5–7 h near‑100% RH or leaf wetness**, with outbreaks associated with cool nights (**~4.4–15.6 °C**, 40–60 °F). citeturn13view4 Another extension source adds “fast infection” context: at **~10–22.2 °C** (50–72 °F), infection can occur in **as little as 3 h** when leaves are wet; and preventive logic is framed in terms of morning drying (dry by ~8 a.m. vs wet until ~10 a.m.). citeturn13view3

For **control methods**, Cornell CEA explicitly positions computerised systems (e.g., **Argus/Hortimax/Priva**) plus sensors as core infrastructure that activates **heating, ventilation, and lighting**. citeturn12view0turn3view2 Heat stress mitigation for lettuce is explicitly linked to **shading, evaporative cooling, and ventilation**. citeturn12view4 For humidity management and disease prevention, UConn IPM provides specific operational patterns such as **heat-and-vent cycling 2–3 times/hour** around evening and sunrise, plus **horizontal airflow (HAF) fans** to reduce condensation by preventing leaf surfaces cooling below dew point. citeturn17view5turn17view1 Cornell’s basil downy mildew guidance identifies environmental manipulation steps that map cleanly into component/process controls: **fans to keep leaves moving**, **dehumidification + heat to keep canopy RH <85%**, and **night lighting to reduce spore production**. citeturn12view7

## Corroboration table

Each row is a candidate finding ready to promote into your Layer‑1 parameter library, species stress models, or greenhouse control/component models.

| normalized field name | candidate value or rule | source | source type | trust tier | direct quote / close paraphrase | exact page / section | context tags | recommendation |
|---|---|---|---:|---:|---|---|---|---|
| climate.control.computer_system_required | Use a greenhouse computer control system (e.g., Argus/Hortimax/Priva) to control abiotic environment; sensors feed control actions | Cornell CEA *Hydroponic Lettuce Handbook* PDF citeturn12view0 | University handbook (PDF) | 1 | “A computer control system (example: Argus, Hortimax, Priva) should be used…” citeturn12view0 | p.16 “Computer Technology and Monitoring” | hydroponics/CEA; lettuce; greenhouse | Promote to component/control model |
| climate.targets.lettuce.air_temp_day_night_c | Lettuce air temp setpoints: **24 °C day / 19 °C night** | Cornell CEA Lettuce Handbook citeturn12view1 | University handbook (PDF) | 1 | “Air Temperature 24 C Day/19 C Night…” citeturn12view1 | p.18 “3.3 Set-points” | hydroponics/CEA; lettuce; greenhouse | Promote to species stress model |
| climate.targets.lettuce.solution_temp_c | Lettuce nutrient solution temp: **≤25 °C** (cooling/heat actions around 26/24 °C noted) | Cornell CEA Lettuce Handbook citeturn12view1 | University handbook (PDF) | 1 | “Water Temperature No higher than 25C…” citeturn12view1 | p.18 “3.3 Set-points” | hydroponics/CEA; lettuce; greenhouse | Promote to species stress model + parameter library |
| climate.targets.lettuce.RH_band_pct | Lettuce RH operating band: **min 50%**, **max 70%** | Cornell CEA Lettuce Handbook citeturn12view1 | University handbook (PDF) | 1 | “Relative Humidity minimum 50 and no higher than 70%” citeturn12view1 | p.18 “3.3 Set-points” | hydroponics/CEA; lettuce; greenhouse | Promote to parameter library |
| climate.effect.RH_high_transpiration_nutrients_cooling | High RH reduces transpiration → less nutrient transport and leaf cooling; can increase disease pressure | Cornell CEA Lettuce Handbook citeturn12view2 | University handbook (PDF) | 1 | “High RH… less transport of nutrients… less cooling… encourages… botrytis and mildew.” citeturn12view2 | p.16 “Relative Humidity” | hydroponics/CEA; leafy greens; greenhouse | Promote to parameter library + species stress model |
| climate.targets.lettuce.air_temp_max_day_night_c | Lettuce air temperature should **not exceed 24 °C day / 18 °C night** | UKY CCD *Hydroponic Lettuce Production in Controlled Environments* PDF citeturn12view4 | University extension (PDF) | 1 | “Air temperature… should not exceed… 24 °C… day and… 18 °C… night” citeturn12view4 | p.2 “Growing environment” | hydroponics; lettuce; greenhouse | Promote (split by “setpoint” vs “max”) |
| lettuce.failure.bolting_trigger_heat_fluctuation | Prolonged heat and/or high temperature fluctuations → bolting → bitter/unmarketable | UKY CCD hydro lettuce PDF citeturn12view4 | University extension (PDF) | 1 | “Prone to bolting… prolonged heat… high temperature fluctuations… unmarketable crop.” citeturn12view4 | p.2 “Growing environment” | hydroponics; lettuce; greenhouse | Promote to species stress model |
| climate.control.heat_mitigation_methods | Heat stress mitigation methods: shading, evaporative cooling, ventilation | UKY CCD hydro lettuce PDF citeturn12view4 | University extension (PDF) | 1 | “Implementing shading, evaporative cooling, and ventilation…” citeturn12view4 | p.2 “Growing environment” | hydroponics; lettuce; greenhouse | Promote to component/control model |
| climate.threshold.lettuce.tolerate_low_day_night_c | Lettuce can tolerate **10 °C night / 15 °C day** (winter) but slower crop time | UKY CCD hydro lettuce PDF citeturn3view2 | University extension (PDF) | 1 | “Tolerate nighttime… 10 °C and daytime… 15 °C… will extend… time… to harvest.” citeturn3view2 | p.3 “suboptimal conditions” | hydroponics; lettuce; greenhouse/winter | Promote to species stress model |
| climate.monitoring.pack.recommended_sensors | Recommended sensors: air temp, RH, VPD; IR thermometer for leaf & solution temps; DO meter for root-zone oxygen | UKY CCD hydro lettuce PDF citeturn12view3 | University extension (PDF) | 1 | “Portable climate sensors… air temperature… relative humidity… VPD… IR thermometers… leaf and nutrient solution…” citeturn12view3 | p.1 tools section | hydroponics; lettuce; greenhouse | Promote to component/control model |
| lettuce.stress.tipburn_mechanism_humidity_airflow | Lettuce head blocks airflow → humid micro-environment → low transpiration at tip → reduced Ca transport → necrosis | e‑GRO Edible Alert E406 PDF citeturn14view0 | University-led extension network (PDF) | 1 | “Block air movement… very humid micro‑environment… low transpiration… reduces calcium transport…” citeturn14view0 | p.1 cause section | hydroponics/CEA; lettuce; greenhouse/indoor | Promote to species stress model |
| lettuce.stress.tipburn_prevention_climate_controls | Tipburn prevention relies on climate: dehumidify via heating/venting; increase HAF/vertical fans; shade/cool under high light/heat | e‑GRO E406 PDF citeturn14view1 | University-led extension network (PDF) | 1 | “Modify the growing climate… dehumidify… Increase… airflow fans… shading/cooling…” citeturn14view1 | p.2 “Modify the growing climate” | hydroponics/CEA; lettuce; greenhouse/indoor | Promote to component/control model + species stress model |
| climate.control.spacing_to_reduce_RH_microclimates | Crowding increases canopy RH microclimates; wider spacing dries tissues faster & reduces disease | UKY Plant Pathology PPFS‑GH‑01 PDF citeturn13view0 | University extension (PDF) | 1 | “Overlapping canopies… higher relative humidity… first sites for disease… Wider spacing… dry… quickly.” citeturn13view0 | p.2 “Increase Plant Spacing” | greenhouse/high tunnel; general crops | Promote to component/control model |
| climate.control.ventilation_reduces_RH | Ventilation is important to reduce internal RH; high humidity encourages downy mildew and leaf mould | UKY PPFS‑GH‑01 PDF citeturn13view0 | University extension (PDF) | 1 | “Ventilating… is important… reducing internal relative humidity… encourages… downy mildew…” citeturn13view0 | p.1 Fig 4 caption text | greenhouse/high tunnel; disease prevention | Promote to component/control model |
| humidity.physics.dew_point_condensation_leaf_wetness | Night cooling to dew point → condensation droplets on leaves → promotes fungal spore germination | UConn IPM “Reduce Greenhouse Humidity” citeturn12view6 | University extension webpage | 1 | “At night… cools to the dewpoint… water droplets… leaves… promotes… Botrytis… powdery mildews.” citeturn12view6 | page intro | greenhouse; general disease prevention | Promote to parameter library |
| humidity.control.heat_vent_dehumidify_principle | Vent humid air + replace with cooler/drier outside air; when warmed it absorbs more moisture | UConn humidity page citeturn17view0 | University extension webpage | 1 | “Exhaust… replace… cooler, dryer… outside air… when warmed will absorb more moisture…” citeturn17view0 | “Vent the humid air” | greenhouse; general | Promote to component/control model |
| humidity.control.rule_of_thumb_20F | Rule: for each **20 °F** rise in dry-bulb, moisture capacity doubles and RH halves (within greenhouse range) | UConn humidity page citeturn17view0 | University extension webpage | 1 | “For every 20 deg F rise… capacity… doubles and… RH… reduced by one-half.” citeturn17view0 | “Vent the humid air” | greenhouse; psychrometrics | Promote to parameter library |
| humidity.control.antidrip_glazing | Anti-drip plastic/wetting agent reduces dripping onto plants (reduces leaf wetness spread) | UConn humidity page citeturn17view0 | University extension webpage | 1 | “Anti-drip Plastic… moisture… drain… rather than forming droplets and dripping onto the plants.” citeturn17view0 | “Anti-drip Plastic” | greenhouse; disease prevention | Promote to component/control model |
| airflow.effect.canopy_RH_stratification | In dense canopies, RH can be **20–40% higher** than air above; continuous circulation reduces stratification | UConn humidity page citeturn17view1 | University extension webpage | 1 | “Relative humidity can be 20%–40% higher… Continuous air circulation helps…” citeturn17view1 | “Air Movement” | greenhouse; canopy microclimate | Promote to parameter library + simulation hook |
| airflow.control.HAF_specs | HAF fans: small fans (~**1/15 hp**, **12–20 inch**) run continuously except when exhaust fans are on | UConn humidity page citeturn17view1 | University extension webpage | 1 | “HAF… small fans (1/15 horsepower, 12” to 20”…). Fans are run continuously…” citeturn17view1 | “HAF system” | greenhouse; airflow control | Promote to component/control model |
| humidity.control.VPD_preferred_metric | VPD is a better humidity measure than RH; some greenhouse computers control humidity based on VPD | UConn humidity page citeturn17view2 | University extension webpage | 1 | “Vapor pressure deficit… gives a better measure… Some… systems… control… based on VPD…” citeturn17view2 | “Control” | greenhouse; control systems | Promote to parameter library + simulation hook |
| disease.trigger.botrytis_moisture_RH_temp | Botrytis favourable conditions: **8–12 h moisture film**, **RH ≥93%**, **55–65 °F (12.8–18.3 °C)** | UConn Botrytis factsheet PDF citeturn12view5 | University extension (PDF) | 1 | “Film of moisture for 8 to 12 hours… RH of 93%… temperatures 55° and 65°F.” citeturn12view5 | p.1 “Favorable Conditions” | greenhouse; disease trigger | Promote to species stress model + parameter library |
| disease.control.botrytis_irrigation_timing | Water in morning to shorten leaf wetness; avoid end-of-day leaf wetness | UConn Botrytis factsheet citeturn13view5 | University extension (PDF) | 1 | “Always water in the morning… leaves stay dry… Avoid watering… long periods… end of the day.” citeturn13view5 | p.2 cultural practices | greenhouse; disease prevention | Promote to component/control model |
| disease.control.botrytis_heat_vent_cycle | Heat+vent dehumidification pattern: heat and vent **2–3 times per hour** after sunset and at sunrise | UConn Botrytis factsheet citeturn17view4 | University extension (PDF) | 1 | “Heat and vent two or three times per hour… evening… and… morning at sunrise.” citeturn17view4 | p.3 humidity tips | greenhouse; dehumidification schedule | Promote to component/control model |
| disease.control.botrytis_HAF_dewpoint_logic | HAF airflow reduces condensation by preventing leaf surface air cooling below dew point | UConn Botrytis factsheet citeturn17view5 | University extension (PDF) | 1 | “HAF… reduce condensation… mixed air… does not cool below the dew point…” citeturn17view5 | p.3 | greenhouse; airflow; leaf wetness | Promote to component/control model |
| disease.trigger.basil_downy_mildew_leafwetness_RH_temp | Basil downy mildew: infection needs **≥4 h leaf wetness**; sporulation needs **>7.5 h night RH >95%**; optimum **68 °F (20 °C)**; no growth **<53 °F (11.7 °C)** or **>77 °F (25 °C)** | UConn basil downy mildew PDF citeturn3view4 | University extension (PDF) | 1 | “Needs at least 4 hours… leaf wetness… more than 7.5 hours… >95%… Optimum… 68°F…” citeturn3view4 | p.1 “Conditions Favoring…” | greenhouse; basil; disease trigger | Promote to species stress model + event triggers |
| disease.control.basil_downy_mildew_RH_target | Control target to suppress basil downy mildew: keep canopy RH **below 85%**; use fans, dehumidification + heat | Cornell (McGrath) basil downy mildew greenhouse PDF citeturn12view7 | University extension bulletin (PDF) | 1 | “Dehumidification… and heat to keep… RH… below 85%” citeturn12view7 | p.1 | greenhouse; basil; disease prevention | Promote to component/control model |
| disease.control.basil_downy_mildew_night_lighting | Night lighting can be used to prevent or reduce spore production (basil downy mildew management) | Cornell basil downy mildew greenhouse PDF citeturn12view7 | University extension bulletin (PDF) | 1 | “Lighting at night to prevent spore production.” citeturn12view7 | p.1 | greenhouse; basil; disease prevention | Promote to component/control model |
| climate.targets.basil.air_temp_ideal_c | Basil air temperature: “ideal” around **27.5 °C**; also referenced “optimal air temp ~26 °C” | HortScience (OSU) open-access basil NFT study citeturn11view0turn11view1 | Peer‑reviewed journal (PDF) | 2 | “27.5 °C is considered the ideal air temperature…” citeturn11view0 | p.3 discussion | hydroponics; basil; greenhouse | Promote (split by “optimal vs ideal”; tier‑2) |
| climate.tradeoff.rootzone_heating_vs_air_temp | Root-zone heating can achieve comparable root growth under suboptimal air temperatures (reduce air-heating energy need) | HortScience basil NFT study citeturn11view0 | Peer‑reviewed journal (PDF) | 2 | “Root zone heating allows for… root growth under suboptimal air temperatures.” citeturn11view0 | p.3 discussion | hydroponics; basil; greenhouse | Promote to component/control model (tier‑2) |
| climate.targets.basil.rootzone_temp_c | In NFT basil, recommended nutrient solution/root-zone water temp **~27.5 °C** for growth across most cultivars | HortScience basil NFT study citeturn10view0 | Peer‑reviewed journal (PDF) | 2 | “A 27.5 °C water temperature would be recommended…” citeturn10view0 | p.1 abstract | hydroponics; basil; greenhouse; root-zone | Promote to species stress model (tier‑2) |
| climate.monitoring.lettuce_air_water_must_control | Both air and water temperature should be monitored and controlled | Cornell CEA Lettuce Handbook citeturn12view2 | University handbook (PDF) | 1 | “Both the air and the water temperature must be monitored and controlled.” citeturn12view2 | p.16 temperature section | hydroponics; lettuce; greenhouse | Promote to parameter library + component/control model |
| climate.tradeoff.lettuce_optimum_air_and_water_24C | In floating lettuce system study, optimum dry weight production: **24 °C air and 24 °C water**; root temperature contributes to quality | Cornell CEA Lettuce Handbook (embedded study abstract) citeturn4view2 | University handbook citing peer‑reviewed study | 1 | “Optimal… 24 deg C air and 24 deg C water… Root temperature… contributed…” citeturn4view2 | p.42–43 embedded abstract | hydroponics; lettuce; root vs shoot | Promote (as “study anchor”) |
| disease.trigger.lettuce_downy_mildew_cool_nights_RH_wetness | Lettuce downy mildew: favoured by cool temps; outbreaks when nights **40–60 °F (4.4–15.6 °C)**; needs **5–7 h** near 100% RH or leaf wetness | UF/IFAS lettuce downy mildew PDF citeturn13view4 | University extension (PDF) | 1 | “Nighttime… 40 to 60°F… Five to 7 hours… near 100% RH… or leaf wetness…” citeturn13view4 | p.1 “Epidemiology” | greenhouse/field; lettuce; disease trigger | Promote to species stress model + event triggers |
| disease.trigger.lettuce_downy_mildew_fast_infection_3h | Downy mildew of lettuce: at **50–72 °F (10–22.2 °C)** infection can occur in as little as **3 h** when leaves are wet | University of Arizona Cooperative Extension PDF citeturn13view3 | University extension (PDF) | 1 | “At… 50 to 72°F, infection can occur in as little as 3 hours when leaves are wet…” citeturn13view3 | p.2 bullets | greenhouse/field; lettuce; disease trigger | Promote (note: infection-only context) |
| disease.trigger.lettuce_downy_mildew_morning_drying_rule | If leaves dry by **~8 a.m.** no infection; if wetness persists until **~10 a.m.** or later infection occurs | University of Arizona Cooperative Extension PDF citeturn13view3 | University extension (PDF) | 1 | “No infection… dry by 8 a.m… infections occur… do not dry until 10 a.m…” citeturn13view3 | p.2 bullets | greenhouse/field; lettuce; leaf wetness timing | Promote to event triggers |
| climate.failure.mode_summary | Climate-linked failure modes: lettuce bolting (heat/fluctuations), lettuce tipburn (humid/low airflow), basil downy mildew (wet leaves + high night RH), Botrytis (long leaf wetness + high RH), lettuce downy mildew (cool + wet) | Multi-source synthesis citeturn12view4turn14view0turn3view4turn12view5turn13view4 | Synthesis of Tier‑1 inputs | 1–2 | Close paraphrase of thresholds in sources | Compilation | greenhouse; aquaponics-compatible | Promote (as model-level mapping) |

## Contradictions table

Where values differ, sources usually describe **different operational goals** (optimising vs “do not exceed”), **different system contexts** (greenhouse vs indoor, cultivar differences), or **different biological phases** (infection vs sporulation).

| field | conflicting candidates | sources | reason | recommended action |
|---|---|---|---|---|
| climate.targets.lettuce.air_temp_day_night_c | 24/19 °C setpoint vs “should not exceed” 24/18 °C | Cornell CEA setpoints citeturn12view1 vs UKY CCD guidance citeturn12view4 | Cornell expresses a default setpoint; UKY expresses an upper constraint for quality risk management. | Split: store `lettuce.air_temp.setpoint_day/night` and `lettuce.air_temp.max_day/night`. |
| lettuce.cold_tolerance.day_night_c | “Should not exceed 24/18 °C” vs “can tolerate 15 °C day / 10 °C night (winter)” | UKY CCD citeturn12view4turn3view2 | Different management regimes: comfort/quality setpoints vs survival/production under resource constraints. | Split into `preferred` vs `tolerated` and add growth‑rate penalty under tolerated lows. |
| basil.air_temp_target_c | “Optimal air temp ~26 °C” vs “ideal air temp 27.5 °C” | HortScience NFT basil study citeturn11view1turn11view0 | The paper cites different references/framings (“optimal” vs “ideal”). | Promote as a range: `basil.air_temp.preferred ≈26–27.5 °C` with cultivar/energy cost notes. |
| lettuce_downy_mildew.wetness_duration_hours | “5–7 h high humidity/leaf wetness required” vs “infection can occur in as little as 3 h wet leaves (50–72 °F)” | UF/IFAS citeturn13view4 vs Arizona CE citeturn13view3 | Likely different endpoints: combined infection+sporulation requirement vs minimum infection window under certain temperatures and dawn timing. | Keep both; label endpoints: `infection_min_hours` vs `infection+sporulation_hours` and gate by temperature context. |
| humidity.targets | Lettuce RH cap 70% vs basil downy mildew management target canopy RH <85% vs sporulation threshold >95% | Cornell lettuce setpoints citeturn12view1, Cornell basil DM citeturn12view7, UConn basil DM citeturn3view4 | Different crops and different objectives: lettuce quality, basil disease suppression, pathogen sporulation conditions. | Split by crop and by purpose: `RH_target`, `RH_management_ceiling`, `RH_pathogen_threshold`. |

## Simulation-hook-ready fields

These are the **lowest-friction canonical fields** to standardise across greenhouse scenarios and crop stress models. Each maps to at least one Tier‑1/2 candidate above.

**Environment state variables**
- `climate.air_temp_day_c`, `climate.air_temp_night_c` (lettuce setpoints and “max” values) citeturn12view1turn12view4  
- `climate.solution_temp_c` (lettuce ≤25 °C; lettuce optimum 24 °C water; basil NFT RZT 23/27.5/31 °C study anchors) citeturn12view1turn4view2turn10view0  
- `climate.RH_pct` plus optional derived `climate.canopy_RH_pct` (canopy RH 20–40% higher under stratification) citeturn17view1  
- `climate.VPD_kPa` (preferred control quantity vs RH; also good for “transpiration capacity” proxy) citeturn17view2  
- `climate.leaf_wetness_hours` (daily/nightly) citeturn3view4turn12view5turn13view4  
- `climate.dew_point_margin_c` (e.g., `leaf_temp - dew_point_temp`), used to proxy condensation/leaf wetness risk citeturn12view6turn17view5  
- Optional monitoring proxies: `climate.leaf_temp_c` and `climate.rootzone_DO_mg_L` (UKY recommends IR thermometers and DO meters for root zones) citeturn12view3  

**Control/actuator states**
- `control.heating_on`, `control.ventilation_on` (explicitly recommended for humidity reduction and disease control) citeturn17view0turn17view4  
- `control.evaporative_cooling_on`, `control.shade_on` (lettuce heat stress management) citeturn12view4  
- `control.dehumidification_on` (basil downy mildew management; general RH control) citeturn12view7  
- `control.HAF_fans_on` with basic metadata `control.HAF_fan_spec` (small fans, continuous operation) citeturn17view1turn17view5  
- `control.night_lighting_on` (basil downy mildew suppression) citeturn12view7  
- `control.irrigation_time_of_day` (morning watering to reduce leaf wetness duration; avoid end-of-day wetness) citeturn13view5  

**Disease/quality-risk derived indices**
- `risk.lettuce_bolting` (heat + fluctuations) citeturn12view4  
- `risk.lettuce_tipburn` (high RH + low airflow + rapid growth) citeturn14view0turn14view1  
- `risk.basil_downy_mildew` (leaf wetness + nighttime RH + temperature window) citeturn3view4turn12view7  
- `risk.botrytis` (leaf wetness film duration + RH + cool temps + poor airflow) citeturn12view5turn17view5  
- `risk.lettuce_downy_mildew` (cool nights + wetness hours; morning drying rule) citeturn13view4turn13view3  

## Best excerpts to ingest into a local pipeline

Each excerpt is short and maps directly to a JSON field or an event trigger.

### Excerpt 1
- excerpt_text: “Air Temperature 24 C Day/19 C Night… Relative Humidity minimum 50 and no higher than 70%.” citeturn12view1  
- mapping: `climate.targets.lettuce.air_temp_day_night_c`, `climate.targets.lettuce.RH_band_pct`  
- why high-value: single authoritative setpoint block for lettuce CEA operations.  
- recommended use: parameter library defaults + lettuce stress model baseline.

### Excerpt 2
- excerpt_text: “High RH… less transport of nutrients… less cooling… encourages the growth of botrytis and mildew.” citeturn12view2  
- mapping: `climate.effect.RH_high_transpiration_nutrients_cooling`  
- why high-value: directly links RH → physiology → disease pressure.  
- recommended use: transpiration/uptake modifier + disease risk multiplier.

### Excerpt 3
- excerpt_text: “Lettuce… becomes prone to bolting… prolonged heat and/or high temperature fluctuations… unmarketable crop.” citeturn12view4  
- mapping: `lettuce.failure.bolting_trigger_heat_fluctuation`  
- why high-value: crisp failure condition with gameplay consequences (quality loss).  
- recommended use: lettuce event trigger + scoring penalty.

### Excerpt 4
- excerpt_text: “Block air movement and create a very humid micro-environment… low transpiration… reduces calcium transport…” citeturn14view0  
- mapping: `lettuce.stress.tipburn_mechanism_humidity_airflow`  
- why high-value: establishes tipburn as microclimate/airflow failure, not simply nutrient deficiency.  
- recommended use: tipburn risk model tied to RH + airflow + head stage.

### Excerpt 5
- excerpt_text: “Needs at least 4 hours of leaf wetness… more than 7.5 hours… humidity (>95%) at night…” citeturn3view4  
- mapping: `disease.trigger.basil_downy_mildew_leafwetness_RH_temp`  
- why high-value: fully simulation-grade numeric thresholds.  
- recommended use: basil downy mildew infection/sporulation event triggers.

### Excerpt 6
- excerpt_text: “Dehumidification of air and heat to keep relative humidity in the plant canopy below 85%, and lighting at night…” citeturn12view7  
- mapping: `disease.control.basil_downy_mildew_RH_target`, `disease.control.basil_downy_mildew_night_lighting`  
- why high-value: maps disease management to actionable greenhouse controls.  
- recommended use: control-model actions + “management investment” mechanics.

### Excerpt 7
- excerpt_text: “Film of moisture for 8 to 12 hours, relative humidity of 93%… temperatures between 55° and 65°F.” citeturn12view5  
- mapping: `disease.trigger.botrytis_moisture_RH_temp`  
- why high-value: high-impact general fungal trigger for many crops (including herbs).  
- recommended use: Botrytis risk function for mixed-crop greenhouse.

### Excerpt 8
- excerpt_text: “Five to 7 hours of high humidity (near 100% RH) or leaf wetness… required…” citeturn13view4  
- mapping: `disease.trigger.lettuce_downy_mildew_cool_nights_RH_wetness`  
- why high-value: numeric wetness/humidity trigger for lettuce downy mildew.  
- recommended use: lettuce downy mildew event trigger in cool/wet scenarios.

### Excerpt 9
- excerpt_text: “At temperatures between 50 to 72°F, infection can occur in as little as 3 hours when leaves are wet…” citeturn13view3  
- mapping: `disease.trigger.lettuce_downy_mildew_fast_infection_3h`  
- why high-value: enables “rapid escalation” modelling under favourable conditions.  
- recommended use: shorten latency period in disease model when temp + wetness align.

### Excerpt 10
- excerpt_text: “Vapor pressure deficit… gives a better measure of humidity… control… based on VPD…” citeturn17view2  
- mapping: `humidity.control.VPD_preferred_metric`  
- why high-value: justifies VPD as a first-class simulation variable.  
- recommended use: greenhouse controller mode: RH-based vs VPD-based.

## Starter event triggers for greenhouse climate and disease

These are **Layer‑1 event rules** designed to be simple, explainable, and directly backed by the corroborated thresholds above.

### Temperature-driven crop-quality events
- **Lettuce bolting risk escalation**: if `climate.air_temp_day_c > 24` for sustained periods **or** `daily_temp_variability` is high during warm conditions, increase `risk.lettuce_bolting` and shorten harvest window; when triggered, apply bitterness/unmarketable penalty. citeturn12view4  
- **Lettuce slow-growth penalty (winter tolerance mode)**: if `climate.air_temp_night_c ≤ 10` and `climate.air_temp_day_c ≈ 15`, allow continued growth but apply a time-to-harvest multiplier (slower development). citeturn3view2  
- **Solution temperature stress guardrail (lettuce raft/DWC contexts)**: if `climate.solution_temp_c > 25`, raise stress risk; if targeting optimum growth-quality mode, bias towards `solution_temp_c ≈ 24` alongside `air_temp_day_c ≈ 24`. citeturn12view1turn4view2  

### Humidity/airflow-driven physiological disorder events
- **Lettuce tipburn onset**: require combination of (a) low transpiration proxy (high RH / low VPD) and (b) poor airflow proxy and (c) fast growth/head stage. Mechanism is explicitly tied to humid micro-environment and low Ca transport to young leaves. citeturn14view0turn14view1  
- **Canopy stratification penalty**: if `HAF_fans_on = false` and canopy is dense, set `canopy_RH = greenhouse_RH + 20–40%` to represent stratification; increases Botrytis/mildew and leaf-wetness persistence risk. citeturn17view1turn12view2  

### Leaf wetness and pathogen events
- **Basil downy mildew infection**: if `leaf_wetness_hours ≥ 4` and `temp_c` within **~11.7–25 °C**, mark infection possible; if additionally `night_RH > 95%` for `>7.5 h`, allow sporulation and rapid spread. citeturn3view4  
- **Basil downy mildew suppression action**: if risk rising, allow player/controller to reduce canopy RH below **85%** (dehumidification + heat) and keep leaves moving (fans) and optionally enable night lighting to suppress spore production. citeturn12view7  
- **Botrytis trigger**: if `leaf_wetness_film_hours ≥ 8` and `RH ≥ 93%` and `temp_c ≈ 12.8–18.3`, increase Botrytis risk sharply; apply management action “water in morning” and “heat+vent cycles + HAF fans” to reduce wetness duration and condensation. citeturn12view5turn13view5turn17view5  
- **Lettuce downy mildew trigger**: if `night_temp_c ≈ 4.4–15.6` and `leaf_wetness_hours ≥ 5` (or high RH near saturation) then risk increases; “fast infection” override: if `temp_c ≈ 10–22.2` and wet leaves persist ≥3h, allow early lesions; enforce “morning drying” logic (dry by ~8 a.m. vs wet until ~10 a.m.). citeturn13view4turn13view3  

### Control-system behaviour events
- **Dehumidification via heat+vent cycles**: implement a control pattern that can run **2–3 cycles/hour** after sunset and at sunrise (energy cost trade-off), reducing RH and leaf wetness persistence. citeturn17view4turn17view0  
- **VPD-based controller mode**: if `controller_mode = VPD`, use VPD as the primary humidity metric (with RH as secondary), consistent with greenhouse engineering practice notes. citeturn17view2