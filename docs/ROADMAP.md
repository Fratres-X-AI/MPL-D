# Development Roadmap — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Preliminary Design (program baseline). **Internal codename:** MPL-D.

**Supporting evidence:** Wavelength/power trade study complete; 940 nm leading candidate documented; surrogate sensor set, optical stack layout, procurement list, pulse/interlock spec, and Phase 0 gates defined. **No hardware procured, no NHZ analysis completed, no bench test data.**

**Repository:** https://github.com/Fratres-X-AI/MPL-D (private; authorized access only)

---

## Handoff criteria (repository standard)

After this session the repository must allow a new engineer or reviewer to immediately understand (a) exact current maturity level of every major element, (b) all assumptions and their uncertainty bounds, (c) the complete risk picture with evidence basis, and (d) a prioritized, actionable list of next engineering tasks to reach a bench-testable Phase 0 configuration. The state must be usable for planning without requiring reverse-engineering of the documents.

MPL-D is used as internal shorthand only. All formal and safety documentation uses the full descriptive title.

---

## Phase overview

| Phase | Name | Duration (placeholder) | Flight test |
|-------|------|------------------------|-------------|
| **Current** | Preliminary Design → Phase 0 prep | — | No |
| **Phase 0** | Proof-of-Concept (bench) | 3–6 months (resource-dependent) | **No** (explicitly excluded from initial Phase 0 scope) |
| **Phase 1** | Ground + limited flight integration | 6–12 months (placeholder) | Limited, subject to separate approval |

---

## Current phase: Preliminary Design (Phase 0 preparation)

**Objectives:** Complete bench-ready configuration definition — source down-select candidate, optical stack, procurement list, safety gates, and surrogate test matrix — without hardware energization.

**Status:** In progress at repository level. Documentation artifacts below exist; **Phase 0 bench execution not started.**

**Completed (documentation evidence):**

- Architecture trade study: laser source, beam delivery, surrogate set, NHZ requirement, cross-cutting risks.
- Candidate component capture: AeroDiode-class 940 nm path (`hardware/candidate_components.md`).
- First-order link budgets: generic + 940 nm (`analysis/nir_940nm_link_budget_notes.md`).
- Phase 0 procurement list, optical layout, pulse control spec, surrogate sensor procurement guide.
- Risk register preparatory structure for R-EFF-001 / R-VIB-001.

**Not complete (blocks Phase 0 energization):**

- LSO assigned; NHZ analysis (G-SAF-01, G-SAF-02).
- Hardware procured and received.
- Any bench test T-01–T-05 executed.

**Exit criteria to enter Phase 0 bench execution:**

- G-SAF-01 through G-SAF-04 satisfied per `docs/ARCHITECTURE.md`.
- P0 procurement items on hand (laser, collimator, power meter, eyewear, interlocks).
- Written SOP approved by LSO.

---

## Prior phase: Concept (closed)

**Exit criteria (met):**

- Architecture, requirements, risk register, physics basis, and Phase 0 test outline exist.
- First-order analysis script present (`analysis/power_thermal_budget.py`).
- Initial subsystem maturity labels assigned with explicit evidence gaps.

---

## Phase 0: Proof-of-Concept (bench only)

### Objectives

1. Demonstrate multi-point optical pattern generation on bench.
2. Measure irradiance vs range and compare to first-order model (document deviation; do not force fit).
3. Capture surrogate camera image degradation under controlled bench exposure.
4. Log electrical power and thermal behavior vs duty cycle.
5. Execute basic vibration table test to quantify beam wander sensitivity.

### Key activities

| Activity | Output |
|----------|--------|
| Component procurement (emitters, DOE or array, drivers, optics) | Procurement list with datasheet links |
| Laser safety case + SOP | LSO-approved bench procedure |
| Bench optical alignment | Pattern photos + irradiance map |
| Surrogate sensor exposure tests | Raw images + exposure metadata |
| Power/thermal logging | CSV logs; updated thermal model |
| Vibration table test | Displacement vs frequency plot |
| Documentation update | Revised docs with measured bounds |

