from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from .config import load_config
from .preprocessing import make_preprocessor

def build_models(config=None):
    cfg = config or load_config()
    p = cfg["model_parameters"]
    return {
      "Logistic Regression": Pipeline([("preprocess",make_preprocessor(True)),("classifier",LogisticRegression(**p["logistic_regression"]))]),
      "Decision Tree": Pipeline([("preprocess",make_preprocessor()),("classifier",DecisionTreeClassifier(random_state=cfg["random_seed"],**p["decision_tree"]))]),
      "Random Forest": Pipeline([("preprocess",make_preprocessor()),("classifier",RandomForestClassifier(random_state=cfg["random_seed"],**p["random_forest"]))]),
      "Gradient Boosting": Pipeline([("preprocess",make_preprocessor()),("classifier",GradientBoostingClassifier(random_state=cfg["random_seed"],**p["gradient_boosting"]))]),
    }
