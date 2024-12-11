# Main running script

from source.clean import create_table
from source.location import Location

# from source.scrape import scrape_location_data, url_overview

# this line only needs to be used once to populate the webpage table urls
# data = scrape_location_data(url_overview)


# create table
Location()
create_table(location=Location.CAMBRIDGE_NIAB)
