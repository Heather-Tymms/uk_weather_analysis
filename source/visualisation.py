"""Visualisations from the data."""  #

import pandas as pd
import seaborn as sns


def create_line_graph(df: pd.DataFrame, col_x_name: str, col_y_name: str):
    """Plots a visualisation with col x and col y."""

    sns.lineplot(data=df, x=col_x_name, y=col_y_name)

    pass
