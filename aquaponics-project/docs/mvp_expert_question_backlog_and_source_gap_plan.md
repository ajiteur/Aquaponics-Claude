# MVP Expert Question Backlog and Source-Gap Plan

## 1. Purpose

This document is a lightweight backlog for unresolved source gaps, expert
questions, customer/operator questions, and observed-data needs in the
Aquaponics MVP.

It supports the current seed pathway:

1. technical spine
2. seed-goal reset
3. unit-economics data contract
4. benchmark scenario dataset
5. seed-demo report
6. expert/customer validation later when accessible
7. real-world unit-economics proof later

This is not a canonical ticket update, not an evidence-map update, and not an
implementation plan.

## 2. Relationship to seed-goal reset, data contract, benchmark fixture, and seed-demo report

The seed-goal reset defines the long-term goal: determine whether one bounded
tilapia + basil DWC/raft aquaponics unit can be measured, modeled, and
evaluated for commercial unit economics using real measured data, explicit
scenario data, or clearly labeled benchmark assumptions.

The data contract defines the field types, readiness levels, metadata, and
blocked outputs needed for that future evaluation.

The benchmark fixture
`data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json` is a
pre-customer benchmark fixture. It is mostly L1/L2 material, not L4/L5
validation. It is not canon, not customer validated, not commercial proof, and
not real-world operating proof.

The seed-demo report shows the current Mode A + P1 + P1.5 + P2a structure using
that fixture. This backlog identifies the source gaps and review questions that
remain after that report.

## 3. Current source-gap baseline

Current status:

- Technical spine: done enough for the current demo path.
- Seed-goal reset: done.
- Unit-economics data contract: done.
- Benchmark scenario design and fixture: done.
- Seed-demo benchmark report: done.
- Customer/operator validation: not yet available.
- Commercial proof: not yet available.
- Real-world operating proof: not yet available.

Known benchmark fixture source gaps:

| gap_id | current status | planning interpretation |
|---|---|---|
| `uvi_like_exact_mapping` | `source_gap` | Needs public/institutional source review before fixture assumptions can be more tightly source-backed. |
| `supplier_feed_price_metadata` | `source_gap` | Current feed price is scenario material until supplier evidence is attached. |
| `electricity_tariff_metadata` | `source_gap` | Current tariff is scenario material until tariff evidence is attached. |
| `labor_and_maintenance_basis` | `source_gap` | Labor and maintenance cadence are not sourced in the fixture. |
| `basil_harvest_and_saleability_basis` | `blocked_until_observed` | Observed or explicitly reviewed crop-output evidence is required before any saleability quantity can be populated. |

## 4. Gap classification system

Use these classifications for proposed questions and gaps:

| classification | meaning |
|---|---|
| `deep_research_candidate` | Requires synthesis across public, institutional, supplier, or research sources. |
| `public_evidence_search` | Can likely be resolved by targeted public or supplier-source review. |
| `benchmark_assumption_ok_for_now` | Can remain scenario/benchmark material without blocking the current seed-demo report. |
| `expert_question_candidate` | Public evidence may narrow the issue, but expert review is needed before stronger use. |
| `customer_operator_question_later` | Requires customer/operator access and should be saved for later. |
| `blocked_until_observed_data` | Cannot be resolved without observed or explicitly reviewed real data. |
| `do_not_pursue_now` | Likely to create goal drift or premature claims if pursued now. |

## 5. Domain classification system

Use these domain labels:

- `fish/feed`
- `stocking/biomass`
- `water quality`
- `tank/system volume`
- `TAN/NH3 chemistry`
- `aeration/oxygen`
- `solids/removal`
- `operating costs`
- `labor/maintenance`
- `fish output/revenue`
- `basil saleable output/revenue`
- `business/unit economics`
- `customer validation`

## 6. Backlog field format

Each backlog item should include:

- gap/question
- why it matters
- current status
- classification
- domain
- priority: high / medium / low
- decision impact
- source basis already available
- what evidence would resolve it
- resolution path
- whether it blocks the benchmark report
- whether it blocks unit-economics proof
- whether it should become a future open-question ticket
- next artifact affected
- recommended next action

