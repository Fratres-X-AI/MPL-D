# Mitigation Execution Log — MPL-D

**Document ID:** MPL-D-MEL-001  
**Purpose:** Track **execution** of risk mitigations — distinct from mitigation options listed in [`RISK_REGISTER.md`](RISK_REGISTER.md).

**Rule:** Status **Complete** only when evidence column contains file path, PO number, or signed record.

---

## Execution log

| Risk ID | Planned mitigation | Owner role | Execution status | Evidence | Residual after mitigation |
|---------|-------------------|------------|------------------|----------|---------------------------|
| R-VIB-001 | Elastomer mount + T-05 vibe table | Mechanical Lead | **Not started** | — | **High** until T-05 |
| R-THM-001 | Pulsed duty + sink/fan + T-04 soak | Thermal Lead | **Partial** — spec only | pulse_control_spec | **Medium** |
| R-ATM-001 | Document σ bounds; indoor Phase 0 only | Systems Engineer | **Partial** — docs only | ATMOSPHERIC_AND_TRACKING_ASSESSMENT | **High** outdoors |
| R-EYE-001 | NHZ + interlocks + eyewear + LSO | **LSO (UNASSIGNED)** | **Not started** | NHZ worksheet unsigned | **High** |
| R-ROE-001 | Defensive CONOPS + legal review | Program Legal | **Partial** — CONOPS only | ROE_PROTOCOL_IV | **Medium** |
| R-EXP-001 | Compliance review + access control | Compliance Officer | **Partial** — screening doc | EXPORT_CONTROL_SCREENING | **Medium** |
| R-EFF-001 | Three-class surrogate T-03 | Test Lead | **Not started** | — | **High** |
| R-PWR-001 | Duty cap + T-04 bus measurement | Systems + Host | **Partial** — spec only | — | **Medium** |
| R-SUP-001 | Order DOE early or alternate array | Procurement | **Not started** | — | **Medium** |
| R-TRK-001 | Accept static pattern Phase 0 OR Phase 1 track | Program Lead | **Partial** — waiver implicit in scope | ROADMAP exclusions | **High** Phase 0 |
| R-EMI-001 | Shielding/filter Phase 1 | EE Lead | **Not started** | — | **L–M** |
| R-DOE-001 | Zero-order dump + measure | Optics + LSO | **Partial** — design only | zero_order_checklist unsigned | **Medium** |
| R-DAT-001 | Independent doc review | Tech Lead | **Partial** — military handoff pass | git 0b7fcc3+ | **Medium** |
| R-INT-001 | Host vendor ICD | Integration Lead | **Not started** | — | **Medium** |
| R-REG-001 | Phase 0 indoor scope only | LSO + Legal | **Partial** — scope documented | GATE_CLOSURE_PLAN | **Low** if obeyed |

---

## Owner roster (assign names when staffed)

| Role | Assigned name | Contact |
|------|---------------|---------|
| Program Lead | **TBD** | — |
| LSO | **UNASSIGNED** | — |
| Test Lead | **TBD** | — |
| Compliance Officer | **TBD** | — |
| Procurement Lead | **TBD** | — |
| Systems Engineer | **TBD** | — |

---

## Update protocol

After each mitigation step, update Execution status and Evidence. Mirror changes to [`RISK_REGISTER.md`](RISK_REGISTER.md) residual columns.

---

## Next required actions

1. Program Lead fills Owner roster with names.  
2. LSO begins R-EYE-001 execution (NHZ worksheet).  
3. Test Lead prepares `tests/logs/` folders before first session.
