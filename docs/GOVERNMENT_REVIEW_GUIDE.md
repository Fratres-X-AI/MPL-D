# How to Use This Package for Government Review

**Audience:** Military/government technical reviewers, CSO/OT evaluators, prime subcontractor assessors.

**Maturity of package:** Preliminary Design documentation and unvalidated analysis — **conceptual study only, not a proposal, not a capability claim.**

---

## 1. What this package is and is not

| Is | Is not |
|----|--------|
| Structured technical data for a counter-UAS **sensor-denial** research concept | A fielded system or program of record |
| Traceable requirements, risks, and planned verification | Evidence of dazzle effectiveness against threat systems |
| Phase 0 bench plan with safety gates | LSO-approved laser operation authorization |
| Conservative first-order models with stated uncertainty | Validated range or engagement envelope |

---

## 2. Recommended reading order (≈2–4 hours)

| Step | Document | Time | Purpose |
|------|----------|------|---------|
| 1 | [`README.md`](../README.md) — Executive Summary | 15 min | Scope, gates, top risks |
| 2 | [`phase0_gate_status.md`](phase0_gate_status.md) | 10 min | What is blocked vs documented |
| 3 | [`CONOPS.md`](CONOPS.md) | 15 min | Defensive employment intent |
| 4 | [`ARCHITECTURE.md`](ARCHITECTURE.md) | 45 min | System design and trades |
| 5 | [`REQUIREMENTS_TRACEABILITY.md`](REQUIREMENTS_TRACEABILITY.md) | 20 min | Req → test → risk links |
| 6 | [`RISK_REGISTER.md`](RISK_REGISTER.md) | 30 min | Residual risks |
| 7 | [`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md) + [`ROE_PROTOCOL_IV.md`](ROE_PROTOCOL_IV.md) | 20 min | Safety and policy gaps |
| 8 | [`ANALYSIS_VALIDATION_STATUS.md`](ANALYSIS_VALIDATION_STATUS.md) | 15 min | Model limits |
| 9 | [`TDP_STRUCTURE.md`](TDP_STRUCTURE.md) | 10 min | Full tree map |

**Optional depth:** [`ICD_HOST_INTEGRATION.md`](ICD_HOST_INTEGRATION.md), hardware folder, test procedures T-01–T-05.

---

## 3. Gate status summary (reviewer checklist)

| Gate | Status | Reviewer implication |
|------|--------|---------------------|
| G-DOC | PASS | Documentation sufficient to *plan* bench work |
| G-PROTO | PASS | Design artifacts exist on paper |
| G-SAF-01/02/03 | OPEN | **Do not assume safe laser ops** |
| G-HW-P0 | OPEN | No hardware evidence |
| G-ENR | BLOCKED | No energization authorized |

---

## 4. Top risks (residual after documented mitigations)

| ID | Residual | Why still open |
|----|----------|----------------|
| R-EFF-001 | **High** | No threat-representative test data |
| R-EYE-001 | **High** | NHZ not completed; NIR invisible |
| R-VIB-001 | **High** | No T-05 data |
| R-ROE-001 | **Medium** | No legal review |
| R-EXP-001 | **Medium** | No ITAR/EAR determination |

Full table: [`RISK_REGISTER.md`](RISK_REGISTER.md).

---

## 5. Caveats for evaluators

1. **Do not treat irradiance tables as operational range.**
2. **Do not treat Phase 0 surrogate success as threat effectiveness.**
3. **Drone-X integration is a program baseline, not a verified ICD.**
4. **940 nm leading candidate is not down-selected until three-class surrogate tests run.**
5. **Hero/schematic art excludes host platform by policy — not an omission of integration intent.**

---

## 6. Questions this package can answer today

- What is the design concept and maturity?
- What would Phase 0 bench attempt to measure?
- What safety and legal gates block hardware work?
- Where are requirements traced to tests and risks?

## 7. Questions this package cannot answer today

- Does the dazzler work against a specific threat UAS at a specific range?
- What is the approved NHZ and laser class?
- What is the ECCN or export classification?
- Is flight test or field employment authorized?

---

## 8. Suggested reviewer feedback to request from Fratres X AI

1. LSO assignment date and NHZ completion date.
2. Host vendor ICD or waiver.
3. Export control determination path and timeline.
4. Phase 0 bench schedule contingent on G-ENR.
