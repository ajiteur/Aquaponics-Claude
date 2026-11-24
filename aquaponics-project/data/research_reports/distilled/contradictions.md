# Contradictions And Open Questions

Source pack: `data/sources/research_reports/distilled/Distilled_Research_Pack_Aquaponics_L1.md`

## Related Notes

- [[Learnings/Simulation Learnings]]
- [[Learnings/contradictions_log|Contradictions Log]]

## Tracked Entries

### UQ-001
- Issue: FAO "Small-scale aquaponic food production" manual not directly ingested as primary text.
- Why unresolved: Water chemistry report notes the FAO PDF was not retrievable during research; only secondary references were used.
- Evidence still needed: Direct ingestion of FAO manual sections on pH, filtration, pumps/aeration, and monitoring targets.
- Source section: `Unresolved item 1`

### UQ-002
- Issue: Pump power draw anchor contradiction (`0.37 kW` vs `0.74 kW` at similar reported flow).
- Why unresolved: Same UVI hosted-copy document reports different motor ratings across system versions or trials.
- Evidence still needed: Identify which value maps to which UVI system configuration and whether it is nameplate or measured draw.
- Source section: `Unresolved item 2`

### UQ-003
- Issue: TAN-from-feed alternative rule (`2.2 lb NH3-N per 100 lb feed`) not reconciled with the protein-based equation.
- Why unresolved: Reports flag it as provisional pending reconciliation of assumptions such as protein percent, assimilation, and solids removal.
- Evidence still needed: Decide one canonical TAN production model, with the protein-based model preferred and the other retained only as a cross-check.
- Source section: `Unresolved item 3`

### UQ-004
- Issue: Lettuce preferred pH `6.0-7.0` in some small-system tables vs tight CEA optimum near `5.8`.
- Why unresolved: Lettuce report flags the `6-7` table values as context-dependent and possibly not trial-derived.
- Evidence still needed: Decide whether to add a small-system or low-precision mode, or keep one global lettuce pH optimum.
- Source section: `Unresolved item 4`

### UQ-005
- Issue: Basil tolerates pH as low as `4.0` in a short trial vs toxicity guidance below `5.8` in soilless substrate.
- Why unresolved: Basil report flags likely differences by system type, nutrient recipe, and duration.
- Evidence still needed: Decide whether to encode `pH < 5.8` as disorder risk and reserve `pH 4.0` for special-case experiments only.
- Source section: `Unresolved item 5`

### UQ-006
- Issue: Missing direct energy-per-oxygenation anchors such as `kg O2/kWh` or blower curves in uploaded reports.
- Why unresolved: Pump and aeration report provides only limited kW anchors from UVI, which is not enough for general energy modelling.
- Evidence still needed: Tier 1-2 RAS or aquaponics engineering manuals, or peer-reviewed aeration efficiency studies, to parameterize energy models.
- Source section: `Unresolved item 6`
