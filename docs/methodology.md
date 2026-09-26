# Methodology

## Design

This is a controlled computational proof-of-concept using 1,000 synthetic higher-education administrative staff profiles, with 200 profiles assigned to each of five administrative roles. The fixed random seed is 42. No measured employee data are used.

## Competencies and role requirements

Eight operational digital competencies (C1–C8) are scored on a five-level proficiency scale. The operational role requirement matrix and competency definitions are recorded in `config.yaml` and `data/raw/competency_dictionary.csv`. The requirements are experiment assumptions; they are not numerical values prescribed by DigComp or Jisc. C8 is an operational competency drawn from the professional-services context and is not an official DigComp domain.

## Synthetic profile generation

Profiles are generated from role-specific competency means in the configuration, with Gaussian shared latent factors for related competency pairs and competency-specific noise. Scores are rounded to ordinal levels and clipped to the range 1–5. These parameters create controlled variation and correlation for the computational experiment; they are not estimates of actual staff proficiency.

## Gap calculation and target

For employee i, competency j and their role's requirement, the competency gap is `Gij = max(0, Rij - Cij)`. The overall gap score is `sum(Gij) / 32 × 100`. Classes are Low Gap for 0 to <25%, Moderate Gap for 25 to <50%, and High Gap for 50 to 100%. The thresholds are operational definitions for this experiment.

## Classification and evaluation

The feature matrix contains role and C1–C8. `Gap_Class` is the target. Gap components and the overall score are excluded from the feature matrix. Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting are evaluated using a stratified 80/20 train/test split (seed 42) and five-fold stratified cross-validation on the training partition. Reported metrics are accuracy, macro precision, macro recall, and macro-F1. Held-out permutation importance describes model dependence and is not used for model selection.

## Limitations

The target is mathematically derived from the same competency inputs used as predictors. The experiment therefore demonstrates computational feasibility on synthetic data, not real-world predictive validity. Role requirements and gap thresholds are operational assumptions. External validation would require real institutional data or expert-validated competency assessments.
