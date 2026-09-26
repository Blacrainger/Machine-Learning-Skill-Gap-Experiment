from src.data_generator import generate_profiles
from src.skill_gap import calculate_skill_gaps


def test_no_target_leakage_in_declared_feature_set():
    data = calculate_skill_gaps(generate_profiles())
    features = ["Role"] + [f"C{i}" for i in range(1, 9)]
    assert features == ["Role", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
    assert not any("Gap" in feature or "Score" in feature for feature in features)
