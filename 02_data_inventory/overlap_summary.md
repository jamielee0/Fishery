# Overlap Summary — Trees to Seas v1 (Day 3)

**Last updated:** 2026-04-08 (Day 3 desktop research — no downloads tested)

---

## Overlap Audit: Pamlico Sound and Neuse River Estuary

### Binding Constraints on the Overlap Window

The overlap window is set by whichever continuous environmental monitoring source starts **latest**, because the forcing and response data (USGS, NOAA weather, Program 195) all have longer records.

| Source | Estimated Start | Binding? | Confidence |
|---|---|---|---|
| USGS discharge | ~1930s | No — long record | HIGH |
| NOAA weather | ~1940s | No — long record | HIGH |
| NCDMF Program 195 | 1987 | No — long record | HIGH |
| FerryMon | ~2000-2002 | **Potentially binding** (but surface-only limits usefulness) | MEDIUM |
| NOAA NERRS | ~1995-2003 (varies) | **Potentially binding** | LOW |
| Ty's GitHub | **UNKNOWN** | **Potentially binding — could be the tightest constraint** | NONE |
| Oyster monitoring | UNKNOWN | Binding for oyster target only | NONE |
| SAV layers | UNKNOWN (episodic) | Binding for SAV target only | NONE |
| Bathymetry | Static | Not binding | HIGH |

### Proposed Minimum Viable Overlap Window

**Optimistic estimate:** ~2003–2024 (~21 years)
- Assumes FerryMon and/or NERRS continuous monitoring running by 2003
- Assumes Ty's GitHub data covers this period (UNCONFIRMED)
- Assumes Program 195 data obtainable for this period

**Conservative estimate:** ~2007–2023 (~16 years)
- Accounts for possible later start of bottom-sensor deployments
- Accounts for possible later start of Ty's GitHub data
- Drops most recent year to ensure completeness

**Worst-case scenario:** Window is UNDEFINED
- If Ty's GitHub cannot be located and NERRS has no bottom sensors in the study area, there may be no confirmed source of continuous bottom environmental data for the overlap window
- This would collapse the core variable set for benthic taxa (DEC-007)

**HUMAN APPROVAL NEEDED:** Approve the overlap window once Ty's GitHub and NERRS bottom-sensor status are resolved.

---

## Target-by-Target Supportability Assessment

### Blue Crab (*Callinectes sapidus*) — CONDITIONALLY SUPPORTABLE

| Requirement | Source | Status |
|---|---|---|
| Response variable (CPUE) | Program 195 | CONFIRMED exists; ACCESS requires NCDMF request |
| Bottom temperature | Ty's GitHub or NERRS | UNCONFIRMED |
| Bottom salinity | Ty's GitHub or NERRS | UNCONFIRMED |
| Bottom dissolved oxygen | Ty's GitHub or NERRS | UNCONFIRMED |
| Forcing (discharge, weather) | USGS + NOAA weather | CONFIRMED exists; access untested |
| Bathymetry | NOAA coastal DEM | CONFIRMED exists; access untested |

**Risk level:** MEDIUM — Response data and forcing are strong. Bottom environmental data is the critical gap.

### Southern Flounder (*Paralichthys lethostigma*) — CONDITIONALLY SUPPORTABLE

Same requirements and status as Blue Crab. Program 195 covers Southern Flounder.

**Risk level:** MEDIUM — Same gaps as blue crab. Must confirm Southern Flounder sample sizes in Program 195.

### Eastern Oyster (*Crassostrea virginica*) — AT RISK

| Requirement | Source | Status |
|---|---|---|
| Response variable (live density) | Oyster monitoring | UNCONFIRMED — provider, access, temporal resolution all unknown |
| Bottom temperature | Ty's GitHub or NERRS | UNCONFIRMED |
| Bottom salinity | Ty's GitHub or NERRS | UNCONFIRMED |
| Bottom dissolved oxygen | Ty's GitHub or NERRS | UNCONFIRMED |
| Dermo prevalence (covariate) | Unknown | UNCONFIRMED — no dataset identified (ASM-009) |
| Forcing | USGS + NOAA weather | CONFIRMED exists |

**Risk level:** HIGH
- Response data source unconfirmed
- Even if data exists, likely annual/seasonal surveys — limits event-scale compression analysis
- Dermo disease confounding unaddressed (ASM-009)
- May need to downgrade oyster to annual-trend analysis only (similar to SAV)

### Seagrass / SAV — AT RISK

| Requirement | Source | Status |
|---|---|---|
| Response variable (extent) | SAV mapping layers | UNCONFIRMED — episodic campaigns with multi-year gaps |
| Turbidity / light | FerryMon or Ty's GitHub | UNCONFIRMED for shallow SAV areas |
| Water temperature | FerryMon or Ty's GitHub | UNCONFIRMED for shallow areas |
| Salinity | FerryMon or Ty's GitHub | UNCONFIRMED for shallow areas |

