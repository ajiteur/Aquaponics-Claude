# Sump Tank

Generated at: `2026-04-14T13:30:48Z`

- Component ID: `sump_tank`
- Category: `water_loop`
- Role: Collects return water and stabilizes loop volume before recirculation.
- Status: `draft`
- CAPEX: `250.0`
- Power (W): `0`
- Maintenance interval (days): `21`
- Upgrade tier: `starter`

## Affects Variables

- water_volume_l
- recirculation_rate_lph
- system_stability_score

## Failure Modes

- low_water_level
- overflow
- float_switch_failure
- debris_buildup

## Notes

- Placeholder values for a basic sump vessel.
- Often used as the pump draw point in coupled systems.

## Related Notes

- [[Home|Home]]
- [[Components/Components|Components]]
- [[Sources/Source Register|Source Register]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Atomic Truths/Parameter Atomic Truths|Parameter Atomic Truths]]
