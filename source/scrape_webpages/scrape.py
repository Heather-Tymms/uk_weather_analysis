"""functions that and set up overall location data."""

import os
from pathlib import Path

import pandas as pd

# column names
weather_data_headers = {
    "year": pd.Int64Dtype(),
    "month": pd.Int64Dtype(),
    "tmax_degC": pd.Float64Dtype(),
    "tmin_degC": pd.Float64Dtype(),
    "af_days": pd.Float64Dtype(),
    "rain_mm": pd.Float64Dtype(),
    "sun_hours": pd.Float64Dtype(),
    "is_predicted": bool,
}

# file paths and names
input_filepath = Path.cwd().parent / "input"


def read_location_page(
    location_name: str, location_url: str, refresh: bool = False
) -> pd.DataFrame:
    """Read specific txt  file on a web page."""
    location_filepath = None

    # check if file already exists in input folder
    location_file = [
        c
        for c in os.listdir(input_filepath)
        if c.endswith(".txt")  # is a text file
        and c.startswith(location_name.title())  # is the correct location name
    ]

    # if file exists and refresh is False, use the file in input folder.
    if not refresh and len(location_file) > 0:
        location_filepath = input_filepath / location_file[0]

    # choose the data location based on whether we have a file path or a URL
    data_location = location_filepath or location_url

    # read the data into a pandas dataframe
    df = pd.read_csv(
        data_location,
        sep=r"\s+",
        skiprows=7,
        names=weather_data_headers,
        na_values=["---"],
    )
    return df
