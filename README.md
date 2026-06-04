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

**Maturity:** Concept. Supporting evidence: No hardware, simulation validation, or test data generated in this repository. All content is preliminary design initiation only.

---

## Navigation

| Path | Contents |
|------|----------|
| [`docs/`](docs/) | Architecture, requirements, risk register, roadmap, physics basis |
| [`analysis/`](analysis/) | First-order power/thermal script and beam propagation notes |
| [`hardware/`](hardware/) | Host–payload interface specification (preliminary) |
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

Naming hygiene for MPL-D internal codename is complete in repository headers and navigation. Prioritized next steps:

1. **Review and expand [`docs/RISK_REGISTER.md`](docs/RISK_REGISTER.md)** with any Fratres X AI domain knowledge or host-platform specifics not captured at Concept initiation.
2. **Refine laser source trade study** in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) Section 2 — down-select wavelength and DOE vs multi-emitter architecture with datasheet-backed bounds.
3. **Validate [`analysis/power_thermal_budget.py`](analysis/power_thermal_budget.py)** against a known commercial laser module datasheet (replace assumed η_wp and divergence).
4. **Draft initial laser safety checklist** from [`tests/phase0_test_plan_outline.md`](tests/phase0_test_plan_outline.md) and assign Laser Safety Officer before procurement.

---

## Tone and philosophy

Grounded and realistic. Favor simplicity, producibility, and cost-exchange over maximum theoretical performance. Treat this primarily as a defensive countermeasure / sensor attack tool rather than a primary hard-kill weapon.
