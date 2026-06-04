# Pulse Control and Interlock Specification (Preliminary)

**Maturity:** Preliminary Design — logical timing, safety interlocks, and host interface defined. **No firmware, no schematic, no bench validation.**

**Scope:** 940 nm NIR-primary bench path; visible alternate requires separate LSO pulse classification.

---

## 1. Operating modes

| Mode | Optical output | Entry condition |
|------|----------------|-----------------|
| SAFE | Off | Default at power-up; fault state |
| ALIGN | Reduced current (LSO-defined ceiling) | Key enable + ALIGN command |
| ARM | Driver enabled, output suppressed until FIRE | ALIGN complete + ARM sequence |
| PULSE | Timed emission per profile | ARM + FIRE + interlocks closed |

---

## 2. Pulse profile (planning — LSO must approve)

| Parameter | Planning value | Notes |
|-----------|----------------|-------|
| Burst duration | 0.1–3.0 s | CONOPS input; NHZ may restrict |
| Intra-burst structure | Optional 10× 20 ms pulses @ 50% drive | Flicker hypothesis — **unvalidated** |
| Cooldown | ≥ 5 s minimum between bursts (planning) | Thermal T-04 may increase |
| Max duty cycle | ≤ 10% over 60 s window (planning) | Until thermal data |
| Peak drive | ≤ 13 A (vendor max) | AeroDiode class limit |

---

## 3. Hardware interlocks (REQ-S-002)

1. **Key switch** in series with laser enable — physical removal → SAFE.
2. **E-stop** — cuts driver power independent of MCU.
3. **Over-temperature** — heat sink sensor trips enable (threshold TBD at T-04).
4. **Interlock loop** — bench door or enclosure chain; open → SAFE.

---

## 4. Host interface (logical — `interface_spec.md`)

| Signal | Direction | Function |
|--------|-----------|----------|
| TARGET_LOCK | Host → payload | Preconditions FIRE (no closed-loop aim in Phase 0) |
| FIRE | Host → payload | Starts approved pulse profile |
| SAFE | Host → payload | Immediate disable |
| FAULT | Payload → host | Over-temp, interlock open |

Phase 0 bench may use manual FIRE button with TARGET_LOCK tied true.

---

## 5. Logging requirements (T-04)

- Timestamp, mode, burst duration, peak/avg current, heat sink temperature pre/post burst.

---

## Recommended next actions

1. LSO review pulse profile before driver commissioning.
2. Implement on STM32-class MCU with watchdog and fail-safe GPIO default-off.

## Open questions / gaps

- IEC 60825-1 classification for pulsed vs CW at same average power — LSO determination.
- EMI from 13 A switched driver on host GPS — R-EMI-001.
