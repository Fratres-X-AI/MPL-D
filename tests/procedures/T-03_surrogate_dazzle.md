# T-03 Surrogate Sensor Dazzle — Detailed Procedure

**Maturity:** Preliminary Design — not executed.

**Links:** REQ-F-002, REQ-P-002, R-EFF-001

---

## Setup

Three surrogate classes per `hardware/surrogate_sensor_procurement.md` — one session per class minimum.

Fixed exposure / documented AGC state per camera.

## Steps

| Step | Action | Record |
|------|--------|--------|
| 1 | Baseline image, laser SAFE | REF_*.png |
| 2 | LSO-approved pulse at 2 m | DAZZLE_*.png |
| 3 | Log irradiance at sensor location (T-02 meter) | I [W/m²] |
| 4 | Repeat for Class 1, 2, 3 | |

## Pass (Phase 0)

Qualitative saturation/bloom on Class 1; document **pass/fail/no-effect** on Class 2 and 3 for wavelength trade.

## Fail implication

940 nm no effect on Class 2 → NIR single-band trade fails for filtered EO.

**Do not** claim operational range or threat effectiveness.
