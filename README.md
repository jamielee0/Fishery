# Trees to Seas

> **This repo is scaffold and configuration only. No pipeline code, no model code, no data, and no results exist yet. Nothing here is runnable science.**

**Dynamic estuarine habitat and fishery risk modeling — Pamlico Sound and Neuse River Estuary proof-of-concept (v1)**

## Research Question

> Can species-specific habitat compression derived from dynamic North Carolina estuarine conditions predict focal-species risk better than static zones, fixed survey timing, or annual-average summaries?

## Central Claim

Species-specific habitat compression estimated from dynamic water conditions provides a better out-of-sample and forecast-ready management signal than static annual or survey-timed summaries in North Carolina estuarine systems.

## Focal Targets (v1) — Locked

| Target | Scientific Name | Type | Primary Mechanism |
|---|---|---|---|
| Blue crab | *Callinectes sapidus* | Mobile crustacean | Hypoxia-temperature squeeze |
| Eastern oyster | *Crassostrea virginica* | Sessile bivalve | Osmotic stress from freshening |
| Southern Flounder | *Paralichthys lethostigma* | Estuarine finfish | Hypoxia-temperature squeeze |
| Seagrass / SAV | Species TBD at Day 3 | Habitat indicator | Thermal limits and light limitation |

Southern Flounder is the approved finfish target. SAV role is locked as an annual/episodic habitat indicator (not an event-scale target on par with the mobile species); the exact species (*Zostera marina* vs. *Halodule wrightii*) is a Day 3 decision because thresholds differ dramatically between candidates.

## Key Environmental Variables

Temperature, salinity, dissolved oxygen, turbidity/light proxies, degree-days, and watershed forcing signals.

## Repo Structure

```
00_project_brief/       Project brief, hypotheses, scope lock
01_literature_map/      Literature matrix, variable ontology, trait tables
02_data_inventory/      Data inventory, access tracking
03_pipeline/            ETL pipeline code and documentation
04_features/            Feature engineering and catalog
05_benchmarks/          Benchmark registry and baseline results
06_models/              Primary and fallback model specifications
07_ablation_robustness/ Ablation studies and robustness checks
08_figures/             Figure plan and generated outputs
09_manuscript/          Paper outline and drafts
configs/                Project configuration and species/source/feature registries
tests/                  Test suite
data/                   Raw / intermediate / processed (not committed)
docs/                   Developer and onboarding documentation
scripts/                Utility and runner scripts
refs/                   Literature reference stubs
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

- Pamlico Sound and Neuse River Estuary pilot. Great Lakes is context, not modeling geography.
- One central paper claim only.
- Observational, benchmarked modeling paper — not a management platform.
- No fabricated data. No fake results.
- Conservative claim language: predictive, associative, forecast-ready — not causal.

## What This Repo Contains Today

Scaffold only: directory structure, configuration templates, trait tables, variable ontology, reviewer notes, reference stubs, and test suite. All numeric thresholds are null pending literature sign-off (DEC-005). All data source paths are null pending Day 3 inventory. No code runs a model. No code fetches data.
