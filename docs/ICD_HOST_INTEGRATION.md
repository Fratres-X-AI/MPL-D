# Interface Control Document (ICD) — Host Platform Integration

**Document ID:** MPL-D-ICD-001  
**Maturity:** Preliminary Design — interface definition stub. **No ICD baseline released; no joint test with host vendor.**

**Evidence / analysis status:** Parameters aligned with [`../hardware/interface_spec.md`](../hardware/interface_spec.md) and 940 nm candidate. No measured interface data.

**Known gaps:** Drone-X hardpoint drawing, connector standard, power tap location, and EMI test data absent (R-INT-001).

**Next required action:** Obtain host vendor ICD inputs; issue ICD Rev A after mutual review.

---

## 1. Scope

Defines mechanical, electrical, thermal, optical boresight, and logical control interfaces between the MPL-D payload module and a host UAV. **Primary reference host:** Drone-X (10 kg payload program baseline).

This ICD does **not** authorize flight integration or field employment.

---

## 2. Interface summary

| Interface | ICD section | Status | Verification (planned) |
|-----------|-------------|--------|------------------------|
| Mechanical mount | §3 | Defined (planning) | Inspection; Phase 1 fit check |
| Electrical power | §4 | Defined (planning) | T-04; bus sag test Phase 1 |
| Thermal | §5 | Defined (planning) | T-04 soak |
| Optical boresight | §6 | Defined (planning) | T-01 alignment log |
| Control / data | §7 | Defined (planning) | T-04 interlock demo |
| EMI / EMC | §8 | **Not defined** | Phase 1 if authorized |

---

## 3. Mechanical interface (MPL-D-ICD-M-001)

| Parameter | Host requirement | Payload provision | Tolerance | Maturity |
|-----------|------------------|-------------------|-----------|----------|
| Mount pattern | **TBD — vendor drawing required** | 4-bolt plate or dual rail (planning) | ±0.5 mm hole pattern once frozen | Concept |
| Module mass | ≤10 kg payload budget | 0.7–3.0 kg planning | ±30% without CAD | Preliminary Design |
| Envelope | Host bay clearance TBD | 120×45×35 mm to 180×80×60 mm | See mechanical_bom | Preliminary Design |
| CG | Host stability limits TBD | Target <20 mm aft of mount plane | Unverified | Concept |
| Vibration isolation | Host spectrum TBD | 4× elastomer mounts | Effectiveness unvalidated (R-VIB-001) | Preliminary Design |

**Assumption:** A-HST-01. **Risk:** R-INT-001.

---

## 4. Electrical interface (MPL-D-ICD-E-001)

| Signal | Direction | Specification (planning) | Notes |
|--------|-----------|-------------------------|-------|
| V_BUS | Host → Payload | 18–26 V DC | Host must document source impedance |
| I_PEAK | Payload → Host | 20–30 W peak (~1.2 A @ 24 V planning) | At η_wp ≈ 0.40, 10 W optical |
| I_AVG | Payload → Host | 2–5 W avg @ 10% duty | pulse_control_spec |
| ENABLE | Host → Payload | Active-high after interlock chain | REQ-S-002 |
| ARM / PULSE | Host → Payload | Logic-level; pulse duration capped in firmware | REQ-I-002 |
| FAULT | Payload → Host | Open-collector OT; OT on over-temp | REQ-S-004 |
| GND | Common | Low-impedance return | Shielded harness required |

**Connector:** **TBD** (XT60, Anderson, or circular — host-dependent).

---

## 5. Thermal interface (MPL-D-ICD-T-001)

| Parameter | Host obligation | Payload obligation |
|-----------|-----------------|-------------------|
| Heat rejection path | Provide airflow or accept duty limit | Sink + optional 5–12 V fan |
| Dissipation (planning) | — | 10–35 W peak module heat |
| Ambient | Document operating band | Derating above 35 °C **unquantified** |

---

## 6. Optical / pointing interface (MPL-D-ICD-O-001)

| Parameter | Value (planning) | Verification |
|-----------|------------------|--------------|
| Boresight vs host body axis | Coarse aligned at install; ±1–3° | T-01 |
| Field of regard | Fixed forward ±15° mechanical | Install procedure |
| Pattern | Static multi-spot; no gimbal Phase 0 | T-01 |

---

## 7. Control / data interface (MPL-D-ICD-C-001)

| Message | Payload response | Safety |
|---------|------------------|--------|
| SAFE (default) | Emitters off | Power-up state |
| ARM | Interlock armed; no emission | Requires ENABLE |
| DAZZLE_PULSE(t) | Emission ≤ t_max (LSO/SOP) | Rearm required |
| STATUS | Temp, faults, state | Telemetry only |

Transport: UART or CAN — **host selects**. Protocol ICD Rev A pending.

---

## 8. EMI / EMC (MPL-D-ICD-EM-001)

**Status:** **Not defined.** **Risk:** R-EMI-001. Planned Phase 1 activity if program continues.

---

## 9. ICD traceability

| Requirement | ICD section |
|-------------|-------------|
| REQ-I-001 | §4 |
| REQ-I-002 | §7 |
| REQ-I-003 | §3 |
| REQ-S-002 | §4, §7 |
| REQ-F-003 | §3, §6 |

**Related:** [`ASSUMPTIONS_AND_CONSTRAINTS.md`](ASSUMPTIONS_AND_CONSTRAINTS.md) · [`../hardware/electrical_architecture.md`](../hardware/electrical_architecture.md)
