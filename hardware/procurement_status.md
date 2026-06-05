# Phase 0 Procurement Status

**Maturity:** Phase 0 — **ordering not executed.** No received goods. **G-HW-P0 OPEN.**

**Execution plan:** Order sequence in [`../docs/GATE_CLOSURE_PLAN.md`](../docs/GATE_CLOSURE_PLAN.md) Block B.

---

## Status legend

| Status | Meaning |
|--------|---------|
| SPEC | Specified; not ordered |
| ORDER | PO issued — record PO # and date |
| RECV | Received; inspection pending |
| OK | Inspected; bench-ready |

---

## Order sequence (mandatory)

| Order | ID | Item | Prerequisite | Status |
|-------|-----|------|--------------|--------|
| 1 | I-01 | Power meter + sensor | Export workflow initiated | SPEC |
| 2 | S-03 | Eyewear 940 nm (OD by LSO) | LSO specifies OD in NHZ worksheet | SPEC |
| 3 | S-04 | Interlock / beam blocks | — | SPEC |
| 4 | L-02 | Driver ≥13 A | — | SPEC |
| 5 | L-01 | 940 nm 10 W module | Compliance memo + LSO safety path | SPEC |
| 6 | O-01 | Collimator | — | SPEC |
| 7 | O-02 | DOE 3×3 | θ measured or vendor beam spec | SPEC |
| 8 | O-03 | Zero-order dump | — | SPEC |

---

## P0 items detail

| ID | Item | Status | PO # | Date | Notes |
|----|------|--------|------|------|-------|
| L-01 | 940 nm 10 W module | SPEC | — | — | Export HOLD until memo |
| L-02 | Diode driver ≥13 A | SPEC | — | — | |
| O-01 | 940 nm collimator | SPEC | — | — | |
| O-02 | DOE 3×3 | SPEC | — | — | Long lead |
| O-03 | Zero-order dump | SPEC | — | — | |
| I-01 | Power meter + sensor | SPEC | — | — | **Order first** |
| S-03 | Eyewear 940 nm | SPEC | — | — | LSO OD TBD |
| S-04 | Interlock / blocks | SPEC | — | — | |

**G-HW-P0:** **OPEN** (all SPEC)

---

## P1 — surrogate sensors

| Item | Status | Gate |
|------|--------|------|
| Surrogate Class 1–3 per surrogate_sensor_procurement.md | SPEC | G-SAF-05 |

---

## Procurement lead next actions

1. Trigger Compliance Step 1–2 ([`EXPORT_DETERMINATION_WORKFLOW.md`](../docs/EXPORT_DETERMINATION_WORKFLOW.md)).  
2. After LSO OD: order S-03.  
3. Order I-01, S-04, interlock hardware.  
4. Hold L-01 until export memo + LSO ALIGN authorization path documented.  
5. Update this file with PO numbers — **do not mark RECV without physical receipt**.
