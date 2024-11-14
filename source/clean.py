# functions that clean the datasets

import pandas as pd
from  pathlib import Path

headers = [
    "year", "month", "tmax_degC", "tmin_degC", "af_days", "rain_mm", "sun_hours", "is_predicted",
]

def full_path(input_file_name):
    """Find file path for input files."""
    path = Path.cwd() / "input"/ f"{input_file_name}"

    return path


def create_table(filename):
    """Clean file and outputs a df with the data."""
    file_path = full_path(filename)
    df = pd.read_csv(file_path, delim_whitespace=True, skiprows=7, names=headers, na_values=["---"])


    return df



