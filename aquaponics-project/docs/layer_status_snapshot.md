# Layer Status Snapshot

Status: `draft`

## Purpose

- Give one practical snapshot of the project's current layers, what each layer does, how complete it is, and what still remains.
- Help choose next work without pretending the project is more quantified than it is.
- Keep the current objective visible: one narrow, reviewable first vertical slice from runtime outputs to business interpretation.

## How to Read This Snapshot

- This is a planning snapshot, not a canonical contract.
- Percentages below are rough planning judgments, not precise measurements.
- Read the `Now / Next / Later` planning docs and layer notes together rather than treating one percentage as decisive.
- This table mixes true repo layers with two readiness-oriented planning rows: `First vertical slice readiness` and `Propagation / transplant-readiness`.
- The current repo boundary still matters most:
  - `data/knowledge/**` = canonical
  - `data/simulation/**` = derived runtime
  - `knowledge-vault/**` = navigation and human-readable note layer

## Layer-by-Layer Table

| Layer | Approx. completion | What exists now | Main remaining gaps |
|---|---:|---|---|
| Evidence / source-trust layer | 90% | Trust-policy direction is clear, core reports are in place, and architecture, species, and chemistry evidence has been reviewed repeatedly. | Distilled-pack refresh, more repeatable contradiction handling, and cleaner source-registry discipline. |
| Repo truth / canonical knowledge layer | 85% | Canonical ownership is clear in `data/knowledge/**`, and core species, business, and architecture knowledge now lives in repo-grounded files. | More normalization passes, more explicit promotion workflow, and a few still-provisional canon decisions. |
| Biological / process / simulation layer | 78% | Starter scenarios, runtime outputs, water chemistry behavior, and species/runtime mirrors exist and are usable for internal work. | Harvest/event rollups are still thin, some outputs are snapshot-shaped rather than business-ready, and richer scenario result structure is still missing. |
| Business layer foundation | 82% | Contract, plan, pricing, channels, cost, labor, CAPEX, yield-to-revenue, and deferred risk scaffolding all exist in canonical form. | One narrow populated path is still missing, many numeric assumptions remain null by design, and deferred paths are not yet active. |
| Runtime-to-business translation layer | 30% | The first read-only audit now exists and identifies direct fields, simple mappings, null-allowed fields, and real blockers. | No thin adapter exists yet, harvest-mass mapping is still unresolved, and naming or period-frame normalization has not been implemented. |
| Vault / navigation / glossary / explainers layer | 92% | Glossary, chemistry explainers, and multiple restrained linking passes are in place, and the vault is much easier to navigate. | Only light hygiene and incremental linking remain. |
| Governance / rules / agent-usage layer | 80% | `AGENTS.md`, decision-rule guidance, automation-candidate planning, and backlog discipline are all in place. | More repeatable review queues, a lightweight contradiction workflow, and some helper automation remain. |
| First vertical slice readiness | 45% | The slice objective is clear, the runtime audit exists, and the cleanest first slice now points toward basil bulk kg wholesale. | The chosen slice still needs a formal narrow path populated and one reviewable interpretation output produced. |
| Propagation / transplant-readiness layer | 10% | A few propagation or transplant-related hints exist, especially lettuce propagation fields and runtime `days_since_transplant` tracking. | No coherent propagation layer exists yet, it is not integrated into the first slice, and cross-species readiness is still very early. |

## Short Notes on Each Layer

### 1. Evidence / source-trust layer

What it is: the research, corroboration, and trust-policy base that decides what belongs in canon.

What is done: the project already has strong species, chemistry, pump, aeration, biofilter, solids-filter, and architecture evidence, plus a stable canonical-vs-derived boundary.

What remains: contradiction handling and source-registry discipline are still more manual than they should be.

Approx. completion: `90%`

### 2. Repo truth / canonical knowledge layer

What it is: the repo-owned source-of-truth layer under `data/knowledge/**`.

What is done: canonical business, species, and architecture knowledge now has clearer ownership and cleaner repo structure than earlier passes.

