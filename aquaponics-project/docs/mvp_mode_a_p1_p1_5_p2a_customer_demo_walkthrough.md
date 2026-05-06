# MVP Four-Level Customer/Advisor Demo Walkthrough

## 1. Purpose

This walkthrough explains the current four-level Aquaponics MVP demo for
customers, operators, technical advisors, and seed-stage reviewers. It is a
communication artifact only. It does not add model logic, does not define a
product spec, and does not claim fish safety, system safety, profitability, or
revenue.

The walkthrough uses actual output from the current JSON demo runner and
example inputs.

## 2. Current seed-MVP goal

Build and validate an evidence-backed aquaponics planning engine that turns
explicit fish feed inputs into water-quality, aeration/solids, and selected
operating-cost-pressure insights for a tilapia + basil DWC/raft system.

The current MVP keeps basil saleable output unresolved unless saleable harvest
mass is observed or explicitly reviewed. The demo does not infer
`saleable_harvest_mass_kg` from plant biomass, plant count, daily gain, or any
fish/feed output.

## 3. Four-level demo overview

The four demo levels build progressively:

1. Mode A load-only report: direct feed and protein inputs produce TAN-N load,
   nitrification oxygen demand, and alkalinity demand.
2. P1 water-quality context report: complete water volume, time, pH, and
   temperature inputs add fish-tank TAN-N concentration and NH3 chemistry
   context.
3. P1.5 aeration/solids context report: measured DO and an explicit dry-solids
   coefficient add context labels for oxygen and solids without claiming
   adequacy or removal capacity.
4. P2a operating-cost pressure report: explicit feed price, equipment power,
   runtime, and electricity tariff inputs add selected feed and power cost
   pressure without claiming total operating cost or profitability.

## 4. Demo commands

