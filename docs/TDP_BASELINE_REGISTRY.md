# TDP Baseline Registry — MPL-D

**Document ID:** MPL-D-TDP-REG-001  
**Authority:** [`CONFIGURATION_MANAGEMENT.md`](CONFIGURATION_MANAGEMENT.md)

---

## Released baselines

| Baseline tag | Git tag | Release date | Criteria met | Validation level | Notes |
|--------------|---------|--------------|--------------|------------------|-------|
| **tdp-baseline-0.1** | `tdp-baseline-0.1` | 2026-06-04 | G-DOC PASS, G-PROTO PASS, military handoff doc structure | **Documentation only — zero test validation** | Suitable for **concept review** — not validated TDP |
| tdp-baseline-0.2 | — | — | G-SAF-01/02/03 PASS | — | **Not released** |
| tdp-baseline-1.0 | — | — | Phase 0 exit + RTM evidence | — | **Not released** |

---

## tdp-baseline-0.1 contents (summary)

- Full TDP tree per [`TDP_STRUCTURE.md`](TDP_STRUCTURE.md)  
- RTM, risk register, safety/export/ROE outlines  
- Gate closure plan, gap tracker, execution trackers (empty logs)  
- **Excluded from validation claims:** all `tests/logs/` (no executed data)

---

## Baseline identification in test records

When tests execute, each record **must** cite:

```
TDP baseline: tdp-baseline-0.1 (or later)
Git commit: <hash>
Configuration: <hardware serial / DOE lot if applicable>
```

---

## Supersession

New baseline tag supersedes prior for external reference. Do not re-tag retroactively after test data — issue new baseline number.

---

## Handoff statement for reviewers

**tdp-baseline-0.1** is a **released documentation configuration** — not evidence of system validation. See [`HANDOFF_READINESS.md`](HANDOFF_READINESS.md).