## 7. Source gaps that can be addressed by Deep Research

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| DR1 | Which UVI/SRAC/FAO/extension benchmark is the closest public source basis for the bounded tilapia + basil DWC/raft fixture? | Tightens the benchmark source basis without turning it into canon. | Source gap. | `deep_research_candidate` | `tank/system volume` | high | Affects benchmark credibility and seed-demo assumptions. |
| DR2 | Which public tilapia feed-regime and stocking inputs are appropriate comparison bounds for the fixture? | Helps keep feed and biomass assumptions explicitly bounded. | Research pack exists; fixture still scenario-based. | `deep_research_candidate` | `fish/feed` | medium | Affects future benchmark revisions and Mode B review. |
| DR3 | What public evidence supports tank volume, exchange, pH, temperature, and TAN-to-NH3 context for a comparable system? | Helps separate chemistry context from safety claims. | Research pack exists; fixture values are scenario inputs. | `deep_research_candidate` | `TAN/NH3 chemistry` | medium | Affects water-quality explanation and assumption register. |
| DR4 | What public evidence supports oxygen-demand and dry-solids translation boundaries without claiming adequacy? | Helps explain P1.5 context without crossing into adequacy claims. | Research pack exists; fixture uses provisional scenario inputs. | `deep_research_candidate` | `aeration/oxygen` | high | Affects aeration/solids guardrails and future expert questions. |
| DR5 | What public evidence exists for labor and maintenance tasks in comparable DWC/raft or RAS-adjacent systems? | Labor and maintenance are required before any broader cost scope. | Source gap. | `deep_research_candidate` | `labor/maintenance` | high | Affects future P2c cost-extension design. |
| DR6 | What public evidence can define basil saleability evidence requirements without inferring `saleable_harvest_mass_kg`? | Keeps saleability blocked until observed or reviewed evidence exists. | Research exists; quantity remains blocked. | `deep_research_candidate` | `basil saleable output/revenue` | high | Affects future revenue/output contract and observed-data plan. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| DR1 | Benchmark design, fixture, UVI/SRAC/FAO/extension source families. | Cited public benchmark with comparable architecture, species, and unit boundaries. | Deep Research plus public source review. | no | partially | yes | benchmark fixture; seed-demo report | Create a Deep Research prompt focused on benchmark mapping. |
| DR2 | Tilapia feed-regime and stocking research pack. | Source-backed ranges or constraints with explicit context tags. | Deep Research. | no | partially | maybe | data contract; future Mode B review | Review only; do not implement biomass feeding yet. |
| DR3 | Tank volume, exchange, and TAN-to-NH3 research pack. | Source-backed chemistry/context explanation, not safety thresholds. | Deep Research. | no | partially | maybe | seed-demo report; data contract | Add to a future research synthesis queue. |
| DR4 | Aeration and solids-load research pack. | Evidence for translation boundaries and required records, not adequacy. | Deep Research plus expert review later. | no | yes | yes | P1.5 notes; customer questions | Draft expert-facing questions after research synthesis. |
| DR5 | Operating economics pack and benchmark fixture gap list. | Comparable task lists, cadence ranges, and record types. | Deep Research. | no | yes | yes | P2c cost extension | Prioritize before any broader cost scope. |
| DR6 | Basil saleability research and saleability docs. | Required observed/reviewed evidence standard for non-null saleable quantity. | Deep Research plus later expert/customer review. | no | yes | yes | revenue/output contract | Keep quantity blocked; research evidence requirements only. |

## 8. Source gaps that can be addressed by public evidence review

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| PE1 | Which supplier source should support the fixture feed price metadata? | Keeps feed price traceable and dated. | Source gap. | `public_evidence_search` | `operating costs` | high | Affects selected cost-pressure example. |
| PE2 | Which electricity tariff source should support the fixture tariff metadata? | Keeps power cost traceable by date, geography, and currency. | Source gap. | `public_evidence_search` | `operating costs` | high | Affects selected cost-pressure example. |
| PE3 | What public or supplier evidence should support pump/blower power basis? | Separates nameplate scenario input from measured power. | Scenario input. | `public_evidence_search` | `aeration/oxygen` | high | Affects future power-cost confidence. |
| PE4 | What public sources can define buffer, water, discharge, and disposal input metadata for future scope? | Helps prepare later cost fields without claiming total cost. | Mostly absent from current fixture. | `public_evidence_search` | `operating costs` | medium | Affects future P2c or data-contract update. |
| PE5 | Which public diagrams or descriptions best explain DWC/raft unit architecture for the report layer? | Improves communication without changing model behavior. | Current report uses high-level system overview. | `public_evidence_search` | `tank/system volume` | low | Affects future report/dashboard design. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| PE1 | Fixture has scenario feed price. | Supplier page, quote, invoice, or dated catalog metadata. | Public supplier review. | no | partially | maybe | benchmark fixture | Capture source metadata in a future update pass. |
| PE2 | Fixture has scenario electricity tariff. | Dated tariff source with geography and currency. | Public tariff review. | no | partially | maybe | benchmark fixture | Capture tariff metadata in a future update pass. |
| PE3 | Fixture uses nameplate pump/blower values. | Device datasheet, nameplate basis, or metering record requirement. | Public/supplier review. | no | partially | yes | seed-demo report; future P2c | Record basis; do not infer measured power. |
| PE4 | Data contract lists future cost inputs. | Public tariff/fee sources and required metadata. | Public source review. | no | yes | maybe | data contract; P2c | Defer until P2c design is approved. |
| PE5 | Report design and benchmark architecture label. | Public architecture references and diagrams. | Public source review. | no | no | no | future report/dashboard | Use only as explanatory support. |

