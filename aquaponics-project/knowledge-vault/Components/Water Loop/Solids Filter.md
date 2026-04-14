# Solids Filter

Generated at: `2026-04-14T02:11:26Z`

- Component ID: `solids_filter`
- Category: `water_loop`
- Role: Removes suspended solids before downstream biological treatment.
- Status: `draft`
- CAPEX: `300.0`
- Power (W): `0`
- Maintenance interval (days): `7`
- Upgrade tier: `starter`

## Affects Variables

- tan_mg_L
- dissolved_oxygen_mg_L
- system_stability_score

## Failure Modes

- clogging
- bypass_flow
- reduced_capture_efficiency
- sludge_overload

## Notes

- Placeholder maintenance assumes routine cleaning.
- Solids management can indirectly reduce oxygen demand and ammonia release.
- Settling clarifier anchor from the distilled pack: design around 15 to 30 minutes HRT, with aquaponics operational corroboration around 19 to 20 minutes and weaker capture near about 9.5 minutes.
- Radial-flow settlers outperform swirl separators on mean TSS removal under the distilled-pack comparison.

## Related Notes

- [[Home|Home]]
- [[Components/Components|Components]]
- [[Sources/Source Register|Source Register]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Atomic Truths/Parameter Atomic Truths|Parameter Atomic Truths]]
