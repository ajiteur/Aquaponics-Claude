# Aquaponics equipment inventory: Monitoring and control, Lighting, Propagation

Scope note for the report writer: evidence-first inventory notes, not a farm design. All prices were read on 2026-11-25. No currency was converted, and no price, efficacy, lifetime or sizing number was estimated or filled in. Where a field is unknown it says "not found". Each value carries a tier (tier_1 = peer-reviewed / government / university research station; tier_2 = extension, research institute, industry report, manufacturer datasheet; tier_3 = retail/B2B listing, forum, blog, video), a confidence with a one-line reason, and corroboration status. Scale labels used: hobby (<20 m2 grow area), small commercial (20-500 m2), commercial (>500 m2). Scale fit and system-type fit are agent inferences unless a source is cited, and they are listed under Inferences.

Research constraint: during this session the shared web-fetch budget (100 fetches/hour across all agents) ran out repeatedly. Several high-value pages were found but could not be read: the Signify GreenPower LED toplighting force datasheet, IndiaMART LED grow-light and test-kit listings, the Atlas Scientific DO probe page, and hobby LED retailer pages. The Gavita CT1930e spec sheet and the WUR LED vs SON-T page were read on later retries. They are listed under Gaps with URLs so a later pass can read them. Search results returned titles and URLs only, with no snippets, so no value below comes from a search snippet.

Repo context (for mapping, not evidence): `aquaponics-project/data/knowledge/components/component_library.json` already has placeholder entries `grow_light` ("Placeholder light power and economics."), `ph_sensor` (failure modes include `probe_fouling`), `do_sensor` and `temperature_sensor` (failure modes include `sensor_drift`, `probe_disconnect`). These notes are candidate inputs for those entries, not canon.

## 1. Monitoring and control: item records (function, fit, specs, maintenance, failure modes)

### Takeaway
Manufacturer and extension sources agree that pH and EC probes need regular calibration (Bluelab: monthly; Atlas Scientific lab-grade pH in fish tank or hydroponic water: yearly for the first two years, then about every six months) and must be kept wet. Optical DO sensors trade higher price and 2-4x slower response for no flow requirement, less drift and about 12-month cap replacement, against about 6-month tip replacement for galvanic sensors (Horiba). FAO's aquaponics manual sets the testing rhythm at weekly colorimetric tests, with ammonia and nitrite mainly for new units.

### Cited Findings

#### 1a. Water-test regime and test kits (FAO 589 baseline)
Source: FAO Fisheries and Aquaculture Technical Paper 589, *Small-scale aquaponic food production* (Somerville et al., 2014), Chapter 3 "Water testing", read via FarmHub's reproduction of the chapter. Tier: tier_1, following the repo's distilled research pack, which treats the FAO manual as a "Tier 1 primary" source (`distilled research pack.md` line 590). Confidence: medium, because it was read through a third-party reproduction rather than the FAO PDF itself. Corroboration: see each row.

| Field | Value | Source | Tier | Confidence (reason) | Corroboration |
|---|---|---|---|---|---|
| Test frequency | "it is recommended to perform water tests once per week" | [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/3-water-quality-in-aquaponics/water-testing/) | tier_1 | medium (secondary host of FAO text) | single_source in this pass |
| Mature systems | "mature and seasoned aquaponic units will have consistent water chemistry and do not need to be tested as often"; then "water testing is only needed if a problem is suspected" | [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/3-water-quality-in-aquaponics/water-testing/) | tier_1 | medium (same) | single_source |
| Weekly priority parameters | pH, nitrate, carbonate hardness (KH), water temperature, logged weekly; ammonia and nitrite "extremely helpful", especially in new units | [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/3-water-quality-in-aquaponics/water-testing/) | tier_1 | medium | single_source |
| Kit coverage | Freshwater kits cover "pH, ammonia, nitrite, nitrate, GH, and KH" | same | tier_1 | medium | single_source |
| Minutes per test (labour) | each test "5-10 drops of a reagent into 5 millilitres of aquaponic water" and takes no more than five minutes | same | tier_1 | medium (time is a stated maximum per test, not a measured mean) | single_source |
| Method trade-off | colour-coded kits "readily available and easy to use"; digital pH or nitrate meters "relatively expensive and very accurate"; test strips "cheapest and moderately accurate" | same | tier_1 | medium | single_source |
| Daily checks | daily fish and plant health observation "is not a substitution for water testing" | same | tier_1 | medium | single_source |
| DO in the test regime | not mentioned on this page | same | - | - | not found |

