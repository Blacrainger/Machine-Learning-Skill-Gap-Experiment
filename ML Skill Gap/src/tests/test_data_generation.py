import pandas as pd
from src.config import load_config
from src.data_generator import generate_profiles


def test_dataset_contract_and_reproducibility():
    a = generate_profiles()
    b = generate_profiles()
    cfg = load_config()
    codes = [c["code"] for c in cfg["competencies"]]
    pd.testing.assert_frame_equal(a, b)
    assert len(a) == 1000 and a.Role.value_counts().to_dict() == {r: 200 for r in cfg["roles"]}
    assert a.Employee_ID.is_unique and a[codes].notna().all().all()
    assert a[codes].stack().between(1, 5).all() and a[codes].nunique().min() > 1
