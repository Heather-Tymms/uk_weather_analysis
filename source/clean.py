# functions that clean the datasets
import pandas as pd
from scrape_webpages.scrape import read_location_page, weather_data_headers


def create_table(location_url: str) -> pd.DataFrame:
    """Clean file and outputs a df with the data."""

    df = read_location_page(location_url=location_url)

    # clean columns
    float_headers = [c for c in weather_data_headers.keys() if c != "is_predicted"]
    for c in float_headers:
        # replace anything thats not digit, white space or fill stop
        df[c] = df[c].replace(r"(\*)|(\#)", "", regex=True)

        # Ensure dtype is correct
        df[c] = df[c].astype(weather_data_headers[c])

    # clean "is_predicted" column
    df.loc[df["is_predicted"].notnull(), "is_predicted"] = True
    df.loc[df["is_predicted"].isnull(), "is_predicted"] = False

    # find decade
    df["decade"] = df["year"].astype("str").str[:3] + "0"
    df["decade"] = df["decade"].astype(weather_data_headers["year"])

    df["worded_month"] = pd.to_datetime(df["month"], format="%m").dt.month_name()

    return df
