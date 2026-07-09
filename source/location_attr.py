"""Location attributes."""

from pathlib import Path
from typing import TYPE_CHECKING, Literal

import pandas as pd

if TYPE_CHECKING:
    from typing import Any, Self

    from source.location import Location

location_filename = "location_webpages"
input_location_filepath = Path.cwd().parent / "input" / f"{location_filename}.csv"


class LocationAttributes:
    """Attributes of a location."""

    country = "United Kingdom"
    df = pd.DataFrame()
    filepath = ""

    def __init__(self: "Self", location: "Location") -> None:
        """Initialise instance."""

        # attributes
        self.name = location.value
        self.url = self.find_location_attribute(location.value, "url")
        self.position = self.find_location_attribute(location.value, "co-ordinates")

    def find_location_attribute(
        self: "Self",
        location_name: str,
        location_attribute: Literal["url", "coordinates"],
    ) -> "Any":
        """Find location attribute from name and attribute name."""

        # find what column in the table to look for
        column_connection = {"url": "Data", "co-ordinates": "Location"}
        column_name = column_connection[location_attribute]

        # find df
        df = pd.read_csv(input_location_filepath)

        # In this df, there should only be one row per location name.
        # If there is more than one row, raise an error. If there is no row, raise an error.

        # Find answer from table
        output = df.loc[
            df["Name"].str.upper().str.replace("-", "_").str.replace(" ", "_")
            == location_name,
            column_name,
        ]
        # correct number of rows in output
        if len(output) == 1:
            return output.iloc[0]

        # incorrect number of rows in the output
        if len(output) > 1:
            error_message = (
                f"There are more than one name with {location_name}."
                "Please check the names in the Location Class."
            )

        if len(output) == 0:
            error_message = (
                f"There are no names found like {location_name}. "
                "Please check the names in the Location Class."
            )

        raise ValueError(error_message)
