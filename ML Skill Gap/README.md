<<<<<<< HEAD
# Machine Learning-Based Identification of Role-Specific Digital Skill Gaps Among Higher Education Administrative Staff

## Overview

This repository contains the computational experiment developed for the MSc Computer Science research project:

**Machine Learning Framework for Intelligent Skill-Gap Analysis and Reskilling Recommendations in Higher Education Institutions**

The experiment investigates the feasibility of using machine-learning classification models to identify role-specific digital skill-gap categories among higher education administrative staff.

The current experiment focuses specifically on five administrative roles:

1. Registry / Records Administration
2. Human Resources Administration
3. Finance / Accounts Administration
4. Admissions Administration
5. Departmental / Academic Administration

The experiment uses a synthetic dataset of 1,000 staff profiles and compares four machine-learning classification algorithms.

---

## Research Objective

The objective of this experiment is to determine whether machine-learning models can classify administrative staff into different digital skill-gap categories based on their current digital competency profiles and role requirements.

The experiment is designed as a controlled computational proof-of-concept.

---

## Important Data Notice

**The dataset used in this experiment is entirely synthetic.**

The generated staff profiles do not represent measured competency levels of actual Nigerian universities or higher education institutions.

The synthetic data were created because confidential institutional employee competency data were not available for this experimental stage.

Therefore, the results should not be interpreted as evidence of the actual digital skill levels of Nigerian higher education administrative staff.

---

## Digital Competency Framework

The experiment uses eight operational digital competencies derived from the competency areas of DigComp and the Jisc Digital Capability Profile for professional services staff in education.

| Code | Competency |
|---|---|
| C1 | ICT Proficiency & Digital Productivity |
| C2 | Information Literacy |
| C3 | Data Literacy & Analysis |
| C4 | Digital Communication & Collaboration |
| C5 | Digital Content & Document Creation |
| C6 | Digital Safety, Privacy & Security |
| C7 | Digital Problem Solving |
| C8 | Digital Administrative Systems Use |

C8 is an operational competency derived from the professional-services context and is not presented as an additional official DigComp domain.

---

## Proficiency Scale

Each competency is represented using a five-level scale:

| Level | Description |
|---|---|
| 1 | Basic Awareness |
| 2 | Developing |
| 3 | Functional |
| 4 | Proficient |
| 5 | Advanced |

---

## Role Requirement Matrix

The experiment uses the following operational role requirements:

| Role | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Registry / Records | 4 | 5 | 4 | 4 | 4 | 5 | 4 | 5 |
| Human Resources | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 5 |
| Finance / Accounts | 4 | 4 | 5 | 4 | 4 | 5 | 4 | 5 |
| Admissions | 4 | 5 | 4 | 5 | 4 | 5 | 4 | 5 |
| Departmental / Academic | 4 | 4 | 4 | 5 | 4 | 4 | 4 | 5 |

These numerical values are operational research assumptions used to construct the experiment. They are not values explicitly prescribed by DigComp or Jisc.

---

## Synthetic Dataset

The experiment contains:

- 1,000 synthetic staff profiles
- 200 profiles per administrative role
- 8 digital competency variables
- 5-level competency scores
- Role-specific competency distributions
- Controlled variation and correlations between related competencies

A fixed random seed of **42** is used to support reproducibility.

---

## Skill-Gap Calculation

For employee `i` and competency `j`, the competency-level gap is calculated as:

\[
G_{ij} = max(0, R_{rj} - C_{ij})
\]

where:

- `R` = required competency level
- `C` = current competency level
- `G` = competency-level gap

The overall skill-gap score is calculated as:

\[
GS_i =
\frac{\sum G_{ij}}{32}
\times100
\]

The maximum possible gap is 32 because there are eight competencies and the maximum deficit per competency is four levels.

---

## Gap Classification

The experiment uses three operational categories:

| Score | Classification |
|---|---|
| 0–<25% | Low Gap |
| 25–<50% | Moderate Gap |
| 50–100% | High Gap |

These thresholds are experimental operational definitions and are not presented as universally validated thresholds.

---

## Machine-Learning Models

Four classification algorithms are evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting

The ML features are:

- Role
- C1
- C2
- C3
- C4
- C5
- C6
- C7
- C8

The target variable is:

`Gap_Class`

The overall gap score and individual calculated gap variables are excluded from the feature set to prevent target leakage.

---

## Experimental Design

The dataset is divided using:

- 80% training data
- 20% held-out test data
- Stratified splitting

Five-fold stratified cross-validation is performed on the training data.

The following evaluation metrics are calculated:

- Accuracy
- Precision
- Recall
- Macro-F1
- Confusion Matrix

Feature importance is also calculated to support model interpretation.

---

## Experimental Results

The experiment produced the following held-out test results:

| Model | Accuracy | Precision | Recall | Macro-F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 92.50% | 88.98% | 93.06% | 90.73% |
| Decision Tree | 67.00% | 62.92% | 74.17% | 64.05% |
| Random Forest | 91.50% | 87.20% | 91.39% | 89.05% |
| Gradient Boosting | 89.00% | 94.84% | 74.44% | 79.89% |

These values were generated by executing the experimental pipeline.

They should not be manually changed or entered independently of the generated result files.

---

## Reproducibility

Clone the repository:

```bash
git clone <repository-url>
cd hei-digital-skill-gap-ml
```

Install dependencies, run the checks, and reproduce the complete experiment from the repository root:

```bash
python -m pip install -r requirements.txt
python -m pytest src/tests
python -m src.run_experiment
```

The fixed-seed run regenerates the raw profiles, processed skill-gap dataset, result tables, and figures. Results are written to `results/`; figures are written to `figures/`.

## Repository map

- `config.yaml`: experiment configuration and role requirements.
- `data/raw/`: generated staff profiles, role requirements, and competency dictionary.
- `data/processed/`: profiles with calculated competency gaps and classes.
- `src/`: experiment implementation; `src/tests/` contains the existing test cases grouped by topic.
- `results/`: generated tables, predictions, confusion matrices, and run summaries.
- `figures/`: generated figures, including model confusion matrices.
- `docs/`: methodology and experiment notes.

The reported test metrics above are reproduced from the checked-in configuration and experiment pipeline; the underlying result files are the generated record of the run.
=======
# Machine-Learning-Skill-Gap-Experiment
The experiment investigates the feasibility of using machine-learning classification models to identify role-specific digital skill-gap categories among higher education administrative staff.
>>>>>>> af06a4ed69c521b9150b808f26539fd7f923814e
