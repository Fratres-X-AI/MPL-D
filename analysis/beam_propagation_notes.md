# Beam Propagation Notes — First-Order Analysis

**Maturity:** Concept. Supporting evidence: Analytical approximations only; no wave-optics simulation, no measured beam profiles, no atmospheric test data.

**Scope:** Non-kinetic sensor-denial link budget support for the Counter-UAS Multi-Point Laser Dazzler Prototype. Defensive EO/IR dazzle context only.

---

## 1. Purpose

These notes document assumptions behind [`power_thermal_budget.py`](power_thermal_budget.py) and bound expected irradiance at target range for multi-point patterns. They do **not** establish engagement success criteria.

---

## 2. Beam Model (Simplified)

### 2.1 Divergence and spot size

Half-angle divergence θ (radians) and range R (meters):

```
w(R) ≈ R · tan(θ) ≈ R · θ     (small-angle, waist neglected)
```

Typical planning bounds for compact drone-mountable optics:

| Parameter | Conservative range | Basis |
|-----------|-------------------|-------|
| Half-angle θ | 1–5 mrad | Compact diode/DOE assemblies; not measured here |
| Waist w₀ | 0.5–2 mm | Module-dependent; often negligible vs R·θ beyond ~50 m |

**Omitted:** M² beam quality degradation, thermally induced divergence drift, vibration-induced pointing error.

### 2.2 On-axis irradiance (single Gaussian beamlet)

```
I = 2P / (π w(R)²)    [W/m²]
```

For N equal-power non-overlapping beamlets: use P/N per beamlet unless pattern overlap is characterized by measurement.

**Omitted:** Speckle, interference between beamlets, partial coherence effects from DOE splitters.

---

## 3. Atmospheric Transmission

Beer-Lambert law (single path, no multiple scattering):

```
T(R) = exp(−β R)
```

β = extinction coefficient [m⁻¹]. Convert from km⁻¹: β = σ / 1000.

| Condition | σ (km⁻¹) indicative range | Uncertainty |
|-----------|---------------------------|-------------|
| Clear, 532 nm, sea level | 0.05–0.2 | High — locale and aerosol loading unknown |
| Haze / moderate pollution | 0.3–1.0 | Very high |
| Fog / rain | >> 1 | Not modeled; likely defeats system at tactically relevant ranges |

**Omitted:** Turbulence (Cn²), scintillation, beam wander, wavelength-specific aerosol models.

---

## 4. Multi-Point Pattern Considerations

| Approach | Advantage | Limitation |
|----------|-----------|------------|
| Static DOE (diffractive optical element) | No moving parts; low SWaP | Efficiency loss 60–85% typical (vendor-dependent); zero-order leakage safety risk |
| Multiple discrete emitters | Per-beam control possible | Alignment drift; wiring/thermal complexity |
| Galvo scanning | Flexible pattern | Mass, power, vibration sensitivity; rejected for Phase 0 simplicity |

Pattern fill factor on target sensor FOV is unknown without tracking integration. A static pattern may miss off-axis sensors on maneuvering targets.

---

## 5. Conservative Example Bounds (Unvalidated)

Assumptions: P_opt = 5 W total, 9 beamlets, θ = 2 mrad, clear air σ = 0.1 km⁻¹.

| Range [m] | T | Peak I per beamlet [W/m²] (order of magnitude) |
|-----------|---|--------------------------------------------------|
| 100 | ~0.99 | ~10⁻² |
| 500 | ~0.95 | ~10⁻³ |
| 1000 | ~0.90 | ~10⁻⁴ |

These values are **not** engagement thresholds. Camera saturation depends on exposure, f-number, filter stack, and sensor dynamic range — none modeled here.

---

## 6. Known Gaps

1. No validated open data mapping irradiance → operational dazzle against modern FPV or military UAS cameras under motion.
2. No measurement of zero-order DOE leakage for eye-safety zoning.
3. No platform vibration transfer function to beam wander at range.

---

## Recommended next actions

1. Run `power_thermal_budget.py` and record outputs; do not treat plot as design authority.
2. Obtain vendor datasheets for candidate emitters and DOEs; replace assumed η and divergence with datasheet bounds.
3. If bench testing proceeds, measure spot size and irradiance at 10 m, 50 m, 100 m with calibrated power meter and beam profiler.

## Open questions / gaps

- What minimum irradiance (with uncertainty) causes measurable image degradation for representative surrogate cameras?
- How does multi-beamlet overlap affect peak vs average sensor exposure?
