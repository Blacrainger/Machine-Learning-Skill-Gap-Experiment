import pandas as pd
from src.config import load_config
from src.skill_gap import calculate_skill_gaps, assign_gap_class


def test_gap_calculation_and_score():
    cfg = load_config()
    row = {"Employee_ID": "X", "Role": cfg["roles"][0], **{f"C{i}": 3 for i in range(1, 9)}}
    out = calculate_skill_gaps(pd.DataFrame([row]), cfg).iloc[0]
    assert out.C1_Gap == 1 and out.C2_Gap == 2
    expected = sum(max(0, level - 3) for level in cfg["role_requirements"][cfg["roles"][0]]) / 32 * 100
    assert out.Overall_Gap_Score == expected


def test_thresholds():
    assert assign_gap_class(0) == "Low Gap" and assign_gap_class(24.99) == "Low Gap"
    assert assign_gap_class(25) == "Moderate Gap" and assign_gap_class(49.99) == "Moderate Gap"
    assert assign_gap_class(50) == "High Gap" and assign_gap_class(100) == "High Gap"
