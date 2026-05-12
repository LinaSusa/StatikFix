"""
Snow load calculation – simplified approach
(Not a load-bearing structural verification)
"""

def shape_coefficient(roof_pitch: float) -> float:
    """
    Simplified according to EN 1991-1-3:
    - up to 30°: μ = 0.8
    - from 60°: μ = 0.0
    - linear interpolation in between
    """
    if roof_pitch <= 30:
        return 0.8
    if roof_pitch >= 60:
        return 0.0

    return 0.8 * (60 - roof_pitch) / 30


def snow_load(
    ground_snow_load: float,
    roof_pitch: float,
    ce: float = 1.0,
    ct: float = 1.0,
) -> dict:
    """
    Calculates characteristic snow load on the roof.
    """
    mu = shape_coefficient(roof_pitch)
    s = mu * ce * ct * ground_snow_load

    return {
        "mu": mu,
        "ce": ce,
        "ct": ct,
        "s": s,
    }