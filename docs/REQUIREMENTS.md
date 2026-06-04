# Requirements — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Concept. Supporting evidence: Requirements derived from project objective and constraints only. No verification evidence exists.

MPL-D is used as internal shorthand only. All formal and safety documentation uses the full descriptive title. Requirement text below uses the full title where safety or regulatory context applies.

---

## Summary table

| ID | Category | Priority | Verification |
|----|----------|----------|--------------|
| REQ-F-001 | Functional | High | Test |
| REQ-F-002 | Functional | High | Test |
| REQ-F-003 | Functional | High | Analysis |
| REQ-F-004 | Performance | High | Analysis |
| REQ-F-005 | Performance | Medium | Test |
| REQ-F-006 | Performance | Medium | Analysis |
| REQ-P-001 | Performance | High | Analysis |
| REQ-P-002 | Performance | Medium | Demonstration |
| REQ-E-001 | Environmental | High | Test |
| REQ-E-002 | Environmental | Medium | Analysis |
| REQ-E-003 | Environmental | High | Analysis |
| REQ-I-001 | Interface | High | Inspection |
| REQ-I-002 | Interface | High | Demonstration |
| REQ-I-003 | Interface | Medium | Inspection |
| REQ-S-001 | Safety | High | Inspection |
| REQ-S-002 | Safety | High | Demonstration |
| REQ-S-003 | Safety | High | Inspection |
| REQ-S-004 | Safety | High | Test |
| REQ-R-001 | Regulatory/ROE | High | Analysis |
| REQ-R-002 | Regulatory/ROE | High | Analysis |
| REQ-R-003 | Regulatory/ROE | Medium | Analysis |
| REQ-R-004 | Regulatory/ROE | High | Analysis |
| REQ-O-001 | Operational | Medium | Demonstration |
| REQ-O-002 | Operational | Medium | Analysis |

---

## Functional / Performance requirements

### REQ-F-001 — Multi-point optical output

**Description:** The Counter-UAS Multi-Point Laser Dazzler Prototype shall produce a static pattern of two or more spatially separated optical beamlets from a single module assembly.

**Rationale:** Core project constraint — multi-point / patterned approach instead of single high-power focused beam.

**Verification:** Test (Phase 0 T-01 pattern formation).

**Priority:** High

---

### REQ-F-002 — Non-kinetic sensor denial intent

**Description:** System design shall target electro-optical sensor degradation (dazzle, saturation, temporary blinding) and shall not require burn-through or structural damage to the target.

**Rationale:** Project objective limits scope to soft-kill / sensor denial.

**Verification:** Test (surrogate camera exposure); design inspection confirming power tier below hard-kill thresholds.

**Priority:** High

---

### REQ-F-003 — Drone-mountable form factor

**Description:** The payload module shall have a total mass target not exceeding 3 kg for small-host integration or 8 kg for medium VTOL-class hosts, with envelope suitable for external mount.

**Rationale:** Mountable on small-to-medium UAV platforms per project constraints.

**Verification:** Analysis (mass rollup); inspection of as-built mockup.

**Priority:** High

**Note:** Mass targets are planning bounds, not validated against a selected host.

---

### REQ-F-004 — Optical power tier

**Description:** Total useful optical power delivered to the pattern shall be configurable within a planning range of 1–15 W (combined beamlets), selected to balance drone power budget and sensor exposure.

**Rationale:** Low-power producible approach vs high-power single beam.

**Verification:** Analysis (link budget); test (power meter at bench).

**Priority:** High

---

### REQ-F-005 — Static pattern (Phase 0)

**Description:** Phase 0 configuration shall use a fixed pattern without moving-beam scanning hardware.

**Rationale:** Simplicity and producibility; rejected galvo scanning for initial POC.

**Verification:** Test (T-01); inspection.

**Priority:** Medium

---

### REQ-F-006 — Duty-cycle control

**Description:** Emitter drive electronics shall support pulsed operation with software-defined maximum pulse duration and cumulative on-time logging.

**Rationale:** Thermal limits and ROE-relevant exposure control on drone power budget.

**Verification:** Analysis; demonstration on bench controller.

**Priority:** Medium

---

### REQ-P-001 — Beam divergence class

**Description:** Effective half-angle divergence per beamlet shall fall within 1–5 mrad class unless measured bench data requires revision.

**Rationale:** Compact optics compatible with drone SWaP; bounds spot size at engagement ranges.

**Verification:** Analysis; test (beam profiler at Phase 0).

**Priority:** High

---

### REQ-P-002 — Surrogate sensor exposure effect

**Description:** At bench distance (1–10 m), the system shall produce measurable image degradation (saturation or bloom) on at least one documented surrogate commercial camera at a defined operating exposure.

**Rationale:** Phase 0 success metric — qualitative dazzle demonstration only.

**Verification:** Demonstration (T-03). **Not** a range or operational effectiveness requirement.

**Priority:** Medium

---

## Environmental requirements

### REQ-E-001 — Operating temperature (planning)

**Description:** The module shall operate in ambient temperatures from −10 °C to +40 °C at reduced duty cycle if thermal model predicts exceedance.

**Rationale:** Real-world drone operating envelope (planning assumption).

**Verification:** Test (thermal chamber or ambient soak if available).

**Priority:** High

---

### REQ-E-002 — Vibration exposure

**Description:** The optical assembly shall remain structurally intact and attached after exposure to sinusoidal vibration sweep 5–200 Hz at 0.5 g equivalent on vibration table (Phase 0 surrogate).

