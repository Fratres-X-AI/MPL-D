# Risk Register — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Concept. Supporting evidence: Risks identified from first principles, public literature classes, and stated project constraints. No test data to adjust likelihood beyond qualitative assessment.

**Core uncertainty (explicit):** Many low-power multi-point dazzler concepts have sparse public flight-test validation against operationally relevant threats under dynamic conditions. Effectiveness against filtered, AGC-equipped, or AI-assisted sensors is **not established** in open literature at known power tiers. This is a primary program risk, not a minor documentation gap.

Safety and policy entries below use the full descriptive title. MPL-D appears only in this document header as internal codename context.

---

## Risk table

| ID | Category | Risk description | Potential impact | Likelihood | Evidence basis | Mitigation options (complexity / cost / SWaP) | Status |
|----|----------|------------------|------------------|------------|----------------|-----------------------------------------------|--------|
| R-VIB-001 | Technical | Vibration-induced beam wander and alignment drift on propeller-driven or VTOL platforms decenter the multi-point pattern on target sensor FOV | To be quantified post-bench | To be quantified post-bench | Pending measured irradiance and image degradation data on defined surrogate sensor set | Update with actual bench data from Phase 0 T-01/T-05. Do not advance system maturity label until populated with measured values. | Open |
| R-THM-001 | Technical | Thermal management limits on small UAV reduce laser duty cycle and mission endurance | Dazzle unavailable when needed; host battery depleted 10–30% faster during continuous dazzle (planning estimate, unvalidated) | H | First principles (η_wp 0.15–0.35 → heat >> optical out); drone thermal literature | Heat sinking to airframe; pulsed operation; lower P_opt (reduces effect); forced cooling fan (+mass/power) | Open |
| R-ATM-001 | Atmospheric | Clear-air attenuation, haze, fog, and scintillation reduce effective range below tactically useful thresholds | Useful engagement range may be <100–300 m in degraded conditions vs planning estimates at 500 m+ | H | Public atmospheric optics; Beer-Lambert models | Wavelength trade study; accept shorter envelope; multiple engagement geometry (increases ROE complexity) | Open |
| R-EYE-001 | Technical / Policy | Eye-safety non-compliance (IEC 60825-1) or collateral exposure to personnel/aircrew from diverging beams or specular reflection during platform maneuver | Injury; program termination; legal liability | M | IEC 60825-1 framework; divergence geometry | NHZ analysis; beam dumps; interlocks; training (admin cost); reduce power/aperture (reduces dazzle) | Open |
| R-ROE-001 | Policy-Legal-ROE | Design or employment parameters interpreted as prohibited blinding laser under Protocol IV to the CCW | Weapon system classification; operational prohibition | M | Treaty text; employment-dependent | Defensive CONOPS; sensor-only targeting; pulse limits; legal review (process overhead) | Open |
| R-EXP-001 | Policy-Legal-ROE | Export control (ITAR/EAR) triggered by laser performance, integration data, or foreign access | Shipping/license delays; compliance violations | M | Public export control frameworks; performance thresholds uncertain | Early compliance screening; segregate repo access; limit performance in exportable configs | Open |
| R-EFF-001 | Technical | Limited validated open data on real-world effectiveness against military or hardened FPV UAS sensors (filters, AGC, burst modes, AI rejection) | To be quantified post-bench | To be quantified post-bench | Pending measured irradiance and image degradation data on defined surrogate sensor set | Update with actual bench data from Phase 0 T-01/T-05. Do not advance system maturity label until populated with measured values. | Open |
| R-PWR-001 | Technical | Power budget impact on host platform mission time | Reduced sortie duration 5–25% depending on duty cycle (uncertain) | H | First-order power model | Lower optical power; duty cycling; larger host platform | Open |
| R-SUP-001 | Technical | Producibility and supply-chain risk for custom diffractive optics or high-reliability laser modules | Schedule slip 3–12 months; cost overrun 2× | M | Industry lead times for custom DOEs; single-source diodes | COTS multi-emitter array instead of custom DOE (alignment risk trade); dual-source qualification (+cost) | Open |
| R-TRK-001 | Operational | Static pattern without closed-loop tracking fails against maneuvering targets | Missed sensor exposure during engagement window | H | Geometry first principles | Add tracking/gimbal (+SWaP; Phase 1+); cooperative target scenarios only (limited ops value) | Open |
| R-EMI-001 | Technical | Laser driver EMI degrades host GPS/comms | Navigation failure on host | L–M | Known EMI coupling class; no test on selected host | Shielding; filtering; spatial separation (mass) | Open |
| R-DOE-001 | Technical | DOE zero-order leakage and efficiency loss waste power and create hazard path | 15–40% optical power in uncontrolled order (vendor-class estimate); eye hazard | M | Public DOE efficiency ranges | Block zero order; measure before full power; replace DOE with emitter array (+wiring) | Open |
| R-DAT-001 | Technical | AI-generated design documentation contains omission or numeric error | Wrong design decisions before independent review | M | Known LLM documentation risk | Independent review; bench validation before commitment | Open |
| R-INT-001 | Operational | Host platform interface (Solace or other) payload/power limits unknown | Integration infeasible without redesign | M | No vendor datasheet in repo | Early vendor engagement; ground mockup only Phase 0 | Open |
| R-REG-001 | Policy-Legal-ROE | Outdoor or flight laser tests without regulatory authorization | Fines; test shutdown | M | Local aviation/laser rules vary | Restrict Phase 0 to indoor bench; legal review before outdoor | Open |

