# Analysis Validation Status — MPL-D

**Maturity:** Preliminary Design — analytical artifacts inventory with validation state.

**Evidence / analysis status:** Scripts run locally; outputs are **synthetic / first-order only**. No calibration against measured hardware.

**Known gaps:** All models lack bench validation. Dazzle threshold not modeled anywhere in repo.

**Next required action:** After P0 procurement, run T-02 and update this table with log file references.

---

## 1. Model inventory

| Artifact | Type | Inputs | Outputs | Validation status | Uncertainty treatment |
|----------|------|--------|---------|-------------------|----------------------|
| [`power_thermal_budget.py`](../analysis/power_thermal_budget.py) | First-order budget | P_opt, η_wp (planning) | P_elec, Q_diss | **Unvalidated** | η_wp bracket 0.15–0.50; label all prints as estimates |
| [`thermal_pulse_model.py`](../analysis/thermal_pulse_model.py) | Transient soak (planning) | Duty, sink R_th (assumed) | T_junction vs time | **Unvalidated** | R_th ±50% until measured |
| [`vibration_wander_model.py`](../analysis/vibration_wander_model.py) | Spot displacement | Δθ, R | Lateral miss [m] | **Unvalidated** | Δθ from T-05 pending |
| [`nir_940nm_link_budget_notes.md`](../analysis/nir_940nm_link_budget_notes.md) | Link budget | P, θ, σ, N, η_DOE | I(R) tables | **Unvalidated** | θ: 0.5–3 mrad bracket; multimode source |
| [`beam_propagation_notes.md`](../analysis/beam_propagation_notes.md) | Physics notes | Literature σ classes | Qualitative bounds | **Unvalidated** | No locale-specific σ |
| [`prebench_t02_analytical_report.md`](../analysis/prebench_t02_analytical_report.md) | Pre-check T-02 | Model inputs | Expected vs measure plan | **Pre-bench only** | Explicitly not T-02 pass |
| [`PHYSICS_BASIS.md`](PHYSICS_BASIS.md) | Equation reference | — | Formulas + example | **Unvalidated** | Example ±order of magnitude |

---

## 2. Sensitivity notes (quantitative estimates)

### 2.1 Irradiance at range (940 nm, single beam)

**Baseline (planning):** P=10 W, θ=1 mrad, R=500 m, σ=0.1 km⁻¹ → I_eff ≈ **0.8 W/m²** (order of magnitude).

| Parameter perturbation | Direction on I_eff @ 500 m | Notes |
|------------------------|----------------------------|-------|
| θ: 0.5 → 3 mrad | **−36× to −4×** (spot area scales θ²) | Dominant geometric sensitivity |
| P_opt: 10 → 5 W | **−2×** | Linear |
| σ: 0.05 → 0.2 km⁻¹ | **−5% to −18%** at 500 m | Secondary vs θ |
| 9-spot DOE, η=0.75 | Per-beamlet **~−9×** vs single beam | Coverage vs peak trade |

**Validation required:** Measured θ_half at alignment power; measured η_DOE and zero-order fraction.

### 2.2 Power / thermal

| Parameter | Nominal | Low bound | High bound | Impact |
|-----------|---------|-----------|------------|--------|
| η_wp | 0.40 | 0.35 | 0.50 | Q_diss at 10 W opt: ~15–19 W |
| Duty cycle | 10% / 60 s | 5% | 20% | Mission energy drain uncertain ±2× |

Cross-reference: R-THM-001, R-PWR-001, [`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md) (duty limits set by LSO, not model).

### 2.3 Atmospheric

Models omit: turbulence (Cn²), multiple scattering, fog. Outdoor engagement variance **not bounded** in repo. Cross-reference: R-ATM-001.

### 2.4 Sensor dazzle

**No model exists.** Do not infer operational effectiveness from I(R) tables. Cross-reference: R-EFF-001, T-03.

---

## 3. Analysis ↔ requirement traceability

| Requirement | Primary analysis | Test to validate |
|-------------|----------------|------------------|
| REQ-F-004 | nir_940nm_link_budget, power_thermal_budget | T-02 |
| REQ-P-001 | beam_propagation, prebench_t02 | T-02 |
| REQ-E-001 | thermal_pulse_model | T-04 |
| REQ-E-002 | vibration_wander_model | T-05 |
| REQ-E-003 | PHYSICS_BASIS | T-02 outdoor (if ever authorized) |
| REQ-S-004 | thermal_pulse_model | T-04 |

---

## 4. Prohibited uses of analysis outputs

1. **NHZ standoff distances** — use LSO analysis only ([`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md)).
2. **Operational engagement range certification** — requires validated sensor data not in scope.
3. **Threat effectiveness claims** — surrogate bench only (Phase 0).

---

## 5. Next required actions

1. Record model version hash / commit ID in test records when T-01–T-05 execute.
2. Update validation status column to **Partially validated** only when measured data within stated uncertainty brackets.
3. If model error >±50%, revise assumptions in [`ASSUMPTIONS_AND_CONSTRAINTS.md`](ASSUMPTIONS_AND_CONSTRAINTS.md).
