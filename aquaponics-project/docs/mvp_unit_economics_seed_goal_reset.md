# MVP Unit-Economics Seed-Goal Reset

## 1. Purpose

This document resets the Aquaponics MVP strategy around the seed-funding goal:
showing whether one bounded tilapia + basil DWC/raft aquaponics unit can be
measured, modeled, and eventually evaluated for commercial unit economics using
real data or explicitly supplied scenario data.

This is a strategic documentation pass only. It is not an operating manual, not
a product spec, not an implementation plan, and not approval to change source,
canonical knowledge, simulation output, scripts, tests, configs, ontology, or
business files.

Use these as source-of-truth support rather than duplicating them:

- `docs/mvp_operating_manual_decision_playbook.md`
- `docs/mvp_prompt_library.md`
- `docs/mvp_docs_source_of_truth_and_archive_inventory.md`
- `docs/mvp_current_truths_terminology_and_loophole_audit.md`
- `docs/mvp_mode_a_p1_p1_5_p2a_customer_demo_walkthrough.md`
- `docs/mvp_current_progress_map_update_spec.md`
- `docs/business_layer_contract.md`
- `docs/business_layer_plan.md`
- `docs/first_slice_adapter_saleable_harvest_null_status_design.md`
- `docs/first_slice_harvest_saleability_runtime_output_alignment.md`

## 2. Why this reset is needed

The current MVP has a credible four-level technical spine, but that spine can
drift away from the original seed-funding question if the next work keeps adding
technical layers without forcing them through unit-economics relevance.

The reset is needed because:

- the current demo proves a bounded calculation/report chain, not commercial
  operability
- P2a selected cost pressure is useful, but it is not total operating cost
- basil saleable harvest mass remains null/unresolved
- revenue and profitability remain blocked
- direct customer/operator feedback is not available yet
- benchmark scenarios can improve demo credibility, but they are not customer
  validation, real-world operating proof, or commercial proof

Future work should be judged by whether it advances the bounded unit-economics
proof path, not by whether it adds more calculations.

## 3. Revised seed-funding goal

Revised goal:

> Build a seed-demo evidence chain that shows how one bounded tilapia + basil
> DWC/raft aquaponics unit would be measured, modeled, and evaluated for unit
> economics once real or explicitly supplied scenario inputs are available,
> while keeping unsupported commercial claims blocked.

The goal is not to claim that the current MVP is commercially operable. The goal
is to show a disciplined path from measurable operating inputs to future
unit-economics evaluation, with missing inputs and uncertainty visible.

The near-term seed-funding story should be:

1. The technical spine can turn explicit feed, water, aeration/solids, and
   selected feed/electricity inputs into a guarded report.
2. The missing business inputs are known and can be captured in a data contract.
3. Public evidence and benchmark systems can populate scenario datasets with
   metadata for pre-customer demo credibility.
4. Real operator/customer/expert input is still required before commercial
   proof, revenue, profitability, or operability claims.

## 4. Current MVP foundation

The implemented foundation remains Mode A + P1 + P1.5 + P2a.

Mode A direct feed path:

- explicit `feed_kg_day`
- explicit `protein_fraction`
- TAN-N load
- nitrification oxygen demand
- alkalinity demand

P1 water-quality context:

- fish-tank TAN-N concentration context when complete inputs exist
- unionized NH3 fraction
- NH3-N and NH3 chemistry context

P1.5 aeration/solids context:

- measured DO context
- nitrification oxygen demand as a sub-load
- provisional dry-solids potential when an explicit coefficient is supplied

P2a operating-cost pressure:

- scenario feed cost
- scenario power kWh/day
- scenario power cost
- selected operating-cost pressure subtotal

This foundation is necessary because unit economics needs a traceable operating
model before it can ask whether a bounded unit is economically credible.

## 5. What the current MVP does not prove

The current MVP does not prove:

- fish safety
- system safety
- aeration adequacy
- total oxygen demand
- solids-removal capacity
- total operating cost
- revenue
- profitability
- commercial operability
- customer demand
- operator usability
- real basil saleable harvest mass
- real fish harvest mass or sale timing
- real labor, water, supplement, packaging, distribution, CAPEX, or risk costs

The current MVP also does not show that benchmark assumptions match any
operator's real system. Benchmarks can support scenario design; they cannot
replace field data or customer/operator validation.

## 6. Strategic constraint: no customer access yet

