# functions that clean the datasets
import pandas as pd
from scrape_webpages.scrape import read_location_page, weather_data_headers


def create_decade_column(df: pd.DataFrame) -> pd.Series:
    """Create a decade column from the year column."""

    df["decade"] = df["year"].astype("str").str[:3] + "0"

    return df["decade"].astype("int")


def create_worded_month_column(df: pd.DataFrame) -> pd.Series:
    """Create a worded month column from the month column."""

    df["worded_month"] = pd.to_datetime(df["month"], format="%m").dt.month_name()

    return df["worded_month"]


def create_table(
    location_name: str, location_url: str, data_refresh: bool = False
) -> pd.DataFrame:
    """Clean file and outputs a df with the data."""

    df = read_location_page(
        location_name=location_name, location_url=location_url, refresh=data_refresh
    )

    # clean columns
    float_headers = [c for c in weather_data_headers.keys() if c != "is_predicted"]
    for c in float_headers:
        # replace * or # with empty string
        df[c] = df[c].replace(r"(\*)|(\#)", "", regex=True)

        # Ensure dtype is correct
        df[c] = df[c].astype(weather_data_headers[c])

    # clean "is_predicted" column
    df.loc[df["is_predicted"].notnull(), "is_predicted"] = True
    df.loc[df["is_predicted"].isnull(), "is_predicted"] = False

    # find decade
    df["decade"] = create_decade_column(df)

    # find worded month
    df["worded_month"] = create_worded_month_column(df)

    return df
