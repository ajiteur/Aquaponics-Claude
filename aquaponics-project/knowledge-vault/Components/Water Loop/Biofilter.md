# Biofilter

Generated at: `2026-04-14T14:24:38Z`

- Component ID: `biofilter`
- Category: `water_loop`
- Role: Supports nitrifying bacteria for TAN and nitrite conversion.
- Status: `draft`
- CAPEX: `400.0`
- Power (W): `0`
- Maintenance interval (days): `14`
- Upgrade tier: `starter`

## Affects Variables

- tan_mg_L
- nitrite_mg_L
- nitrate_mg_L
- nitrification_efficiency
- system_stability_score

## Failure Modes

- media_clogging
- oxygen_limitation
- biofilm_dieoff
- channeling

## Notes

- Placeholder biofilter economics and service interval.
- Critical component for ammonia control.
- Feed-based sizing anchors from the distilled pack: fluidized sand about 16 to 32 kg feed/m3 media/day, MBBR about 8 to 16 kg feed/m3 media/day, and bead systems about 16 to 32 kg feed/m3 media/day when washing is adequate.
- Nitrification stoichiometry anchors from the distilled pack: oxygen demand about 4.57 g O2 per g TAN-N and alkalinity demand about 7.14 g CaCO3 per g TAN-N.
- Startup and maturation are modeled as a lagged ramp rather than instant full capacity.

## Related Notes

- [[Home|Home]]
- [[Components/Components|Components]]
- [[Sources/Source Register|Source Register]]
- [[Learnings/Simulation Learnings|Simulation Learnings]]
- [[Atomic Truths/Parameter Atomic Truths|Parameter Atomic Truths]]
