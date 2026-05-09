# Aquaponics MVP Expert/Advisor Review Prep

## 1. Purpose

This prep packet helps reviewers navigate the current Aquaponics MVP seed-demo
package for `uvi_like_tilapia_basil_dwc_raft_benchmark_v0`.

It is a review-prep and navigation artifact only. It is not public marketing
copy, customer outreach copy, a pitch deck, a dashboard, a new report, a
commercial-proof document, or approval for implementation work.

The package is pre-customer and benchmark-backed only in a guarded sense:
public-evidence-inspired, scaled, scenario-augmented, and not canon. Reviewers
should focus on whether the current framing, assumptions, labels, and blocked
claims are clear enough for expert/advisor review.

## 2. Who this review is for

| Reviewer type | Useful focus | Boundary |
| --- | --- | --- |
| Technical investor/advisor | Whether the MVP spine, evidence labels, traceability, and blocked-claim discipline are understandable. | Advisor review does not create customer validation, commercial proof, or real-world operating proof. |
| Aquaponics/RAS expert | Module scope, fish-tank concentration display, aeration/solids boundaries, power scaling, and source-fit caveats. | Expert judgment can improve framing, but it does not prove safety or commercial operation. |
| Future operator/customer reviewer | Which later records would be needed from a real unit and which labels would help operator review. | Future operator/customer review is later-stage unless explicitly available. |

## 3. What to open first

Recommended order:

1. [Review package index](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_review_package_index.md) for the package map and review order.
2. [Static dashboard prototype](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_dashboard_prototype.html) for a visual summary with visible guardrails.
3. [Seed-demo benchmark report](uvi_like_tilapia_basil_dwc_raft_benchmark_v0_report.md) for the written four-level walkthrough, assumptions, evidence labels, and blocked claims.
4. [Expert-question package](../../docs/mvp_expert_question_package_for_benchmark_review.md) for the detailed question set.
5. [Benchmark fixture JSON](../../data/benchmarks/uvi_like_tilapia_basil_dwc_raft_benchmark_v0.json) only if reviewing field-level metadata, evidence classes, readiness labels, or blocked/null fields.

If the review package index is unavailable in a future checkout, proceed with
the report, prototype, expert-question package, and benchmark fixture, then
restore or recreate the index before external review prep.

## 4. What feedback is most useful

Useful feedback is specific, scoped, and tied to one of these buckets:

- Technical-model feedback: units, output names, water-quality interpretation,
  aeration/solids boundaries, and whether the current four-level MVP spine is
  understandable.
- Benchmark/source feedback: whether public-evidence-inspired, scaled,
  scenario-augmented framing is honest enough and where source gaps remain.
- UI/report clarity feedback: whether evidence class, readiness level, scope,
  modelled-versus-observed status, business-overlay status, and blocked claims
  are visible enough.
- Business-evidence feedback: which future records are needed before business
  overlays can become stronger than scenario context.
- Blocked-claim feedback: any place the package appears to imply a claim that
  should remain blocked.
- Future customer/operator feedback: questions that should wait for observed
  customer/operator records.

Please name the artifact, section, field, or label affected. Avoid broad
requests to add new outputs unless the required evidence and scope are clear.

## 5. Priority review questions

1. Module boundary: what exact unit does this fixture represent?
2. Raft area implied by `feed_kg_day = 1.0`: what raft growing area, if any,
   should be paired with this scaled feed scenario?
3. Fish-tank versus total-system display: should reports show only fish-tank
   concentration context, or a separately labelled total-system context later?
4. Pump/blower scaling: how should nameplate pump and blower assumptions be
   scaled, labelled, or reviewed?
5. Backup aeration/power evidence: what records are needed before any
   reliability-adjacent wording is allowed?
6. Basil saleability evidence standard: what observed or explicitly reviewed
   handling or buyer evidence is enough before `saleable_harvest_mass_kg` can
   become non-null?

