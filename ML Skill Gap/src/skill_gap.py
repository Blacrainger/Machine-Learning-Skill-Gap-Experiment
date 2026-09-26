import numpy as np
import pandas as pd
from .config import load_config

def assign_gap_class(score, config=None):
    cfg = config or load_config()
    if score < cfg["gap_thresholds"]["low_upper_exclusive"]:
        return "Low Gap"
    if score < cfg["gap_thresholds"]["moderate_upper_exclusive"]:
        return "Moderate Gap"
    return "High Gap"

def calculate_skill_gaps(profiles, config=None):
    cfg = config or load_config()
    result = profiles.copy()
    codes = [c["code"] for c in cfg["competencies"]]
    req = cfg["role_requirements"]
    gaps = np.maximum(0, np.array([req[r] for r in result["Role"]]) - result[codes].to_numpy())
    gap_cols = [f"{c}_Gap" for c in codes]
    result[gap_cols] = gaps
    result["Overall_Gap_Score"] = gaps.sum(axis=1) / 32 * 100
    result["Gap_Class"] = result["Overall_Gap_Score"].map(lambda x: assign_gap_class(x, cfg))
    return result
