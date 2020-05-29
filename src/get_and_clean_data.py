'''
This module fetches newest COVID-19 data from the CSSEGI and cleans it for use
in a Metabase Dashboard.
'''
import os
import warnings
import pandas as pd
import wget
import numpy as np


path = os.path.abspath(os.getcwd())
warnings.simplefilter(action='ignore', category=FutureWarning)
print(path)
try:
    # if previous files exist, deleting them first
    os.remove(path+'/data/raw/time_series_covid19_confirmed_global.csv')
    os.remove(path+'/data/raw/time_series_covid19_deaths_global.csv')

finally:
    # fetching newest data
    urls = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
            'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv']
    for url in urls:
        filename = wget.download(url, out=path+"/data/raw")

    # reading and mangling data
    conf_df = pd.read_csv(path+'/data/raw/time_series_covid19_confirmed_global.csv')
    deaths_df = pd.read_csv(path+'/data/raw/time_series_covid19_deaths_global.csv')
    dates = conf_df.columns[4:]
    conf_df_long = conf_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Confirmed')
    deaths_df_long = deaths_df.melt(id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], value_vars=dates, var_name='Date', value_name='Deaths')
    full_table = pd.concat([conf_df_long, deaths_df_long['Deaths']], axis=1, sort=False)
    full_table = full_table[full_table['Province/State'].str.contains(',') != True]

    # Replacements of names for easier matching with countries_mapping.csv in Metabase.
    full_table['Country/Region'] = full_table['Country/Region'].replace('US', 'United States')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Vietnam', 'Viet Nam')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Iran', 'Iran, Islamic Republic of')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Korea, South', 'Korea, Republic of')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Moldava', 'Moldava, Republic of')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Russia', 'Russian Federation')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Taiwan*', 'Taiwan, Province of China')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Venezuela', 'Venezuela, Bolivarian Republic of')
    full_table['Country/Region'] = full_table['Country/Region'].replace('North Macedonia', 'Macedonia, the Former Yugoslav Republic of')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Czechia', 'Czech Republic')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Brunei', 'Brunei Darussalam')
    full_table['Country/Region'] = full_table['Country/Region'].replace('Bolivia', 'Bolivia, Plurinational State of')

    full_table.rename(columns={"Province/State": "Province", "Country/Region": "Country"}, inplace=True)

    # calculating mortality rate and dividing data into files with data on
    # a country-level, and data on a regional-level.
    full_table["Mortality_rate"] = (full_table['Deaths']/full_table['Confirmed'])
    full_table_country = full_table.groupby(['Country', "Date"])['Lat', 'Long', 'Confirmed', 'Deaths'].sum().reset_index()
    full_table_country["Mortality_rate"] = (full_table_country['Deaths']/full_table_country['Confirmed'])
    full_table_country.loc[~np.isfinite(full_table_country['Mortality_rate']), 'Mortality_rate'] = np.nan
    full_table.loc[~np.isfinite(full_table['Mortality_rate']), 'Mortality_rate'] = np.nan
    full_table_country["Mortality_rate"] = full_table_country["Mortality_rate"].fillna(0)
    full_table["Mortality_rate"] = full_table["Mortality_rate"].fillna(0)

    # in case of negative values, set to zero
    full_table_country["Deaths"] = full_table_country["Deaths"].clip(lower=0)
    full_table_country["Confirmed"] = full_table_country["Confirmed"].clip(lower=0)

    # output cleaned csvs
    full_table.to_csv(path+'/data/processed/covid_19_clean_complete_region.csv', index=False)
    full_table_country.to_csv(path+'/data/processed/covid_19_clean_complete_country.csv', index=False)

print("\nThe CSV's have been updated.")
