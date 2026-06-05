# Requirements Traceability Matrix (RTM) — MPL-D

**Maturity:** Preliminary Design — full forward and backward trace. **Verification evidence: 0 / 22 recorded.**

**Evidence / analysis status:** Each requirement linked to source deliverable, risk(s), analysis artifact, verification method, and gate.

**Known gaps:** No pass/fail column populated; no test log references.

**Next required action:** After each T-01–T-05 run, update Verification Evidence column with log path and commit hash.

---

## RTM — full traceability

| Req ID | Source deliverable | Requirement summary | Linked risk(s) | Analysis artifact | Verification method | Phase 0 test | Gate | Verification evidence |
|--------|-------------------|---------------------|----------------|-------------------|---------------------|--------------|------|----------------------|
| REQ-F-001 | D1 Architecture | Multi-point optical output | R-DOE-001 | preliminary_optical_layout | Test | T-01 | G-ENR | **None** |
| REQ-F-002 | D5 CONOPS | Non-kinetic sensor denial | R-ROE-001, R-EFF-001 | CONOPS | Test + inspection | T-03 | G-ENR | **None** |
| REQ-F-003 | D1 Architecture | Drone-mountable module | R-INT-001 | mechanical_bom, ICD | Analysis + inspection | — | G-PROTO | **None** |
| REQ-F-004 | D2 Physics | Wavelength/power class trade | R-EFF-001, R-ATM-001 | nir_940nm_link_budget, power_thermal_budget | Analysis + test | T-02 | G-ENR | **None** |
| REQ-F-005 | D2 Physics | Pattern coverage (≥2 beamlets) | R-TRK-001 | ARCHITECTURE §3 | Test | T-01 | G-ENR | **None** |
| REQ-F-006 | D3 Power | Pulsed operation / duty | R-THM-001, R-PWR-001 | pulse_control_spec, thermal_pulse_model | Demo + test | T-04 | G-ENR | **None** |
| REQ-P-001 | D3 Effects | Irradiance vs range bounded | R-ATM-001, R-EFF-001 | PHYSICS_BASIS, prebench_t02 | Analysis + test | T-02 | G-ENR | **None** |
| REQ-P-002 | D3 Effects | Surrogate sensor degradation | R-EFF-001 | surrogate_sensor_procurement | Demo | T-03 | G-ENR | **None** |
| REQ-E-001 | D3 Power | Thermal limits | R-THM-001 | thermal_pulse_model | Test | T-04 | G-ENR | **None** |
| REQ-E-002 | D1 Architecture | Vibration environment | R-VIB-001 | vibration_wander_model | Test | T-05 | G-ENR | **None** |
| REQ-E-003 | D2 Physics | Atmospheric planning | R-ATM-001 | PHYSICS_BASIS | Analysis | T-02 | G-ENR | **None** |
| REQ-I-001 | D1 ICD | Electrical interface | R-PWR-001, R-EMI-001 | electrical_architecture, ICD §4 | Inspection | T-04 | G-HW-P0 | **None** |
| REQ-I-002 | D1 ICD | Control / interlock | R-EYE-001 | pulse_control_spec, SOP | Demo | — | G-SAF-03 | **None** |
| REQ-I-003 | D1 ICD | Mechanical interface | R-INT-001, R-VIB-001 | mechanical_bom, ICD §3 | Inspection | — | G-PROTO | **None** |
| REQ-S-001 | D4 Safety | IEC 60825-1 compliance path | R-EYE-001 | LASER_SAFETY_PLAN, safety_case | Inspection | — | G-SAF-02 | **None** |
| REQ-S-002 | D4 Safety | Hardware interlocks | R-EYE-001 | electrical_architecture | Demo | — | G-SAF-03 | **None** |
| REQ-S-003 | D4 Safety | Zero-order containment | R-DOE-001, R-EYE-001 | zero_order_checklist | Inspection + test | T-01 | G-SAF-04 | **None** |
| REQ-S-004 | D4 Safety | Over-temperature fault | R-THM-001 | thermal_pulse_model | Test | T-04 | G-ENR | **None** |
| REQ-R-001 | D4 ROE | Protocol IV defensive framing | R-ROE-001 | ROE_PROTOCOL_IV | Analysis | — | G-PROTO | **None** |
| REQ-R-002 | D5 CONOPS | Non-personnel targeting intent | R-ROE-001, R-EYE-001 | CONOPS | Analysis | — | G-PROTO | **None** |
| REQ-R-003 | D4 Compliance | Export control screening | R-EXP-001 | EXPORT_CONTROL_SCREENING | Analysis | — | G-PROTO | **None** |
| REQ-R-004 | D4 Safety | Phase 0 scope limits | R-REG-001 | phase0_test_plan, SOP | Analysis | — | G-PROTO | **None** |
| REQ-O-001 | D3 Power | Duty cycle operational bound | R-THM-001 | pulse_control_spec | Demo | T-04 | G-ENR | **None** |
| REQ-O-002 | D3 Effects | Effectiveness uncertainty documented | R-EFF-001 | RISK_REGISTER | Analysis | — | G-PROTO | **None** |

**Deliverable key:** D1=Architecture · D2=Beam physics · D3=Power/effects · D4=Risks/compliance · D5=CONOPS

---

## Coverage summary

| Metric | Value |
|--------|-------|
| Requirements traced to verification method | 22 / 22 |
| Requirements traced to ≥1 risk | 22 / 22 |
| Requirements traced to analysis or design doc | 22 / 22 |
| Requirements with recorded pass/fail | **0 / 22** |

---

## Assumption traceability

Requirements depending on open assumptions: see [`ASSUMPTIONS_AND_CONSTRAINTS.md`](ASSUMPTIONS_AND_CONSTRAINTS.md) (A-SAF-02 **unmet** blocks all G-ENR verification).

---

## Next steps

1. Populate Verification Evidence from `tests/logs/` after each procedure.
2. Re-run RTM review at Phase 0 exit (TDP baseline 1.0 target).