Until direct customer/operator feedback is available, the pathway should rely on:

- deep research
- public datasets
- institutional reports
- benchmark systems such as UVI, SRAC, FAO, and extension examples
- supplier price evidence with geography, date, unit, and source metadata
- manually created scenario datasets with explicit assumptions
- expert/customer questions only when public evidence cannot resolve a blocker

Do not assume customer validation can happen immediately. Pre-customer work
should make the demo more credible and the questions sharper, but it must not
claim validation.

## 7. Recommended pathway

Use this sequence even if older Path A / Path B labels conflict:

| Step | Status | Purpose | Output |
| --- | --- | --- | --- |
| Unit-economics seed-goal reset | next | Re-anchor the MVP to the seed-funding proof question. | This strategy reset document. |
| Unit-economics data contract | next | Define the data needed to evaluate one bounded tilapia + basil unit without inventing values. | Docs-only contract for inputs, units, provenance, nulls, and blocked claims. |
| Benchmark scenario dataset | later | Create explicitly labeled benchmark/scenario inputs from public evidence and supplier metadata. | Scenario dataset or dataset design with provenance and uncertainty. |
| Seed-demo report | later | Present current MVP outputs plus the benchmark data contract gap map. | Guarded report for seed review, not commercial proof. |
| Expert/customer validation | blocked | Test clarity, usefulness, missing inputs, and real-world fit. | Feedback packet after access exists. |

## 8. Checkpoint roadmap

