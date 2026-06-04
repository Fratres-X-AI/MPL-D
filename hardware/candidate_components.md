# Candidate Components — NIR Fiber-Coupled Dazzler Path

**Project:** Counter-UAS Multi-Point Laser Dazzler Prototype  
**Maturity:** Preliminary Design — vendor-published datasheet parameters captured for trade study. **No parts procured, no independent verification, no integration test data.**

**Scope:** Defensive non-kinetic sensor denial only. Hard-kill / permanent sensor damage modes referenced in vendor marketing are **explicitly out of scope** for this program.

---

## 1. Purpose

Document real, commercially available components surfaced for a compact NIR dazzler concept (915–940 nm, fiber-coupled, pulsed operation, centerline host mount). All performance claims from suppliers, papers, or informal briefs require independent validation before design commitment.

---

## 2. Primary laser candidate (not down-selected)

### AeroDiode 940 nm 10 W Model 2 (fiber-coupled multimode)

**Source:** Vendor-published datasheet (AeroDiode). Parameters below are **typical/nominal from vendor** unless marked; this repository has not verified them on received hardware.

| Parameter | Vendor-stated value | Planning uncertainty |
|-----------|---------------------|----------------------|
| Output power (CW rating) | 10 W | ±10–20% unit-to-unit; derating above 55 °C case |
| Center wavelength | 940 nm (typ), 935–945 nm range | 0.3 nm/°C thermal shift (vendor) |
| Spectral width (FWHM) | 3 nm (typ) | Bandpass filter interaction on sensors **unmodeled** |
| Fiber | 105 µm core / 125 µm clad, NA 0.22, SMA905 | Multimode — **not** diffraction-limited beam quality |
| Electrical (typ) | 11.5 A @ 1.7 V (~19.6 W electrical) | Max 13 A @ 1.8 V (~23.4 W) |
| Conversion efficiency (typ) | ~50% | Treat as **upper vendor tier**; budget η_wp 0.35–0.50 for analysis |
| Package | 17 × 11.8 × 7.7 mm | Diode only — excludes driver, fiber strain relief, heatsink |
| Operating temp | 15–55 °C | Below 15 °C or above 55 °C requires derating or prohibited operation |
| Back-reflection isolation | 30 dB typ (1020–1200 nm band) | Does not eliminate all feedback paths in integrated stack |

**915 nm variant:** Vendor offers similar 915 nm 10 W class modules (BWT, QPhotonics, AeroDiode). Trade vs 940 nm is sensor-filter dependent — **not resolved** without surrogate testing (see `docs/ARCHITECTURE.md` Phase 0 Minimum Surrogate Sensor Set).

**Price (order of magnitude, public listings):** ~€345–600 diode/module tier — excludes driver, optics, DOE, integration labor. Not a program cost estimate.

**Gap vs MPL-D multi-point architecture:** This part is a **single** fiber output. A static DOE or multi-emitter pattern still required downstream. Splitting 10 W across N beamlets reduces per-beamlet irradiance by ~N (plus DOE efficiency loss 60–85% class).

---

## 3. Collimation optics (candidate classes)

| Option | Description | Maturity | Notes |
|--------|-------------|----------|-------|
| AeroDiode COL010 (vendor matched) | High-power collimator cited for ~12 mm output beam diameter | Preliminary Design (vendor claim) | Must measure divergence and M² equivalent on bench — multimode fiber will **not** achieve diffraction-limited performance |
| COTS SMA905 aspheric collimators | AliExpress / generic, ~$25–50 class | Concept for prototype | Alignment and power handling **unverified** at 10 W |
| Thorlabs / Edmund adjustable fiber collimators | Higher quality, often smaller beam | Preliminary Design (component class) | May require beam expander for low divergence at range — adds mass and alignment |

**Blunt statement:** Collimation quality dominates irradiance at 1000 m more than nominal diode wattage. **No** engagement range at 1000 m is certified in this repository for any collimator option.

---

## 4. External benchmark systems (not MPL-D validation)

| System | Published envelope | Relevance | Limitation |
|--------|-------------------|-----------|------------|
| LUMIBIRD Dazzler module | ~100 × 40 × 30 mm, ~0.5 kg, 24 VDC (vendor/marketing) | SWaP reference for compact dazzler packaging | Wavelength, optics, pattern, and effectiveness **not** verified for this program; vendor also markets hard-damage variants — **out of scope** |
| EOS Laser Dazzler (RWS add-on) | Field-demonstrated C-UAS context (public reporting) | Shows deployed dazzler class exists | Performance parameters **not** disclosed at actionable level |
| Lyocon portable dazzler (NUBURU) | 1–10 W adjustable, 2.5–30 mrad divergence class (public reporting) | Divergence envelope reference | Not a drone-integrated multi-point MPL-D architecture |

