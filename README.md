# Trees to Seas

**Dynamic estuarine habitat and fishery risk modeling — North Carolina proof-of-concept (v1)**

## Research Question

> Can species-specific habitat compression derived from dynamic North Carolina estuarine conditions predict focal-species risk better than static zones, fixed survey timing, or annual-average summaries?

## Central Claim

Species-specific habitat compression estimated from dynamic water conditions provides a better out-of-sample and forecast-ready management signal than static annual or survey-timed summaries in North Carolina estuarine systems.

## Focal Targets (v1)

| Target | Type | Status |
|---|---|---|
| Blue crab (*Callinectes sapidus*) | Mobile crustacean | Confirmed |
| Eastern oyster (*Crassostrea virginica*) | Sessile bivalve | Confirmed |
| TBD estuarine finfish | Finfish | Pending data overlap review |
| Seagrass (species TBD) | Habitat indicator | Pending confirmation |

## Key Environmental Variables

Temperature, salinity, dissolved oxygen, turbidity/light proxies, degree-days, and watershed forcing signals.

## Repo Structure

```
00_project_brief/       Project brief, hypotheses, scope lock
01_literature_map/      Literature matrix, variable ontology
02_data_inventory/      Data inventory, access tracking
03_pipeline/            ETL pipeline code and documentation
04_features/            Feature engineering and catalog
05_benchmarks/          Benchmark registry and baseline results
06_models/              Primary and fallback model specifications
07_ablation_robustness/ Ablation studies and robustness checks
08_figures/             Figure plan and generated outputs
09_manuscript/          Paper outline and drafts
configs/                Project configuration templates
tests/                  Test suite
data/                   Raw / intermediate / processed (not committed)
docs/                   Developer and onboarding documentation
scripts/                Utility and runner scripts
```

## Quick Start

```bash
# Option A: conda
conda env create -f environment.yml
conda activate trees-to-seas

# Option B: pip
pip install -e ".[dev,ml]"
```

## Running Tests

```bash
pytest
# or
make test
```

## Project Management

- **issue_board.md** — Sprint task board
- **decisions_log.md** — Architectural and scientific decisions
- **assumptions_log.md** — Tracked assumptions requiring validation

## Validation Strategy

- Time-blocked held-out years (no random CV alone)
- Estuary holdout as secondary strategy if sample size permits
- Uncertainty and calibration required for any risk/forecast output
- Every claimed gain reported with uncertainty and failure notes

## v1 Scope Rules

- North Carolina only. Great Lakes is context, not modeling geography.
- One central paper claim only.
- Observational, benchmarked modeling paper — not a management platform.
- No fabricated data. No fake results.
- Conservative claim language: predictive, associative, forecast-ready — not causal.

## Day 1 Definition of Done

- [x] Repo tree created with all sprint folders
- [x] Config template with geography, species, date ranges, sources, validation, benchmarks
- [x] Tests scaffolding in place
- [x] Issue board with Day 2–3 tasks
- [x] Decisions log, assumptions log initialized
- [x] Brief and hypotheses committed
- [x] README sufficient for next contributor to orient without questions
- [x] No fabricated data or results anywhere in repo
