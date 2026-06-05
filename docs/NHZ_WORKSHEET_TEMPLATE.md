# NHZ Worksheet Template — MPL-D (LSO Use Only)

**Document ID:** MPL-D-NHZ-001  
**Status:** **TEMPLATE — NOT COMPLETED. NO NHZ DISTANCES APPROVED.**

**Configuration:** 940 nm fiber module ~10 W CW rated → collimator → static 3×3 DOE → output window + zero-order dump  
**Gate:** G-SAF-02

---

## LSO certification block

| Field | Value |
|-------|-------|
| LSO name | **UNASSIGNED** |
| Date of analysis | — |
| IEC 60825-1 edition applied | — |
| Configuration ID / git commit | — |
| Signature | — |

**Until signed, G-SAF-02 remains OPEN.**

---

## 1. Measured accessible emission (LSO to complete at bench)

| Path | λ [nm] | P_accessible [W] | Measurement method | Date | Operator |
|------|--------|------------------|-------------------|------|----------|
| Primary beamlet (max) | | | | | |
| Zero-order port | | | | | |
| Stray reflection (worst) | | | | | |

**Planning note:** Do not use link-budget target irradiance as ocular exposure substitute.

---

## 2. Beam geometry (measured)

| Parameter | Value | Instrument | Uncertainty |
|-----------|-------|------------|-------------|
| Collimated beam diameter @ aperture | | | |
| Half-angle divergence θ (per beamlet) | | | |
| Zero-order angular offset | | | |
| Pattern grid angular span | | | |

---

## 3. NHZ boundary distances (LSO computed — fill when complete)

| Zone | Distance from reference point | Reference point | Controls required |
|------|------------------------------|-----------------|-------------------|
| NHZ boundary | **TBD** | | |
| Alignment zone | **TBD** | | |
| Bystander exclusion | **TBD** | | |

---

## 4. Laser classification (LSO official)

| Classification | — |
| Accessible emission limits applied | — |
| Product / open-beam configuration | Open-beam bench |

---

## 5. Controls required before energization

| Control | Required | Implemented (Y/N) | Date verified |
|---------|----------|-------------------|---------------|
| Hardware key interlock | Yes | N | |
| E-stop | Yes | N | |
| Beam blocks all exit paths | Yes | N | |
| Remote firing from outside NHZ | Yes | N | |
| Zero-order dump verified | Yes | N | |
| Eyewear OD ≥ ___ @ 940 nm | LSO sets OD | N | |
| Posted warning signage | Yes | N | |
| Training completed for operators | Yes | N | |

---

## 6. Eyewear specification (LSO)

| Wavelength | Required OD | Manufacturer / model | Procured (Y/N) |
|------------|-------------|----------------------|----------------|
| 940 nm | **TBD by LSO** | | N (S-03 SPEC) |
| 532 nm (if used) | **Separate pair — TBD** | | N |

---

## 7. Pulse / duty limits approved by LSO

| Parameter | Approved value | Notes |
|-----------|----------------|-------|
| Max pulse duration | | |
| Max duty cycle | | |
| Max power level per session | ALIGN / LOW / FULL | |

---

## 8. Attachments (LSO to add)

- [ ] Lab layout sketch with NHZ overlay  
- [ ] Power meter calibration certificate  
- [ ] DOE zero-order measurement at ALIGN  
- [ ] Session authorization log reference  

---

**Related:** [`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md) · [`phase0_safety_case_draft.md`](phase0_safety_case_draft.md)
