# functions that clean the datasets

import pandas as pd

from source.location import Location
from source.scrape import read_location_page


def create_table(location: Location) -> pd.DataFrame:
    """Clean file and outputs a df with the data."""
    df = read_location_page(location_name=location)

    return df
