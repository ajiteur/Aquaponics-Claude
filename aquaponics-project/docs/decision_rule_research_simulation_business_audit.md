# Decision Rule for Research vs Simulation vs Business vs Repo Audit

_Last updated: 2026-04-19_

## Purpose

This document explains how to decide which kind of work should answer a project question:

- **deep research / evidence review**
- **simulation**
- **business calculation**
- **repo audit / compatibility check**

This prevents the project from using the wrong tool for the wrong decision.

Short rule:

- **Research decides structure and evidence-backed distinctions.**
- **Simulation decides dynamic behavior within that structure.**
- **Business calculation decides financial interpretation of simulated outcomes.**
- **Repo audit decides what current code and files can safely support right now.**

In most cases, the project should decide structure first, then simulate behavior, then interpret business meaning, and only use repo audit to check what the current implementation can safely support.

## Core distinction

### Use deep research when the question is:
**“What should exist in the model?”**

Deep research is best for:

- categories that should become first-class keys
- architecture differences that are real and reusable
- units, bases, and schema choices
- thresholds, constraints, and supported qualitative orderings
- context splits that should remain separate
- variables that are exogenous to a scenario
- deciding what is strong enough for canon vs what should remain TODO, deferred, or provisional

### Use simulation when the question is:
**“What happens when these things interact over time?”**

Simulation is best for:

- scenario-specific outcomes
- interaction effects
- time-accumulating behavior
- realized labor burden within a scenario
- realized downtime severity within a scenario
- yield continuity under a chosen setup
- effect of mitigations, upgrades, or operating choices
- comparison of strategies and combinations

### Use business calculation when the question is:
**“What does this scenario mean economically under the current business contract?”**

Business calculation is best for:

- revenue translation
- cost allocation
- architecture-specific cost interpretation
- risk-penalty interpretation
- contribution margin and payback framing
- scenario comparison on business grounds
- turning simulated biological or operational outcomes into decision-support outputs

### Use repo audit when the question is:
**“What does the current repo, code, or test surface actually assume right now?”**

Repo audit is best for:

- real code consumer checks
- field-shape compatibility
- scalar-vs-object safety
- deletion safety
- alias handling requirements
- snapshot and fixture impacts
- knowing what can safely change without breaking current consumers

## Rule 1: Exogenous vs endogenous

### Exogenous -> deep research
Use deep research when the answer comes from outside the scenario and should stay stable across many runs.

Examples:

- media bed, DWC/raft, and NFT are different business and technical archetypes
- NFT is more flow-fragile than raft
- media beds have integrated-filtration tradeoffs and clogging burden
- DWC/raft is currently treated in the project evidence base as the clearest commercial leafy-greens archetype
- architecture should be a first-class key in CAPEX, labor, yield-form, and risk models

### Endogenous -> simulation
Use simulation when the answer emerges from the chosen system over time.

Examples:

- how often flow interruption causes lost output in one starter scenario
- how much extra labor media beds create under one feed-loading regime
- how many delivery windows are missed under one operating strategy
- whether backup power or better solids removal changes the result enough to matter

## Rule 2: Stable reusable rule vs scenario result

### Stable reusable rule -> deep research
Research should define:

- architecture-specific CAPEX bundles
- task libraries
- driver-basis candidates
- failure-mode taxonomies
- output-form and channel-fit structure
- what should remain deferred or TODO

### Scenario result -> simulation
Simulation should estimate:

- event counts
- realized penalty curves
- realized labor frequency
- output continuity
- mitigation value
- comparative performance of candidate setups

## Rule 3: Financial interpretation vs biological behavior

### Biological or operational behavior -> simulation
Examples:

- TAN or NH3 dynamics
- downtime cascade severity
- disease-trigger frequency
- continuity under specific failure conditions

### Financial meaning of that behavior -> business calculation
Examples:

- lost-output interpretation
- recovery labor cost interpretation
- missed-delivery risk interpretation
- architecture-specific economic trade-off framing
- scenario margin comparison

## Rule 4: Canon truth vs current compatibility

### Canon truth -> research + evidence review
Use evidence and canon rules when deciding:

- what the canonical structure should be
- what names are authoritative in `data/knowledge/**`
- what context splits are justified
- what should remain draft, provisional, accepted, or TODO

### Current compatibility -> repo audit
Use repo audit when deciding:

- whether a field can be deleted
- whether a scalar can become an object
- whether a range object can change shape
- whether aliases are currently required for runtime compatibility
- whether fixtures or tests need updates

Repo audit proves **compatibility requirements**, not **biological truth**.

Repo audit should not be used to justify canon design unless the user explicitly asks for compatibility-first tradeoffs.

## Rule 5: Strong enough for canon vs TODO only

### Strong enough for canon
Promote when evidence is strong on:

- category direction
- architecture difference
- qualitative ordering
- existence of a risk mode
- likely driver-basis candidates
- reusable structural distinctions

Examples:

- architecture-specific maintenance categories
- architecture-specific CAPEX bundles
- architecture-specific risk-mode categories
- architecture-specific output-form context

### Not strong enough for canon
Keep as TODO, optional, provisional, or deferred when:

- evidence is directionally strong but not numerically stable
- task frequency varies too much by crop, species, loading, or management
- exact CAPEX numbers are too context-sensitive
- penalty curves are not consistently quantified
- the result depends heavily on local, operator, or channel context

## Best use of deep research

The highest-value research targets are:

