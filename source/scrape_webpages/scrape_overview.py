"""functions that and set up overall location data."""

from io import StringIO
from pathlib import Path
from typing import TYPE_CHECKING

import pandas as pd
import requests
from bs4 import BeautifulSoup

if TYPE_CHECKING:
    pass

url_overview = (
    "https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data"
)

# column names
location_col_names = ["Name", "Location", "Opened", "Data"]

# file paths and names
location_filename = "location_webpages"
input_filepath = Path.cwd() / "input"
input_location_filepath = input_filepath / f"{location_filename}.csv"


def scrape_overview_location_data(url: str) -> None:
    """Get overview table with location and webpages from website."""

    # check if input folder exists, if not create it
    if not input_filepath.exists():
        input_filepath.mkdir(parents=True, exist_ok=True)

    # check if we have already scraped the data, if not scrape it and save to csv
    if input_location_filepath.exists():
        return

    # web scraping - get request from webpage and locate table
    request = requests.get(url=url)
    souped = BeautifulSoup(request.content, "html.parser")
    table_of_names = souped.find(class_="table")

    # use pandas to read table in html format
    df = pd.read_html(StringIO(str(table_of_names)), extract_links="body")[0]

    # clean columns - grab required info from tuple
    # format (seen on the web page, url link behind the seen info or None)
    for c in [col for col in location_col_names if col != "Data"]:
        df[c] = df[c].str[0]

    # taking second from tuple because so we take link to data
    df["Data"] = df["Data"].str[1]

    # save information to csv
    df.to_csv(input_location_filepath, index=False)
