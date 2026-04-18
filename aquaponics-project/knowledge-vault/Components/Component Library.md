# Component Library

Generated at: `2026-04-06T23:17:38Z`

Version: `0.1`
Status: `draft`

## Library Notes

- Starter component library for aquaponics simulation assembly.
- Placeholder values are used where evidence-backed specifications are not yet available.
- All starter components are marked draft until component-specific evidence is collected.

## Water Loop Components

Count: **4**

### Fish Tank

- Component ID: `fish_tank`
- Category: `water_loop`
- Role: Primary fish rearing volume and ammonia source zone.
- Status: `draft`
- CAPEX: `500.0`
- Power (W): `0`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

#### Affects Variables

- water_volume_l
- tan_mg_L
- unionized_nh3_mg_L
- dissolved_oxygen_mg_L
- fish_biomass_kg

#### Failure Modes

- leak_or_crack
- overflow
- poor_solids_accumulation
- insufficient_aeration_distribution

#### Notes

- Placeholder tank cost and maintenance interval.
- Acts as the main livestock process vessel.

### Sump Tank

- Component ID: `sump_tank`
- Category: `water_loop`
- Role: Collects return water and stabilizes loop volume before recirculation.
- Status: `draft`
- CAPEX: `250.0`
- Power (W): `0`
- Maintenance interval (days): `21`
- Upgrade tier: `starter`

#### Affects Variables

- water_volume_l
- recirculation_rate_lph
- system_stability_score

#### Failure Modes

- low_water_level
- overflow
- float_switch_failure
- debris_buildup

#### Notes

- Placeholder values for a basic sump vessel.
- Often used as the pump draw point in coupled systems.

### Biofilter

- Component ID: `biofilter`
- Category: `water_loop`
- Role: Supports nitrifying bacteria for TAN and nitrite conversion.
- Status: `draft`
- CAPEX: `400.0`
- Power (W): `0`
- Maintenance interval (days): `14`
- Upgrade tier: `starter`

#### Affects Variables

- tan_mg_L
- nitrite_mg_L
- nitrate_mg_L
- nitrification_efficiency
- system_stability_score

#### Failure Modes

- media_clogging
- oxygen_limitation
- biofilm_dieoff
- channeling

#### Notes

- Placeholder biofilter economics and service interval.
- Critical component for ammonia control.

### Solids Filter

- Component ID: `solids_filter`
- Category: `water_loop`
- Role: Removes suspended solids before downstream biological treatment.
- Status: `draft`
- CAPEX: `300.0`
- Power (W): `0`
- Maintenance interval (days): `7`
- Upgrade tier: `starter`

#### Affects Variables

- tan_mg_L
- dissolved_oxygen_mg_L
- system_stability_score

#### Failure Modes

- clogging
- bypass_flow
- reduced_capture_efficiency
- sludge_overload

#### Notes

- Placeholder maintenance assumes routine cleaning.
- Solids management can indirectly reduce oxygen demand and ammonia release.

## Grow Components

Count: **3**

### Media Bed

- Component ID: `media_bed`
- Category: `grow`
- Role: Plant grow bed with media support and supplemental biofiltration surface area.
- Status: `draft`
- CAPEX: `350.0`
- Power (W): `0`
- Maintenance interval (days): `14`
- Upgrade tier: `starter`

#### Affects Variables

- plant_avg_biomass_g
- nitrate_mg_L
- biofilter_maturity
- system_stability_score

#### Failure Modes

- media_clogging
- poor_drainage
- root_zone_anaerobic_conditions
- uneven_flow_distribution

#### Notes

- Placeholder values for a small starter media bed.
- Can contribute both plant support and biological treatment.

### DWC Raft Bed

- Component ID: `dwc_raft_bed`
- Category: `grow`
- Role: Deep water culture bed for raft-based plant production.
- Status: `draft`
- CAPEX: `450.0`
- Power (W): `0`
- Maintenance interval (days): `10`
- Upgrade tier: `starter`

#### Affects Variables

- plant_avg_biomass_g
- nitrate_mg_L
- water_temperature_c
- dissolved_oxygen_mg_L

#### Failure Modes

- low_root_zone_oxygen
- algae_growth
- raft_damage
- stagnant_flow

#### Notes

- Placeholder economics and maintenance assumptions.
- Often benefits from strong aeration and even flow.

### NFT Channel

- Component ID: `nft_channel`
- Category: `grow`
- Role: Nutrient film technique channel for lightweight high-turnover crops.
- Status: `draft`
- CAPEX: `275.0`
- Power (W): `0`
- Maintenance interval (days): `10`
- Upgrade tier: `starter`

#### Affects Variables

- plant_avg_biomass_g
- nitrate_mg_L
- water_temperature_c
- recirculation_rate_lph

#### Failure Modes

- channel_blockage
- root_mat_obstruction
- dryout_from_pump_interruption
- uneven_slope

