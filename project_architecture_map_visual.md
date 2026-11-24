# Project Architecture Map — Visual

Status: `draft`

## Visual Map

```mermaid
flowchart TD
    A[Evidence / Source-Trust Layer<br/>Trusted reports, corroboration, distilled research] --> B[Canonical Knowledge Layer<br/>data/knowledge/**]
    B --> C[Biological / Process / Simulation Layer<br/>Species, chemistry, components, scenario logic]
    C --> D[Derived Runtime / Simulation Output Layer<br/>data/simulation/**]
    D --> E[Runtime-to-Business Translation Layer<br/>Flattening, renaming, rollups, adapter]
    E --> F[Business Layer Foundation<br/>pricing, cost, labor, capex, channel, yield rules]
    B --> F
    F --> G[First Vertical Slice<br/>basil bulk kg wholesale]

    B --> H[Vault / Navigation Layer<br/>knowledge-vault/** hubs, notes, links]
    H --> I[Glossary / Explainers Layer<br/>Definitions, first-mention links, explainers]

    J[Governance / Agent / Automation Layer<br/>AGENTS, backlog, automation candidates, decision rules] --> A
    J --> B
    J --> D
    J --> E
    J --> F
    J --> H

    K[Propagation / Transplant Readiness Layer<br/>Emerging next layer] --> C
    K --> E

    classDef strong fill:#e8f3ff,stroke:#3b82f6,stroke-width:1px;
    classDef weak fill:#fff7e6,stroke:#f59e0b,stroke-width:1px;
    classDef next fill:#ecfdf5,stroke:#10b981,stroke-width:1px;

    class A,B,C,F,H,I,J strong;
    class D,E weak;
    class G,K next;
```

## Boundary Rules

- `data/knowledge/**` = canonical
- `data/simulation/**` = derived runtime output
- `knowledge-vault/**` improves navigation and understanding, but does not override canon
- deferred business rules stay explicit rather than hidden
- repeated low-judgment checks should gradually move toward local Python helpers

## Reading Guide

- **Blue nodes** = strong current layers
- **Amber nodes** = weaker bridge/output layers that need more work
- **Green nodes** = next target / emerging layer

## Main Current Gap

The main bridge gap is the **Runtime-to-Business Translation Layer**.

This is where the project still needs:
- flattening and renaming from runtime fields into business-contract fields
- period framing
- one explicit source for `saleable_harvest_mass_kg`

## First Vertical Slice Target

Current best first slice:
- `basil bulk kg wholesale`

Why:
- direct-mass path is already the cleanest
- avoids head-count, bunch-count, timing-heavy, and architecture-advisory complexity
- matches the runtime-to-business audit direction
