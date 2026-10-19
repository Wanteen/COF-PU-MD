"""Simple deterministic TPU composition checks."""
PTMG_REPEAT_MASS = 72.106
WATER_MASS = 18.015
MDI_MASS = 250.25
BDO_MASS = 90.12

def ptmg_molar_mass(repeats: int) -> float:
    if type(repeats) is not int or repeats < 1:
        raise ValueError("PTMG repeat count must be a positive integer")
    return repeats * PTMG_REPEAT_MASS + WATER_MASS

def check_stoichiometry(mdi: int, ptmg: int, bdo: int) -> dict:
    if any(type(x) is not int or x < 0 for x in (mdi, ptmg, bdo)):
        raise ValueError("Counts must be nonnegative integers")
    nco, oh = 2 * mdi, 2 * (ptmg + bdo)
    if oh == 0:
        raise ValueError("At least one diol is required")
    return {"NCO": nco, "OH": oh, "NCO_OH_ratio": nco / oh, "balanced": nco == oh}

def nominal_hard_segment_wt_fraction(mdi: int, ptmg: int, bdo: int, ptmg_mass: float) -> float:
    hard = mdi * MDI_MASS + bdo * BDO_MASS
    total = hard + ptmg * ptmg_mass
    if total <= 0:
        raise ValueError("Nonzero composition required")
    return hard / total