#### Notes

- Placeholder values for a small NFT section.
- Sensitive to flow interruption compared with media-based beds.

## Equipment Components

Count: **5**

### Water Pump

- Component ID: `pump`
- Category: `equipment`
- Role: Moves water through the recirculating loop.
- Status: `draft`
- CAPEX: `120.0`
- Power (W): `80`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

#### Affects Variables

- recirculation_rate_lph
- dissolved_oxygen_mg_L
- system_stability_score

#### Failure Modes

- power_loss
- impeller_clogging
- seal_failure
- flow_rate_drop

#### Notes

- Power value aligned with current starter scenario equipment assumptions.
- Single-point failure for many coupled systems.

### Aerator

- Component ID: `aerator`
- Category: `equipment`
- Role: Adds oxygen to fish and plant water zones.
- Status: `draft`
- CAPEX: `100.0`
- Power (W): `60`
- Maintenance interval (days): `21`
- Upgrade tier: `starter`

#### Affects Variables

- dissolved_oxygen_mg_L
- system_stability_score
- nitrification_efficiency

#### Failure Modes

- blower_failure
- diffuser_fouling
- line_leak
- insufficient_air_delivery

#### Notes

- Power value aligned with current starter scenario equipment assumptions.
- Critical for fish safety and nitrifier performance.

### Water Heater

- Component ID: `heater`
- Category: `equipment`
- Role: Raises water temperature toward warmwater setpoints.
- Status: `draft`
- CAPEX: `180.0`
- Power (W): `500`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

#### Affects Variables

- water_temperature_c
- daily_operating_cost
- fish_growth_score
- plant_growth_score

#### Failure Modes

- thermostat_failure
- heating_element_burnout
- overheating
- electrical_fault

#### Notes

- Power value aligned with current starter scenario equipment assumptions.
- Placeholder capex and service interval.

### Water Chiller

- Component ID: `chiller`
- Category: `equipment`
- Role: Reduces water temperature when thermal load is too high.
- Status: `draft`
- CAPEX: `900.0`
- Power (W): `700`
- Maintenance interval (days): `30`
- Upgrade tier: `advanced`

#### Affects Variables

- water_temperature_c
- daily_operating_cost
- dissolved_oxygen_mg_L
- system_stability_score

#### Failure Modes

- compressor_failure
- coolant_loss
- sensor_drift
- reduced_cooling_capacity

#### Notes

- Placeholder values only.
- Not assumed active in current starter scenarios.

### Grow Light

- Component ID: `grow_light`
- Category: `equipment`
- Role: Provides supplemental plant lighting for indoor or low-light operation.
- Status: `draft`
- CAPEX: `220.0`
- Power (W): `150`
- Maintenance interval (days): `60`
- Upgrade tier: `starter`

#### Affects Variables

- plant_avg_biomass_g
- daily_operating_cost
- plant_growth_score

#### Failure Modes

- driver_failure
- reduced_output
- timer_failure
- fixture_overheating

#### Notes

- Placeholder light power and economics.
- Not active in the current starter scenario equipment profile.

## Sensor Components

Count: **3**

### pH Sensor

- Component ID: `ph_sensor`
- Category: `sensor`
- Role: Monitors system pH for control and alerting.
- Status: `draft`
- CAPEX: `90.0`
- Power (W): `2`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

#### Affects Variables

- pH
- target_pH_mode
- system_stability_score

#### Failure Modes

- calibration_drift
- probe_fouling
- signal_loss
- slow_response

#### Notes

- Placeholder instrument values.
- Useful for automation and trend logging.

### Dissolved Oxygen Sensor

- Component ID: `do_sensor`
- Category: `sensor`
- Role: Monitors dissolved oxygen for fish safety and aeration control.
- Status: `draft`
- CAPEX: `250.0`
- Power (W): `3`
- Maintenance interval (days): `14`
- Upgrade tier: `advanced`

#### Affects Variables

- dissolved_oxygen_mg_L
- system_stability_score

#### Failure Modes

- membrane_fouling
- calibration_drift
- signal_dropout
- temperature_compensation_error

#### Notes

- Placeholder monitoring hardware values.
- Can support alarms or closed-loop aeration control.

### Temperature Sensor

- Component ID: `temperature_sensor`
- Category: `sensor`
- Role: Monitors water or air temperature for thermal control and risk detection.
- Status: `draft`
- CAPEX: `35.0`
- Power (W): `1`
- Maintenance interval (days): `30`
- Upgrade tier: `starter`

#### Affects Variables

- water_temperature_c
- air_temperature_c
- system_stability_score

#### Failure Modes

- sensor_drift
- probe_disconnect
- slow_response
- incorrect_placement

#### Notes

- Placeholder values for a basic temperature probe.
- Supports heater and chiller control logic.

## Related Notes

- [[Components/Components|Components]]
