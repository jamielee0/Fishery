# Project Brief — Trees to Seas v1

> Pamlico Sound and Neuse River Estuary fisheries depend not just on harvest rules but on when and where estuarine habitat is usable, and that habitat shifts with temperature, salinity, dissolved oxygen, turbidity, flow, and watershed inputs.

> **This repo is scaffold and configuration only. No pipeline code, no model code, no data, and no results exist yet. Nothing here is runnable science.**

## Aim

Build a publication-oriented proof-of-concept in Pamlico Sound and the Neuse River Estuary that tests whether species-specific habitat compression, estimated from dynamic estuarine conditions, can serve as a better management signal than static annual or survey-timed summaries.

## Pipeline Blueprint

Watershed/weather forcing -> Environmental state -> Species response -> Habitat-days/compression outputs

## Focal Targets — Locked

| Target | Scientific Name | Type |
|---|---|---|
| Blue crab | *Callinectes sapidus* | Mobile crustacean |
| Eastern oyster | *Crassostrea virginica* | Sessile bivalve |
| Southern Flounder | *Paralichthys lethostigma* | Estuarine finfish |
| Seagrass / SAV | Species TBD at Day 3 | Habitat indicator |

Southern Flounder is the approved estuarine finfish target, selected for its benthic ecology, strong NCDMF survey coverage, and textbook hypoxia-avoidance behavior. The SAV role is locked as an annual/episodic habitat indicator (not an event-scale target on par with the mobile species); the exact species (*Zostera marina* vs. *Halodule wrightii*) depends on NC data availability and will be decided at Day 3 because thresholds differ dramatically between candidates.

## Data Sources

- FerryMon and related water-quality feeds
- NOAA and USGS stations
- Ty's GitHub environmental data
- Fishery-independent surveys
- Oyster, seagrass, and habitat layers

## Deliverable

A benchmarked NC study that maps:
1. Where focal targets are within healthy environmental ranges
2. When that habitat becomes compressed or unsafe
3. Which variables are most associated with risk

## v1 Scope Lock

- Pamlico Sound and Neuse River Estuary pilot
- Great Lakes used only as introduction context
- No whole-USA model in v1
- One central paper claim only
- Focal set: blue crab, eastern oyster, Southern Flounder, and seagrass/SAV
- Observational, benchmarked modeling paper — not a management platform

## What Not To Do in v1

- Do not expand to the whole USA
- Do not treat the Great Lakes as a second modeling domain
- Do not claim observational associations prove causation
- Do not add many species before the overlap window is confirmed
- Do not accept a model that only looks good under random splits or static annual averages
