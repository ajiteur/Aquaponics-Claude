# Operating Economics Input Research Pack for the Aquaponics MVP

## Executive summary

The safest first economics layer is a **cost-pressure layer**, not a profitability layer. The MVP already has daily biological/engineering load outputs from feed; with explicit business inputs, it can next calculate **daily feed cost**, **daily pump/blower electricity cost**, **daily alkalinity-buffer cost**, **daily water-replacement cost**, and **task-based filter-maintenance labour cost**. It should **not** calculate profit, gross margin, fish revenue, or basil revenue until explicit revenue inputs and fuller cost coverage exist. citeturn37search4turn36search4turn1view1

Feed needs the strictest handling. Across tilapia production contexts, feed is routinely one of the largest operating-cost drivers: FAO guidance for Nile tilapia and milkfish in the Philippines states feed accounts for **50–70% of production costs**, while a peer-reviewed commercial tilapia risk study reports **71–74%** feed-cost shares in the analysed cases. That makes feed-price sensitivity worth showing early, but it also means a fake “default feed price” would distort the MVP quickly. citeturn37search4turn36search4

Public price evidence is strong enough to support **scenario inputs**, not canon. India has retrievable tilapia/fish-feed seller prices around the mid-₹30s to high-₹40s per kg depending on protein, product and seller, but much of this is supplier or marketplace evidence rather than institutional benchmarking. The Netherlands/EU context is weaker for tilapia-specific public pricing; the best readily retrievable public analogue in this pass was a commercial UK/EU aquaculture-feed seller listing a 25 kg, 38% protein fish pellet at **£46.78**. US extension budgets remain useful for structure, but the feed and power prices in them are historical planning assumptions rather than current market defaults. citeturn23search0turn25search10turn25search7turn26view1turn1view1

Electricity should be modelled from **equipment power × runtime × tariff**, with a clear distinction between **nameplate power** and **measured operating power**. The Dutch official statistics are strong enough to supply reference bands for non-household electricity, but these are still best used as scenario examples, not canonical defaults. In the second half of 2025, CBS reported total electricity prices for Dutch non-household consumers of **€0.241/kWh** for the 500–2,000 MWh band and **€0.115/kWh** for the 150,000+ MWh band; Eurostat reported an EU average of **€0.1837/kWh** for medium non-household consumers in the same period. citeturn8view2turn6view1

For alkalinity cost, the MVP is now close to a useful operating-cost bridge: because alkalinity is already expressed on a CaCO3-equivalent basis in aquaponics/RAS management, the next step is not to invent a universal buffer material price, but to require **material identity, purity/neutralising value, package basis, and price metadata**. Calcium hydroxide and potassium hydroxide are standard aquaponic pH-raising choices because they also supply plant nutrients; sodium bicarbonate is a common recirculating-aquaculture buffer. citeturn29view2turn29view1turn30search6

The highest-confidence maintenance-cost bridge is **task-based**, not blanket labour rates. UVI commercial aquaponics documentation gives directly useful recurring solids tasks: clarifier solids removal **three times daily** and filter-tank cleaning **one or two times weekly**. Those frequencies are valuable as a design pattern for a maintenance library, but they should still be treated as scenario/context-dependent rather than universal. citeturn31search0turn31search4turn29view1

## Evidence hierarchy and context splits

**Evidence hierarchy used**

1. **Institutional and extension sources** for enterprise-budget structure, water chemistry, and operating practices: UF/IFAS, Texas A&M, NMSU, SRAC/NCRAC, UVI, CBS, Eurostat, CEA, FAO. citeturn1view1turn29view0turn29view1turn31search0turn8view2turn6view1turn9search1turn37search4  
2. **Peer-reviewed studies** for economic cost shares and FCR context. citeturn36search4turn34view0  
3. **Supplier / seller pages** only where needed for current product-and-package price examples, and always marked as non-canonical. citeturn25search10turn23search0turn26view1

**Context split notes**

