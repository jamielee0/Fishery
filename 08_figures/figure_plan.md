# Figure Plan — Trees to Seas v1

> **This repo is scaffold and configuration only. No figures exist yet.**

<!-- TODO: Generate figures during Day 13–14 -->

## Flagship Figure

**Fig 1: Habitat compression through time**
- Show temporal compression fraction and consecutive-unsafe-days over time for one or more focal targets at representative stations
- Temporal panel showing when compression events happen within and across years
- Station-level or cell-level time series, NOT spatially interpolated maps (DEC-008: spatial compression is DEFERRED)

## Supporting Figures

**Fig 2: Study area and data coverage**
- Map of Pamlico Sound and Neuse River Estuary with station locations
- Temporal coverage bars for each data source

**Fig 3: Species-specific healthy ranges**
- Multi-panel: one per focal target (blue crab, eastern oyster, Southern Flounder; SAV as annual/episodic panel)
- Show environmental variable distributions with healthy-range thresholds overlaid

**Fig 4: Benchmark comparison**
- Bar or dot plot: primary metric for each baseline and the primary model
- Include uncertainty intervals
- Held-out data only

**Fig 5: Ablation results**
- Heatmap or bar chart: performance change when each feature group is removed
- One panel per focal target

**Fig 6: Calibration**
- Reliability diagram for primary model
- Coverage plot for prediction intervals

## Supplementary Figures

- S1: Raw time series for key environmental variables at representative stations
- S2: Feature importance or variable attribution
- S3: Sensitivity to healthy-range threshold perturbation
- S4: Random CV vs. time-blocked comparison (showing why random CV is misleading)
