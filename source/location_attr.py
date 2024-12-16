"""Location attributes."""

from typing import TYPE_CHECKING, Literal

import pandas as pd

from source.scrape_webpages.scrape import input_location_filepath

if TYPE_CHECKING:
    from .location import Location
    from typing import Any, Self


class LocationAttributes():
    country = "England"

    def __init__(self:"Self", location:"Location")-> None:
        """Initialise instance."""

        # attributes
        self.name = location.value
        self.url = self.find_location_attribute(location.value, "url")
        self.position = self.find_location_attribute(location.value, "co-ordinates")


    def find_location_attribute(
            self:"Self",
            name: str,
            location_attribute: Literal["url","coordinates"]
        ) -> "Any":
        """Find location attribute from name and attribute name."""

        # find what column in the table to look for
        column_connection = {"url":"Data","co-ordinates":"Location"}
        column_name = column_connection[location_attribute]

        # find df
        df = pd.read_csv(input_location_filepath)

        # Find answer from table
        output = df.loc[
            df["Name"].str.upper().str.replace("-", "_").str.replace("\s", "_", regex=True)
            == name,
            column_name,
        ]
        # correct number of rows in output
        if len(output) == 1:
            return output.iloc[0]

        # incorrect number of rows in the output
        if len(output) > 1:
            error_message = f"There are more than one name with {name}. Please check the names in the Location Class"

        if len(output) == 0:
            error_message = f"There are no names found like {name}. Please check the names in the Location Class"

        raise ValueError(error_message)