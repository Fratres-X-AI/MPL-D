# T-02 Irradiance vs Range — Detailed Procedure

**Maturity:** Preliminary Design — **not executed.** Analytical pre-check: `analysis/prebench_t02_analytical_report.md`.

**Links:** REQ-F-004, REQ-P-001, REQ-E-003

---

## Setup

- Calibrated power meter + 940 nm sensor.
- Ranges: 1, 2, 5, 10 m along optical axis (indoor only).
- LSO sets max power for this test.

## Steps

| Step | Range [m] | Action | Record P [W], I [W/m²] |
|------|-----------|--------|------------------------|
| 1 | 1 | Stable emission; meter at center of one beamlet | |
| 2 | 2 | Repeat | |
| 3 | 5 | Repeat | |
| 4 | 10 | Repeat | |

Repeat for center beamlet and corner beamlet if time permits.

## Pass

Measured I(R) within ±50% of model **or** model updated with measured θ and η_DOE documented.

## Compare

Run `analysis/power_thermal_budget.py` and `nir_940nm_link_budget_notes` with measured θ.
