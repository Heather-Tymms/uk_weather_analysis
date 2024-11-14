# Main running script

from source.clean import create_table
from source.calculation import calc_monthly_average_per_decade

heathrow_filename = "Heathrow London Airport.txt"

df_heatherow = create_table(heathrow_filename)

heathrow_decade_monthly_avg = calc_monthly_average_per_decade(df_heatherow)