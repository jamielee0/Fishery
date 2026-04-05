# Reviewer Notes — Trees to Seas v1 (Day 2)

Consolidated reviewer-perspective notes from Day 2 science review. These notes anticipate likely peer-review objections and inform the robustness plan in `07_ablation_robustness/reviewer_attack.md`.

**Source:** Gemini Day 2 reviewer output, cross-checked against Day 1 approved hypotheses and brief.

---

## Strongest Mechanisms for v1

### 1. The Hypoxia-Temperature Squeeze (Blue Crab & Finfish)

Canonical, ecologically verified mechanism for habitat compression in NC (especially Neuse River Estuary and Pamlico Sound). Bottom DO dropping below ~2.0 mg/L acts as a hard physical boundary, forcing mobile taxa into warmer shallows. Perfectly operationalizes H1 and H2.

### 2. Osmotic Stress / Freshening (Oysters)

Extreme runoff events driving prolonged salinity drops provide a massive, highly measurable signal for eastern oyster mortality. Clear, defensible pathway for H3 (Watershed Forcing -> Estuarine State -> Species Response).

### 3. Thermal Limits (Seagrass)

Eelgrass (*Zostera marina*) in NC is at its southern thermal limit. Prolonged summer heat provides a powerful, direct predictor for physiological dieback. Pristine habitat-condition target — if SAV is confirmed as the habitat indicator.

---

## Weakest or Most Weakly Measurable Mechanisms

### 1. Sediment Loading / Physical Burial (B2)

Scientifically real, but continuous spatial data on bottom sedimentation across NC estuaries is practically nonexistent. Interpolating from basic wind/flow proxies will look fabricated to a reviewer.

**Recommendation:** Defer B2 from active v1 implementation. Turbidity remains as a light-limitation proxy for SAV only.

**Conflict note:** Day 1 hypotheses_v1.md lists B2 as a backup hypothesis. Deferral is proposed, not yet approved. Human must decide.

### 2. Direct Nutrient Loading

Biogeochemical cascade (Nutrients -> Algae -> Decay -> Hypoxia) introduces massive temporal lags and nonlinearities. Point-in-time grab samples of TN/TP are too sparse for dynamic weekly modeling.

**Status:** Rejected from core v1 variable set per ontology.

---

## Critical Reviewer Concerns

### RC-1: Catchability vs. Abundance (The Compression Paradox)

Fishery-independent surveys measure CPUE. When hypoxia forces crabs and fish into shallow margins, a survey trawl in those margins sees an artificial **spike** in CPUE due to spatial crowding, even as the population is stressed. Reviewers will demand this non-linear "catchability" dynamic be addressed.

**Implication for v1:** Must acknowledge in methods and discussion. Consider whether CPUE spikes during compression events are interpretable as risk signals or confounds. This does not invalidate the modeling — compression-driven CPUE anomalies are themselves a signal of habitat stress — but language must be precise.

### RC-2: Vertical Stratification (The Salt Wedge)

Oysters, crabs, and flounder live on the bottom. FerryMon and satellites often measure surface conditions. Using surface salinity/DO to predict benthic species without explicitly acknowledging vertical stratification will be rejected.

**Implication for v1:** Bottom measurements must be prioritized. Where only surface data exist, the depth policy must be explicit and documented. See ASM-007 (new assumption).

### RC-3: High-Salinity Disease Dynamics

Oysters die from freshets, but also from *Perkinsus marinus* (Dermo) when salinity and temperature are both high. Treating high salinity as unconditionally "healthy" ignores lagged disease mortality.

**Implication for v1:** Oyster disease is a deferred variable. Must be documented as a known limitation. If a clean, time-aligned Dermo prevalence dataset surfaces during Day 3, consider adding as sensitivity covariate.

### RC-4: Fishing Mortality

Blue crab and finfish are heavily exploited. Decreases in CPUE could reflect localized commercial harvest, not habitat compression.

**Implication for v1:** Fishing mortality is a deferred variable. Must be documented as a known confounder. Spatially aligned commercial effort data would be needed to address directly.

---

## Variable Class Staging (Required for Peer Review)

To survive review, variable classes must be explicitly staged, not mixed in a kitchen-sink model:

1. **Forcing variables (External Drivers):** Basin precipitation, air temperature, wind speed/fetch, USGS river discharge
2. **Estuarine state variables (Direct Environment):** Bottom water temperature, bottom salinity, bottom DO, turbidity
3. **Habitat-condition variables (Physical Context):** Bathymetry/depth, benthic substrate type, proximity to shoreline/inlet
4. **Engineered features (Compression Metrics):** Consecutive days DO < threshold, temporal variance of salinity, cumulative degree-days, % of spatial area within safe bounds
5. **Species-response variables (Targets):** Standardized survey CPUE, live-oyster density, SAV mapped presence/absence

This staging directly supports the H3 comparison (staged vs. direct models).

---

## Must-Keep Variables (Minimum Viable Set)

- **Forcing:** River discharge (USGS), cumulative precipitation
- **State:** Bottom water temperature, bottom salinity, bottom DO
- **Response:** Standardized survey CPUE, SAV spatial extent
- **Engineered:** Mathematically defined temporal/spatial compression features

## Defer-for-Later Variables

- Nutrient concentrations (TN, TP)
- Sediment burial / accretion metrics
- 3D hydrodynamic wave-energy routing
- Oyster disease prevalence
- Fishing mortality / effort

## Reject-Now Variables

- Point-sampled nutrients as core weekly predictors
- Direct sedimentation rates (no data)
- Static annual land-use as direct H1 predictor
- Surface-only state as benthic proxy
- Retrospectively tuned thresholds (DEC-005)
