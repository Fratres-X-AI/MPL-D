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

**Maturity:** Preliminary Design. Supporting evidence: Trade studies, 940 nm leading candidate, optical stack, procurement list, pulse/interlock spec, and Phase 0 gates documented. **No hardware procured, no NHZ completed, no bench test data.**

---

## Navigation

| Path | Contents |
|------|----------|
| [`docs/`](docs/) | Architecture, requirements, risk register, roadmap, physics basis |
| [`analysis/`](analysis/) | First-order power/thermal script, beam propagation notes, [940 nm link budget notes](analysis/nir_940nm_link_budget_notes.md) |
| [`hardware/`](hardware/) | Interface spec; [candidate components](hardware/candidate_components.md); [procurement list](hardware/phase0_procurement_list.md); [optical layout](hardware/preliminary_optical_layout.md); [pulse control](hardware/pulse_control_spec.md); [surrogate sensors](hardware/surrogate_sensor_procurement.md) |
| [`tests/`](tests/) | Phase 0 bench test plan outline (no flight test in initial scope) |

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

1. **Assign LSO; complete NHZ** for 940 nm + DOE stack (G-SAF-01/02 in `docs/ARCHITECTURE.md`).
2. **Execute P0 procurement** per [`hardware/phase0_procurement_list.md`](hardware/phase0_procurement_list.md).
3. **Run Phase 0 T-01–T-03** with three-class surrogates per [`hardware/surrogate_sensor_procurement.md`](hardware/surrogate_sensor_procurement.md).
4. **Populate R-EFF-001 / R-VIB-001** with measured bench data before claiming Phase 0 progress toward exit.

---

## Tone and philosophy

Grounded and realistic. Favor simplicity, producibility, and cost-exchange over maximum theoretical performance. Treat this primarily as a defensive countermeasure / sensor attack tool rather than a primary hard-kill weapon.