Hydroponic counterpart (tier_2 extension): University of Kentucky CCD-CP-63, *Hydroponic Lettuce Production in Controlled Environments* (Sharma, Leonberger, Gauthier, Ying; 2025 revision of the 2016 original). For liquid systems (DWC, NFT), continuous monitoring of nutrient-solution pH and EC is "essential"; reservoir top-up every few days; full or partial solution replacement every 3 to 4 weeks. It recommends "calibrated electrical conductivity (EC) and pH meters", plus a dissolved oxygen meter, a light meter or quantum sensor, and infrared thermometers, with no brand named. Leachate in substrate systems with pH below 5.5 or above 7.0, or EC below 0.8 or above about 2.5 mS/cm, should prompt adjustment. — [UKy CCD-CP-63](https://ccd.uky.edu/sites/default/files/2026-02/ccd-cp-63_hydrolettuce-updated_accessible.pdf). Tier_2; confidence high (current university extension publication); single_source in this pass.

Context split: FAO's weekly manual testing applies to small-scale coupled aquaponics; UKy's "continuous monitoring is essential" applies to hydroponic lettuce in DWC or NFT. These are different system contexts, not a contradiction.

#### 1b. Handheld pH / EC pens and meters

**Item: Bluelab pH Pen / pH PenPlus / OnePen / Combo Meter (handheld, NZ brand, EU store)**
- function: spot measurement of pH (pen), pH+EC+temperature (OnePen, Combo Meter)
- system_types / grow_methods: no system restriction stated by the manufacturer; see Inferences
- calibration: "Calibration is recommended once a month, or more frequently if the instrument is used heavily"; the on-screen calibration check mark stays 30 days; pH two-point calibration, pH 7.0 first then 4.0 or 10.0 — [Bluelab care, calibration and maintenance](https://eu.bluelab.com/pages/care-calibration-maintenance). Tier_2 (manufacturer); confidence high (manufacturer's own procedure); single_source.
- storage and maintenance: store pH probe in KCl storage solution; "Fresh application is recommended once per week"; a dried-out tip should be rehydrated in KCl for 24 hours and then given a two-point recalibration; rinse after each use; clean the EC probe before calibrating; check EC with 2.77 EC solution — [Bluelab care page](https://eu.bluelab.com/pages/care-calibration-maintenance). Tier_2; high; single_source.
- probe lifetime: not stated on the care page (not found).
- warranty (Guardian Monitor listing, as an indicator of probe warranty): "2-year limited warranty; 6-months for the Bluelab pH Probe" — [Bluelab Guardian Monitor Wi-Fi](https://eu.bluelab.com/bluelab-guardian-monitor-wi-fi). Tier_2; high; single_source.
- prices: see Section 4.

**Item: Hanna HI98115 Groline hydroponics pH tester**
- specs: range 0.00-14.00 pH; accuracy ±0.2 pH; resolution 0.01 pH; automatic one- or two-point calibration; replaceable HI1271 electrode; battery about 1000 hours continuous use (CR2032) — [Hanna Service EU listing](https://hannaservice.eu/ph-tester-groline-hi98115-product). Tier_3 (retail listing of manufacturer specs); confidence medium (distributor page, not the datasheet); single_source.
- note: accuracy ±0.2 pH with 0.01 resolution means the display resolution is finer than the stated accuracy.

**Item: Hanna HI98107 pHep pocket pH tester**
- specs: ±0.1 pH accuracy, 0.1 pH resolution, 0-14 pH, 0-50 °C operating, 95 g, 41 × 175 × 23 mm, waterproof and floats, renewable junction, one- or two-point automatic calibration — [RS Components NL](https://nl.rs-online.com/web/p/ph-meters/0218970). Tier_3; medium; single_source.
- conflict: battery life is "1000 hours" in the description and "700 h" in the spec table on the same page. Both values are kept and not averaged — [RS Components NL](https://nl.rs-online.com/web/p/ph-meters/0218970). Corroboration: conflicting.

#### 1c. Continuous probes, monitors and controllers

**Item: Atlas Scientific Lab Grade pH probe (ENV-40-pH), for DIY/IoT (EZO circuit, Arduino/ESP32/Raspberry Pi)**
- construction: double-junction Ag/AgCl with EXR glass; range 0-14; stated accuracy "+/– 0.002"; -5 to 99 °C; max 100 PSI; can be "fully submerged in fresh or salt water, up to the SMA connector indefinitely"; max depth 70 m; 12 × 150.6 mm — [Atlas Scientific pH probe datasheet (v4.8, RobotShop CDN)](https://cdn.robotshop.com/media/A/Atl/RB-Atl-39/pdf/atlas-scientific-ph-probe-v48-datasheet.pdf). Tier_2 (manufacturer datasheet); confidence medium. Accuracy of ±0.002 pH is an unusually tight manufacturer claim and was not checked independently. single_source.
- lifetime: "Life expectancy ~2.5 Years +"; "Storage Life ~5 Years". Basis: manufacturer claim, no test method given — same datasheet. Tier_2; medium (manufacturer claim, method not stated); single_source.
- calibration: in weakly acidic or basic water such as "fish tanks or hydroponics", recalibrate "once per year for the first two years", then about every six months; monthly or per batch in strong acids or bases — same datasheet. Tier_2; medium; conflicting with Bluelab's monthly guidance (see Section 5; the two are kept separate, different products and use patterns).
- price: not found (the Atlas Scientific product page was not readable within the fetch budget).

**Item: Bluelab Guardian Monitor Wi-Fi (continuous pH, EC, temperature monitor with alarms)**
- function: continuous display of "pH, conductivity (EC), and temperature"; "High/low pH, temperature and conductivity alarms"; built-in Wi-Fi with Edenic app for "Instant alarm alerts to your phone", "Remote monitoring", "History reporting" — [Bluelab EU](https://eu.bluelab.com/bluelab-guardian-monitor-wi-fi). Tier_2 for function (manufacturer); high; single_source.
- power: "110 – 240 VAC (Mains powered)"; adaptor "Output 5 VDC 1.5 A". Rated power consumption: not stated (not found). Duty: continuous (24 h/day) by design, as an agent inference from its continuous-monitor function.
- probe: pH probe replaceable (BNC); replacement interval not stated (not found).
- warranty: 2-year limited; 6 months on the pH probe — same page.

**Item: Bluelab controllers and dosing (pH Controller Wi-Fi, Pro Controller Wi-Fi, IntelliDose Controller Kit, PeriPod M3/M4/L3)** — listed with prices on the [Bluelab EU pH collection](https://eu.bluelab.com/collections/ph); functional specs not read in this pass (not found).

**Item: Hyperfarms "Hydroponics Nutrient Controller" (Bengaluru, Karnataka)**
- specs: pH range 0-14; 230 V AC; outputs RS485, relay, Modbus RTU; 4 relays. The page does not say whether it doses for pH, EC or both, and does not mention Wi-Fi — [IndiaMART, Hyperfarms](https://m.indiamart.com/hyperfarms-bengaluru/hydroponics-nutrient-controller.html). Tier_3; confidence low (B2B listing, specs incomplete, and the seller is described as both "Proprietorship-based" and "Private Limited"); single_source.

**Item: Greenhouse climate and fertigation computers (Priva, Hoogendoorn)** — not found in this pass (no page read).

#### 1d. Dissolved oxygen meters: optical vs galvanic
Source: Horiba technical tip "Galvanic vs Optical Dissolved Oxygen Sensors" — [Horiba](https://www.horiba.com/int/water-quality/support/technical-tips/electrodes/galvanic-vs-optical-dissolved-oxygen-sensors/). Tier_2 (manufacturer technical note); confidence medium (a manufacturer that sells both types, qualitative comparison); single_source in this pass.

| Factor | Galvanic | Optical (luminescent) |
|---|---|---|
| Warm-up | "Not required" | "Not required" |
| Stirring/flow | "Required" | "Not required" |
| Oxygen consumption | oxygen is "reduced and consumed at the cathode" | not stated |
| Consumable replacement | DO tip "every after 6 months depending on the application and handling"; electrolyte "can be used for a long time" | sensor cap "every after 12 months depending on the application and handling" |
| Calibration | "frequent calibration is required" (drifts) | "regular calibration is still recommended" (little drift) |
| Response time | "Faster than optical DO sensor" | "takes 2-4x longer than electrochemical DO sensor" |
| Cost | "Cheaper than optical" | "More expensive than electrochemical" |
| Lifetime | "Shorter than optical" | "Longer than electrochemical" |

DO meter prices: not found (no NL or India DO-meter listing was readable in this pass).

#### 1e. Temperature sensors, alarms (power failure, water level, low DO), IoT
- High/low pH, EC and temperature alarms with phone alerts are built into the Bluelab Guardian Monitor Wi-Fi (see 1c) — [Bluelab EU](https://eu.bluelab.com/bluelab-guardian-monitor-wi-fi). It has no DO alarm, because DO is not one of its measured parameters.
- Dedicated power-failure alarms, water-level float alarms and stand-alone low-DO alarms: not found (no listing read).
- DIY ESP32/Arduino monitors: several student and conference papers were found (for example [UBC ELEC 491 Aquaponics Monitoring and Control System final report](https://sustain.ubc.ca/sites/default/files/seedslibrary/ELEC_491_Aquaponics%20Monitoring%20and%20Control%20System_FinalReport.pdf) and a [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC7662340)), but none were read, so they supply no values here.

### Inferences
- System and grow-method fit (agent inference, not sourced): handheld pH/EC pens and colorimetric kits apply to all listed system types (coupled, decoupled, recirculating hydroponics) and grow methods (DWC, NFT, media bed, Dutch bucket, towers, ebb and flow). Ammonia and nitrite kits matter mostly in fish-containing loops (coupled aquaponics, and the fish side of decoupled systems), because FAO frames them as diagnostic for new aquaponic units.
- Scale fit (agent inference): colorimetric kits and pens suit hobby and small commercial; continuous monitors with alarms (Guardian class) suit small commercial and above, where unattended hours exist; dosing controllers (IntelliDose, PeriPod, Modbus controllers) suit small commercial to commercial; Priva/Hoogendoorn-class climate computers are typically commercial greenhouse systems, but no source was read to confirm this.
- DO sensor choice (inference from Horiba): galvanic probes read in flowing water only, so a galvanic probe dropped into a still sump may under-read. Optical probes avoid this, at higher price and slower response. This is context on measurement, not a claim about aeration adequacy.
- Calibration labour: the sources give frequencies (weekly kit tests, monthly pen calibration) and a ≤5-minute per-test FAO figure for kits. No source gave minutes per calibration, so calibration labour time stays "not found".
- Failure modes (inference from manufacturer care guidance, effects not quantified): a pH probe allowed to dry out or left uncalibrated past the interval drifts; a controller acting on a drifting probe will dose acid or base to the wrong target, and the plant/fish effect depends on the size of the error. This is a monitoring-reliability point, not a fish-safety claim.

### Gaps
- Price of Atlas Scientific probes and EZO kits, DFRobot Gravity sensors and other DIY modules in EU and India: not found (fetch budget).
- DO meter prices (Hanna HI9147/HI98193, YSI ProODO, Lutron, cheap galvanic pens) in NL and India: not found.
- Priva, Hoogendoorn, Ridder climate and fertigation computer specs and prices: not found.
- Power-failure alarms, float-switch water-level alarms, low-DO alarms (products and prices): not found.
- Tetra, JBL and Hach test kit specs (tests per kit, resolution, minutes per test): not found. API kit specs were only seen as search-result titles (for example "800 Test"), which is not enough to record.
- Probe replacement interval from Bluelab (not on the care page) and Hanna: not found.
- Peer-reviewed or extension evaluation of cheap pH pens or ESP32 sensor drift: found but unread (see 1e URLs).

## 2. Lighting: item records (efficacy, W, coverage, lifetime, supplemental vs sole-source)

### Takeaway
DLC Horticultural V3.0 (effective 31 March 2023) requires PPE ≥2.30 µmol/J, Q90 ≥36,000 h, driver life ≥50,000 h and a 5-year luminaire warranty. A peer-reviewed review (Kusuma, Pattison and Bugbee, 2020) places typical fixtures at 2-3 µmol/J, with physical limits of about 3.4 µmol/J (white + red) and 4.1 µmol/J (blue + red). For NL greenhouses, WUR found that LED-for-SON-T swaps save 10-25% of total energy in lit tomato, not the 40% often claimed, because the lost lamp heat must be replaced. The Gavita CT1930e spec sheet gives 780 W and a 5-year warranty, but no PPF or µmol/J. Signify datasheets and all NL/India fixture prices could not be read.

### Cited Findings

#### 2a. Efficacy and lifetime benchmarks (fixture-independent)
| Value | Source | Tier | Confidence (reason) | Corroboration |
|---|---|---|---|---|
| DLC Hort V3.0 PPE threshold "≥2.30 µmol × J-1", with -5% tolerance (results ≥2.19 accepted) | [DLC Hort Technical Requirements V3.0 (final, May 2024 PDF)](https://designlights.org/wp-content/uploads/2024/05/DLC_HORT-Technical-Requirements-V3-0_FINAL_05132024.pdf) | tier_2 (industry standard body) | high (primary document) | single_source |
| V3.0 effective 31 March 2023, released 30 November 2022 | same | tier_2 | high | single_source |
| V3.0 threshold is "a 21% increase over the Hort V2.1 PPE threshold" | same | tier_2 | high | corroborated with the next row (2.30/1.21 is about 1.9) |
| Earlier DLC minimum "1.9 µmol J−1" | [Kusuma, Pattison & Bugbee 2020, Hortic Res 7:56](https://www.nature.com/articles/s41438-020-0283-7) | tier_1 | high (peer-reviewed) | corroborated (consistent with DLC's 21% statement) |
| Photon flux maintenance "Q90 ≥ 36,000 hours" (400-700 nm) | DLC V3.0 PDF | tier_2 | high | single_source |
| Driver lifetime ≥50,000 h; fan lifetime ≥50,000 h | DLC V3.0 PDF | tier_2 | high | single_source |
| Warranty ≥5 years luminaires, ≥3 years replacement lamps | DLC V3.0 PDF | tier_2 | high | single_source |
| Dimming required for AC luminaires with PPF ≥350 µmol/s; PF ≥0.90; THDi ≤20% | DLC V3.0 PDF | tier_2 | high | single_source |
| Best LED fixtures in 2014: 1.7 µmol/J | Kusuma et al. 2020 | tier_1 | high | single_source |
| Recent fixtures: 2.5-2.8 µmol/J (white + red), 3 µmol/J (blue + red); typical 2-3 µmol/J | Kusuma et al. 2020 | tier_1 | high (peer-reviewed; values are 2020 state of the art and may be outdated by 2026) | single_source |
| Efficacy limits 3.4 µmol/J (white + red), 4.1 µmol/J (blue + red); ~4.6 µmol/J theoretical for colour-mixed white with direct green | Kusuma et al. 2020 | tier_1 | high | single_source |
| "A typical L70 for LED fixtures is 50,000 h"; a 60,000 h depreciation claim needs 10,000 h of testing | Kusuma et al. 2020 | tier_1 | medium (general statement, not fixture-specific) | single_source |
| HPS fixtures (1 kW) "$200 to $350 USD per kW (5–9 µmol s−1 per $)" (US, 2020) | Kusuma et al. 2020 | tier_1 | medium (2020 US prices, global reference only) | single_source |
| HPS (SON-T) efficacy in µmol/J | not found in pages read | - | - | not found |
| Older Purdue threshold: "the photon efficiency of the fixture should be above 1 µmol/J" | [Purdue CEA, supplemental lighting for hydroponic lettuce](https://www.purdue.edu/hla/sites/cea/article/how-do-i-know-if-supplemental-lighting-is-economical-for-hydroponic-lettuce-in-winter/) | tier_2 | low (undated page, threshold far below current DLC floor) | conflicting with the DLC 2.30 floor; context: older and lower bar |

#### 2b. Supplemental greenhouse toplighting (HPS vs LED), Netherlands context
- Rabobank (17 February 2022): when growers replace part of their HPS lamps with LED, the light level often rises, "Bijvoorbeeld van 200 µmol/m2/s naar meer dan 300 µmol/m2/s"; the EG subsidy (Energie-efficiëntie Glastuinbouw) had closed and did not apply to growers who significantly raised light levels. No investment cost, saving percentage or µmol/J figure on the page — [Rabobank](https://www.rabobank.nl/kennis/d011237581-energiemarkt-in-tuinbouw-kan-led-belichting-helpen). Tier_2 (bank industry note); confidence medium (example figure, not a survey); single_source.
- WUR (David Katzin, Business Unit Greenhouse Horticulture and Flower Bulbs, 14 June 2022), on lit tomato greenhouses, GreenLight model: the common claim is that "LED lamps use 40% less energy than SON-T lamps", but the realistic total energy saving WUR found is "10 to 25%, depending on climate settings" and lamp type, because growers must add heating in winter to replace the heat SON-T lamps supply. The added heating is not quantified, and no µmol/J values are given — [WUR, "Are LED lamps indeed more economical than SON-T?"](https://www.wur.nl/en/show/are-led-lamps-indeed-more-economical-than-son-t.htm). Tier_2 (research institute note backed by a model study); confidence medium (tomato crop context, not leafy greens or basil; model-based); corroboration: conflicting between the "40%" claim (lamp electricity) and "10-25%" (whole-greenhouse energy). These are different system boundaries, so they form a context split and both values are kept.
- KWIN Glastuinbouw 2026 (WUR) is the 28th edition, sold as a paid PDF through the WUR webshop; its public page gives no lighting cost data and no price — [WUR KWIN Glastuinbouw 2026](https://www.wur.nl/nl/onderzoek/producten-diensten/kwin-glastuinbouw-2026). Tier_2; high for the publication facts; lighting cost values not found.

#### 2c. Fixture-level records
- **Item: Gavita CT 1930e LED (120-277 V version; a retailer title calls it "The first true 1:1 replacement for HPS")** — the spec sheet states "INPUT WATTS: 780 W"; "WEIGHT: 33.07 lb / 15 kg"; "DIM: 29 in x 11.8 in x 3.9 in"; "WARRANTY: 5 Year"; "MOUNTING: Hangers and Unistrut Bracket"; certifications "UL 1598, ANSI/CAN/UL 8800, and CSA C22.2 No. 250.0" — [Gavita CT1930e spec sheet V6 (2021)](https://cdn.shopify.com/s/files/1/0856/1428/files/1000600889_V6_906740_Gavita_1930eLED_120-277V_Spec_Sheet_210909as.pdf). Tier_2 (manufacturer datasheet); high; the 780 W figure is corroborated by retailer titles ([Hydrobuilder](https://hydrobuilder.com/products/gavita-ct-1930e-780-watt-led-grow-light-120-277-volt), tier_3). PPF, µmol/J, L90 hours, recommended coverage, mounting height and DLC listing are not on the spec sheet (not found). This is the North American voltage version; an EU-voltage datasheet and an EU price were not found. Duty hours per day: not stated (depends on the lighting strategy; not found).
- Philips GreenPower LED toplighting force (greenhouse toplighting): datasheets found but not readable — [Signify product sheet 2023](https://www.assets.signify.com/is/content/Signify/Assets/philips-lighting/global/20230706-toplighting-force-d02-d-400v-06-2023.pdf). All fields not found.
- Fluence fixtures: not searched successfully; not found.
- Spider Farmer, Mars Hydro and other hobby bar or board lights (sole-source, tent scale): retailer pages found ([Galaxus CH, Spider Farmer SF1000](https://www.galaxus.ch/en/s4/product/spider-farmer-sf1000-led-plant-lamps-20925342)) but not readable; all fields not found.
- Indian LED grow light sellers found on IndiaMART but not readable: [LED Grow Light category](https://m.indiamart.com/impcat/led-grow-light.html), [GL Lightings hydroponic](https://m.indiamart.com/gllightings/hydroponic.html), [Eye-Que Lights and Technologies](https://m.indiamart.com/eye-que-lights-and-technologies), [Lumiserve](https://m.indiamart.com/lumiserve/), [Nexsel](https://m.indiamart.com/nexsel/). Prices, wattages and µmol/J: not found.
- T5 seedling fluorescents and "shop lights": not found.

### Inferences
- Supplemental vs sole-source (inference): greenhouse toplighting (Gavita CT1930e class, Signify toplighting force) is supplemental lighting for greenhouses and fits small commercial and commercial greenhouses with NFT, DWC or substrate gutters. Bar and board fixtures (Spider Farmer class) fit sole-source indoor tents and vertical racks at hobby to small commercial scale. The fixture records needed to confirm W, PPF and coverage were not read.
- The DLC 2.30 µmol/J floor is a usable screening rule for a component database: a fixture without a DLC listing or a third-party PPE test report should have its µmol/J stored as a manufacturer claim (tier_2 at best, tier_3 if from a retailer page).
- Lifetime basis: DLC specifies Q90 (photon flux maintenance) and driver hours; Kusuma et al. cite a typical L70. These are different metrics (Q90 vs L70) and should be stored as separate fields, not merged.

### Gaps
- µmol/J, W, PPF, coverage and L90 for Gavita, Fluence, Signify and hobby fixtures: not found (datasheets found, fetch budget exhausted).
- HPS (SON-T 1000 W) efficacy in µmol/J from a tier_1 or tier_2 source: not found in pages read.
- WUR and KWIN greenhouse lighting investment per m2 and installed W/m2: not found (KWIN is paid). WUR's LED vs SON-T energy result was found (2b), but it covers tomato, not leafy greens.
- DLC QPL statistics (count of listed products, median µmol/J by year): not found. The MSU "2024-01, Update on LED efficacy" PDF was blocked (bot protection) and later unreachable.
- LED prices in NL, EU and India: not found.

## 3. Propagation: item records (trays, plugs, cubes, domes, heat mats, chambers, seedling lights)

### Takeaway
University of Kentucky extension strongly recommends bonded 1-inch plugs (rockwool, coco or peat-based) for DWC and NFT lettuce, with germination in about 3 days at 20 °C and RH above 88%, dome removal about 2 days after seeding, and transplant at 14-21 days. Cornell gives the seedling light rule (≥50 µmol/m2/s in the first 24 h; 250 µmol/m2/s at 24 h or 375 µmol/m2/s at 16 h; DLI 22). One EU retail price was found for a Grodan 150-plug tray. Heat mats, domes, Jiffy, Oasis, germination chambers and T5 lights were not priced in this pass.

### Cited Findings
**Item: Grodan SBS propagation cubes 25/150 in plastic tray (stone wool)**
- dimensions: 150 plugs per tray; each plug 25 × 25 × 40 mm; tray 530 × 318 mm — [Growmart](https://growmart.eu/Grodan-SBS-Propagation-Cubes-25-150-plastic-tray). Tier_3; medium (retailer restating product specs); single_source.
- price: see Section 4.

**Item: Grodan Plantop plug (stone wool, NL datasheet)**
- specs: "Max bezinktijd < 25 seconden" (max settling time under 25 s); vertical fibre structure; 2 sowing-hole variants; several tray types; aimed at "opkweek van vruchtgroenten en snijbloemen" (fruiting vegetables and cut flowers), so not specifically leafy greens or basil; suited to manual or mechanical germinating, sorting and transplanting — [Grodan Plantop plug datasheet (NL)](https://www.grodan.com/siteassets/downloads/downloads-nl/product-data-sheets-nl/grodan202064-gew-hrdrk-pds-grodan-plantop-plug-a4---ned.pdf). Tier_2 (manufacturer datasheet); high; single_source. Plug dimensions, plugs per tray, water holding and soaking pH/EC: not on this datasheet (not found).

**Plug/cube material choice and propagation schedule (extension rule)**
- Bonded plugs of rockwool, coco coir or peat are options; bonded 1-inch plugs are "strongly recommended" for DWC and NFT; loose substrates can be filled into high-density trays, e.g. a 128-cell tray. Oasis is not mentioned — [UKy CCD-CP-63](https://ccd.uky.edu/sites/default/files/2026-02/ccd-cp-63_hydrolettuce-updated_accessible.pdf). Tier_2; high; single_source.
- Germination about 3 days at "68 °F (20 °C)" with relative humidity over 88%; dome removal about two days after seeding; seedling growth about 10 days; transplant at 3-4 true leaves with visible roots, usually 14-21 days after seeding — same source. Tier_2; high; single_source.
- Germination light "around 50 µmol/m2/s", rising to 200-300 µmol/m2/s as seedlings develop — same source. Tier_2; high; corroborated by Cornell (next row) for the 50 µmol/m2/s germination floor.
- Cornell (Mattson, GPN October 2016): germination "a minimum instantaneous light intensity no less than 50 µmol·m-2·s-1" in the first 24 hours; seedling lighting "to 250 µmol·m-2·s-1 with a 24-hour photoperiod or 375 µmol·m-2·s-1 for a 16-hour photoperiod"; seedling DLI 22 mol·m-2·d-1 from sunlight plus supplemental light — [Cornell CEA, GPN Oct 2016](https://bpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/8/8824/files/2019/06/GPNOctober2016_LeafyGreens.pdf). Tier_2 (extension specialist in a trade magazine); high; 50 µmol/m2/s corroborated with UKy; the seedling 250/375 PPFD values are single_source and differ from UKy's 200-300 µmol/m2/s (different photoperiod contexts; both kept).

**Basil seedlings (experimental, not a recommendation)**
- MSU (Walters and Lopez, *Produce Grower*, June 2019): basil seedlings grown at 100, 200, 400 and 600 µmol/m2/s for 16 h, giving DLIs of 6, 12, 23 and 35 mol/m2/d, then 14 mol/m2/d in the greenhouse for three weeks. The authors note results "may be species dependent" and that 400-600 µmol/m2/s exceeds what most indoor facilities provide — [MSU Floriculture lighting PDF](https://www.canr.msu.edu/floriculture/resources/lighting.pdf). Tier_2; medium (these are treatment levels, not a target); single_source.

### Inferences
- Fit (inference): stone wool, coco and peat plugs suit all grow methods that take a plug transplant (DWC rafts, NFT, towers, Dutch bucket start, ebb and flow). Media-bed aquaponics can also direct-seed or take plugs. Stone wool is not biodegradable; the disposal trade-off is an inference and was not sourced.
- Scale (inference): 150-plug trays and domes suit hobby to small commercial; mechanised plug lines (Grodan's datasheet mentions mechanical sorting and transplanting) suit commercial operations.
- The germination conditions (20 °C, RH >88%, ≥50 µmol/m2/s) are the sizing rules that a heat mat, a humidity dome and a seedling light exist to meet. No source in this pass sized a heat mat (W per tray) or a seedling light (W per tray).

### Gaps
- Prices and specs for Jiffy/peat pellets, coco plugs, Oasis/Rootcubes, humidity domes, heat mats (W, °C rise), germination chambers and T5 seedling fixtures in NL and India: not found.
- Indian seedling-tray prices: sellers found but not read ([IndiaMART seedling trays category](https://m.indiamart.com/impcat/seedling-trays.html), [Kanera Sales 102-cavity](https://m.indiamart.com/kanerasales), [SSK Agro 42-cavity](https://m.indiamart.com/sskagroindustries), [Formatech 104-cavity](https://m.indiamart.com/formatechindustries/), [Flipkart 98-cavity 10-pack](https://www.flipkart.com/moglecart-seedling-tray-98-cavities-pack-10-plant-container-set/p/itmb71bb75e43951)).
- Basil-specific propagation light targets from an extension source: not found.

## 4. Price ranges per market (NL/EU first, then India, then global)

### Takeaway
NL/EU prices were found for Bluelab (EU official store, incl VAT; pH Pen €86.40 up to IntelliDose kit €1,574.40), Hanna pocket testers (€62.85-€76.05 at RS NL; €73.00 excl VAT from a Slovenian Hanna distributor) and a Grodan 150-plug tray (€14.90 incl 19% DE VAT). India prices were found only for Bengaluru IndiaMART pH meters (₹1,000 to ₹29,990 per piece, GST status not stated) and one Bengaluru controller (₹1,75,000). No LED fixture, DO meter, test-kit, heat-mat or dome price could be read for either market.

### Cited Findings

#### 4a. Netherlands / EU (read 2026-11-25)
| Item | Price | Currency | Unit | VAT | Seller (country) | URL | Tier / confidence / corroboration |
|---|---|---|---|---|---|---|---|
| Bluelab pH Pen | 86.40 | EUR | each | incl VAT | Bluelab EU official store | [eu.bluelab.com/collections/ph](https://eu.bluelab.com/collections/ph) | tier_3 / high (seller's own listing) / single_source |
| Bluelab pH PenPlus | 110.40 (struck-through 138.00, "On Sale") | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab OnePen (pH, EC, temp) | 191.04 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab Combo Meter | 297.60 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab pH and Conductivity Starter Pack | 201.60 | EUR | pack | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab pH Probe (replacement) | 81.60 (shown "Sold Out") | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab pH Probe 5M | 86.40 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab pH Probe Inline | 182.40 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab OnePen Replacement Probe | 85.44 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab Guardian Monitor Wi-Fi | 373.44 (struck-through 466.80; "Sold Out") | EUR | each | incl VAT | Bluelab EU | [eu.bluelab.com/bluelab-guardian-monitor-wi-fi](https://eu.bluelab.com/bluelab-guardian-monitor-wi-fi) | tier_3 / high / corroborated across the collection page and the product page |
| Bluelab Guardian Monitor Inline Wi-Fi | 556.80 | EUR | each | incl VAT | Bluelab EU | [eu.bluelab.com/collections/ph](https://eu.bluelab.com/collections/ph) | tier_3 / high / single_source |
| Bluelab pH Controller Wi-Fi | 504.00 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab Pro Controller Wi-Fi | 1,248.00 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab IntelliDose Controller Kit | 1,574.40 | EUR | kit | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab PeriPod M3 / M4 / L3 (peristaltic dosing) | 1,075.20 / 1,454.40 / 2,625.60 | EUR | each | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab Probe Care Kit pH / pH+Conductivity | 22.08 / 28.80 | EUR | kit | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab calibration and storage sachets, 30 box | 43.20 | EUR | box of 30 | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Bluelab pH Probe KCl Storage Solution 100 ml | 13.44 | EUR | 100 ml | incl VAT | Bluelab EU | same | tier_3 / high / single_source |
| Hanna HI98107 pHep | 62.85 excl / 76.05 incl | EUR | each | both shown | RS Components NL | [nl.rs-online.com](https://nl.rs-online.com/web/p/ph-meters/0218970) | tier_3 / high (NL B2B distributor) / single_source |
| Hanna HI98115 Groline pH tester | 73.00 ("Out of stock") | EUR | each | excl VAT, excl shipping | Hanna Service d.o.o., Koper, Slovenia | [hannaservice.eu](https://hannaservice.eu/ph-tester-groline-hi98115-product) | tier_3 / medium (shipping to NL not stated) / single_source |
| Grodan SBS propagation cubes 25/150, plastic tray | 14.90 | EUR | tray of 150 plugs | incl 19% VAT, plus shipping | Growmart (CRP Import-Export GmbH; Germany inferred from "GmbH" and a "DE" delivery note) | [growmart.eu](https://growmart.eu/Grodan-SBS-Propagation-Cubes-25-150-plastic-tray) | tier_3 / medium (German VAT rate, not Dutch 21%; NL shipping cost not stated) / single_source |

Shipping note: a Bluelab EU page title reads "Free shipping to European Union countries on orders over €250" ([eu.bluelab.com/pages/reviews](https://eu.bluelab.com/pages/reviews)). This is from a search-result title only, so confidence is low.

Not found for NL/EU: bol.com, toppy.nl and Kweekshop listings (none readable); API, Tetra, JBL and Hach test kits; DO meters; LED fixtures; heat mats; domes; Jiffy; T5; alarms; Priva or Hoogendoorn systems.

#### 4b. India (read 2026-11-25)
Karnataka (Bengaluru), IndiaMART "Digital pH Meter" city listing — [IndiaMART Bengaluru digital pH meter](https://m.indiamart.com/city/bengaluru/digital-ph-meter.html?biz=10). Tier_3; confidence low to medium (B2B list prices, GST status not stated on any listing, many lab or industrial meters rather than hydroponic pens); single_source per listing.

| Listing title (quoted) | Price (INR) | Unit | Seller | Locality |
|---|---|---|---|---|
| "Handheld Digital PH Meter with LCD Display (0-14 pH...)" | 1,000 | Piece | Culture Instruments India LLP | Nelamangala |
| "Pocket pH Meter" | 2,500 | Number | Biobee Tech | Bengaluru |
| "RENOWN SYSTEMS DIGITAL PH METER, For Laboratory, Light Weight" | 4,600 | Piece | Teklab India Solutions | Bengaluru |
| "PH Meter" | 6,400 | Piece | Micro Agri Solutions | Bengaluru |
| "0.5% +- 1 Digit pH Controller 112 pH, For Industrial" | 6,660 | Piece | Countronics | Bengaluru |
| "Portable Digital Ph Meter - Alpha 01" | 7,125 | Piece | Labmatrix Manufacturing LLP | Bengaluru |
| "Biovision Services 3 Point Ph Meter, 1.4 Kg" | 7,200 | Piece | Biovision Services | Bengaluru |
| "Ph Meter Digital" (online/inline type) | 8,999 | Piece | Utkarsh Scientific Instruments Suppliers | Bengaluru |
| "Portable Digital P.h Meter" | 10,000 | Piece | Spectraa Lab Solutions | Bengaluru |
| "Anamatrix PH Meter Digital Table Top 101, For Laboratory" | 11,600 | Piece | Anamatrix Instrument Technologies Pvt Ltd | Bengaluru |
| "PH Meter" | 29,990 | Piece | S. L. V. Scientific Instruments | Bengaluru |
| "Digital PH Meter" | not stated | - | Engineering & Engineers Instruments | Bengaluru |

Hydroponic controller (Karnataka): Hyperfarms Private Limited, Bengaluru, "Hydroponics Nutrient Controller", ₹ 1,75,000 per piece, GST status not stated — [IndiaMART Hyperfarms](https://m.indiamart.com/hyperfarms-bengaluru/hydroponics-nutrient-controller.html). Tier_3; low; single_source.

Tamil Nadu, Andhra Pradesh, Telangana: no listing read (not found). Amazon.in, Hydroponics India, Brown Living and Ugaoo: no listing read (not found). API Freshwater Master Test Kit listings exist on Flipkart and IndiaMART ([Flipkart](https://www.flipkart.com/api-liquid-aquarium-water-test-kit/p/itmey6f52ju4xn4j), [IndiaMART](https://m.indiamart.com/proddetail/api-master-test-kit-21782016333.html)), but their prices were not read.

#### 4c. Global reference
- US HPS fixtures (1 kW) "$200 to $350 USD per kW" in 2020 — [Kusuma et al. 2020](https://www.nature.com/articles/s41438-020-0283-7). Tier_1; medium (dated and US, reference only); single_source.
- Purdue's older lettuce lighting economics assumed "the cost of electricity at 10 cents per unit" (US) — [Purdue CEA](https://www.purdue.edu/hla/sites/cea/article/how-do-i-know-if-supplemental-lighting-is-economical-for-hydroponic-lettuce-in-winter/). Tier_2; low (undated, US); this is the article's own assumption and must not be reused as an input.

### Inferences
- The Bengaluru pH-meter range (₹1,000 to ₹29,990) mixes pocket pens, lab benchtop and industrial controller listings. It should be stored per listing with a product-class tag, not as one range.
- The Bluelab EU store gives a consistent single-seller price ladder from a spot pen (€86.40) to continuous monitor (€373.44-€556.80) to dosing controller (€1,248.00-€2,625.60), all incl VAT. A replacement pH probe (€81.60) costs about the same as a new pH Pen (€86.40), which suggests users may replace the whole pen rather than the probe (inference).
- No price in these notes supports a total-cost, revenue or viability statement. Under AGENTS.md 1C, they are candidate manual inputs that need user review before any scenario-estimate use.

### Gaps
- All LED fixture prices (NL and India), DO meter prices, test-kit prices (API, Tetra, JBL, Hach), propagation sundries (heat mats, domes, Jiffy, coco plugs, Oasis, T5), alarm prices: not found.
- India state differences (TN, AP, TS) and GST treatment: not found.
- No exchange rate was used, and no cross-market comparison was made.

## 5. Efficacy and lifetime claims (DLC, µmol/J, L90/Q90, probe and sensor lifetimes)

### Takeaway
Lifetime claims in this pass are all manufacturer or standard-body figures, each with a different basis: DLC Q90 ≥36,000 h and driver ≥50,000 h (standard); "typical L70 50,000 h" (peer-reviewed review); Atlas lab-grade pH probe "~2.5 years+" (manufacturer claim); galvanic DO tip about 6 months and optical DO cap about 12 months (manufacturer note); Bluelab pH probe warranty of 6 months versus a 2-year device warranty. No depreciation study or independent field-life survey was found.

### Cited Findings
| Item | Lifetime / interval value | Basis | Source | Tier | Confidence | Corroboration |
|---|---|---|---|---|---|---|
| DLC-listed LED luminaire | Q90 ≥36,000 h; driver ≥50,000 h; fan ≥50,000 h; warranty ≥5 y | standard requirement (minimum, not measured life) | [DLC V3.0](https://designlights.org/wp-content/uploads/2024/05/DLC_HORT-Technical-Requirements-V3-0_FINAL_05132024.pdf) | tier_2 | high | single_source |
| LED fixtures (general) | "typical L70 ... 50,000 h" | review statement | [Kusuma et al. 2020](https://www.nature.com/articles/s41438-020-0283-7) | tier_1 | medium | single_source |
| LED efficacy | DLC floor ≥2.30 µmol/J (V3.0), previously 1.9 (V2.x); typical 2-3 µmol/J in 2020; limits 3.4 / 4.1 µmol/J | standard plus review | DLC V3.0; Kusuma et al. 2020 | tier_2 / tier_1 | high | corroborated for the 1.9 V2.x floor |
| Atlas Scientific ENV-40-pH probe | "Life expectancy ~2.5 Years +"; storage life ~5 years | manufacturer claim | [Atlas datasheet](https://cdn.robotshop.com/media/A/Atl/RB-Atl-39/pdf/atlas-scientific-ph-probe-v48-datasheet.pdf) | tier_2 | medium | single_source |
| Bluelab pH probe | warranty 6 months (device 2 years) | warranty term, not life | [Bluelab Guardian Wi-Fi](https://eu.bluelab.com/bluelab-guardian-monitor-wi-fi) | tier_2 | high | single_source |
| Galvanic DO sensor | tip replacement "every after 6 months depending on the application and handling" | manufacturer guidance | [Horiba](https://www.horiba.com/int/water-quality/support/technical-tips/electrodes/galvanic-vs-optical-dissolved-oxygen-sensors/) | tier_2 | medium | single_source |
| Optical DO sensor | cap replacement "every after 12 months depending on the application and handling" | manufacturer guidance | same | tier_2 | medium | single_source |
| Hanna HI98107 battery | 1000 h vs 700 h on the same page | retailer listing | [RS NL](https://nl.rs-online.com/web/p/ph-meters/0218970) | tier_3 | low | conflicting |
| Hanna HI98115 battery | about 1000 h continuous | retailer listing | [Hanna Service EU](https://hannaservice.eu/ph-tester-groline-hi98115-product) | tier_3 | medium | single_source |

Calibration intervals (kept separate, not averaged):
- Bluelab pH and EC: once a month, or more often under heavy use — [Bluelab](https://eu.bluelab.com/pages/care-calibration-maintenance). Tier_2; high.
- Atlas Scientific lab-grade pH in fish tank or hydroponic water: once per year for the first two years, then about every six months — [Atlas datasheet](https://cdn.robotshop.com/media/A/Atl/RB-Atl-39/pdf/atlas-scientific-ph-probe-v48-datasheet.pdf). Tier_2; medium.
- Corroboration: conflicting (a 12x difference in the first-year interval). Context split: Bluelab gives a general rule for handheld pens and monitors; Atlas is product-specific for a lab-grade, continuously immersed probe.

### Inferences
- For the component database, store `lifetime_value`, `lifetime_unit` and `lifetime_basis` (one of standard_minimum, manufacturer_claim, warranty_term, review_statement) as separate fields, because the values above are not comparable across bases.
- A warranty term (Bluelab pH probe, 6 months) is not a service life, and it should not be used as a replacement interval without a separate source.

### Gaps
- Fixture-specific L90/LM-80/TM-21 hours for Gavita, Fluence and Signify: not found (datasheets unread).
- Independent field-life data for pH probes in aquaponic water (biofilm, fish-waste fouling): not found.
- HPS lamp replacement interval (hours) from a tier_1 or tier_2 source: not found.
- EC probe lifetime: not found.

## 6. Sizing rules from extension sources (DLI, PPFD, test frequency)

### Takeaway
Cited lettuce DLI targets differ by source and context: Cornell 17 mol/m2/d (13-14 without vertical airflow), Kentucky 12-17 optimal (minimum about 6.5-9.7), Purdue 15-20. These are kept as a context split, not averaged. No extension-sourced basil production DLI target was found; the only basil figures are MSU experimental seedling treatments. Test-frequency rules: FAO weekly manual tests for aquaponics; Kentucky continuous pH/EC monitoring for DWC/NFT hydroponics.

### Cited Findings
| Rule | Value | Context | Source | Tier | Confidence | Corroboration |
|---|---|---|---|---|---|---|
| Head lettuce DLI | 17 mol·m-2·d-1, giving "5- to 6-ounce heads ... 24 days after transplanting" | Cornell greenhouse hydroponic leafy greens | [Mattson, GPN Oct 2016 (Cornell CEA)](https://bpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/8/8824/files/2019/06/GPNOctober2016_LeafyGreens.pdf) | tier_2 | high | context_split with UKy and Purdue |
| Lettuce DLI without proper airflow | "a lower DLI target such as 13 to 14 mol·m-2·d-1" (tipburn context) | Cornell | same | tier_2 | high | single_source |
| Baby-leaf greens DLI | 17 mol·m-2·d-1 at 75/66 °F day/night | Cornell | same | tier_2 | high | single_source |
| Lettuce seedling DLI and PPFD | DLI 22; 250 µmol·m-2·s-1 at 24 h or 375 at 16 h; ≥50 µmol·m-2·s-1 in the first 24 h | Cornell propagation | same | tier_2 | high | 50 floor corroborated by UKy |
| Lettuce optimal DLI | "12-17 mol/m2/day"; minimum about 6.5-9.7 (slower growth) | Kentucky CEA hydroponic lettuce | [UKy CCD-CP-63 (2025)](https://ccd.uky.edu/sites/default/files/2026-02/ccd-cp-63_hydrolettuce-updated_accessible.pdf) | tier_2 | high | context_split |
| Lettuce DLI | "can vary from 15-20 mol/m2/day"; winter greenhouse sun DLI "approx. 5 mol/m2/day in these regions" (US Midwest context); yield "approx. 0.0151 lb (or 6.8 g) for every mole of light incident" | Purdue greenhouse winter | [Purdue CEA](https://www.purdue.edu/hla/sites/cea/article/how-do-i-know-if-supplemental-lighting-is-economical-for-hydroponic-lettuce-in-winter/) | tier_2 | medium (undated page) | context_split |
| Basil DLI | experimental seedling treatments 6, 12, 23, 35 mol/m2/d (100-600 µmol/m2/s × 16 h); post-transplant 14 mol/m2/d; authors say results "may be species dependent" | MSU research summary, not a target | [Walters & Lopez, Produce Grower June 2019 (MSU)](https://www.canr.msu.edu/floriculture/resources/lighting.pdf) | tier_2 | medium | single_source |
| Aquaponics water-test frequency | weekly; less in mature units; ammonia and nitrite for new units | FAO small-scale aquaponics | [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/3-water-quality-in-aquaponics/water-testing/) | tier_1 | medium | single_source |
| Hydroponic pH/EC monitoring | continuous in DWC/NFT; top-up every few days; replace solution every 3-4 weeks | Kentucky hydroponic lettuce | [UKy CCD-CP-63](https://ccd.uky.edu/sites/default/files/2026-02/ccd-cp-63_hydrolettuce-updated_accessible.pdf) | tier_2 | high | single_source |
| Meter calibration | monthly (Bluelab) vs yearly then 6-monthly (Atlas) | manufacturer | see Section 5 | tier_2 | high / medium | conflicting (context split) |
| Greenhouse light level with LED retrofit | 200 µmol/m2/s rising to >300 µmol/m2/s (example) | NL greenhouses, 2022 | [Rabobank](https://www.rabobank.nl/kennis/d011237581-energiemarkt-in-tuinbouw-kan-led-belichting-helpen) | tier_2 | medium | single_source |

### Inferences
- Converting a DLI target into a fixture count needs PPFD = DLI × 10^6 / (photoperiod_h × 3600). This is a unit identity, not a sourced sizing rule, and no farm is sized here. Cornell's own seedling pairs (250 µmol/m2/s × 24 h, 375 × 16 h) both work out to about 21.6 mol/m2/d, consistent with its stated seedling DLI of 22.
- The 17 mol/m2/d Cornell figure belongs to a greenhouse with CO2 and airflow management (the article ties lower targets to missing airflow and says CO2 can achieve similar growth at lower DLI). It should be stored with those context tags and not as a universal lettuce number.

### Gaps
- Basil production DLI target from an extension source: not found in this pass. The repo's `Basil_Corroboration report ... .pdf` may hold one, but it was not read here.
- Sole-source (indoor, vertical) lettuce PPFD and photoperiod recommendations from an extension source: only the UKy germination and seedling values were found.
- FAO 589's DO-testing guidance and its own meter calibration advice: not on the page read.
- Monitoring frequency for DO in coupled aquaponics from a tier_1 or tier_2 source: not found.

## 7. What growers use instead, and what fails

### Takeaway
Sourced alternatives found: colorimetric aquarium kits and strips instead of meters (FAO calls strips "cheapest and moderately accurate" and meters "relatively expensive and very accurate"), cheap pocket pH testers (Hanna HI98107 at ±0.1 pH; IndiaMART pocket meters from ₹1,000), and DIY Atlas-Scientific-based probes for ESP32/Arduino builds. Failure evidence is limited to manufacturer guidance on drying, drift and flow dependence. No forum anecdote or independent test of cheap pens or ESP32 builds was read, so these remain gaps.

### Cited Findings
- Kits vs strips vs meters: kits "readily available and easy to use"; meters "relatively expensive and very accurate"; strips "cheapest and moderately accurate" — [FAO 589 via FarmHub](https://learn.farmhub.ag/resources/small-scale-aquaponic-food-production/3-water-quality-in-aquaponics/water-testing/). Tier_1; medium; single_source.
- Pocket tester accuracy classes: Hanna HI98107 ±0.1 pH / 0.1 resolution ([RS NL](https://nl.rs-online.com/web/p/ph-meters/0218970)); Hanna HI98115 ±0.2 pH / 0.01 resolution ([Hanna Service EU](https://hannaservice.eu/ph-tester-groline-hi98115-product)); Atlas lab-grade probe ±0.002 (manufacturer claim) ([Atlas datasheet](https://cdn.robotshop.com/media/A/Atl/RB-Atl-39/pdf/atlas-scientific-ph-probe-v48-datasheet.pdf)). Tier_3 / tier_3 / tier_2; medium; single_source each.
- Failure mode, pH probe drying out: a dried tip must be rehydrated in KCl for 24 h and recalibrated at two points — [Bluelab](https://eu.bluelab.com/pages/care-calibration-maintenance). Tier_2; high.
- Failure mode, calibration drift: Bluelab requires recalibration after 30 days (check-mark expiry) — [Bluelab](https://eu.bluelab.com/pages/care-calibration-maintenance); galvanic DO sensors drift and need "frequent calibration" — [Horiba](https://www.horiba.com/int/water-quality/support/technical-tips/electrodes/galvanic-vs-optical-dissolved-oxygen-sensors/). Tier_2; high / medium.
- Failure mode, flow dependence: galvanic DO needs stirring or flow and consumes oxygen at the cathode — [Horiba](https://www.horiba.com/int/water-quality/support/technical-tips/electrodes/galvanic-vs-optical-dissolved-oxygen-sensors/). Tier_2; medium.
- Probe warranty much shorter than device warranty (6 months vs 2 years) — [Bluelab Guardian Wi-Fi](https://eu.bluelab.com/bluelab-guardian-monitor-wi-fi). Tier_2; high.
- Lighting alternative, older threshold: Purdue's ">1 µmol/J" fixture guidance is far below DLC V3.0's 2.30 floor, so cheaper non-listed fixtures may sit anywhere in between — [Purdue](https://www.purdue.edu/hla/sites/cea/article/how-do-i-know-if-supplemental-lighting-is-economical-for-hydroponic-lettuce-in-winter/); [DLC V3.0](https://designlights.org/wp-content/uploads/2024/05/DLC_HORT-Technical-Requirements-V3-0_FINAL_05132024.pdf). Tier_2; medium.

### Inferences
- Effects on fish and plants (inference, not quantified, not a safety claim): an unnoticed pH drift in a dosing loop moves the tank and root-zone pH away from target; a galvanic DO probe in still water may under-read and trigger false low-DO alarms, or, after drift, hide a real drop; a dried pH probe gives sluggish or offset readings until rehydrated. Severity depends on the size and duration of the error, which no source here quantified.
- The per-test labour of colorimetric kits (≤5 minutes per test, FAO) times the number of parameters (pH, NH3/NH4, NO2, NO3, KH) suggests a weekly manual test round of several tests. The total minutes are left uncomputed because FAO gives only a per-test maximum.
- Cheap Chinese pH pens, shop lights and DIY ESP32 monitors are common alternatives, but no source was read for this pass. Any claim about how they fail would be anecdote and is not recorded.

### Gaps
- Forum or user reports (anecdote) on cheap pH pen drift, ESP32 sensor isolation and ground-loop problems, EC probe interference, and shop-light (non-horticultural LED) performance: not read.
- Peer-reviewed comparisons of low-cost IoT sensors against reference meters in aquaponics: found but unread ([PMC7662340](https://pmc.ncbi.nlm.nih.gov/articles/PMC7662340), [UBC ELEC 491 report](https://sustain.ubc.ca/sites/default/files/seedslibrary/ELEC_491_Aquaponics%20Monitoring%20and%20Control%20System_FinalReport.pdf), [EPJ Conf 2026](https://www.epj-conferences.org/articles/epjconf/pdf/2026/33/epjconf_ips2026_02004.pdf)).
- Accuracy of API, Tetra and JBL aquarium kits against lab methods (Hach): not found.
- Power-failure and pump-stop failure modes and alarm products: not found.