**Likelihood key:** H = High, M = Medium, L = Low (qualitative; no historical failure rate data for this program).

---

## Mandatory risk expansions

### R-VIB-001 — Vibration (detail)

At range R = 500 m, angular jitter Δθ = 0.5 mrad produces lateral spot displacement Δx ≈ R·Δθ ≈ 0.25 m — potentially moving beamlets off a cm-class sensor FOV. VTOL platforms often exhibit narrowband energy at rotor harmonics. Vibration table Phase 0 test quantifies sensitivity; it does not prove flight performance.

**Post-bench update (pending):** Likelihood, potential impact, and mitigation trade space for this risk remain **unquantified** until Phase 0 delivers measured spot displacement (T-05) and pattern/irradiance context (T-01) on the **defined surrogate sensor set**. Until then, retain the first-principles displacement model above; do **not** map vibration-table results to propeller/VTOL flight engagement. Mitigation options shall be rewritten only after T-01/T-05 data are logged with uncertainty — **do not** advance the system maturity label until populated with measured values.

### R-THM-001 — Thermal (detail)

For P_opt = 5 W and η_wp = 0.22, dissipated heat ≈ 18 W continuous. Small tactical drones often allocate 50–200 W total propulsion power; continuous 18 W dazzle is a significant fraction. Duty cycling reduces average but also reduces dazzle probability.

### R-EFF-001 — Effectiveness data gap (detail)

Bench surrogate cameras (fixed exposure, no narrowband filter) may saturate at irradiance levels insufficient for filtered military EO systems. Public demonstrations of laser dazzlers often lack peer-reviewed engagement data against modern FPV stacks at operational ranges under relative motion. **Do not extrapolate Phase 0 surrogate results to threat effectiveness.**

**Effectiveness against representative sensors (post-bench, pending):** Representativeness of bench outcomes against military or hardened FPV stacks remains **unresolved** until measured irradiance and image-degradation data exist for each class in the minimum surrogate sensor set. Phase 0 T-01 and T-05 supply inputs to bound whether multi-point irradiance stays on-sensor under jitter; they do **not** by themselves establish operational dazzle against filtered, AGC-controlled, or AI-assisted threat sensors. Likelihood and impact fields stay **"To be quantified post-bench"** until those measurements are linked to surrogate exposure records — **do not** promote maturity or effectiveness claims until the risk table cells contain measured values, not extrapolation from surrogate bench success.

### R-ROE-001 — Protocol IV (detail)

The Counter-UAS Multi-Point Laser Dazzler Prototype is intended for sensor denial on hostile UAS, not deliberate permanent blinding of human vision. However, diverging beams and platform dynamics create human exposure paths. Legal review must precede any operational deployment. Classification as prohibited blinding weapon is **employment- and parameter-dependent** — not resolved at Concept maturity.

---

## Recommended next actions

1. Prioritize R-EFF-001 and R-EYE-001 in Phase 0 test design — surrogate vs threat representativeness and NHZ.
2. Update likelihood for R-VIB-001 and R-THM-001 after bench and vibration table data.
3. Initiate export control screening (R-EXP-001) before foreign vendor or partner access.

## Open questions / gaps

- No program-selected wavelength → eye hazard and atmospheric risks remain bounded but not finalized.
- No selected host platform → R-INT-001 and R-PWR-001 remain open with wide uncertainty.
