# Tank Volume, Exchange and TAN-to-NH3 Risk Research Pack

## Executive summary

For the next MVP layer, the strongest research-supported move is to keep **load**, **concentration**, and **NH3 risk** as separate stages rather than collapsing them into one value. The feed-based load equation used in RAS design literature produces **total ammonia nitrogen load** first; concentration only becomes meaningful once a **control volume** and **time basis** are added; and **unionized NH3 risk** still cannot be estimated until **pH** and **water temperature** are known. Texas A&M’s aquaponics guidance is explicit that TAN on its own “reveals nothing about toxicity”, while Florida DEP and EPA chemistry guidance show that speciation depends on pH and temperature. citeturn26view0turn3view4turn13view0turn27view0

For a **tilapia + basil DWC/raft demo**, the strongest non-canonical benchmark is still the UVI commercial raft system. It gives a coherent, high-trust set of coupled-system anchors: **7,800 L per fish tank**, **~111,000 L total system volume**, **378 L/min recirculation**, **~1.37 h rearing-tank retention**, **~19–20 min clarifier retention**, and **~3 h hydroponic trough retention**. Those anchors are unusually valuable because they show the system is **not one instantaneously mixed volume**; fish-tank risk and whole-system average concentration are not the same thing. That conclusion is an engineering inference from the residence-time split reported by UVI, not a direct quote. citeturn25view0turn23view0turn3view0

The safest first-pass concentration basis is **TAN-N mg/L**. That matches the feed-derived ammonia-load equation, matches how total ammonia is commonly measured analytically, and matches the freshwater speciation method in official chemistry guidance. Only after the NH3 fraction is calculated should the model optionally convert **NH3-N** to **NH3** using the **17/14** factor if a downstream threshold source is stated in NH3 rather than NH3-N. citeturn26view0turn13view0turn27view0

No universal tank-volume default, no universal retention default, and no universal stocking-density default are defensible from Tier 1 sources. SRAC tank-culture guidance shows that carrying capacity changes materially with aeration, oxygen supplementation, solids control, and system design, while UVI changed stocking rates between CA1 and CA2 to improve growth and feed conversion. These should remain **scenario inputs or demo assumptions**, not canon. citeturn11view2turn11view4turn25view0

Biofilter conversion should also remain conditional. SRAC and UF/IFAS sources make clear that nitrifiers need oxygen and alkalinity, and that new biofilters need time to mature. UVI shows that a well-aerated raft component can provide substantial nitrification capacity when the feeding-rate ratio and biofilm condition are right, but that does **not** justify assuming universal complete removal. citeturn8view0turn19view0turn14view0turn23view0turn7view0

## Evidence hierarchy

The source stack used here was prioritised as follows:

- **Tier 1 aquaponics operation anchors:** UVI commercial aquaponic system pages and the UVI “25 Years of Research” paper. These are the strongest sources for **real coupled DWC/raft component volumes, residence times, flow rates, and operating context**. citeturn3view0turn23view0turn25view0turn7view0
- **Tier 1 RAS and aquaculture management guidance:** SRAC 452, 453, 454, 5007, 282 and 283. These are the strongest sources for **tank exchange logic, warmwater DO expectations, clarifier retention, stocking-density context, pH/alkalinity/biofilter sensitivity, and tilapia-specific ammonia stress response**. citeturn8view0turn8view4turn24view0turn17view2turn19view0turn11view0turn11view2turn22view3
- **Tier 1 chemistry and post-measurement interpretation guidance:** Texas A&M aquaponics extension, UF/IFAS ammonia guidance, Florida DEP SOP, and EPA freshwater ammonia criteria. These are the strongest sources for **what TAN means analytically, what inputs are required for NH3 speciation, the Emerson freshwater equation, and unit-conversion cautions**. citeturn3view4turn14view0turn13view0turn27view0
- **Open-access peer-reviewed support for feed-to-TAN load formulation:** the Cornell-linked *Horticulturae* paper is used only to surface the explicit **PTAN = F × PC × 0.092 / t** formulation and its notation. It is helpful for implementation framing, but not used as the sole authority for system-operation anchors. citeturn26view0

## Context split notes

### Flow-through tanks

