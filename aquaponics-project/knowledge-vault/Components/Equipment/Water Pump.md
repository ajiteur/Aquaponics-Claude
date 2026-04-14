# Water Pump

Generated at: `2026-04-14T03:03:47Z`

- Component ID: `pump`
- Category: `equipment`
- Role: Moves water through the recirculating loop.
- Status: `draft`
- CAPEX: `120.0`
- Power (W): `80`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

## Affects Variables

- recirculation_rate_lph
- dissolved_oxygen_mg_L
- system_stability_score

## Failure Modes

- power_loss
- impeller_clogging
- seal_failure
- flow_rate_drop

## Notes

- Power value aligned with current starter scenario equipment assumptions.
- Single-point failure for many coupled systems.

## Related Notes

- [[Home|Home]]
- [[Components/Components|Components]]
- [[Sources/Source Register|Source Register]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Atomic Truths/Parameter Atomic Truths|Parameter Atomic Truths]]
