# Export Control Determination Workflow — MPL-D

**Document ID:** MPL-D-EXP-WF-001  
**Status:** **NO DETERMINATION OBTAINED.** Screening only.

**Parent:** [`EXPORT_CONTROL_SCREENING.md`](EXPORT_CONTROL_SCREENING.md) · **Risk:** R-EXP-001

---

## 1. Current determination record

| Field | Value |
|-------|-------|
| ITAR jurisdiction | **Undetermined — no ruling** |
| EAR jurisdiction | **Undetermined — no ruling** |
| ECCN | **Not assigned** |
| Commodity jurisdiction (CJ) request filed | **No** |
| Compliance officer review completed | **No** |
| Effective date of determination | — |
| Next review trigger | First laser module PO; foreign partner access; integration drawing release |

**Operational rule:** **HOLD** on international shipment and foreign-person technical disclosure until written memo exists.

---

## 2. Workflow steps

| Step | Action | Owner | Output artifact |
|------|--------|-------|-----------------|
| 1 | Package technical description (config in screening doc + CONOPS) | Systems Engineer | Screening packet |
| 2 | Identify end-use, end-user, destination | Program Lead | End-use statement |
| 3 | Compliance officer review | Compliance Officer | Memo: HOLD / RELEASE / LICENSE REQUIRED |
| 4 | If HOLD: document restrictions (repo access, vendor country, travel) | Compliance Officer | Access policy update |
| 5 | Vendor ECCN / CoO on PO | Procurement | procurement_status note |
| 6 | Re-screen on config change (power, λ, integration data) | Systems Engineer | Revised EXP-001 rev |

---

## 3. Triggers requiring re-screen

- Optical power class increase above 10 W CW rated  
- Release of host hardpoint CAD to foreign party  
- Foreign national access to repo or lab  
- Change from bench to flight integration  
- Dual-wavelength or classified performance data added  

---

## 4. Repository disclosure stance

MIT LICENSE on documentation **does not** override export law. Directed-energy sensor-denial content may be controlled when combined with hardware or performance validation data.

---

## 5. Next required action

Compliance Officer completes Step 3 and files memo reference in EXPORT_CONTROL_SCREENING §3 determination record — **even if outcome remains HOLD**.