SRAC’s tilapia tank-culture guidance states that flow-through systems depend on water exchange to flush wastes and uses a rule of thumb of **replacing 100 percent of tank water every 90 to 120 minutes**. It also notes that such systems are often not suitable for commercial tilapia unless warm source water is available. In this context, **tank volume** is the primary concentration-control volume and **exchange rate** is the critical dilution variable. citeturn11view0turn11view1

### RAS

SRAC 452 treats recirculating systems as high-control environments where water quality must be managed for fish growth and biofilter function. It recommends **warmwater DO at or above 5 ppm**, **biofilter effluent above 2 ppm DO**, **pH 7.0–8.0**, **alkalinity 50–100 ppm or more as CaCO3**, and **un-ionized ammonia-N below 0.05 ppm**. In this context, concentration modelling requires **volume, recirculation, biofilter state, and gas-transfer assumptions**, not just feed load. citeturn8view0turn8view4turn8view5

### DWC and raft aquaponics

UVI’s aquaponics guidance states that in a **raft aquaponic system**, adequate biofiltration occurs in the hydroponic component and that, when the optimum feeding-rate ratio is maintained, there is **excess waste-treatment capacity**. The same UVI guidance also says that **deep-flow channels need no specific exchange target as long as they are aerated**, whereas **unaerated channels need faster exchange**. This is the strongest support for keeping DWC/raft as the best-supported biological baseline for a coupled tilapia+basil demo, while still treating actual removal capacity as conditional. citeturn23view0

### Small aquaponics

SRAC 5007 does **not** support a universal small-system tank-volume default. Instead, it gives **relative sizing and operational rules**: the biofilter tank should be **15–20 percent of fish-tank volume**, DWC float beds should usually be **10–12 inches deep**, and roots in float beds should be aerated at roughly **one air stone per 10 square feet**. For small systems, the defensible canon is therefore **relative sizing guidance**, not a hard-coded total volume. citeturn19view0

### Commercial aquaponics

The UVI commercial raft system is the strongest commercial anchor because it reports component volumes, recirculation, residence times, stocking densities, partial water dumping during cleaning, and actual water-quality outcomes in one coupled DWC/raft design. It is suitable as a **demo preset** but not as a universal design default. citeturn25view0turn7view0turn3view0

## Tank and system volume guidance table

| value or range | unit | system context | fish stage or biomass context | source | confidence | recommended use |
|---|---:|---|---|---|---|---|
| 7,800 per rearing tank | L | UVI CA2 commercial DWC/raft aquaponics | 24-week tilapia growout; Nile tilapia averaged 813.8 g in one CA2 evaluation | UVI 25-year paper and UVI CAS page citeturn25view0turn3view0 | high | strongest **demo fish-tank volume** anchor |
| 111,196 total system volume | L | UVI CA2 commercial DWC/raft aquaponics | same system as above | UVI 25-year paper citeturn25view0 | high | strongest **demo whole-system volume** anchor |
| 29,000 gallons | 110,000 L | UVI CAS page summary | same CA2/CAS class of system | UVI CAS page citeturn3view0 | high | corroborating total-volume anchor |
| 11,356 per hydroponic tank | L | UVI CA2 DWC/raft troughs | plant-side only | UVI 25-year paper and CAS page citeturn25view0turn3view0 | high | useful if modelling subsystem residence separately |
| 3,785 per clarifier | L | UVI CA2 clarifiers | solids-treatment subsystem | UVI 25-year paper and CAS page citeturn25view0turn3view0 | high | useful for clarifier retention calculations |
| 700 per filter tank and per degassing tank | L | UVI CA2 filter and degassing tanks | treatment subsystem | UVI 25-year paper and CAS page citeturn25view0turn3view0 | high | secondary subsystem anchors |
| 4,400 per rearing tank | L | UVI CA1 predecessor system | earlier commercial-scale iteration | UVI 25-year paper citeturn25view0 | medium | context split showing UVI itself changed tank scale |
| 15–20% of fish-tank volume | relative volume | SRAC 5007 small aquaponics biofilter sizing | small systems; architecture-neutral | SRAC 5007 citeturn19view0 | high | strong **relative small-system sizing** rule |
| Use smaller nursery volumes, then move fish to larger tanks as biomass grows | structural guidance | phased tank culture/RAS | fish biomass and daily feed increase over time | SRAC 282 citeturn11view4 | high | strong non-numeric guidance; no universal single tank size |

## Exchange, retention and flow guidance table

