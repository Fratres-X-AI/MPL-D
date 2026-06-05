# Rules of Engagement and Protocol IV Considerations

**Document ID:** MPL-D-ROE-001  
**Maturity:** Preliminary Design — policy framing only. **No legal review completed. No government determination obtained.**

**Evidence / analysis status:** Defensive CONOPS documented in [`CONOPS.md`](CONOPS.md). Treaty text referenced at high level only — program legal counsel must apply current law and policy.

**Known gaps:** No JAG/legal memo; no Protocol IV national implementation review; no field employment authorization.

**Next required action:** Legal review before any operational discussion outside research context.

---

## 1. Intended employment (defensive framing only)

| Parameter | Statement | Maturity |
|-----------|-----------|----------|
| Target | Hostile UAS **electro-optical sensors** | Preliminary Design (CONOPS) |
| Mechanism | Temporary dazzle, saturation, image degradation | **Unvalidated** effectiveness |
| Explicitly excluded | Deliberate permanent blinding of human vision | Program constraint C-NK-01 / REQ-F-002 |
| Explicitly excluded | Hard-kill burn-through of airframe or personnel | Program constraint |
| Host role | Defensive counter-UAS sensor denial | CONOPS |

This is **not** authorization to employ any laser against any target. It is design intent documentation for a research prototype.

---

## 2. Reversible vs permanent effects (design intent)

| Effect class | Design intent | Evidence |
|--------------|---------------|----------|
| EO sensor saturation / temporary bloom | **In scope** — primary CONOPS | Surrogate test T-03 **not executed** |
| Temporary loss of usable video for closed-loop UAS guidance | **Possible** — not proven | R-EFF-001 open |
| Permanent sensor damage (burn-through) | **Out of scope** — not design goal | Power tier bounded below industrial burn-through |
| Permanent human eye injury | **Unacceptable collateral** — controlled via NHZ, ROE, training | NHZ **not completed** (R-EYE-001) |

**Blunt statement:** Low-power dazzle can still cause **permanent eye injury** if NHZ discipline fails. Reversible sensor effects are **not guaranteed** even when eye safety is maintained.

---

## 3. Protocol IV to the CCW (Blinding Laser Weapons)

Protocol IV prohibits laser weapons specifically designed to cause **permanent blindness** to unenhanced vision.

| Question | Program position | Status |
|----------|------------------|--------|
| Is MPL-D designed as a blinding weapon against humans? | **No** — sensor denial on UAS EO | Design intent documented |
| Can human exposure occur? | **Yes** — diverging beams, platform dynamics, specular paths | R-EYE-001, R-ROE-001 |
| Is Protocol IV compliance resolved? | **No** — employment parameters and national implementation not reviewed | Legal review **required** |

Classification as prohibited blinding weapon is **employment- and parameter-dependent**. Preliminary Design documentation does **not** resolve this.

**Risk:** R-ROE-001. **Mitigation status:** CONOPS defensive framing, pulse limits, sensor-only targeting language — **not verified by legal review**. **Residual risk:** Medium.

---

## 4. ROE constraints (research / bench)

| Rule | Phase 0 | Phase 1+ (if authorized) |
|------|---------|---------------------------|
| Personnel in NHZ during emission | **Prohibited** (once NHZ defined) | Same |
| Outdoor emission | **Prohibited** without separate authorization | Regulatory + aviation review |
| Flight test | **Prohibited** Phase 0 | Separate program gate |
| Target | Surrogate cameras only Phase 0 | Hostile UAS sensors only if separately authorized |
| Pulse duration | LSO-capped in SOP | ROE-specific cap TBD |

Cross-reference: REQ-R-001, REQ-R-002, [`LASER_SAFETY_PLAN.md`](LASER_SAFETY_PLAN.md).

---

## 5. Traceability

| Requirement | This document |
|-------------|---------------|
| REQ-R-001 | §1–3 |
| REQ-R-002 | §2, §4 |
| REQ-F-002 | §2 |

**Related risks:** R-ROE-001, R-EYE-001, R-REG-001.

---

## 6. Next required actions

1. Program legal counsel review of CONOPS + safety case before government briefing.
2. Document national Protocol IV implementation assumptions if briefing international partners.
3. Do not represent this package as ROE-approved or employment-cleared.
