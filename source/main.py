# Main running script

from source.calculation import calc_monthly_attribute_per_decade, calc_min_max_per_decade
from source.clean import create_table
from source.location import Location
from source.location_attr import LocationAttributes
from source.visualisation import create_line_graph

# from source.scrape import scrape_location_data, url_overview

# this line only needs to be used once to populate the webpage table urls
# data = scrape_location_data(url_overview)


# create table
cambridge = LocationAttributes(location=Location.CAMBRIDGE_NIAB)
df_camb = create_table(location_url=cambridge.url)

# clean calculate for visualisation 
df_avg_month_by_decade = calc_monthly_attribute_per_decade(df_camb, "tmax_degC")
df_min_max_camb = calc_min_max_per_decade(df_camb)

# visualisation
create_line_graph(
    df_avg_month_by_decade,
)
