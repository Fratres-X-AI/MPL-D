# Gate Closure Plan — G-ENR and Phase 0 Execution

**Document ID:** MPL-D-GCP-001  
**Objective:** Close G-SAF-* and G-HW-P0 prerequisites so Phase 0 bench work may begin at **alignment power only**, progressing to full-power only with LSO authorization per session.

**Current state:** G-ENR **BLOCKED**. This plan does **not** authorize skipping steps.

---

## Closure dependency graph

```
Program Lead assigns LSO (G-SAF-01)
        ↓
LSO completes NHZ worksheet + approves safety case (G-SAF-02)
        ↓
LSO approves bench SOP (G-SAF-03)
        ↓
Compliance export memo (R-EXP-001 partial) + order safety hardware (I-01, S-03, S-04, interlock)
        ↓
Receive + inspect P0 (G-HW-P0) + zero-order checklist when optics exist (G-SAF-04)
        ↓
Program Lead + LSO authorize G-ENR for ALIGN power only
        ↓
T-01 → T-05 per PHASE0_EXECUTION_TRACKER
        ↓
Phase 0 exit → consider tdp-baseline-1.0
```

---

## Step-by-step checklist

### Block A — Safety (human-only)

| Step | Action | Gate | Owner | Artifact |
|------|--------|------|-------|----------|
| A1 | Assign named LSO with qualifications | G-SAF-01 | Program Lead | `lso_assignment_record.md` signed |
| A2 | LSO reviews configuration vs safety case draft | G-SAF-02 prep | LSO | Review memo |
| A3 | LSO completes NHZ worksheet with measured or bounded accessible emission | G-SAF-02 | LSO | `NHZ_WORKSHEET_TEMPLATE.md` signed |
| A4 | LSO approves bench SOP | G-SAF-03 | LSO | Signed SOP |
| A5 | LSO specifies eyewear OD; approve procurement S-03 | G-SAF-02 | LSO | Safety case § eyewear |

### Block B — Export and procurement

| Step | Action | Gate | Owner | Artifact |
|------|--------|------|-------|----------|
| B1 | Compliance officer review | R-EXP-001 | Compliance | Determination memo (even if HOLD) |
| B2 | Order metrology + safety first (I-01, S-03, S-04, interlock) | — | Procurement | PO numbers in procurement_status |
| B3 | Order laser module L-01 after B1 + A4 path clear | G-HW-P0 partial | Procurement | PO + export record |
| B4 | Receive and inspect all P0 lines | G-HW-P0 | Test Lead | RECV/OK in procurement_status |

### Block C — Energization authorization

| Step | Action | Gate | Owner | Artifact |
|------|--------|------|-------|----------|
| C1 | Zero-order inspection at ALIGN (when DOE installed) | G-SAF-04 | LSO + Optics | zero_order_checklist signed |
| C2 | Written G-ENR authorization **ALIGN power only** | G-ENR partial | LSO + Program Lead | Email/memo in `tests/logs/admin/` |
| C3 | Session-by-session LSO authorization for power level increases | G-ENR | LSO | Session log |

### Block D — Verification execution

| Step | Action | RTM | Owner | Artifact |
|------|--------|-----|-------|----------|
| D1 | T-01 pattern formation | REQ-F-001, F-005, S-003 | Test Lead | `tests/logs/T-01/` |
| D2 | T-02 irradiance vs range | REQ-F-004, P-001, E-003 | Analyst | `tests/logs/T-02/` |
| D3 | T-03 surrogate dazzle | REQ-F-002, P-002 | Test Lead | `tests/logs/T-03/` |
| D4 | T-04 power/thermal | REQ-E-001, S-004, O-001 | Thermal | `tests/logs/T-04/` |
| D5 | T-05 vibration | REQ-E-002 | Mechanical | `tests/logs/T-05/` |
| D6 | Update RTM verification evidence column | All | Systems Engineer | REQUIREMENTS_TRACEABILITY.md |

---

## Power escalation policy (mandatory)

| Level | Typical power | Authorization |
|-------|---------------|---------------|
| OFF | 0 | Default |
| ALIGN | ≤1% CW or vendor alignment spec | G-ENR partial + LSO |
| LOW | LSO-defined fraction of full | Per-session LSO written OK |
| FULL | Up to approved config max | LSO + NHZ compliance per session |

**No step may be skipped.**

---

## Phase 1 / Phase 2

**Not in this plan.** Separate program authorization required ([`ROADMAP.md`](ROADMAP.md), GAP-PH-01).

---

## Status tracking

Live status: [`phase0_gate_status.md`](phase0_gate_status.md), [`HANDOFF_GAP_TRACKER.md`](HANDOFF_GAP_TRACKER.md), [`../tests/PHASE0_EXECUTION_TRACKER.md`](../tests/PHASE0_EXECUTION_TRACKER.md).
