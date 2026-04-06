# Paper Outline — Trees to Seas v1

> **This repo is scaffold and configuration only. No manuscript text exists yet.**

<!-- TODO: Draft sections during Day 13–14 -->

## Title (working)

"Dynamic habitat compression predicts estuarine species risk better than static summaries: a Pamlico Sound and Neuse River Estuary proof-of-concept"

## Abstract

<!-- TODO: Write last, after results are final -->

## 1. Introduction

- Managed fisheries can still experience unexpected declines
- Great Lakes collapse as motivating context (warning, not modeling domain)
- Static-water framing may miss dynamic habitat loss
- Research question: Can dynamic habitat compression predict species risk better than static summaries?
- Contribution: first benchmarked test of temporal compression-based risk signals in NC estuaries

## 2. Study System

- Pamlico Sound and Neuse River Estuary geography
- Focal species: blue crab, eastern oyster, Southern Flounder
- Habitat indicator: seagrass/SAV (annual/episodic resolution; not event-scale)
- Key environmental drivers: temperature, salinity, DO, turbidity, degree-days
- Data density: Program 195, FerryMon, ModMon, NERRS, AVPs

## 3. Data

- Data sources (FerryMon, NOAA, USGS, NCDMF surveys, habitat layers)
- Temporal and spatial coverage within the pilot sub-systems
- Analysis unit and alignment
- Limitations and caveats (SAV temporal resolution, survey catchability)

## 4. Methods

### 4.1 Healthy-range definitions (literature-sourced, DEC-005)
### 4.2 Temporal habitat compression metrics (station-based; spatial interpolation deferred)
### 4.3 Feature engineering
### 4.4 Baseline models
### 4.5 Primary model
### 4.6 Validation strategy (time-blocked)
### 4.7 Ablation and robustness design

## 5. Results

### 5.1 Benchmark comparison (H1)
### 5.2 Temporal compression vs. mean conditions (H2)
### 5.3 Staged vs. direct watershed models (H3)
### 5.4 Ablation results
### 5.5 Calibration and uncertainty

## 6. Discussion

- What the results mean for the central claim
- Where the model fails and why
- SAV as annual/episodic indicator: interpretation limits
- Catchability paradox: CPUE under compression events
- Limitations: pilot geography, observational design, data constraints
- Implications for management signals
- Future work: spatial compression extension, other geographies, operational forecasting

## 7. Conclusion

- One-paragraph summary of the tested claim and result

## References

## Supplementary Material
