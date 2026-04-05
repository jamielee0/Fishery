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

<!-- TODO: Add Day 2+ decisions as they are approved -->
<!-- Template:
## DEC-NNN: Title

**Date:**
**Decision:**
**Rationale:**
**Approved by:**
**Dissent:**
-->
