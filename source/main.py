"""Run the main program to scrape, clean, calculate and visualise the data."""

from source.calculation import (
    calc_monthly_attribute_per_decade,
    calc_min_max_per_decade,
)
from source.clean import create_table
from source.scrape_webpages.scrape import (
    input_location_Filepath,
    scrape_location_data,
    url_overview,
)
from source.scrape_webpages.location import Location
from source.scrape_webpages.location_attr import LocationAttributes
from source.visualisation import create_line_graph

# check if we have already scraped the data, if not scrape it and save to csv
if not input_location_Filepath.exists():
    data = scrape_location_data(url_overview)

# create table for cambridge niab location
cambridge = LocationAttributes(location=Location.CAMBRIDGE_NIAB)
df_camb = create_table(location_url=cambridge.url)

# clean calculate for visualisation
df_avg_month_by_decade = calc_monthly_attribute_per_decade(df_camb, "tmax_degC")
df_min_max_camb = calc_min_max_per_decade(df_camb)

# visualisation
create_line_graph(
    df_avg_month_by_decade,
)
