# Drone-Mounted Multi-Point Laser Dazzler for Counter-UAS Sensor Denial

**Codename:** MPL-D | **Full title:** Counter-UAS Multi-Point Laser Dazzler Prototype

**Attribution:** Fratres X AI — Defense Prototype Documentation  
**Repository:** https://github.com/Fratres-X-AI/MPL-D (private)

---

## Project definition

**Project:** Drone-Mounted Multi-Point Laser Dazzler for Counter-UAS Sensor Denial

**Objective:** Design a practical, drone-mountable (or air-launched) multi-point / pattern laser dazzler system focused on non-kinetic sensor denial against hostile drones. The primary goal is to degrade, blind, or overwhelm electro-optical sensors and cameras on enemy UAS rather than attempting hard-kill burn-through.

### Core requirements and constraints

- Must be mountable on existing or near-term drone platforms (target weight class: small-to-medium UAVs, with consideration for integration onto platforms like Solakair Solace or similar VTOL/fixed-wing systems).
- Use a multi-point or patterned beam approach (multiple lower-power emitters or beam-splitting optics) instead of a single high-power focused beam.
- Prioritize non-kinetic / soft-kill effects (sensor dazzling, image degradation, navigation disruption, or temporary blinding of EO/IR cameras).
- Keep the system as simple, low-power, and producible as possible while remaining effective.
- Account for real-world constraints: power budget, thermal management, size/weight, vibration, and atmospheric effects.
- Consider eye-safety and rules-of-engagement implications for operational use.

---

## Current status

**Maturity:** Phase 0 — **Elite prototype package complete (G-PROTO PASS).** G-ENR blocked. Supporting evidence: full design, test, traceability, and analysis artifacts in [`ELITE_PROTOTYPE_HANDOFF.md`](docs/ELITE_PROTOTYPE_HANDOFF.md). **No LSO approval, no hardware energized, no bench tests executed.**

---

## Navigation

| Path | Contents |
|------|----------|
| [`docs/`](docs/) | [Handoff index](docs/ELITE_PROTOTYPE_HANDOFF.md), architecture, [CONOPS](docs/CONOPS.md), [traceability](docs/REQUIREMENTS_TRACEABILITY.md), [gate status](docs/phase0_gate_status.md) |
| [`analysis/`](analysis/) | Link budget, thermal pulse, vibration wander, prebench T-02 |
| [`hardware/`](hardware/) | Electrical, mechanical BOM, procurement, optics, pulse spec |
| [`firmware/`](firmware/) | Pulse controller state machine design |
| [`tests/`](tests/) | SOP, [procedures](tests/procedures/), [templates](tests/templates/) |

MPL-D is used as internal shorthand only. All formal and safety documentation uses the full descriptive title.

---

## Handoff criteria

After this session the repository must allow a new engineer or reviewer to immediately understand (a) exact current maturity level of every major element, (b) all assumptions and their uncertainty bounds, (c) the complete risk picture with evidence basis, and (d) a prioritized, actionable list of next engineering tasks to reach a bench-testable Phase 0 configuration. The state must be usable for planning without requiring reverse-engineering of the documents.

MPL-D is used as internal shorthand only. All formal and safety documentation uses the full descriptive title.

---

## Limitations (read before use)

Initial documents contain first-order engineering estimates only. All performance predictions, range claims, and component recommendations require independent verification against measured data or higher-fidelity modeling before any design commitment. AI generation of technical content carries inherent risk of omission or inaccuracy.

This repository describes defensive, non-kinetic sensor denial concepts only. It does not document hard-kill burn-through, anti-personnel employment, or classified performance parameters.

---

## Recommended immediate actions

Naming hygiene for MPL-D internal codename is complete in repository headers and navigation. Program baseline is **Preliminary Design — Phase 0 preparation**. Prioritized next steps:

1. **Assign named LSO** — sign [`docs/lso_assignment_record.md`](docs/lso_assignment_record.md), [`docs/phase0_safety_case_draft.md`](docs/phase0_safety_case_draft.md), [`tests/phase0_bench_sop_draft.md`](tests/phase0_bench_sop_draft.md).
2. **Order P0 hardware** — update [`hardware/procurement_status.md`](hardware/procurement_status.md).
3. **ALIGN-power commissioning** — zero-order checklist; then T-01.
4. **Do not claim T-02 complete** until power meter data logged — analytical report is pre-check only.

---

## Tone and philosophy

Grounded and realistic. Favor simplicity, producibility, and cost-exchange over maximum theoretical performance. Treat this primarily as a defensive countermeasure / sensor attack tool rather than a primary hard-kill weapon.
