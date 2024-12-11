# Scripts for calculating statistics

# import numpy as np
# import pandas as pd


def calc_monthly_average_per_decade(df):
    """Calculate monthly average for each decade"""
    # find decade
    df["decade"] = df["year"].astype("str").str[:3]

    # group
    df_monthly = df.drop(["year", "is_predicted"], axis=1)
    df_monthly = (
        df_monthly[["decade", "month", "tmax_degC"]]
        .groupby(["decade", "month"])
        .mean()
        .reset_index()
    )
    df_pivoted = df_monthly.pivot(index="month", columns="decade", values="tmax_degC")

    return df_pivoted
