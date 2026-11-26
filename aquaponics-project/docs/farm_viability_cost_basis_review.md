# Farm Viability Cost Basis Review

Status: `draft`, scenario estimate, not validated.

Inputs file: `data/scenarios/farm_viability_inputs_v0.json` (non-canonical).

## Purpose

- Record the inputs Ajit's real-farm go/no-go needs, with origin labels.
- Review the two constructed calculator inputs in
  `scripts/example_first_slice_working_inputs.json`
  (`variable_cost_per_saleable_kg` 5.0 / 5.8 / 6.8 and `fixed_batch_cost` 500)
  and look for sourced replacements.
- This pass does not run the go/no-go and does not change the example inputs file.

## Sources read in this pass

| Source | What it gives | Limits |
|---|---|---|
| Heidemann and Bailey 2015, *Economic Analysis of the UVI Commercial Aquaponics System* (SARE case study #3, draft) | Whole-system labour 3,120 h/yr (2 people x 30 h/week), electricity 23,360 kWh/yr, basil 3,000 kg/yr, Table 7 depreciation (sum USD 3,420/yr), rent USD 300/yr | USD 2014, St. Croix; no split of labour or power between fish, lettuce and basil; basil not costed; materials-only owner build |
| Rakocy et al., *Aquaponic Production of Tilapia and Basil: Batch vs Staggered* (UVI, 2002 trials) | 214 m2 grow area; staggered basil projection 5,008 kg/yr (23.4 kg/m2) | Projection from trials; no cost or labour data |
| CBS StatLine 85666ENG | Non-household gas, smallest band (28,433 to 284,333 m3/yr), incl. VAT and tax: EUR 1.43 to 1.45/m3 in 2024, 1.34 to 1.39 in 2025, 1.355 in 2026 H1 (provisional) | Heat demand for a Dutch basil farm is still unknown |

## Finding 1: the constructed variable cost is probably too low if labour is hired

Charging all UVI whole-system labour and electricity to basil kg, at the research
pack's Dutch rates (labour EUR 16 to 19/h, electricity EUR 0.24 to 0.26/kWh):

| Basil output basis | Labour EUR/kg | Electricity EUR/kg | Labour + electricity EUR/kg |
|---|---:|---:|---:|
| 5,008 kg/yr (UVI trial projection) | 9.97 to 11.84 | 1.12 to 1.21 | 11.09 to 13.05 |
| 3,000 kg/yr (UVI economic study) | 16.64 to 19.76 | 1.87 to 2.02 | 18.51 to 21.78 |

Benchmark price is EUR 7 to 9/kg.

How to read this:

- It overstates basil's share, because the same hours and power also produce fish
  and lettuce. The source gives no split, so none is applied.
- It understates Dutch costs, because it has no heating, no grow lights, and no
  feed, seed, fingerlings, chemicals or packaging.
- Even so, hired labour at UVI intensity alone exceeds the price band. The
  constructed EUR 5.0 to 6.8/kg is not supported once labour is paid at Dutch rates.
- If Ajit's own hours are not costed, the labour line drops to zero and the
  picture changes completely. Owner hours and whether they count is the most
  decisive input.

## Finding 2: no sourced replacement yet for the EUR 500 batch fixed cost

- The only sourced fixed costs (UVI depreciation and rent) are USD 2014 for an
  owner-built tropical system with a USD 2,000 greenhouse. They do not transfer to
  a Dutch build, and no exchange rate is sourced in the repo.
- Recommendation: replace `fixed_batch_cost` with an annual fixed cost built from
  Ajit's own setup budget, building type and depreciation life, once he gives them.
  Until then the field stays null and break-even stays unreported.

## Finding 3: India side by side (added 2026-11-25 at Ajit's request)

Values from the research pack, in INR. Confidence is mostly low; see the inputs file
for tier, confidence and reason per value.

| Input | Netherlands | India |
|---|---|---|
| Basil price per kg | EUR 7 to 9 (medium: old wholesale examples) | INR 600 to 1,000 (low: one hydroponic study price plus haircuts) |
| Hired labour | EUR 16 to 19 per hour (medium) | INR 536 to 703 per day (medium: minimum wage plus burden proxy) |
| Electricity | EUR 0.24 to 0.26 per kWh (high) | INR 7.5 to 9.5 per kWh (low: one Tamil Nadu tariff plus spread, demand charge excluded) |
| Heating | gas EUR 1.34 to 1.45 per m3 (high), demand unknown | no source; cooling may matter more |
| Saleability | 0.85 to 0.95 (low) | 0.80 to 0.92 (low) |

Per-kg cost bounds for India:

| Line | Basis | INR per harvested kg | Compared with price |
|---|---|---:|---|
| Labour | Andhra study's own 288 labour days for 238 kg, re-priced at INR 536 to 703 per day | 649 to 851 | about equal to the INR 600 to 1,000 price band |
| Labour | Same study at its own INR 250 per day (below minimum wage) | 303 | |
| Electricity | UVI 23,360 kWh at INR 7.5 to 9.5, over 3,000 to 5,008 kg | 35 to 74 | small |

How to read this:

- India's electricity per kg is small. Labour per kg depends almost entirely on
  yield per labour day.
- The Andhra study's yield (about 0.95 kg per m2) is about 25 times below UVI's
  23.4 kg per m2 per year. If the study period was a single short cycle, its
  per-kg labour is far too high. The paper should be re-read before this is used.
- UVI hours cannot be priced in INR yet, because hours per paid day are not sourced.
- Euro equivalents are not used. The research pack has a comparison rate only.

## Finding 4: four Indian states (added 2026-11-25 at Ajit's request)

Inputs file: `data/scenarios/india_state_location_inputs_v0.json`. Wages are legal
minimum x 1.1525 burden proxy / 8 paid hours. Electricity is energy charge only.

| State | Wage INR/hour | Wage source (confidence) | Electricity INR/kWh | Tariff source (confidence) |
|---|---:|---|---:|---|
| Telangana | 77.6 to 102.5 | State G.O.Ms.No.6, from 1 Jun 2026, covers agriculture (medium) | 4.00 to 8.50 | TGSPDCL FY2025-26 schedule, expired Mar 2026 (medium) |
| Karnataka | 76.8 | Agriculture rate Rs 533/day, Apr 2025 to Mar 2026, secondary (low) | 3.45 to 7.10 | Aggregator plus news report of KERC review, conflicting (low) |
| Tamil Nadu | 70.0 to 91.8 | No state agri rate found; central-sphere proxy, Oct 2026 (low) | 4.95 to 10.45 | TNERC T.O. 6 of 2025 via secondary site (medium) |
| Andhra Pradesh | 70.0 to 91.8 | No state agri rate found; central-sphere proxy, Oct 2026 (low) | 3.85 to 4.50 | APERC FY2025-26, unverified extract; commercial rate not found (low) |

How to read this:

- The four states are close on wages (about INR 70 to 100 per hour). The labour gap
  between them is small next to the gap between hired and owner labour.
- Electricity varies about 2x within each state, depending on whether an aquaponic
  unit counts as agriculture, horticulture, aquaculture or commercial. That category
  question matters more than the choice of state.
- Andhra Pradesh has free power for horticultural nurseries and a Rs 1.50/unit
  aquaculture concession. Eligibility for an aquaponic farm is unknown.
- No state has its own basil price. Price is still the weakest Indian input.
- Conflict: 10 Bengaluru B2B listings for fresh Italian basil (IndiaMART, Nov 2026)
  ask INR 65 to 180 per kg (median about 110). That is 5 to 15 times below the
  INR 600 to 1,000 band. Confidence is low (asking prices, market level unstated),
  but if it holds, labour per kg (INR 300 to 850 on the Andhra basis) would exceed
  price. Recorded as a candidate, not swapped into the default band.

## Gaps still open

- Ajit's inputs: location, area, building, budget, electricity tariff, heating,
  sales channel and price, hours per week, owner labour costed or not.
- Dutch heat demand (m3 gas or kWh heat per m2 per year) for basil.
- Basil-specific labour hours per kg (harvest, handling). Neither UVI source has them.
- Feed, seed and other consumables at Dutch prices.
- A current Dutch basil wholesale price (the research pack's are March 2020).
- India: primary KERC and TNERC agriculture tariff orders, AP and TN state
  agriculture minimum wages, which tariff category an aquaponic farm gets, a first-wholesale basil price, hours per paid labour day,
  the Andhra study's crop period, and demand charges.

## What this does not claim

- No revenue, margin, profitability, viability or break-even claim.
- The per-kg figures are bounds from whole-system data, not basil cost facts.
- Nothing here is canon or a value for `saleable_harvest_mass_kg`.
