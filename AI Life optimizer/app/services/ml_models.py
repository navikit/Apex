"""Machine learning helpers.

This module provides scaffolding for training and prediction pipelines.
"""

from __future__ import annotations

import pandas as pd
from sklearn.linear_model import LinearRegression


def estimate_productivity_trend(df: pd.DataFrame) -> dict:
    """Estimate a simple productivity trend based on historical metrics.

    This is a placeholder and should be replaced with a more sophisticated model.
    """

    if df.empty:
        return {"status": "no_data", "trend": 0.0}

    # Example feature: day index vs productivity score.
    df = df.sort_values("recorded_at")
    df = df.reset_index(drop=True)
    df["day_index"] = df.index.astype(float)

    model = LinearRegression()
    model.fit(df[["day_index"]], df["metric_value"])

    # higher slope => improving productivity
    return {"status": "ok", "trend": float(model.coef_[0])}