| value or range | unit | subsystem | source | confidence | recommended use |
|---|---:|---|---|---|---|
| 100% tank-water replacement every 90–120 minutes | turnover / residence time | flow-through tilapia tanks | SRAC 282 citeturn11view0turn11view1 | high | strongest **flow-through exchange** anchor |
| 378 | L/min | UVI CA2 total recirculation flow | UVI 25-year paper citeturn25view0 | high | strongest **demo recirculation-flow** anchor |
| ~82 minutes | rearing-tank retention time | UVI CA1 rearing tank | SRAC 454 and UVI 25-year paper describe earlier configuration and flow logic citeturn5view4turn25view0 | high | context split for earlier UVI system |
| ~1.37 hours | rearing-tank retention time | UVI CA2 rearing tank | UVI aquaponic systems page and UVI 25-year paper citeturn23view0turn25view0 | high | strongest **demo fish-tank exchange** anchor |
| ~19–20 minutes | clarifier retention time | UVI CA2 clarifiers | UVI aquaponic systems page and UVI 25-year paper citeturn23view0turn25view0 | high | strongest **demo clarifier** anchor |
| 9.5 minutes was inadequate relative to prior trials with >20 minutes | clarifier retention comparison | UVI CA1 vs earlier trials | UVI 25-year paper citeturn25view0 | high | strong evidence that too-short clarifier HRT hurts solids removal |
| 15–30 minutes | hydraulic retention time | general RAS settling basin | SRAC 453 citeturn24view0 | high | best general RAS clarifier/settling-basin range |
| ~3 hours | trough water-retention time | UVI DWC/raft hydroponic troughs | UVI 25-year paper; corroborated by UVI abstract noting 125 L/min and 3 h trough retention citeturn7view0turn15view0 | high | strongest **demo raft/DWC retention** anchor |
| “Unimportant as long as they are aerated” | qualitative rule | deep-flow hydroponic channels | UVI aquaponic systems page citeturn23view0 | high | strong rule for DWC/raft: aeration matters more than strict exchange target |
| “Unaerated channels must have a faster exchange rate” | qualitative rule | hydroponic channels without aeration | UVI aquaponic systems page citeturn23view0 | high | strong warning rule |
| Less than 2% daily water exchange in closed aquaponic recirculation | daily exchange fraction | aquaponics general | SRAC 454 revised version citeturn17view2 | medium | useful broad aquaponics context, not a demo default |
| 5% weekly dump during filter cleaning | weekly replacement / dilution | UVI CA2 | UVI 25-year paper citeturn7view0 | high | important if using UVI-style steady-state benchmark |
| Air stones 3–4 feet apart in plant troughs | spacing anchor | aquaponic plant trough aeration | Texas A&M aquaponics extension citeturn16view0 | medium | small-to-medium system trough aeration anchor |
| One air stone per 10 square feet | spacing anchor | DWC float bed aeration | SRAC 5007 citeturn19view0 | high | strongest small-system DWC aeration anchor |

## Stocking-density context table

| value or range | unit | system context | hardware or aeration dependency | source | confidence | recommended use |
|---|---:|---|---|---|---|---|
| ~30 | kg fish/m3 | highly aerated tank systems | no supplemental pure oxygen assumed | SRAC 282 citeturn11view2 | high | strong **warmwater tank baseline** context row |
| 60–72 | kg fish/m3 | some highly aerated systems | requires efficient solids removal and low suspended solids | SRAC 282 citeturn11view2 | medium | context split, not a default |
| 90–120 | kg fish/m3 | systems using supplemental oxygen | not vigorous aeration alone; oxygen-supported designs | SRAC 282 citeturn11view3 | medium | high-intensity context only |
| 182 fish/m3; final biomass 81.1 kg/m3 | fish/m3; kg/m3 | UVI CA1 red tilapia | diffused aeration system; later judged too high for best growth/FCR | UVI 25-year paper citeturn25view0 | high | strong historical context; do not use as first default |
| 154 fish/m3; production 70.7 kg/m3 | fish/m3; kg/m3 | UVI CA2 red tilapia | commercial raft system | UVI 25-year paper citeturn25view0 | high | commercial context split |
| 77 fish/m3; production 61.5 kg/m3 | fish/m3; kg/m3 | UVI CA2 Nile tilapia | commercial raft system; reported as near-optimal for desired product size | UVI 25-year paper citeturn25view0 | high | strongest **Nile tilapia + UVI DWC/raft** context row |
| No universal single density | structural note | tilapia tank/RAS/aquaponics | depends on oxygenation, solids removal, pH, feed rate and desired final size | SRAC 282 plus UVI CA1/CA2 comparison citeturn11view2turn11view4turn25view0 | high | must remain scenario-dependent |

