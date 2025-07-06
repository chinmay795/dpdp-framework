
def estimate_penalty(violators, total, base_penalty_inr=12_000_000, reduction_pct=0.38):
    """
    Estimates the penalty with potential reduction for compliance effort.
    """
    base_total_penalty = base_penalty_inr * violators
    reduced_penalty = base_total_penalty * (1 - reduction_pct)
    return {
        "estimated_penalty_inr": base_total_penalty,
        "adjusted_penalty_inr": reduced_penalty,
        "penalty_reduction_pct": reduction_pct * 100
    }
