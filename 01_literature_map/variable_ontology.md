# Variable Ontology — Trees to Seas v1 (Day 2)

## Project Logic

v1 remains a North Carolina estuarine proof-of-concept built to test one predictive claim only: whether species-specific habitat compression, derived from dynamic estuarine conditions, outperforms static annual or survey-timed summaries on held-out years. The pipeline blueprint from brief_v1.md is: watershed/weather forcing -> environmental state -> species response -> habitat-days/compression outputs.

The ontology stages variables rather than pooling them into one kitchen-sink model. This staging follows the DAG and is required for H3 testing (staged vs. direct models).

**Practical rule for v1:** Retain only variables that map cleanly to H1, H2, or H3 and can plausibly survive reviewer scrutiny on measurement, alignment, and interpretation. Mechanisms that are ecologically real but poorly observed at NC v1 scale are deferred or rejected.

## Variable Families

| Family | Meaning in v1 | Modeling Rule |
|---|---|---|
| Forcing | External watershed and weather drivers | Use mainly upstream of local state models for H3 |
| Local estuarine state | Direct environmental conditions organisms experience | Main explanatory layer for H1 |
| Habitat-condition | Physical context that shapes exposure severity | Use as modifiers/context, not as substitutes for state |
| Engineered features | Literature-backed summaries of exposure through time/space | Main H2 layer; secondary support for H1/B1 |
| Response | Observed biological or habitat endpoints | Use for evaluation; interpret as observational signals |
| Benchmark | Intentionally simple static or survey-timed covariates | Use only in baseline models testing the central claim |

---

## Approved Variables

### Forcing Variables (External Drivers)

| Variable | Unit | Source(s) | Temporal Res | Spatial Res | Hypotheses | Priority | Known Risks |
|---|---|---|---|---|---|---|---|
| Basin precipitation | mm/day or cumulative mm | NOAA weather/gridded products; Ty's feeds if documented | Daily | Watershed or sub-basin | H3 | Essential | Basin mismatch, lag uncertainty, localized storms missed |
| River discharge | cfs or m³/s | USGS stations | Daily | Gauge linked to estuary | H3 | Essential | Gauge not representative of receiving estuary, routing lag uncertain |
| Air temperature | °C | NOAA stations/products | Daily | Regional or estuary-nearby | H3, B1 | Essential | Poor proxy for benthic thermal exposure in complex shallows |
| Wind speed / direction | m/s; degrees | NOAA stations | Hourly to daily | Estuary or nearby station | H3 (support) | Useful | Local fetch/sheltering omitted; directionality oversimplified |

### Local Estuarine State Variables (Direct Environment)

| Variable | Unit | Source(s) | Temporal Res | Spatial Res | Hypotheses | Priority | Known Risks |
|---|---|---|---|---|---|---|---|
| Bottom water temperature | °C | FerryMon; NOAA; Ty's GitHub data | Sub-daily to daily | Station, transect, or cell | H1, B1 | Essential | Surface substitution invalid for benthic exposure |
| Bottom salinity | PSU/ppt | FerryMon; NOAA; USGS; Ty's GitHub data | Sub-daily to daily | Station, transect, or cell | H1, H3 | Essential | Surface salinity misses salt wedge and bottom conditions |
| Bottom dissolved oxygen | mg/L | FerryMon; NOAA; Ty's GitHub data | Sub-daily to daily | Station, deep channel, or cell | H1, H2 | Essential | Daytime sampling misses nighttime lows; bottom data sparse |
| Turbidity / clarity metric | NTU, Secchi depth, or Kd | FerryMon; Ty's GitHub data | Daily to weekly | Shallow stations, shoals | H1 (SAV), B2 | Essential for SAV; useful otherwise | Biofouling, sensor inconsistency, sediment-vs-algae ambiguity |
| Stratification metric | Delta salinity/temp or density proxy | NOAA/FerryMon where paired depths exist | Hourly to daily | Paired-depth stations | H2 (support), H3 (support) | Useful | Paired profile coverage may be too sparse |

### Habitat-Condition Variables (Physical Context)

