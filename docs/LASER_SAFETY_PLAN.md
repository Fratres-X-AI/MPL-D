# Laser Safety and Eye-Safety Plan — Outline

**Document ID:** MPL-D-SAF-001  
**Maturity:** Preliminary Design — **outline only**. **Not LSO-approved. No NHZ distances approved.**

**Evidence / analysis status:** Framework aligned with IEC 60825-1 (reference edition — LSO must apply current). Draft safety case exists: [`phase0_safety_case_draft.md`](phase0_safety_case_draft.md).

**Known gaps:** No named LSO; no NHZ calculation; no lab layout; no eyewear OD selection; zero-order not measured on hardware.

**Next required action:** Close G-SAF-01 (assign LSO); LSO completes NHZ and signs G-SAF-02/03.

---

## 1. Scope and configuration

| Item | Planning value | Validated? |
|------|----------------|------------|
| Wavelength | 940 nm (935–945 nm) | Datasheet only |
| Max CW optical power | 10 W | Vendor rating; not measured accessible emission |
| Pattern | 3×3 DOE; ~9 beamlets | Not fabricated |
| Per-beamlet power (plan) | ~0.83 W (10×0.75/9) | Unmeasured |
| Pulse | 0.1–3 s; ≤10% duty / 60 s | SOP draft |
| Environment (Phase 0) | Indoor controlled optics lab | Assumption A-SAF-01 |

**940 nm is invisible.** Collateral exposure risk exceeds visible systems where operators rely on visual beam awareness (R-EYE-001).

---

## 2. Hazard summary

| Hazard path | Mechanism | Severity | Control category |
|-------------|-----------|----------|------------------|
| Intrabeam | Direct 940 nm into eye | Retinal injury | Engineering + admin |
| Specular reflection | Optics, window, target lens | Retinal injury | Beam blocks, angle control |
| Zero-order (DOE) | Undiffracted leakage | Intrabeam / specular | REQ-S-003 dump; measure before full power |
| Multi-beamlet cumulative | Nine accessible paths | Retinal injury | NHZ encompasses all orders |
| Electrical | 11.5–13 A driver | Shock, fire | E-stop, qualified wiring |

**Planning classification expectation:** Accessible emission at full power open-beam configuration is consistent with **high-hazard / Class 4** treatment until LSO measurement proves otherwise. **Do not assume Class 3B.**

---

## 3. Nominal Hazard Zone (NHZ) requirements

**Status:** **Not computed. No distances in this repository.**

LSO shall produce NHZ package including:

1. Measured accessible emission at source, each beamlet, and zero-order port.
2. Measured divergence after collimator and DOE at alignment and full power (separate if required).
3. Worst-case pulse duty per approved SOP.
4. Lab layout with operator and bystander positions.
5. Documented NHZ boundary distances, control measures, and signage.

**Forbidden:** Using [`analysis/nir_940nm_link_budget_notes.md`](../analysis/nir_940nm_link_budget_notes.md) target-plane irradiance as ocular NHZ standoff.

**Gate:** G-SAF-02.

---

## 4. Zero-order beam management

| Step | Requirement | Status |
|------|-------------|--------|
| Optical design includes dump or block for zero-order | REQ-S-003 | Layout documented |
| Zero-order power measured at ALIGN power | SOP | **Not done** |
| Zero-order blocked before full-power DOE test | zero_order_inspection_checklist | **Not inspected** |
| Zero-order re-measured after vibration (T-05) | Phase 0 extension | Planned |

**Risk:** R-DOE-001. **Residual:** High until measured and blocked.

---

## 5. Protective eyewear (recommendations — LSO must confirm)

| Wavelength tested | Minimum planning guidance | Gap |
|-------------------|---------------------------|-----|
| 940 nm NIR | OD ≥ 4 at 900–1000 nm for alignment work (LSO to specify exact OD and brand) | **Not procured or verified** |
| 532 nm (if dual-path bench) | Separate green-line eyewear — **do not reuse NIR glasses** | Only if 532 nm bench authorized |

Wrong eyewear is a **hard failure**, not a margin issue.

---

## 6. LSO prerequisites (G-SAF-01)

| Item | Status |
|------|--------|
| Named LSO with documented authority | **OPEN** — [`lso_assignment_record.md`](lso_assignment_record.md) template |
| LSO review of configuration | **Not done** |
| LSO approval of safety case | **Not done** — draft only |
| LSO approval of bench SOP | **Not done** — [`../tests/phase0_bench_sop_draft.md`](../tests/phase0_bench_sop_draft.md) |
| Energization authorization (G-ENR) | **BLOCKED** |

---

## 7. Engineering controls (required before energization)

| Control | REQ | Built | Verified |
|---------|-----|-------|----------|
| Hardware key enable | REQ-S-002 | No | No |
| E-stop (driver power cut) | REQ-S-002 | No | No |
| Enclosure / door interlock | Lab-dependent | TBD | No |
| Beam blocks on all exit paths | SOP | TBD | No |
| Remote firing from outside NHZ | SOP | TBD | No |

---

## 8. Administrative controls

- Laser safety training for all bench personnel (LSO-led).
- Posted warning signage (940 nm invisible beam).
- Written energization checklist per pulse level (ALIGN → LOW → FULL only with LSO authorization).
- Incident reporting path to LSO and program lead.

---

## 9. Cross-references

| Topic | Document |
|-------|----------|
| Risk | R-EYE-001, R-DOE-001, R-REG-001 in [`RISK_REGISTER.md`](RISK_REGISTER.md) |
| ROE / Protocol IV | [`ROE_PROTOCOL_IV.md`](ROE_PROTOCOL_IV.md) |
| Export | [`EXPORT_CONTROL_SCREENING.md`](EXPORT_CONTROL_SCREENING.md) |
| Tests | T-01 (pattern/zero-order), T-04 (thermal/interlock) |

---

## 10. Residual safety posture

**Current:** **Unacceptable for full-power open-beam operation.** Documentation exists; controls are not built, measured, or LSO-approved.

**After planned mitigations (if executed):** Residual risk remains **Medium** for invisible NIR collateral until flight/outdoor segments are separately analyzed.