## 6. Feedback classification rubric

Use one classification per issue:

| Classification | Meaning |
| --- | --- |
| blocker | The package should not be used for review prep until this is corrected. |
| caution | The package can be reviewed, but the issue should be flagged clearly. |
| non-blocking note | Useful wording, layout, or traceability improvement. |
| source/evidence gap | A source, record, or provenance basis is missing. |
| expert judgment needed | A domain expert should decide the label, scope, or interpretation. |
| customer/operator question later | Requires observed customer/operator access or operating records. |
| do-not-pursue-now | Would create scope drift or require unsupported claims. |

Also tag the feedback type:

- `technical-model`
- `benchmark/source`
- `UI/report clarity`
- `business-evidence`
- `blocked-claim`
- `future customer/operator`

## 7. Claims reviewers should not assume

Do not assume the current package demonstrates:

- customer validation
- commercial proof
- real-world operating proof
- fish safety
- system safety
- aeration adequacy
- oxygen-transfer capacity
- total oxygen demand
- solids-removal capacity
- total operating cost
- revenue
- profitability
- margin, ROI, payback, break-even, or economic viability
- commercial operability
- known basil saleable harvest mass

Do not infer `saleable_harvest_mass_kg` from plant context, benchmark basil
context, feed, water quality, solids, cost pressure, readiness labels, or
saleability labels.

## 8. What decisions this review can inform

This review can inform later scoped decisions about:

- safer module-boundary wording
- whether fish-tank scope labels are clear enough
- whether benchmark/source caveats are visible enough
- whether pump/blower and backup-power questions are framed correctly
- whether report/prototype labels prevent overclaiming
- what evidence standard should gate any later non-null basil saleable mass
- whether to prepare a separate expert outreach packet
- whether a later guarded prototype update is worth scoping

## 9. What decisions this review cannot inform yet

This review cannot yet decide:

- whether a system is safe for fish or operators
- whether aeration or oxygen-transfer capacity is adequate
- whether solids removal is sufficient
- total operating cost
- revenue, profitability, margin, ROI, payback, break-even, or economic
  viability
- commercial operability
- customer validation
- real-world operating proof
- non-null `saleable_harvest_mass_kg`
- canon/default biology, model, business, or ontology values

Those decisions require observed records, explicit reviewed inputs, or separate
approved evidence/review passes.

## 10. Suggested review flow

1. Spend a few minutes on the review package index to understand the artifact
   map.
2. Scan the static dashboard prototype and note any place guardrails are not
   visible enough.
3. Read the seed-demo benchmark report sections on scenario identity,
   assumptions, four-level outputs, blocked claims, and next data needed.
4. Use the expert-question package to answer or classify the six priority
   questions.
5. Record each issue using the rubric in this packet.
6. Mark whether the issue should change fixture metadata, report/prototype
   wording, future data collection, or remain blocked.
7. Stop before proposing new calculations, revenue/profitability work, safety
   conclusions, or canon promotion.

## 11. Response template for reviewers

```text
Reviewer role:
Artifact reviewed:
Issue title:
Feedback type:
Classification:
Affected field/section/label:
Observation:
Why it matters:
Suggested wording or action:
Evidence/source basis, if any:
What this feedback does not resolve:
Should this be handled now, later, or not pursued now?
```

Use one response block per issue. If feedback is an answer to a priority
question, name the priority question in the issue title.

## 12. Recommended next action after feedback

After review, triage feedback into three groups:

1. Immediate wording or navigation updates that can be handled in a scoped
   report/prototype/package pass without changing values or claims.
2. Metadata or source-gap updates that need a separate benchmark fixture or
   evidence-review pass.
3. Later observed-data questions that should wait for customer/operator or
   explicitly reviewed records.

If a reviewer asks for a blocked claim, keep the claim blocked and record the
required evidence instead of treating the request as an approval to proceed.
