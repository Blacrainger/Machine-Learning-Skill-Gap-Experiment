import json
from .config import ROOT, load_config
from .competency_framework import save_framework
from .data_generator import generate_profiles
from .skill_gap import calculate_skill_gaps
from .evaluate import evaluate_models
from .visualization import make_figures
import pandas as pd
from sklearn.model_selection import train_test_split

def run():
    cfg=load_config()
    for path in [ROOT/"data/raw",ROOT/"data/processed",ROOT/"figures"]: path.mkdir(parents=True,exist_ok=True)
    save_framework()
    profiles=generate_profiles(cfg); profiles.to_csv(ROOT/"data/raw/synthetic_staff_profiles.csv",index=False)
    data=calculate_skill_gaps(profiles,cfg); data.to_csv(ROOT/"data/processed/staff_skill_gap_dataset.csv",index=False)
    roles=profiles.Role.value_counts().reindex(cfg["roles"]); roles.rename_axis("Role").rename("count").reset_index().to_csv(ROOT/"results/dataset_summary.csv",index=False)
    data.Gap_Class.value_counts().reindex(["Low Gap","Moderate Gap","High Gap"],fill_value=0).rename_axis("Gap_Class").rename("count").reset_index().to_csv(ROOT/"results/gap_distribution.csv",index=False)
    data.groupby("Role").Overall_Gap_Score.agg(["mean","median","std","min","max"]).reset_index().to_csv(ROOT/"results/role_gap_statistics.csv",index=False)
    X=data[["Role"]+[f"C{i}" for i in range(1,9)]]; y=data.Gap_Class
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=cfg["train_test_ratio"],random_state=cfg["random_seed"],stratify=y)
    performance,cv,matrices,predictions,importance=evaluate_models(X_train,X_test,y_train,y_test,cfg)
    performance.to_csv(ROOT/"results/model_performance.csv",index=False); cv.to_csv(ROOT/"results/cross_validation_results.csv",index=False)
    predictions["Employee_ID"] = predictions["Employee_ID"].map(data["Employee_ID"])
    predictions.to_csv(ROOT/"results/model_predictions.csv",index=False)
    importance.to_csv(ROOT/"results/feature_importance.csv",index=False)
    for name, matrix in matrices.items(): matrix.to_csv(ROOT/"results"/("confusion_matrix_"+name.lower().replace(" ","_")+".csv"))
    data.groupby("Role").Overall_Gap_Score.describe().to_json(ROOT/"results/role_gap_statistics.json",orient="index",indent=2)
    summary={"n_records":len(data),"roles":roles.to_dict(),"gap_classes":data.Gap_Class.value_counts().to_dict(),"feature_columns":X.columns.tolist(),"target":"Gap_Class","test_size":len(X_test),"seed":cfg["random_seed"]}
    (ROOT/"results/experiment_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    make_figures(data,performance,matrices,importance,ROOT/"figures")
    return data,performance,cv,importance

if __name__ == "__main__": run()

