# Experiment notes

The repository records a controlled synthetic experiment for five higher-education administrative roles. The configuration sets the random seed to 42, generates 1,000 profiles (200 per role), and evaluates Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting with an 80/20 stratified split and five-fold stratified cross-validation on the training data.

The source data, configuration, scripts, and generated output files are the record of the run. Re-running `python -m src.run_experiment` regenerates them with the checked-in configuration. The data do not represent measured competency levels of real staff.
