# Pre-Bench T-02 Analytical Report — Link Budget Only

**Maturity:** Analytical pre-check only. **This is NOT T-02 test execution.** No laser energized. No power meter measurements.

**Gate contribution:** Supports G-DOC (documentation) only. **Does not close G-ENR or substitute for T-02.**

**Generated from:** `analysis/power_thermal_budget.py` and `analysis/nir_940nm_link_budget_notes.md`

---

## 1. Configuration modeled

| Parameter | Value |
|-----------|-------|
| Case A | 5 W total, 9 beamlets, θ = 2 mrad |
| Case B | 10 W total, η_DOE = 0.75, 9 beamlets, θ = 1 mrad (940 nm candidate) |
| Atmosphere | σ = 0.1 km⁻¹ clear; haze column in script output for Case A |

---

## 2. Case A output (5 W multi-point)

```
Range [m]    T_clear     I_clear [W/m2]      I_haze [W/m2]
       50     0.9950          35.19               34.49
      100     0.9900           8.75                8.41
      200     0.9802           2.17                2.00
      500     0.9512           0.34                0.28
     1000     0.9048           0.08                0.05
```

Electrical (η=0.22): ~22.7 W peak; ~17.7 W dissipated.

---

## 3. Case B output (940 nm candidate + DOE)

```
P_opt=10 W, eta_DOE=0.75, pattern power=7.5 W
P_elec_peak~25 W @ eta_wp=0.40

R=50 m   I_beamlet_eff~211 W/m2
R=100 m  I_beamlet_eff~53 W/m2
R=500 m  I_beamlet_eff~2.0 W/m2
R=1000 m I_beamlet_eff~0.48 W/m2
```

---

## 4. Acceptance criterion preview (T-02 when hardware exists)

Phase 0 success: measured irradiance within **±50%** of model **or** model updated with measured θ and η_DOE.

**Current state:** No measured data — criterion **not evaluable**.

---

## 5. Explicit gaps

- θ = 1 mrad assumed for Case B; multimode fiber may exceed 3 mrad.
- DOE efficiency not measured.
- No sensor dazzle threshold linked to I_eff.

---

## Recommended next actions

1. After collimator alignment, measure θ and replace Case B inputs.
2. Execute hardware T-02 at LSO-approved power levels; log to `tests/logs/`.