## 9. Benchmark assumptions acceptable for now

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| BA1 | Can `feed_kg_day = 1.0` and `protein_fraction = 0.32` remain fixture inputs? | They support the current reproducible demo path. | Scenario inputs. | `benchmark_assumption_ok_for_now` | `fish/feed` | high | Keeps current technical demo reproducible. |
| BA2 | Can `effective_water_volume_l = 7800`, one-day accumulation, and `fish_tank` scope remain fixture inputs? | They anchor P1 context for the fixture. | Scenario inputs. | `benchmark_assumption_ok_for_now` | `tank/system volume` | high | Keeps current P1 output table reproducible. |
| BA3 | Can pH, temperature, freshwater, and measured DO remain fixture inputs? | They provide chemistry and context values without safety claims. | Scenario inputs. | `benchmark_assumption_ok_for_now` | `water quality` | high | Keeps P1/P1.5 demo values reproducible. |
| BA4 | Can nameplate pump/blower values and runtime remain fixture inputs? | They support the selected cost-pressure example. | Scenario inputs. | `benchmark_assumption_ok_for_now` | `operating costs` | high | Keeps P2a reproducible. |
| BA5 | Can feed price and electricity price remain scenario values until source metadata is attached? | They allow a selected cost-pressure example, not a total cost claim. | Source gaps. | `benchmark_assumption_ok_for_now` | `operating costs` | medium | Supports current report only with labels. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| BA1 | Current demo fixture and report. | Measured or source-backed feed record. | Keep scenario for now. | no | partially | no | benchmark fixture | Preserve labels. |
| BA2 | Current demo fixture and report. | Source-backed or measured volume records. | Keep scenario for now. | no | partially | maybe | data contract | Preserve labels. |
| BA3 | Current demo fixture and report. | Measured water-quality records. | Keep scenario for now. | no | partially | no | seed-demo report | Preserve guardrails. |
| BA4 | Current demo fixture and report. | Metered records or accepted source basis. | Keep scenario for now. | no | partially | maybe | P2c | Preserve nameplate basis label. |
| BA5 | Current demo fixture and report. | Dated supplier/tariff metadata. | Public evidence review. | no | partially | maybe | benchmark fixture | Treat as source gap, not canon. |

## 10. Expert question candidates

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| EQ1 | Which public benchmark should an expert consider closest to this bounded fixture? | Reduces risk of using a misleading benchmark anchor. | Candidate from fixture. | `expert_question_candidate` | `tank/system volume` | high | Affects benchmark confidence. |
| EQ2 | Should the first seed-demo report prefer nameplate, metered, duty-cycle adjusted, or supplier-estimated equipment power basis? | Clarifies data quality before stronger cost treatment. | Candidate from fixture. | `expert_question_candidate` | `operating costs` | high | Affects future P2c. |
| EQ3 | Which aeration and solids records are needed before any adequacy or capacity evaluation is considered? | Keeps current work from making adequacy claims. | Candidate from fixture. | `expert_question_candidate` | `aeration/oxygen` | high | Affects future data collection. |
| EQ4 | Which labor and maintenance activities must be tracked before broader cost scope is designed? | Labor is required for later unit-economics proof. | Candidate from fixture. | `expert_question_candidate` | `labor/maintenance` | high | Affects future cost contract. |
| EQ5 | What observed basil handling or buyer review record is sufficient before a saleability quantity can become non-null? | Prevents proxy-based saleable harvest inference. | Candidate from fixture. | `expert_question_candidate` | `basil saleable output/revenue` | high | Affects future output/revenue contract. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| EQ1 | Fixture, benchmark design, public-source families. | Expert-ranked benchmark fit with caveats. | Expert review after source review. | no | partially | yes | benchmark fixture | Save for expert interview. |
| EQ2 | Fixture device assumptions. | Expert recommendation on acceptable power basis. | Expert review. | no | partially | yes | P2c | Ask after public/supplier evidence is collected. |
| EQ3 | P1.5 design and report guardrails. | Required records and evaluation boundaries. | Expert review. | no | yes | yes | data contract | Ask as record-design question only. |
| EQ4 | Operating economics pack and data contract. | Task/cadence list and record standard. | Expert review. | no | yes | yes | P2c | Ask before broader cost design. |
| EQ5 | Basil saleability research and blocked field rule. | Acceptable observed/reviewed evidence standard. | Expert review plus customer/operator later. | no | yes | yes | revenue/output contract | Keep `saleable_harvest_mass_kg` blocked. |

