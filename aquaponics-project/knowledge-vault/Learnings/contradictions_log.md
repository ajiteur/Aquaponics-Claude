# Contradictions Log

[[Reference/Glossary and Naming Conventions#Derived|Derived]] from: `data/sources/research_reports/distilled/Distilled_Research_Pack_Aquaponics_L1.md`

## Related Notes

- [[Home]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Sources/Source Register|Source Register]]

## Open Questions

### [[Learnings/contradictions_log#UQ-001|UQ-001]]
- Issue: FAO "Small-scale aquaponic food production" manual not directly ingested as primary text.
- Why unresolved: Water chemistry report notes the FAO PDF was not retrievable during research; only secondary references were used.
- Evidence still needed: Direct ingestion of FAO manual sections on pH, filtration, pumps/aeration, and monitoring targets.

### [[Learnings/contradictions_log#UQ-002|UQ-002]]
- Issue: Pump power draw anchor contradiction (`0.37 kW` vs `0.74 kW` at similar reported flow).
- Why unresolved: Same UVI hosted-copy document reports different motor ratings across system versions or trials.
- Evidence still needed: Identify which value maps to which UVI system configuration and whether it is nameplate or measured draw.

### [[Learnings/contradictions_log#UQ-003|UQ-003]]
- Issue: TAN-from-feed alternative rule (`2.2 lb NH3-N per 100 lb feed`) not reconciled with the protein-based equation.
- Why unresolved: Reports flag it as provisional pending reconciliation of assumptions such as protein percent, assimilation, and solids removal.
- Evidence still needed: Decide one [[Reference/Glossary and Naming Conventions#Canonical|canonical]] [[Reference/Glossary and Naming Conventions#TAN|TAN]] production model, with the protein-based model preferred and the other retained only as a cross-check.

### [[Learnings/contradictions_log#UQ-004|UQ-004]]
- Issue: Lettuce preferred pH `6.0-7.0` in some small-system tables vs tight CEA optimum near `5.8`.
- Why unresolved: Lettuce report flags the `6-7` values as context-dependent and possibly not trial-derived.
- Evidence still needed: Decide whether to add a small-system or low-precision mode, or keep one global lettuce pH optimum.

### [[Learnings/contradictions_log#UQ-005|UQ-005]]
- Issue: Basil tolerates pH as low as `4.0` in a short trial vs toxicity guidance below `5.8` in soilless substrate.
- Why unresolved: Basil report flags likely differences by system type, nutrient recipe, and duration.
- Evidence still needed: Decide whether to encode `pH < 5.8` as disorder risk and reserve `pH 4.0` for special-case experiments only.

### [[Learnings/contradictions_log#UQ-006|UQ-006]]
- Issue: Missing direct energy-per-oxygenation anchors such as `kg O2/kWh` or blower curves in uploaded reports.
- Why unresolved: Pump and aeration report provides only limited kW anchors from UVI, which is not enough for general energy modelling.
- Evidence still needed: Tier 1-2 RAS or aquaponics engineering manuals, or peer-reviewed aeration efficiency studies, to parameterize energy models.