## TAN-N load to concentration requirements

The strongest explicit feed-to-ammonia-load equation surfaced in the source set is:

- **PTAN = F × PC × 0.092 / t**
- where **PTAN** is **kg of total ammonia nitrogen per day**, **F** is feed provided per day, **PC** is feed protein fraction in decimal form, and **t** is usually one day. citeturn26view0

That gives a **load**, not a concentration. To move from load to concentration, the minimum defensible engineering picture needs a **control volume** and a **time basis**. Texas A&M’s aquaponics guidance is explicit that limited water volume can make unionized ammonia rise quickly after feeding, whereas ponds dilute it because their water volume is much larger relative to fish load. citeturn16view1

The minimum **practical** input set for recirculating concentration is:

- **TAN-N load over a defined time period**
- **control-volume choice**: fish tank, treatment loop, or total system
- **effective water volume** of that control volume
- **timestep / accumulation period**
- **exchange / recirculation / retention term**, or an explicit assumption that there is none
- **biofilter removal assumption or biofilter state**
- **replacement or inflow-water concentration**, if exchange/dilution is non-zero. citeturn26view0turn16view1turn23view0turn25view0

A defensible first-pass formula candidate for implementation design is therefore an **engineering mass-balance inference**, not a sourced threshold:

- **Upper-bound no-removal estimate**  
  `ΔC_TAN-N ≈ load_TAN-N_over_Δt / effective_water_volume`
- **Mixed-volume estimate with dilution/removal**  
  `C_next = C_now + ((load - biofilter_removal - other_removal) - exchange_loss + inflow_gain) / volume`

That structure is justified by the cited sources because they show that **tank exchange**, **clarifier retention**, **DWC retention**, **water dumping/replacement**, and **biofilter status** all materially change concentration outcomes. citeturn23view0turn25view0turn7view0turn24view0

The most important unsafe shortcuts to avoid are:

- dividing daily TAN-N load by **total system volume** when the real question is **fish-tank peak risk**
- assuming the whole coupled system is **instantaneously and uniformly mixed**
- assuming **100% biofilter conversion** every timestep
- treating **TAN-N load/day** as if it were already a **mg/L concentration**
- producing NH3 risk without **pH** and **temperature**. citeturn3view4turn23view0turn25view0turn14view0

A particularly important inference for the MVP is that UVI’s reported component residence times imply **two different useful concentration scopes**:

- **fish-tank-local TAN-N**, for fish safety and near-term NH3 warning logic
- **whole-system average TAN-N**, for slower nutrient accumulation and plant-side diagnostics. citeturn23view0turn25view0

## TAN concentration to NH3 risk requirements

To move from TAN concentration to unionized NH3 risk, the strongest required-input set is:

- **TAN concentration basis**, preferably **TAN-N mg/L**
- **pH**
- **water temperature**
- **freshwater versus saline context**
- **threshold-unit basis** for the comparison target
- **exposure duration context**, because chronic and short-term danger are not the same. citeturn13view0turn27view0turn3view4turn22view3

Texas A&M’s aquaponics extension states that unionized ammonia is calculated from **TAN + pH + temperature**, and that **TAN alone reveals nothing about toxicity**. It also shows example cases where the same TAN is safe or dangerous depending on pH and temperature. citeturn3view4turn16view2

Tilapia-specific stress evidence from SRAC 283 adds the exposure caveat that **feeding depression begins around 0.08 mg/L un-ionized ammonia**, **first mortalities from prolonged exposure may begin around 0.2 mg/L**, and **losses occur above about 1 mg/L**, especially in fry or juveniles and under low DO. This is stronger for tilapia physiology than general aquaponics guidance, but its unit basis should still be stored explicitly because aquaculture literature is inconsistent about “as N” labelling. citeturn22view3turn22view0

