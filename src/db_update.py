'''
This module reads the cleaned csv and writes the data into a database.
Make sure to provide a "DB_STRING" environment variable in the format
"mysql://username:password@host/dbname".
'''
import os
from sqlalchemy import create_engine, String, DateTime, Float, Integer
import pandas as pd

path = os.path.abspath(os.getcwd())
df = pd.read_csv(path+"/data/processed/covid_19_clean_complete_country.csv")

try:
    db_string = os.getenv("DB_STRING", "mysql://username:password@host/dbname")
    engine = create_engine(db_string)
    df.to_sql('corona_country', con=engine, index=False, if_exists='replace',
              dtype={"Country": String(),
                     "Date": DateTime(),
                     "Lat": Float(),
                     "Long": Float(),
                     "Confirmed": Integer(),
                     "Deaths": Integer(),
                     "Mortality_rate": Float()
                    }
             )
    print("Data has been written into the DB.")
except ModuleNotFoundError:
    print("Oops, seems like something went wrong with your environment variable!")
    print("Make sure you have a DB_STRING environment variable as following:")
    print("DB_STRING = mysql://username:password@host/dbname")
    