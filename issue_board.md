# Issue Board — Trees to Seas v1 Sprint

## Day 1 (Complete)

- [x] Create repo structure with all sprint folders (00–09)
- [x] Add pyproject.toml / environment.yml
- [x] Add .gitignore
- [x] Create config template with all required sections
- [x] Add tests scaffolding
- [x] Write project brief and hypotheses
- [x] Initialize issue board, decisions log, assumptions log
- [x] Create placeholder files for all sprint folders
- [x] Add Makefile
- [x] Write README with orientation for next contributor

## Day 2 — Data Inventory & Access

- [ ] Complete `02_data_inventory/data_inventory.csv` with all candidate sources
  - FerryMon feeds: confirm URL, temporal range, variables, access method
  - NOAA stations: identify NC estuarine stations, confirm API access
  - USGS stations: identify relevant gauges, confirm data service
  - Ty's GitHub data: locate repo, catalog variables and temporal coverage
  - Fishery-independent surveys: identify NC DMF or similar, confirm access
  - Oyster layers: source and format
  - Seagrass layers: source, vintage, and spatial resolution
  - Watershed / land-use / disturbance: NLCD, NHD, or equivalent
- [ ] Fill `02_data_inventory/access_tracker.md` with access status per source
- [ ] Determine actual temporal overlap window across all sources
- [ ] Select the estuarine finfish target based on data overlap
- [ ] Confirm seagrass species for habitat indicator
- [ ] Draft station metadata schema in `configs/schemas/station_metadata.yaml`
- [ ] Get human approval on: focal set, geography cut, overlap window, response variables

## Day 3 — Literature & Variable Ontology

- [ ] Populate `01_literature_map/lit_matrix.csv` with key references
  - Healthy-range thresholds for each focal species
  - Degree-day literature per taxon
  - Habitat compression definitions from prior work
  - NC estuarine environmental baselines
- [ ] Complete `01_literature_map/variable_ontology.md`
  - Map every candidate variable to source, unit, expected role, and species relevance
- [ ] Define operational "healthy range" per focal target (requires literature + approval)
- [ ] Define habitat compression metric operationally (consecutive days, spatial fraction)
- [ ] Update `configs/project_config_template.yaml` with approved values from Day 2 decisions
- [ ] Write first entries in `decisions_log.md` for any Day 2 approvals

## Day 4–5 — ETL Pipeline (Preview)

- [ ] Build raw data download/ingestion scripts in `scripts/`
- [ ] Implement station-to-grid or station-to-estuary alignment
- [ ] QA/QC pass: flag missing data, outliers, unit inconsistencies
- [ ] Write pipeline README in `03_pipeline/`
- [ ] Add integration tests for data loading

## Day 6–7 — Feature Engineering (Preview)

- [ ] Implement healthy-range features per species
- [ ] Implement habitat compression features (event-based)
- [ ] Implement degree-day accumulation
- [ ] Implement watershed/forcing features
- [ ] Update `04_features/feature_catalog.md`
- [ ] Add unit tests for feature transforms

## Day 8–10 — Benchmarks & Primary Model (Preview)

- [ ] Implement all baseline models from benchmark registry
- [ ] Implement primary dynamic habitat model
- [ ] Run time-blocked validation
- [ ] Record results in `05_benchmarks/`

## Day 11–12 — Ablation & Robustness (Preview)

- [ ] Run single-feature ablations
- [ ] Run event-compression vs. mean-only comparison
- [ ] Run staged vs. direct watershed model comparison
- [ ] Document in `07_ablation_robustness/`

## Day 13–14 — Figures & Manuscript (Preview)

- [ ] Generate flagship habitat-compression-through-time figure
- [ ] Generate all planned figures from `08_figures/figure_plan.md`
- [ ] Draft manuscript sections per `09_manuscript/paper_outline.md`
- [ ] Final robustness and calibration checks
