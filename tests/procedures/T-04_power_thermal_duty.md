# T-04 Power and Thermal Duty — Detailed Procedure

**Maturity:** Preliminary Design — not executed.

**Links:** REQ-F-006, REQ-S-004, REQ-E-001, R-THM-001

---

## Setup

- Current probe or inline meter on driver input.
- Thermocouple on heat sink.
- Run `analysis/thermal_pulse_model.py` before test for planning bounds only.

## Duty scenarios

| Scenario | Pulse | Cooldown | Bursts |
|----------|-------|----------|--------|
| A | 0.5 s | 5 s | 6 |
| B | 1.0 s | 5 s | 6 |
| C | 0.5 s | 2 s | 10 (LSO approval required) |

## Record

Time series: t, I_A, V_V, P_W, T_C — CSV.

## Pass

No runaway T > LSO limit in 10 min; document equilibrium.

Update `thermal_pulse_model.py` R_th, C_th from soak if possible.