For general warmwater RAS management, SRAC 452 recommends **un-ionized ammonia-N below 0.05 ppm**, and lists **high ammonia above 0.05 ppm as un-ionized** as a management trigger. Texas A&M’s aquaponics note is less conservative and calls for **increased monitoring at 0.25 ppm unionized ammonia** and says many species begin to die at **0.5 ppm**. These should not be silently merged: they are different source families with different contexts and likely different unit framings. citeturn8view4turn16view3turn16view4

## Unionized NH3 fraction method

The strongest explicit freshwater method is the Florida DEP SOP, which states:

- `pKa = 0.0901821 + 2729.92 / Tk`
- where `Tk = °C + 273.2`
- and the un-ionized ammonia fraction is  
  `f = 1 / (10^(pKa - pH) + 1)`. citeturn13view0

EPA’s 2013 freshwater ammonia criteria document gives the same freshwater pKa relation and notes that **total ammonia (often expressed as TAN)** is the sum of **NH4+ and NH3**, and that Emerson et al.’s formulas are recommended for estimating the relative concentrations from total ammonia. citeturn27view0

For MVP purposes, the clean freshwater method is:

- **input:** `TAN-N mg/L`, `pH`, `temperature °C`, and freshwater assumption
- **compute:** `f_NH3`
- **compute:** `NH3-N mg/L = TAN-N × f_NH3`
- **optional:** `NH3 mg/L = NH3-N × 17/14` if threshold source is stated as NH3 rather than NH3-N. citeturn13view0turn27view0

Important limitations:

- The Florida DEP SOP is explicit that the freshwater equation was developed for **zero salinity** and that salinity affects the fraction; a different correction is needed for saline water. citeturn13view0
- The same SOP also emphasises that **field pH and field temperature** matter, and that pH error of even **±0.1** is important. citeturn13view0
- Texas A&M’s extension note recommends tables or calculators based on Emerson et al. if the operator is not using the direct formula. citeturn3view4

## Unit and terminology conversion notes

The safest first-pass terminology stack is:

- **PTAN load**: `kg TAN-N / day`
- **TAN concentration**: `mg TAN-N / L`
- **unionized fraction**: dimensionless `f_NH3`
- **unionized concentration (as N)**: `mg NH3-N / L`
- **optional unionized concentration (as NH3)**: `mg NH3 / L`. citeturn26view0turn13view0turn27view0

Safe conversions:

- `NH3 mg/L = NH3-N mg/L × 17/14`
- `NH3-N mg/L = NH3 mg/L × 14/17`.  
  Florida DEP states this explicitly. citeturn13view0

Unsafe conversions:

- **TAN-N to “TAN as NH3”** with a single molecular-weight factor is **not** safe, because TAN is a mixture of **NH4+ and NH3**, and the mixture depends on **pH and temperature**. EPA and UF/IFAS both make clear that TAN is the sum of ionized and un-ionized forms and that their ratio depends on pH and temperature. citeturn27view0turn14view0
- Treating any source that says simply “ammonia” as if it unambiguously means **NH3**, **NH3-N**, or **TAN-N** is unsafe. Texas A&M and UF/IFAS both discuss “ammonia” in sections that analytically refer to **total ammonia nitrogen**, while toxicological discussion turns to the **unionized** part. citeturn3view4turn14view0

Recommended modelling rule:

- Keep **TAN-N** as the core concentration basis.
- Partition to **NH3-N** with pH and temperature.
- Convert to **NH3** only when the comparison threshold explicitly requires NH3 units. citeturn13view0turn27view0

## Biofilter conversion and removal assumptions

What is strongly known:

- Nitrifying bacteria need oxygen; SRAC 452 says they become inefficient below **2 ppm DO** in the biofilter, while warmwater production generally aims for **5 ppm or more**. citeturn8view0turn8view5
- UF/IFAS says both nitrifier groups need **oxygen** and **alkalinity**, and that if oxygen is insufficient the process can break down; it also states that if alkalinity is **below 20 mg/L**, nitrifying bacteria will not function effectively. citeturn14view0
- UF/IFAS also says a new biofilter needs roughly **6–8 weeks** to build up sufficient bacteria to reduce ammonia and nitrite effectively. citeturn14view0
- UVI states that raft aquaponic systems can achieve adequate biofiltration in the hydroponic component and may have **excess treatment capacity** when the feeding-rate ratio is maintained correctly. citeturn23view0
- UVI’s 25-year paper goes further for that specific commercial raft design: the raft system showed wastewater-treatment capacity equivalent to about **180 g feed/m²/day**, and after an acclimation period of about one month, ammonia and nitrite did not need routine monitoring **provided the nitrifying film on the underside of the rafts remained intact**. citeturn7view0

