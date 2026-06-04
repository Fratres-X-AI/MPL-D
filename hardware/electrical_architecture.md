# Electrical Architecture — 940 nm Phase 0 Bench Stack

**Maturity:** Preliminary Design — block diagram and interface spec. **No schematic capture, no PCB, no bench wiring.**

---

## Block diagram

```
[Host 24 VDC bench supply]
        │
        ▼
[Fuse 15 A] ──► [Key switch ENABLE] ──► [E-stop NC] ──► [Interlock loop]
        │
        ▼
[Laser driver module ≥13 A @ 1.7–1.8 V]
        │ TTL ENABLE ◄── [MCU pulse controller]
        │ FAULT ───────► MCU (interrupt)
        ▼
[AeroDiode-class 940 nm module SMA905]
        │
[Thermistor on sink] ──► MCU ADC + hardware OT trip
```

---

## Power budget

| Mode | P_elec (planning) | Duration |
|------|-------------------|----------|
| IDLE | <0.5 W | Continuous |
| ALIGN | 1–5 W (LSO set) | Seconds |
| PULSE peak | ~20–25 W | ≤3 s burst |
| PULSE avg @ 10% duty | ~2–3 W | 60 s window |

**Input:** 18–26 V DC compatible with `interface_spec.md`.

---

## MCU pulse controller (logical)

| Pin / signal | Function |
|--------------|----------|
| ENABLE_OUT | Driver TTL; default low |
| KEY_IN | Key switch sense |
| INTERLOCK_IN | Door loop; active = closed |
| ESTOP_IN | Active = fault |
| TEMP_ADC | Heat sink NTC |
| TARGET_LOCK_IN | Host or bench toggle |
| FIRE_IN | Momentary; gated |
| FAULT_OUT | Latched over-temp / fault |

See [`../firmware/pulse_controller_design.md`](../firmware/pulse_controller_design.md).

---

## EMI notes (R-EMI-001)

- Twisted pair for driver current paths; star ground at driver return.
- Shield SMA fiber path separately from switcher noise.
- **Not validated** on host avionics.

---

## Recommended next actions

1. Select commercial laser driver with documented interlock inputs.
2. Capture schematic in CAD when driver SKU fixed.

## Open questions / gaps

- Driver SKU not selected (L-02).