1. **Architecture-specific CAPEX basis choice**
   - media bed: area vs media volume vs plant sites
   - DWC/raft: grow area vs water surface vs hydro volume
   - NFT: grow area vs channel length vs plant sites

2. **Maintenance task library and driver basis**
   - what tasks exist by architecture
   - whether each is best driven by:
     - per event
     - per day
     - per crop cycle
     - per grow area
     - per channel length
     - per media volume

3. **Output-form / channel-fit structure**
   - which harvest forms fit which architecture
   - what should remain advisory rather than becoming a universal profitability rule

4. **Failure-mode taxonomy**
   - what risk modes exist
   - what losses they can create:
     - shrink
     - lost output
     - recovery labor
     - missed delivery windows

## Best use of simulation

The highest-value simulation targets are:

1. **Penalty curves**
   - how often a risk triggers
   - how severe it becomes
   - how quickly it compounds

2. **Labor frequency under a chosen regime**
   - event counts
   - task burden under a specific architecture + crop + fish + loading regime

3. **Yield continuity and delivery reliability**
   - whether the system can meet weekly channel commitments
   - how continuity changes under failure or mitigation

4. **Value of mitigations**
   - backup power
   - improved solids removal
   - better aeration
   - more buffering

## Best use of business calculation

The highest-value business-calculation targets are:

1. **Revenue translation**
   - how saleable mass, count, timing, and continuity become revenue interpretation

2. **Cost allocation**
   - how labor, maintenance, utilities, and architecture burden are translated into business outputs

3. **Risk translation**
   - how downtime, shrink, quality loss, and missed commitments become penalties or degraded economics

4. **Scenario comparison**
   - which setup is more viable under the current contract assumptions

## Best use of repo audit

The highest-value repo-audit targets are:

1. **Consumer compatibility**
   - what current readers actually assume

2. **Field-contract safety**
   - what shapes must remain unchanged for now

3. **Alias boundary checks**
   - what belongs in canonical knowledge vs derived runtime compatibility

4. **Test-surface impact**
   - what fixture or snapshot changes are required after approved canonical changes

## Best hybrid pattern

Many project variables should use a hybrid pattern:

### Deep research defines:
- the variable
- the allowed units
- the architecture contexts
- the likely driver basis
- the evidence strength
- whether it is active, optional, provisional, or deferred

### Simulation later estimates:
- its realized value in a scenario
- its frequency
- its consequences
- its sensitivity to user choices

### Business calculation later interprets:
- its economic meaning
- its effect on margin, continuity, penalty, or payback
- its scenario-comparison relevance

## Practical checklist

Use **deep research** if the question is mainly:

- definitional
- structural
- taxonomic
- architecture-intrinsic
- threshold or constraint oriented
- reusable across many scenarios
- needed to choose schema keys or units

Use **simulation** if the question is mainly:

- dynamic
- interaction-driven
- scenario-specific
- action-dependent
- time-accumulating
- better expressed as a curve, distribution, or comparative outcome

Use **business calculation** if the question is mainly:

- margin-oriented
- payback-oriented
- channel-fit oriented
- penalty-translation oriented
- scenario-comparison oriented in financial terms

Use **repo audit** if the question is mainly:

- compatibility-oriented
- consumer-oriented
- schema-safety oriented
- alias-boundary oriented
- test-impact oriented

Keep it **deferred / TODO / provisional** if:

- evidence is directionally strong but not numerically stable
- the category exists but the driver basis is unresolved
- the answer would require inventing a number
- the answer depends too much on local or operator context

## Anti-patterns to avoid

Do not:

- use simulation output as proof that a canonical schema should exist
- use research to fabricate scenario-specific dynamic results
- use business-layer placeholders as proof of real market assumptions
- use `data/simulation/**` as source-of-truth for canon
- use repo compatibility requirements as proof of biological truth
- collapse context-dependent facts into one universal number just because the schema is simpler

## Output destination rule

- **Deep research output** -> `data/knowledge/**`, evidence memos, contradiction entries, open questions
- **Simulation output** -> `data/simulation/**`, scenario outputs, day logs, summaries
- **Business calculation output** -> business metrics, comparison outputs, later reporting layers
- **Repo audit output** -> compatibility memos, proposed diffs, fixture updates, consumer checks

## CAPEX example

A good way to think about CAPEX:

- **Deep research** decides what the system is sized by.
- **Simulation** decides how large the chosen system needs to be in one scenario.
- **Business calculation** decides what that size means economically.
- **Repo audit** decides whether current code can safely consume the chosen representation.

Example:

- Research should tell us whether NFT CAPEX is better modeled by channel length, grow area, or plant sites.
- Simulation can later tell us how many channels or how much grow area are needed for a specific lettuce + tilapia setup.
- Business calculation can later translate that into payback or cost structure.
- Repo audit can tell us whether the current contract can support that field shape safely.

That means:

- research chooses the ruler
- simulation decides what number to measure with that ruler
- business decides what that measurement means financially
- repo audit checks whether the current system can safely hold it

## Bottom line

Use **deep research** to decide:

- what variables exist
- how they differ by architecture
- what units and driver bases make sense
- what should remain deferred

Use **simulation** to decide:

- what happens in a specific plant / fish / system combination
- how often events occur
- how severe they become
- which combination performs best dynamically

Use **business calculation** to decide:

- what the scenario means economically
- how outcomes translate into cost, revenue, penalty, margin, or payback terms

Use **repo audit** to decide:

- what current files, code, and tests can safely support without breakage
