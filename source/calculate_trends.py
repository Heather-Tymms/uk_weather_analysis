# Scripts for calculating statistics
from typing import Literal

import pandas as pd


def calc_monthly_attribute_per_decade(
    df: pd.DataFrame,
    column_name: Literal["tmax_degC", "tmin_degC", "af_days", "rain_mm", "sun_hours"],
    month_col: Literal["month", "worded_month"] = "month",
    aggregate_func: Literal["mean", "sum"] = "mean",
) -> pd.DataFrame:
    """Calculate monthly average for each decade for a given column name."""

    # group
    df_monthly = df.drop(["year", "is_predicted"], axis=1)
    df_monthly = (
        df_monthly[["decade", month_col, column_name]]
        .groupby(["decade", month_col])
        .agg({column_name: aggregate_func})
        .reset_index()
    )
    # pivot the output
    df_pivoted = df_monthly.pivot(index="decade", columns=month_col, values=column_name)

    return df_pivoted


def calc_min_max_per_decade(
    df: pd.DataFrame, month_col: Literal["month", "worded_month"] = "month"
) -> pd.DataFrame:
    """Pull out max and min of each decade."""

    # group
    df_monthly = df.drop(["year", "is_predicted"], axis=1)
    df_monthly = (
        df_monthly[["decade", month_col, "tmax_degC", "tmin_degC"]]
        .groupby(["decade", month_col])
        .agg({"tmax_degC": "max", "tmin_degC": "min"})
        .reset_index()
    )
    # pivot the output
    df_pivoted = df_monthly.pivot(
        index="decade", columns=month_col, values=["tmax_degC", "tmin_degC"]
    )

    return df_pivoted
