# MVP Current Progress Map Update Spec

## 1. Purpose

Create a text-only visual update spec for the current Aquaponics MVP progress
map. This pass prepares copy and layout guidance for a later designer or
image-generation step. It does not generate an image, modify code, modify
runtime output, or change any canonical knowledge files.

Status reconciliation: the prompt text describes P2a operating-cost pressure
report integration as the current next build, but current repo inspection shows
that P2a report/demo integration now exists in the report path and scripts.
This spec therefore treats P2a report/demo integration as completed and makes
the next visual focus the updated customer/advisor walkthrough with four demos.

## 2. Old visual state

The old visual was titled:

`Seed-MVP Progress: Tilapia + Basil DWC/Raft Aquaponics Planner`

It used three zones:

- Zone 1: Completed / Built and Tested
- Zone 2: Next Build / Current Focus
- Zone 3: Future / Planned Roadmap

Old Zone 1 showed early completed items:

1. Evidence-backed knowledge base
2. Basil saleability honesty layer
3. Mode A feed input
4. TAN-N load calculator
5. O2 demand calculator
6. Alkalinity demand calculator
7. Report builder
8. JSON demo runner

Old Zone 2 focused on:

- P1 TAN concentration + NH3 chemistry helper

Old Zone 3 included:

- P1 report integration
- P1.5 aeration + solids layer
- total oxygen-demand envelope
- aeration capacity context
- DWC/root-zone aeration context
- solids-load potential
- feed-cost scenario economics
- Mode B biomass-derived feeding
- customer/advisor validation
- seed-demo dashboard

Old guardrails included:

- no fake basil saleable output
- no TAN concentration without volume + time
- no NH3 risk without pH + temperature
- O2 demand is not aeration capacity
- nitrification demand is not biofilter removal
- feed cost is scenario input, not canon

## 3. Current actual MVP state

Current repo truth supports a four-level demo path:

1. Level 1: Mode A load-only report
2. Level 2: P1 fish-tank TAN-N concentration and NH3 chemistry context
3. Level 3: P1.5 aeration and solids context
4. Level 4: P2a selected operating-cost pressure context

Completed current assets include:

1. Evidence-backed knowledge base
2. Basil saleability honesty/null layer
3. Mode A direct feed input
4. TAN-N load calculator
5. Nitrification oxygen-demand calculator
6. Alkalinity-demand calculator
7. Mode A report builder
8. JSON demo runner
9. P1 TAN concentration + NH3 chemistry helper
10. P1 report/demo integration
11. P1.5 aeration/solids context helper
12. P1.5 report/demo integration
13. Three-level customer/advisor walkthrough
14. Operating-cost pressure design
15. P2a feed + electricity operating-cost pressure helper
16. P2a report/demo integration

The current next build is:

- Updated customer/advisor walkthrough with four demos: load-only, P1, P1.5,
  and P2a selected operating-cost pressure.

## 4. Updated Zone 1 completed

Zone 1 should be retitled:

`Completed / Built and Tested`

Use compact completed cards or a left-side vertical chain:

1. Evidence-backed knowledge base
2. Basil saleability honesty/null layer
3. Mode A direct feed input
4. TAN-N load calculator
5. Nitrification O2-demand calculator
6. Alkalinity-demand calculator
7. Mode A report builder
8. JSON demo runner
9. P1 TAN concentration + NH3 chemistry helper
10. P1 report/demo integration
11. P1.5 aeration/solids context helper
12. P1.5 report/demo integration
13. Three-level customer/advisor walkthrough
14. Operating-cost pressure design
15. P2a feed + electricity cost-pressure helper
16. P2a report/demo integration

Recommended visual treatment:

- Use completed styling for all items above.
- Show the completed chain as evidence-to-demo progression, not a product
  launch claim.
- Keep "built and tested" scoped to helper/report/demo tests, not field
  validation.

## 5. Updated Zone 2 current build

Zone 2 should be retitled:

`Current Focus / Next Build`

Current visual focus:

- Updated customer/advisor walkthrough with four demos

The center highlight should show:

- Demo 1: Mode A load-only
- Demo 2: P1 water-quality context
- Demo 3: P1.5 aeration/solids context
- Demo 4: P2a selected operating-cost pressure

Include a small note:

`P2a report integration is now built; next step is explaining it cleanly to
operators, technical advisors, and seed-MVP reviewers.`

If a designer is updating from an older snapshot that still shows P2a report
integration as pending, move that item into Zone 1 completed and replace Zone 2
with the four-demo walkthrough update.

## 6. Updated Zone 3 future roadmap

Zone 3 should be retitled:

`Future / Planned Roadmap`

Use right-side roadmap boxes:

1. Customer/advisor validation
2. P2c buffer/water/maintenance cost-pressure extensions
3. Mode B biomass-derived feeding
4. Seed-demo dashboard
5. Fish revenue only with explicit fish harvest and sale-price inputs
6. Basil revenue only after observed/reviewed saleable harvest mass
7. Profitability only after explicit revenue and complete-enough cost inputs

Optional lower-priority future labels:

- total oxygen-demand envelope, only after fish respiration and other oxygen
  loads are designed
- aeration capacity comparison, only after explicit equipment and transfer
  assumptions
- solids-removal capacity, only after filter design inputs

## 7. Updated outputs

