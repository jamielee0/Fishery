# Data Dictionary — Trees to Seas v1

<!-- TODO: Populate as data sources are confirmed during Day 2 -->

## Directory Structure

```
data/
  raw/            # Original downloaded data, never modified
  intermediate/   # Cleaned, QA/QC'd, but not yet aligned
  processed/      # Feature-ready panels for modeling
```

## Naming Convention

```
data/raw/{source}_{variable}_{start}_{end}.{ext}
data/intermediate/{source}_{variable}_clean.parquet
data/processed/panel_{species}_{unit}.parquet
```

## Data Sources

See `02_data_inventory/data_inventory.csv` for the full inventory.

## Schemas

See `configs/schemas/` for field definitions:
- `species.yaml` — Focal species metadata
- `environmental_variables.yaml` — Environmental variable definitions
- `station_metadata.yaml` — Monitoring station metadata
- `survey_metadata.yaml` — Survey program metadata
