# Concept of Operations — Counter-UAS Multi-Point Laser Dazzler Prototype (MPL-D)

**Maturity:** Preliminary Design — CONOPS documented for defensive bench and future host-mounted employment. **No field employment authorized.**

**Scope:** Drone-on-drone defensive sensor denial. Non-kinetic. No hard-kill. No anti-personnel use.

---

## 1. Mission

Degrade, overwhelm, or temporarily blind hostile UAS electro-optical sensors using a multi-point NIR laser pattern from a host platform (centerline mount, no gimbal in Phase 0–1 baseline).

**Success (Phase 0):** Demonstrate pattern generation and surrogate sensor degradation on bench — **not** operational kill chain.

---

## 2. Employment geometry (planning)

```
Host VTOL ──► coarse point at target ──► static multi-spot pattern ──► target EO aperture
     ▲                                              │
     └── host maintains LOS; no closed-loop dazzle track in Phase 0
```

| Parameter | Planning value |
|-----------|----------------|
| Engagement type | Drone-on-drone, defensive |
| Pointing | Host airframe boresight + pattern width |
| Range (planning envelope) | Bench 1–10 m Phase 0; outdoor **not authorized** in Phase 0 |
| Pulse | 0.1–3 s burst; ≤10% duty / 60 s until thermal data revises |

---

## 3. Rules of engagement (research / bench)

1. Surrogate cameras and calibrated sensors only in Phase 0.
2. No deliberate exposure of personnel; NHZ controls per safety case.
3. No outdoor or flight emission without separate legal and LSO authorization.
4. Protocol IV defensive sensor-denial framing — not blinding weapons employment.

---

## 4. Host platform (future)

| Host | Role | Status |
|------|------|--------|
| Solace-class VTOL | Centerline under-fuselage mount | Payload limit **unverified** |
| Small tactical UAS | Limited duty-cycle dazzle | Mass/power constrained |
| 18 in / <3.5 kg rocket (user reference) | Separate air-launched concept | **Not integrated in MPL-D CAD** |

---

## 5. Kill chain (sensor denial — not kinetic)

| Step | Phase 0 | Phase 1+ |
|------|---------|----------|
| Detect target | External to payload | Host sensor fusion |
| Track / lock | Manual / host-level | Host cue TARGET_LOCK |
| Arm payload | SAFE → ARM | Same + interlocks |
| Dazzle pulse | Bench T-03 | PULSE on lock |
| Assess effect | Image review | **Unvalidated** vs threat |

---

## Recommended next actions

1. Align CONOPS with signed safety case before any full-power test.
2. Revisit range and duty assumptions after T-02/T-04 data.

## Open questions / gaps

- Operational range never certified at any phase without measured data.
- AI-assisted target cueing not specified.