| Checkpoint name | Category | Status | Purpose | Required inputs | Required outputs | Evidence required | Validation method | Definition of done | Drift risks | Stop conditions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Integrity snapshot | Demo credibility milestone | done | Confirm current repo demo guardrails before strategy work. | `python scripts/check_mvp_integrity.py --quick` result. | PASS/FAIL snapshot. | Current command output. | Quick integrity runner. | PASS with forbidden keys clean. | Treating PASS as field validation. | Stop if quick integrity fails. |
| Four-level MVP spine | Demo credibility milestone | done | Show the current calculation/report chain from feed input to selected cost pressure. | Mode A, P1, P1.5, and P2a demo inputs. | Guarded four-level demo report. | Current demo walkthrough and integrity runner. | Demo commands and quick/full integrity as appropriate. | All levels run and blocked claims remain blocked. | Calling P2a total cost or profit. | Stop if report wording implies safety, total cost, revenue, or profitability. |
| Seed-goal reset | Demo credibility milestone | next | Reconnect current technical work to the unit-economics proof objective. | Current source-of-truth docs and integrity snapshot. | Strategy reset doc. | Source docs listed in this reset. | Docs-only diff and protected-path checks. | Accepted reset that preserves blocked claims. | Turning reset into product spec or implementation plan. | Stop if benchmark scenarios are framed as validation or commercial proof. |
| Unit-economics data contract | Pre-customer evidence-backed proof milestone | next | Define required real/scenario inputs, units, provenance, null handling, and blocked outputs. | Business contract, business plan, current MVP outputs, saleable-harvest null design. | Docs-only data contract. | Existing business-layer boundary docs and public-evidence needs. | Docs diff, integrity quick, protected-path diff. | Required inputs and null states are explicit. | Smuggling invented values into contract. | Stop if contract populates values or changes canonical business files. |
| Benchmark source plan | Pre-customer evidence-backed proof milestone | next | Identify public evidence families for benchmark scenario creation. | Deep research questions, source policies, current data contract draft. | Source plan with evidence classes and metadata needs. | Public datasets, institutional reports, supplier evidence. | Research review and source traceability check. | Evidence families are ranked and gaps are visible. | Treating public benchmarks as customer feedback. | Stop if evidence is too weak for the intended precision. |
| Benchmark scenario dataset | Pre-customer evidence-backed proof milestone | later | Build a scenario-only dataset for seed-demo credibility. | Data contract, benchmark source plan, supplier price metadata. | Explicit scenario records with units, dates, geography, and source notes. | Public benchmark and supplier evidence. | Dataset review, schema/null checks, integrity quick. | All scenario values are labeled not canon and uncertainty is visible. | Treating scenarios as real operating proof. | Stop if any scenario value is promoted to canon. |
| Seed-demo report | Demo credibility milestone | later | Explain the current MVP and benchmark-data gaps to seed reviewers. | Four-level MVP output, data contract, benchmark scenario dataset. | Report showing what is calculated, assumed, missing, and blocked. | Integrity full, source-backed scenario metadata. | Full integrity before external-facing use. | Report is clear without claiming validation or commercial proof. | Making the report sound like a launch-ready business case. | Stop if report claims revenue, profit, total cost, safety, or operability. |
| Real-world data capture packet | Real-world data milestone | later | Prepare the fields needed from an actual operator or pilot run. | Data contract and expert/customer backlog. | Intake checklist for observed data and reviewed manual inputs. | Operator/expert review when accessible. | Review-only until access exists. | Packet distinguishes observed, reviewed manual, modeled, and missing fields. | Collapsing observed and modeled saleable mass. | Stop if `saleable_harvest_mass_kg` is inferred from proxies. |
| Saleable basil evidence path | Real-world data milestone | blocked | Resolve the basil revenue blocker only with observed or reviewed saleable mass. | Harvest/saleability alignment docs and future observed/reviewed inputs. | Non-null value only after explicit approval in a later pass. | Observed acceptance, QA review, or reviewed manual input. | Future adapter/runtime validation if approved. | `saleable_harvest_mass_kg` remains null until backed. | Using plant count, biomass, daily gain, or readiness labels as saleable mass. | Stop if saleable mass is inferred. |
| Unit-economics proof package | Unit-economics proof milestone | blocked | Evaluate whether a bounded unit is economically credible. | Real or explicitly supplied complete-enough cost, yield, price, labor, CAPEX, utilization, and risk inputs. | Unit-economics evaluation packet. | Real data or approved scenario data, with uncertainty. | Future business-layer validation after explicit approval. | Missing inputs propagate nulls; claims stay scoped to evidence. | Treating selected cost pressure as total operating cost. | Stop if revenue/profitability is calculated without required inputs. |
| Expert/customer question backlog | Expert/customer question backlog | later | Save questions that public evidence cannot answer reliably. | Data contract gaps, benchmark source gaps, seed-demo report draft. | Prioritized question list. | Public-evidence gap review. | Review with experts/customers when accessible. | Questions target blockers, not premature proof. | Asking customers to validate unsupported claims. | Stop if questions imply safety, profit, or operability has been proven. |
| Seed-fundraising narrative | Seed-fundraising narrative milestone | later | Explain why the MVP is disciplined enough for seed review. | Seed-demo report, benchmark scenario dataset, data contract, unresolved blockers. | Narrative that separates built, assumed, missing, and blocked. | Integrity full and source-backed benchmark metadata. | Review against forbidden claims. | Narrative asks for funding to reach proof, not because proof already exists. | Overstating commercial readiness. | Stop if narrative claims customer validation or commercial proof. |
| Long-term app/game expansion | Long-term app/game expansion milestone | later | Preserve future product ideas without distracting the unit-economics path. | Validated MVP direction and later user feedback. | Deferred concept notes only. | Post-validation evidence. | Strategy review after seed-demo feedback. | Expansion stays downstream of unit-economics proof. | Building UI/game layers before proof path is credible. | Stop if expansion displaces data contract, benchmark dataset, or seed-demo report. |

## 9. What can be proven before customer access

Before customer access, the project can credibly prove or demonstrate:

- the current four-level MVP report runs from explicit inputs
- the integrity runner detects current demo values and blocked claim keys
- Mode A, P1, P1.5, and P2a preserve important technical boundaries
- P2a can calculate selected feed and electricity cost pressure from explicit
  scenario inputs
- current missing business inputs can be named and organized
- benchmark scenario inputs can be collected with source metadata
- public evidence can narrow plausible scenario ranges and expose uncertainty
- a seed-demo report can show what is calculated, assumed, missing, and blocked

This is pre-customer demo credibility. It is not customer validation,
commercial proof, real-world operating proof, or proof of commercial
operability.

## 10. What remains unresolved until expert/customer/operator input

The following remain unresolved until expert, customer, operator, or real pilot
input is available:

- whether the demo answers the questions buyers, operators, advisors, or seed
  reviewers actually care about
- real saleable basil harvest mass and rejection/downgrade behavior
- real fish harvest mass, timing, mortality, and sale unit handling
- practical labor time, maintenance burden, harvest handling, and packaging
- actual equipment duty cycles, downtime, backup power needs, and failure modes
- actual local price realization by channel and product form
- acceptable risk, uncertainty, and confidence framing for decisions
- whether a bounded unit is commercially operable in a real setting
- whether benchmark scenarios are representative enough to justify seed funding

