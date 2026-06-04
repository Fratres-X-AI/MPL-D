# NIR 940 nm Link Budget Notes — AeroDiode-Class Candidate

**Maturity:** Preliminary Design — first-order calculations using vendor-stated diode parameters and conservative optical assumptions. **No measured beam profile, no sensor dazzle test, no atmospheric campaign data.**

**Warning:** Informal claims that “10 W at 940 nm easily dazzles at 1000 m” are **not supported** by this document. See computed bounds below.

---

## 1. Input parameters (vendor-stated, unverified on bench)

| Symbol | Value | Source |
|--------|-------|--------|
| P_opt | 10 W (CW rating) | AeroDiode 940 nm 10 W Model 2 datasheet (typ) |
| λ | 940 nm | Vendor |
| η_wp | 0.50 (typ), budget 0.35–0.50 | Vendor typ; use 0.40 for nominal planning |
| P_elec | 11.5 A × 1.7 V ≈ 19.6 W (typ) | Vendor |
| Q_diss | P_elec − P_opt ≈ 9.6 W (typ @ 50% η) | First-order |
| Fiber core | 105 µm, NA 0.22 | Vendor |
| Collimated beam diameter (vendor collimator claim) | ~12 mm (COL010 class) | Vendor marketing — **must measure** |

---

## 2. Divergence estimates (multimode — high uncertainty)

Multimode fiber output is **not** diffraction-limited. Two bounds:

### 2.1 Geometric (optimistic if well collimated)

If collimator output diameter D_beam ≈ 12 mm and fiber etendue is preserved roughly:

Half-angle θ_geo ≈ (core_radius / focal_eff) — order of magnitude comparable to NA after collimation scaling.

Using NA 0.22 and magnification to 12 mm beam (radius 6 mm), rough half-angle:

```
θ ≈ (105e-6 / 2) / f_eff  ... from fiber acceptance
```

**Planning bracket for MPL-D until measured:** θ_half = **0.5–3 mrad** (wider than diffraction limit below).

### 2.2 Diffraction-limited floor (NOT achievable with 105 µm multimode fiber)

```
θ_diff ≈ λ / (π w₀)  with w₀ = 6 mm
θ_diff ≈ 9.4e-7 / (π × 0.006) ≈ 5.0e-5 rad ≈ 0.05 mrad
```

**Do not** use θ_diff for link budget — it understates divergence by an order of magnitude or more for multimode sources.

---

## 3. Irradiance at range (single collimated beam, no DOE split)

On-axis peak irradiance (Gaussian approximation):

```
I(R) ≈ 2 P_opt / (π w(R)²)
w(R) ≈ R × θ_half   (far field, w₀ negligible)
```

| R [m] | θ = 0.5 mrad, P = 10 W | θ = 1 mrad | θ = 3 mrad |
|-------|------------------------|------------|------------|
| 100 | ~85 W/m² | ~21 W/m² | ~2.4 W/m² |
| 500 | ~3.4 W/m² | ~0.85 W/m² | ~0.09 W/m² |
| 1000 | ~0.85 W/m² | ~0.21 W/m² | ~0.024 W/m² |

Apply Beer-Lambert clear-air T(R) ≈ exp(−0.0001 × R) (σ = 0.1 km⁻¹ planning):

| R [m] | I_eff @ θ=1 mrad (approx) |
|-------|---------------------------|
| 500 | ~0.81 W/m² |
| 1000 | ~0.19 W/m² |

---

## 4. Multi-point DOE penalty (MPL-D architecture)

If static DOE splits into N = 9 beamlets with η_DOE = 0.75 and uniform split:

```
P_beamlet ≈ P_opt × η_DOE / N ≈ 10 × 0.75 / 9 ≈ 0.83 W per beamlet
```

Per-beamlet irradiance scales linearly with power — **~12× lower** than single-beam 10 W table at same θ and R.

At R = 500 m, θ = 1 mrad: I_beamlet ≈ 0.07 W/m² (order of magnitude).

**Conclusion:** 10 W CW into a 9-spot DOE **does not** automatically reproduce single-beam irradiance tables. Multi-point requirement trades peak I for coverage — this is intentional but **reduces** range-to-saturate unless θ or P_opt increases.

---

## 5. Pulsed operation (duty cycle)

Average electrical load:

```
P_elec_avg = duty × P_elec_peak
```

Example: 0.5 s burst every 10 s at full 10 W → duty = 5% → P_elec_avg ≈ 1 W (typ efficiency path).

Peak thermal load during burst remains ~10 W dissipated class — ram-air must handle **peak**, not average.

**No** dazzle effectiveness vs pulse width has been modeled for representative drone cameras in this repo.

---

## 6. Comparison to informal 1000 m claim

| Statement | Assessment |
|-----------|------------|
| “10 W plenty for 1000 m short pulses” | **Unverified.** Depends on θ, DOE split, sensor F/#, AGC, filters, and exposure time — none measured |
| Wu et al. km-class results | Different experimental setup; **not** proof for this stack |
| Kuantama 23.5 mW @ 5 m | Short range + tracking; **not** scalable proof |

---

## 7. Recommended next actions

1. Measure θ_half and spot profile after COL010 or selected collimator at **low power** alignment.
2. Re-run table in Section 3 with measured θ; expand uncertainty bands ±50%.
3. Add DOE efficiency and spot count from T-01; update Section 4.
4. Compare I_eff to surrogate camera saturation tests (T-03) — do not infer from literature alone.

## Open questions / gaps

- Sensor full-well and AGC transfer function for each surrogate class.
- Whether 0.1–3 s bursts at measured I_eff produce dazzle on IR-cut filtered sensors (class 2 surrogate).
