# Reviewer Attack Surface — Trees to Seas v1

Anticipate likely reviewer objections and pre-build robustness checks.

<!-- TODO: Expand during Day 11–12 -->

## Ablation Studies

Remove one feature group at a time and report impact on primary metric:

1. Remove temperature
2. Remove salinity
3. Remove dissolved oxygen
4. Remove turbidity/light
5. Remove degree-days
6. Remove watershed forcing
7. Remove habitat layers

## Head-to-Head Comparisons

- Event-based compression features vs. mean-only features
- Staged model (watershed -> estuarine -> species) vs. direct model (all inputs unrestricted)

## Likely Reviewer Objections

| # | Objection | Pre-emptive Response Plan |
|---|---|---|
| 1 | "Random CV inflates performance" | We use time-blocked validation only. Show random CV for reference but do not claim from it. |
| 2 | "Healthy ranges are post hoc" | Ranges defined from literature before modeling. Document in `decisions_log.md`. |
| 3 | "Correlation ≠ causation" | Claim language is predictive/associative only. Mechanistic consistency is discussed, not asserted. |
| 4 | "Only one geography" | Acknowledged as NC proof-of-concept. Generalization is future work. |
| 5 | "Survey data is biased" | Discuss gear, timing, effort, detectability. Sensitivity test with subsets if possible. |
| 6 | "Short overlap window" | Report exact window. Discuss power limitations honestly. |
| 7 | "Degree-days add nothing once temperature is in the model" | Ablation B1 tests this directly. Report either way. |
| 8 | "Seagrass data too coarse for event-scale" | Acknowledge if true. May limit seagrass to annual trend analysis. |

## Calibration Checks

- Reliability diagrams for probabilistic outputs
- Coverage of prediction intervals
- Sharpness vs. calibration trade-off

## Sensitivity Checks

- Sensitivity to healthy-range threshold choices (±10% perturbation)
- Sensitivity to analysis unit (cell-week vs. estuary-week)
- Sensitivity to held-out year selection
