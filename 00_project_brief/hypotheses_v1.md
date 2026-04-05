# Hypotheses — Trees to Seas v1

## Primary Hypotheses

### H1: Dynamic habitat models outperform static summaries

For each focal target, a model using time-varying temperature, salinity, dissolved oxygen, turbidity/light proxies, and degree-day features will outperform models based on static zones, season/calendar only, or annual-average environmental covariates in held-out prediction of standardized survey response or habitat condition.

- **Benchmark:** Time-blocked out-of-sample comparison against prespecified static baselines.
- **Failure condition:** Reject H1 if the best dynamic model does not beat the best static baseline on the primary metric.

### H2: Habitat compression is more informative than mean conditions

Event-based habitat compression metrics (e.g., fraction of area or time outside a species-specific healthy range for at least k consecutive days) will predict within-season downturns better than contemporaneous mean conditions alone.

- **Benchmark:** Compare event-feature models against mean-only models.
- **Failure condition:** Reject H2 if compression features provide no stable incremental skill across held-out years.

### H3: Watershed/weather forcing matters mainly through local estuarine state

Models that route rainfall, runoff, land-use, and disturbance variables through estuarine water-condition features will match or outperform direct species models that use watershed/weather predictors as unrestricted inputs.

- **Benchmark:** Compare watershed-only, estuarine-state-only, combined direct, and staged models.
- **Failure condition:** Reject H3 if staged modeling yields no performance or interpretability advantage.

## Backup Hypotheses

### B1: Degree-days are taxon- and life-stage-specific rather than universally useful

Degree-day features will improve prediction for blue crab and the finfish target more than for oyster or seagrass, and may add little once temperature extremes are already modeled.

### B2: Sediment/disturbance proxies matter most for benthic and habitat-forming targets

Adding turbidity, runoff, land-disturbance, and any direct burial/sediment proxies will improve risk prediction for oyster and seagrass more than for the mobile targets.

## Success Criterion

Support the central paper claim only if the dynamic habitat model beats the best static baseline on held-out data, remains reasonably calibrated, and retains its advantage under key mechanism ablations.

## Reporting Rule

Every claimed gain must be reported with uncertainty and a short failure note describing where it does not hold.
