# Assumptions Log — Trees to Seas v1

Track every assumption that the project depends on. Each assumption must be validated or revisited before the work that depends on it ships.

---

## ASM-001: Sufficient temporal overlap across data sources

**Date:** 2026-04-05 (Day 1)
**Assumption:** FerryMon, NOAA, USGS, Ty's GitHub feeds, fishery surveys, and habitat layers have enough temporal overlap for a meaningful multi-year analysis.
**Risk if wrong:** v1 overlap window may be very short (a few years), limiting statistical power and generalizability.
**Validation plan:** Day 2 data inventory will determine actual overlap. Human must approve minimum acceptable window.
**Status:** UNVALIDATED

---

## ASM-002: Fishery-independent surveys are usable as response variable

**Date:** 2026-04-05 (Day 1)
**Assumption:** NC fishery-independent survey data (e.g., NC DMF trawl surveys) can serve as a defensible response variable for blue crab and finfish targets.
**Risk if wrong:** Survey timing, gear selectivity, effort variation, and detectability may bias the response variable enough to undermine the modeling claim.
**Validation plan:** Day 2–3 literature review and data inspection. May need catch-per-effort standardization.
**Status:** UNVALIDATED

---

## ASM-003: Siltation/burial requires proxy variables

**Date:** 2026-04-05 (Day 1)
**Assumption:** No direct time-resolved sediment/burial dataset is available at useful temporal resolution for NC estuaries. Turbidity and runoff will serve as proxies.
**Risk if wrong:** If direct data exists, proxy approach may be unnecessarily imprecise. If proxies are too weak, sediment effects are unmodeled.
**Validation plan:** Day 2 data inventory search. Human approval required.
**Status:** UNVALIDATED

---

## ASM-004: Weekly temporal resolution is sufficient

**Date:** 2026-04-05 (Day 1)
**Assumption:** Estuary-cell-week or estuary-week is fine enough to capture biologically meaningful habitat compression events.
**Risk if wrong:** Some events (oxygen crashes, heat spikes) may be sub-weekly. Aggregation could blur critical episodes.
**Validation plan:** Inspect FerryMon and NOAA sampling frequency during Day 2. Consider daily resolution if data supports it.
**Status:** UNVALIDATED

---

## ASM-005: Seagrass layers update frequently enough for event-scale validation

**Date:** 2026-04-05 (Day 1)
**Assumption:** Seagrass extent or density data updates at least annually.
**Risk if wrong:** If seagrass data is episodic (every few years), event-scale habitat compression validation is not possible for this target.
**Validation plan:** Day 2 data inventory. May need to treat seagrass as annual trend only.
**Status:** UNVALIDATED

---

## ASM-006: Degree-day base temperatures are species-specific

**Date:** 2026-04-05 (Day 1)
**Assumption:** Literature provides defensible base temperatures for degree-day calculations for blue crab and the finfish target. Degree-days may not be useful for oyster or seagrass.
**Risk if wrong:** Using a wrong base temperature undermines the degree-day feature. Generic bases may add noise.
**Validation plan:** Day 3 literature review.
**Status:** UNVALIDATED

---

## ASM-007: Surface measurements are not valid proxies for bottom conditions in benthic taxa

**Date:** 2026-04-06 (Day 2)
**Assumption:** Bottom or near-bottom environmental measurements are required for blue crab, eastern oyster, and the finfish target. Surface readings are not valid stand-ins due to vertical stratification (salt wedge).
**Risk if wrong:** If bottom data are unavailable at required stations, the core variable set collapses. Fallback policies (e.g., surface-to-bottom correction models) would need development and approval.
**Validation plan:** Day 3 data inventory must confirm which sources provide bottom measurements vs. surface only. See DEC-007.
**Status:** UNVALIDATED

---

## ASM-008: CPUE is interpretable as a risk signal despite catchability confounds

**Date:** 2026-04-06 (Day 2)
**Assumption:** Standardized CPUE from fishery-independent surveys can serve as a defensible response variable even though CPUE may spike during compression events due to spatial crowding (the compression paradox).
**Risk if wrong:** If CPUE anomalies during compression events are primarily catchability artifacts rather than risk signals, the response variable may not be interpretable as claimed.
**Validation plan:** Literature review (REF-BC-06) and explicit discussion in methods. Consider whether CPUE direction during known compression events is consistent with risk interpretation.
**Status:** UNVALIDATED

---

## ASM-009: Oyster disease (Dermo) can be treated as a documented limitation rather than a modeled covariate

**Date:** 2026-04-06 (Day 2)
**Assumption:** *Perkinsus marinus* (Dermo) disease dynamics at high salinity + high temperature can be acknowledged in the paper without being explicitly modeled in v1, unless a clean time-aligned dataset is found.
**Risk if wrong:** Reviewers may demand disease confounding be addressed more directly. Treating high salinity as unconditionally "healthy" for oysters is incorrect if Dermo prevalence is high.
**Validation plan:** Day 3 data inventory search for Dermo prevalence data. Human must approve whether this is a modeled covariate or documented limitation.
**Status:** UNVALIDATED

---

## ASM-010: Temporal compression proxy is adequate without spatial interpolation

**Date:** 2026-04-06 (Day 2)
**Assumption:** Measuring compression as temporal squeeze at stations/cells (fraction of days outside healthy range) is adequate for the v1 central claim, even without full spatial interpolation of habitable area.
**Risk if wrong:** Reviewers may argue that temporal compression at fixed stations does not capture true spatial habitat loss. Spatial extension may be needed for a credible "habitat compression" claim.
**Validation plan:** Human must approve temporal-only default (DEC-008). If spatial extension is needed, Day 3 must confirm data density supports it.
**Status:** UNVALIDATED

---

<!-- TODO: Add new assumptions as they arise -->
<!-- Template:
## ASM-NNN: Title

**Date:**
**Assumption:**
**Risk if wrong:**
**Validation plan:**
**Status:** UNVALIDATED | VALIDATED | INVALIDATED | REVISED
-->
