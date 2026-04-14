# Temperature Sensor

Generated at: `2026-04-14T02:11:26Z`

- Component ID: `temperature_sensor`
- Category: `sensor`
- Role: Monitors water or air temperature for thermal control and risk detection.
- Status: `draft`
- CAPEX: `35.0`
- Power (W): `1`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

## Affects Variables

- water_temperature_c
- air_temperature_c
- system_stability_score

## Failure Modes

- sensor_drift
- probe_disconnect
- slow_response
- incorrect_placement

## Notes

- Placeholder values for a basic temperature probe.
- Supports heater and chiller control logic.

## Related Notes

- [[Home|Home]]
- [[Components/Components|Components]]
- [[Sources/Source Register|Source Register]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Atomic Truths/Parameter Atomic Truths|Parameter Atomic Truths]]
