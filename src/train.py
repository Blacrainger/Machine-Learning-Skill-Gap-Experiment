"""Model fitting helpers used by the experiment."""

from .config import load_config
from .models import build_models


def train_models(X_train, y_train, config=None):
    """Fit and return the configured classifiers on the supplied training split."""
    models = build_models(config or load_config())
    for model in models.values():
        model.fit(X_train, y_train)
    return models
