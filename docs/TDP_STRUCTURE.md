# Technical Data Package (TDP) Structure — MPL-D

**Maturity:** Preliminary Design — **recommended TDP tree for formal government handoff.** Most items exist as drafts or outlines; **none constitute a released TDP baseline.**

**Evidence / analysis status:** Current repo content mapped below. Gaps flagged per item.

**Next required action:** Assign TDP custodian; issue TDP Baseline 0.1 after LSO assignment and ICD Rev A.

---

## 1. Purpose

Suggested document tree aligned with common DoD/contractor technical data package expectations for a research prototype handoff. This is a **structure guide**, not a delivery commitment.

---

## 2. TDP document tree

```
MPL-D-TDP/
├── 00_ADMIN/
│   ├── README.md                          [Done — executive summary]
│   ├── GOVERNMENT_REVIEW_GUIDE.md         [Done]
│   ├── CONFIGURATION_MANAGEMENT.md        [Done]
│   ├── DATA_RIGHTS.md                     [Done]
│   ├── NOTICE                                 [Done]
│   └── phase0_gate_status.md              [Done]
├── 01_SYSTEM/
│   ├── ARCHITECTURE.md                    [Done — Preliminary Design]
│   ├── CONOPS.md                          [Done]
│   ├── ASSUMPTIONS_AND_CONSTRAINTS.md     [Done]
│   ├── ICD_HOST_INTEGRATION.md            [Done — stub]
│   └── interface_spec.md (hardware/)      [Done — merge to ICD Rev A]
├── 02_REQUIREMENTS/
│   ├── REQUIREMENTS.md                    [Done]
│   └── REQUIREMENTS_TRACEABILITY.md       [Done — elevated RTM]
├── 03_DESIGN/
│   ├── preliminary_optical_layout.md      [Done — paper]
│   ├── electrical_architecture.md         [Done — paper]
│   ├── mechanical_bom.md                  [Done — paper]
│   ├── pulse_control_spec.md              [Done]
│   └── pulse_controller_design.md (fw/)   [Done — design only]
├── 04_ANALYSIS/
│   ├── PHYSICS_BASIS.md                   [Done]
│   ├── ANALYSIS_VALIDATION_STATUS.md      [Done]
│   ├── nir_940nm_link_budget_notes.md     [Done — unvalidated]
│   ├── power_thermal_budget.py            [Done — script]
│   ├── thermal_pulse_model.py             [Done — script]
│   └── vibration_wander_model.py          [Done — script]
├── 05_VERIFICATION/
│   ├── phase0_test_plan_outline.md        [Done]
│   ├── procedures/T-01 … T-05           [Done — procedures only]
│   ├── phase0_bench_sop_draft.md          [Done — unsigned]
│   └── templates/test_record_template.md  [Done]
├── 06_SAFETY_COMPLIANCE/
│   ├── LASER_SAFETY_PLAN.md               [Done — outline]
│   ├── phase0_safety_case_draft.md        [Done — unsigned]
│   ├── lso_assignment_record.md           [Still Weak — template only]
│   ├── ROE_PROTOCOL_IV.md                 [Done]
│   ├── EXPORT_CONTROL_SCREENING.md        [Done — no ruling]
│   └── zero_order_inspection_checklist.md [Done — not executed]
├── 07_RISK/
│   └── RISK_REGISTER.md                   [Done — elevated]
├── 08_PROGRAM/
│   ├── ROADMAP.md                         [Done — Ph 0/1/2]
│   ├── PROTOTYPE_HANDOFF.md               [Done]
│   └── procurement_status.md (hardware/) [Still Weak — open orders]
└── 09_VISUALS/
    ├── hero-laser-dazzler-emitter-schematic.*  [Done — non-operational]
    └── LaserDazzlerHero.tsx (components/)      [Done — schematic only]
```

---

## 3. TDP completeness assessment

| TDP section | Status | Gap |
|-------------|--------|-----|
| 00 Admin | **Done** (docs) | Baseline **tdp-baseline-0.1 released** — see TDP_BASELINE_REGISTRY |
| 01 System | **Still Weak** | ICD host drawings missing |
| 02 Requirements | **Done** (trace forward) | Zero verification evidence |
| 03 Design | **Still Weak** | No CAD, no released drawings |
| 04 Analysis | **Still Weak** | All models unvalidated |
| 05 Verification | **Still Weak** | No test records executed |
| 06 Safety | **Still Weak** | LSO/NHZ open |
| 07 Risk | **Done** (structure) | Residual ratings qualitative |
| 08 Program | **Done** (plan) | Phase 1/2 not authorized |
| 09 Visuals | **Done** | Schematic only — correct |

---

## 4. Recommended TDP baseline release criteria

1. G-SAF-01/02/03 **PASS** (LSO + NHZ + SOP).
2. ICD Rev A mutual sign-off with host vendor (or documented host waiver).
3. T-01–T-05 records archived with configuration ID.
4. RTM updated with pass/fail evidence links.
5. Export control determination documented (even if "hold").

**Current TDP releasable to government for *document review*:** Yes, with caveats in [`GOVERNMENT_REVIEW_GUIDE.md`](GOVERNMENT_REVIEW_GUIDE.md).

**Current TDP releasable as *validated capability data*:** **No.**