- **Netherlands / EU:** strong on electricity tariff statistics, weak on public tilapia-feed price sheets. Use Dutch/EU power numbers as reference-grade scenario examples; use feed prices only as EU-adjacent analogues unless you later collect supplier quotations or invoices. citeturn8view2turn6view1turn26view1  
- **India:** stronger public visibility on seller-side fish-feed prices than on clean institutional tilapia-feed benchmarks. Use Indian feed-price evidence only as scenario input scaffolding, with mandatory date, protein and package metadata. Electricity is state- and tariff-class-specific; this pass found indicative state examples, but not a single national commercial tariff default that is safe to canonise. citeturn25search10turn23search0turn25search7turn9search1turn12search1  
- **US / extension budgets:** excellent for structure and cost-category decomposition; weak for current pricing unless the budget is recent and local to the target scenario. The UF/IFAS tilapia enterprise budget explicitly states its price assumptions, making it useful as a modelling template and not as today’s market rate. citeturn1view1  
- **Global / institutional benchmarks:** reliable for “feed is a dominant cost” and for keeping economics linked to feed quality/FCR rather than arbitrary price assumptions. citeturn37search4turn36search4turn37search0

## Feed price evidence and feed-cost calculation basis

**Feed price evidence table**

| Price | Unit | Currency | Region | Date basis | Supplier / source type | Package size | Feed class / protein | Confidence | Recommended use | Classification |
|---|---:|---|---|---|---|---|---|---|---|---|
| $0.20 | per lb | USD | US | Budget assumption in UF/IFAS enterprise budget, updated 2026 page for legacy budget | Extension enterprise budget | not stated in line item; purchased feed | juvenile feed | Medium for structure, low for current price | historical benchmark only; useful for schema and sensitivity scaffolding, not a live default | `do_not_use_yet` citeturn1view1 |
| $0.15 | per lb | USD | US | same budget source | Extension enterprise budget | not stated in line item; purchased feed | grow-out feed | Medium for structure, low for current price | historical benchmark only | `do_not_use_yet` citeturn1view1 |
| ₹44–₹47.5 | per kg | INR | India | current seller listing crawled in this pass | Supplier / marketplace listing | 20 kg bag | 4 mm tilapia feed, 32% protein | Medium-low | India scenario input example; store exact product metadata | `business_input_required` citeturn25search10 |
| ₹37 | per kg | INR | India | current manufacturer listing crawled in this pass | Manufacturer product listing | not clear from snippet | high-protein fish feed, not tilapia-specific | Low-medium | lower-end India analogue only; not tilapia-specific | `demo_assumption_candidate` citeturn23search0 |
| ₹38 | per kg | INR | India | current marketplace listing crawled in this pass | Marketplace listing | 25 kg | sinking fish feed, not clearly tilapia-specific | Low | broad India bracket only | `demo_assumption_candidate` citeturn25search7 |
| ₹40–₹45 | per kg | INR | India | current marketplace listing crawled in this pass | Marketplace listing | not uniform | floating fish feed, not clearly tilapia-specific | Low | broad India bracket only | `demo_assumption_candidate` citeturn25search7 |
| £46.78 | per 25 kg bag | GBP | UK / EU-adjacent | current seller listing crawled in this pass | Commercial aquaculture-feed seller | 25 kg | Aller Aqua “Best”, 38% protein, not tilapia-specific | Low-medium | EU-adjacent feed analogue for sensitivity only; do not label as Netherlands tilapia price | `demo_assumption_candidate` citeturn26view1 |

**Feed-cost calculation basis**

| Formula | Required inputs | Units | Limitations | Classification |
|---|---|---|---|---|
| `daily_feed_cost = feed_kg_day × feed_price_per_kg` | `feed_kg_day`, `feed_price_per_kg` | kg/day, currency/kg, currency/day | safest first-pass formula; valid only if feed price is explicitly supplied | `scenario_input_required` |
| `period_feed_cost = daily_feed_cost × days_in_period` | same plus period length | days | assumes unchanged feed class and price over the period | `scenario_input_required` |
| `feed_cost_per_kg_biomass = FCR × feed_price_per_kg` | `FCR`, `feed_price_per_kg` | ratio, currency/kg | useful for scenario analysis only when FCR context is explicit; not needed for Mode A load-costing | `customer_validation_required` |

