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

<!-- TODO: Add new assumptions as they arise -->
<!-- Template:
## ASM-NNN: Title

**Date:**
**Assumption:**
**Risk if wrong:**
**Validation plan:**
**Status:** UNVALIDATED | VALIDATED | INVALIDATED | REVISED
-->
