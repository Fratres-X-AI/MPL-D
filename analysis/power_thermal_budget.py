# MPL-D internal codename | Counter-UAS Multi-Point Laser Dazzler Prototype
"""
First-order power and thermal budget estimates for drone-mountable laser dazzler concepts.

WARNING — READ BEFORE USE
-------------------------
This script provides first-order estimates only. It does not model M² beam quality,
atmospheric turbulence, platform vibration/jitter, sensor AGC/filtering, or real-time
dynamics. All outputs carry high uncertainty. Validation against hardware measurements
is required before any design use.

Dependencies (install if missing):
    pip install numpy scipy matplotlib

Maturity: Concept. Supporting evidence: No validation against measured hardware data.
"""

from __future__ import annotations

import math
from typing import Tuple

try:
    import numpy as np
except ImportError as exc:
    raise ImportError("numpy required: pip install numpy") from exc

try:
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


# ---------------------------------------------------------------------------
# Physical constants and conservative assumption bounds
# ---------------------------------------------------------------------------

# Wall-plug efficiency for compact diode/DPSS modules (literature range, not measured here)
WALL_PLUG_EFF_MIN = 0.15  # conservative lower bound
WALL_PLUG_EFF_MAX = 0.35  # upper bound for well-cooled modules
WALL_PLUG_EFF_NOMINAL = 0.22  # nominal planning value; uncertainty ±40% relative

# Beer-Lambert: visible/NIR extinction coefficient (km^-1), clear day, sea level
# Source class: public atmospheric optics texts; highly weather-dependent
EXTINCTION_CLEAR_KM = 0.1   # 0.05–0.2 km^-1 typical range for 532 nm, clear
EXTINCTION_HAZE_KM = 0.5    # degraded visibility


def beam_radius_at_range(
    range_m: float,
    half_angle_rad: float,
    waist_radius_m: float = 0.0,
) -> float:
    """
    Far-field beam radius at distance R.

    For a Gaussian beam with half-angle divergence θ (small-angle approx):
        w(R) ≈ R * tan(θ) ≈ R * θ   (when waist contribution negligible)

    Parameters
    ----------
    range_m : slant range to target [m]
    half_angle_rad : half-angle beam divergence [rad]
    waist_radius_m : beam waist radius at exit [m]; often << R*θ for compact emitters

    Returns
    -------
    beam_radius_m : 1/e² intensity radius at range [m]
    """
    if range_m <= 0:
        raise ValueError("range_m must be positive")
    if half_angle_rad <= 0:
        raise ValueError("half_angle_rad must be positive")
    return math.sqrt(waist_radius_m ** 2 + (range_m * math.tan(half_angle_rad)) ** 2)


def irradiance_at_range(
    optical_power_w: float,
    range_m: float,
    half_angle_rad: float,
    num_beamlets: int = 1,
    overlap_factor: float = 1.0,
    waist_radius_m: float = 0.0,
) -> float:
    """
    Peak/on-axis irradiance estimate for a circular Gaussian spot (single beamlet).

    I ≈ (2 * P) / (π * w(R)²)   [W/m²]

    For N non-overlapping equal-power beamlets, total power divides; per-spot
    irradiance uses P/N per beamlet unless overlap_factor > 1 redistributes power.

    overlap_factor : 1.0 = no overlap; >1.0 not physically valid for peak irradiance
                     — kept for sensitivity studies only.

    Uncertainty: does not account for atmospheric scintillation, beam wander,
    or non-Gaussian profiles from DOE pattern generators.
    """
    if optical_power_w <= 0:
        raise ValueError("optical_power_w must be positive")
    if num_beamlets < 1:
        raise ValueError("num_beamlets must be >= 1")

    power_per_beamlet = optical_power_w / num_beamlets
    w = beam_radius_at_range(range_m, half_angle_rad, waist_radius_m)
    area = math.pi * w ** 2
    return (2.0 * power_per_beamlet) / area


def atmospheric_transmission(
    range_m: float,
    extinction_per_km: float = EXTINCTION_CLEAR_KM,
) -> float:
    """
    Beer-Lambert atmospheric transmission (single-scattering, no turbulence).

    T = exp(-β * L)   where β = extinction coefficient [1/m], L = path length [m]

    extinction_per_km : extinction coefficient [km^-1]; convert to [m^-1] internally.

    Omitted: multiple scattering, wavelength-specific aerosol models, fog/rain.
    """
    if range_m < 0:
        raise ValueError("range_m must be non-negative")
    if extinction_per_km < 0:
        raise ValueError("extinction_per_km must be non-negative")
    beta = extinction_per_km / 1000.0  # km^-1 -> m^-1
    return math.exp(-beta * range_m)


def effective_irradiance_at_range(
    optical_power_w: float,
    range_m: float,
    half_angle_rad: float,
    extinction_per_km: float = EXTINCTION_CLEAR_KM,
    num_beamlets: int = 1,
    waist_radius_m: float = 0.0,
) -> float:
    """Irradiance at range after simple atmospheric attenuation (linear model)."""
    i_vacuum = irradiance_at_range(
        optical_power_w, range_m, half_angle_rad, num_beamlets, waist_radius_m=waist_radius_m
    )
    return i_vacuum * atmospheric_transmission(range_m, extinction_per_km)


