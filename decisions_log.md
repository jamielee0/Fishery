# Decisions Log — Trees to Seas v1

Record every architectural, scientific, or scope decision here. Include date, decision, rationale, who approved, and any dissent.

---

## DEC-001: v1 scope locked to North Carolina

**Date:** 2026-04-05 (Day 1)
**Decision:** v1 models only North Carolina estuarine systems. Great Lakes collapse is introduction context only, not a modeling domain.
**Rationale:** Focus maximizes data overlap and keeps the proof-of-concept defensible within a 14-day sprint.
**Approved by:** Project brief
**Dissent:** None recorded.

---

## DEC-002: Single central claim strategy

**Date:** 2026-04-05 (Day 1)
**Decision:** The paper makes exactly one central claim — that dynamic habitat compression outperforms static summaries on held-out NC data.
**Rationale:** A single claim is easier to test, falsify, and defend. Additional findings are secondary.
**Approved by:** Project brief
**Dissent:** None recorded.

---

## DEC-003: Time-blocked validation as primary strategy

**Date:** 2026-04-05 (Day 1)
**Decision:** Primary validation uses time-blocked held-out years. Random CV is not sufficient alone. Estuary holdout is secondary if sample size permits.
**Rationale:** Temporal autocorrelation in environmental data makes random splits unreliable. Time-blocking is the defensible standard.
**Approved by:** Project brief
**Dissent:** None recorded.

---

## DEC-004: Conservative claim language

**Date:** 2026-04-05 (Day 1)
**Decision:** All claims use predictive, associative, and forecast-ready language. No causal claims.
**Rationale:** Observational study design cannot support causal inference. Reviewers will flag overclaiming.
**Approved by:** Project brief
**Dissent:** None recorded.

---

## DEC-005: Healthy ranges defined in advance, not from model outputs

**Date:** 2026-04-05 (Day 1)
**Decision:** Species-specific healthy ranges must be operationalized from literature before modeling, not labeled retrospectively.
**Rationale:** Retrospective labeling would be circular and indefensible.
**Approved by:** Project brief
**Dissent:** None recorded.

---

## DEC-006: Variable ontology staging is mandatory

**Date:** 2026-04-06 (Day 2)
**Decision:** Variables must be classified into families (forcing, local estuarine state, habitat-condition, engineered features, response, benchmark) and models must respect the staging. No kitchen-sink models mixing all families as unrestricted inputs.
**Rationale:** Staging is required for H3 testing (staged vs. direct models) and for surviving reviewer scrutiny on mechanistic interpretation vs. spurious correlation.
**Approved by:** Day 2 science structure
**Dissent:** None recorded.

---

## DEC-007: Bottom measurements required for benthic taxa

**Date:** 2026-04-06 (Day 2)
**Decision:** Blue crab, eastern oyster, and the finfish target require bottom or near-bottom environmental measurements. Surface-only salinity or DO must not be used as a stand-in for benthic exposure without an explicit, documented fallback policy approved by humans.
**Rationale:** Reviewers will reject benthic-species models built on surface data without acknowledging vertical stratification (the salt wedge). See reviewer concern RC-2.
**Approved by:** Day 2 science structure
**Dissent:** None recorded.

---

## DEC-008: Temporal station-based compression as v1 default

**Date:** 2026-04-06 (Day 2)
**Decision:** v1 habitat compression is defined as temporal squeeze at stations/cells by default. Spatial safe-area interpolation is deferred to an optional extension only if Day 3 shows sufficient spatial density, bottom-state coverage, and bathymetric support.
**Rationale:** Temporal compression is computationally defensible with observational point data. Spatial interpolation introduces fragile assumptions that add engineering risk without guaranteed scientific payoff.
**Approved by:** Day 2 science structure
**Dissent:** None. Spatial extension remains an option, not a rejection.

---

## DEC-009: Point-sampled nutrients rejected from core v1

**Date:** 2026-04-06 (Day 2)
**Decision:** Point-sampled nutrient concentrations (TN, TP, DIN) are rejected from core v1 models as direct weekly predictors. The nutrient-to-hypoxia cascade is too lagged and nonlinear for dynamic weekly modeling, and grab samples are too temporally sparse.
**Rationale:** Day 2 mechanism review confirms the biogeochemical cascade introduces massive temporal lags. Hypoxia is modeled directly via bottom DO, which captures the downstream result of nutrient loading.
**Approved by:** Day 2 science structure
**Dissent:** None recorded.

---

## DEC-010: Southern Flounder locked as finfish target

**Date:** 2026-04-06 (Day 2)
**Decision:** Southern Flounder (*Paralichthys lethostigma*) is the approved estuarine finfish target for v1.
**Rationale:** Benthic, heavily surveyed by NCDMF, hypoxia-driven avoidance behavior is a textbook example of habitat compression. Best candidate for H2 testing alongside blue crab.
**Approved by:** Day 2 science structure, locked in Day 2 consistency pass
**Dissent:** None.

---

## DEC-011: B2 (sediment/burial) deferred

**Date:** 2026-04-06 (Day 2)
**Decision:** Backup hypothesis B2 (sediment/disturbance proxies for benthic targets) is deferred from active v1 implementation. Turbidity remains in the variable set as a light-limitation proxy for SAV, but direct sedimentation/burial is not modeled.
**Rationale:** Day 2 mechanism review confirms that continuous spatial data on dynamic sediment deposition does not exist across NC estuaries at useful temporal resolution. Interpolating from wind/flow proxies would look fabricated.
**Approved by:** Day 2 science structure, locked in Day 2 consistency pass
**Dissent:** None. B2 is marked DEFERRED (not deleted) in hypotheses_v1.md. Turbidity-based light limitation for SAV is retained separately. B2 may be revived if Day 3 inventory reveals a usable sediment dataset.

---

## DEC-012: Pilot geography locked to Pamlico Sound and Neuse River Estuary

**Date:** 2026-04-06 (Day 2)
**Decision:** v1 pilot geography is Pamlico Sound and the Neuse River Estuary, not all NC coastal estuaries. This is the canonical proof-of-concept area.
**Rationale:** Pamlico Sound has the strongest data density (Program 195 since 1987, FerryMon, ModMon, AVPs, NERRS) and the best-documented hypoxia-compression literature. Neuse River Estuary is the classic hypoxia study site. Broader NC coverage would dilute overlap and weaken the proof-of-concept.
**Approved by:** Day 2 consistency pass
**Dissent:** None. Albemarle Sound may serve as estuary holdout if sample size permits.

---

## DEC-013: SAV is an annual/episodic indicator, not an event-scale target

**Date:** 2026-04-06 (Day 2)
**Decision:** SAV/seagrass is retained as a habitat indicator but explicitly at annual or episodic temporal resolution. It is not an event-scale target on par with the three mobile/sessile species. Event-scale attribution of compression to SAV loss is unlikely to be defensible in v1.
**Rationale:** Official NC SAV monitoring relies on infrequent multi-year mapping products. ASM-005 flags this risk. Treating SAV as if it has the same temporal resolution as survey CPUE would be misleading.
**Approved by:** Day 2 consistency pass
**Dissent:** None. If Day 3 reveals higher-frequency SAV data, the resolution can be upgraded.

---

<!-- TODO: Add Day 3+ decisions as they are approved -->
<!-- Template:
## DEC-NNN: Title

**Date:**
**Decision:**
**Rationale:**
**Approved by:**
**Dissent:**
-->
