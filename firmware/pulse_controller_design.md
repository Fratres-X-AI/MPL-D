# Pulse Controller Firmware Design

**Maturity:** Preliminary Design — state machine and timing spec. **No source code flashed; no hardware-in-loop test.**

**Target:** STM32-class MCU or equivalent; matches `hardware/pulse_control_spec.md`.

---

## State machine

```
SAFE ──(key+interlock+no fault)──► ARMED_IDLE
ARMED_IDLE ──(TARGET_LOCK)──► ARMED_LOCKED
ARMED_LOCKED ──(FIRE + cooldown ok)──► PULSING
PULSING ──(timer done)──► COOLDOWN
COOLDOWN ──(timer done)──► ARMED_LOCKED
ANY ──(fault|estop|key open)──► SAFE
```

---

## Timing parameters (defaults — LSO may override)

| Parameter | Default | Range |
|-----------|---------|-------|
| `PULSE_MS` | 500 | 100–3000 |
| `COOLDOWN_MS` | 5000 | ≥5000 |
| `MAX_DUTY_PERCENT` | 10 | 1–10 |
| `ALIGN_CURRENT_PERCENT` | 2 | LSO sets |

---

## Safety rules (firmware)

1. `ENABLE_OUT` hard low in SAFE; watchdog forces SAFE on hang.
2. Pulse count and total on-time logged to flash/serial.
3. Over-temp ADC threshold trips SAFE (threshold = LSO constant in header).
4. No FIRE unless TARGET_LOCK true for ≥100 ms debounce.

---

## Pseudocode (reference)

```c
// NOT COMPILED IN REPO — design reference only
if (state == SAFE) { laser_enable = 0; return; }
if (estop || !key || !interlock || overtemp) { state = SAFE; return; }
if (state == PULSING && elapsed >= PULSE_MS) { state = COOLDOWN; laser_enable = 0; }
```

---

## Recommended next actions

1. Implement on Nucleo-class board with driver mock before L-01 install.
2. Log serial CSV matching `tests/templates/` schemas.

## Open questions / gaps

- No production firmware repository or CI.
