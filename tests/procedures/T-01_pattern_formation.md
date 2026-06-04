# T-01 Pattern Formation — Detailed Procedure

**Maturity:** Preliminary Design — executable when G-ENR open. **Not executed.**

**Links:** REQ-F-001, REQ-F-005, REQ-S-003, R-DOE-001

---

## Setup

1. Complete SOP pre-session checklist.
2. ALIGN mode only until LSO authorizes full power for this test.
3. Target: white paper or beam profiler at 2.0 m ±0.05 m.

## Steps

| Step | Action | Record |
|------|--------|--------|
| 1 | SAFE → ALIGN; verify zero-order in dump | Photo dump spot |
| 2 | Expose pattern at 2 m | Photo full pattern |
| 3 | Count spot centers | N_spots |
| 4 | Measure spot spacing (mm on target) | Grid table |
| 5 | Relative power per spot (profiler or meter scan) | CSV |
| 6 | Return SAFE | Timestamp |

## Pass (Phase 0)

- N_spots matches DOE design intent within ±1 spot.
- Zero-order contained in dump at alignment and authorized power.

## Fail actions

- Realign collimator–DOE; re-inspect dump; do not increase power.

## Data file

`tests/logs/T-01_YYYYMMDD_pattern.csv` — use template fields in `tests/templates/test_record_template.md`.
