# MMDA: Practical Assignment 1

Team project for Methods and models for multivariate data analysis.
We predict `churn` (`Yes` = positive class) with logistic regression and study
whether univariate data cleaning improves its performance.

Dataset: [Telecom churn on Kaggle](https://www.kaggle.com/datasets/amnaasabahat/telecom-churn/data).
The version already in this repository is `telecom_churn.csv`; keep it unchanged.
It contains 20,030 rows, 23 columns, and 20,000 distinct customer IDs.
`diabetes.csv` is a separate dataset and is not used for this project.

## Start here

1. Read [the proposed team split](TEAM_PLAN.md). Agree on owners before assigning work.
2. Install Python 3.11 or later, then run `python -m pip install -r requirements.txt`.
3. Run `python -m notebook` from this repository directory.
4. Open `01_numeric_audit.ipynb` and select **Restart Kernel and Run All Cells**.

The numeric notebook is an initial contribution: training-data statistics, plots,
formatting issues, and outlier flags for three columns. It does not fit a model
or finish the cleaning. The original `data.ipynb` is preserved.

Every analysis notebook should use `from data_split import load_split` followed
by `train, test = load_split()`. The split holds out 20% of customer IDs and keeps
all records for one customer on the same side. Use training data for exploration
and choosing cleaning rules; reserve test data for the final model comparison.

## Remaining deliverables

- A combined Jupyter notebook containing baseline, per-variable analysis,
  justified cleaning, and the model comparison.
- A PDF report with introduction, analysis, results, and conclusion.

No baseline, improvement claim, or final report has been produced yet.
