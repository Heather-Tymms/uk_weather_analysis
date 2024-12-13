# functions that clean the datasets
from typing import TYPE_CHECKING

import pandas as pd

from source.scrape_webpages.scrape import read_location_page

if TYPE_CHECKING:
    from source.location import Location


def create_table(location: "Location") -> pd.DataFrame:
    """Clean file and outputs a df with the data."""
    df = read_location_page(location_name=location)

    # ensure column types are correct

    return df