EIA’s definition of the kilowatt-hour is the right pattern to copy conceptually for feed too: keep the MVP on **rate × quantity × time** rather than embedding assumptions inside opaque lump sums. citeturn35search0

**Feed-cost sensitivity approach**

Use **low / base / high** cases tied to explicit source types, not one fake “market price”:
- **Low:** bulk or lower-protein commercial feed in the target geography.
- **Base:** the actual quoted or recently paid feed for the scenario.
- **High:** higher-protein / smaller-package / specialist supply or stressed-market case.

That structure is justified because public examples differ materially by protein %, package size and seller type. The MVP should therefore require feed-price records to store:
- currency,
- date captured,
- geography,
- seller/supplier type,
- package size,
- feed class,
- crude protein %,
- whether price is quoted per kg or derived from bag price,
- source document / URL reference. citeturn25search10turn23search0turn26view1turn1view1

**FCR and feed-efficiency connection**

FCR is useful for:
- scenario comparisons,
- later biomass-plan reconciliation,
- “what if cheaper feed worsens efficiency?” analysis,
- feed cost per kg fish produced.

It is **not** required for first-pass daily feed cost if Mode A already receives `feed_kg_day`. UF/IFAS used FCR assumptions of **1.2** for juveniles and **1.75** for grow-out in its enterprise budget; a 2024 aquaponics-vs-RAS tilapia study reported tilapia FCR around **1.13 in aquaponics** and **1.27 in RAS** in that experimental context. Those numbers are useful for scenario ranges, but too context-dependent to hard-code as canon. citeturn1view1turn34view0

## Electricity and power-cost evidence and calculation basis

**Electricity / power-cost evidence table**

| Electricity price / basis | Unit | Currency | Geography | Date basis | Tariff / source type | Confidence | Recommended use | Classification |
|---|---:|---|---|---|---|---|---|---|
| 0.241 | per kWh | EUR | Netherlands | 2025 2nd semester* | CBS total price incl. VAT and tax, non-households 500–2,000 MWh | High | Dutch medium-user scenario example; not canon | `business_input_required` citeturn8view2 |
| 0.115 | per kWh | EUR | Netherlands | 2025 2nd semester* | CBS total price incl. VAT and tax, non-households ≥150,000 MWh | High | large-user Dutch lower-bound reference only | `do_not_use_yet` for MVP default citeturn8view2 |
| 0.1837 | per kWh | EUR | EU average | 2025 2nd semester | Eurostat non-household average for medium-size consumers; excludes refundable taxes and levies | High | EU benchmark context only | `demo_assumption_candidate` citeturn6view1 |
| ₹7.50 | per kWh | INR | Tamil Nadu, India | FY 2025–26 | HT-I energy charge from tariff-analysis document based on TNERC update | Medium-low | indicative India commercial-power example only | `demo_assumption_candidate` citeturn12search1 |
| ₹7.38 | per kWh | INR | Maharashtra, India | 2025 announcement | reported industrial power rate after revision | Low | rough India reference only; not safe for canon | `do_not_use_yet` citeturn5news38 |
| $0.07 | per kWh | USD | US | enterprise-budget assumption | UF/IFAS tilapia budget | Medium for structure, low for current market | historical benchmark only | `do_not_use_yet` citeturn1view1 |

\* CBS marks the two most recent semesters as provisional. citeturn8view0turn8view2

**Pump / aeration electricity-cost calculation basis**

| Formula | Required inputs | Units | Nameplate caveats | Classification |
|---|---|---|---|---|
| `kwh_day = Σ(device_kw × runtime_h_day × load_fraction)` | per-device power, runtime, load fraction | kW, h/day, kWh/day | safest if `device_kw` is measured; if only nameplate exists, mark higher uncertainty | `scenario_input_required` |
| `daily_power_cost = kwh_day × electricity_price_per_kwh` | `kwh_day`, tariff | kWh/day, currency/kWh | excludes fixed demand charges unless modelled separately | `business_input_required` |
| `daily_power_cost_with_fixed = energy_charge + apportioned_fixed_charge + demand_charge_if_applicable` | above plus monthly fixed/demand charges | currency/day | only worth adding once tariff schema supports it | `customer_validation_required` |

