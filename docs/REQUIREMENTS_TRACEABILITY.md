# Requirements Traceability Matrix — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Preliminary Design — full forward trace from requirements to verification artifacts. **No verification evidence recorded.**

---

## Traceability table

| Req ID | Verification | Phase 0 test | Supporting documents | Gate |
|--------|--------------|--------------|----------------------|------|
| REQ-F-001 | Test | T-01 | ARCHITECTURE §3, optical_layout | G-ENR |
| REQ-F-002 | Test | T-03 | CONOPS, safety case | G-ENR |
| REQ-F-003 | Analysis | — | mechanical_bom, interface_spec | G-PROTO |
| REQ-F-004 | Analysis | T-02 | nir_940nm_link_budget, power_thermal_budget | G-ENR |
| REQ-F-005 | Test | T-01 | ARCHITECTURE §3 | G-ENR |
| REQ-F-006 | Demonstration | T-04 | pulse_control_spec, firmware design | G-ENR |
| REQ-P-001 | Analysis | T-02 | prebench_t02, beam_propagation | G-ENR |
| REQ-P-002 | Demonstration | T-03 | surrogate_sensor_procurement | G-ENR |
| REQ-E-001 | Test | T-04 | thermal_pulse_model | G-ENR |
| REQ-E-002 | Test | T-05 | vibration_wander_model | G-ENR |
| REQ-E-003 | Analysis | T-02 | PHYSICS_BASIS | G-ENR |
| REQ-I-001 | Inspection | T-04 | electrical_architecture | G-HW-P0 |
| REQ-I-002 | Demonstration | — | pulse_control_spec, SOP | G-SAF-03 |
| REQ-I-003 | Inspection | — | mechanical_bom | G-PROTO |
| REQ-S-001 | Inspection | — | phase0_safety_case_draft | G-SAF-02 |
| REQ-S-002 | Demonstration | — | SOP, electrical_architecture | G-SAF-03 |
| REQ-S-003 | Inspection | T-01 | zero_order_checklist | G-SAF-04 |
| REQ-S-004 | Test | T-04 | thermal_pulse_model | G-ENR |
| REQ-R-001 | Analysis | — | CONOPS, RISK_REGISTER R-ROE-001 | G-PROTO |
| REQ-R-002 | Analysis | — | CONOPS | G-PROTO |
| REQ-R-003 | Analysis | — | EXPORT_CONTROL_SCREENING | G-PROTO |
| REQ-R-004 | Analysis | — | phase0_test_plan, SOP | G-PROTO |
| REQ-O-001 | Demonstration | T-04 | pulse_control_spec | G-ENR |
| REQ-O-002 | Analysis | — | RISK_REGISTER R-EFF-001 | G-PROTO |

**G-PROTO:** Elite prototype documentation package complete (this repository session class).

---

## Coverage summary

| Status | Count |
|--------|-------|
| Requirements with linked verification artifact | 22 / 22 |
| Requirements with recorded pass/fail | 0 / 22 |

---

## Recommended next actions

Update Status column after each T-01–T-05 execution with log file reference under `tests/logs/`.
