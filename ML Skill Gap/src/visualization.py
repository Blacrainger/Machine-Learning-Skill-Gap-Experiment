from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

def make_figures(dataset, performance, matrices, importance, output):
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    (output / "confusion_matrices").mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", context="paper", font_scale=1.15)
    order = dataset.Role.drop_duplicates().tolist()
    fig, ax = plt.subplots(figsize=(9,5)); sns.countplot(data=dataset,x="Role",order=order,ax=ax,color="#4472C4"); ax.tick_params(axis="x",rotation=25); ax.set(title="Synthetic staff distribution by role",xlabel="Administrative role",ylabel="Employees"); fig.tight_layout(); fig.savefig(output/"staff_distribution_by_role.png",dpi=300); plt.close(fig)
    fig, ax = plt.subplots(figsize=(9,5)); sns.barplot(data=dataset,x="Role",y="Overall_Gap_Score",order=order,errorbar="sd",ax=ax,color="#70AD47"); ax.tick_params(axis="x",rotation=25); ax.set(title="Mean skill-gap score by administrative role",xlabel="Administrative role",ylabel="Overall gap score (%)"); fig.tight_layout(); fig.savefig(output/"mean_gap_by_role.png",dpi=300); plt.close(fig)
    fig, ax = plt.subplots(figsize=(7,5)); sns.countplot(data=dataset,x="Gap_Class",order=["Low Gap","Moderate Gap","High Gap"],ax=ax,color="#ED7D31"); ax.set(title="Skill-gap class distribution",xlabel="Gap class",ylabel="Employees"); fig.tight_layout(); fig.savefig(output/"gap_class_distribution.png",dpi=300); plt.close(fig)
    fig, ax = plt.subplots(figsize=(8,5)); perf=performance.melt("model",var_name="metric",value_name="score"); sns.barplot(data=perf,x="model",y="score",hue="metric",ax=ax); ax.set(ylim=(0,1),title="Held-out model performance",xlabel="Classifier",ylabel="Score"); ax.tick_params(axis="x",rotation=15); fig.tight_layout(); fig.savefig(output/"model_comparison.png",dpi=300); plt.close(fig)
    for name, matrix in matrices.items():
        fig, ax = plt.subplots(figsize=(5.5,4.5)); sns.heatmap(matrix,annot=True,fmt="d",cmap="Blues",ax=ax); ax.set(title=f"Confusion matrix: {name}",xlabel="Predicted",ylabel="Actual"); fig.tight_layout(); fig.savefig(output/"confusion_matrices"/(name.lower().replace(" ","_")+".png"),dpi=300); plt.close(fig)
    if not importance.empty:
        means=importance.groupby("feature",as_index=False).importance_mean.mean().sort_values("importance_mean")
        fig, ax=plt.subplots(figsize=(7,5)); ax.barh(means.feature,means.importance_mean,color="#5B9BD5"); ax.set(title="Mean permutation importance across models",xlabel="Macro-F1 decrease after permutation",ylabel="Input feature"); fig.tight_layout(); fig.savefig(output/"feature_importance.png",dpi=300); plt.close(fig)

