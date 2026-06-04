# MPL-D internal codename | Counter-UAS Multi-Point Laser Dazzler Prototype
"""
Pulsed thermal duty-cycle model for 940 nm candidate stack.

WARNING: First-order lumped thermal model only. No measured R_th, no CFD.
"""

from __future__ import annotations

try:
    import numpy as np
except ImportError:
    np = None


def dissipated_power(optical_w: float, eta_wp: float = 0.40) -> float:
    p_elec = optical_w / eta_wp
    return p_elec - optical_w


def lumped_thermal_step(
    temp_c: float,
    p_diss_w: float,
    dt_s: float,
    r_th_c_per_w: float = 2.0,
    c_th_j_per_c: float = 30.0,
    t_amb_c: float = 25.0,
) -> float:
    """Single-node: C dT/dt = P - (T-T_amb)/R."""
    dT = (p_diss_w * dt_s / c_th_j_per_c) - ((temp_c - t_amb_c) * dt_s / (r_th_c_per_w * c_th_j_per_c))
    return temp_c + dT


def simulate_burst_profile(
    optical_w: float = 10.0,
    pulse_s: float = 0.5,
    cooldown_s: float = 5.0,
    bursts: int = 6,
    eta_wp: float = 0.40,
    r_th: float = 2.0,
    c_th: float = 30.0,
) -> None:
    p_diss = dissipated_power(optical_w, eta_wp)
    dt = 0.1
    t = 0.0
    temp = 25.0
    t_max = 25.0
    print("=" * 60)
    print("Thermal pulse model (UNVALIDATED lumped parameters)")
    print(f"P_opt={optical_w} W, P_diss~{p_diss:.1f} W, R_th={r_th} C/W, C_th={c_th} J/C")
    print("=" * 60)
    for b in range(bursts):
        elapsed = 0.0
        while elapsed < pulse_s:
            temp = lumped_thermal_step(temp, p_diss, dt, r_th, c_th)
            t_max = max(t_max, temp)
            elapsed += dt
            t += dt
        elapsed = 0.0
        while elapsed < cooldown_s:
            temp = lumped_thermal_step(temp, 0.0, dt, r_th, c_th)
            elapsed += dt
            t += dt
    print(f"After {bursts} bursts: T_max={t_max:.1f} C (planning limit 55 C vendor case — LSO may set lower)")
    duty = bursts * pulse_s / (bursts * (pulse_s + cooldown_s))
    print(f"Duty cycle={100*duty:.1f}%")
    print("Replace R_th, C_th with measured soak data from T-04.")
    print("=" * 60)


if __name__ == "__main__":
    simulate_burst_profile()
