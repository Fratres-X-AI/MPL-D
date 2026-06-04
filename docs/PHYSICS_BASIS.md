# Physics Basis — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Concept. Supporting evidence: First-order analytical equations only. No Monte Carlo propagation, no hardware validation, no sensor response models.

**Purpose:** Document the physics assumptions underlying range, irradiance, atmospheric, and thermal estimates in this repository. All numerical examples are conservative planning bounds, not performance guarantees.

---

## 1. Far-Field Beam Divergence and Spot Size

For a collimated or weakly focusing exit aperture with half-angle divergence θ (radians):

```
w(R) = sqrt(w₀² + (R · tan θ)²) ≈ R · θ     when w₀ << R·θ
```

| Symbol | Meaning | Typical planning bounds |
|--------|---------|-------------------------|
| w(R) | 1/e² beam radius at range R | Derived |
| w₀ | Beam waist at exit | 0.5–2 mm (module-dependent; unverified) |
| θ | Half-angle divergence | 1–5 mrad (compact drone optics class) |
| R | Slant range to target | 50–1000 m (engagement envelope TBD) |

**Simplification:** Treat each beamlet as Gaussian with scalar θ. **Omitted:** M² ≠ 1, astigmatism, thermal lensing, vibration-induced pointing.

---

## 2. On-Axis Irradiance

For a single Gaussian beamlet with optical power P:

```
I(R) = 2P / (π · w(R)²)    [W/m²]
```

For N equal-power beamlets with negligible overlap:

```
I_n(R) = 2(P/N) / (π · w(R)²)
```

**Omitted:** Partial overlap interference, speckle-averaged exposure, sensor pixel integration time effects.

---

## 3. Atmospheric Attenuation (Beer-Lambert)

```
T(R) = exp(−β · R)
β = σ / 1000
```

σ = extinction coefficient [km⁻¹]; β [m⁻¹].

| Condition | σ (km⁻¹) used for planning | Basis |
|-----------|----------------------------|-------|
| Clear | 0.05–0.2 | Public atmospheric optics literature; locale unknown |
| Haze | 0.3–1.0 | Order-of-magnitude degradation |
| Fog/rain | Not modeled | Likely prevents tactically useful engagement |

Effective irradiance at range:

```
I_eff(R) = I(R) · T(R)
```

**Omitted:** Multiple scattering, path-dependent humidity/aerosol models, wavelength-specific absorption lines (except as rolled into σ).

---

## 4. Wall-Plug Efficiency and Thermal Load

```
P_elec = P_opt / η_wp
Q_diss ≈ P_elec − P_opt = P_opt · (1/η_wp − 1)
```

| η_wp (planning) | Interpretation |
|-----------------|----------------|
| 0.15 (lower bound) | Conservative diode module, poor cooling |
| 0.22 (nominal) | Mid-range planning value |
| 0.35 (upper bound) | Well-cooled DPSS/diode; not assumed without datasheet |

**Example (nominal η = 0.22):**

| P_opt [W] | P_elec [W] | Q_diss [W] |
|-----------|------------|------------|
| 2 | ~9 | ~7 |
| 5 | ~23 | ~18 |
| 10 | ~45 | ~35 |

**Omitted:** Driver switching losses separate from laser chip, convective cooling coefficient, altitude derating.

---

## 5. Diffractive Optics Efficiency (If Used)

DOE splitters typically report optical efficiency η_DOE in vendor datasheets (often 60–85% for binary gratings; **not verified for any selected part**).

```
P_pattern = η_DOE · P_in
P_lost = P_in − P_pattern − P_zero_order
```

Zero-order leakage is a **safety and wasted-power** term, not included in dazzle pattern power. Must be measured in Phase 0.

---

## 6. Sensor Dazzle — Deliberately Not Modeled

No equation in this repository predicts operational dazzle success. Relevant omitted phenomena:

- Auto-exposure and auto-gain control (AGC)
- Narrowband/OD laser protective filters on military sensors
- Rolling shutter vs global shutter behavior
- AI-based glare rejection (unvalidated open literature for this application)
- Target motion and line-of-sight occlusion

Public literature does not provide a single irradiance threshold valid across threat UAS EO/IR sensors.

---

## 7. Conservative Numerical Example (Unvalidated)

**Inputs:** P_opt = 5 W total, N = 9 beamlets, θ = 2 mrad, σ = 0.1 km⁻¹, R = 500 m.

```
w(500) ≈ 500 × 0.002 = 1.0 m
I_beamlet ≈ 2 × (5/9) / (π × 1²) ≈ 0.35 W/m² (vacuum)
T(500) ≈ exp(−0.0001 × 500) ≈ 0.95
I_eff ≈ 0.33 W/m²
```

At R = 1000 m: w ≈ 2 m, I_eff drops ~4× further (~0.04 W/m² order of magnitude under same assumptions).

These values **do not** imply effective dazzle at those ranges against any specific sensor.

---

## 8. Explicit Omissions Summary

| Phenomenon | Impact if omitted |
|------------|-------------------|
| Atmospheric turbulence (Cn²) | Irradiance scintillation; peak exposure uncertain ±10 dB or more |
| Platform vibration / jitter | Beam wander; pattern may miss sensor FOV |
| Beam quality M² | Spot size larger than geometric estimate |
| Sensor-specific response | Cannot predict soft-kill outcome |
| Eye-safety NHZ dynamics | Safety case incomplete without LSO analysis |

---

## Recommended next actions

1. Replace assumed η_wp and θ with vendor datasheet bounds for selected modules.
2. Run `analysis/power_thermal_budget.py`; compare outputs to bench measurements when available.
3. If outdoor tests occur, record meteorological visibility and revise σ with measured transmission.

## Open questions / gaps

- Selected wavelength(s) determine σ and safety classification — not fixed in this repository.
- Required irradiance at sensor aperture for surrogate camera saturation — must be measured, not inferred from this document.