### Success metrics (Phase 0)

- Multi-point pattern observed and documented at 2–10 m bench range.
- Measured irradiance within **±50% of first-order model** OR model updated with measured divergence/efficiency and uncertainty stated.
- Surrogate camera shows **qualitative** saturation/bleeding at bench distance — **no operational range claim**.
- No uncontrolled thermal runaway during 10-minute duty-cycle test at planned power.
- Risk register updated with test-derived likelihood adjustments where evidence exists.

### Explicit exclusions (Phase 0 initial scope)

- Flight test on any UAV platform.
- Closed-loop track-to-dazzle integration.
- Operational engagement against non-surrogate targets.
- Claims of effectiveness against military-hardened sensors.

### Resources required

| Resource | Need |
|----------|------|
| Optics / laser lab | Controlled access bench |
| Laser Safety Officer | Mandatory |
| Optics engineer | Alignment and DOE characterization |
| Electrical engineer | Driver, interlock, logging |
| ~$5k–$25k parts budget (rough order of magnitude) | Highly configuration-dependent; not validated |

### Dependencies

- Wavelength and emitter architecture selection (`docs/ARCHITECTURE.md`).
- LSO approval before energization.
- Surrogate camera and calibrated power meter procurement.

### Phase 0 exit / handoff criteria

- Updated docs incorporating bench data where available.
- Validated first-order power/thermal model against measurements (or documented failure to match with revised assumptions).
- Risk register updated with test-derived likelihoods where applicable.
- Draft laser safety plan and instrumentation list finalized from outline.
- Prioritized component procurement list for Phase 1 integration (if pursued).
- Quantified performance envelope with **explicit uncertainty statements** — no point estimates without bounds.
- **Naming consistency verified** (MPL-D internal shorthand only; full title used in all safety and requirements artifacts).

---

## Phase 1: Integrated ground and limited flight test (outline only)

### Objectives

- Integrate payload mockup on surrogate ground platform and optionally limited flight on authorized test range.
- Measure beam stability under real prop/rotor vibration (not vibration table alone).
- Assess power bus interaction with host avionics.

### Success metrics (indicative — not committed)

- Payload remains within host mass/power budget with documented duty cycle.
- No safety interlock failures in scripted ground tests.
- Flight test (if authorized): beam pattern stable within quantified wander bounds at hover — **engagement effectiveness still not claimed**.

### Dependencies

- Phase 0 exit criteria met.
- Host platform interface confirmed (`hardware/interface_spec.md`).
- Regulatory and airworthiness review for flight segment.
- ROE and legal review for field laser emission.

### Duration placeholder

6–12 months after Phase 0 completion; highly uncertain.

---

## Regulatory and safety overhead (blunt statement)

Moving past bench testing requires laser safety classification analysis (IEC 60825-1), potential notification or authorization for outdoor emission, aviation coordination, and review under Protocol IV to the CCW on blinding laser weapons. Export control (ITAR/EAR) may apply depending on final performance parameters and destination. **None of these approvals exist in the Preliminary Design repository state.** Phase 0 bench work still requires an LSO and written SOP before any Class 3B or open-beam operation. Flight or field employment is a separate program gate, not an extension of Phase 0.

---

## Recommended next actions

1. Assign LSO; complete NHZ for 940 nm + DOE stack (G-SAF-01/02).
2. Execute P0 procurement per `hardware/phase0_procurement_list.md`.
3. Run T-01/T-02 at alignment power; measure θ_half before full-power T-03.
4. Populate R-EFF-001 / R-VIB-001 with bench data — do not advance to Phase 0 exit without measurements.

## Open questions / gaps

- Program decision on whether Phase 1 flight test is authorized at all.
- Host platform selection (Solace vs smaller tactical) — affects all interface assumptions.
