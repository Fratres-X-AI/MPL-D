# System Architecture — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Concept. Supporting evidence: Architecture description and parameter bounds only. No breadboard, CAD release, or test data.

**Project objective (verbatim):** Design a practical, drone-mountable (or air-launched) multi-point / pattern laser dazzler system focused on non-kinetic sensor denial against hostile drones. The primary goal is to degrade, blind, or overwhelm electro-optical sensors and cameras on enemy UAS rather than attempting hard-kill burn-through.

---

## 1. High-level architecture

### Block diagram

```mermaid
flowchart TB
  subgraph payload [Payload Module]
    LS[Laser Source(s)]
    BCP[Beam Conditioning and Pattern Generation]
    OO[Output Optics and Aperture]
    MV[Mount and Vibration Isolation]
    PM[Power Management]
    TM[Thermal Management]
    CE[Control Electronics and Targeting Interface]
  end
  subgraph host [Host UAV]
    BUS[Power Bus]
    FC[Flight Controller]
    CAM[Optional Host Camera]
  end
  BUS --> PM
  PM --> LS
  PM --> TM
  PM --> CE
  CE --> LS
  LS --> BCP
  BCP --> OO
  MV --- payload
  FC --> CE
  CAM -.-> CE
  OO -->|optical pattern| TARGET[Target UAS EO/IR Sensor]
```

### Information and power flows

**Power flow:** Host DC bus → power management (conditioning, enable interlock) → laser drivers and control electronics. Majority of electrical energy converts to waste heat at laser modules (η_wp ≈ 0.15–0.35 planning range) → thermal management path to ambient or airframe.

**Control flow:** Flight controller or mission computer → arm/enable commands → control electronics → laser drivers (pulsed). Optional host camera metadata may cue dazzle timing in future phases; **Phase 0 has no closed-loop tracking.**

**Optical flow:** Laser source(s) → beam conditioning (collimation, filtering) → pattern generation (DOE or discrete emitters) → output aperture → free-space propagation → target sensor aperture (uncontrolled alignment unless platform pointing cooperates).

---

## 2. Recommended laser source(s)

### Recommended approach

**Primary recommendation (Phase 0):** Multiple discrete visible-wavelength diode laser modules (520–532 nm class) or a single diode-pumped solid-state (DPSS) module feeding a static diffractive optical element (DOE).

**Rationale:** Commercial availability, moderate wall-plug efficiency, established safety classification paths, and compatibility with COTS beam profiling for Phase 0. Visible wavelength simplifies surrogate camera testing (with acknowledged mismatch to IR-dominant military sensors).

| Option | Wavelength | Planning P_opt per module | Maturity | Evidence |
|--------|------------|---------------------------|----------|----------|
| Fiber-coupled diode modules | 520 nm ±10 nm | 0.5–2 W | Preliminary Design (component class) | Vendor datasheets exist; none selected here |
| Compact DPSS | 532 nm | 1–5 W | Preliminary Design (component class) | Higher efficiency than direct diode; thermal management required |
| VCSEL arrays | 850 nm (example) | mW–W class | Concept for this application | Less common for long-range dazzle; eye safety differs |

**Conservative total optical power (planning):** 2–10 W combined in pattern (low-watt to low-tens-of-watts upper planning bound for medium host); default analysis example uses 5 W in `analysis/power_thermal_budget.py`.

**Multi-wavelength:** Not recommended for Phase 0 — doubles driver, safety, and optics complexity. IR channel (e.g., 808 nm or 1550 nm class) may be needed for IR sensor denial but requires separate hazard analysis and test assets.

**Rejected:** Single high-power focused beam (10–100+ W class) — exceeds small UAV thermal/power budget, increases eye hazard and export sensitivity, contradicts multi-point requirement.

**Maturity:** Concept at system level. Component classes are commercial; integrated system is unbuilt.

---

## 3. Beam delivery / pattern generation

### Recommended approach

**Phase 0:** Static diffractive optical element (DOE) splitting one collimated beam into N spots **or** fixed linear array of 3–9 low-power emitters with individual collimation.

| Method | Pros | Cons |
|--------|------|------|
| Static DOE | Minimal moving parts; single emitter driver | Efficiency loss; zero-order leakage; alignment sensitive |
| Multiple emitters | No zero-order; per-beam control | Mechanical alignment drift; wiring/thermal complexity |
| Galvo scanning | Flexible pattern | Mass, power, vibration sensitivity — **rejected Phase 0** |
| MEMS scanning | Lower mass than galvo | Reliability and control complexity — **rejected Phase 0** |

**Pattern geometry (planning):** 3×3 or linear 5-spot array covering ~0.5–2° total field — wide enough to reduce precise tracking requirement; narrow enough to maintain per-beam irradiance at range. Exact angles **unvalidated**.

**Divergence:** 1–5 mrad half-angle per beamlet (compact optics class).

