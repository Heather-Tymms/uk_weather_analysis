"""Visualisations from the data."""  #

from typing import Any, Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def create_min_max_graph(
    df: pd.DataFrame,
    ax: plt.Axes,
    col_x: Optional[Any] = None,
    col_y: Optional[Any] = None,
) -> plt.Axes:
    """Plots a graph with col x and col y."""

    # filter to correct month
    cols = [c for c in df.columns if c[1] == col_y]
    df = df[cols]
    df.columns = pd.Index([e[0] for e in df.columns.tolist()])

    # plot the data
    sns.lineplot(data=df, ax=ax)

    return ax


def create_line_graph(
    df: pd.DataFrame,
    col_x: Optional[Any] = None,
    col_y: Optional[Any] = None,
    is_min_max: bool = False,
    title: str = None,
):
    """Plots a graph with col x and col y."""
    sns.set()

    fig, ax = plt.subplots(figsize=(12, 6))
    if is_min_max:
        # filter and plot the columns to one month
        ax = create_min_max_graph(df, ax, col_x, col_y)

    elif not col_y:
        sns.lineplot(data=df, ax=ax)
    else:
        sns.lineplot(data=df, x=col_x, y=col_y, ax=ax)

    if title:
        ax.set_title(title)

    pass
