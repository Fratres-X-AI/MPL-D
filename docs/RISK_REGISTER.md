# Risk Register — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Preliminary Design. **Evidence basis:** First principles, literature classes, gate definitions. **No test-derived likelihood updates.**

**Analysis status:** R-EFF-001 and R-VIB-001 await T-01/T-03/T-05. Mitigation **execution** tracked in [`MITIGATION_EXECUTION_LOG.md`](MITIGATION_EXECUTION_LOG.md). Residual ratings assume documented mitigations are executed — most are **not executed**.

**Known gaps:** No quantitative risk model; owners are role placeholders until program staffing assigned.

**Next required action:** LSO + test lead to update rows after G-SAF-01 and T-01 execution.

---

## Risk scoring key

| Field | Definition |
|-------|------------|
| **Inherent likelihood** | H/M/L before mitigation |
| **Mitigation status** | Not started / Partial / Complete |
| **Residual likelihood** | H/M/L after planned mitigation (if executed) |
| **Residual impact** | Qualitative consequence if risk occurs after mitigation |
| **Owner** | Responsible role (TBD until assigned) |
| **Evidence to close/reduce** | Measurable artifact required |

---

## Risk table

| ID | Category | Description | Inherent L | Impact | Mitigation (planned) | Mitigation status | Residual L | Residual impact | Owner | Evidence to close | Status |
|----|----------|-------------|------------|--------|----------------------|-------------------|------------|-----------------|-------|-------------------|--------|
| R-VIB-001 | Technical | Vibration decenters multi-point pattern on target EO FOV | H | Missed dazzle; invalid bench-to-flight map | Elastomer mount; T-05 vibe table; pattern re-align procedure | **Not started** | H→M if T-05 passes criteria | Spot miss at range | Mechanical / Test | T-05 log: Δθ vs input; T-01 irradiance map under vibe | Open |
| R-THM-001 | Technical | Thermal limits reduce duty cycle / endurance | H | Dazzle unavailable; battery drain | Pulsed op; sink/fan; duty cap in firmware | **Partial** (spec only) | M | Reduced availability | Thermal / Systems | T-04 soak log; revised duty limits | Open |
| R-ATM-001 | Atmospheric | Attenuation/scintillation shrinks envelope | H | Range below planning | Accept shorter envelope; document σ; avoid degraded weather | **Not started** | H | Engagement gap | Systems | Measured transmission if outdoor ever authorized | Open |
| R-EYE-001 | Safety / Policy | IEC 60825-1 non-compliance; collateral eye exposure | M | Injury; program stop | NHZ; interlocks; eyewear; zero-order control | **Partial** (drafts) | **H until NHZ done** | Retinal injury | **LSO** | Signed NHZ; G-SAF-02/03 PASS; checklist complete | Open |
| R-ROE-001 | Policy | Protocol IV / blinding weapon interpretation | M | Operational prohibition | Defensive CONOPS; legal review; pulse limits | **Partial** (CONOPS) | M | Legal block | Program Legal | Written legal memo | Open |
| R-EXP-001 | Policy | ITAR/EAR violation on export/access | M | Fines; delay | Compliance review; access control; hold ship | **Partial** (screening doc) | M | Export hold | Compliance | Written ECCN/classification or hold memo | Open |
| R-EFF-001 | Technical | Unproven dazzle vs filtered/AGC/AI threat EO | H | System fails mission | Three-class surrogate tests; conservative claims | **Not started** | **H** | No operational effect | Test / Systems | T-03 per sensor class + RTM update | Open |
| R-PWR-001 | Technical | Host power budget reduces sortie time | H | Reduced mission time | Duty cap; lower P_opt; larger host | **Partial** (spec) | M | Endurance loss | Systems / Host | Measured bus draw T-04; host vendor confirm | Open |
| R-SUP-001 | Technical | DOE/laser supply chain slip | M | Schedule/cost | Alternate multi-emitter; dual vendor | **Not started** | M | Delay | Procurement | PO + receipt or approved alternate | Open |
| R-TRK-001 | Operational | Static pattern misses maneuvering target | H | Engagement miss | Phase 1+ tracking (not Phase 0) | **Not started** | H (Phase 0) | Miss windows | Systems | CONOPS accept or Phase 1 req | Open |
| R-EMI-001 | Technical | Driver EMI affects GPS/comms | L–M | Nav degradation | Shielding; filter; separation | **Not started** | L–M | EMI events | EE / Host | Phase 1 EMI test if authorized | Open |
| R-DOE-001 | Technical | Zero-order leakage / η loss | M | Hazard + wasted power | Dump optics; measure; block before full power | **Partial** (design) | M→L if measured OK | Stray beam | Optics / LSO | zero_order checklist signed; T-01 map | Open |
| R-DAT-001 | Technical | Documentation error (incl. AI-assisted) | M | Wrong decisions | Independent review; bench validation | **Partial** (this audit pass) | M | Design error | Tech Lead | Signed review record per baseline | Open |
| R-INT-001 | Operational | Drone-X ICD details missing | M | Integration rework | Vendor ICD; mock fit | **Not started** | M | Schedule slip | Integration | ICD Rev A signed | Open |
| R-REG-001 | Policy | Unauthorized outdoor/flight laser ops | M | Fines; shutdown | Phase 0 indoor only; legal pre-clear | **Partial** (scope) | L if scope obeyed | Test halt | LSO / Legal | Written authorization for any outdoor | Open |

---

## Mandatory expansions

### R-EFF-001

Phase 0 surrogate results **shall not** be extrapolated to military-hardened EO. Closing evidence requires irradiance + image degradation logs on **each** surrogate class in [`../hardware/surrogate_sensor_procurement.md`](../hardware/surrogate_sensor_procurement.md) with uncertainty stated.

### R-EYE-001

Invisible 940 nm beam increases accidental exposure vs visible systems. Residual remains **High** until G-SAF-02 PASS. See [`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md).

### R-VIB-001

Vibration table data **does not** prove flight performance without separate Phase 1 gate.

---

## Risk summary for executive review

| Residual band | Count | IDs |
|---------------|-------|-----|
| **High** | 4 | R-EFF-001, R-EYE-001 (until NHZ), R-VIB-001 (until T-05), R-TRK-001 (Phase 0 static pattern) |
| **Medium** | 11 | All others (as mitigations incomplete) |
| **Low** | 0 | — |

---

## Next steps

1. Assign risk owners (replace TBD roles).
2. Close G-SAF-01/02 before any full-power work (R-EYE-001).
3. Execute T-01/T-03/T-05; update R-EFF-001 and R-VIB-001 with measured fields only.
