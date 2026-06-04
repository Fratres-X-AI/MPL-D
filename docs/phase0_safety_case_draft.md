# Phase 0 Laser Safety Case — DRAFT (Not Approved)

**Project:** Counter-UAS Multi-Point Laser Dazzler Prototype  
**Configuration:** 940 nm fiber-coupled ~10 W class → collimator → static DOE (3×3) → output window + zero-order dump  
**Gate:** G-SAF-02  
**Standard:** IEC 60825-1 (framework reference — LSO must apply current edition)

**Maturity:** Draft safety case — inputs and controls documented. **No LSO signature. No NHZ boundary distances calculated or approved in this document.** **Not authorized for full-power operation.**

---

## 1. Configuration summary

| Parameter | Planning value | Source |
|-----------|----------------|--------|
| Wavelength | 940 nm (935–945 nm) | AeroDiode-class datasheet |
| CW optical power (max) | 10 W | Vendor rating |
| Pattern | 3×3 DOE; η_DOE ~0.75 planning | Optical layout |
| Per-beamlet power (planning) | ~0.83 W | 10 × 0.75 / 9 |
| Collimated beam diameter | ~12 mm (until measured) | COL010-class claim |
| Divergence (planning bracket) | 0.5–3 mrad half-angle | Must measure |
| Pulse profile | 0.1–3 s burst; ≤10% duty / 60 s | Pulse control spec |
| Environment | Indoor controlled optics lab | Phase 0 scope |

---

## 2. Hazard identification

| Hazard | Mechanism | Severity |
|--------|-----------|----------|
| Direct intrabeam | 940 nm NIR — **invisible** to eye | Retinal injury |
| Specular reflection | Optical components, window, target optics | Retinal injury |
| Zero-order leakage | DOE undiffracted order | Intrabeam / specular |
| Multi-beamlet exposure | Nine spots — cumulative exposure | Retinal injury |
| Electrical | 11.5–13 A driver circuit | Shock, fire |
| Thermal | ~10 W dissipated at peak | Burn, component failure |

**940 nm is not eye-safe at 10 W class for any open-beam path.** Invisible wavelength increases accidental exposure risk vs visible.

---

## 3. Classification (qualitative — LSO must assign official class)

**LSO determination required.** Planning expectation for open-beam 10 W NIR multimode:

- Accessible emission at source and uncontrolled paths is consistent with **Class 4** or high-hazard accessible emission limits under IEC 60825-1 for unrestricted open-beam bench work.
- **Do not** assume Class 3B at full power without LSO measurement of accessible emission and divergence after DOE split.

**This draft does not substitute for LSO classification testing.**

---

## 4. Nominal Hazard Zone (NHZ) — methodology only

**No NHZ distances are approved in this draft.** LSO shall compute NHZ using:

- Measured accessible emission at each beamlet and zero-order port
- Measured divergence after collimator and DOE
- Worst-case pulse duty per approved SOP
- Worst-case operator and bystander positions in lab layout sketch (to be attached by LSO)

**Forbidden:** Using irradiance-at-target link budget (`analysis/nir_940nm_link_budget_notes.md`) as NHZ standoff — that models target plane, not ocular hazard at bench.

---

## 5. Engineering controls (required before energization)

| Control | Requirement | Status |
|---------|-------------|--------|
| Hardware key enable | REQ-S-002 | Specified; not built |
| E-stop | Cuts driver power | Specified; not built |
| Interlock loop | Door/enclosure | Lab-dependent |
| Zero-order dump | REQ-S-003 | Defined in optical layout; not inspected |
| Beam blocks | All specular exit paths | Lab setup TBD |
| Remote firing | Operator outside NHZ | SOP required |

---

## 6. Administrative controls

| Control | Requirement | Status |
|---------|-------------|--------|
| LSO assignment | G-SAF-01 | **OPEN** |
| Written SOP | G-SAF-03 | Draft exists |
| Operator training log | Before first session | Empty |
| Eyewear | OD at 940 nm per LSO | Not specified numerically here |
| Signage | Laser controlled area | Lab TBD |

---

## 7. Alignment / reduced-power protocol (LSO to set ceiling)

**Before full 10 W:**

1. LSO defines maximum alignment current (e.g., 1–5% of rated power — **LSO sets numeric limit**).
2. Verify zero-order path blocked at alignment power before scaling.
3. Confirm power meter calibration at 940 nm.
4. Document spot pattern at 2 m before full-power surrogate tests.

---

## 8. Protocol IV / ROE

Defensive sensor-denial research on surrogate cameras only. No human targeting. No outdoor emission without separate authorization (R-REG-001).

---

## 9. Approval block

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Laser Safety Officer | **PENDING** | — | — |
| Program lead | **PENDING** | — | — |

**Until signed, G-SAF-02 remains OPEN and G-ENR remains BLOCKED.**

---

## Recommended next actions

1. LSO site visit or lab layout review; attach sketch to this case.
2. LSO sets alignment-power ceiling and approves NHZ boundaries (separate attachment).
3. Sign jointly with program lead before P0 energization.
