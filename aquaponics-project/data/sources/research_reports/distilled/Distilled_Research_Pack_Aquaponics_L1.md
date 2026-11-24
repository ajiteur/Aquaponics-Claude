# Distilled Research Pack

## Report metadata
- report_scope: Distilled synthesis of uploaded aquaponics Layer 1 Deep Research reports into implementation-ready findings for species profiles (tilapia, lettuce, basil) and component/parameter library (water chemistry, filtration, pumps, aeration), including simulation hooks and local file update mapping.
- source_files_used:
  - `/mnt/data/Tilapia Species Profile Corroboration Report for Aquaponics Layer 1.pdf` fileciteturn0file4
  - `/mnt/data/Lettuce_Corroboration report for aquaponics Layer 1 species profile.pdf` fileciteturn0file2
  - `/mnt/data/Basil_Corroboration report for aquaponics Layer 1 species profile.pdf` fileciteturn0file0
  - `/mnt/data/Water Chemistry and pH Management_Aquaponics Layer 1 Parameter Corroboration Report.pdf` fileciteturn0file5
  - `/mnt/data/Biofilters and solids filters_Corroboration report for aquaponics Layer 1.pdf` fileciteturn0file1
  - `/mnt/data/Pumps and aeration_Corroboration report for aquaponics Layer 1 component library.pdf` fileciteturn0file3
- generated_at: 2026-04-11 (Europe/Amsterdam)
- trust_policy_applied: Primary sources are the uploaded reports (each already constrained to Tier 1–2 underlying sources: university/experiment station/extension, SRAC/UVI, peer‑reviewed). No new broad web research performed; unresolved items list identifies gaps where direct Tier 1–2 originals should be ingested later. fileciteturn0file5

## Executive summary
- **System pH is a managed compromise variable**: strongest operational guidance anchors coupled aquaponics near **pH ≈7** with explicit tolerable envelopes (e.g., **6.4–7.4**) and narrower “optimal compromise” bands (e.g., **6.8–7.0**) to balance plants, fish, and nitrifiers. fileciteturn0file5
- **Do not model toxicity from TAN alone**: strong guidance repeatedly frames **unionised NH₃** (computed from TAN + pH + temperature) as the toxicity driver; paired with explicit warning thresholds. fileciteturn0file5
- **Tilapia Layer 1 defaults**: tank/RAS-like optimum growth temperature **~27–29 °C**; acceptable growth **~25–32 °C**; operational DO setpoint **~5–7.5 mg/L**; unionised NH₃ sensitivity ladder begins near **~0.08 mg/L** (feeding suppression) with escalating mortality thresholds. fileciteturn0file4
- **Lettuce Layer 1 defaults**: hydroponic optimum pH is tightly centred near **pH 5.8** (acceptable **5.6–6.0**), with preferred air temperatures around **≤24 °C day / ~18–19 °C night**; heat/fluctuations drive bolting; humidity/low transpiration drives tipburn. fileciteturn0file2
- **Basil Layer 1 defaults**: hydroponic preferred pH **~5.8–6.2** (but aquaponics often operates **~7.0–7.5**); preferred air temperature **~26–27.5 °C**; root-zone solution preferred **~27.5 °C**; chilling injury below **~10 °C**. Disease triggers for basil downy mildew are explicitly defined (leaf wetness and night RH). fileciteturn0file0
- **Filtration train**: remove solids **ahead of biofilter/hydroponics**. Clarifier design anchors include **15–30 min HRT** (UVI operationally ~19–20 min) and strong evidence that **radial-flow** settlers outperform **swirl** separators on TSS removal under tested conditions. fileciteturn0file1
- **Biofilter sizing anchors** are most implementation-ready when expressed per feed load: e.g., fluidised sand and some bead systems up to **~16–32 kg feed/m³ media/day**, MBBR **~8–16 kg feed/m³ media/day**; nitrification DO floor **~2 mg/L** and conservative DO setpoint **>5 mg/L** appear repeatedly. fileciteturn0file1
- **Pumps + aeration**: core pump deliverable is **stable turnover** (UVI-style rearing tank exchange ~1 hr; clarifier ~20 min; per-tank flow example 100 L/min), while aeration deliverable is **continuous DO protection** with alarm triggers like **DO <5 mg/L → increase aeration + stop feeding** and **CO₂ >20 mg/L → increase stripping/aeration**. fileciteturn0file3

## Standardized key findings

### Finding 1
- topic: Water chemistry and pH
- normalized_field_name: waterchem.pH_target_range_general
- statement: Use **pH 6.0–7.0** as the default *system-level target range* for coupled aquaponics.
- confidence: High
- context_tags: [aquaponics-specific, system-level, robust-compromise-mode]
- source_basis: Water Chemistry & pH Management report summarises Texas A&M AgriLife “target range” pH 6–7 (Table 1) as promote-to-accepted. fileciteturn0file5
- recommended_target_files: [data/simulation/parameters/waterchemistry.json, data/simulation/species_evidence/waterchemistry.evidence.json, knowledge-vault/Learnings/waterchemistry_pH.md]

### Finding 2
- topic: Water chemistry and pH
- normalized_field_name: waterchem.pH_compromise_optimal_and_tolerable
- statement: Encode **pH compromise optimal 6.8–7.0** and **tolerable envelope 6.4–7.4** for “all-components” operation (fish + plants + nitrifiers).
- confidence: High
- context_tags: [aquaponics-specific, system-level, compromise, nitrification+plant-uptake-balance]
- source_basis: Water Chemistry report promotes NMSU Circular 680: compromise 6.8–7.0; tolerable 6.4–7.4. fileciteturn0file5
- recommended_target_files: [data/simulation/parameters/waterchemistry.json, data/simulation/scenario_defaults.json, knowledge-vault/Learnings/pH_compromise.md]

### Finding 3
- topic: Water chemistry and pH
- normalized_field_name: waterchem.nitrification_pH_inhibition_ladder
- statement: Model nitrification performance as a ladder: **inhibited at ~pH 6.0**, increasing failure risk below; **die‑off risk begins below ~pH 5.5**.
- confidence: High
- context_tags: [aquaponics-specific, bacteria/nitrifiers, warning-ladder]
- source_basis: Water Chemistry report promotes Texas A&M statement: inhibited at pH 6.0; begin dying below 5.5, and corroborates with UVI “practically ceases <6.0”. fileciteturn0file5
- recommended_target_files: [data/simulation/models/nitrification_models.json, data/simulation/parameters/waterchemistry.json, data/simulation/species_evidence/waterchemistry.evidence.json]

### Finding 4
- topic: Water chemistry and pH
- normalized_field_name: waterchem.TAN_target_guidance
- statement: Use **TAN < 1 ppm** as an operational guidance target (not a hard toxicity rule), with explicit note: fish tolerate higher TAN if **pH < 7.0**.
- confidence: Medium-High
- context_tags: [aquaponics-specific, operational-guidance, TAN, pH-dependent-toxicity]
- source_basis: Water Chemistry report promotes NMSU: “recommended TAN <1 ppm”, plus pH dependence. fileciteturn0file5
- recommended_target_files: [data/simulation/parameters/waterchemistry.json, data/simulation/species_evidence/waterchemistry.evidence.json]