**Risk level:** HIGH
- Episodic mapping (multi-year gaps) cannot support event-scale analysis (DEC-013 already acknowledges this)
- May not support annual-trend analysis either if campaigns are >5 years apart
- Species selection (*Zostera marina* vs. *Halodule wrightii*) still pending
- Recommend: If mapping campaign dates show <4 data points in the overlap window, SAV should be flagged as potentially unsupportable even as an annual indicator

---

## Depth Mismatch Analysis

DEC-007 mandates bottom measurements for benthic taxa (blue crab, oyster, Southern Flounder).

**Sources that CANNOT provide bottom data:**
- FerryMon: Surface-only (flow-through intake at ~1-1.5m)
- USGS: River gauge, not estuarine
- NOAA weather: Atmospheric

**Sources that MIGHT provide bottom data (UNCONFIRMED):**
- NOAA NERRS: Some national NERRS stations have paired-depth sondes, but NC station configuration is unverified
- Ty's GitHub: Variable ontology lists it for bottom variables, but source cannot be located

**Sources NOT in current registry that might fill the gap:**
- ModMon (Modeling and Monitoring in the Neuse River Estuary, UNC-IMS): Bi-weekly water column profiles including bottom measurements, operating since ~1994. Covers Neuse River Estuary but not open Pamlico Sound.
- Autonomous Vertical Profilers (AVPs, UNC-IMS): High-frequency vertical profiles in Neuse River Estuary.
- Both are referenced in DEC-012 rationale ("ModMon, AVPs"). May already be compiled in Ty's GitHub data.

**HUMAN APPROVAL NEEDED:** If Ty's GitHub data is a ModMon/AVP compilation, confirming the repo URL would resolve the bottom-data gap for the Neuse River Estuary. Open Pamlico Sound bottom data may still be sparse.

---

## Spatial Coverage Gaps

| Sub-system | Forcing | Environmental State | Response (mobile) | Response (sessile) | Habitat |
|---|---|---|---|---|---|
| **Pamlico Sound (open)** | Good (USGS/NOAA) | FerryMon transects (surface only); NERRS uncertain | Program 195 (good) | Oyster monitoring (unconfirmed); SAV (unconfirmed) | Bathymetry (likely good) |
| **Neuse River Estuary** | Good (USGS Kinston gauge) | FerryMon (Cherry Branch route, surface only); NERRS/Ty's GitHub uncertain; ModMon if available | Program 195 (good) | Oyster monitoring (unconfirmed); SAV (unconfirmed) | Bathymetry (likely good) |

**Key spatial gap:** Bottom environmental data in open Pamlico Sound. Even if ModMon/Ty's GitHub cover the Neuse River Estuary, open sound bottom data may be very sparse. This affects whether the project can make sound-wide claims or must restrict to the Neuse sub-system.

---

## Weakest Dependencies (Ranked)

1. **Ty's GitHub data** — Cannot locate. If it provides bottom measurements (as variable_ontology.md implies), its absence collapses DEC-007 compliance. **CRITICAL.**
2. **FerryMon surface-only limitation** — Confirmed surface-only. The most spatially extensive estuarine monitoring source cannot serve the primary modeling need (bottom data). No workaround without an alternative bottom source.
3. **SAV temporal resolution** — Episodic mapping cannot support event-scale analysis. Even annual trends may have too few data points. Day 3 species selection cannot proceed without knowing campaign dates.
4. **Oyster response data** — Provider, access, and temporal resolution all unknown. If only annual surveys exist, event-scale compression analysis for oysters is not possible.
5. **NERRS station placement** — If NC NERRS stations are concentrated near Beaufort/inlet areas rather than inside Pamlico Sound or Neuse River Estuary, they provide no direct coverage of the study area.

---

## Recommendations

1. **Resolve Ty's GitHub immediately** — This is the single highest-priority action. If this source provides compiled bottom data from ModMon/AVPs, it resolves the biggest gap.
2. **Submit NCDMF data request for Program 195** — This is the primary response variable source for 2 of 4 targets. Lead time may be weeks.
3. **Identify NOAA NERRS stations** — Use CDMO station finder to determine which (if any) NC NERRS stations are inside the study area and have bottom sondes.
4. **Investigate ModMon as a named alternative** — If Ty's GitHub cannot be located, ModMon (UNC-IMS) should be evaluated as a direct replacement for bottom data in the Neuse River Estuary.
5. **Assess SAV campaign dates** — If fewer than 4 mapping campaigns fall within the overlap window, formally recommend downgrading SAV from "annual indicator" to "contextual background layer" (not a modeled target).
6. **Do not start ETL until blockers 1-3 are resolved.**
