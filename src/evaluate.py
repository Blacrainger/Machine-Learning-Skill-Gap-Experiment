import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import StratifiedKFold, cross_validate
from .config import load_config
from .models import build_models

METRICS = {"accuracy":"accuracy", "precision_macro":"precision_macro", "recall_macro":"recall_macro", "macro_f1":"f1_macro"}

def evaluate_models(X_train, X_test, y_train, y_test, config=None):
    cfg = config or load_config()
    models = build_models(cfg)
    cv = StratifiedKFold(n_splits=cfg["cv_folds"], shuffle=True, random_state=cfg["random_seed"])
    performance, cv_rows, matrices, predictions, importances = [], [], {}, [], []
    for name, model in models.items():
        scores = cross_validate(model, X_train, y_train, cv=cv, scoring=METRICS, n_jobs=1)
        for metric in METRICS:
            vals = scores[f"test_{metric}"]
            cv_rows.append({"model":name,"metric":metric,"mean":vals.mean(),"std":vals.std(ddof=1)})
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        performance.append({"model":name,"accuracy":accuracy_score(y_test,pred),"precision_macro":precision_score(y_test,pred,average="macro",zero_division=0),"recall_macro":recall_score(y_test,pred,average="macro",zero_division=0),"macro_f1":f1_score(y_test,pred,average="macro",zero_division=0)})
        labels = ["Low Gap","Moderate Gap","High Gap"]
        matrices[name] = pd.DataFrame(confusion_matrix(y_test,pred,labels=labels), index=labels, columns=labels)
        predictions.extend({"model":name,"Employee_ID":i,"actual":a,"predicted":p} for i,a,p in zip(X_test.index,y_test,pred))
        # Permutation importance on held-out set measures score decrease under shuffling.
        pi = permutation_importance(model,X_test,y_test,n_repeats=20,random_state=cfg["random_seed"],scoring="f1_macro",n_jobs=1)
        importances.extend({"model":name,"feature":feature,"importance_mean":mean,"importance_std":std,"method":"held-out permutation importance; macro-F1 decrease"} for feature,mean,std in zip(X_test.columns,pi.importances_mean,pi.importances_std))
    return pd.DataFrame(performance), pd.DataFrame(cv_rows), matrices, pd.DataFrame(predictions), pd.DataFrame(importances)
