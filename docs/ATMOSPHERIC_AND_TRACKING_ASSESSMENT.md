# Atmospheric Effects and Tracking Limitations — MPL-D

**Document ID:** MPL-D-ATM-001  
**Maturity:** Preliminary Design — analytical bounds and explicit program limits. **No outdoor campaign data.**

**Evidence status:** Beer-Lambert first-order in PHYSICS_BASIS; turbulence and scintillation **omitted** from numeric claims.

**Known gap:** Operational outdoor envelope **not certified**. Closed-loop tracking **not in Phase 0**.

---

## 1. Atmospheric effects

### 1.1 Modeled (first-order)

| Effect | Model in repo | Planning parameter | Validation |
|--------|---------------|-------------------|------------|
| Clear-air extinction | Beer-Lambert T(R)=exp(−βR), β=σ/1000 | σ = 0.05–0.2 km⁻¹ | **Unvalidated** — locale unknown |
| Multi-spot split | Per-beamlet I ∝ (P/N)/w(R)² | N=9, η_DOE planning | **Unvalidated** |

### 1.2 Not modeled (explicit omissions)

| Effect | Impact | Program stance |
|--------|--------|----------------|
| Cn² turbulence / scintillation | Irradiance variance ±10 dB or more at range | **Not bounded** — R-ATM-001 High |
| Fog, rain, heavy haze | Likely prevents useful engagement | Phase 0 **indoor only** |
| Multiple scattering | Further attenuation | Omitted |
| Wavelength-specific absorption lines | Rolled into σ only | Uncertain |

### 1.3 Conservative planning statement

Indoor bench results at 2–10 m **do not** predict outdoor performance at 100–1000 m. Any outdoor test requires separate authorization (R-REG-001), meteorological logging, and revised σ from measurement — **not planned in Phase 0**.

### 1.4 Sensitivity (order of magnitude)

At fixed P and θ, I_eff ∝ T(R). For σ=0.1 km⁻¹ vs 0.2 km⁻¹ at R=500 m: T drops ~5% vs ~10% — **secondary** to θ uncertainty (0.5–3 mrad bracket spans ~36× in spot area).

---

## 2. Closed-loop tracking

### 2.1 Phase 0 architecture

| Capability | Status | Requirement |
|------------|--------|-------------|
| Static multi-point pattern | **In scope** | REQ-F-001 |
| Host boresight pointing only | **In scope** | CONOPS |
| Gimbal on payload | **Out of scope** | ARCHITECTURE |
| Track-to-dazzle closed loop | **Out of scope** | Phase 0 exclusion |

### 2.2 R-TRK-001 assessment

| Factor | Effect |
|--------|--------|
| Maneuvering target | Target may leave fixed pattern FOV faster than host repositions |
| Static pattern width | Partial mitigation — increases capture volume vs single beam |
| Vibration (R-VIB-001) | Additional decentering — compounds miss |

**Phase 0 acceptance:** Program **accepts** static-pattern miss risk for bench surrogate work only. **Does not** accept operational engagement claim without Phase 1+ tracking or measured miss-rate data.

### 2.3 Phase 1+ options (not authorized)

| Option | SWaP / complexity | Evidence required to adopt |
|--------|-------------------|----------------------------|
| Host-level track cue + pulse on lock | Moderate | Miss rate quantification |
| Payload gimbal | High | Vibration + EMI data |
| Scanning pattern (galvo/MEMS) | High | R-DOE + safety review |

**Decision gate:** Document static-pattern miss rate from Phase 0 geometry + T-05 before funding tracking hardware.

---

## 3. Traceability

| Risk | This document |
|------|---------------|
| R-ATM-001 | §1 |
| R-TRK-001 | §2 |
| R-VIB-001 | §2.2 (compound) |

**Analysis:** [`ANALYSIS_VALIDATION_STATUS.md`](ANALYSIS_VALIDATION_STATUS.md) · [`PHYSICS_BASIS.md`](PHYSICS_BASIS.md)

---

## 4. Next required actions

1. Phase 0: record indoor conditions only; do not extrapolate range.  
2. If Phase 1 authorized: specify tracking requirement in new REQ set + ICD update.  
3. Optional: outdoor transmission measurement as separate gated test — not default.
