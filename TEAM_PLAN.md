# Proposed three-person work plan

This is a proposal for the team to agree on, not a confirmed assignment of tasks.

## What the assignment means

1. **Baseline:** fit a simple logistic regression to predict churn and record F1
   and ROC-AUC. The baseline needs a documented minimum treatment of missing
   values and text so that the model can run.
2. **Investigate:** each person examines their columns and explains problems.
3. **Clean:** implement justified rules, using training data to choose them.
4. **Compare:** refit the same model with the same customers and evaluate it on
   the same held-out test set. Report the actual change, even if it is small or negative.
5. **Submit:** one combined notebook and a PDF report.

Numeric variables are amounts or counts: use means, quartiles, histograms,
boxplots, and density plots. Categorical variables are labels: use frequency
tables, bar plots, missing-label checks, and spelling/category checks. Do not
calculate a mean of arbitrary category codes.

## Suggested division

| Proposed owner | Columns | Contribution |
| --- | --- | --- |
| Hazem (5 columns) | `tenure`, `monthly_charges`, `total_charges`, `paperless_billing`, `payment_method` | Numeric statistics and plots, charge formatting, missingness, outlier review, and billing-label frequencies and normalization proposals. |
| Teammate 2 (7 columns; owner to confirm) | `gender`, `senior_citizen`, `partner`, `dependents`, `signup_date`, `phone_service`, `multiple_lines` | Customer and phone category frequencies, label normalization proposals, and date validity and availability. |
| Teammate 3 (8 columns; owner to confirm) | `internet_service`, `online_security`, `online_backup`, `device_protection`, `tech_support`, `streaming_tv`, `streaming_movies`, `contract` | Internet-service and contract frequencies, structural categories, and normalization proposals. |
| Shared decisions (3 columns) | `churn`, `customer_id`, `internal_flag` | Audit churn as the prediction target. Use customer ID for splitting and duplicate review. Exclude `internal_flag` from both models until its meaning and availability at prediction time are established. |

The 5/7/8 proposal covers 20 owned columns and leaves 3 shared columns, accounting
for all 23 CSV columns. The numeric group has extra work on formatting, missing
values, outliers, and transformations. Each person writes the report paragraphs
for their own columns. Agree on the distribution together, and choose owners for
the shared baseline and final integration before implementing those steps.

## Agree on these before fitting models

- **Dataset suitability:** the assignment asks for multiple numerical features,
  at least five predictors, and continuous and discrete variables. There are
  three numeric measurement/count columns here plus binary categories. Confirm
  with the instructor whether encoded binary predictors count. Do not use the
  customer ID or arbitrary category numbers to satisfy the requirement. A possible
  starting feature set, subject to this confirmation, is the three numeric
  columns plus normalized `senior_citizen`, `partner`, and `dependents`.
- **One split:** use `load_split()` from `data_split.py` in each notebook. It uses
  a fixed seed (42), stratifies unique customers by churn, and holds out 20% of
  customer IDs. All repeated records for a customer stay together. There are
  30 extra records beyond unique IDs, including 20 exact duplicate rows. Keep
  them for this initial audit; agree on a duplicate policy before the baseline,
  and apply that policy consistently to both model comparisons.
- **Baseline:** logistic regression cannot consume blank numeric values or raw
  category strings. Agree on minimum numeric conversion, training-median
  imputation, one-hot encoding (`handle_unknown='ignore'`), and scaling. Record
  these as baseline necessities. Compare additional cleaning against that
  frozen baseline. The formatting-aware diagnostic view in the numeric notebook
  is not an already-defined baseline preprocessing pipeline.
- **Fair comparison:** keep model settings, predictors, split, and decision
  threshold fixed for the main comparison. Fit imputers, scaling, clipping
  bounds, and transformations only on training data. Use validation folds
  within training data for choosing changes, keeping customers grouped.
- **Metrics:** use churn-positive F1 and probability-based ROC-AUC, plus PR-AUC,
  precision, recall, and a confusion matrix if useful. Include a majority-class
  reference; accuracy alone can hide missed churn cases.
- **Scope:** assess `signup_date` for validity, but exclude it from initial
  predictors until its timing and a legitimate prediction date are established.
  Preserve `No internet service` and `No phone service` as meaningful categories
  unless a documented reason supports merging them.

## What each person hands over

For every owned column, record its meaning/type, missing count, distribution,
problem evidence, proposed rule, justification, and implementation status.
For numeric columns include mean, median, sample standard deviation, minimum,
maximum, range, quartiles, skewness, and excess kurtosis. Flag IQR outliers for
review; an extreme observation is not automatically an error. Logistic regression
does not require normally distributed predictors, so do not transform everything
just to make it look normal.

Use separate notebooks (`01_numeric_audit.ipynb`, which now also audits billing
categories, a future
`02_customer_categories.ipynb`, and a future `03_service_categories.ipynb`) to
avoid editing the same notebook simultaneously. Each notebook reads the same
raw CSV and shared split. Do not delete or reorder rows independently and then
join results by position; use original row indices and customer IDs.

## Small commits and review order

1. **Current contribution:** proposed division, shared split, numeric audit.
2. **Teammate contributions:** customer/date audit and service audit, each in its
   own branch and pull request.
3. **Shared baseline:** agree on features and duplicate handling, fit and record metrics.
4. **Cleaning:** review rules, implement them, and select options within training data.
5. **Final comparison and report:** integrate once; include each person's analysis.

Use branches and pull requests; each person reviews another person's work.
Choose one integration owner. Once merged, everyone pulls the shared setup
before starting their column work.

## Status

- [x] Inspect the supplied assignment and repository CSV.
- [x] Propose ownership and a reproducible customer-level split.
- [x] Prepare numeric profiling with diagnostic format parsing and IQR flags.
- [x] Audit billing-category frequencies and diagnostic label normalization.
- [ ] Team accepts or revises ownership and confirms dataset suitability.
- [ ] Establish baseline and duplicate policy.
- [ ] Complete remaining categorical/date audits and numeric cleaning decisions.
- [ ] Implement, validate, and compare cleaning steps.
- [ ] Combine notebook and write the PDF report.