What remains: some names, normalization choices, and promotion decisions are still provisional rather than fully settled.

Approx. completion: `85%`

### 3. Biological / process / simulation layer

What it is: the derived runtime layer that models scenario behavior and emits day logs, summaries, and starter-scenario outputs.

What is done: current simulation outputs are already good enough to support internal biological and operational review.

What remains: the output shape is still more snapshot-oriented than business-ready, especially for harvest rollups, event records, and normalized period framing.

Approx. completion: `78%`

### 4. Business layer foundation

What it is: the canonical contract and scaffolding that translate runtime outcomes into business meaning.

What is done: the first-pass business foundation exists, architecture-aware CAPEX and maintenance scaffolding has been strengthened, and deferred paths are explicit instead of hidden.

What remains: one narrow path still needs actual populated assumptions and one first reviewable output path.

Approx. completion: `82%`

### 5. Runtime-to-business translation layer

What it is: the thin mapping layer between derived runtime output shapes and the normative business contract field names.

What is done: the first audit makes the direct/derivable/missing split visible and shows that basil bulk kg wholesale is the cleanest first target.

What remains: there is still no working adapter, and `saleable_harvest_mass_kg` remains the clearest blocker.

Approx. completion: `30%`

### 6. Vault / navigation / glossary / explainers layer

What it is: the human-readable navigation layer used for glossary control, explainer notes, and vault browsing.

What is done: glossary, chemistry explainers, and restrained first-meaningful-mention linking are in place and already useful.

What remains: mostly low-risk maintenance and selective linking follow-ups.

Approx. completion: `92%`

### 7. Governance / rules / agent-usage layer

What it is: the operating-rule layer that keeps research, repo audit, business, and bounded automation work from bleeding into each other.

What is done: the repo now has concrete guidance for agent behavior, decision routing, bounded automation, and repeated-task evaluation.

What remains: more operational repetition data, some local helpers, and a lighter contradiction queue workflow.

Approx. completion: `80%`

### 8. First vertical slice readiness

What it is: readiness to show one working internal path from runtime outputs to business interpretation.

What is done: the objective is clear, the business foundation is usable, and the first audit already narrowed the best slice candidate.

What remains: one explicit slice choice artifact, one populated pricing/cost/labor path, and one reviewable interpretation output.

Approx. completion: `45%`

### 9. Propagation / transplant-readiness layer

What it is: the still-early layer for propagation, seedling, transplant, and nursery-stage reasoning.

What is done: there are some lettuce propagation anchors and some runtime transplant-timing fields.

What remains: this layer has not been built into a coherent workflow yet and is not part of the current narrow slice.

Approx. completion: `10%`

## Strongest Completed Layers

- Evidence / source-trust layer
- Vault / navigation / glossary / explainers layer
- Repo truth / canonical knowledge layer

These layers are already strong enough to support review-first work without reopening major boundary confusion.

## Most Important Incomplete Layers

- Runtime-to-business translation layer
- First vertical slice readiness
- Propagation / transplant-readiness layer

The first two are important because they block the current objective. The last one is clearly behind, but it is not the current bottleneck.

## Current Overall Read

- Overall foundation readiness: about `80%`
- First working internal slice readiness: about `45%`

Interpretation:

- The repo is past the major cleanup and boundary-confusion phase.
- The foundation is strong enough for focused forward work.
- The project is not yet at a clean first internal slice because the translation layer and one narrow populated business path still need to be completed.

## Recommended Next Actions

1. Use `docs/runtime_to_business_field_audit.md` as the working input for immediate integration planning.
2. Record the first direct-mass slice choice explicitly, with `basil bulk kg wholesale` as the current best candidate.
3. Populate one narrow pricing/cost/labor path for that slice without widening into bunch, head, or timing-heavy logic.
4. Produce one first reviewable business interpretation output from that narrow path.
5. Leave broader propagation/transplant-readiness work for later, after the first internal slice is working.