Run the four commands in this order:

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_feed_load_inputs.json
```

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_water_quality_inputs.json
```

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p1_5_aeration_solids_inputs.json
```

```powershell
python scripts/build_mvp_mode_a_feed_load_report.py --input scripts/example_mvp_mode_a_p2a_operating_cost_inputs.json
```

## 5. Demo 1 explanation: Mode A load-only

Demo 1 reads explicit direct-feed inputs:

- `feed_kg_day = 1.0`
- `protein_fraction = 0.32`
- `input_mode = mode_a_direct_feed`
- `feed_class = grow_out`
- `architecture_context = tilapia_basil_dwc_raft`

It calculates load-only outputs:

- TAN-N load
- nitrification oxygen demand
- alkalinity demand

Plain-language explanation:

`For one kilogram of feed per day at 32 percent protein, the prototype can
estimate the nitrogen load and the support demand for nitrification. It does
not yet know the tank concentration, NH3 chemistry, aeration adequacy, feed
cost, or basil saleable output. Those need additional inputs.`

## 6. Demo 2 explanation: P1 water-quality context

Demo 2 adds complete P1 inputs:

- `effective_water_volume_l = 7800`
- `accumulation_period_day = 1`
- `concentration_scope = fish_tank`
- `ph = 7.0`
- `water_temp_c = 28.0`
- `freshwater_assumption = true`

It keeps the original load outputs and adds:

- estimated fish-tank TAN-N concentration
- unionized NH3 fraction
- estimated NH3-N concentration
- estimated NH3 concentration

Plain-language explanation:

`With explicit fish-tank water volume, time basis, pH, and temperature, the
prototype can add a fish-tank upper-bound/no-removal concentration estimate and
NH3 chemistry context. This is not a safety verdict. It does not compare the
result to a threshold, model post-feeding peaks, or prove fish safety.`

## 7. Demo 3 explanation: P1.5 aeration/solids context

Demo 3 keeps the Mode A and P1 values, then adds P1.5 context:

- `include_aeration_solids_context = true`
- `measured_do_mg_l = 5.0`
- `dry_solids_coefficient = 0.25`
- `dry_solids_basis = demo_scenario_input_not_canon`

It adds:

- nitrification oxygen demand echoed as a known sub-load
- measured DO echoed as a point/context measurement
- provisional feed-linked dry-solids potential
- missing-context labels for aeration capacity, oxygen transfer, fish
  respiration oxygen demand, total oxygen demand, DWC/root-zone aeration,
  solids-removal capacity, clarifier retention, and backup aeration/power
  continuity

Plain-language explanation:

`This level separates useful context from overclaiming. It can show the
nitrification oxygen sub-load, echo measured DO, and estimate provisional
dry-solids potential from an explicit coefficient. It does not calculate total
oxygen demand, aeration capacity, wet sludge, TSS, or solids-removal capacity.`

## 8. Demo 4 explanation: P2a operating-cost pressure

Demo 4 keeps Mode A, P1, and P1.5 context, then adds explicit P2a scenario
business inputs:

- `feed_price_per_kg = 45.0`
- `feed_price_currency = INR`
- `feed_price_date = 2026-05-06`
- `feed_price_geography = India scenario`
- `feed_price_source_type = demo_scenario_input`
- `electricity_price_per_kwh = 7.5`
- `electricity_price_currency = INR`
- `electricity_tariff_date = 2026-05-06`
- `electricity_price_geography = India scenario`
- pump: `0.2 kW`, `24 h/day`, `load_fraction = 1.0`,
  `power_basis = nameplate_kw`
- blower: `0.1 kW`, `24 h/day`, `load_fraction = 1.0`,
  `power_basis = nameplate_kw`

It adds:

- scenario feed cost per day
- equipment kWh/day
- scenario power cost per day
- selected operating-cost pressure subtotal
- nameplate-power uncertainty label
- labels that the result is a scenario estimate, not canon, not market truth,
  not total operating cost, and not profitability

Plain-language explanation:

`With explicit price and tariff inputs, the prototype can show a selected
cost-pressure subtotal for supplied categories. It is intentionally named
selected operating-cost pressure, not total operating cost. It does not include
buffer, water, labor, backup power, revenue, margin, or profitability.`

## 9. What changes across the four demo levels

Demo 1 to Demo 2:

- Adds water volume, time basis, pH, temperature, and freshwater assumption.
- Converts load context into a fish-tank upper-bound/no-removal TAN-N
  concentration estimate.
- Adds NH3 chemistry context.
- Suppresses the missing TAN concentration and missing NH3 context labels.

Demo 2 to Demo 3:

- Adds measured DO as context.
- Adds provisional dry-solids potential from explicit feed and coefficient.
- Keeps aeration and solids labels as warning/context labels.
- Does not turn measured DO into fish safety or aeration adequacy.

Demo 3 to Demo 4:

- Adds explicit scenario feed price, electricity tariff, equipment kW, runtime,
  and load fraction.
- Calculates selected feed and power cost pressure.
- Keeps cost outputs separate from revenue, profitability, and total operating
  cost.

## 10. Actual output values

Values from the current demo commands:

| Output | Demo level | Actual value |
| --- | --- | --- |
| TAN-N load | Demo 1+ | `0.02944 kg/day` |
| TAN-N load | Demo 1+ | `29.44 g/day` |
| Nitrification oxygen demand | Demo 1+ | `134.5408 g/day` |
| Alkalinity demand | Demo 1+ | `210.2016 g CaCO3/day` |
| Estimated TAN-N concentration | Demo 2+ | `3.7743589743589743 mg TAN-N/L` |
| Estimated unionized NH3 fraction | Demo 2+ | `0.006971085009084945` |
| Estimated NH3-N concentration | Demo 2+ | `0.026311377265059072 mg NH3-N/L` |
| Estimated NH3 concentration | Demo 2+ | `0.031949529536143155 mg NH3/L` |
| Measured DO context | Demo 3+ | `5.0 mg/L` |
| Provisional dry-solids potential | Demo 3+ | `0.25 kg/day` |
| Scenario feed cost per day | Demo 4 | `45.0 INR/day` |
| Pump power use | Demo 4 | `4.8 kWh/day` |
| Blower power use | Demo 4 | `2.4 kWh/day` |
| Scenario power use | Demo 4 | `7.2 kWh/day` |
| Scenario power cost per day | Demo 4 | `54.0 INR/day` |
| Selected operating-cost pressure subtotal | Demo 4 | `99.0 INR/day` |

The P2a power calculation uses nameplate kW in the example, so the output
includes `power_cost_uses_nameplate_kw_not_measured_kw`.

## 11. Calculated versus context-only versus scenario-input versus blocked

Calculated outputs:

- TAN-N load
- nitrification oxygen demand
- alkalinity demand
- estimated fish-tank TAN-N concentration when complete P1 inputs exist
- estimated NH3 fraction, NH3-N, and NH3 when complete P1 inputs exist
- provisional dry-solids potential when feed and coefficient are supplied
- scenario feed cost per day when explicit feed price inputs exist
- scenario power kWh/day and power cost per day when explicit equipment and
  tariff inputs exist
- selected operating-cost pressure subtotal when supplied money outputs share
  one currency

Context-only values:

- feed class
- architecture context
- concentration scope
- measured DO
- dry-solids basis
- equipment role and power basis
- scenario price metadata

Scenario/business inputs:

- daily feed amount
- feed protein fraction
- fish-tank water volume and accumulation period
- pH and water temperature
- measured DO
- dry-solids coefficient
- feed price, currency, date, geography, and source type
- electricity tariff, currency, date, geography, tariff class, and source type
- pump/blower kW, runtime, load fraction, and power basis

Blocked claims:

- fish safety
- system safety
- aeration adequacy
- oxygen-transfer capacity
- total oxygen demand
- solids-removal capacity
- wet sludge or TSS
- total operating cost
- revenue
- profitability
- basil saleable harvest mass

## 12. Claims to avoid

Do not say or imply:

- the demo proves fish safety
- the demo proves system safety
- the demo proves aeration adequacy
- measured DO proves future safety
- nitrification oxygen demand is total oxygen demand
- oxygen demand is aeration capacity
- dry-solids potential is wet sludge
- dry-solids potential is TSS
- dry-solids potential is solids-removal capacity
- selected operating-cost pressure is total operating cost
- feed or electricity prices are canon
- the demo calculates profitability
- the demo calculates revenue
- the demo calculates margin
- the demo calculates ROI
- the demo calculates payback
- the demo calculates break-even
- the demo proves economic viability
- basil saleable harvest mass is known

## 13. 10-minute operator/advisor script

Minute 0 to 1: Frame the goal.

`This is a planning-engine demo for a tilapia + basil DWC/raft system. The
point is not to claim safety or profit. The point is to show how explicit
operator inputs can turn feed into transparent load, water-quality context,
aeration/solids context, and selected cost pressure.`

Minute 1 to 3: Run Demo 1.

Show direct feed and protein inputs. Explain TAN-N load, nitrification oxygen
demand, and alkalinity demand. Point out the missing-context labels as a
strength: the system refuses to infer concentration, NH3 chemistry, cost,
tank suitability, or basil saleability without the needed inputs.

Minute 3 to 5: Run Demo 2.

Show water volume, time basis, pH, and temperature. Explain fish-tank
upper-bound/no-removal TAN-N concentration and NH3 chemistry context. State
clearly that this is not a safe/unsafe threshold check.

Minute 5 to 7: Run Demo 3.

Show measured DO and dry-solids coefficient. Explain that measured DO is a
point/context value and that dry-solids potential is not wet sludge, TSS, or
filter capacity.

Minute 7 to 9: Run Demo 4.

Show feed price, pump/blower records, and electricity tariff. Explain scenario
feed cost, power kWh/day, power cost/day, and selected cost-pressure subtotal.
State that it is not total operating cost or profitability.

Minute 9 to 10: Ask for feedback.

Ask which inputs are easy to provide, which warnings are useful, and which next
layer would make the demo more credible: deeper NH3 interpretation,
oxygen/aeration details, solids/filter details, or operating-cost extensions.

## 14. 15-minute investor/advisor script

Minute 0 to 2: Thesis.

`The MVP turns a concrete operating input, daily fish feed, into a transparent
chain of engineering and business-risk context. It is deliberately conservative:
it shows what can be calculated, labels what is missing, and blocks claims that
would require unsupported assumptions.`

Minute 2 to 4: Baseline load engine.

Run Demo 1. Emphasize that the first useful vertical slice is direct feed to
TAN-N, oxygen demand, and alkalinity demand.

Minute 4 to 7: Water-quality layer.

Run Demo 2. Explain that the P1 layer separates load from concentration and
NH3 chemistry. Highlight that fish-tank exposure is not the same as a
whole-system average and that no safety threshold is applied yet.

Minute 7 to 10: Aeration and solids context.

Run Demo 3. Explain that the P1.5 layer prevents a common fake-precision error:
nitrification oxygen demand is not total oxygen demand, and dry-solids
potential is not filter performance.

Minute 10 to 13: Operating-cost pressure.

Run Demo 4. Explain selected feed and electricity cost pressure. Highlight that
prices are scenario inputs with metadata, and that the subtotal is explicitly
not total operating cost or profitability.

Minute 13 to 15: Decision ask.

Ask whether the current chain is credible enough for customer/advisor
validation, which missing inputs should be prioritized, and whether P2c
buffer/water/maintenance extensions should wait until operators confirm that
the selected cost-pressure view is valuable.

## 15. Discovery questions

Operator questions:

- Can operators provide daily feed in kg/day?
- Can they provide feed protein percentage from the feed label?
- Can they provide fish-tank volume?
- Can they provide pH and water temperature?
- Can they provide measured DO?
- Can they provide pump/blower kW and runtime?
- Can they provide feed price and electricity tariff with date and location?
- Can they provide solids-filter details?
- Which warning labels are useful or confusing?

Technical advisor questions:

- Is fish-tank upper-bound/no-removal TAN-N concentration a useful first
  concentration scope?
- What threshold basis should be used later, if any: TAN-N, NH3-N, or NH3?
- Which DO and oxygen-transfer inputs are realistic for operators to supply?
- What evidence would be needed before estimating total oxygen demand?
- What evidence would be needed before translating dry-solids potential into
  wet sludge, TSS, or solids-removal capacity?

Investor/advisor questions:

- Which output feels most useful: NH3 context, oxygen/solids context, or
  selected operating-cost pressure?
- Does the warning-label approach increase credibility or make the demo feel
  incomplete?
- Which next layer most improves seed-MVP clarity?
- Should P2c buffer/water/maintenance cost-pressure extensions wait until
  customer feedback confirms value?
- What claims should the team avoid in pitch/demo language?

## 16. Feedback-capture rubric

Must-have for credibility:

- Operators can recognize the inputs.
- Advisors accept the load/concentration/context separation.
- Cost-pressure outputs are understood as selected scenario costs, not total
  operating cost.
- The unresolved basil saleable output boundary is clear.

Confusing or unclear:

- TAN-N versus NH3-N versus NH3.
- fish-tank exposure versus whole-system average.
- measured DO versus aeration adequacy.
- nitrification oxygen demand versus total oxygen demand.
- dry-solids potential versus wet sludge/TSS/filter removal.
- selected cost pressure versus profitability.

Useful next input:

- pH and water temperature capture.
- measured DO capture.
- equipment kW and runtime capture.
- feed price and electricity tariff metadata.
- solids-filter type and maintenance data.

Not valuable:

- outputs that operators cannot act on.
- labels that feel too technical without improving trust.
- cost categories that customers cannot estimate reliably.

Claims to avoid:

- any safety, adequacy, revenue, profitability, or viability claim not backed by
  explicit inputs and later design.

Customer-supplied inputs available now:

- daily feed
- feed protein
- rough tank volume
- pH and temperature
- current feed price
- local electricity tariff

Customer-supplied inputs hard to provide:

- measured kW versus nameplate kW
- oxygen-transfer assumptions
- total oxygen demand
- solids-removal capacity
- reliable labor and maintenance time
- observed/reviewed basil saleable harvest mass

## 17. Recommended next action

Run a small customer/advisor validation batch using the four-level demo. Capture
which outputs are credible, which labels are confusing, and which inputs
operators can actually provide.

Defer P2c buffer/water/maintenance extensions until feedback confirms that the
selected operating-cost-pressure view is valuable.

Do not add fish revenue, basil revenue, total operating cost, margin, ROI,
payback, break-even, profitability, or economic viability until explicit revenue
inputs and complete-enough cost inputs exist.