## 11. Scenario-based assumptions versus canon

Keep these scenario-based unless a later explicit canon pass approves otherwise:

- feed amount and protein fraction used in demo inputs
- fish-tank water volume, pH, temperature, and accumulation period in examples
- measured DO in examples
- dry-solids coefficient and dry-solids basis
- feed price, electricity tariff, equipment power, runtime, geography, and date
- benchmark yield, cost, price, labor, CAPEX, utilization, and risk assumptions
- UVI/SRAC/FAO/extension benchmark values adapted to this unit
- supplier price evidence
- manually created scenario datasets

Scenario values may support demos and sensitivity framing. They must not become
canonical biology, canonical business truth, runtime truth, or customer
validation by implication.

## 12. Expert/customer question backlog

Save these questions for later expert/customer/operator access:

- Which operating inputs would you trust enough to provide before seeing
  revenue or profitability estimates?
- Which missing costs matter most first: labor, water, supplements, packaging,
  backup power, maintenance, rent, financing, or CAPEX?
- What is the acceptable source for feed price and electricity tariff evidence?
- How should saleable basil mass be observed, reviewed, or accepted for the
  target sale form?
- What downgrade, shrink, rejection, or handling losses matter in practice?
- What fish harvest timing, mortality, sale unit, and price evidence is needed?
- What equipment power basis is acceptable: nameplate, measured, duty-cycle, or
  meter-derived?
- Which benchmark system is most comparable, and what context differences make
  it weak?
- Which output would make the seed-demo credible enough for a follow-up?
- What would make the demo misleading, even if the calculations are correct?

## 13. Claims that remain forbidden

Do not claim or imply:

- `saleable_harvest_mass_kg` is known unless observed or explicitly reviewed
- benchmark scenarios are customer validation
- benchmark scenarios are commercial proof
- benchmark scenarios are real-world operating proof
- pre-customer demo credibility is customer validation
- fish safety
- system safety
- aeration adequacy
- total oxygen demand
- total operating cost
- revenue
- profitability
- commercial operability
- seed readiness because the four-level demo runs
- scenario assumptions are canon

## 14. Anti-drift implications

Every future task should be checked against one question:

> Does this advance the tilapia + basil unit-economics proof path?

Useful next work should make one of these clearer:

- what can be measured
- what can be modeled
- what must remain scenario-based
- what public evidence can support
- what real operator/customer input is still missing
- what is blocked from commercial claims

Anti-drift rules:

- benchmark scenarios are not customer validation
- benchmark scenarios are not real-world operating proof
- pre-customer demo credibility is not commercial proof
- technical helper expansion should not outrun the unit-economics data contract
- business-layer work should preserve nulls instead of inventing values
- app/game expansion should remain downstream of seed-demo credibility and
  unit-economics proof

## 15. Next 3-5 actions

1. Create a docs-only unit-economics data contract that names the fields, units,
   provenance, null behavior, and blocked outputs needed for one bounded unit.
2. Draft a Deep Research request for benchmark systems, public datasets,
   institutional reports, and supplier-price evidence needed by that contract.
3. Create a benchmark scenario dataset design that keeps every value labeled as
   scenario, source-backed, and not canon.
4. Create a seed-demo report design that combines the four-level MVP output with
   the data contract and benchmark scenario gaps.
5. Prepare the expert/customer question backlog for later use when access exists.

## 16. What not to do next

Do not do these next:

- do not start customer validation as if customer access exists
- do not add revenue or profitability calculations
- do not claim total operating cost from P2a selected cost pressure
- do not infer or populate `saleable_harvest_mass_kg`
- do not promote benchmark values into canon
- do not modify `data/knowledge/**`, `data/simulation/**`, `src/**`,
  `scripts/**`, `tests/**`, configs, ontology files, or knowledge-vault notes
- do not start Mode B, P2c, simulation integration, business-consumer logic, or
  app/game expansion before the unit-economics data contract and benchmark
  scenario path are clear
- do not archive or move docs as part of this reset

## 17. Recommended next action

Run a docs-only unit-economics data contract pass next. It should define the
minimum input set, units, provenance requirements, null propagation behavior,
scenario-versus-canon boundaries, and blocked outputs needed before benchmark
scenario data or a seed-demo report is created.