EIA defines one kWh as one kilowatt used for one hour, which is the correct basis for cost calculations. Oklahoma State notes that motor output horsepower depends on actual load as well as efficiency and power factor, so **measured kW** is better than relying purely on nameplate HP. citeturn35search0turn35search2

**Equipment metadata required for electricity-cost scenarios**

- device name / role,
- device type: pump, blower, aerator, oxygen cone, backup blower, controller,
- measured kW if available,
- otherwise nameplate kW or HP,
- runtime hours/day,
- duty cycle or control schedule,
- redundancy count,
- whether the device is always-on, duty-cycled, alarm-triggered, or backup-only,
- tariff class and whether demand/fixed charges apply.

These should all remain explicit scenario/business inputs, because RAS/aquaponics systems are power-dependent and backup infrastructure matters materially. SRAC’s tilapia tank-culture guidance warns that systems relying on continuous pumping/aeration/oxygenation are vulnerable to catastrophic losses without backup systems; FAO guidance similarly notes the need for emergency generators and security systems in recirculation systems. citeturn32search1turn32search15

**Backup-power cost input requirements**

Minimum categories:
- backup technology type,
- protected load list,
- backup runtime target,
- generator fuel consumption basis or battery capacity basis,
- fuel or recharge price,
- routine test-run schedule,
- service / maintenance cost,
- start reliability / alarm dependency.

These should remain **user-supplied**. The evidence supports the need for backup power, not a universal cost default. citeturn32search1turn32search15

## Buffer, water, solids and maintenance cost input requirements

**Alkalinity / buffer-cost input requirements**

Aquaponics guidance from UF and NMSU supports **calcium hydroxide** and **potassium hydroxide** as standard pH-raising materials because they also supply calcium and potassium to the crop; RAS buffering guidance commonly uses **sodium bicarbonate** to maintain alkalinity and pH. NMSU expresses alkalinity in **ppm CaCO3 equivalent**, which is the right canonical basis for a later cost bridge. citeturn29view2turn29view1turn30search6

**Cost bridge to support later**
- `alkalinity_demand_caCO3eq_kg_day` from the bio/chemistry engine,
- buffer material name,
- purity fraction,
- neutralising value or CaCO3-equivalent basis,
- package size,
- material price,
- dose conversion notes.

**Recommended cost formula**
- `required_material_kg_day = alkalinity_demand_caCO3eq_kg_day / effective_neutralising_value`
- `daily_buffer_cost = required_material_kg_day × price_per_kg`

Because materials differ chemically, the MVP should **not** assume that one kg of any base equals one kg CaCO3 equivalent without an explicit material record. That is why this belongs in a scenario/business-input layer, not canon. citeturn29view1turn30search6

**Classification**
- common material classes: `demo_assumption_candidate`
- actual material chosen, purity, price: `business_input_required`
- dose conversion basis for the chosen product: `customer_validation_required`

**Water replacement / discharge-cost input requirements**

The MVP should keep water economics extremely simple at first:

| Formula candidate | Required inputs | What must remain scenario input | Classification |
|---|---|---|---|
| `daily_water_cost = replacement_m3_day × water_price_per_m3` | replacement volume, water price | local water tariff basis, metering basis | `business_input_required` |
| `daily_water_and_effluent_cost = (replacement_m3_day × supply_tariff) + (discharge_m3_day × effluent_tariff)` | above plus discharge volume and effluent price | whether effluent billing applies at all | `customer_validation_required` |

Texas A&M notes that poor source water can make an aquaponic operation unprofitable; that supports keeping source-water quality and cost explicit rather than hidden in generic overhead. citeturn29view0

**Solids / filter-maintenance labour-cost input requirements**

