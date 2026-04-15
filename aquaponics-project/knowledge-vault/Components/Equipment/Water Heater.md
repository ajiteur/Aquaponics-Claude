# Water Heater

Generated at: `2026-04-14T16:13:16Z`

- Component ID: `heater`
- Category: `equipment`
- Role: Raises water temperature toward warmwater setpoints.
- Status: `draft`
- CAPEX: `180.0`
- Power (W): `500`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

## Affects Variables

- water_temperature_c
- daily_operating_cost
- fish_growth_score
- plant_growth_score

## Failure Modes

- thermostat_failure
- heating_element_burnout
- overheating
- electrical_fault

## Notes

- Power value aligned with current starter scenario equipment assumptions.
- Placeholder capex and service interval.

## Related Notes

- [[Home|Home]]
- [[Components/Components|Components]]
- [[Sources/Source Register|Source Register]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Atomic Truths/Parameter Atomic Truths|Parameter Atomic Truths]]