## 11. Customer/operator questions for later

These questions should wait until customer/operator access exists unless a
specific blocker cannot be reduced by public evidence.

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| CO1 | What real daily feed records, feed class, and fish-biomass records are available? | Required for measured unit evaluation. | No customer access. | `customer_operator_question_later` | `fish/feed` | high | Affects real-world data readiness. |
| CO2 | What real tank/system volume, equipment, and runtime records are available? | Required for measured water and power context. | No customer access. | `customer_operator_question_later` | `tank/system volume` | high | Affects real-world data readiness. |
| CO3 | What water-quality measurements are collected, how often, and by whom? | Required to move beyond scenario context. | No customer access. | `customer_operator_question_later` | `water quality` | high | Affects future validation plan. |
| CO4 | What fish harvest, mortality, downgrade, and sale records exist? | Required before fish-output economics can be evaluated. | No customer access. | `customer_operator_question_later` | `fish output/revenue` | high | Affects future output contract. |
| CO5 | What basil harvest, rejection, saleability, buyer/channel, and sale records exist? | Required before basil saleable output can be non-null. | No customer access. | `customer_operator_question_later` | `basil saleable output/revenue` | high | Affects future output contract. |
| CO6 | What decision would make the MVP useful to a customer/operator? | Required for customer validation, later. | No customer access. | `customer_operator_question_later` | `customer validation` | medium | Affects outreach plan. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| CO1 | Data contract. | Operator records. | Customer/operator later. | no | yes | no | real-world report | Save for later intake form. |
| CO2 | Data contract. | Operator records and equipment metadata. | Customer/operator later. | no | yes | no | real-world report | Save for later intake form. |
| CO3 | Data contract. | Measurement logs and method metadata. | Customer/operator later. | no | yes | no | validation plan | Save for later intake form. |
| CO4 | Data contract. | Harvest and sale records. | Customer/operator later. | no | yes | no | revenue/output contract | Save for later intake form. |
| CO5 | Data contract and basil research docs. | Observed/reviewed harvest and buyer records. | Customer/operator later. | no | yes | no | revenue/output contract | Save for later intake form. |
| CO6 | Seed-demo report. | Direct customer/operator feedback. | Customer/operator later. | no | yes | no | customer validation plan | Do not assume immediate access. |

## 12. Blocked-until-observed-data items

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| BO1 | `saleable_harvest_mass_kg` | Must remain null/blocked unless observed or explicitly reviewed. | Blocked. | `blocked_until_observed_data` | `basil saleable output/revenue` | high | Blocks basil-output economics. |
| BO2 | Fish and basil sale quantities and price records. | Required before any revenue output can be evaluated. | Blocked. | `blocked_until_observed_data` | `fish output/revenue` | high | Blocks revenue evaluation. |
| BO3 | Labor hours, maintenance events, and consumable records. | Required before broader cost scope can be evaluated. | Blocked. | `blocked_until_observed_data` | `labor/maintenance` | high | Blocks unit-economics proof. |
| BO4 | Measured equipment power or accepted power-basis records. | Required before stronger power-cost evidence exists. | Blocked or scenario-only. | `blocked_until_observed_data` | `operating costs` | medium | Blocks real-world cost confidence. |
| BO5 | Real customer/operator outcome feedback. | Required for customer validation. | Blocked. | `blocked_until_observed_data` | `customer validation` | high | Blocks customer validation. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| BO1 | Data contract and report guardrails. | Observed or explicitly reviewed basil saleable mass record. | Observed data required. | no | yes | yes | revenue/output contract | Keep null/blocked. |
| BO2 | Data contract. | Actual sale records with quantity, price, currency, date, geography, and channel. | Observed data required. | no | yes | no | real-world report | Do not calculate from benchmark fixture. |
| BO3 | Data contract. | Operator task records and cost basis. | Observed data required. | no | yes | yes | P2c | Defer implementation. |
| BO4 | Benchmark fixture and data contract. | Metered data or reviewed acceptable basis. | Observed or reviewed data required. | no | partially | yes | P2c | Preserve nameplate/scenario labels. |
| BO5 | Seed-goal reset and goal-drift checklist. | Direct user/customer/operator feedback. | Customer/operator later. | no | yes | no | validation plan | Save questions for later. |

