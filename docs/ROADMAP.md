# Development Roadmap — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Phase 0 pre-energization — G-DOC **PASS**, G-PROTO **PASS**, G-ENR **BLOCKED**.

**Evidence / analysis status:** Documentation and analysis scripts complete. **No LSO signature, no hardware, no tests executed.**

**Known gaps:** Phase 1 and Phase 2 **not authorized** — criteria listed for planning only.

**Next required action:** Close G-SAF-01/02/03; procure P0 (G-HW-P0); begin T-01 at alignment power.

---

## Phase map

| Phase | Name | Authorization | Flight | Maturity target |
|-------|------|---------------|--------|-----------------|
| **Complete** | Preliminary Design | Closed | No | Preliminary Design ✓ |
| **Current** | Phase 0 — bench POC | G-ENR blocked | **No** | Implemented & Tested (bench) — **not reached** |
| **Future** | Phase 1 — ground / limited flight | **Not authorized** | If separately approved | Validated (subsystems) — **not planned active** |
| **Future** | Phase 2 — engineering validation | **Not authorized** | Possible | Validated — **not planned active** |

---

## Phase 0 — Proof of concept (bench)

### Entry criteria (met)

- [x] Architecture, requirements, RTM, risk register exist
- [x] Safety case draft, SOP draft, test procedures T-01–T-05
- [x] Analysis scripts and validation status documented
- [x] G-DOC PASS, G-PROTO PASS

### Entry criteria (not met — blocks execution)

- [ ] G-SAF-01 LSO assigned
- [ ] G-SAF-02 NHZ complete and approved
- [ ] G-SAF-03 SOP LSO-approved
- [ ] G-HW-P0 hardware on hand
- [ ] G-ENR energization authorized

### Objectives

1. Multi-point pattern on bench (T-01)
2. Irradiance vs range vs model (T-02)
3. Surrogate camera degradation (T-03)
4. Power/thermal vs duty (T-04)
5. Vibration sensitivity (T-05)

### Exit criteria

| Criterion | Evidence artifact | Responsible party |
|-----------|-------------------|-------------------|
| Pattern documented 2–10 m | T-01 record + photos | Test lead |
| Irradiance within ±50% of model OR model revised | T-02 log | Analyst |
| Qualitative surrogate saturation only | T-03 images | Test lead |
| No thermal runaway 10 min duty test | T-04 log | Thermal lead |
| Vibration wander quantified | T-05 log | Mechanical lead |
| RTM updated with evidence links | REQUIREMENTS_TRACEABILITY | Systems |
| Risk register updated (R-EFF, R-VIB) | RISK_REGISTER | Systems |
| LSO safety package signed | G-SAF-02/03 | **LSO** |

### Explicit exclusions

Flight test; outdoor emission; threat targets; operational range claims; closed-loop tracking.

### Duration (placeholder)

3–6 months after G-ENR — resource-dependent, **not committed**.

---

## Phase 1 — Integrated ground and limited flight (outline — not authorized)

### Entry criteria

- [ ] Phase 0 exit criteria met
- [ ] ICD Rev A with host vendor (or waiver documented)
- [ ] Program authorization for ground integration
- [ ] Legal/regulatory review for any outdoor/flight laser emission
- [ ] Export control determination updated if config changed

### Objectives

- Payload mockup on ground platform; optional hover flight on authorized range
- Beam stability under prop/rotor vibration (beyond vibe table)
- Power bus / EMI characterization with host

### Exit criteria (indicative)

| Criterion | Evidence |
|-----------|----------|
| Mass/power within host budget | Measured log + host sign-off |
| Interlock fail-safe demonstrated | Test record |
| Flight segment (if done): pattern wander within quantified bounds | Flight log — **no effectiveness claim** |

### Responsible parties (TBD)

Integration lead, host vendor, LSO, airworthiness authority as applicable.

### Duration (placeholder)

6–12 months after Phase 0 — **highly uncertain**.

---

## Phase 2 — Engineering validation (outline — not authorized)

### Entry criteria

- [ ] Phase 1 exit (if Phase 1 executed)
- [ ] Program decision to pursue threat-representative testing
- [ ] Legal/ROE/Protocol IV review for expanded scope
- [ ] Export and safety approvals for test articles

### Objectives

- Threat-representative or government-furnished sensor testing (if approved)
- Environmental campaign (selected conditions)
- Reliability / duty cycle validation
- Updated effectiveness bounds with uncertainty — **still not operational fielding**

### Exit criteria (indicative)

Documented test report with bounded performance envelope; updated TDP baseline; risk register with measured residual ratings; **no fielding without separate program gate**.

---

## Regulatory overhead (all phases)

IEC 60825-1, aviation rules, Protocol IV, ITAR/EAR — **none resolved** at Preliminary Design. See [`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md), [`EXPORT_CONTROL_SCREENING.md`](EXPORT_CONTROL_SCREENING.md), [`ROE_PROTOCOL_IV.md`](ROE_PROTOCOL_IV.md).

---

## Gate cross-reference

| Gate | Phase | Status |
|------|-------|--------|
| G-DOC | Pre-Phase 0 | PASS |
| G-PROTO | Pre-Phase 0 | PASS |
| G-SAF-* | Phase 0 entry | OPEN |
| G-HW-P0 | Phase 0 entry | OPEN |
| G-ENR | Phase 0 execution | BLOCKED |
| Phase 0 exit | → Phase 1 consideration | Not met |
| Phase 1 authorization | — | **Not granted** |
| Phase 2 authorization | — | **Not granted** |

Full table: [`phase0_gate_status.md`](phase0_gate_status.md)

---

## Next steps

1. Assign LSO — G-SAF-01
2. Complete NHZ + SOP — G-SAF-02/03
3. Procure P0 — G-HW-P0
4. Execute T-01–T-05 — Phase 0 exit
