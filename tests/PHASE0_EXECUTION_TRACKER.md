# Phase 0 Test Execution Tracker

**Document ID:** MPL-D-TST-TRK-001  
**TDP baseline:** tdp-baseline-0.1  
**Overall status:** **NOT STARTED — G-ENR BLOCKED**

**Rule:** Do not mark PASS without log folder path and LSO session authorization reference.

---

## Test matrix

| Test | Procedure | Requirements | Status | Date | Operator | Log path | LSO session auth | Result |
|------|-----------|--------------|--------|------|----------|----------|------------------|--------|
| T-01 | [T-01_pattern_formation.md](procedures/T-01_pattern_formation.md) | REQ-F-001, F-005, S-003 | **NOT EXECUTED** | — | — | — | — | — |
| T-02 | [T-02_irradiance_vs_range.md](procedures/T-02_irradiance_vs_range.md) | REQ-F-004, P-001, E-003 | **NOT EXECUTED** | — | — | — | — | — |
| T-03 | [T-03_surrogate_dazzle.md](procedures/T-03_surrogate_dazzle.md) | REQ-F-002, P-002 | **NOT EXECUTED** | — | — | — | — | — |
| T-04 | [T-04_power_thermal_duty.md](procedures/T-04_power_thermal_duty.md) | REQ-E-001, S-004, O-001 | **NOT EXECUTED** | — | — | — | — | — |
| T-05 | [T-05_vibration_wander.md](procedures/T-05_vibration_wander.md) | REQ-E-002 | **NOT EXECUTED** | — | — | — | — | — |

---

## RTM verification summary

| Metric | Value |
|--------|-------|
| Requirements with test-linked verification | 22 |
| Tests executed | **0 / 5** |
| Requirements with recorded PASS | **0 / 22** |

Update [`../docs/REQUIREMENTS_TRACEABILITY.md`](../docs/REQUIREMENTS_TRACEABILITY.md) only when log paths exist.

---

## Prerequisites (all must be true before T-01)

- [ ] G-SAF-01 LSO assigned  
- [ ] G-SAF-02 NHZ worksheet signed  
- [ ] G-SAF-03 SOP approved  
- [ ] G-HW-P0 minimum: I-01, interlock, S-03, S-04 received  
- [ ] G-ENR ALIGN-power authorization documented in `logs/admin/`  

---

## Log directory convention

```
tests/logs/
  admin/          # G-ENR auths, LSO session approvals
  T-01/           # Pattern photos, irradiance map
  T-02/           # Range vs meter CSV
  T-03/           # Surrogate images per sensor class
  T-04/           # Thermal + electrical CSV
  T-05/           # Vibration displacement data
```

---

## Next required action

Close Block A–C in [`../docs/GATE_CLOSURE_PLAN.md`](../docs/GATE_CLOSURE_PLAN.md), then schedule T-01 at ALIGN power.
