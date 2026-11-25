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

| Configuration | NL headroom EUR/m2/yr (low / mid / high) | India headroom INR/m2/yr (low / mid / high) |
|---|---|---|
| A. UVI-style DWC basil, hired, UVI labour intensity (0.62-0.93 h/kg) | -212 / -142 / -59 | 5,232 / 11,458 / 19,841 (about EUR 48 / 105 / 181) |
| B. Large raceway DWC basil, hired, Hawaii lettuce-farm labour per m2 (0.09-0.13 h/kg) | 26 / 84 / 153 | 6,334 / 12,583 / 20,942 |
| C. Basil farm at Purdue labour per kg (0.53-0.65 h/kg) | -128 / -82 / -13 | 5,617 / 11,884 / 20,326 |
| D. Large raceway DWC lettuce, Flemish auction price | -42 / -19 / 6 | gap: no India lettuce price |
| E. Owner-operated DWC basil, owner hours not costed | 65 / 119 / 185 | 6,513 / 12,733 / 21,063 |

Break-even labour intensity for basil wholesale:

- **Netherlands: 0.22 to 0.49 labour hours per harvested kg** (at EUR 16-19/h).
- **India: about 4.7 to 15 hours per kg** (at about INR 60-88/h). Labour is not the
  binding constraint there; price evidence and real yield are.

## Findings

1. **In the Netherlands, hired labour decides it.** Every sourced basil labour
   intensity (UVI 0.62-0.93 h/kg, Purdue 0.53-0.65 h/kg) is above the 0.22-0.49 h/kg
   break-even, before heating or CAPEX. Only configuration B clears, and it borrows a
   lettuce farm's labour per m2 for basil. Basil-specific harvest and handling hours
   per kg are the most important missing number.
2. **Scale and simple raceways cut labour per m2 about sevenfold** (UVI 14.6 h/m2/yr at
   214 m2 versus Hawaii 2.0 h/m2/yr at about 1,142 m2). Processing and packing was 44%
   of the Hawaii hours, so harvest and pack flow is the design target.
3. **Owner-operated in the Netherlands leaves EUR 65-185/m2/yr** for heating, CAPEX and
   owner pay. In the low case that is about EUR 4.5 per owner hour before heating and
   CAPEX; in the mid case about EUR 14.
4. **Wholesale lettuce in the Low Countries does not work** at auction prices
   (EUR 0.19-0.72 per head) even at Hawaii labour efficiency. Basil earns about four to
   seven times more revenue per m2.
5. **India clears labour and electricity in every case** (about EUR 48-191/m2/yr
   headroom), but the price band rests on one hydroponic study and the same study's
   yield is about 25 times below UVI's. India's open questions are price stage and
   achievable yield, not wages.

## Leading design candidates

- **Netherlands:** a larger (several hundred m2 or more) simple DWC raceway for basil,
  laid out for fast harvest and packing, either owner-operated or with labour under
  about 0.2-0.5 h/kg. Viable only if heating plus CAPEX fit inside the headroom.
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
| Real yield | Scales revenue | UVI canon 23.4 kg/m2/yr; simulator 15.7 kg/m2/yr nitrate-limited |

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
- State-level India inputs (Karnataka, Tamil Nadu, Andhra Pradesh, Telangana) from the
  Farm inputs thread, then re-run.