### Finding 5
- topic: Water chemistry and pH
- normalized_field_name: waterchem.NH3_unionised_thresholds_actions
- statement: Add unionised ammonia operational triggers: **≥0.25 ppm NH₃ → increased monitoring**, **≥0.5 ppm NH₃ → fish may begin to die**.
- confidence: Medium-High
- context_tags: [aquaponics-specific, safety-thresholds, NH3, temperature-dependent]
- source_basis: Water Chemistry report promotes Texas A&M operational monitoring thresholds for unionised ammonia. fileciteturn0file5
- recommended_target_files: [data/simulation/scenario_defaults.json, data/simulation/models/toxicity_models.json, data/simulation/species_evidence/waterchemistry.evidence.json]

### Finding 6
- topic: Water chemistry and pH
- normalized_field_name: waterchem.alkalinity_target_CaCO3
- statement: Maintain alkalinity **≈100 mg/L as CaCO₃ or above** as a stabilising target for pH control in aquaponics.
- confidence: High
- context_tags: [aquaponics-specific, alkalinity/buffering, pH-stability]
- source_basis: Water Chemistry report promotes consistent alkalinity targets from NMSU/SRAC/Texas A&M clustered at ≳100 mg/L as CaCO₃. fileciteturn0file5
- recommended_target_files: [data/simulation/parameters/waterchemistry.json, data/simulation/models/acid_base_models.json]

### Finding 7
- topic: Tilapia
- normalized_field_name: tilapia.preferred_pH_range
- statement: For fish physiology, store preferred/ideal pH as **6.5–8.5** (ideal band), separate from aquaponics compromise pH.
- confidence: Medium
- context_tags: [general_aquaculture, warmwater, species-physiology]
- source_basis: Tilapia report promotes WorldFish “ideal pH 6.5–8.5” as preferred pH for profile. fileciteturn0file4
- recommended_target_files: [data/simulation/species/fish/tilapia.json, data/simulation/species_evidence/fish/tilapia.evidence.json]

### Finding 8
- topic: Tilapia
- normalized_field_name: tilapia.tolerated_pH_range_and_best_performance
- statement: Store tolerated pH **5–10** with “do best” performance band **6–9** (fish-only).
- confidence: High
- context_tags: [general_aquaculture, warmwater, species-physiology]
- source_basis: Tilapia report summarises SRAC 283: survive 5–10; do best 6–9. fileciteturn0file4
- recommended_target_files: [data/simulation/species/fish/tilapia.json, data/simulation/species_evidence/fish/tilapia.evidence.json]

### Finding 9
- topic: Tilapia
- normalized_field_name: tilapia.preferred_temperature_range_c
- statement: Use **27–29 °C** as tank/RAS-like **optimum growth** temperature for tilapia.
- confidence: High
- context_tags: [RAS_baseline, warmwater, growth-optimised]
- source_basis: Tilapia report promotes SRAC 282 “optimum growth 27–29°C”. fileciteturn0file4
- recommended_target_files: [data/simulation/species/fish/tilapia.json, data/simulation/species_evidence/fish/tilapia.evidence.json]

### Finding 10
- topic: Tilapia
- normalized_field_name: tilapia.tolerated_temperature_range_c
- statement: Use **25–32 °C** as “acceptable growth” temperature band for tank/RAS contexts.
- confidence: High
- context_tags: [RAS_baseline, warmwater, tolerated_growth_band]
- source_basis: Tilapia report promotes SRAC 282 “acceptable growth 25–32°C”. fileciteturn0file4
- recommended_target_files: [data/simulation/species/fish/tilapia.json, data/simulation/species_evidence/fish/tilapia.evidence.json]

### Finding 11
- topic: Tilapia
- normalized_field_name: tilapia.DO_operational_targets_and_stress_ladder
- statement: Encode DO ladder: **5.0–7.5 mg/L recommended operating**, **chronic <3.5 mg/L → growth/feed impacts**, and much lower short-term survival possible (system-specific).
- confidence: High
- context_tags: [RAS_baseline, warmwater, operational_target, stress_ladder]
- source_basis: Tilapia report promotes SRAC 282 DO operating range and chronic impact threshold. fileciteturn0file4
- recommended_target_files: [data/simulation/species/fish/tilapia.json, data/simulation/models/oxygen_models.json]

### Finding 12
- topic: Tilapia
- normalized_field_name: tilapia.NH3_UIA_sensitivity_ladder
- statement: Use unionised NH₃ ladder: **0.08 mg/L → feeding suppression**, **0.2 mg/L → mortality onset (prolonged)**, **>1 mg/L → losses**, **>2 mg/L → massive mortality risk** (strongly duration/DO/stage dependent).
- confidence: High
- context_tags: [general_aquaculture, warmwater, toxicity_ladder, context_dependent_high]
- source_basis: Tilapia report promotes SRAC 283 ladder (and SRAC 282 avoid >1 mg/L ceiling). fileciteturn0file4
- recommended_target_files: [data/simulation/species/fish/tilapia.json, data/simulation/models/toxicity_models.json, data/simulation/species_evidence/fish/tilapia.evidence.json]

### Finding 13
- topic: Lettuce
- normalized_field_name: lettuce.preferred_pH_range
- statement: Hydroponic/CEA lettuce pH: **optimum 5.8** with acceptable **5.6–6.0**; store as the plant-optimised baseline.
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse/CEA, plant-optimised]
- source_basis: Lettuce report promotes Cornell CEA handbook pH optimum/acceptable band. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/species_evidence/plants/lettuce.evidence.json]

### Finding 14
- topic: Lettuce
- normalized_field_name: lettuce.pH_lockout_high_risk
- statement: Treat **pH >7** as a nutrient availability risk (lockout/availability interference), especially for micronutrients.
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse, pH_lockout]
- source_basis: Lettuce report promotes UK CCD note that source water pH >7 interferes with nutrient availability; also includes high-pH micronutrient solubility mechanism. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/models/nutrient_uptake_models.json]

### Finding 15
- topic: Lettuce
- normalized_field_name: lettuce.preferred_air_temperature_range_c
- statement: Use lettuce preferred air temperature setpoints: **≤24 °C day** and **~18–19 °C night** (quality oriented).
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse/CEA, air_temperature]
- source_basis: Lettuce report promotes UK CCD day/night caps + Cornell CEA setpoints alignment. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/scenario_defaults.json]

### Finding 16
- topic: Lettuce
- normalized_field_name: lettuce.tolerated_cold_temperature_range_c
- statement: Lettuce can tolerate **10 °C night / 15 °C day** in winter conditions, but with slower time-to-harvest.
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse_winter, suboptimal_but_possible]
- source_basis: Lettuce report promotes UK CCD tolerance statement with explicit consequence. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/models/growth_models.json]

