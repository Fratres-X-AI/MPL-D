# Phase 0 Procurement List — Bench Proof-of-Concept

**Project:** Counter-UAS Multi-Point Laser Dazzler Prototype  
**Maturity:** Preliminary Design — line items defined for Phase 0 bench build. **No purchase orders placed; no received-goods inspection records.**

**Leading architecture (planning):** 940 nm fiber-coupled 10 W class diode → collimator → static DOE (3×3 or 5-spot) → output window + zero-order dump. Alternate visible 532 nm path retained as bench comparison if budget allows.

---

## Priority tiers

| Tier | Meaning |
|------|---------|
| P0 | Required before any open-beam alignment above alignment power |
| P1 | Required before full-power dazzle surrogate tests (T-03) |
| P2 | Required before vibration test (T-05) or thermal soak logging |

---

## Laser source and driver (P0)

| ID | Item | Spec / class | Qty | Est. cost (order of magnitude) | Evidence |
|----|------|--------------|-----|-------------------------------|----------|
| L-01 | 940 nm 10 W fiber-coupled diode module | AeroDiode Model 2 class or equivalent; 105 µm core, SMA905 | 1 | $475–600 | Vendor datasheet |
| L-02 | Laser diode driver | CW/pulsed, ≥13 A peak, 1.8 V min; interlock input; TTL enable | 1 | $200–800 | **Not selected** — must match L-01 |
| L-03 | Thermistor / case temperature sensor | On heat sink, logged | 1 | $20–50 | T-04 |

**Alternate (comparison only):** 532 nm DPSS 2–5 W module — P2 if dual-band bench comparison authorized by LSO.

---

## Optics (P0 alignment / P1 full power)

| ID | Item | Spec / class | Qty | Notes |
|----|------|--------------|-----|-------|
| O-01 | Fiber collimator | COL010-class or Thorlabs F280APC-940 / equivalent 940 nm rated | 1 | Measure θ_half before DOE |
| O-02 | Static DOE / beam splitter | 3×3 or 5-spot grid; 940 nm design wavelength; custom or catalog | 1 | Lead time risk R-SUP-001 |
| O-03 | Zero-order beam dump / block | Absorptive for 940 nm at planned power | 1 | REQ-S-003 |
| O-04 | Output window | AR-coated 940 nm; clear aperture ≥ collimated beam | 1 | Last optical surface |
| O-05 | Beam profiler or scanning slit | Calibrated at 940 nm | 1 borrow/rent | T-01, T-02 |

---

## Surrogate sensors (P1)

See [`surrogate_sensor_procurement.md`](surrogate_sensor_procurement.md).

---

## Instrumentation (P0–P1)

| ID | Item | Qty | Test |
|----|------|-----|------|
| I-01 | Laser power meter + 940 nm sensor | 1 | T-02 |
| I-02 | Calibrated neutral density filters | Set | Alignment |
| I-03 | Data logger / scope | 1 | T-04 current draw |
| I-04 | IR viewer or compliant IR card (optional) | 1 | NIR alignment safety |

---

## Safety (P0 — before energization)

| ID | Item | Notes |
|----|------|-------|
| S-01 | LSO assignment | G-SAF-01 — administrative, not purchasable |
| S-02 | NHZ analysis completion | G-SAF-02 — before full power |
| S-03 | Wavelength-matched laser eyewear | OD per LSO; separate sets if dual wavelength |
| S-04 | Beam blocks, curtains, interlock hardware | REQ-S-002 |
| S-05 | Key switch or hardware enable | REQ-S-002 |

---

## Mechanical / thermal (P2)

| ID | Item | Notes |
|----|------|-------|
| M-01 | Aluminum heat sink + ram-air scoop mock | Bench only; not flight-qualified |
| M-02 | Optical bench mounts (kinematic) | Alignment |
| M-03 | Elastomer isolation feet | Vibration table prep T-05 |

---

## Budget envelope (unvalidated)

| Category | Planning range |
|----------|----------------|
| Laser + driver + optics | $2k–8k |
| Instrumentation (excl. profiler rental) | $1k–4k |
| Surrogate cameras | $200–800 |
| Safety / misc | $500–2k |
| **Total Phase 0 parts (order of magnitude)** | **$4k–15k** |

---

## Recommended next actions

1. Assign LSO; complete NHZ for 940 nm + DOE configuration before L-01 full-power operation.
2. Issue PO for L-01, O-01, I-01, S-03/S-04 after NHZ alignment-power limits defined.
3. Order DOE (O-02) with measured collimator beam diameter and wavelength.

## Open questions / gaps

- Export control review before international vendor shipment (R-EXP-001).
- DOE supplier and grid geometry not frozen — blocks O-02 order.
