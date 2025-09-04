"""Visualisations from the data."""  #

import pandas as pd
import seaborn as sns


def create_line_graph(df: pd.DataFrame, col_x: str, col_y: str):
    """Plots a visualisation with col x and col y."""

    sns.lineplot(data=df, x=col_x, y=col_y)

    pass