### Finding 17
- topic: Lettuce
- normalized_field_name: lettuce.nutrient_demand_N_and_EC_anchor
- statement: Hydroponic recipe anchor: **N ≈150 ppm** with **EC ≈1.5 mS/cm** (example fertigation).
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse, nutrient_recipe_anchor]
- source_basis: Lettuce report promotes UK CCD Table 1 fertigation recipe (N and EC). fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/parameters/nutrients.json]

### Finding 18
- topic: Lettuce
- normalized_field_name: lettuce.aquaponics_nitrate_min_spec_mg_L
- statement: Aquaponics anchor: maintain nitrate around **~47 mg/L** (reported as a minimal specification supporting good lettuce growth).
- confidence: Medium-High
- context_tags: [aquaponics-specific, DWC/raft, nitrate_anchor]
- source_basis: Lettuce report promotes UH CTAHR aquaponics/hydroponics lettuce guidance “nitrate ~47 mg/L minimal spec”. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/species_evidence/plants/lettuce.evidence.json]

### Finding 19
- topic: Lettuce
- normalized_field_name: lettuce.stress_bolting_heat_fluctuations
- statement: Model bolting/quality failure trigger: **prolonged heat and/or high temperature fluctuations → bolting → bitterness/unmarketable**.
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse, heat_stress_quality_failure]
- source_basis: Lettuce report promotes UK CCD bolting trigger statement. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/models/plant_stress_models.json]

### Finding 20
- topic: Lettuce
- normalized_field_name: lettuce.stress_tipburn_humidity_transpiration_Ca
- statement: Tipburn is driven by **humid microclimate + low transpiration → poor Ca transport**, with a management knob of **Ca 40–50 ppm** as a starting point.
- confidence: Medium-High
- context_tags: [hydroponic_baseline, greenhouse, humidity_stress, physiological_disorder]
- source_basis: Lettuce report promotes e‑GRO E406 tipburn mechanism and Ca starting point. fileciteturn0file2
- recommended_target_files: [data/simulation/species/plants/lettuce.json, data/simulation/models/plant_stress_models.json, data/simulation/parameters/nutrients.json]

### Finding 21
- topic: Basil
- normalized_field_name: basil.preferred_pH_range_hydroponics
- statement: Hydroponic/soilless basil preferred pH: **5.8–6.2** (primary) with corroborating table value **5.5–6.0**.
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse/CEA, plant-optimised]
- source_basis: Basil report promotes SCRI CEA Herbs (5.8–6.2) and OSU Extension table corroboration (5.5–6.0). fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/species_evidence/plants/basil.evidence.json]

### Finding 22
- topic: Basil
- normalized_field_name: basil.pH_operating_aquaponics
- statement: Coupled aquaponics basil is demonstrated under **pH 7.0–7.5** control with observed **~6.9–7.6** in UVI trials; treat as aquaponics operating evidence, not hydroponic optimum.
- confidence: High
- context_tags: [aquaponics-specific, warmwater, commercial-scale, system-compromise]
- source_basis: Basil report promotes UVI basil aquaponics trial pH control/observed range. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/scenario_defaults.json]

### Finding 23
- topic: Basil
- normalized_field_name: basil.pH_lockout_or_deficiency_rules
- statement: Encode basil pH disorder rules: **pH <5.8 → Fe/Mn toxicity symptoms**, **pH >6.5 → Fe deficiency (chlorosis)**; corrective action triggers **5.5–5.7** (low) and **6.2–6.4** (high).
- confidence: High
- context_tags: [hydroponic_baseline, greenhouse, pH_lockout, nutrient_disorder]
- source_basis: Basil report promotes SCRI CEA Herbs basil factsheet thresholds and corrective triggers. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/models/nutrient_uptake_models.json, knowledge-vault/Learnings/basil_pH_disorders.md]

### Finding 24
- topic: Basil
- normalized_field_name: basil.preferred_temperature_ranges_air_and_solution_c
- statement: Preferred basil temperatures: **air ~26–27.5 °C**, **solution/root-zone ~27.5 °C**; tested solution band **23–31 °C** (operational, not lethal).
- confidence: Medium-High
- context_tags: [hydroponic_baseline, NFT, greenhouse, air_temp_and_solution_temp]
- source_basis: Basil report promotes Hendrickson et al. (*HortScience*) air and root-zone temperature statements and test conditions. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/models/growth_models.json]

### Finding 25
- topic: Basil
- normalized_field_name: basil.tolerated_cold_stress_threshold_c
- statement: Basil is chilling sensitive: injury below **~10 °C**; severe injury at **≤5 °C** (quality loss/unmarketable).
- confidence: High
- context_tags: [general_or_postharvest, cold_stress_quality_failure, temperature_threshold]
- source_basis: Basil report promotes Simon et al. 2021 chilling threshold summary. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/models/plant_stress_models.json]

### Finding 26
- topic: Basil
- normalized_field_name: basil.nutrient_demand_N_EC_and_tolerance
- statement: Nutrient anchor: basil “best” with **100–150 ppm N** and **EC 0.5–1.5 mS/cm**; robustness note: EC up to **~5.5 dS/m** did not reduce final growth over **8 weeks** (context‑dependent).
- confidence: Medium-High
- context_tags: [hydroponic_baseline, greenhouse_or_indoor, nutrient_anchor, tolerance_note]
- source_basis: Basil report promotes SCRI CEA Herbs N/EC guidance and Solis‑Toapanta 2020 EC tolerance finding. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/parameters/nutrients.json]

### Finding 27
- topic: Basil
- normalized_field_name: basil.aquaponics_nitrateN_anchor_mg_L
- statement: UVI aquaponics basil nitrate‑N anchor: **~42 mg/L nitrate‑N** (reported ranges roughly mid‑20s to low‑50s).
- confidence: Medium-High
- context_tags: [aquaponics-specific, warmwater, nitrateN_anchor]
- source_basis: Basil report promotes UVI table value “Nitrate‑N 42.2 (26.7–54.7) / 42.9 (30.9–51.8) mg/L”. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/species_evidence/plants/basil.evidence.json]

### Finding 28
- topic: Basil
- normalized_field_name: basil.growth_yield_aquaponics_kg_m2
- statement: Aquaponics yield anchor (UVI): mean basil yield **2.0 kg/m² (batch)** and **1.8 kg/m² (staggered)**; field comparison **0.6 kg/m²**.
- confidence: High
- context_tags: [aquaponics-specific, commercial-scale, yield_anchor]
- source_basis: Basil report promotes UVI abstract yield figures for batch/staggered/field. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/models/growth_models.json]

### Finding 29
- topic: Basil
- normalized_field_name: basil.stress_multi_harvest_root_disease_and_deficiency
- statement: Multi-harvest risk: cutting weakens plants; roots infected with **Pythium**; deficiencies visible by **4th harvest**; final survival **~84.7%** after harvest cycles.
- confidence: High
- context_tags: [aquaponics-specific, multi_cut, disease_risk, cumulative_deficiency]
- source_basis: Basil report promotes UVI “Pythium after cutting” + “deficiencies by fourth harvest” + “final survival 84.7%”. fileciteturn0file0
- recommended_target_files: [data/simulation/species/plants/basil.json, data/simulation/models/plant_stress_models.json]

