# Configuration Management Plan — MPL-D

**Document ID:** MPL-D-CM-001 Rev A  
**Maturity:** **Released** — formal CM plan for documentation baseline `tdp-baseline-0.1`. Hardware CM activates at G-HW-P0.

**Registry:** [`TDP_BASELINE_REGISTRY.md`](TDP_BASELINE_REGISTRY.md)

---

## 1. Scope

Configuration control for:

- Technical documentation (TDP)  
- Requirements and RTM  
- Analysis scripts (version = git commit)  
- Test procedures and **executed logs** under `tests/logs/`  
- Hardware specifications (serial/lot when procured)

---

## 2. Roles

| Role | CM responsibility |
|------|-------------------|
| Program Lead | Baseline release authority; ECO approval |
| Systems Engineer | RTM sync; assumption register |
| Test Lead | Test log integrity; PHASE0_EXECUTION_TRACKER |
| LSO | Safety-impacting ECO veto |
| Compliance Officer | Export-controlled artifact control |

---

## 3. Version control scheme

| Item | Scheme |
|------|--------|
| Documentation | Semantic TDP baseline tags on git (`tdp-baseline-x.y`) |
| Document revisions | Git commit hash; major docs carry Document ID + Rev in header |
| Analysis scripts | Commit hash recorded in every test log |
| Test evidence | Folder per test ID; immutable after sign-off (new run = new subfolder) |
| Hardware | Serial/lot in procurement_status + test logs when received |

**Branch policy:** `main` is controlled; changes via commit with factual message; no force-push without Program Lead approval.

---

## 4. Baseline release process

1. Verify gate criteria for target baseline ([`TDP_BASELINE_REGISTRY.md`](TDP_BASELINE_REGISTRY.md)).  
2. Program Lead approves release memo (commit message or `docs/cm/releases/` note).  
3. Apply annotated git tag: `git tag -a tdp-baseline-x.y -m "..."`.  
4. Update registry table with date, commit hash, validation level.  
5. Notify reviewers via [`HANDOFF_READINESS.md`](HANDOFF_READINESS.md) update.

### Released baselines

| Tag | Commit | Validation | Status |
|-----|--------|------------|--------|
| `tdp-baseline-0.1` | (see registry) | Documentation only | **RELEASED** |

---

## 5. Engineering Change Order (ECO)

| ECO type | Required approvals | Records |
|----------|-------------------|---------|
| Doc / req change | Systems Engineer + Program Lead | Git commit; RTM row update |
| Safety impact | + LSO | MITIGATION_EXECUTION_LOG |
| Analysis model | Analyst + Systems Engineer | ANALYSIS_VALIDATION_STATUS |
| ICD / interface | Integration Lead + Host vendor | ICD rev letter |
| Hardware config | EE/ME leads + Program Lead | procurement_status |

**ECO ID format:** `ECO-YYYYMMDD-###` in commit body until formal tool adopted.

---

## 6. Test log CM

- Executed tests **shall not** overwrite prior logs — use dated subfolders e.g. `T-01/2026-06-15_run1/`.  
- `PHASE0_EXECUTION_TRACKER.md` is the master index — only Test Lead updates PASS/FAIL.  
- RTM evidence column updated only when tracker shows PASS with log path.

---

## 7. Analysis outputs

`analysis/*.csv` and `analysis/*.png` remain gitignored. Canonical analysis tied to tests lives in `tests/logs/` with script commit hash.

---

## 8. Excluded from baseline tdp-baseline-0.1 validation

- All content under `tests/logs/` except structure/README  
- Any fabricated or synthetic test data  
- Archived drone hero assets (reference only)

---

## 9. Next baseline targets

| Tag | Gate to close |
|-----|---------------|
| tdp-baseline-0.2 | G-SAF-01/02/03 |
| tdp-baseline-1.0 | Phase 0 exit per ROADMAP |
