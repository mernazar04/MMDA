"""Shared raw-data loading and customer-level train/test split.

This module does not clean predictors or fit a model.
"""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


DATA_PATH = Path(__file__).resolve().parent / "telecom_churn.csv"
RANDOM_STATE = 42
TEST_SIZE = 0.20


def load_split(path=DATA_PATH):
    """Return raw train/test DataFrames with original zero-based row indices.

    Preserve strings and empty fields so formatting and missingness can be audited.
    Split sorted unique customer IDs, stratified by their consistent churn label.
    Repeated records are retained and always stay on one side of the split.
    """
    raw = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {"customer_id", "churn"}
    if not required.issubset(raw.columns):
        raise ValueError("The CSV must contain customer_id and churn.")
    if raw["customer_id"].str.strip().eq("").any():
        raise ValueError("Resolve missing customer IDs before splitting.")
    if not raw["churn"].isin(["No", "Yes"]).all():
        raise ValueError("Expected nonmissing churn labels No/Yes.")
    if raw.groupby("customer_id")["churn"].nunique().gt(1).any():
        raise ValueError("Resolve conflicting churn labels within a customer.")

    customers = (
        raw[["customer_id", "churn"]]
        .drop_duplicates("customer_id")
        .sort_values("customer_id")
    )
    train_ids, test_ids = train_test_split(
        customers["customer_id"],
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=customers["churn"],
    )
    train = raw.loc[raw["customer_id"].isin(train_ids)].copy()
    test = raw.loc[raw["customer_id"].isin(test_ids)].copy()
    assert set(train["customer_id"]).isdisjoint(test["customer_id"])
    assert len(train) + len(test) == len(raw)
    return train, test
