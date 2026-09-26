import pandas as pd
from .config import ROOT, load_config

def competency_dictionary(config=None):
    cfg = config or load_config()
    rows = []
    for item in cfg["competencies"]:
        code = item["code"]
        definition = cfg["competency_definitions"][code]
        rows.append({"competency_code": code, "competency_name": item["name"], **definition})
    return pd.DataFrame(rows)

def role_requirements(config=None):
    cfg = config or load_config()
    codes = [c["code"] for c in cfg["competencies"]]
    return pd.DataFrame.from_dict(cfg["role_requirements"], orient="index", columns=codes).rename_axis("Role").reset_index()

def save_framework():
    (ROOT / "data" / "raw").mkdir(parents=True, exist_ok=True)
    competency_dictionary().to_csv(ROOT / "data" / "raw" / "competency_dictionary.csv", index=False)
    role_requirements().to_csv(ROOT / "data" / "raw" / "role_requirements.csv", index=False)
