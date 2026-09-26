from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def make_preprocessor(scale_numeric=False):
    numeric = [f"C{i}" for i in range(1,9)]
    transformers = [("role", OneHotEncoder(handle_unknown="ignore"), ["Role"])]
    if scale_numeric:
        transformers.append(("numeric", StandardScaler(), numeric))
    else:
        transformers.append(("numeric", "passthrough", numeric))
    return ColumnTransformer(transformers, remainder="drop")
