# Pipeline — Trees to Seas v1

## Overview

ETL pipeline: raw data ingestion -> QA/QC -> alignment -> feature-ready panels.

## Pipeline Steps

<!-- TODO: Implement during Day 4–5 -->

1. **Ingest** — Download/copy raw data to `data/raw/`
2. **QA/QC** — Flag missing values, outliers, unit inconsistencies
3. **Align** — Interpolate/aggregate station data to common analysis unit (estuary-cell-week or estuary-week)
4. **Merge** — Join environmental state, forcing, survey, and habitat layers
5. **Export** — Write feature-ready panels to `data/processed/`

## Running the Pipeline

```bash
# TODO: Implement
make pipeline
```

## Configuration

Pipeline reads from `configs/project_config.yaml`. See `configs/project_config_template.yaml` for schema.
