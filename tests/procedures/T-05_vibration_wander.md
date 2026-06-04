# T-05 Vibration Table — Detailed Procedure

**Maturity:** Preliminary Design — not executed.

**Links:** REQ-E-002, R-VIB-001

---

## Setup

- Payload mock on isolation feet mounted to vibration table.
- Pointer laser or low-power 940 nm ALIGN through pattern optics at 2 m target grid.
- Accelerometer on mount.

## Sweep

| Freq [Hz] | Amplitude (table setting) | Duration |
|-----------|----------------------------|----------|
| 5–50 | Low (start) | 30 s sweep |
| 50–200 | Low | 30 s sweep |

LSO must approve any energization during sweep.

## Record

Spot centroid displacement vs time/frequency — camera at 2 m or position sensor.

Compare to `analysis/vibration_wander_model.py` assumptions.

## Pass (Phase 0)

Displacement quantified; R-VIB-001 updated with measured jitter — not engagement pass/fail.