These benchmarks prove compact dazzler **packaging is physically plausible**. They do **not** validate MPL-D effectiveness, range, or multi-point pattern approach.

---

## 5. Published literature (evidence class — not program test data)

| Reference | Claimed result (summary) | Applicability to MPL-D | Gap |
|-----------|-------------------------|------------------------|-----|
| Wu et al. (2024, MDPI) | Dazzle/blind effects at 600 m–1.2 km on miniature UAV detectors in reported setup | Supports **plausibility** of km-class effects at **unspecified** laser parameters in paper | Laser power, beam geometry, and sensor type in paper **≠** this 10 W 940 nm multi-point concept |
| Abdelhakim et al. (2024) | 1.06 µm effects on EO at multi-km in modeled/reported conditions | Shows EO vulnerability class exists at **high power** | **Not transferable** to 10 W 940 nm pulsed dazzler without separate analysis |
| Goyvaerts et al. (2024, SPIE) | Vulnerabilities in commercial drone cameras (lab/field) | Supports surrogate test rationale | Does not specify required irradiance for MPL-D stack |
| Kuantama et al. (2024) | 23.5 mW green at 5 m with tracker | Shows low power works at **short range** with precise aim | **Does not** extrapolate to 940 nm / 1000 m / static pattern |
| Grundmark (LiU, 2021) | Close-range dazzle with tracking | Tracking dependency | MPL-D Phase 0 has **no** closed-loop track-to-dazzle |

**Do not** use these papers to assert 1000 m dazzle success for the AeroDiode 10 W module. Use them only to justify Phase 0 bench investment.

---

## 6. Thermal — ram-air scoop concept

**Concept:** Forward-facing air scoop routing flight-relative airflow over aluminum heatsink bonded to diode/driver package.

**Maturity:** Concept. No CFD, no flight test, no measured thermal resistance.

| Factor | Planning assessment |
|--------|---------------------|
| Forward flight / fixed-wing cruise | Ram-air **may** provide adequate cooling for **pulsed** 10 W class if scoop and sink sized correctly — **unproven** |
| Hover / low airspeed (VTOL) | Mass flow drops; ram-air **may fail** without derating or alternate cooling — R-THM-001 |
| Pulsed duty cycle | Average heat ∝ duty × P_diss; short bursts reduce steady-state load — duty limits **TBD** by measurement |
| Altitude | Colder air increases convective benefit; lower density reduces mass flow — **net effect unmodeled** |

**Rejected assumption:** “Hundreds of watts air-cooled heatsink class” implies continuous industrial cooling — irrelevant unless duty cycle and airflow are measured on host.

---

## 7. Pulse timing and control (planning)

**Maturity:** Concept. No firmware, no interlock hardware, no sync interface to host targeting.

| Parameter | Planning range | Evidence |
|-----------|----------------|----------|
| Engagement burst | 0.1–3 s total (informal CONOPS input) | Industry practice class; **not** validated for MPL-D |
| Intra-burst structure | ms–µs pulse trains possible | May increase sensor confusion; driver bandwidth and eye-safety classification **TBD** by LSO |
| Cooldown | Required between bursts | Prevents thermal runaway; duration **TBD** from soak test |
| Trigger | On host “target acquired” signal | Requires defined electrical interface — see `interface_spec.md` |

**Hard gate:** No full-power pulsed bench work without completed IEC 60825-1 NHZ analysis (`docs/ARCHITECTURE.md`).

---

## 8. Host platform notes (Drone-X / centerline mount)

| Claim | Status in repository |
|-------|---------------------|
| Drone-X **10 kg payload** | **Program baseline** (assigned) |
| Centerline “A-10 style” mount, no gimbal | Consistent with static-pattern architecture; boresight held by **host pointing only** |
| Rocket host <3.5 kg / 18 in | Outside current MPL-D module envelope docs — if used as separate air-launched host, requires separate interface spec |

---

## Recommended next actions

1. Obtain AeroDiode (or alternate) **full datasheet PDF** and driver module specs; record in repo with revision date.
2. Procure or borrow COL010 or equivalent collimator; measure beam diameter and divergence at low power before 10 W operation.
3. Run `analysis/nir_940nm_link_budget_notes.md` calculations against **measured** divergence, not vendor marketing.
4. Execute Phase 0 surrogate sensor tests (three-class minimum) before locking 915/940 nm single-band recommendation.

## Open questions / gaps

- Driver module mass, efficiency, and EMI behavior for 11.5 A pulsed operation.
- DOE split of 10 W fiber output — zero-order leakage and per-beamlet power unmeasured.
- Export control screening for 10 W NIR fiber module + integration data (R-EXP-001).
