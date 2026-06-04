# MPL-D internal codename | Counter-UAS Multi-Point Laser Dazzler Prototype
"""
Vibration-induced beam wander — first-order angular jitter to linear displacement.

WARNING: No measured host vibration spectrum. R-VIB-001 quantification pending T-05.
"""

from __future__ import annotations

import math


def spot_displacement_m(range_m: float, delta_theta_rad: float) -> float:
    """Lateral displacement at range R for small angle jitter."""
    return range_m * math.tan(delta_theta_rad)


def irradiance_loss_fraction(beam_radius_m: float, displacement_m: float) -> float:
    """
    Crude fraction of peak irradiance retained if beam center shifts by displacement
    (Gaussian approx, on-axis peak scales as exp(-2*(d/w)^2)).
    """
    if beam_radius_m <= 0:
        raise ValueError("beam_radius_m must be positive")
    x = displacement_m / beam_radius_m
    return math.exp(-2.0 * x * x)


def example_table() -> None:
    theta_uRad_values = [100, 500, 1000]  # micro-rad jitter
    ranges = [50, 500, 1000]
    w = 0.05  # 5 cm spot radius at target (planning)
    print("=" * 70)
    print("Vibration wander model (UNVALIDATED — illustrative jitter values)")
    print(f"Assumed spot radius at target w={w} m")
    print("=" * 70)
    print(f"{'R[m]':>6} {'jitter[urad]':>14} {'disp[m]':>12} {'I/I0':>10}")
    for r in ranges:
        for urad in theta_uRad_values:
            dtheta = urad * 1e-6
            disp = spot_displacement_m(r, dtheta)
            frac = irradiance_loss_fraction(w, disp)
            print(f"{r:6d} {urad:14d} {disp:12.4f} {frac:10.4f}")
    print("=" * 70)
    print("T-05 must replace assumed jitter with measured table spectrum.")


if __name__ == "__main__":
    example_table()