### Finding 30
- topic: Basil
- normalized_field_name: basil.disease_downy_mildew_triggers
- statement: Basil downy mildew greenhouse triggers: **leaf wetness ≥4 h** and **night RH >95% for >7.5 h**; pathogen temperature window **~53–77 °F**, optimum **~68 °F**.
- confidence: High
- context_tags: [greenhouse, disease_trigger, humidity_leafwetness, temperature_window_pathogen]
- source_basis: Basil report promotes UConn IPM bulletin trigger thresholds and temperature window. fileciteturn0file0
- recommended_target_files: [data/simulation/models/disease_models.json, data/simulation/species/plants/basil.json, knowledge-vault/Learnings/basil_downy_mildew.md]

### Finding 31
- topic: Biofilters and solids filters
- normalized_field_name: solids_filter.design_settling_HRT_minutes
- statement: Clarifier/settling design anchors: **15–30 min HRT** (RAS); aquaponics operational corroboration: **~19–20 min** improves capture vs **~9.5 min**; sludge removal can be multiple times daily.
- confidence: High
- context_tags: [RAS_baseline, aquaponics-specific, warmwater, small_to_commercial]
- source_basis: Biofilters+solids report promotes SRAC settling HRT 15–30 min and UVI clarifier retention time and sludge removal frequency. fileciteturn0file1
- recommended_target_files: [data/simulation/components/component_library.json, data/simulation/components/component_variants.json, data/simulation/models/solids_models.json]

### Finding 32
- topic: Biofilters and solids filters
- normalized_field_name: solids_filter.performance_TSS_removal_and_surface_loading
- statement: Settler performance anchors (tested): surface loading **0.0031 m³/s per m²**; mean TSS removal **~77.9% radial-flow** vs **~37.1% swirl** at that loading.
- confidence: Medium-High
- context_tags: [RAS_baseline, coolwater_study, performance_anchor, solids_capture]
- source_basis: Biofilters+solids report promotes Davidson & Summerfelt performance comparison and surface loading rate. fileciteturn0file1
- recommended_target_files: [data/simulation/models/solids_models.json, data/simulation/components/component_variants.json]

### Finding 33
- topic: Biofilters and solids filters
- normalized_field_name: biofilter.sizing_feed_loading_kgfeed_per_m3_media_day
- statement: Feed-based sizing anchors: **fluidised sand 16–32 kg feed/m³/day**, **MBBR 8–16 kg feed/m³/day**, **bead systems 16–32 kg feed/m³/day** (conditional on frequent washing).
- confidence: High
- context_tags: [RAS_baseline, sizing_anchor, biofilter_variants]
- source_basis: Biofilters+solids report promotes SRAC 0453 design practice capacities for sand, MBBR, and beads. fileciteturn0file1
- recommended_target_files: [data/simulation/components/component_library.json, data/simulation/components/component_variants.json, data/simulation/models/nitrification_models.json]

### Finding 34
- topic: Biofilters and solids filters
- normalized_field_name: nitrification.feed_to_TAN_formula_and_stoichiometry
- statement: Nitrification modelling anchors: **PTAN = F × PC × 0.092 (kg/day)**; oxygen demand **4.57 g O₂ per g TAN‑N**, alkalinity demand **7.14 g CaCO₃ per g TAN‑N** (commonly reported).
- confidence: Medium-High
- context_tags: [RAS_baseline, mass_balance, nitrification_stoichiometry]
- source_basis: Biofilters+solids report promotes Ebeling et al. formula and “normally reported” O₂/alkalinity demands. fileciteturn0file1
- recommended_target_files: [data/simulation/models/nitrification_models.json, data/simulation/models/oxygen_models.json, data/simulation/models/acid_base_models.json]

### Finding 35
- topic: Biofilters and solids filters
- normalized_field_name: biofilter.startup_protocol_and_maturation_dynamics
- statement: Startup hooks: **raise TAN to 3–5 mg/L (fishless cycling)**; **alkalinity 150 mg/L (better 200–250)**; **pH 6.8–7.2 best**; ammonia then nitrite peak after lag; warm temps (e.g., **28 °C**) speed cycling.
- confidence: High
- context_tags: [RAS_baseline, startup, maturation_lag, temperature_sensitive]
- source_basis: Biofilters+solids report promotes SRAC 4502 start-up steps, monitoring parameters, and lag narrative. fileciteturn0file1
- recommended_target_files: [data/simulation/models/nitrification_models.json, data/simulation/scenario_defaults.json, knowledge-vault/Learnings/biofilter_startup.md]

### Finding 36
- topic: Pumps and aeration
- normalized_field_name: pump.exchange_rate_targets_UVI_style
- statement: Turnover anchors in coupled aquaponics: rearing tank exchange **~1 hr target** (UVI example **1.37 hr**); clarifier **20 min**; per-tank flow anchor **~100 L/min** with full exchange **~1:20 hrs**; total four-tank flow **~100 gpm**.
- confidence: High
- context_tags: [aquaponics-specific, warmwater, commercial-scale, hydraulic_stability]
- source_basis: Pumps+aeration report promotes UVI exchange rate targets and UVI CAS per-tank flow plus OSU/SRAC four-tank flow anchor. fileciteturn0file3
- recommended_target_files: [data/simulation/components/component_library.json, data/simulation/models/hydraulics_models.json, data/simulation/scenario_defaults.json]

### Finding 37
- topic: Pumps and aeration
- normalized_field_name: aeration.DO_targets_and_continuous_operation
- statement: Aeration/DO anchors: warmwater DO should be **>60% saturation or >5 mg/L**; nitrifiers become inefficient below **2 mg/L**; aeration must operate **continuously** in intensive systems.
- confidence: High
- context_tags: [RAS_baseline, warmwater, safety_setpoints, nitrification_support]
- source_basis: Pumps+aeration report promotes SRAC 0452 DO targets, nitrifier DO threshold, and continuous aeration requirement. fileciteturn0file3
- recommended_target_files: [data/simulation/models/oxygen_models.json, data/simulation/models/nitrification_models.json, data/simulation/scenario_defaults.json]

### Finding 38
- topic: Pumps and aeration
- normalized_field_name: aeration.alarm_thresholds_DO_CO2_actions
- statement: Encode operational triggers: **DO <5 mg/L → increase aeration + stop feeding**; **CO₂ >20 mg/L → add stripping/increase aeration**; fish crowding/gulping indicates low oxygen.
- confidence: High
- context_tags: [RAS_baseline, alarm_thresholds, operational_actions]
- source_basis: Pumps+aeration report promotes SRAC 0452 Table 8 and fish behaviour indicators. fileciteturn0file3
- recommended_target_files: [data/simulation/scenario_defaults.json, data/simulation/models/fish_behaviour_models.json, data/simulation/models/oxygen_models.json]