| Variable | Unit | Source(s) | Temporal Res | Spatial Res | Hypotheses | Priority | Known Risks |
|---|---|---|---|---|---|---|---|
| Bathymetry / depth | m | Bathymetry and habitat layers | Static | Cell, transect, or polygon | H1 (support), H2 (support) | Essential | Vertical datum mismatch; coarse shallow-water resolution |
| Benthic habitat / substrate class | Categorical | Oyster, seagrass, and habitat layers | Static to episodic | Polygon or cell | H1 (support) | Useful | Outdated maps, inconsistent class definitions |
| Estuarine position / distance to inlet or river mouth | km or normalized position | Derived from GIS | Static | Station or cell | H1 (support), H3 (support) | Useful | Oversimplifies multi-inlet geometry |

### Engineered Features (Compression Metrics)

| Feature | Unit | Derived From | Hypotheses | Priority | Known Risks |
|---|---|---|---|---|---|
| Daily healthy / unsafe status | Binary or ordinal | State + habitat context + literature thresholds | H1, H2, H3 | Essential | Circular if thresholds are tuned to outcomes (DEC-005 forbids this) |
| Consecutive unsafe days | Days | Healthy/unsafe status | H2 | Essential | Sensitive to missing days and window choice |
| Habitat-days in healthy range | Days or fraction | Healthy/unsafe status | H1, H2 | Essential | Misalignment between exposure window and response date |
| Salinity excursion metric | Days out of bounds, variance, or max deviation | Bottom salinity + thresholds | H1, H3 | Useful | Window and lag choices can look arbitrary if not predeclared |
| Heat-event metric | Days above bound or cumulative exceedance | Bottom water temperature + thresholds | H1, B1 | Useful; essential for SAV | Easy reviewer attack if bound or accumulation rule is ad hoc |
| Hypoxia duration metric | Hours or days out of bounds | Bottom DO + thresholds | H1, H2 | Essential for blue crab and finfish | Coarse sampling misses short severe events |
| Degree-days | Accumulated °C·time | Water temperature | B1, H1 (secondary) | Useful | Can overfit simple seasonality; base-temperature choice vulnerable |
| Habitat compression metric (temporal) | Fraction unsafe, max run, or safe-area proportion | Multiple state variables + thresholds | H2 | Essential concept | Circularity risk; see definitions below |

### Response Variables

| Target | Response Variable | Unit | Source | Priority | Known Risks |
|---|---|---|---|---|---|
| Blue crab | Standardized survey CPUE, occurrence, or occupancy | Standardized CPUE | Fishery-independent survey data | Essential | CPUE can spike under crowding even when population is stressed |
| Eastern oyster | Live density, recruitment, or condition metric | TBD | Oyster monitoring/survey layers | Essential | Temporal frequency may be sparse; disease confounding |
| Estuarine finfish (candidate: Southern Flounder) | Standardized survey CPUE, occurrence, or occupancy | Standardized CPUE | Fishery-independent survey data | Essential once species approved | Species may fail overlap or standardization requirements |
| SAV / seagrass | Presence/absence, mapped extent, or condition class | TBD | Seagrass/SAV layers and habitat products | Essential if SAV retained | Temporal resolution may be too coarse for event attribution |

### Benchmark Variables (Baseline Models Only)

| Variable | Unit | Source | Purpose |
|---|---|---|---|
| Calendar / week-of-year / season | Date features or categories | Survey metadata | Captures seasonality without explicit ecology |
| Static estuary / management zone / fixed survey grid ID | Categorical | Survey design and GIS layers | Captures static spatial structure |
| Annual or seasonal mean state | Same as underlying state | Derived from state data | Static environmental summary comparator |
| Same-day survey snapshot state | Same as underlying state | Derived from state data | Survey-timed snapshot comparator |

---

## Deferred Variables

These are ecologically real but excluded from core v1 modeling due to measurement, alignment, or engineering constraints.

| Variable | Reason Deferred | Revisit Condition |
|---|---|---|
| Spatial / volumetric compression from full interpolation | Requires heavy interpolation assumptions; engineering risk too high for v1 | Day 3 shows sufficient spatial density and bottom-state coverage |
| Oyster disease covariates (e.g., Dermo prevalence) | Important for interpretation but no confirmed time-aligned NC dataset | Clean overlap found during Day 3 inventory |
| Localized fishing mortality / commercial effort | Important sensitivity covariate but spatially aligned effort data not confirmed | Spatially aligned effort data accessible |
| Chlorophyll-a / advanced optical partitioning | Simpler light-limitation pathway should be stabilized first | Basic clarity pathway stable and Chl-a data confirmed |
| Wave-energy / 3D hydrodynamic routing | Too much engineering and assumption load for v1 | Future work |

