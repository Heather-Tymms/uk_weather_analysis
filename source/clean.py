# functions that clean the datasets
from typing import TYPE_CHECKING

import pandas as pd

from source.scrape_webpages.scrape import read_location_page, weather_data_headers

if TYPE_CHECKING:
    from source.location_info.location import Location


def create_table(location_url: str) -> pd.DataFrame:
    """Clean file and outputs a df with the data."""

    df = read_location_page(location_url=location_url)

    # clean columns
    float_headers = [ c for c in weather_data_headers if c != "is_predicted"]
    for c in float_headers:
        # replace anything thats not digit, white space or fill stop
        df[c] = df[c].replace("\*", "",regex=True)

        # sort out data types
        if c in ["month","year"]:
            df[c] = df[c].astype("int")
        else:
            df[c] = df[c].astype("float")

    # clean "is_predicted" column
    df.loc[df["is_predicted"].notnull(),"is_predicted"] = True
    df.loc[df["is_predicted"].isnull(),"is_predicted"] = False

    # find decade
    df["decade"] = int(df["year"].astype("str").str[:3] + "0")

    return df
