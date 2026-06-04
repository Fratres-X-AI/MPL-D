# Phase 0 Bench Standard Operating Procedure — DRAFT

**Project:** Counter-UAS Multi-Point Laser Dazzler Prototype  
**Gate:** G-SAF-03  
**Status:** **DRAFT — NOT APPROVED.** Requires LSO signature before use.

**Scope:** Indoor bench only. 940 nm + DOE configuration. No flight. No outdoor propagation.

---

## 1. Authorized personnel

Only operators listed on the LSO authorization log (`docs/lso_assignment_record.md`) may execute this SOP.

---

## 2. Pre-session checklist

| Step | Action | Initial |
|------|--------|---------|
| 2.1 | Verify LSO authorization for today's session | |
| 2.2 | Verify eyewear OD approved by LSO for 940 nm | |
| 2.3 | Verify key switch / E-stop / interlock functional | |
| 2.4 | Verify zero-order dump aligned (visual at alignment power) | |
| 2.5 | Verify beam blocks and curtains in place | |
| 2.6 | Verify power meter calibrated at 940 nm | |
| 2.7 | Verify no unauthorized personnel in controlled area | |
| 2.8 | Confirm mode = SAFE at power-up | |

**Stop if any item fails. Return to SAFE.**

---

## 3. Operating modes (see `hardware/pulse_control_spec.md`)

| Mode | Optical output | When |
|------|----------------|------|
| SAFE | Off | Default |
| ALIGN | ≤ LSO-defined ceiling | Alignment only |
| ARM | Enabled, suppressed | Pre-fire |
| PULSE | LSO-approved profile | T-01–T-05 only |

**Full 10 W CW prohibited unless LSO explicitly authorizes for a named test step.**

---

## 4. Alignment procedure (ALIGN mode)

1. LSO or delegate confirms NHZ and controlled area.
2. Insert ND filters as directed by LSO.
3. Enable ALIGN at current ≤ LSO ceiling.
4. Center collimated beam on DOE input; verify zero-order into dump.
5. Document spot pattern at 2 m (photo + profiler if available).
6. Return to SAFE before any personnel enter optical path.

---

## 5. Test execution (PULSE mode)

| Test | Max power authorized by LSO | Record |
|------|----------------------------|--------|
| T-01 Pattern | LSO sets | Spot map |
| T-02 Irradiance vs range | LSO sets | Power meter log |
| T-03 Surrogate dazzle | LSO sets | Camera frames + exposure metadata |
| T-04 Thermal/duty | LSO sets | Current + temperature log |
| T-05 Vibration | LSO sets | Displacement vs frequency |

Raw data → `tests/logs/` (gitignored).

---

## 6. Emergency procedures

| Event | Action |
|-------|--------|
| Exposure suspected | E-stop; medical protocol per LSO |
| Interlock open | Automatic SAFE; investigate before reset |
| Over-temperature fault | SAFE; cooldown per LSO |
| Fire | E-stop; fire extinguisher; evacuate |

---

## 7. Post-session

1. Return to SAFE; remove key.
2. Log session in operator log (date, operators, tests, max power, incidents).
3. Deliver logs to LSO within 24 h.

---

## 8. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Laser Safety Officer | **PENDING** | — | — |

**G-SAF-03 OPEN until signed.**
