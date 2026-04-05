# Variable Ontology — Trees to Seas v1

Map every candidate variable to its source, unit, expected mechanistic role, and species relevance.

<!-- TODO: Complete during Day 3 literature review -->

## Environmental State Variables

| Variable | Unit | Source(s) | Role | Species Relevance |
|---|---|---|---|---|
| Water temperature | °C | FerryMon, NOAA, USGS | Direct thermal stress, degree-day accumulation | All |
| Salinity | PSU | FerryMon, NOAA | Osmoregulatory stress, range definition | All |
| Dissolved oxygen | mg/L | FerryMon, NOAA | Hypoxia stress, lethal/sublethal thresholds | All |
| Turbidity | NTU | FerryMon | Light attenuation, sediment proxy | Seagrass, oyster |
| PAR / light | µmol/m²/s | TBD | Photosynthesis driver | Seagrass |
| pH | standard units | FerryMon, NOAA | Acidification stress | Oyster |

## Derived Features

| Feature | Unit | Derived From | Role | Species Relevance |
|---|---|---|---|---|
| Degree-days | °C·days | Temperature | Cumulative thermal exposure | Blue crab, finfish |
| Habitat compression (temporal) | fraction | Healthy-range exceedance | Event-based risk | All |
| Habitat compression (spatial) | fraction of area | Healthy-range exceedance | Spatial risk | All |
| Consecutive days outside range | days | Healthy-range exceedance | Event severity | All |

## Watershed / Forcing Variables

| Variable | Unit | Source(s) | Role | Species Relevance |
|---|---|---|---|---|
| Rainfall | mm | NOAA, USGS | Freshwater pulse, runoff driver | All (indirect) |
| River discharge | m³/s | USGS | Salinity forcing, nutrient loading | All (indirect) |
| Land-use / impervious cover | % | NLCD | Runoff quality proxy | Oyster, seagrass |
| Disturbance signals | TBD | TBD | Sediment/burial proxy | Oyster, seagrass |

## Response Variables

| Target | Response Variable | Unit | Source | Notes |
|---|---|---|---|---|
| Blue crab | TBD | TBD | Fishery-independent survey | TODO: CPUE or occurrence |
| Eastern oyster | TBD | TBD | TBD | TODO: Condition index or reef extent |
| Finfish (TBD) | TBD | TBD | Fishery-independent survey | TODO: Select species first |
| Seagrass | TBD | TBD | TBD | TODO: Aerial extent or density |