### Finding 39
- topic: Pumps and aeration
- normalized_field_name: pump_and_aeration.failure_modes_and_backup_patterns
- statement: Model failure modes: poor mixing can create supersaturation zones → gas bubble disease (fry sensitive); NFT flow disruption → rapid wilting/death; require emergency aeration + backup power.
- confidence: High
- context_tags: [RAS_baseline, aquaponics-specific, failure_modes, backup_required]
- source_basis: Pumps+aeration report promotes SRAC mixing/supersaturation warning, OSU NFT flow disruption note, and SRAC+UVI backup guidance. fileciteturn0file3
- recommended_target_files: [data/simulation/models/aeration_models.json, data/simulation/models/hydraulics_models.json, data/simulation/components/component_variants.json]

### Finding 40
- topic: Pumps and aeration
- normalized_field_name: energy.anchor_UVI_example_kW
- statement: Energy anchors (context-split UVI examples): pump **0.37 kW** (or **0.74 kW** in earlier trial) at ~378 L/min; blowers **1.1 kW** (fish) and **0.74 kW** (plants).
- confidence: Medium (context-split)
- context_tags: [aquaponics-specific, commercial-scale, energy_anchor, needs_version_tag]
- source_basis: Pumps+aeration report notes UVI hosted-copy motor ratings and flags contradiction across system versions. fileciteturn0file3
- recommended_target_files: [data/simulation/components/component_variants.json, data/simulation/models/energy_models.json]

## Best excerpts to ingest

### Excerpt 1
- topic: Water chemistry and pH
- excerpt_text: “Compromise… pH of **6.8 to 7.0**… tolerable… **6.4 and 7.4**.”
- why_it_matters: Single most implementation-ready pH compromise + tolerable envelope for coupled systems.
- recommended_use: Codex pH module; `waterchem.pH_compromise_optimal_and_tolerable`. fileciteturn0file5

### Excerpt 2
- topic: Water chemistry and pH
- excerpt_text: “TAN… maintained at **<1 ppm**… fish can tolerate higher TAN… if **pH… <7.0**.”
- why_it_matters: Converts TAN “limit” into a conditional rule linked to toxicity computation.
- recommended_use: `waterchem.TAN_target_guidance` + NH₃ conversion hook. fileciteturn0file5

### Excerpt 3
- topic: Water chemistry and pH
- excerpt_text: “Start increased monitoring when unionized ammonia… **0.25 ppm**… begin to die… **0.5 ppm**…”
- why_it_matters: Direct alarm thresholds for safety modelling and UI warnings.
- recommended_use: `waterchem.NH3_unionised_thresholds_actions`. fileciteturn0file5

### Excerpt 4
- topic: Biofilters and solids filters
- excerpt_text: “hydraulic retention times… **15 to 30 minutes**.”
- why_it_matters: Core sizing rule for clarifiers/settlers; maps directly to solids capture performance.
- recommended_use: `solids_filter.design_settling_HRT_minutes`. fileciteturn0file1

### Excerpt 5
- topic: Biofilters and solids filters
- excerpt_text: “coarse sand fluidized bed… **16 to 32 kg/m³/day**” and MBBR “**8 to 16 kg/m³/day**.”
- why_it_matters: Feed-rate proportional sizing is the most scalable + simulation-friendly foundation.
- recommended_use: component variants + sizing formulas in simulator. fileciteturn0file1

### Excerpt 6
- topic: Biofilters and solids filters
- excerpt_text: “PTAN = **F × PC × 0.092**.”
- why_it_matters: Enables feeding → TAN → biofilter load → oxygen/alkalinity demand modelling.
- recommended_use: `nitrification.feed_to_TAN_formula_and_stoichiometry`. fileciteturn0file1

### Excerpt 7
- topic: Pumps and aeration
- excerpt_text: “Low dissolved oxygen (**<5 ppm**)… **increase aeration**… **stop feeding** until corrected.”
- why_it_matters: Concrete operational trigger for failure prevention and gameplay feedback.
- recommended_use: `aeration.alarm_thresholds_DO_CO2_actions`. fileciteturn0file3

### Excerpt 8
- topic: Pumps and aeration
- excerpt_text: “Water is pumped… **100 l/min**… full volume exchange every **1:20 hrs**.”
- why_it_matters: Strong hydraulic anchor to calibrate turnover-time effects.
- recommended_use: hydraulics defaults + pump component variant baseline. fileciteturn0file3

### Excerpt 9
- topic: Tilapia
- excerpt_text: Unionised NH₃ begins to depress feeding at **0.08 mg/L**; first mortalities may begin around **0.2 mg/L** (prolonged).
- why_it_matters: Core fish-toxicity ladder for warnings and mortality model.
- recommended_use: `tilapia.NH3_UIA_sensitivity_ladder`. fileciteturn0file4

### Excerpt 10
- topic: Lettuce
- excerpt_text: “Air temperature… should not exceed **24 °C**… day and **18 °C** at night…”
- why_it_matters: Direct temperature setpoints for quality and bolting avoidance.
- recommended_use: `lettuce.preferred_air_temperature_range_c`. fileciteturn0file2

### Excerpt 11
- topic: Basil
- excerpt_text: “Plants prefer a pH within the range of **5.8 to 6.2**…”
- why_it_matters: Simple hydroponic pH target for basil; yields predictable nutrient availability.
- recommended_use: `basil.preferred_pH_range_hydroponics`. fileciteturn0file0

### Excerpt 12
- topic: Basil
- excerpt_text: “Needs at least **4 hours** of leaf wetness… and more than **7.5 hours**… humidity (**>95%**) at night…”
- why_it_matters: Disease model trigger variables (greenhouse) that map cleanly to simulation.
- recommended_use: `basil.disease_downy_mildew_triggers`. fileciteturn0file0

## Recommended local actions

### Action 1
- priority: P0
- action: Update `tilapia.json` with DO ladder + NH₃ ladder + temperature growth bands; store aquaponics operating setpoints separately from physiology.
- target_files: [data/simulation/species/fish/tilapia.json, data/simulation/species_evidence/fish/tilapia.evidence.json, data/simulation/scenario_defaults.json]
- reason: Tilapia report explicitly recommends a two-layer approach (physiology vs aquaponics operation) and provides crisp thresholds. fileciteturn0file4

### Action 2
- priority: P0
- action: Update lettuce species JSON with tight pH optimum band and thermal setpoints; add bolting and tipburn stress rules.
- target_files: [data/simulation/species/plants/lettuce.json, data/simulation/species_evidence/plants/lettuce.evidence.json, data/simulation/models/plant_stress_models.json]
- reason: Lettuce report provides direct setpoints and simulation-ready stress triggers. fileciteturn0file2

### Action 3
- priority: P0
- action: Update basil species JSON with hydroponic vs aquaponics pH split, root-zone temperature preference, chilling thresholds, and downy mildew triggers.
- target_files: [data/simulation/species/plants/basil.json, data/simulation/species_evidence/plants/basil.evidence.json, data/simulation/models/disease_models.json]
- reason: Basil report is already structured as candidate fields with promotion flags and includes explicit disease trigger variables. fileciteturn0file0

