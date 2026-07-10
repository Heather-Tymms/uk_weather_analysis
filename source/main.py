"""Run the main program to scrape the table of weather data required to run the notebooks."""

from source.scrape_webpages.scrape_overview import (
    input_location_filepath,
    scrape_overview_location_data,
    url_overview,
)

# check if we have already scraped the data, if not scrape it and save to csv
if not input_location_filepath.exists():
    data = scrape_overview_location_data(url_overview)
