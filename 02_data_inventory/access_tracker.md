# Data Access Tracker — Trees to Seas v1 (Day 3)

Track access status, credentials needed, and blockers for each data source.

**Last updated:** 2026-04-08 (Day 3 inventory — desktop research only, no downloads tested)

**Legend:**
- CONFIRMED = verified from domain knowledge, published literature, or known federal data programs
- UNCONFIRMED = plausible but not verified by direct access test
- HUMAN APPROVAL NEEDED = requires human action (data request, repo URL, etc.)

---

## Source Access Status

| Source | Provider (confidence) | Access Confirmed | Access Method | Credentials Needed | Download Tested | Measurement Depth | Blocker | Action Needed |
|---|---|---|---|---|---|---|---|---|
| FerryMon | UNC-IMS (CONFIRMED) | No | UNCONFIRMED (likely download or request) | UNCONFIRMED | No | SURFACE ONLY | Surface-only violates DEC-007 for benthic taxa | HUMAN: Confirm access URL. Verify whether any bottom profiling data exists. |
| NOAA estuarine (NERRS) | NOAA NERRS (CONFIRMED) | No | API via CDMO (CONFIRMED program exists) | No (public) | No | UNCONFIRMED — paired-depth sondes vary by station | Must confirm stations inside study area + bottom sensor availability | HUMAN: Identify specific NC NERRS station IDs inside Pamlico Sound / Neuse River Estuary. Confirm which have bottom sondes. |
| USGS stations | USGS (CONFIRMED) | No | API via NWIS (CONFIRMED program exists) | No (public) | No | N/A (river gauge) | Minimal — must confirm specific gauge IDs | Confirm gauge IDs: Neuse at Kinston (02089500?), Tar-Pamlico gauges. |
| NOAA weather | NOAA NCEI (CONFIRMED) | No | API or bulk download (CONFIRMED program exists) | No (public) | No | N/A (land weather station) | Minimal — must choose station vs. gridded product | Confirm station IDs or gridded product selection (GHCN-Daily vs. nClimGrid vs. PRISM). |
| Ty's GitHub | UNKNOWN | No | GitHub repo (claimed) | UNCONFIRMED | No | UNCONFIRMED — may include bottom data | **CRITICAL: Repo cannot be located. No URL, no provider, no variable catalog.** | **HUMAN APPROVAL NEEDED: Provide repo URL or confirm this source exists. This is the #1 blocker.** |
| Fishery-independent (P195) | NCDMF (CONFIRMED) | No | Formal data request to NCDMF | Yes (data request required) | No | Trawl samples near-bottom | Access requires formal request; processing time unknown | **HUMAN APPROVAL NEEDED: Submit data request to NCDMF for Program 195 data. Confirm species coverage, effort variables, and environmental readings at tow.** |
| Oyster monitoring | UNCONFIRMED (likely NCDMF) | No | UNCONFIRMED (likely data request) | UNCONFIRMED | No | Reef-level (bottom) | Provider, access method, temporal range all unconfirmed | **HUMAN APPROVAL NEEDED: Identify NC oyster monitoring program, data custodian, and submit request.** |
| SAV / seagrass layers | UNCONFIRMED (likely NOAA/APNEP/NC DEQ) | No | Download (GIS layers expected) | UNCONFIRMED | No | Shallow benthic (aerial/satellite mapping) | Episodic temporal resolution (multi-year gaps) | HUMAN: Identify exact mapping campaign dates and download source. Confirm whether Pamlico Sound is covered. |
| Bathymetry / habitat | NOAA NCEI (CONFIRMED for coastal DEMs) | No | Download (public raster/GIS) | No (public) | No | Full water column (depth) | Low risk — static data | Confirm specific DEM product for Pamlico Sound and vertical datum. |

---

## Summary Counts

| Status | Count |
|---|---|
| Access confirmed and tested | 0 |
| Provider confirmed, access untested | 5 (USGS, NOAA weather, NOAA NERRS, FerryMon, Bathymetry) |
| Provider and access both unconfirmed | 3 (Ty's GitHub, Oyster monitoring, SAV layers) |
| Requires formal data request | 2 (Fishery-independent P195, Oyster monitoring) |
| **Critical blockers** | **2 (Ty's GitHub location, FerryMon depth limitation)** |

---

## Depth Audit (DEC-007 Compliance)

DEC-007 requires bottom measurements for blue crab, eastern oyster, and Southern Flounder.

| Source | Provides Bottom Data? | Notes |
|---|---|---|
| FerryMon | **NO — surface only** | Flow-through intake at ~1-1.5m. Cannot satisfy DEC-007. |
| NOAA NERRS | UNCONFIRMED | Some NERRS stations nationally deploy paired sondes. NC station configuration not verified. |
| Ty's GitHub | UNCONFIRMED | Variable ontology lists this source for bottom variables, but source cannot be located. |
| USGS | N/A | River discharge — not an estuarine depth measurement. |
| NOAA weather | N/A | Atmospheric — not a water measurement. |
| Program 195 | Partial | Trawl surveys sample near-bottom, and some surveys record environmental data at tow site. Unconfirmed whether bottom temp/sal/DO are systematically recorded. |

**Depth policy conclusion:** No source has CONFIRMED bottom-measurement capability for the study area. This is a critical gap. If Ty's GitHub data or NERRS bottom sondes cannot fill this gap, the project must either (a) find an alternative bottom-data source (e.g., ModMon, AVPs, or other UNC-IMS programs), or (b) propose and get approval for a fallback depth policy.

**HUMAN APPROVAL NEEDED:** Propose and approve a fallback depth policy for stations with surface-only data.

---

## Actions Required Before Day 4

1. **CRITICAL:** Human must provide Ty's GitHub repo URL or confirm the source does not exist
2. **CRITICAL:** Human must submit NCDMF data request for Program 195 fishery-independent survey data
3. **HIGH:** Identify specific NOAA NERRS station IDs inside Pamlico Sound / Neuse River Estuary and confirm bottom sonde deployments
4. **HIGH:** Confirm FerryMon data access URL and verify no bottom profiling capability exists
5. **HIGH:** Identify NC oyster monitoring program and data custodian
6. **MEDIUM:** Identify SAV mapping campaign dates and download source for Pamlico Sound
7. **MEDIUM:** Confirm USGS gauge IDs for Neuse and Tar-Pamlico watersheds
8. **MEDIUM:** Select NOAA weather product (station vs. gridded)
9. **LOW:** Confirm NOAA coastal DEM product for Pamlico Sound bathymetry