What must remain scenario input:

- whether the biofilter is **mature**, **immature**, or **unknown**
- whether the plant side is **DWC/raft with intact nitrifying film**, **NFT requiring a separate biofilter**, or another architecture
- actual **alkalinity**, **pH**, **DO**, and **cleaning practice**
- actual **water replacement/dump rate**, because UVI’s final commercial system still dumped about **5% of system water weekly** during filter cleaning. citeturn23view0turn14view0turn7view0

What should not be assumed:

- that all feed-derived TAN is nitrified within one timestep
- that all DWC/raft systems behave like the UVI CA2 raft troughs
- that plant uptake alone replaces biofilter logic
- that NFT has the same nitrification surface behaviour as raft DWC.  
  UVI explicitly says NFT has less nitrification surface area and needs a separate biofilter. citeturn23view0

## MVP warning-label recommendations

| warning label concept | trigger condition | evidence basis | recommendation |
|---|---|---|---|
| concentration unavailable due to missing control volume | feed-derived TAN-N load exists but tank/system volume missing | concentration depends on limited water volume; load is not concentration citeturn16view1turn26view0 | keep as warning until a volume is supplied |
| concentration unavailable due to missing time basis | feed load given but no timestep / accumulation period | PTAN source is per day; concentration requires time basis citeturn26view0 | require explicit daily or sub-daily period |
| fish-tank concentration unavailable | total-system volume exists but fish-tank volume or exchange is missing | UVI reports distinct rearing-tank and whole-system residence times citeturn23view0turn25view0 | separate fish-tank from whole-system scope |
| NH3 risk unavailable due to missing pH | TAN concentration exists but pH missing | TAN alone reveals nothing about toxicity; fraction depends on pH citeturn3view4turn13view0turn27view0 | mandatory warning |
| NH3 risk unavailable due to missing temperature | TAN concentration exists but temperature missing | NH3 fraction depends on temperature citeturn3view4turn13view0turn27view0 | mandatory warning |
| freshwater formula assumed | pH and temperature known but salinity not supplied | freshwater equation is valid for zero/dilute salinity only citeturn13view0 | acceptable demo assumption if explicitly labelled |
| biofilter-removal assumption missing | concentration model uses recirculation but no removal state is supplied | nitrification depends on oxygen, alkalinity and maturity citeturn8view0turn14view0 | warn and fall back to conservative no-removal or low-removal mode |
| biofilter not mature | startup or recent reset state | UF/IFAS says new biofilter needs 6–8 weeks citeturn14view0 | high-severity warning |
| threshold-unit mismatch | comparing NH3-based threshold to NH3-N or TAN-N output without conversion | ammonia literature mixes TAN, NH3 and NH3-N citeturn13view0turn14view0turn27view0 | block comparison until basis is explicit |
| low-DO biofilter impairment risk | DO in biofilter or system below support level | nitrifiers inefficient below 2 ppm DO; warmwater growth target above 5 ppm citeturn8view0turn8view5 | strong warning |
| low-pH nitrification impairment risk | pH around 6 or lower | Texas A&M and UVI say nitrification is inhibited near 6 and can cease below it citeturn23view0turn16view4 | strong warning |

## Missing-context labels that can later become calculated outputs

These are the current “missing-context” areas that can defensibly become calculated values once enough inputs exist:

- **estimated_fish_tank_tan_n_mg_l**
- **estimated_system_average_tan_n_mg_l**
- **estimated_unionized_nh3_fraction**
- **estimated_nh3_n_mg_l**
- **estimated_nh3_mg_l**
- **estimated_rearing_tank_retention_h**, if tank volume and tank flow allocation are supplied
- **estimated_clarifier_retention_min**, if clarifier volume and clarifier flow are supplied
- **estimated_dwc_trough_retention_h**, if trough volume and trough flow are supplied.  
  These follow directly from the UVI-style residence-time framing and the formal NH3 fraction method. citeturn23view0turn25view0turn13view0

## Missing-context labels that should remain warnings

Even after more inputs are present, these should still remain warnings rather than pretending to be observed facts:

- **actual_biofilter_removal_efficiency_unknown**
- **actual_post_feeding_peak_spike_unknown**
- **actual_nitrifying_biofilm_condition_unknown**
- **actual_pH_measurement_quality_unknown**
- **actual_salinity_correction_unknown**
- **threshold_basis_mismatch_warning**
- **whole-system-average-only warning** when fish-tank-local concentration is not being modelled.  
  The sources support the need for these warnings because biofilter function depends on maturity, oxygen and alkalinity, and because UVI’s residence-time split means a whole-system average is not equivalent to fish-tank-local exposure. citeturn14view0turn8view0turn25view0

## Demo input candidates

The narrowest useful input pack beyond the existing load-only Mode A is:

- `feed_kg_day`
- `protein_fraction`
- `fish_tank_volume_l`
- `total_system_volume_l`
- `recirculation_flow_l_min` or `rearing_tank_retention_h`
- `water_temp_c`
- `pH`
- `biofilter_state` with at least `mature / immature / unknown`
- `concentration_scope` with at least `fish_tank / system_average / both`
- `replacement_water_fraction_per_day_or_week` or `dump_water_l_per_period`
- `freshwater_assumption` or `salinity_ppt`
- `threshold_basis_family` such as `NH3-N` or `NH3`.  
  This set is the smallest one that can support both concentration context and unionized-ammonia risk context without pretending to know more than the operator has supplied. citeturn26view0turn13view0turn23view0turn25view0

## Scenario-default candidates

These are reasonable **demo assumptions**, not canon:

- **freshwater / zero salinity assumption** for the first tilapia+basil DWC/raft slice, because the core formula set is explicitly freshwater and the crop/fish combination is freshwater by default. citeturn13view0
- **UVI CA2 benchmark volumes and flows**:
  - fish tank: **7,800 L**
  - total system: **111,196 L**
  - recirculation: **378 L/min**
  - rearing-tank retention: **1.37 h**
  - clarifier retention: **19–20 min**
  - hydroponic retention: **3 h**. citeturn25view0turn23view0
- **pH compromise mode around 7.0** for aquaponic operation, because UVI and Texas A&M both frame this as a practical compromise region. citeturn23view0turn16view5
- **weekly partial water loss/replacement around 5%** only if the demo is explicitly “UVI-like”; not as a global default. citeturn7view0
- **biofilter mature = false/unknown** as the safer default if the user has not stated startup age, because new biofilters take time to establish. citeturn14view0

## Customer-validation inputs

The following inputs should remain customer-, operator-, or adviser-validated before any serious claim is made:

- actual **fish-tank volume**
- actual **total system volume**
- actual **flow allocation per fish tank**
- actual **water replacement / dump schedule**
- actual **pH** and **temperature** at the time of interest
- actual **biofilter maturity and architecture**
- actual **stocking density** and target harvest size
- actual **threshold family** the customer wants used
- actual **salinity**, if the system is not plainly freshwater. citeturn25view0turn11view2turn13view0

## Do-not-use-yet findings

The following should **not** be promoted into early canon or hard-coded MVP logic:

- a universal **tank-volume default**
- a universal **stocking-density default**
- a universal **biofilter removal percent**
- a universal **water-exchange default**
- a universal **NH3 warning threshold** without explicit unit basis
- the assumption that **whole-system volume** is the right denominator for fish-exposure risk
- the assumption that **DWC/raft always eliminates the need for a separate biofilter**
- any conversion from **TAN-N** to a single “TAN as NH3” value without first partitioning NH3 and NH4+. citeturn11view2turn25view0turn23view0turn13view0turn27view0

## Open questions

- What default **biofilter-removal mode** is conservative but still useful for a mature DWC/raft demo: no removal, partial removal, or UVI-like benchmark mode?
- Should the first public-facing risk output use **NH3-N mg/L** or **NH3 mg/L** as its primary threshold basis?
- Will the MVP model a **daily average concentration**, a **post-feeding peak estimate**, or both?
- Should fish safety be judged from **fish-tank-local concentration**, **whole-system average concentration**, or a paired view?
- How should **tank-specific flow apportionment** be represented when total system flow is known but individual tank flow is not?
- How much **partial water replacement** is normal in non-UVI commercial DWC/raft systems, and does the MVP need a default dilution assumption or only an explicit user input? citeturn5view4turn25view0turn7view0

## Recommended next repo-side use

Codex should use this research to define, at the design level, a **three-stage water-quality interpretation chain**:

