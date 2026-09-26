import numpy as np
import pandas as pd
from .config import load_config

# Correlated latent factors couple related skill families while retaining independent noise.
CORRELATIONS = [(0,2),(0,6),(0,7),(1,2),(3,4),(5,7),(6,7)]

def generate_profiles(config=None):
    cfg = config or load_config()
    rng = np.random.default_rng(cfg["random_seed"])
    rows = []
    codes = [c["code"] for c in cfg["competencies"]]
    loading = np.zeros((8, len(CORRELATIONS)))
    for f, (a,b) in enumerate(CORRELATIONS):
        loading[a,f] = loading[b,f] = np.sqrt(cfg["correlation_strength"])
    for role in cfg["roles"]:
        means = np.asarray(cfg["generation_means"][role])
        n = cfg["employees_per_role"]
        factors = rng.normal(0, cfg["latent_factor_sd"], size=(n,len(CORRELATIONS)))
        noise = rng.normal(0, cfg["individual_noise_sd"], size=(n,8))
        latent = means + factors @ loading.T + noise
        # Ordinal rounding plus clipping provides the specified 1–5 scale.
        scores = np.clip(np.rint(latent), 1, 5).astype(int)
        for k, score in enumerate(scores):
            rows.append({"Employee_ID": f"EMP{len(rows)+1:04d}", "Role": role, **dict(zip(codes, score.tolist()))})
    return pd.DataFrame(rows)