### Action 4
- priority: P0
- action: Refactor water chemistry parameter library into separate records: pH target, pH compromise optimal, tolerable envelope, nitrification pH ladder, TAN guidance, NH₃ action thresholds, alkalinity targets.
- target_files: [data/simulation/parameters/waterchemistry.json, data/simulation/species_evidence/waterchemistry.evidence.json, knowledge-vault/Learnings/waterchemistry_pH.md]
- reason: Water chemistry report explicitly recommends splitting “accepted targets” into context-tagged records rather than promoting vague ranges. fileciteturn0file5

### Action 5
- priority: P0
- action: Update filtration component library with clarifier HRT defaults, settler performance variants (radial vs swirl), and biofilter sizing by feed load (sand/MBBR/bead).
- target_files: [data/simulation/components/component_library.json, data/simulation/components/component_variants.json, data/simulation/models/solids_models.json, data/simulation/models/nitrification_models.json]
- reason: Biofilters/solids report provides the most “engineering-anchored” sizing and performance primitives in your library. fileciteturn0file1

### Action 6
- priority: P0
- action: Implement nitrification mass-balance + demands: feed → TAN production formula, plus O₂ and alkalinity demand coefficients.
- target_files: [data/simulation/models/nitrification_models.json, data/simulation/models/oxygen_models.json, data/simulation/models/acid_base_models.json]
- reason: Biofilters/solids report gives formulaic anchors and notes their assumptions, enabling consistent simulator behaviour. fileciteturn0file1

### Action 7
- priority: P1
- action: Expand pump/aeration component library with exchange-rate defaults, DO setpoints, and alarm-based operational responses.
- target_files: [data/simulation/components/component_library.json, data/simulation/models/hydraulics_models.json, data/simulation/models/aeration_models.json, data/simulation/scenario_defaults.json]
- reason: Pumps/aeration report provides the most simulation-ready operational triggers and turnover anchors. fileciteturn0file3

### Action 8
- priority: P1
- action: Create component variants for “power-backup posture” (none / generator / generator+mobile backup) with failure probabilities and recovery delays.
- target_files: [data/simulation/components/component_variants.json, data/simulation/models/failure_models.json, data/simulation/scenario_defaults.json]
- reason: UVI backup maintenance pattern is explicit and can be mapped to resilience mechanics. fileciteturn0file3

### Action 9
- priority: P1
- action: Create contradiction tickets for (a) pump power anchors (0.37 vs 0.74 kW) and (b) any “single-number” pH strategy that conflicts with the pH~6 plant-yield optimisation branch.
- target_files: [data/research_reports/distilled/contradictions.md, knowledge-vault/Learnings/contradictions_log.md]
- reason: Uploaded reports explicitly flag these as context-splits/contradictions requiring version tags or mode selection. fileciteturn0file3turn0file5

### Action 10
- priority: P2
- action: Write Obsidian source notes per uploaded report (one note per PDF) with a “promoted values” block and “provisional/context split” block.
- target_files: [knowledge-vault/Sources/Reports/Tilapia_L1.md, knowledge-vault/Sources/Reports/Lettuce_L1.md, knowledge-vault/Sources/Reports/Basil_L1.md, knowledge-vault/Sources/Reports/WaterChem_L1.md, knowledge-vault/Sources/Reports/Filtration_L1.md, knowledge-vault/Sources/Reports/PumpsAeration_L1.md]
- reason: Makes evidence tracking durable and keeps Codex/JSON updates auditable. fileciteturn0file4turn0file2turn0file0turn0file5turn0file1turn0file3

## Candidate simulation hooks

### Hook 1
- variable_or_model_area: ammonia_toxicity_model
- proposed_rule: Compute unionised NH₃ from TAN + pH + temperature; apply multi-threshold ladder (monitoring, feeding suppression, mortality) rather than a single TAN limit.
- evidence_strength: High
- depends_on: waterchem NH₃ action thresholds; tilapia NH₃ ladder; temperature & pH model linkage. fileciteturn0file5turn0file4

### Hook 2
- variable_or_model_area: nitrification_rate_vs_pH
- proposed_rule: Apply nitrification performance multiplier that declines around pH ~6.0 and collapses toward/below ~5.5; add optional “plant-yield mode” pH~6 with higher nitrification monitoring burden.
- evidence_strength: Medium-High
- depends_on: waterchem nitrification pH ladder; scenario “mode” flag. fileciteturn0file5

### Hook 3
- variable_or_model_area: nitrification_oxygen_floor
- proposed_rule: If biofilter DO <2 mg/L, nitrification efficiency sharply reduces; if DO <5 mg/L, apply system-wide stress and prompt “increase aeration / stop feeding”.
- evidence_strength: High
- depends_on: aeration DO targets and alarm threshold rules. fileciteturn0file3turn0file1

### Hook 4
- variable_or_model_area: feed_to_TAN_load
- proposed_rule: TAN production per day: PTAN = feed_mass × protein_fraction × 0.092; propagate to TAN concentration via hydraulics/volume and to oxygen/alkalinity demand via coefficients.
- evidence_strength: Medium-High
- depends_on: feed composition model, tank volumes, exchange rates, solids removal assumption. fileciteturn0file1

### Hook 5
- variable_or_model_area: clarifier_capture_and_solids_carryover
- proposed_rule: Settler TSS capture increases with HRT (target band 15–30 min) and with better settler type (radial > swirl); under-sized HRT increases downstream clogging/disease risk.
- evidence_strength: Medium-High
- depends_on: chosen solids filter variant; flow rate; HRT. fileciteturn0file1

### Hook 6
- variable_or_model_area: pump_failure_hydraulic_instability
- proposed_rule: When pump stops, turnover time → ∞; fish tank TAN/CO₂ accumulates; aeration distribution degrades; NFT plants rapidly wilt/die.
- evidence_strength: High
- depends_on: pump state, aeration state, plant system type (NFT vs DWC), backup power. fileciteturn0file3

### Hook 7
- variable_or_model_area: DWC_exchange_vs_aeration_tradeoff
- proposed_rule: If DWC channels aerated, channel exchange-rate constraint relaxes; if unaerated, enforce faster exchange to avoid root hypoxia.
- evidence_strength: High
- depends_on: aeration coverage in plant channels; plant system type. fileciteturn0file3

### Hook 8
- variable_or_model_area: lettuce_bolting_risk
- proposed_rule: Bolting probability increases with sustained air temperature above recommended cap and with high temperature fluctuations; bolting reduces quality/marketability.
- evidence_strength: High
- depends_on: greenhouse climate model; cultivar optional. fileciteturn0file2

### Hook 9
- variable_or_model_area: lettuce_tipburn_risk
- proposed_rule: Tipburn risk increases with high humidity/low airflow (low transpiration) and fast growth; Ca supply is a mitigation knob but does not fully solve if microclimate is poor.
- evidence_strength: Medium-High
- depends_on: humidity/airflow model; nutrient model; growth rate. fileciteturn0file2