def electrical_power_draw(
    optical_power_w: float,
    wall_plug_efficiency: float = WALL_PLUG_EFF_NOMINAL,
) -> Tuple[float, float, float]:
    """
    Estimate electrical input power from optical output and wall-plug efficiency.

    P_elec = P_opt / η_wp

    Returns (nominal, min_eff_case, max_eff_case) using efficiency bounds.
    """
    if optical_power_w <= 0:
        raise ValueError("optical_power_w must be positive")
    if not (0 < wall_plug_efficiency <= 1):
        raise ValueError("wall_plug_efficiency must be in (0, 1]")

    p_nom = optical_power_w / wall_plug_efficiency
    p_high = optical_power_w / WALL_PLUG_EFF_MAX  # lower electrical draw
    p_low = optical_power_w / WALL_PLUG_EFF_MIN   # higher electrical draw
    return p_nom, p_low, p_high


def thermal_dissipation_w(
    optical_power_w: float,
    wall_plug_efficiency: float = WALL_PLUG_EFF_NOMINAL,
) -> float:
    """
    Rough heat load to platform: electrical in minus optical out.

    Q ≈ P_elec - P_opt = P_opt * (1/η - 1)

    Does not include driver electronics losses separately or convective cooling capacity.
    """
    p_elec, _, _ = electrical_power_draw(optical_power_w, wall_plug_efficiency)
    return p_elec - optical_power_w


def example_sweep() -> None:
    """
    Print conservative example bounds and optionally plot irradiance vs range.

    Example parameters (not validated):
        P_opt = 5 W total, 9 beamlets, θ = 2 mrad half-angle, clear air
    """
    p_opt = 5.0
    n_beams = 9
    theta_mrad = 2.0
    theta_rad = theta_mrad * 1e-3

    print("=" * 60)
    print("MPL-D first-order link budget example (UNVALIDATED)")
    print("=" * 60)
    print(f"Total optical power: {p_opt} W | Beamlets: {n_beams} | theta: {theta_mrad} mrad")
    print()

    p_elec_nom, p_elec_high, p_elec_low = electrical_power_draw(p_opt)
    q_heat = thermal_dissipation_w(p_opt)
    print(f"Electrical draw (nom/min/max eta): {p_elec_nom:.1f} / {p_elec_high:.1f} / {p_elec_low:.1f} W")
    print(f"Thermal dissipation (nominal eta): {q_heat:.1f} W")
    print()

    ranges = [50, 100, 200, 500, 1000]
    print(f"{'Range [m]':>10} {'T_clear':>10} {'I_clear [W/m2]':>18} {'I_haze [W/m2]':>18}")
    for r in ranges:
        t_clear = atmospheric_transmission(r, EXTINCTION_CLEAR_KM)
        i_clear = effective_irradiance_at_range(p_opt, r, theta_rad, EXTINCTION_CLEAR_KM, n_beams)
        i_haze = effective_irradiance_at_range(p_opt, r, theta_rad, EXTINCTION_HAZE_KM, n_beams)
        print(f"{r:10d} {t_clear:10.4f} {i_clear:18.6f} {i_haze:18.6f}")

    print()
    print("Sensor dazzle threshold is sensor- and scenario-dependent.")
    print("No universal open-source threshold is assumed here.")
    print("=" * 60)

    if HAS_MPL:
        r_arr = np.linspace(10, 1000, 200)
        i_arr = [
            effective_irradiance_at_range(p_opt, float(r), theta_rad, EXTINCTION_CLEAR_KM, n_beams)
            for r in r_arr
        ]
        plt.figure(figsize=(8, 5))
        plt.semilogy(r_arr, i_arr)
        plt.xlabel("Range [m]")
        plt.ylabel("Effective irradiance [W/m2] (clear air, unvalidated)")
        plt.title("First-order irradiance vs range — NOT FOR DESIGN COMMITMENT")
        plt.grid(True, which="both", alpha=0.3)
        plt.tight_layout()
        out_path = "analysis/irradiance_vs_range_example.png"
        plt.savefig(out_path, dpi=120)
        print(f"Plot saved: {out_path} (optional; gitignored if regenerated locally)")


def example_940nm_doe_sweep() -> None:
    """
    940 nm AeroDiode-class candidate with DOE split — see nir_940nm_link_budget_notes.md.

    Planning: P_opt=10 W, N=9, eta_DOE=0.75, theta=1 mrad (mid bracket until measured).
    """
    p_opt = 10.0
    eta_doe = 0.75
    p_pattern = p_opt * eta_doe
    n_beams = 9
    theta_mrad = 1.0
    theta_rad = theta_mrad * 1e-3

    print("=" * 60)
    print("940 nm candidate + DOE example (UNVALIDATED)")
    print("=" * 60)
    p_elec_nom, _, _ = electrical_power_draw(p_opt, wall_plug_efficiency=0.40)
    print(f"P_opt={p_opt} W, eta_DOE={eta_doe}, pattern power={p_pattern:.1f} W")
    print(f"P_elec_peak~{p_elec_nom:.1f} W @ eta_wp=0.40")
    for r in [50, 100, 500, 1000]:
        i = effective_irradiance_at_range(
            p_pattern, float(r), theta_rad, EXTINCTION_CLEAR_KM, n_beams
        )
        print(f"  R={r} m  I_beamlet_eff~{i:.4f} W/m2")
    print("=" * 60)


if __name__ == "__main__":
    example_sweep()
    print()
    example_940nm_doe_sweep()
