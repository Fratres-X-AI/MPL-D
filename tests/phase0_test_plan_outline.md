# MPL-D internal codename | Counter-UAS Multi-Point Laser Dazzler Prototype

**Document:** Phase 0 Test Plan Outline  
**Maturity:** Concept. Supporting evidence: No test procedures have been executed. This outline supports planning only.

**Scope:** Bench-top proof-of-concept for multi-point pattern generation and surrogate sensor exposure measurement. **No flight test** in Phase 0 initial scope. Outdoor testing requires additional regulatory review beyond this outline.

---

## 1. Objectives

1. Demonstrate multi-point optical pattern at bench distance (1–10 m) with documented irradiance map.
2. Measure image degradation on surrogate EO cameras (commercial USB/CSI modules) under controlled exposure.
3. Log electrical power and module temperature vs duty cycle.
4. Characterize beam wander under simulated platform vibration (limited vibration table test).

**Success is defined as data collection**, not operational dazzle effectiveness against representative threat UAS.

---

## 2. Prerequisites

| Item | Requirement |
|------|-------------|
| Laser Safety Officer (LSO) | Required before Class 3B+ or any unenclosed beam work |
| Controlled access lab | Door interlock or controlled hours; signage per IEC 60825-1 awareness |
| Instrumentation | Calibrated power meter, beam profiler or scanning slit (if available), thermocouple/IR sensor |
| Surrogate sensors | Commercial cameras with documented specs; not claimed as threat-representative |
| Legal review | Internal review for Protocol IV CCW implications and local laser use regulations |

---

## 3. Safety Controls (Mandatory)

### 3.1 Exclusion zones

- Nominal hazard zone computed from worst-case irradiance and divergence before first energization.
- Physical barriers (beam stops, curtains) for all specular reflection paths.
- No personnel in hazard zone during emission; use remote firing station.

### 3.2 Engineering controls

- Key switch hardware inhibit in series with emitter enable.
- Software time-out: maximum pulse duration enforced in firmware (bench controller).
- Emergency stop cutting emitter power independently of software.
- Zero-order beam from DOE (if used) must be blocked or dumped; verify with low-power alignment procedure first.

### 3.3 Administrative controls

- Written standard operating procedure (SOP) approved by LSO.
- Laser safety eyewear matched to wavelength(s) — **not** a substitute for beam containment on bench.
- Training log for all participants.

### 3.4 PPE

- Wavelength-appropriate laser eyewear when within nominal hazard boundary.
- Non-reflective tools and clothing in optical path vicinity.

---

## 4. Test Cases (Outline)

| ID | Test | Method | Data recorded | Pass criterion (Phase 0) |
|----|------|--------|---------------|--------------------------|
| T-01 | Pattern formation | Visual + beam profiler at 2 m | Spot count, spacing, relative power | Pattern matches design intent within measurement uncertainty |
| T-02 | Irradiance vs range | Power meter at 1, 2, 5, 10 m | I vs R | Within ±50% of first-order model OR document deviation |
| T-03 | Surrogate dazzle | Camera + fixed exposure captures | Image saturation/bleed metrics | Qualitative degradation observed; no threshold claim |
| T-04 | Power/thermal | Wattmeter + thermocouple, duty cycles 10–100% | P_elec, T vs time | Thermal equilibrium documented; no runaway in 10 min |
| T-05 | Vibration sensitivity | Vibration table, low amplitude sweep | Spot displacement on target | Displacement quantified; no pass/fail vs engagement |

---

## 5. Instrumentation List (Draft)

- Laser power meter (calibrated, appropriate for wavelength)
- Optical power sensor for each beamlet (optional; increases confidence)
- USB/CSI surrogate camera(s) with fixed lens
- Digital oscilloscope or data logger for current draw
- Thermocouple or IR thermometer on laser heat sink
- Vibration table with accelerometer (if available)
- Neutral density filters for alignment at reduced power

---

## 6. Data Management

- Raw data stored under `tests/logs/` (gitignored).
- Summary results incorporated into `docs/ROADMAP.md` Phase 0 exit artifacts and `docs/RISK_REGISTER.md` likelihood updates.
- No performance claims in repository without linked raw data files and uncertainty statement.

---

## 7. Regulatory Flags

| Activity | Additional review required |
|----------|---------------------------|
| Indoor bench, enclosed low-power alignment | LSO + internal SOP |
| Indoor open-beam Class 3B+ | Full NHZ/OHD analysis, registered LSO |
| Outdoor propagation | Local aviation/laser notification rules; may require authority coordination |
| Flight test | **Out of Phase 0 scope**; separate airworthiness and ROE review |

---

## Recommended next actions

1. Appoint or identify LSO; complete wavelength-specific hazard analysis before procurement.
2. Draft detailed SOP from this outline with named responsible engineer.
3. Procure surrogate cameras and calibrated power meter before emitter purchase.

## Open questions / gaps

- Selected laser wavelength(s) and class — determines entire safety case.
- Whether DOE zero-order beam requires dedicated dump optics in bench layout.