## Rejected Variables

These are excluded from v1 core and baseline models.

| Variable | Reason Rejected |
|---|---|
| Point-sampled nutrient concentrations (TN, TP, DIN) | Too sparse for dynamic weekly modeling |
| Direct sedimentation / burial rates / bottom shear stress | No high-frequency NC dataset confirmed |
| Static annual land-use percentage as direct biological predictor | Too static for H1; violates dynamic requirement |
| Surface-only salinity or DO as stand-in for benthic exposure | Invalid proxy for benthic taxa (oyster, crab, benthic finfish) |
| Any healthy-range threshold inferred retrospectively from model fit | Violates DEC-005 |

---

## DAG Summary

```
[Weather forcing: precip / air temp / wind]
                 |  \
                 v   v
   [Watershed runoff/discharge] ----\
                                     v
[Habitat context: depth/substrate/position] ---> [True local estuarine state]
                                                      /             \
                                                     v               v
                              [Measurement representation] --> [Observed estuarine state]
                                                                   |
                                                                   v
                  [Threshold library] ------------------------> [Derived habitat-days /
[Habitat context] ------------------------------------------->  compression metrics]
                                                                   |
                                                                   |  predictive proxy only
                                                                   v
[ Fishing mortality ] ----\                                 [Observed response]
[ Oyster disease ] ------- > [True species/habitat status] ----^
[ Habitat context ] -------/                                      |
[ True local state ] --------------------------------------------|
                                                                  ^
                                                [Survey / catchability process]
```

**Key distinction:** The edge from derived compression metrics to observed response is **not a causal claim** — it is the predictive test at the heart of the paper. Benchmark variables are omitted from the DAG because they are comparison devices, not mechanisms.

---

## Definitions to Finalize Before Feature Engineering

Templates only — **no numeric thresholds until literature sign-off.**

### Healthy Range

For species *s*, life stage *l*, location *i*, time *t*:
`Healthy_{s,l,i,t} = 1` if every required direct state variable lies within its literature-approved bound set for that species/life stage and the habitat context is admissible; otherwise `0`.

### Unsafe Habitat

`Unsafe_{s,l,i,t} = 1` when any acute bound is violated, or when a predeclared chronic-exposure rule is exceeded within the approved lookback window. Store the responsible variable class(es) for attribution.

### Habitat-Days

For a lookback window *W*:
`HabitatDays_{s,l,i,W} = sum over t in W of Healthy_{s,l,i,t}`
Report either raw days or proportion of days healthy.

### Habitat Compression

**Temporal v1 default:**
`CompressionTemporal_{s,l,i,W} = 1 - HabitatDays_{s,l,i,W} / |W|`
and report `MaxConsecutiveUnsafeDays_{s,l,i,W}` alongside it.

**Spatial extension (only if justified later):**
`CompressionSpatial_{s,l,t} = 1 - (sum_i a_i * Healthy_{s,l,i,t}) / (sum_i a_i)`
where `a_i` is an area or volume weight. For v1, temporal squeeze is the safer default.

### Missing-Data Rule

A feature window is computable only if minimum temporal coverage is met; event-scale gaps must not be silently filled.

### Response-Alignment Rule

Every response observation must carry its exact preceding exposure window, depth policy, and station/cell mapping before any model training begins.

---

## Concepts Needing Literature Sign-Off

- [ ] Species- and life-stage-specific healthy bounds for temperature, salinity, DO, and clarity/light
- [ ] Which state dimensions are required per taxon vs. assumed universally
- [ ] Degree-day base temperatures, accumulation start rules, and taxon-specific season reset logic
- [ ] Whether SAV target is specifically eelgrass (*Zostera marina*) or broader SAV class
- [ ] Accepted bottom-exposure policy: true bottom measurement, near-bottom proxy, or approved fallback
- [ ] Whether oyster disease must be modeled as sensitivity covariate or documented as limitation only