### Hook 10
- variable_or_model_area: basil_downy_mildew_infection_model
- proposed_rule: Trigger downy mildew infection when leaf wetness ≥4h and night RH >95% ≥7.5h within pathogen temperature window; apply yield/quality penalties.
- evidence_strength: High
- depends_on: greenhouse humidity, leaf wetness proxy, night duration, temperature. fileciteturn0file0

## Unresolved items

### Unresolved item 1
- issue: FAO “Small-scale aquaponic food production” manual not directly ingested as primary text
- why_unresolved: Water chemistry report notes the FAO PDF was not retrievable during research; only secondary references were used.
- what_evidence_is_still_needed: Direct ingestion of FAO manual sections on pH, filtration, pumps/aeration, monitoring targets (Tier 1 primary). fileciteturn0file5

### Unresolved item 2
- issue: Pump power draw anchor contradiction (0.37 kW vs 0.74 kW at similar reported flow)
- why_unresolved: Same UVI hosted-copy document reports different motor ratings across system versions/trials.
- what_evidence_is_still_needed: Identify which value corresponds to which UVI system configuration and whether it is nameplate or measured draw. fileciteturn0file3

### Unresolved item 3
- issue: TAN-from-feed alternative rule (2.2 lb NH₃‑N per 100 lb feed) not reconciled with protein-based equation
- why_unresolved: Reports flag it as provisional pending reconciliation of assumptions (protein %, assimilation, solids removal).
- what_evidence_is_still_needed: Decide a single canonical TAN production model (protein-based preferred) and keep the other only as a cross-check. fileciteturn0file1

### Unresolved item 4
- issue: Lettuce “preferred pH 6.0–7.0” in some small-system tables vs tight CEA optimum ~5.8
- why_unresolved: Lettuce report flags table-based 6–7 values as context-dependent and potentially not trial-derived.
- what_evidence_is_still_needed: Decide whether to add a “small-system/low-precision” mode or keep one global lettuce pH optimum. fileciteturn0file2

### Unresolved item 5
- issue: Basil tolerates pH as low as 4.0 in short trial vs toxicity guidance below 5.8 in soilless substrate
- why_unresolved: Basil report flags likely differences by system type (water culture vs substrate), nutrient recipe, and duration.
- what_evidence_is_still_needed: Decide whether to encode pH<5.8 as “disorder risk” and allow short-run pH 4.0 only as a special-case experiment. fileciteturn0file0

### Unresolved item 6
- issue: Missing direct energy-per-oxygenation anchors (e.g., kg O₂/kWh, blower curves) in uploaded reports
- why_unresolved: Pump/aeration report provides only limited kW anchors from UVI; not enough for general energy modelling.
- what_evidence_is_still_needed: Tier 1–2 RAS/aquaponics engineering manuals or peer‑reviewed aeration efficiency studies to parameterise energy models. fileciteturn0file3

## Per-topic distilled summaries

### Tilapia
- strongest accepted-style findings:
  - `tilapia.preferred_temperature_range_c`: 27–29 °C optimum growth (tank/RAS) fileciteturn0file4
  - `tilapia.tolerated_temperature_range_c`: 25–32 °C acceptable growth fileciteturn0file4
  - `tilapia.DO_operational_targets_and_stress_ladder`: DO 5.0–7.5 mg/L recommended; chronic <3.5 mg/L growth/feed penalty fileciteturn0file4
  - `tilapia.NH3_UIA_sensitivity_ladder`: 0.08 / 0.2 / >1 / >2 mg/L UIA thresholds (warning→mortality) fileciteturn0file4
- strongest provisional/context-split findings:
  - `tilapia.preferred_pH_range` (WorldFish ideal 6.5–8.5) vs aquaponics operational pH compromise near 7 (store separately) fileciteturn0file4turn0file5
- top recommended next update:
  - Implement NH₃ computation + DO ladder in the simulator UI/alerts so growth penalties appear before mortality (“teaching” feedback loop). fileciteturn0file4turn0file5

### Lettuce
- strongest accepted-style findings:
  - `lettuce.preferred_pH_range`: optimum 5.8; acceptable 5.6–6.0 (CEA baseline) fileciteturn0file2
  - `lettuce.preferred_air_temperature_range_c`: ≤24 °C day; ~18–19 °C night fileciteturn0file2
  - `lettuce.nutrient_demand_N_and_EC_anchor`: N ~150 ppm; EC ~1.5 mS/cm fileciteturn0file2
  - `lettuce.stress_bolting_heat_fluctuations`: prolonged heat/fluctuations → bolting → unmarketable fileciteturn0file2
  - `lettuce.stress_tipburn_humidity_transpiration_Ca`: humidity/low transpiration drives tipburn; Ca 40–50 ppm as mitigation knob fileciteturn0file2
- strongest provisional/context-split findings:
  - `lettuce.aquaponics_nitrate_min_spec_mg_L`: nitrate ~47 mg/L minimal spec (aquaponics DWC context) fileciteturn0file2
  - Broader pH tables (6–7) kept as “small system” context, not plant-optimised CEA fileciteturn0file2
- top recommended next update:
  - Add “climate microenvironment” variables (humidity/airflow) as first-class drivers for lettuce quality failures (tipburn) and bolting risk. fileciteturn0file2

### Basil
- strongest accepted-style findings:
  - `basil.preferred_pH_range_hydroponics`: 5.8–6.2 (hydroponic baseline) fileciteturn0file0
  - `basil.pH_operating_aquaponics`: 7.0–7.5 controlled; 6.9–7.6 observed (UVI) fileciteturn0file0
  - `basil.preferred_temperature_ranges_air_and_solution_c`: air ~26–27.5 °C; root-zone ~27.5 °C fileciteturn0file0
  - `basil.tolerated_cold_stress_threshold_c`: injury <10 °C; severe ≤5 °C fileciteturn0file0
  - `basil.disease_downy_mildew_triggers`: leaf wetness + RH triggers + temperature window fileciteturn0file0
- strongest provisional/context-split findings:
  - `basil.nutrient_demand_N_EC_and_tolerance`: EC up to 5.5 dS/m no growth loss (8 weeks) is context-specific; keep as robustness note, not default target fileciteturn0file0
  - Low pH tolerance down to 4.0 is short-run, cultivar and recipe dependent; treat as special-case fileciteturn0file0
- top recommended next update:
  - Add “multi-harvest stress” state to basil that increases root disease probability and nutrient deficiency risk in later cuts. fileciteturn0file0

### Water chemistry and pH
- strongest accepted-style findings:
  - `waterchem.pH_target_range_general`: 6.0–7.0 target fileciteturn0file5
  - `waterchem.pH_compromise_optimal_and_tolerable`: 6.8–7.0 optimal; 6.4–7.4 tolerable fileciteturn0file5
  - `waterchem.TAN_target_guidance`: TAN <1 ppm guidance with pH dependency fileciteturn0file5
  - `waterchem.NH3_unionised_thresholds_actions`: NH₃ 0.25 monitor; 0.5 die fileciteturn0file5
  - `waterchem.alkalinity_target_CaCO3`: ≳100 mg/L CaCO₃ target fileciteturn0file5