High-confidence recurring task evidence exists for solids handling:
- UVI commercial aquaponics design notes: **solids removal three times daily from clarifier** and **filter tank cleaning one or two times weekly**. citeturn31search0turn31search4
- NMSU advises cleaning filter tanks **twice a week** and removing organic deposits from the hydroponic section when anaerobic conditions contribute to rising/stable pH. citeturn29view1

That supports a **task library**, not a fixed labour-rate rule:

| Task category | Evidence basis | Frequency evidence | Labour driver basis | Classification |
|---|---|---|---|---|
| Clarifier sludge purge | UVI commercial aquaponics | 3× daily in that design | time per event × events/day | `scenario_input_required` |
| Filter tank cleaning / backwash | UVI, NMSU | 1–2× weekly in those designs | time per event × events/week | `scenario_input_required` |
| Hydroponic-section solids removal | NMSU | triggered by deposits / anaerobic risk | event-based | `customer_validation_required` |
| Sludge handling / disposal | implied by solids removal | system-specific | time per event + disposal charge | `customer_validation_required` |
| Pump / diffuser inspection relevant to solids fouling | indirect | management-specific | scheduled inspection hours | `customer_validation_required` |

**Recommended labour-cost formula**
- `task_cost_per_period = task_hours_per_event × events_per_period × burdened_labour_rate`
- `total_maintenance_labour_cost = Σ(task_cost_per_period)`

This is the strongest structure because the source evidence supports **recurring tasks**, but not universal labour burdens.

## What the MVP can calculate now and what remains blocked

**What can be calculated now from Mode A + P1 + P1.5 inputs, once business inputs are added**

The MVP can safely calculate:
- daily feed cost,
- daily electricity cost for pumps / blowers / aeration,
- daily alkalinity-buffer cost,
- daily water-replacement cost,
- daily or periodic filter-maintenance labour estimate,
- low/base/high operating-cost sensitivity ranges,
- cost-pressure overlays against biological load outputs.

These all remain legitimate **operating-cost pressure** outputs, not profitability outputs. Feed dominates cost in many tilapia systems, so sensitivity reporting is meaningful even before revenue exists. citeturn37search4turn36search4

**What remains scenario input**

- feed price,
- electricity tariff,
- measured or nameplate device power,
- runtime / duty cycle,
- chosen alkalinity material,
- material purity / neutralising value,
- water tariff,
- replacement volume,
- task durations,
- burdened labour rate,
- disposal fees,
- backup-fuel basis.

**What remains customer / advisor validation input**

- actual commercial feed procurement price,
- actual tariff class and whether fixed/demand charges apply,
- actual measured kW for major devices,
- whether backup systems are included in operating cost,
- chosen buffer chemistry and conversion basis,
- realistic task times and labour burden in the target operation.

**Business-input-only findings**

- Publicly visible feed prices are too heterogeneous by product class to be canonical. citeturn25search10turn23search0turn26view1
- Electricity pricing must carry geography, tariff class, and date, especially in India and for large Dutch/EU users. citeturn8view2turn6view1turn9search1
- FCR is useful for business/scenario interpretation, but not required for first-pass Mode A feed cost. citeturn1view1turn34view0

**Do-not-use-yet findings**

- Do not hard-code UF/IFAS budget feed or power prices as live defaults. They are useful as historical planning assumptions only. citeturn1view1
- Do not hard-code India power pricing as a national commercial default from the limited state-level evidence retrieved here. citeturn12search1turn5news38
- Do not treat UK/EU aquaculture pellet seller prices as Netherlands tilapia-farm procurement prices. citeturn26view1

**Claims to avoid**

- profitability,
- gross margin,
- payback,
- basil revenue,
- fish revenue,
- “economically viable” claims,
- “system is safe” claims,
- any claim that current public seller prices are canon.

## Direct decision support and next repo-side use

**Recommended next repo-side use**

1. Add a **business input schema** for feed-price records, tariff records, buffer-material records, water-price records, and maintenance-task records.  
2. Keep all numeric prices outside canon-style biological defaults.  
3. Expose a first MVP output tier called **operating cost pressure**, not profitability.  
4. Add low/base/high scenario support for feed and power first, because they are the most decision-useful and most easily parameterised.  
5. Add task-based maintenance costing after feed/power, using the UVI/NMSU maintenance pattern as the structural model. citeturn31search0turn29view1

