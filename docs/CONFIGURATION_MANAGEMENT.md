# Configuration Management and Version Control

**Document ID:** MPL-D-CM-001  
**Maturity:** Preliminary Design — process note for repository-based configuration control.

**Evidence / analysis status:** Git version history on GitHub (`Fratres-X-AI/MPL-D`). No formal CM board established.

**Known gaps:** No released baseline tag; analysis outputs not pinned to hardware serial numbers; no ECO workflow.

**Next required action:** Tag `tdp-baseline-0.1` after first LSO-signed safety package.

---

## 1. Configuration items (CIs)

| CI | Location | Baseline authority |
|----|----------|-------------------|
| Documentation package | `/docs`, `/README.md` | Program lead + tech lead |
| Requirements | `docs/REQUIREMENTS.md`, RTM | Systems engineer |
| Analysis scripts | `/analysis/*.py` | Analyst; commit hash = run ID |
| Hardware specs | `/hardware/` | Mechanical/electrical leads |
| Test procedures | `/tests/` | Test lead + LSO for safety |
| Firmware design | `/firmware/` | Embedded lead |

---

## 2. Version control

- **Tool:** Git; default branch `main`.
- **Commit policy:** Atomic commits with factual messages; no force-push to `main` without program lead approval.
- **Analysis reproducibility:** Test records shall cite `git rev-parse HEAD` and script path.
- **Secrets:** Never commit `.env`, credentials, or export-controlled attachments without clearance — see `.gitignore`.

---

## 3. Change control (lightweight ECO)

| Change type | Required action |
|-------------|-----------------|
| Assumption change | Update `ASSUMPTIONS_AND_CONSTRAINTS.md`, RTM, affected risks |
| Requirement change | Update REQUIREMENTS.md, RTM, gate impact assessment |
| Safety-impacting change | LSO review before merge |
| Analysis model change | Update `ANALYSIS_VALIDATION_STATUS.md`; re-run affected tests when hardware exists |
| ICD change | Rev letter increment; notify host interface owner |

**ECO record:** Git commit + PR description until formal tool adopted.

---

## 4. Baseline tagging (planned)

| Tag | Criteria | Status |
|-----|----------|--------|
| `tdp-baseline-0.1` | G-DOC + G-PROTO pass (current) | **Eligible now** — tag optional |
| `tdp-baseline-0.2` | G-SAF-01/02/03 pass | **Not met** |
| `tdp-baseline-1.0` | Phase 0 exit + test records | **Not met** |

---

## 5. Analysis artifact control

Generated outputs (`analysis/*.csv`, `analysis/*.png`) are **gitignored**. Canonical results shall be stored in controlled test logs under `tests/logs/` when created, with reference to input commit and parameter file.

---

## 6. Visual / hero assets

Schematic hero assets are **non-operational** configuration items. Drone/airframe renders in `/assets` are **archived reference only** — not baseline for external TDP release (C-VIS-01).
