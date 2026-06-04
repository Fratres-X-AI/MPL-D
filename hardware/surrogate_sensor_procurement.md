# Surrogate Sensor Procurement — Phase 0 Minimum Set

**Maturity:** Preliminary Design — three classes mapped to purchasable representative hardware. **No units procured; no spectral or dazzle characterization performed.**

Aligns with `docs/ARCHITECTURE.md` Phase 0 Minimum Surrogate Sensor Set.

---

## Class 1 — Unfiltered silicon CMOS

| Field | Planning value |
|-------|----------------|
| **Role** | Bound 532 nm and 940 nm on leaky NIR path |
| **Representative products (examples, not endorsed)** | RunCam Nano / Foxeer Razer micro FPV cameras (no IR-cut variant); Raspberry Pi HQ Camera (remove IR filter module if present — **document modification**) |
| **Interface** | USB capture card or CSI for fixed-exposure test mode |
| **Test config** | Disable auto-exposure if possible; record fixed gain/exposure metadata per T-03 |
| **Limitation** | FPV boards vary; filter status must be verified with simple IR LED test |

---

## Class 2 — IR-cut filtered CMOS

| Field | Planning value |
|-------|----------------|
| **Role** | Test NIR-primary failure mode; validate 532 nm path |
| **Representative products** | DJI-compatible integrated camera modules (daylight); Logitech C920-class webcam (factory IR-cut); any UAS gimbal camera spec sheet confirming IR-cut |
| **Test config** | Default AGC on — represents operational behavior |
| **Limitation** | Not military hardened; filtered bandpass **unknown** without datasheet |

---

## Class 3 — NIR-augmented / low-light path

| Field | Planning value |
|-------|----------------|
| **Role** | Bound 850–940 nm effectiveness on IR-assisted stacks |
| **Representative products** | Sony Starvis-class USB board camera (IMX290/IMX327 family — **verify** NIR QE from sensor datasheet); dedicated 850 nm illuminator + Starvis combo for low-light mode |
| **Test config** | Test with IR illuminator on/off |
| **Limitation** | SWIR (>1400 nm) sensors **not** in minimum set — separate program if required |

---

## Pass/fail criteria (Phase 0 — draft)

| Class | Dazzle indicator (qualitative) | Fail implication |
|-------|-------------------------------|------------------|
| 1 Unfiltered | Visible saturation/bloom in captured frame at logged irradiance | Wavelength trade inconclusive — repeat measurement |
| 2 IR-cut | No effect at 940 nm at same bench geometry where Class 1 saturated | **940 nm single-band fails** filtered EO — 532 nm or dual-band gate |
| 3 NIR-augmented | Measure separately from Class 2 | Informs NIR vs visible down-select |

**No numeric irradiance threshold is set** until T-02/T-03 data exist.

---

## Recommended next actions

1. Procure one unit per class minimum; log serial, firmware, and filter verification photos.
2. Add sensor datasheets to repo under `hardware/datasheets/` (gitignored if export-sensitive — policy TBD).

## Open questions / gaps

- Fixed-exposure mode availability per camera firmware.
- Whether Class 3 Starvis module represents threat UAS or only commercial low-light.
