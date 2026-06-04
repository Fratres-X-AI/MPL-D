# Preliminary Optical Layout — 940 nm DOE Path

**Maturity:** Preliminary Design — stack sequence, planning dimensions, and alignment degrees of freedom documented. **No CAD release, no tolerance stack analysis, no measured beam profile.**

**Evidence:** Vendor datasheet classes (`candidate_components.md`); first-order link budget (`analysis/nir_940nm_link_budget_notes.md`).

---

## 1. Optical train (sequence)

```
[L-01 Diode + fiber] → [O-01 Collimator] → [O-02 DOE] → [O-03 Zero-order dump] + [O-04 Output window] → free space
```

Mechanical stack mounted on [M-01 heat sink] → [M-03 isolation feet] → bench / payload plate.

---

## 2. Planning dimensions (not tolerance-drawn)

| Stage | Parameter | Planning value | Status |
|-------|-----------|----------------|--------|
| Fiber exit | SMA905 interface | Vendor standard | COTS |
| Collimator output | Beam diameter | ~12 mm (COL010-class claim) | **Measure** |
| Collimator output | θ_half | 0.5–3 mrad bracket until measured | Open |
| DOE input | Beam fill | ~90% of clear aperture | Design TBD |
| DOE | Spot count | 9 (3×3) primary; 5-spot alternate | Design TBD |
| DOE | Diffraction efficiency | 60–85% class | Vendor-dependent |
| DOE | Zero-order fraction | **Must measure** — block O-03 | Open |
| Pattern FOV | Total angular spread | 0.5–2° planning | ARCHITECTURE §3 |
| Output window | Clear aperture | ≥ 15 mm | Preliminary |
| Boresight | Mechanical reference | Mount face normal to optical axis | CAD TBD |

---

## 3. Alignment degrees of freedom (bench)

| Adjustment | Purpose |
|------------|---------|
| Collimator X/Y/Z + tip/tilt | Center beam on DOE input |
| DOE tip/tilt | Symmetric spot grid |
| Dump optic position | Capture zero-order only |
| Window normal | Minimize wedge stray reflection |

**Maturity:** Preliminary Design — procedure defined; no alignment record exists.

---

## 4. Vibration / thermal interface

- Diode package bonded to heat sink; fiber strain relief within vendor min bend radius (37.5 mm AeroDiode class).
- Ram-air scoop on sink (bench: fan substitute for T-04 only — **document** if used).
- Isolation feet decouple bench from table; T-05 quantifies pattern wander.

---

## 5. Rejected layout options

| Option | Reason |
|--------|--------|
| Internal gimbal | SWaP + control complexity |
| Scanning mirror after DOE | Deprioritized Phase 0 |
| Common-path visible + NIR without separate hazard case | Safety / NHZ conflict |

---

## Recommended next actions

1. Release CAD block diagram with collimator–DOE spacing from vendor focal lengths.
2. T-01 irradiance map at 2 m validates grid geometry.

## Open questions / gaps

- DOE custom grid period vs supplier catalog part.
- Coating damage threshold at 10 W CW on O-04 if duty cycle exceeds planning.
