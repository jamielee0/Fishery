# Trait Table — Blue Crab (*Callinectes sapidus*)

**Target type:** Mobile crustacean
**Status in v1:** Confirmed focal target (brief_v1.md)
**Primary hypothesis role:** H1 target, H2 target

---

## Life Stages Relevant to v1

| Life Stage | Relevance to v1 | Survey Representativeness | Notes |
|---|---|---|---|
| Juvenile | High — primary survey catch | TODO: Confirm gear selectivity for juveniles | Likely dominant in fishery-independent trawls |
| Adult male | High — survey catch | TODO: Confirm | Seasonal movement patterns may complicate alignment |
| Adult female (sponge crab) | Moderate — seasonal | TODO: Confirm | Spawning migration to high-salinity waters |
| Megalopae / larvae | Low — not directly surveyed | Not represented in trawl surveys | Exclude from v1 response variable |

---

## Healthy-Range Concept

**Definition approach:** Literature-backed thresholds defined a priori per DEC-005. Healthy = all required state variables within bounds simultaneously.

| Variable | Relevance | Healthy Range (Literature Placeholder) | Evidence Strength | Unresolved Questions |
|---|---|---|---|---|
| Temperature (°C) | **Essential** — thermal stress, heat avoidance | TODO: Literature value needed | TODO | What life stage? Acute vs. chronic threshold? |
| Salinity (PSU) | **Essential** — osmoregulatory stress, spatial distribution | TODO: Literature value needed | TODO | Euryhaline but preferences vary by life stage |
| Dissolved oxygen (mg/L) | **Essential** — hypoxia avoidance is primary compression mechanism | TODO: Literature value needed (commonly cited ~2.0 mg/L lethal, ~3.0 sublethal) | TODO | Bottom vs. water-column; duration matters |
| Turbidity (NTU) | **Low relevance** — not primary driver for mobile crustacean | Not planned as primary constraint | — | Optional; may affect prey availability indirectly |

---

## Temperature Relevance

- **Mechanism:** Thermal stress increases metabolic demand; acute heat events cause mortality or emigration
- **Degree-day relevance:** **High** — cumulative thermal energy dictates growth, molting windows, seasonal timing (supports B1)
- **Degree-day base temperature:** TODO: Literature value needed (commonly cited ~10°C but species/life-stage specific)
- **Known risk:** Degree-days may overfit simple seasonality (reviewer concern)

## Salinity Relevance

- **Mechanism:** Rapid freshening causes osmotic shock; prolonged low salinity displaces crabs down-estuary
- **Salinity excursion metric:** Relevant — freshening events from storm runoff (supports H3)
- **Known risk:** Surface salinity ≠ bottom salinity (salt wedge); crabs are benthic

## Dissolved Oxygen Relevance

- **Mechanism:** Bottom hypoxia is the primary habitat compression driver for blue crab in NC
- **Compression role:** Core — hypoxia forces crabs from deep channels to shallow margins, creating the "hypoxia-temperature squeeze"
- **Known risk:** Daytime sampling misses nighttime DO minima; bottom DO data may be sparse
- **Catchability paradox:** CPUE may **increase** during compression events as crabs crowd into surveyed shallow margins

## Turbidity / Light Relevance

- **Direct relevance:** Low for blue crab (not light-dependent)
- **Indirect relevance:** Turbidity from runoff may co-occur with freshening events

## Habitat Dependency

- **Benthic:** Yes — requires bottom conditions, not surface
- **Depth preference:** Channels and deeper waters preferred, but moves to shallows under hypoxia
- **Substrate association:** Soft bottom, mud; some use of structured habitat (oyster reef, SAV edges)

## Degree-Day Relevance

- **Expected value:** High — thermal accumulation affects growth rate, molt timing, spawning migration
- **B1 test:** Degree-days expected to improve prediction for blue crab more than for oyster or seagrass
- **Unresolved:** Base temperature, accumulation start date, season reset logic

---

## Literature Status

| Topic | Literature Status | Key References Needed |
|---|---|---|
| Thermal tolerance range | TODO: Needs literature search | NC-specific preferred |
| Salinity tolerance range | TODO: Needs literature search | Life-stage-specific |
| DO avoidance threshold | TODO: Needs literature search | Commonly cited ~2.0–3.0 mg/L |
| Hypoxia-driven redistribution in NC | TODO: Needs literature search | Neuse River / Pamlico Sound studies |
| Degree-day base temperature | TODO: Needs literature search | Molting/growth literature |
| CPUE-compression relationship | TODO: Needs literature search | Catchability under hypoxia |

---

## Unresolved Threshold Questions (Require Human Approval)

1. Which life stage(s) define the healthy range for the v1 response variable?
2. Are acute thresholds (lethal) or chronic thresholds (sublethal/avoidance) the binding definition?
3. What is the accepted bottom-exposure policy when only surface data exist?
4. How is the lookback window (W) defined relative to survey timing?
5. Is fishing mortality a required sensitivity covariate or a documented limitation?