- **Stage one:** feed-derived **TAN-N load**
- **Stage two:** **estimated concentration** in a named scope such as `fish_tank` or `system_average`
- **Stage three:** **estimated unionized NH3 risk** from concentration + pH + temperature + explicit threshold basis.  
  That chain is directly aligned with the evidence stack and avoids pretending that a load is already a toxicological result. citeturn26view0turn3view4turn13view0

The next design pass should also define four explicit modelling choices:

- **concentration scope**: `fish_tank`, `system_average`, or both
- **unit conventions**: `TAN-N`, `NH3-N`, optional `NH3`
- **threshold-basis tagging**
- **biofilter state / removal mode** as a scenario input, not an invisible constant.  
  These are the minimum structural choices needed before replacing warning-only placeholders with calculated values. citeturn25view0turn13view0turn14view0

What could be implemented next in principle:

- estimated **fish-tank TAN-N**
- estimated **system-average TAN-N**
- estimated **NH3 fraction**
- estimated **NH3-N**
- warning logic for **missing pH**, **missing temperature**, **missing volume**, **missing exchange**, and **biofilter-not-mature**.  
  These are all directly supported by the cited evidence and do not require pretending to know basil saleable output or feed economics. citeturn23view0turn13view0turn14view0

What must remain warning-only for now:

- actual biofilter performance
- actual post-feeding peak transient
- actual plant-side nitrification contribution
- any “safe” or “unsafe” claim when unit basis is ambiguous. citeturn14view0turn23view0turn13view0

## Direct answers

1. **Minimum input set needed to move from TAN-N load to TAN concentration**

   Bare minimum for a crude upper-bound concentration increment: **TAN-N load over a defined time period + effective water volume**.  
   Minimum practical set for a recirculating aquaponics estimate: **TAN-N load + control-volume choice + effective volume + timestep + exchange/retention + biofilter-removal assumption/state + replacement/inflow concentration**. citeturn26view0turn16view1turn23view0turn25view0

2. **Minimum input set needed to move from TAN concentration to NH3 risk**

   **TAN concentration basis, pH, temperature, freshwater/salinity assumption, and threshold-unit basis**. Exposure duration should also be explicit if the system is going to compare against chronic or prolonged-exposure caution levels. citeturn13view0turn27view0turn22view3

3. **Which volume/exchange anchors are strongest for a tilapia + basil DWC/raft demo**

   The strongest anchors are the **UVI CA2 commercial raft values**: **7,800 L fish tanks, ~111,196 L total system volume, 378 L/min flow, 1.37 h fish-tank retention, ~19–20 min clarifier retention, and ~3 h hydroponic retention**. citeturn25view0turn23view0

4. **Which values can be used as demo assumptions without becoming canon**

   The UVI CA2 geometry and residence times, a **freshwater assumption**, and an aquaponic **pH compromise around 7.0** are all defensible as a named **demo preset**, provided they are explicitly labelled as UVI-like benchmark assumptions rather than defaults for all systems. citeturn25view0turn23view0turn16view5

5. **Which values must remain user-supplied scenario inputs**

   Actual **volumes**, **flows**, **pH**, **temperature**, **replacement-water schedule**, **biofilter maturity/state**, **stocking density**, and **threshold family** must remain scenario inputs. citeturn25view0turn11view2turn13view0turn14view0

6. **What warning labels should the MVP report emit when context is missing**

   At minimum: **missing volume**, **missing time basis**, **fish-tank concentration unavailable**, **NH3 risk unavailable due to missing pH**, **NH3 risk unavailable due to missing temperature**, **biofilter assumption missing**, **biofilter not mature**, and **threshold-unit mismatch**. citeturn3view4turn13view0turn14view0turn25view0

7. **Which current labels can become calculated outputs after enough inputs exist**

   **Estimated fish-tank TAN-N**, **estimated system-average TAN-N**, **estimated NH3 fraction**, **estimated NH3-N**, **estimated NH3**, and **estimated subsystem retention times** can become calculated outputs. citeturn23view0turn25view0turn13view0

8. **What should the next Codex design pass do with this research**

   Define the **concentration scopes**, lock the **unit conventions**, require the minimum input set for concentration and NH3 risk, tag every threshold with its **unit basis**, and keep UVI-style values under a named **demo benchmark mode** rather than promoting them to canon. citeturn25view0turn13view0turn14view0