Show these as current output labels:

- TAN-N load
- nitrification oxygen demand
- alkalinity demand
- estimated fish-tank TAN-N concentration
- NH3 chemistry context
- measured DO context
- provisional dry-solids potential
- scenario feed cost
- scenario power cost
- selected operating-cost pressure subtotal

Use the wording `context` or `pressure` for outputs that are not safety,
capacity, revenue, or profitability claims.

## 8. Updated guardrails

Use a bottom guardrail row with short text chips:

- No fake basil saleable output
- No TAN concentration without volume + time
- No NH3 chemistry without pH + temperature
- O2 demand is not aeration capacity
- Nitrification demand is not total oxygen demand
- Nitrification demand is not biofilter removal
- Dry-solids potential is not wet sludge, TSS, or solids-removal capacity
- Feed/electricity prices are scenario inputs, not canon
- Selected cost pressure is not total operating cost
- Cost pressure is not profitability
- No fish revenue, basil revenue, ROI, payback, gross margin, break-even, or
  viability claims

## 9. Suggested visual layout

Top title:

`Seed-MVP Progress: Tilapia + Basil DWC/Raft Aquaponics Planner`

Subtitle:

`Fish feed to water-quality, aeration/solids context, and selected operating-cost pressure. Basil saleable output remains unresolved unless observed or explicitly reviewed.`

Three-zone structure:

- Left: Zone 1 completed chain, dense but readable.
- Center: Zone 2 current focus, visually highlighted.
- Right: Zone 3 future roadmap, grouped by validation, cost extensions,
  feeding model, dashboard, revenue, and profitability.

Bottom physical-system flow:

`Feed input -> TAN-N load -> O2 + alkalinity demand -> TAN-N concentration + NH3 chemistry -> aeration/solids context -> selected operating-cost pressure`

Guardrail row:

- Use compact chips at the bottom.
- Make the guardrail row visually distinct from calculated outputs.

Legend:

- Built/tested: completed helper/report/demo path
- Current focus: next communication or build step
- Context-only: not a safety, adequacy, or revenue claim
- Future: requires more inputs, evidence, or customer validation

## 10. Exact text snippets for image update

Title:

`Seed-MVP Progress: Tilapia + Basil DWC/Raft Aquaponics Planner`

Subtitle:

`Current prototype turns explicit fish feed inputs into load, water-quality context, aeration/solids context, and selected operating-cost pressure. Basil saleable output remains unresolved.`

Zone 1 header:

`Completed / Built and Tested`

Zone 1 card text:

`Knowledge base`

`Basil saleability null-status layer`

`Mode A direct feed input`

`TAN-N load`

`Nitrification O2 demand`

`Alkalinity demand`

`Mode A report builder`

`JSON demo runner`

`P1 TAN-N concentration + NH3 chemistry`

`P1 report/demo integration`

`P1.5 aeration/solids context`

`P1.5 report/demo integration`

`Three-level demo walkthrough`

`Operating-cost pressure design`

`P2a feed + electricity helper`

`P2a report/demo integration`

Zone 2 header:

`Current Focus / Next Build`

Zone 2 card text:

`Update customer/advisor walkthrough to four demos`

`Demo 1: load-only`

`Demo 2: TAN-N + NH3 chemistry context`

`Demo 3: aeration + solids context`

`Demo 4: selected feed + electricity cost pressure`

`Clarify: selected cost pressure is not total operating cost and not profitability`

Zone 3 header:

`Future / Planned Roadmap`

Zone 3 card text:

`Customer/advisor validation`

`P2c buffer/water/maintenance cost-pressure extensions`

`Mode B biomass-derived feeding`

`Seed-demo dashboard`

`Fish revenue only with explicit fish harvest + sale price`

`Basil revenue only after observed/reviewed saleable harvest mass`

`Profitability only after revenue + complete-enough cost inputs`

Bottom flow text:

`feed -> TAN-N load -> O2 + alkalinity demand -> TAN-N/NH3 context -> aeration/solids context -> selected cost pressure`

Guardrail text:

`No fake basil saleable output`

`No TAN concentration without volume + time`

`No NH3 chemistry without pH + temperature`

`O2 demand is not aeration capacity`

`Nitrification demand is not total O2 demand or biofilter removal`

`Dry-solids potential is not wet sludge, TSS, or removal capacity`

`Prices are scenario inputs, not canon`

`Selected cost pressure is not total operating cost`

`Cost pressure is not profitability`

`No revenue, ROI, payback, margin, break-even, or viability claims`

## 11. Claims to avoid

Do not imply:

- basil saleable harvest mass is known
- fish safety is proven
- system safety is proven
- aeration adequacy is proven
- oxygen-transfer capacity is known
- solids-removal capacity is known
- wet sludge or TSS are calculated
- feed or electricity prices are canon
- selected operating-cost pressure is total operating cost
- operating-cost pressure is profitability
- fish revenue, basil revenue, gross margin, ROI, payback, break-even, or
  economic viability are calculated

## 12. Recommended next action

Create or update the customer/advisor demo walkthrough for the current four-demo
state. The walkthrough should show Level 1 load-only, Level 2 P1 water-quality
context, Level 3 P1.5 aeration/solids context, and Level 4 P2a selected
operating-cost pressure, while preserving all guardrails above.