**Rationale:** Propeller/VTOL vibration is a documented risk to beam stability.

**Verification:** Analysis; test (T-05 limited).

**Priority:** Medium

---

### REQ-E-003 — Atmospheric awareness

**Description:** Engagement planning shall document atmospheric visibility and apply conservative extinction coefficients (σ ≥ 0.1 km⁻¹ for clear-day planning unless local data exists).

**Rationale:** Atmospheric attenuation may reduce effective range below useful thresholds.

**Verification:** Analysis (link budget in `analysis/power_thermal_budget.py`).

**Priority:** High

---

## Interface requirements

### REQ-I-001 — Host power interface

**Description:** The module shall accept DC input in a host-defined band (planning: 18–26 V) with documented peak and average current draw.

**Rationale:** Integration with existing drone power buses.

**Verification:** Inspection (interface spec); test (logged draw).

**Priority:** High

---

### REQ-I-002 — Safe default state

**Description:** On power-up, all laser emitters shall be in a disabled (safe) state until a multi-step arm sequence is completed.

**Rationale:** Safety and ROE control.

**Verification:** Demonstration (interlock test).

**Priority:** High

---

### REQ-I-003 — Mechanical mount

**Description:** The module shall provide a mechanical interface compatible with standard payload rails or a documented 4-bolt pattern per `hardware/interface_spec.md`.

**Rationale:** Mountable on candidate host platforms.

**Verification:** Inspection (CAD/mockup).

**Priority:** Medium

---

## Safety requirements

### REQ-S-001 — IEC 60825-1 classification

**Description:** Before open-beam operation, the Counter-UAS Multi-Point Laser Dazzler Prototype shall have a documented laser safety classification and nominal hazard zone analysis per IEC 60825-1.

**Rationale:** Eye safety and collateral exposure risk during maneuvering or beam divergence.

**Verification:** Inspection (LSO-approved safety plan).

**Priority:** High

---

### REQ-S-002 — Hardware interlock

**Description:** A hardware enable line (key switch or equivalent) shall be wired in series with emitter power such that removal of enable forces immediate optical shutdown.

**Rationale:** Fail-safe against software fault.

**Verification:** Demonstration (fault injection).

**Priority:** High

---

### REQ-S-003 — Zero-order beam containment (DOE)

**Description:** If a diffractive optical element is used, zero-order and unused diffraction orders shall be blocked or dumped such that uncontrolled specular paths are eliminated in bench configuration.

**Rationale:** DOE leakage is a safety and efficiency risk.

**Verification:** Inspection; test (low-power alignment).

**Priority:** High

---

### REQ-S-004 — Over-temperature shutdown

**Description:** Emitter drivers shall disable optical output when heat sink temperature exceeds a setpoint defined in thermal test (Phase 0), with setpoint TBD from measurement.

**Rationale:** Thermal runaway limits drone safety and endurance.

**Verification:** Test (T-04).

**Priority:** High

---

## Regulatory / ROE requirements

### REQ-R-001 — Protocol IV compliance review

**Description:** System design and employment concept shall be reviewed for consistency with Protocol IV to the CCW on Blinding Laser Weapons before field use.

**Rationale:** Blinding laser prohibition risk if parameters or employment are not controlled.

**Verification:** Analysis (legal review record).

**Priority:** High

---

### REQ-R-002 — Defensive employment framing

**Description:** Documented concept of operations shall describe defensive counter-UAS sensor denial only, not offensive blinding of personnel or non-UAS targets.

**Rationale:** Project scope and policy alignment.

**Verification:** Analysis (CONOPS review).

**Priority:** High

---

### REQ-R-003 — Export control screening

**Description:** Component selection and performance parameters shall be screened against ITAR/EAR thresholds before export or foreign national access.

**Rationale:** Laser systems may trigger export controls depending on performance.

**Verification:** Analysis (compliance checklist).

**Priority:** Medium

---

### REQ-R-004 — Outdoor emission authorization

**Description:** Outdoor laser propagation tests shall not occur without documented authorization per applicable local regulations and internal Fratres X AI approval.

**Rationale:** Outdoor tests exceed bench SOP scope.

**Verification:** Analysis (permits/approvals on file).

**Priority:** High

---

## Operational requirements

### REQ-O-001 — Power budget documentation

**Description:** The system shall document impact of dazzler operation on host mission endurance for at least two duty-cycle scenarios (e.g., 10% and 50% on-time).

**Rationale:** Power draw reduces host mission time — documented risk.

**Verification:** Demonstration (logged bench duty cycles extrapolated with stated uncertainty).

**Priority:** Medium

---

### REQ-O-002 — Effectiveness uncertainty disclosure

**Description:** All externally communicated performance material shall state that dazzle effectiveness against operational threat UAS sensors is unvalidated in this program phase.

**Rationale:** Sparse public flight-test validation for low-power multi-point dazzlers.

**Verification:** Analysis (document review).

**Priority:** Medium

---

## Recommended next actions

1. Assign verification owners and Phase 0 test mapping for each High-priority requirement.
2. Baseline CONOPS draft to satisfy REQ-R-002.
3. Do not add numeric range-to-kill requirements until bench data exists.

## Open questions / gaps

- Final wavelength selection drives REQ-S-001 hazard analysis — not fixed.
- Host platform selection drives REQ-F-003 mass split — Solace payload limit unverified.
