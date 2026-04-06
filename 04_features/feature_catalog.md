# Feature Catalog — Trees to Seas v1

Document every feature used in modeling: name, definition, source variables, transform, and species relevance.

<!-- TODO: Populate during Day 6–7 feature engineering -->

## Raw Environmental Features

| Feature Name | Definition | Source Variable(s) | Transform | Unit | Species |
|---|---|---|---|---|---|
| temp_weekly_mean | Weekly mean bottom water temperature | bottom_water_temperature | time aggregation | °C | All |
| salinity_weekly_mean | Weekly mean bottom salinity | bottom_salinity | time aggregation | PSU | All |
| do_weekly_mean | Weekly mean bottom dissolved oxygen | bottom_dissolved_oxygen | time aggregation | mg/L | All |
| turbidity_weekly_mean | Weekly mean turbidity | turbidity | time aggregation | NTU | SAV primarily; secondary for others |

## Derived / Engineered Features (Temporal, Station-Based)

| Feature Name | Definition | Source Variable(s) | Transform | Unit | Species |
|---|---|---|---|---|---|
| degree_days_cumulative | Cumulative degree-days above base | temperature | accumulation | °C·days | Blue crab, Southern Flounder |
| temp_outside_range_days | Consecutive days outside healthy range | temperature | threshold + run length | days | Per species |
| habitat_compression_temporal | Fraction of lookback window outside healthy range | multiple | temporal exceedance | fraction | Per species |
| max_consecutive_unsafe_days | Longest run of unsafe days in lookback window | daily healthy/unsafe status | run length | days | Per species |
| hypoxia_duration | Days with bottom DO below species threshold | bottom_dissolved_oxygen | threshold exceedance | days | Blue crab, Southern Flounder |
| salinity_excursion | Days with salinity outside species bounds | bottom_salinity | threshold exceedance | days | Eastern oyster, Blue crab |
| heat_event | Days above temperature upper bound | bottom_water_temperature | threshold exceedance | days | SAV, Blue crab |

**Note:** Spatial safe-area interpolation is DEFERRED from v1 per DEC-008. All v1 compression features are temporal and station-based. Spatial extension may be revisited post-v1 if data density supports it.

## Watershed / Forcing Features

| Feature Name | Definition | Source Variable(s) | Transform | Unit | Species |
|---|---|---|---|---|---|
| discharge_weekly | Weekly mean river discharge | USGS discharge | time aggregation | m³/s | All (indirect) |
| rainfall_weekly | Weekly total rainfall | NOAA precip | time aggregation | mm | All (indirect) |
