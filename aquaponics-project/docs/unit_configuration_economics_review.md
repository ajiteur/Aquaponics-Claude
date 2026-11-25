# Unit Configuration Economics Review

Status: `draft`. Scenario estimate, not validated.

- Inputs: `data/scenarios/unit_configuration_candidates_v0.json` (non-canonical)
- Calculator: `scripts/compare_unit_configurations.py`
- Output: `data/simulation/results/unit_configuration_comparison.json`
- Candidate truths: `data/knowledge/atomic_facts/unit_economics_facts.json` (UE_0001 to UE_0011)

## Question

Which aquaponics unit design gets revenue per kg above cost per kg? Ajit asked for this
before the farm go/no-go, with the Netherlands and India compared side by side.

## What is compared

Each configuration is scored on **headroom per m2 per year**: revenue minus labour and
electricity. Headroom still has to pay for heating, CAPEX, consumables and, when owner
time isn't costed, the owner. None of those have sourced values yet, so headroom is an
upper bound on what a design can carry. It is not profit.

The **break-even labour intensity** is also reported: the labour hours per harvested kg
at which revenue just covers labour plus electricity. It is the clearest single target
for a design.

Cases: `low` takes the worst end of every range and `high` the best; `mid` takes the
midpoints.

## Results (scenario estimate, not validated)

Basil yield range for every basil design: 23.4 kg/m2/yr (UVI staggered, canon CROP_0004)
to 25.9 kg/m2/yr (simulated, fish feed sized to the UVI ratio, 1.99 kg/m2 x 13 crops).
Both are tropical-site yields. An under-fed unit yields far less, and Dutch winter light
and heat are not in the range.

| Configuration | NL headroom EUR/m2/yr (low / mid / high) | India headroom INR/m2/yr (low / mid / high) |
|---|---|---|
| A. UVI-style DWC basil, hired, UVI labour intensity (0.56-0.62 h/kg) | -166 / -105 / -38 | 8,913 / 14,946 / 22,113 (about EUR 81 / 137 / 202) |
| B. Large raceway DWC basil, hired, Hawaii lettuce-farm labour per m2 (0.08-0.09 h/kg) | 72 / 120 / 174 | 10,015 / 16,071 / 23,214 |
| C. Basil farm at Purdue labour per kg (0.53-0.65 h/kg) | -177 / -98 / -13 | 8,862 / 15,153 / 22,520 |
| D. Large raceway DWC lettuce, Flemish auction price | -42 / -19 / 6 | gap: no India lettuce price |
| E. Owner-operated DWC basil, owner hours not costed | 111 / 156 / 206 | 10,195 / 16,221 / 23,335 |

Break-even labour intensity for basil wholesale:

- **Netherlands: 0.25 to 0.50 labour hours per harvested kg** (at EUR 16-19/h). This
  metric barely depends on yield, so it is the most robust result here.
- **India: about 5 to 15 hours per kg** (at about INR 60-88/h). Labour is not the
  binding constraint there; price evidence and real yield are.

### India by state

Inputs from the Farm inputs thread (`india_state_location_inputs_v0.json`): state
minimum wages (Telangana and Karnataka state rates, Tamil Nadu and Andhra Pradesh via
the central-sphere proxy) and state electricity tariffs, with the all-India basil price
and saleability band in every state.

| State | Owner-run basil, INR/m2/yr (low / mid / high) | Hired, UVI labour, INR/m2/yr (low / mid / high) |
|---|---|---|
| Karnataka | 10,457 / 16,497 / 23,586 | 9,337 / 15,253 / 22,304 |
| Tamil Nadu | 10,091 / 16,290 / 23,494 | 8,753 / 14,929 / 22,239 |
| Andhra Pradesh | 10,741 / 16,592 / 23,562 | 9,403 / 15,314 / 22,359 |
| Telangana | 10,304 / 16,414 / 23,552 | 8,809 / 14,954 / 22,233 |

The states differ by only about 5 to 7% in the low case, because wages and power are
small next to revenue and every state shares one price band. **What decides India is the
basil price and a local yield, not which of these four states.** A state-specific basil
price would change this more than anything else.

### Karnataka price sensitivity (Bengaluru B2B listings)

The Farm inputs thread found ten Bengaluru B2B listings for fresh Italian basil
(IndiaMART, read 2026-11-25) asking INR 65-180/kg, median about 110. Three sellers are
hydroponic growers at INR 65-130. That is 5 to 15 times below the INR 600-1,000 band.
Grey literature, asking prices, market level not stated: confidence low. It is run as a
sensitivity case, not as the default.

