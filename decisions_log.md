# Decisions Log — Trees to Seas v1

Record every architectural, scientific, or scope decision here. Include date, decision, rationale, who approved, and any dissent.

---

## DEC-001: v1 scope locked to North Carolina

**Date:** 2026-04-05 (Day 1)
**Decision:** v1 models only North Carolina estuarine systems. Great Lakes collapse is introduction context only, not a modeling domain.
**Rationale:** Focus maximizes data overlap and keeps the proof-of-concept defensible within a 14-day sprint.
**Approved by:** Project brief (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-002: Single central claim strategy

**Date:** 2026-04-05 (Day 1)
**Decision:** The paper makes exactly one central claim — that dynamic habitat compression outperforms static summaries on held-out NC data.
**Rationale:** A single claim is easier to test, falsify, and defend. Additional findings are secondary.
**Approved by:** Project brief (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-003: Time-blocked validation as primary strategy

**Date:** 2026-04-05 (Day 1)
**Decision:** Primary validation uses time-blocked held-out years. Random CV is not sufficient alone. Estuary holdout is secondary if sample size permits.
**Rationale:** Temporal autocorrelation in environmental data makes random splits unreliable. Time-blocking is the defensible standard.
**Approved by:** Project brief (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-004: Conservative claim language

**Date:** 2026-04-05 (Day 1)
**Decision:** All claims use predictive, associative, and forecast-ready language. No causal claims.
**Rationale:** Observational study design cannot support causal inference. Reviewers will flag overclaiming.
**Approved by:** Project brief (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-005: Healthy ranges defined in advance, not from model outputs

**Date:** 2026-04-05 (Day 1)
**Decision:** Species-specific healthy ranges must be operationalized from literature before modeling, not labeled retrospectively.
**Rationale:** Retrospective labeling would be circular and indefensible.
**Approved by:** Project brief (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-006: Variable ontology staging is mandatory

**Date:** 2026-04-06 (Day 2)
**Decision:** Variables must be classified into families (forcing, local estuarine state, habitat-condition, engineered features, response, benchmark) and models must respect the staging. No kitchen-sink models mixing all families as unrestricted inputs.
**Rationale:** Staging is required for H3 testing (staged vs. direct models) and for surviving reviewer scrutiny on mechanistic interpretation vs. spurious correlation.
**Approved by:** Day 2 science structure (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-007: Bottom measurements required for benthic taxa

**Date:** 2026-04-06 (Day 2)
**Decision:** Blue crab, eastern oyster, and the finfish target require bottom or near-bottom environmental measurements. Surface-only salinity or DO must not be used as a stand-in for benthic exposure without an explicit, documented fallback policy approved by humans.
**Rationale:** Reviewers will reject benthic-species models built on surface data without acknowledging vertical stratification (the salt wedge). See reviewer concern RC-2.
**Approved by:** Day 2 science structure (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-008: Temporal station-based compression as v1 default

**Date:** 2026-04-06 (Day 2)
**Decision:** v1 habitat compression is defined as temporal squeeze at stations/cells by default. Spatial safe-area interpolation is deferred to an optional extension only if Day 3 shows sufficient spatial density, bottom-state coverage, and bathymetric support.
**Rationale:** Temporal compression is computationally defensible with observational point data. Spatial interpolation introduces fragile assumptions that add engineering risk without guaranteed scientific payoff.
**Approved by:** Day 2 science structure (PROPOSED — requires human approval before Day 3)
**Dissent:** None recorded. Spatial extension remains an option, not a rejection.

---

## DEC-009: Point-sampled nutrients rejected from core v1

**Date:** 2026-04-06 (Day 2)
**Decision:** Point-sampled nutrient concentrations (TN, TP, DIN) are rejected from core v1 models as direct weekly predictors. The nutrient-to-hypoxia cascade is too lagged and nonlinear for dynamic weekly modeling, and grab samples are too temporally sparse.
**Rationale:** Day 2 mechanism review confirms the biogeochemical cascade introduces massive temporal lags. Hypoxia is modeled directly via bottom DO, which captures the downstream result of nutrient loading.
**Approved by:** Day 2 science structure (pending human confirmation)
**Dissent:** None recorded.

---

## DEC-010: Southern Flounder proposed as finfish target

**Date:** 2026-04-06 (Day 2)
**Decision:** Southern Flounder (*Paralichthys lethostigma*) is proposed as the estuarine finfish target. This is a recommendation, not a locked choice. Final approval requires Day 3 data overlap confirmation.
**Rationale:** Benthic, heavily surveyed by NCDMF, hypoxia-driven avoidance behavior is a textbook example of habitat compression. Best candidate for H2 testing alongside blue crab.
**Approved by:** Day 2 reviewer recommendation (PROPOSED — requires human approval)
**Dissent:** Other candidates may have better data overlap. Human must decide.

---

## DEC-011: B2 (sediment/burial) proposed for deferral

**Date:** 2026-04-06 (Day 2)
**Decision:** Backup hypothesis B2 (sediment/disturbance proxies for benthic targets) is proposed for deferral from active v1 implementation. Turbidity remains in the variable set as a light-limitation proxy for SAV, but direct sedimentation/burial is not modeled.
**Rationale:** Day 2 mechanism review confirms that continuous spatial data on dynamic sediment deposition does not exist across NC estuaries at useful temporal resolution. Interpolating from wind/flow proxies would look fabricated.
**Approved by:** Day 2 reviewer recommendation (PROPOSED — requires human approval)
**Dissent:** B2 is listed in hypotheses_v1.md as a backup hypothesis. This deferral preserves the hypothesis text but removes it from active implementation. Turbidity-based light limitation for SAV is retained separately.
**Conflict:** hypotheses_v1.md still lists B2. If deferral is approved, hypotheses_v1.md should note B2 as deferred, not deleted.

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