## 13. Do-not-pursue-now items

| id | gap/question | why it matters | current status | classification | domain | priority | decision impact |
|---|---|---|---|---|---|---|---|
| DN1 | New fish or plant expansion before first unit proof. | Creates drift away from the bounded tilapia + basil unit. | Premature. | `do_not_pursue_now` | `business/unit economics` | high | Would weaken seed-goal focus. |
| DN2 | App/game prototype before first unit proof. | Presentation layer would outrun evidence. | Premature. | `do_not_pursue_now` | `customer validation` | high | Would weaken seed-goal focus. |
| DN3 | Canon promotion of benchmark assumptions. | Would turn scenario material into false source of truth. | Forbidden. | `do_not_pursue_now` | `business/unit economics` | high | Would violate source hierarchy. |
| DN4 | Runtime or simulation integration from the benchmark fixture. | Current fixture is not a simulation artifact. | Forbidden for this path. | `do_not_pursue_now` | `business/unit economics` | high | Would broaden scope. |
| DN5 | Revenue, profitability, commercial-operability, safety, or total-cost outputs from the fixture. | Current fixture does not support those claims. | Forbidden. | `do_not_pursue_now` | `business/unit economics` | high | Would violate guardrails. |
| DN6 | Dashboard polish without blocked-claim and readiness panels. | UI could imply stronger claims than the evidence supports. | Premature. | `do_not_pursue_now` | `customer validation` | medium | Would create presentation drift. |

| id | source basis already available | evidence to resolve | resolution path | blocks benchmark report? | blocks unit-economics proof? | future open-question ticket? | next artifact affected | recommended next action |
|---|---|---|---|---|---|---|---|---|
| DN1 | Goal-drift checklist. | First bounded unit proof. | Do not pursue now. | no | no | no | long-term roadmap | Revisit only after first unit proof. |
| DN2 | Goal-drift checklist. | First bounded unit proof and validation needs. | Do not pursue now. | no | no | no | long-term roadmap | Revisit later. |
| DN3 | Operating manual and data contract. | Explicit approval plus evidence review. | Do not pursue now. | no | no | no | canonical tickets | Keep assumptions labeled. |
| DN4 | Benchmark design and fixture notes. | Explicit approved integration path. | Do not pursue now. | no | no | no | runtime/simulation | Keep fixture as data fixture only. |
| DN5 | Report guardrails. | Real observed/reviewed data and approved calculation scope. | Do not pursue now. | no | yes | no | unit-economics report | Keep outputs blocked. |
| DN6 | Seed-demo report design. | Approved dashboard design with guardrails. | Do not pursue now. | no | no | no | dashboard design | Require review-first design. |

## 14. Top 5 highest-value gaps to resolve next

| rank | gap | why high-value | decision affected | recommended resolution method | Deep Research prompt? | expert question? | blocks next seed-demo milestone? |
|---|---|---|---|---|---|---|---|
| 1 | Closest UVI/SRAC/FAO/extension benchmark mapping. | It strengthens the benchmark source basis while preserving non-canon status. | Benchmark revision and seed-demo credibility. | Deep Research plus public source review. | yes | yes | no, but improves it. |
| 2 | Feed price and electricity tariff metadata. | Current cost-pressure example is scenario-only until sources are attached. | Benchmark fixture metadata and P2a confidence. | Public supplier/tariff review. | maybe | no | no, but improves it. |
| 3 | Equipment power basis for pump/blower records. | Power cost depends on whether nameplate, metered, or duty-cycle data is accepted. | Future P2c design and data contract. | Public/supplier review, then expert review. | yes | yes | no. |
| 4 | Labor and maintenance basis for solids/filter/aeration operations. | Broader cost scope cannot be evaluated without task and cadence records. | P2c cost extension and future unit-economics proof. | Deep Research, then expert review. | yes | yes | no, but blocks later proof. |
| 5 | Basil saleability evidence standard. | Prevents proxy inference of `saleable_harvest_mass_kg`. | Revenue/output contract and real-world data plan. | Deep Research, then expert/customer review later. | yes | yes | no, but blocks later proof. |