**Top implementation-safe classifications**

- **`demo_assumption_candidate`**
  - EU benchmark electricity context from Eurostat.
  - Dutch non-household electricity examples from CBS.
  - seller-side India or EU/UK feed-price examples when clearly labeled as examples, not canon. citeturn8view2turn6view1turn25search10turn26view1

- **`scenario_input_required`**
  - `feed_price_per_kg`
  - `device_kw` / `runtime_h_day`
  - `electricity_price_per_kwh`
  - `buffer_material_choice`
  - `replacement_m3_day`
  - task frequencies if not copied from a specific known system
  - FCR when used for biomass-linked scenario interpretation.

- **`business_input_required`**
  - all current price/tariff values actually used in a report,
  - water and discharge prices,
  - labour rate,
  - disposal fees,
  - packaging of backup-power costs.

- **`customer_validation_required`**
  - actual feed contract pricing,
  - actual demand-charge exposure,
  - actual measured power draw,
  - actual maintenance times,
  - actual buffer-material conversion basis.

- **`do_not_use_yet`**
  - any universal default feed price,
  - any universal electricity tariff,
  - any universal labour rate,
  - any profitability output before revenue exists.

**Open questions and limitations**

- This pass found strong institutional structure for costs, but **weak public tilapia-feed price transparency in the Netherlands/EU**.
- India power examples were retrievable, but the cleanest official state tariff tables were not consistently machine-readable in this pass.
- Water and discharge cost evidence was sufficient to define input requirements, but not to justify reusable numeric defaults across jurisdictions.
- A later pass could improve quality by collecting **actual supplier quotations, invoices, or customer-provided tariffs** for the target launch geographies.

**Direct answers**

1. **Minimum input set for daily feed cost:** `feed_kg_day` + `feed_price_per_kg`.  
2. **Feed-price metadata that should be required:** currency, date captured, geography, supplier type, package size, feed class, crude protein %, quoted unit basis, and source reference. citeturn25search10turn26view1turn1view1  
3. **Can the MVP show feed-cost sensitivity before profitability?** Yes. It is one of the safest economics outputs to add early, provided it is labelled as operating-cost pressure and uses explicit low/base/high input cases. citeturn37search4turn36search4  
4. **Minimum input set for pump / aeration electricity cost:** per-device kW, runtime hours/day, and electricity tariff. Measured kW is preferred over nameplate-only values. citeturn35search0turn35search2  
5. **Minimum input set for alkalinity / buffer cost:** alkalinity demand on a CaCO3-equivalent basis, chosen material, effective neutralising value / CaCO3-equivalent basis, and material price. citeturn29view1turn29view2turn30search6  
6. **Minimum input set for water replacement cost:** replacement volume and water tariff; add discharge volume and effluent tariff only if billed.  
7. **Minimum input set for filter-maintenance labour cost:** task library, task frequency, hours per event, and burdened labour rate. UVI-style clarifier and filter-cleaning frequencies are good structural anchors. citeturn31search0turn31search4  
8. **Operating-cost values that can be demo assumptions without becoming canon:** Dutch/EU electricity reference values, clearly labeled historical US extension budget values, and example seller-side feed-price bands where source metadata is preserved. citeturn8view2turn6view1turn1view1turn25search10turn26view1  
9. **Operating-cost values that must remain user-supplied scenario inputs:** actual feed price, actual tariff, measured power draw, actual runtime, actual labour rate, actual water tariff, actual buffer material and price.  
10. **What must remain blocked until fish / crop revenue inputs exist:** profit, gross margin, break-even, ROI, payback, fish-side revenue, basil-side revenue, and viability claims.  
11. **What Codex should design next:** a business-input schema and report layer for operating-cost pressure, starting with feed and electricity, then alkalinity and task-based maintenance, while preserving the current block on revenue-and-profit outputs.