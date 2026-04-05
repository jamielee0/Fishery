# Onboarding — Trees to Seas v1

## What is this project?

A 14-day sprint to build a benchmarked North Carolina proof-of-concept testing whether dynamic habitat compression predicts estuarine species risk better than static summaries.

## How to get started

1. Read `README.md` for project overview
2. Read `00_project_brief/brief_v1.md` for the full brief
3. Read `00_project_brief/hypotheses_v1.md` for what we're testing
4. Check `issue_board.md` for current sprint tasks
5. Check `decisions_log.md` and `assumptions_log.md` for context

## Environment setup

```bash
conda env create -f environment.yml
conda activate trees-to-seas
pytest  # verify everything works
```

## Where things live

| What | Where |
|---|---|
| Project config | `configs/project_config_template.yaml` |
| Data schemas | `configs/schemas/` |
| Tests | `tests/` |
| Raw data (not committed) | `data/raw/` |
| Pipeline code | `03_pipeline/` and `scripts/` |
| Task board | `issue_board.md` |

## Key rules

- No fabricated data. No fake results.
- Time-blocked validation only (no random CV as primary).
- Conservative claim language (predictive, not causal).
- Every decision in `decisions_log.md`. Every assumption in `assumptions_log.md`.
