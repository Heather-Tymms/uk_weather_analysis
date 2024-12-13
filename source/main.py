# Main running script

from source.calculation import calc_monthly_average_per_decade
from source.clean import create_table
from source.location import Location
from source.visualisation import create_line_graph

# from source.scrape import scrape_location_data, url_overview

# this line only needs to be used once to populate the webpage table urls
# data = scrape_location_data(url_overview)


# create table
df_camb = create_table(location=Location.CAMBRIDGE_NIAB)
df_avg_month_by_decade = calc_monthly_average_per_decade(df_camb)
create_line_graph(
    df_avg_month_by_decade,
)