| Design (Karnataka, listing prices) | INR/m2/yr (low / mid / high) | About EUR/m2/yr |
|---|---|---|
| A. UVI-style, hired, UVI labour | -679 / 899 / 2,787 | -6 / 8 / 25 |
| B. Large raceway, hired, lean labour | 285 / 1,987 / 3,913 | 3 / 18 / 36 |
| C. Purdue labour per kg | -723 / 1,030 / 3,019 | -7 / 9 / 28 |
| E. Owner-run | 441 / 2,144 / 4,070 | 4 / 20 / 37 |

At these prices headroom falls by about 85 to 95%, below the Netherlands' owner-run
case, and in the low case the owner earns about INR 30 per hour before CAPEX. The
break-even labour intensity drops to about 0.25-2.0 h/kg. **The India result depends
almost entirely on which price is right.** This is a context split (study sale price
versus B2B asking prices) to resolve with a real buyer quote, not an overwrite.

## Findings

1. **In the Netherlands, hired labour decides it.** Every sourced basil labour
   intensity (UVI 0.56-0.62 h/kg, Purdue 0.53-0.65 h/kg) is above the 0.25-0.50 h/kg
   break-even, before heating or CAPEX. Only configuration B clears, and it borrows a
   lettuce farm's labour per m2 for basil. Basil-specific harvest and handling hours
   per kg are the most important missing number.
2. **Scale and simple raceways cut labour per m2 about sevenfold** (UVI 14.6 h/m2/yr at
   214 m2 versus Hawaii 2.0 h/m2/yr at about 1,142 m2). Processing and packing was 44%
   of the Hawaii hours, so harvest and pack flow is the design target.
3. **Owner-operated in the Netherlands leaves EUR 111-206/m2/yr** for heating, CAPEX and
   owner pay. In the low case (UVI labour intensity) that is about EUR 7.6 per owner hour
   before heating and CAPEX; in the mid case about EUR 19.
4. **Wholesale lettuce in the Low Countries does not work** at auction prices
   (EUR 0.19-0.72 per head) even at Hawaii labour efficiency. Basil earns about 4 to 11
   times more revenue per m2.
5. **India clears labour and electricity in every case at the study-based price band** (about EUR 81-213/m2/yr
   headroom at the comparison rate), but the price band rests on one hydroponic study
   whose own yield is about 25 times below UVI's. At Bengaluru B2B listing prices
   (INR 65-180/kg) the headroom shrinks by 85-95% (see the Karnataka sensitivity). India's
   open questions are price stage and achievable yield, not wages.

## Leading design candidates

- **Netherlands:** a larger (several hundred m2 or more) simple DWC raceway for basil,
  laid out for fast harvest and packing, fish feed sized to the UVI ratio, either
  owner-operated or with labour under about 0.25-0.5 h/kg. Viable only if heating plus
  CAPEX fit inside the headroom.
- **India:** the same DWC basil unit, where heating is not the issue, once a
  first-wholesale price and a local yield are confirmed per state.

## Deciding assumptions

| Assumption | Why it decides | Evidence now |
|---|---|---|
| Basil labour h/kg | Sets NL result sign | Only whole-system or cross-crop values (T3, medium/low) |
| Owner hours costed or not | Removes the labour line | Ajit's choice (open in Farm inputs thread) |
| Basil wholesale price | Linear driver of revenue | NL: 2020 price lists (low); India: one study (low) |
| Heating demand in NL | Could eat the headroom | Only a sector average, 0.99 GJ/m2 (not crop-specific) |
| CAPEX per m2 | Must fit the headroom | USD references only (about USD 190-1,110/m2) |
| Real yield | Scales revenue per m2 | UVI canon 23.4 kg/m2/yr; simulator 25.9 kg/m2/yr at the UVI feed ratio; under-fed units far lower |

## Source reliability

Every value in the inputs file carries an origin, and every source carries a tier,
confidence, reason and cross-check. Main internal problems noticed:

- Quagrainie et al. (Purdue): several internal inconsistencies, so confidence is low.
- VBT weekly prices: text extraction was scrambled and the unit is not printed.
- Zappernick et al.: only the methods were read verbatim; its total labour hours are not used.
- Tokunaga et al.: a representative model farm, lettuce only; applying it to basil is a transfer.

## What this does not claim

No profit, margin, ROI, payback, viability or total operating cost. Heating, CAPEX,
consumables and fish revenue are left out on purpose and listed as gaps. Nothing here
is canon or a value for `saleable_harvest_mass_kg`.

## Next steps

- Source basil harvest and pack labour per kg (task timing studies or grower data).
- Dutch heating demand for unlit, low-temperature basil or lettuce glasshouse.
- A Dutch or EU build cost per m2 for a simple greenhouse with DWC.
- A state-level first-wholesale basil price for each Indian state.
