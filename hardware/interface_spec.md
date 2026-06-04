# Hardware Interface Specification

**Project:** Counter-UAS Multi-Point Laser Dazzler Prototype  
**Maturity:** Concept. Supporting evidence: Interface parameters are planning placeholders only. No CAD, no measured mass properties, no electrical integration test data.

---

## 1. Purpose

Define preliminary mechanical, electrical, and data interfaces between a host UAV and a dazzler payload module. This document supports Phase 0 bench integration planning only. No flight clearance is implied.

---

## 2. Host Platform Classes

| Class | Example reference | Payload mass budget (indicative) | Notes |
|-------|-------------------|----------------------------------|-------|
| Small tactical multirotor | Generic 5–15 kg MTOW class | 0.3–1.5 kg module | Severe power/thermal constraint |
| Medium VTOL / fixed-wing | Solakair Solace-class (public marketing references only) | 2–8 kg module (assumed; unverified against Solace payload spec) | Requires airframe vendor confirmation |

**Assumption:** Solace payload capacity, power bus, and hardpoint geometry are **unknown** in this repository. All Solace references require vendor data sheet verification.

---

## 3. Mechanical Interface (Preliminary)

| Parameter | Planning value | Uncertainty |
|-----------|----------------|-------------|
| Mounting | 2× standard drone payload rails or custom 4-bolt plate | Final pattern TBD with host |
| Module envelope (L×W×H) | 150 × 80 × 60 mm (order of magnitude) | ±30% without detailed layout |
| CG offset from mount | < 20 mm aft of mount plane (target) | Requires CAD |
| Vibration isolation | 4× elastomer mounts or integrated dampers | Effectiveness unvalidated |

**Rejected for Phase 0:** Active stabilization gimbal (adds mass, complexity, and control coupling).

---

## 4. Electrical Interface

| Signal / power | Specification (planning) | Notes |
|----------------|-------------------------|-------|
| Input voltage | 18–26 V DC (6S LiPo class) or host-defined bus | Must match host BEC/generator capacity |
| Peak electrical draw | 15–50 W (depends on optical power tier) | See `analysis/power_thermal_budget.py` |
| Steady-state draw | 5–25 W typical for low-duty dazzle | Duty cycle limits endurance |
| Control | PWM arm/disarm + UART/CAN command (host-defined) | Interlock required before emitter enable |
| Ground | Common ground with host; shielded harness for emitters | EMI uncharacterized |

**Safety interlock (mandatory for any energization):**

1. Hardware enable line held inactive until software + hardware arming sequence complete.
2. Key switch or equivalent physical inhibit for bench and field configuration.
3. Fault line: over-temperature → disable emitters.

---

## 5. Thermal Interface

| Parameter | Planning bound | Risk |
|-----------|----------------|------|
| Heat rejection to ambient | 10–35 W module dissipation | May require forced airflow from prop wash or dedicated fan |
| Operating ambient | −10 °C to +40 °C (planning) | Derating above 35 °C unquantified |
| Thermal time constant | Minutes to thermal steady state | Limits safe duty cycle on small hosts |

Host must provide either adequate convective airflow path or accept reduced dazzle duty cycle.

---

## 6. Optical / Pointing Interface

| Parameter | Planning value | Notes |
|-----------|----------------|-------|
| Boresight alignment | Coarse alignment to host camera or INS boresight | ±1–3° acceptable for wide pattern; tracking not in Phase 0 |
| Field of regard | Fixed forward ±15° (mechanical aim at install) | No in-flight steering in Phase 0 concept |
| Pattern | Static multi-spot DOE or fixed emitter array | See `docs/ARCHITECTURE.md` |

---

## 7. Data / Control Interface (Logical)

Minimum command set (conceptual):

| Command | Effect |
|---------|--------|
| `SAFE` | Disable all emitters; default power-up state |
| `ARM` | Enable arming chain; no optical output yet |
| `DAZZLE_PULSE` | Timed emission with max duration cap (e.g., ≤ 2 s per pulse; value TBD with safety review) |
| `STATUS` | Return temperature, fault flags, emitter state |

**Not in Phase 0 scope:** Closed-loop track-to-dazzle; requires separate requirements and safety case.

---

## 8. Integration Risks (Interface-Specific)

1. **Power bus sag:** Laser driver inrush may brown out host avionics if bus impedance is high.
2. **EMI:** Switching drivers may interfere with GPS/comms; no test data.
3. **Vibration:** Prop/rotor harmonics may decenter beam pattern; see `docs/RISK_REGISTER.md` R-VIB-001.

---

## Recommended next actions

1. Obtain host platform electrical architecture diagram and confirmed payload mass limit.
2. Draft wiring harness diagram with interlock chain for Phase 0 bench fixture (non-flying).
3. Define mechanical mock mount for vibration table testing.

## Open questions / gaps

- Confirmed Solace (or alternate host) payload hardpoint drawing and power tap location.
- Required connector standard (XT60, Anderson, military circular — host-dependent).
