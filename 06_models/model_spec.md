# Model Specification — Trees to Seas v1

<!-- TODO: Complete during Day 8–10 -->

## Primary Model: Dynamic Habitat Compression

**Objective:** Predict focal-species response using dynamic environmental state and habitat compression features.

**Architecture:** TBD (candidate: staged model routing watershed forcing through estuarine state, then to species response with compression features)

**Input features:** See `04_features/feature_catalog.md`

**Output:** Species-specific risk/response prediction with calibrated uncertainty

**Training:** All data except held-out years

**Validation:** Time-blocked held-out years (see `configs/project_config_template.yaml`)

## Fallback Model

If the primary model architecture proves too complex for the data:
- Fall back to conventional GAM with compression features added as covariates
- Document in `decisions_log.md` why the fallback was needed

## Model Comparison Protocol

1. Train each baseline and the primary model on the same training set
2. Evaluate on the same held-out years
3. Report primary metric, calibration, and uncertainty for all models
4. Run ablations on the primary model (see `07_ablation_robustness/`)
5. Accept central claim only if primary model beats best baseline and survives ablations