**Maturity:** Concept. DOE or array layout not fabricated.

---

## 4. Power and thermal budget

See `analysis/power_thermal_budget.py` and `docs/PHYSICS_BASIS.md`.

| Parameter | Conservative bound | Basis |
|-----------|-------------------|-------|
| P_opt (total pattern) | 2–10 W | Drone feasibility |
| η_wp | 0.15–0.35 | Literature/vendor class |
| P_elec at 5 W opt, η=0.22 | ~23 W | First-order |
| Q_diss at 5 W opt | ~18 W | First-order |
| Duty cycle (small host) | 10–30% average (planning) | Thermal/endurance guess |

**Cooling:** Passive heat sink to free stream air; optional 5–12 V fan (+2–5 W draw). Liquid cooling **rejected** for SWaP.

**Feasibility:** Bench demonstration is feasible on lab power. Continuous full-power operation on small tactical drone is **questionable** without aggressive duty cycling — see R-THM-001.

**Maturity:** Concept. No measured thermal curves.

---

## 5. Effective range and engagement envelope

**Blunt statement:** This repository does **not** certify an operational engagement range. First-order irradiance falls rapidly with range (∝ 1/R²) and atmospheric transmission.

| Target sensor class | Planning assessment | Evidence |
|--------------------|---------------------|----------|
| Commercial FPV CMOS (unfiltered, fixed exposure) | Bench dazzle likely at tens of meters; hundreds of meters **unvalidated** at 5 W multi-point | No program test data |
| Commercial UAS gimbal camera (AGC) | May auto-attenuate; dazzle duration reduced | Public sensor behavior class |
| Military/hardened EO/IR (filters) | Effectiveness **unknown** at planned power tier | R-EFF-001 |

**Conservative envelope (planning only, ±order of magnitude):**

- **Possible surrogate bench effect:** 1–20 m (Phase 0).
- **Uncertain outdoor effect:** 50–300 m in clear air against unfiltered sensors — **speculative**.
- **Unlikely without higher power or narrow tracking:** >500 m against agile filtered targets.

Atmospheric and scintillation may reduce bounds further.

**Maturity:** Concept. No range test data.

---

## 6. Major risks and limitations

Full register: [`RISK_REGISTER.md`](RISK_REGISTER.md).

Summary:

- Vibration and beam wander on VTOL/prop platforms
- Thermal and power limits on host endurance
- Atmospheric degradation
- Eye safety and Protocol IV / export control
- **Sparse validation of low-power multi-point dazzle against operational threats**

---

## 7. Integration concepts

### Solace-class VTOL / fixed-wing (air-to-air carry)

- **Concept:** Medium payload bay or external hardpoint mount; forward-fixed pattern aligned with approach axis.
- **Assumption:** Payload capacity and power tap **unverified** against Solakair Solace public materials — vendor confirmation mandatory (R-INT-001).
- **Employment concept (defensive only):** Host positions to place dazzler boreSight within target sensor FOV during intercept geometry; static pattern increases capture volume vs single beam.
- **Maturity:** Concept. No interface drawings.

### Small tactical multirotor

- **Concept:** 0.3–1.5 kg module under fuselage; short-duration dazzle pulses during terminal phase.
- **Constraint:** Severe power/thermal limits; likely ≤5 W optical and low duty cycle.
- **Maturity:** Concept.

### Air-launched (future)

- Not detailed in Phase 0. Would add seeker, battery, and safety arming complexity — **out of scope**.

**Rejected integration:** Body-fixed high-power turret with human-targeting capability — ROE and Protocol IV conflict.

---

## 8. Subsystem maturity summary

| Subsystem | Maturity | Supporting evidence |
|-----------|----------|---------------------|
| Laser Source(s) | Concept (system); Preliminary Design (COTS class) | No selected part number |
| Beam Conditioning & Pattern Generation | Concept | No DOE design file |
| Output Optics & Aperture | Concept | No optical design |
| Mount & Vibration Isolation | Concept | No CAD |
| Power Management | Concept | No schematic |
| Thermal Management | Concept | First-order heat estimate only |
| Control Electronics & Targeting Interface | Concept | Logical command set only |

---

## 9. Phase 0 / development next steps

See [`ROADMAP.md`](ROADMAP.md). Phase 0: bench pattern demo, irradiance map, surrogate camera test, power/thermal log, vibration table — **no flight**.

---

## Recommended next actions

1. Down-select laser architecture (DOE vs multi-emitter) based on SWaP and zero-order safety.
2. Run `analysis/power_thermal_budget.py` with candidate datasheet parameters.
3. Begin LSO-led hazard analysis before hardware purchase.

## Open questions / gaps

- Wavelength down-select (visible vs IR vs dual-band).
- Host platform confirmation for interface and mass split.
- Whether operational concept requires tracking (Phase 1+) vs acceptable static pattern limitations.
