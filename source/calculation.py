# Scripts for calculating statistics
from typing import Literal

import numpy as np
import pandas as pd


def calc_monthly_attribute_per_decade(
        df:pd.DataFrame,
        column_name:Literal["tmax_degC","tmin_degC","af_days","rain_mm","sun_hours"],
    )-> pd.DataFrame:
    """Calculate monthly average for each decade for a given column name."""

    # group
    df_monthly = df.drop(["year", "is_predicted"], axis=1)
    df_monthly = (
        df_monthly[["decade", "month", column_name]]
        .groupby(["decade", "month"])
        .mean()
        .reset_index()
    )
    # pivot the output
    df_pivoted = df_monthly.pivot(index="decade", columns="month", values=column_name)

    return df_pivoted


def calc_min_max_per_decade(df:pd.DataFrame):
    """Pull out max and min of each decade."""

    # group
    df_monthly = df.drop(["year", "is_predicted"], axis=1)
    df_monthly = (
        df_monthly[["decade", "month", "tmax_degC", "tmin_degC"]]
        .groupby(["decade", "month"])
        .agg({"tmax_degC":max,"tmin_degC":min})
        .reset_index()
    )
    # pivot the output
    df_pivoted = df_monthly.pivot(index="decade", columns="month", values=["tmax_degC", "tmin_degC"])

    return df_pivoted