- strongest provisional/context-split findings:
  - `waterchem.pH_strategy_mode`: option for plant-yield optimisation around pH ~6 in DWC aquaponics (context-split; monitor nitrification) fileciteturn0file5
- top recommended next update:
  - Encode pH as a **strategy/mode variable** (robust compromise vs plant-yield optimisation) and link to required monitoring intensity and risk multipliers. fileciteturn0file5

### Biofilters and solids filters
- strongest accepted-style findings:
  - `solids_filter.design_settling_HRT_minutes`: 15–30 min HRT; UVI ~19–20 min operational target fileciteturn0file1
  - `solids_filter.performance_TSS_removal_and_surface_loading`: surface loading 0.0031 m³/s/m²; radial > swirl TSS removal fileciteturn0file1
  - `biofilter.sizing_feed_loading_kgfeed_per_m3_media_day`: sand 16–32; MBBR 8–16; beads 16–32 (wash-dependent) fileciteturn0file1
  - `nitrification.feed_to_TAN_formula_and_stoichiometry`: PTAN equation + O₂/alkalinity coefficients fileciteturn0file1
  - `biofilter.startup_protocol_and_maturation_dynamics`: cycling TAN 3–5 mg/L; alkalinity 150–250; pH 6.8–7.2; lag curve fileciteturn0file1
- strongest provisional/context-split findings:
  - Alternative TAN-from-feed rule (2.2 lb per 100 lb feed) kept as cross-check only fileciteturn0file1
- top recommended next update:
  - Implement biofilter start-up as a distinct scenario phase (“maturing”) where nitrification capacity ramps over time and is temperature/pH/DO dependent. fileciteturn0file1

### Pumps and aeration
- strongest accepted-style findings:
  - `pump.exchange_rate_targets_UVI_style`: ~1 hr rearing tank exchange target; 20 min clarifier; per tank 100 L/min (UVI CAS) fileciteturn0file3
  - `aeration.DO_targets_and_continuous_operation`: DO >5 mg/L (warmwater); nitrifiers inefficient <2; continuous aeration fileciteturn0file3
  - `aeration.alarm_thresholds_DO_CO2_actions`: DO <5 stop feeding/increase aeration; CO₂ >20 add stripping fileciteturn0file3
  - `pump_and_aeration.failure_modes_and_backup_patterns`: emergency aeration + backup power; NFT flow disruption kills plants quickly fileciteturn0file3
- strongest provisional/context-split findings:
  - `energy.anchor_UVI_example_kW`: treat power draw anchors as system-version tagged values only fileciteturn0file3
- top recommended next update:
  - Add explicit “backup posture” to scenarios and tie it to catastrophic failure probability during power loss events. fileciteturn0file3

## File generation map
- data/simulation/species/fish/tilapia.json
  - populate: `preferred_pH_range`, `tolerated_pH_range`, `preferred_temperature_range_c`, `tolerated_temperature_range_c`, `DO_ladder`, `NH3_UIA_ladder` fileciteturn0file4
- data/simulation/species/plants/lettuce.json
  - populate: `preferred_pH_range`, `preferred_air_temperature_range_c`, `tolerated_cold_temperature_range_c`, `nutrient_demand_N_EC`, `stress_bolting`, `stress_tipburn` fileciteturn0file2
- data/simulation/species/plants/basil.json
  - populate: hydroponic pH range, aquaponics operating pH range, air/solution temperature targets, nutrient anchors, downy mildew triggers, multi-harvest stress rules fileciteturn0file0
- data/simulation/species_evidence/fish/tilapia.evidence.json
  - ingest: atomic evidence records for DO and NH₃ ladders, temperature bands, pH bands (with context tags) fileciteturn0file4
- data/simulation/species_evidence/plants/lettuce.evidence.json
  - ingest: Cornell/UKY pH and temperature setpoints; bolting and tipburn triggers; aquaponics nitrate anchor fileciteturn0file2
- data/simulation/species_evidence/plants/basil.evidence.json
  - ingest: hydroponic vs aquaponic pH split; temperature targets; nutrient/pH disorder triggers; disease triggers; yield anchors fileciteturn0file0
- data/simulation/parameters/waterchemistry.json
  - populate: `pH_target_range_general`, `pH_compromise_optimal`, `pH_tolerable_envelope`, `alkalinity_target`, `TAN_guidance`, `NH3_unionised_thresholds` fileciteturn0file5
- data/simulation/components/component_library.json
  - add: solids filter types + clarifier HRT targets; biofilter types + feed-based sizing capacities; pump and aeration roles + targets fileciteturn0file1turn0file3
- data/simulation/components/component_variants.json
  - add variants: `settler_radial_flow`, `settler_swirl`, `microscreen_drum_20_60um`, `biofilter_fluidised_sand`, `biofilter_MBBR`, `biofilter_bead`, `pump_UVI_100Lmin`, `aeration_DWC_airstone_density`, `backup_none/generator/generator_plus_mobile` fileciteturn0file1turn0file3
- data/simulation/models/hydraulics_models.json
  - implement: turnover time τ (rearing tank ~1h default; clarifier ~20 min; DWC exchange relaxable if aerated) fileciteturn0file3
- data/simulation/models/aeration_models.json
  - implement: DO setpoint (>5), nitrifier inefficiency (<2), continuous-operation requirement, CO₂ stripping trigger (>20) fileciteturn0file3
- data/simulation/models/nitrification_models.json
  - implement: start-up maturation lag; feed→TAN formula; pH and DO multipliers fileciteturn0file1turn0file5
- data/simulation/models/solids_models.json
  - implement: clarifier HRT effects; radial vs swirl TSS capture differences; solids carryover penalties (clogging/disease) fileciteturn0file1
- data/simulation/scenario_defaults.json
  - set defaults: robust pH compromise mode (~7), alkalinity target, DO setpoint, pump turnover target, alarm thresholds and response actions fileciteturn0file5turn0file3
- data/research_reports/distilled/Distilled_Research_Pack_Aquaponics_L1.md
  - save this output verbatim
- knowledge-vault/Sources/Reports/
  - create notes: `Tilapia_L1_Profile.md`, `Lettuce_L1_Profile.md`, `Basil_L1_Profile.md`, `WaterChem_L1.md`, `Filtration_L1.md`, `Pumps_Aeration_L1.md` with promoted vs provisional blocks fileciteturn0file4turn0file2turn0file0turn0file5turn0file1turn0file3
- knowledge-vault/Learnings/
  - add synthesis notes: `pH_compromise_strategy.md`, `NH3_toxicity_ladder.md`, `biofilter_startup_maturation.md`, `aquaponics_resilience_backup.md`
- pumps and aeration specific:
  - data/simulation/components/component_variants.json (power-backup variants; pump flow variants) fileciteturn0file3
  - data/simulation/models/hydraulics_models.json (turnover-time effects + pump failure) fileciteturn0file3
  - data/simulation/models/aeration_models.json (continuous aeration, DO alarms, CO₂ stripping) fileciteturn0file3
  - data/simulation/scenario_defaults.json (DO <5 response rule; CO₂ >20 response; backup posture default) fileciteturn0file3