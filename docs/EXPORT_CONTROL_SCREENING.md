# Export Control Screening — MPL-D

**Document ID:** MPL-D-EXP-001  
**Maturity:** Preliminary Design — screening checklist and status record. **Not legal advice. Not a license determination.**

**Evidence / analysis status:** Configuration screened at paper level (940 nm ~10 W class fiber module; pulsed bench prototype; US/EU vendor assumption).

**Determination status:** **NO ITAR/EAR RULING OBTAINED.** **HOLD** on international shipment and foreign-person access until compliance officer review.

**Known gaps:** No ECCN assigned; no commodity jurisdiction request; no integrated system classification.

**Next required action:** Fratres X AI compliance officer review before P0 laser module order or foreign disclosure.

---

## 1. Configuration screened

| Parameter | Value |
|-----------|-------|
| Laser | 940 nm fiber-coupled ~10 W CW rated (AeroDiode-class candidate) |
| Purpose documented | Defensive EO sensor denial (CONOPS) |
| Integration data | Drone-X concept only — hardpoint **not** in repo |
| Performance claims in repo | Planning estimates only — no validated range |

---

## 3. Current determination record

| Field | Value |
|-------|-------|
| ITAR jurisdiction | **Undetermined — no ruling obtained** |
| EAR / ECCN | **Not assigned** |
| Compliance officer memo | **None on file** |
| Effective determination date | — |
| Workflow | [`EXPORT_DETERMINATION_WORKFLOW.md`](EXPORT_DETERMINATION_WORKFLOW.md) |

**Operational rule:** **HOLD** — see workflow Step 3.

---

## 2. Screening checklist (R-EXP-001)

| ID | Question | Result | Notes |
|----|----------|--------|-------|
| E1 | Optical power ≥ 10 W CW rated? | **Yes** | Triggers careful review — not automatic ITAR |
| E2 | Military-exclusive wavelength? | **No** | 940 nm industrial/commercial class |
| E3 | Foreign national repo access? | **TBD** | Program policy required |
| E4 | Military platform integration drawings released? | **No** | Concept text only |
| E5 | Defensive purpose documented? | **Yes** | CONOPS, ROE doc |
| E6 | ITAR/EAR classification assigned? | **No** | **Gap — compliance officer required** |
| E7 | Vendor country of origin confirmed? | **No** | Pending procurement |
| E8 | Technical data packaged for export? | **Not authorized** | This repo may contain controlled data when hardware exists |

---

## 4. Recommended next actions

| # | Action | Owner | Target artifact |
|---|--------|-------|-----------------|
| 1 | Compliance officer review of this screening + CONOPS | Compliance | Written hold/release memo |
| 2 | Obtain vendor ECCN / country of origin on PO | Procurement | procurement_status update |
| 3 | Define repo access policy (private vs partner) | Program lead | CONFIGURATION_MANAGEMENT |
| 4 | Re-screen if optical power, wavelength, or integration data changes | Systems | Updated EXP-001 rev |

---

## 5. Traceability

| Requirement | Link |
|-------------|------|
| REQ-R-003 | This document |
| Risk | R-EXP-001 |

**Related:** [`DATA_RIGHTS.md`](DATA_RIGHTS.md) · [`ROE_PROTOCOL_IV.md`](ROE_PROTOCOL_IV.md)

---

## 6. Statement for government reviewers

Fratres X AI has **not** obtained a U.S. government or export authority ruling on this configuration. Evaluators should treat export status as **indeterminate** until a compliance determination is issued and filed here.
