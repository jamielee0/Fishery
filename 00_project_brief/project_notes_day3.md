# Project Notes — Day 3 (2026-04-08)

## What Changed from the Original Story After Looking at Real Data

The Day 1-2 scaffold assumed all nine data sources would be locatable, accessible, and
provide the variables listed in the variable ontology. Desktop research on Day 3 reveals
a more constrained reality:

1. **The bottom-data assumption was optimistic.** The variable ontology lists FerryMon as
   a source for "bottom water temperature," "bottom salinity," and "bottom dissolved
   oxygen." FerryMon is a flow-through system on ferry hulls — it measures **surface
   water only** (~1-1.5m depth). This directly conflicts with DEC-007 (bottom
   measurements required for benthic taxa). The project's most spatially extensive
   estuarine monitoring source cannot serve the primary modeling need.

2. **Ty's GitHub data is the linchpin, and it cannot be located.** The variable ontology
   and brief both reference "Ty's GitHub environmental data" as a source for bottom
   measurements. No URL, provider name, or variable catalog exists anywhere in the repo.
   If this source is a compilation of ModMon/AVP bottom profiles (as DEC-012's mention
   of those programs suggests), it would fill the critical gap. But without locating it,
   the bottom-data requirement for all three benthic species is unmet.

3. **NOAA NERRS spatial coverage may miss the study area.** NC NERRS stations are
   associated with reserve components (Rachel Carson near Beaufort). These may be near
   inlets rather than inside Pamlico Sound or the Neuse River Estuary proper. If so,
   NERRS provides no direct environmental monitoring for the study area.

4. **SAV temporal resolution is worse than assumed.** NC SAV mapping relies on episodic
   aerial/satellite campaigns with multi-year gaps. Even "annual indicator" status
   (DEC-013) may be generous if campaigns are >5 years apart. The Day 3 species
   selection (*Zostera* vs. *Halodule*) cannot proceed without knowing campaign dates.

5. **Oyster response data is entirely unconfirmed.** No provider, access method, temporal
   range, or temporal resolution has been verified. Event-scale compression analysis for
   oysters may not be feasible.

6. **Fishery-independent survey access requires a formal NCDMF request** that has not
   been submitted. This is the primary response variable for 2 of 4 targets. Lead time
   is unknown.

7. **The overlap window is not yet definable.** Without confirming Ty's GitHub temporal
   range and NERRS station availability, the overlap window start date cannot be set.
   The optimistic estimate is ~2003-2024 (~21 years); the conservative estimate is
   ~2007-2023 (~16 years); the worst case is undefined.

---

## Confirmed Sources

These sources are known to exist based on established federal/state programs. Access
has NOT been tested, but the programs are real and public (or semi-public).

| Source | Provider | Confidence | Key Limitation |
|---|---|---|---|
| USGS streamflow | USGS (NWIS) | HIGH | Forcing only — not in-estuary |
| NOAA weather | NOAA NCEI | HIGH | Forcing only — not water data |
| FerryMon | UNC-IMS | HIGH (exists) | **Surface only — cannot satisfy DEC-007** |
| NCDMF Program 195 | NCDMF | HIGH (exists) | **Request-only access — not yet submitted** |
| Bathymetry | NOAA NCEI | HIGH (exists) | Static; vintage and datum concerns |

---

## Risky Sources

| Source | Risk | Impact if Unavailable |
|---|---|---|
| **Ty's GitHub** | Cannot locate — no URL, no provider, no variables | Collapses bottom-data requirement for all benthic species (DEC-007). Project cannot proceed as designed. |
| **NOAA NERRS** | Stations may not be inside study area; bottom sondes unconfirmed | Loses potential fallback for bottom environmental data |
| **Oyster monitoring** | Provider, access, and temporal resolution all unknown | Eastern oyster target becomes unsupportable |
| **SAV layers** | Episodic campaigns with multi-year gaps | SAV may be unsupportable even as annual indicator |
| **FerryMon** | Surface-only (confirmed) | Cannot serve as bottom-data source despite broad spatial coverage |

---

## Human Approvals Needed Today

### CRITICAL (blocks all further work)

1. **Ty's GitHub repo URL** — Provide the URL for "Ty's GitHub environmental data."
   If this source does not exist or is not available, we need to know immediately so
   alternative bottom-data sources (ModMon, AVPs) can be evaluated.

2. **NCDMF Program 195 data request** — Has a formal data request been submitted to
   NCDMF for fishery-independent survey data? If not, this must be initiated today.
   Lead time is unknown and may take weeks.

### HIGH PRIORITY

3. **Depth fallback policy** — DEC-007 requires bottom data, but no bottom source is
   confirmed. Options:
   - (a) Wait for Ty's GitHub / NERRS confirmation before proceeding
   - (b) Approve a documented fallback (e.g., surface-to-bottom correction model using
     stratification proxies) with explicit caveats in the paper
   - (c) Accept that some stations may be surface-only and flag this as a known
     limitation rather than a disqualifier
   **Recommend option (a) with a deadline, falling back to (c) if unresolved by Day 5.**

4. **Oyster monitoring source** — Identify the NC oyster monitoring program and data
   custodian, or approve downgrading Eastern oyster from "event-scale target" to
   "annual-trend indicator" (similar to SAV under DEC-013).

5. **SAV species selection** — Cannot proceed until SAV mapping campaign dates are known.
   If campaigns are too sparse, SAV target may need to be formally downgraded or
   dropped. Preliminary recommendation based on NC coverage: *Halodule wrightii*
   (shoalgrass) is the pragmatic choice over *Zostera marina* (eelgrass) because
   *H. wrightii* is more widespread in Pamlico Sound and more thermally tolerant.
   *Z. marina* is at its southern range limit and may have very limited current extent.

### MEDIUM PRIORITY

6. **Overlap window approval** — Once blockers 1-2 are resolved, approve the minimum
   viable overlap window. Current best estimate: ~2003-2024 (optimistic) or
   ~2007-2023 (conservative).

7. **Dermo disease treatment** — Approve whether *Perkinsus marinus* is a modeled
   sensitivity covariate or a documented limitation only (ASM-009). No Dermo prevalence
   dataset has been identified.

---

## Open Day 3 Decisions Still Pending

| Decision | Status | Blocked By |
|---|---|---|
| Approve minimum overlap window | BLOCKED | Ty's GitHub; NERRS station confirmation |
| Select SAV species | BLOCKED | SAV campaign dates unknown |
| Approve response variable per target | PARTIALLY BLOCKED | P195 data request not submitted; oyster source unconfirmed |
| Approve depth fallback policy | NEEDS HUMAN INPUT | Ty's GitHub; NERRS bottom sondes |
| Approve Dermo treatment | NEEDS HUMAN INPUT | No dataset identified |
| Assess SAV annual-trend viability | BLOCKED | SAV campaign dates unknown |

---

## What We Can Do vs. What We Cannot

**CAN do now (no blockers):**
- Finalize USGS gauge list (public data, well-documented)
- Select NOAA weather product (station vs. gridded)
- Confirm NOAA bathymetry product
- Document FerryMon as surface-only and note its value as a spatial coverage layer
  (even if not usable for bottom data, FerryMon surface transects are valuable for
  surface state and turbidity)

**CANNOT do until human input:**
- Set the overlap window
- Finalize the bottom-data source list
- Select SAV species
- Confirm response variables for oyster and SAV targets
- Start ETL (Day 4-5 task — correctly blocked by Day 3 gaps)
