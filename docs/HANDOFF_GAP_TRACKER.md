# Handoff Gap Tracker — MPL-D

**Document ID:** MPL-D-GAP-001  
**Purpose:** Track every known handoff gap with owner, evidence to close, and honest status. Updated as execution progresses — **no synthetic closure.**

---

## Gap register

| Gap ID | Description | Owner role | Status | Evidence to close | Blocker |
|--------|-------------|------------|--------|-------------------|---------|
| GAP-TEST-01 | Zero verification passes on RTM | Test Lead | **Open** | T-01–T-05 records in `tests/logs/` linked in RTM | G-ENR, G-HW-P0 |
| GAP-SAF-01 | NHZ not computed | **LSO (UNASSIGNED)** | **Open** | Signed [`NHZ_WORKSHEET_TEMPLATE.md`](NHZ_WORKSHEET_TEMPLATE.md) | GAP-SAF-02 |
| GAP-SAF-02 | LSO unsigned | Program Lead | **Open** | Signed [`lso_assignment_record.md`](lso_assignment_record.md) | Human assignment |
| GAP-SAF-03 | SOP not LSO-approved | **LSO** | **Open** | Signed SOP PDF or signed markdown attestation | GAP-SAF-02 |
| GAP-SAF-04 | Eyewear OD not determined | **LSO** | **Open** | Eyewear spec in safety case + procurement S-03 OK | GAP-SAF-02 |
| GAP-RISK-01 | Mitigations not executed | Systems Engineer | **Open** | Entries in [`MITIGATION_EXECUTION_LOG.md`](MITIGATION_EXECUTION_LOG.md) | Hardware + tests |
| GAP-RISK-02 | 4 residual High risks | Systems Engineer | **Open** | Measured data per risk row | T-01/T-03/T-05, NHZ |
| GAP-HW-01 | No P0 hardware | Procurement Lead | **Open** | `procurement_status.md` RECV/OK | Export + LSO path |
| GAP-EXP-01 | No ITAR/EAR ruling | Compliance Officer | **Open** | Written determination memo | External review |
| GAP-CM-01 | No formal baseline (was) | Program Lead | **Closed (doc)** | Tag `tdp-baseline-0.1` + registry | — |
| GAP-PH-01 | Phase 1/2 not authorized | Program Lead | **Open** | Written program authorization memo | Program decision |
| GAP-ATM-01 | Atmospheric effects unquantified outdoors | Analyst | **Partial** | [`ATMOSPHERIC_AND_TRACKING_ASSESSMENT.md`](ATMOSPHERIC_AND_TRACKING_ASSESSMENT.md) | Outdoor test auth |
| GAP-TRK-01 | Closed-loop tracking not addressed | Systems Engineer | **Partial** | Phase 1 requirements draft or accepted Phase 0 waiver | R-TRK-001 acceptance |

---

## Residual High risk closure map

| Risk | Gap(s) | Required evidence |
|------|--------|-------------------|
| R-EFF-001 | GAP-TEST-01 | T-03 per surrogate class + irradiance log |
| R-EYE-001 | GAP-SAF-01–04 | NHZ + LSO + SOP + eyewear |
| R-VIB-001 | GAP-TEST-01 | T-05 displacement vs spectrum |
| R-TRK-001 | GAP-TRK-01 | Phase 0 CONOPS waiver signed OR Phase 1 tracking req |

---

## Weekly update protocol

1. Test Lead updates [`../tests/PHASE0_EXECUTION_TRACKER.md`](../tests/PHASE0_EXECUTION_TRACKER.md).  
2. Systems Engineer updates mitigation log and risk register.  
3. Program Lead updates this tracker and [`HANDOFF_READINESS.md`](HANDOFF_READINESS.md).  
4. No gap marked **Closed** without evidence file path or external memo reference.

---

## Next required actions (priority order)

1. Program Lead → assign LSO (GAP-SAF-02).  
2. Compliance Officer → export workflow (GAP-EXP-01).  
3. LSO → NHZ worksheet + SOP approval (GAP-SAF-01/03).  
4. Procurement → I-01, S-03, S-04, interlock before L-01 full power (GAP-HW-01).  
5. Test Lead → execute T-01 at ALIGN only after G-ENR (GAP-TEST-01).
