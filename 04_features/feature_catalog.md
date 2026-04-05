# Feature Catalog — Trees to Seas v1

Document every feature used in modeling: name, definition, source variables, transform, and species relevance.

<!-- TODO: Populate during Day 6–7 feature engineering -->

## Raw Environmental Features

| Feature Name | Definition | Source Variable(s) | Transform | Unit | Species |
|---|---|---|---|---|---|
| temp_weekly_mean | Weekly mean water temperature | temperature | time aggregation | °C | All |
| salinity_weekly_mean | Weekly mean salinity | salinity | time aggregation | PSU | All |
| do_weekly_mean | Weekly mean dissolved oxygen | dissolved_oxygen | time aggregation | mg/L | All |
| turbidity_weekly_mean | Weekly mean turbidity | turbidity | time aggregation | NTU | All |

## Derived / Engineered Features

| Feature Name | Definition | Source Variable(s) | Transform | Unit | Species |
|---|---|---|---|---|---|
| degree_days_cumulative | Cumulative degree-days above base | temperature | accumulation | °C·days | Blue crab, finfish |
| temp_outside_range_days | Consecutive days outside healthy range | temperature | threshold + run length | days | Per species |
| habitat_compression_spatial | Fraction of area outside healthy range | multiple | spatial exceedance | fraction | Per species |
| habitat_compression_temporal | Fraction of time outside healthy range | multiple | temporal exceedance | fraction | Per species |

## Watershed / Forcing Features

| Feature Name | Definition | Source Variable(s) | Transform | Unit | Species |
|---|---|---|---|---|---|
| discharge_weekly | Weekly mean river discharge | USGS discharge | time aggregation | m³/s | All (indirect) |
| rainfall_weekly | Weekly total rainfall | NOAA precip | time aggregation | mm | All (indirect) |
