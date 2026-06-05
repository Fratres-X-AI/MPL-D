# Assumptions and Constraints — MPL-D

**Maturity:** Preliminary Design — documented assumptions for traceability. **Not validated by test.**

**Evidence / analysis status:** Derived from architecture trade studies, first-order models, and program baseline documents. No independent audit performed.

**Known gaps:** Host interface geometry, LSO-approved NHZ, measured beam parameters, and threat-representative sensor data are absent.

**Next required action:** Assign LSO; procure P0 hardware; measure collimator divergence before updating Assumption IDs A-OPT-03 and A-RNG-01.

---

## 1. Purpose

Central register of assumptions and constraints referenced by the Requirements Traceability Matrix ([`REQUIREMENTS_TRACEABILITY.md`](REQUIREMENTS_TRACEABILITY.md)), risk register, and analysis artifacts. Each assumption carries an ID for audit trail.

---

## 2. Assumption register

| ID | Assumption | Maturity | Evidence | If wrong |
|----|------------|----------|----------|----------|
| A-HST-01 | Primary host is **Drone-X** with **10 kg payload** baseline | Concept | Program baseline in CONOPS, interface_spec | R-INT-001; integration rework |
| A-HST-02 | Host provides 18–26 V DC bus with ≥30 W peak headroom (planning) | Preliminary Design | First-order power model | R-PWR-001; brownout / reduced duty |
| A-OPT-01 | Leading laser path: **940 nm** fiber-coupled ~10 W CW rated module, pulsed on host | Preliminary Design | candidate_components.md | Wavelength down-select reopens |
| A-OPT-02 | Static **3×3 DOE** with η_DOE ≈ 0.60–0.85 (vendor-class, **unmeasured**) | Preliminary Design | preliminary_optical_layout | R-DOE-001; pattern failure |
| A-OPT-03 | Collimated half-angle θ_half = **0.5–3 mrad** until measured | Preliminary Design | nir_940nm_link_budget_notes | Range model error ±order of magnitude |
| A-PWR-01 | Wall-plug efficiency η_wp = **0.35–0.50** (940 nm planning; use 0.40 nominal) | Preliminary Design | Vendor typ; power_thermal_budget.py | R-THM-001; thermal underestimate |
| A-PWR-02 | Average dazzle duty ≤ **10% over 60 s** on small hosts | Preliminary Design | pulse_control_spec | R-THM-001; mission impact |
| A-RNG-01 | Beer-Lambert σ = **0.05–0.2 km⁻¹** clear air (locale unknown) | Concept | PHYSICS_BASIS | R-ATM-001; outdoor envelope wrong |
| A-EFF-01 | Surrogate three-class sensor set represents **minimum** commercial EO classes only | Preliminary Design | ARCHITECTURE § surrogate table | R-EFF-001; threat extrapolation invalid |
| A-SAF-01 | Indoor controlled optics lab for Phase 0 bench | Preliminary Design | phase0_test_plan, SOP draft | R-REG-001 if violated |
| A-SAF-02 | Named **LSO** will complete IEC 60825-1 NHZ before full-power energization | **Unmet** | lso_assignment_record (template) | G-ENR blocked; R-EYE-001 |
| A-ROE-01 | Employment limited to **defensive sensor denial on hostile UAS** | Preliminary Design | CONOPS, ROE_PROTOCOL_IV | R-ROE-001 |
| A-EXP-01 | No ITAR/EAR classification obtained | **Fact** | EXPORT_CONTROL_SCREENING | R-EXP-001 |

---

## 3. Hard constraints (non-negotiable for this program)

| ID | Constraint | Source deliverable |
|----|------------|-------------------|
| C-NK-01 | Non-kinetic sensor denial only — no hard-kill burn-through design intent | REQ-F-002, CONOPS |
| C-MP-01 | Multi-point / patterned beam — not single high-power focused beam | REQ-F-001, project definition |
| C-SAF-01 | No full-power energization without LSO + NHZ + signed SOP | G-SAF-01/02/03 |
| C-SAF-02 | Zero-order beam path must be blocked or dumped (REQ-S-003) | zero_order_inspection_checklist |
| C-PH0-01 | Phase 0 excludes flight test and outdoor emission without separate authorization | ROADMAP, R-REG-001 |
| C-TRK-01 | Phase 0 excludes closed-loop track-to-dazzle | ARCHITECTURE, CONOPS |
| C-VIS-01 | External hero/schematic art excludes host airframe imagery | README, assets policy |

---

## 4. Traceability to eight deliverables

| Deliverable | Primary assumption IDs |
|-------------|------------------------|
| 1 Architecture | A-HST-01, A-OPT-01/02, A-PWR-01 |
| 2 Beam physics | A-OPT-01/02/03, A-RNG-01 |
| 3 Power / thermal / effects | A-PWR-01/02, A-RNG-01, A-EFF-01 |
| 4 Risks / limitations | All; A-SAF-02 unmet |
| 5 CONOPS | A-ROE-01, A-HST-01 |
| 6 Requirements | Mapped in RTM |
| 7 Roadmap | A-SAF-01, C-PH0-01 |
| 8 Repository handoff | A-EXP-01, C-VIS-01 |

---

## 5. Change control

Assumption changes require update to this file, RTM, affected analysis scripts, and risk register entry. See [`CONFIGURATION_MANAGEMENT.md`](CONFIGURATION_MANAGEMENT.md).
