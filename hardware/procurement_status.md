# Phase 0 Procurement Status

**Maturity:** Phase 0 active — **ordering not executed in repository.** No received goods.

**Reference:** [`phase0_procurement_list.md`](phase0_procurement_list.md)

---

## Status legend

| Status | Meaning |
|--------|---------|
| SPEC | Specified; not ordered |
| ORDER | PO issued (record PO # when true) |
| RECV | Received; inspection pending |
| OK | Inspected; bench-ready |

---

## P0 items (required before energization)

| ID | Item | Status | Notes |
|----|------|--------|-------|
| L-01 | 940 nm 10 W module | SPEC | Export review R-EXP-001 before order |
| L-02 | Diode driver ≥13 A | SPEC | Match L-01 |
| O-01 | 940 nm collimator | SPEC | |
| O-02 | DOE 3×3 | SPEC | Long lead — order after θ measured or vendor input beam spec |
| O-03 | Zero-order dump | SPEC | |
| I-01 | Power meter + sensor | SPEC | |
| S-03 | Eyewear 940 nm | SPEC | OD set by LSO — not in repo |
| S-04 | Interlock / blocks | SPEC | |

**G-HW-P0:** **OPEN** (all SPEC)

---

## P1 items (surrogate + full-power dazzle)

| ID | Item | Status |
|----|------|--------|
| Surrogate Class 1–3 | Per surrogate_sensor_procurement.md | SPEC |
| O-05 | Beam profiler | SPEC (rent OK) |

**G-SAF-05:** **OPEN**

---

## Recommended next actions

1. Complete export control screen (R-EXP-001).
2. LSO approve safety case before L-01 order at full rating.
3. Order I-01, S-03, S-04, interlock hardware first for low-power commissioning path.
