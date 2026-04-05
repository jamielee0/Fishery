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

## Day 2 (Complete)

- [x] Encode literature/mechanism matrix into `01_literature_map/lit_matrix.csv`
- [x] Build full variable ontology with staging (forcing, state, habitat, engineered, response, benchmark)
- [x] Write reviewer notes with anticipated objections and robustness plan
- [x] Create trait tables for all 4 focal targets (blue crab, oyster, finfish, SAV)
- [x] Build species config YAMLs in `configs/species/`
- [x] Build source registry in `configs/sources/source_registry.yaml`
- [x] Build feature registry in `configs/features/feature_registry.yaml`
- [x] Create working project config `configs/project_config.yaml` with approved/proposed/deferred classification
- [x] Create reference stubs for all needed literature citations
- [x] Add Day 2 decisions to decisions log (DEC-006 through DEC-011)
- [x] Add Day 2 assumptions to assumptions log (ASM-007 through ASM-010)
- [x] Update issue board for Day 3

## Day 3 — Source Inventory & Overlap Audit

**Goal:** Confirm what data actually exists, what can be accessed, and what the real temporal overlap is. Do NOT start modeling or feature engineering.

### Source Access Confirmation
- [ ] FerryMon: Locate URL/API endpoint, confirm access, test download, document variables and measurement depth (surface vs. bottom)
- [ ] NOAA estuarine stations: Identify all NC estuarine stations with bottom sensors, confirm API access, test download
- [ ] USGS stations: Identify gauges linked to NC estuarine receiving waters, confirm daily discharge access
- [ ] Ty's GitHub data: Locate repo URL, catalog variables, document provenance and temporal coverage
- [ ] Fishery-independent surveys (NCDMF): Confirm data access method (public download vs. data request), document gear, effort, species, and survey timing
- [ ] Oyster monitoring: Identify NC oyster monitoring programs, confirm data source, document temporal resolution
- [ ] SAV/seagrass layers: Identify NC SAV mapping programs, confirm data source, document vintage and temporal resolution
- [ ] Bathymetry and habitat layers: Confirm source and spatial resolution
- [ ] NOAA weather: Confirm precipitation and air temperature data for NC coastal region

### Overlap Audit
- [ ] For each confirmed source, record: temporal range, temporal resolution, spatial coverage, spatial resolution, variables measured, measurement depth
- [ ] Build overlap matrix: which sources overlap in time and space?
- [ ] Determine actual overlap window start and end dates
- [ ] Identify the minimum viable overlap window and get human approval
- [ ] Flag any source that has <5 years of overlap with the core environmental data

### Focal Target Confirmation
- [ ] Confirm or reject Southern Flounder as finfish target based on actual NCDMF survey overlap with environmental data
- [ ] Confirm SAV species (*Zostera marina* vs. *Halodule wrightii* vs. broader class) based on NC data availability
- [ ] Confirm primary response variable for each target based on what data actually exists
- [ ] Assess whether SAV temporal resolution supports event-scale attribution or annual-trend-only analysis (ASM-005)

### Depth & Measurement Audit
- [ ] For each environmental station: record whether measurements are surface, bottom, or paired-depth
- [ ] Flag stations where only surface data exists for variables needed at bottom (ASM-007)
- [ ] Propose depth policy and fallback rule for human approval

### Human Approvals Required After Day 3
- [ ] Approve minimum overlap window
- [ ] Approve finfish target (Southern Flounder or alternative)
- [ ] Approve SAV species
- [ ] Approve primary response variable per target
- [ ] Approve depth/bottom-exposure policy
- [ ] Approve whether B2 is formally deferred
- [ ] Approve whether Dermo disease is a modeled covariate or documented limitation
- [ ] Approve temporal station-based compression as v1 default (DEC-008)

### Deliverables
- [ ] Updated `02_data_inventory/data_inventory.csv` with real values
- [ ] Updated `02_data_inventory/access_tracker.md` with confirmed access status
- [ ] Overlap matrix visualization or table
- [ ] Updated `configs/project_config.yaml` with confirmed date ranges and source paths
- [ ] Updated `configs/sources/source_registry.yaml` with confirmed access details

## Day 4–5 — ETL Pipeline

- [ ] Build raw data download/ingestion scripts in `scripts/`
- [ ] Implement station-to-grid or station-to-estuary alignment
- [ ] QA/QC pass: flag missing data, outliers, unit inconsistencies
- [ ] Apply depth policy from Day 3 approval
- [ ] Write pipeline README in `03_pipeline/`
- [ ] Add integration tests for data loading

## Day 6–7 — Feature Engineering

- [ ] Implement healthy-range features per species (requires Day 3 literature thresholds)
- [ ] Implement habitat compression features (temporal, event-based)
- [ ] Implement degree-day accumulation with approved base temperatures
- [ ] Implement watershed/forcing features
- [ ] Implement response-alignment rule (exposure window -> survey event)
- [ ] Update `04_features/feature_catalog.md`
- [ ] Add unit tests for feature transforms

## Day 8–10 — Benchmarks & Primary Model

- [ ] Implement all baseline models from benchmark registry
- [ ] Implement primary dynamic habitat model
- [ ] Run time-blocked validation
- [ ] Record results in `05_benchmarks/`

## Day 11–12 — Ablation & Robustness

- [ ] Run single-feature ablations
- [ ] Run event-compression vs. mean-only comparison (H2)
- [ ] Run staged vs. direct watershed model comparison (H3)
- [ ] Document in `07_ablation_robustness/`

## Day 13–14 — Figures & Manuscript

- [ ] Generate flagship habitat-compression-through-time figure
- [ ] Generate all planned figures from `08_figures/figure_plan.md`
- [ ] Draft manuscript sections per `09_manuscript/paper_outline.md`
- [ ] Final robustness and calibration checks