## 15. Future Deep Research prompt candidates

1. Compare UVI, SRAC, FAO, extension, and RAS-adjacent sources for the closest
   public benchmark to a bounded tilapia + basil DWC/raft unit.
2. Review tilapia feed-regime, feed-class, stocking, and biomass evidence that
   can inform scenario bounds without implementing biomass-derived feeding.
3. Review tank volume, exchange, pH, temperature, and TAN-to-NH3 source context
   for comparable systems without deriving safety claims.
4. Review aeration, oxygen-demand, and solids-load translation boundaries,
   focusing on records needed later rather than adequacy claims.
5. Review operating-cost input evidence for feed price, electricity tariff,
   power basis, labor task categories, maintenance cadence, water, discharge,
   and disposal metadata.
6. Review basil harvest and saleability evidence requirements for observed or
   explicitly reviewed saleable quantity, without inferring
   `saleable_harvest_mass_kg`.

## 16. Future expert/customer outreach question candidates

Expert candidates:

- Which public benchmark is closest to the bounded UVI-like tilapia + basil
  DWC/raft fixture, and what caveats should be stated?
- Which equipment power basis is acceptable for a seed-demo report before
  metered data exists?
- Which aeration, solids, and maintenance records must be collected before any
  later evaluation of capacity or adequacy is considered?
- Which labor tasks and maintenance events are required for a credible future
  unit-economics dataset?
- What observed or reviewed basil handling and buyer record is sufficient
  before a saleability quantity may become non-null?

Customer/operator later:

- What daily feed, biomass, mortality, water-quality, equipment, harvest,
  labor, cost, and buyer/channel records can the operator actually provide?
- Which decision would the operator use the MVP report to make?
- Which fields are too hard to collect in practice?
- Which assumptions feel misleading or not representative of the operator's
  system?
- Which report outputs are useful, and which would require clearer guardrails?

## 17. Future canonical open-question candidates

These are candidates only. Do not modify
`data/knowledge/model_tickets/open_questions.json` during this backlog pass.

| candidate | why it may belong later | prerequisite before ticketing |
|---|---|---|
| Closest public benchmark context for UVI-like tilapia + basil DWC/raft. | May affect later canonical evidence boundaries. | Deep Research synthesis and review-first approval. |
| Acceptable power-basis vocabulary for equipment records. | May affect future data contract or business layer. | Public/supplier review plus expert review. |
| Required observed/reviewed evidence for basil saleable quantity. | May affect output vocabulary and null-status rules. | Deep Research plus expert/customer review. |
| Labor and maintenance record categories for future cost scope. | May affect future business-layer contracts. | P2c design approval. |
| Boundary between selected cost-pressure subtotal and broader cost scope. | May affect future unit-economics reporting. | Review-first business-layer pass. |

## 18. How to use this backlog before future work

Before new Deep Research tasks:

- Select only high-priority gaps tied to the data contract or benchmark report.
- State which blocked claims must remain blocked.
- Require source metadata and context tags.

Before Codex implementation passes:

- Confirm the task is not trying to resolve a source gap through code.
- Require approved design docs and allowed file lists.
- Stop if source gaps would be promoted into runtime behavior or canon.

Before seed-demo dashboard or report UI design:

- Include readiness labels, guardrail panels, and blocked-claim language.
- Avoid visuals that imply customer validation, real-world operating proof, or
  commercial proof.

Before expert/customer outreach:

- Ask only questions that public evidence cannot resolve safely.
- Do not assume customer/operator access exists now.
- Keep customer validation separate from benchmark credibility.

Before future Pro reviews:

- Provide this backlog, the goal-drift checklist, the seed-demo report, the
  data contract, and the benchmark fixture.
- Ask for prioritization and claim-boundary review, not broad product expansion.

## 19. Recommended next action

Run one focused Deep Research/public-source review on the closest public
benchmark mapping for `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`, including
feed, volume, architecture, and cost-metadata implications. Keep all results as
source-review material until a later review-first update pass approves changes
to the benchmark fixture or related docs.
