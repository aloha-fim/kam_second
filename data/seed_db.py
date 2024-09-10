# Import csv to postgresql db

import psycopg2
import pandas as pd
from dotenv import load_dotenv
from os import environ


# Load environment
load_dotenv('.env')


# Update with your user name
conn = psycopg2.connect("host=dpg-crgcigrv2p9s73ab12ng-a dbname=kamuno_postgresql user=kamuno_postgresql_user password=2DNIRs5rTKyWAWXmIO6GIUz97Kt9NxJl")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS kam_users;')

cur.execute('''CREATE TABLE kam_users (
    id SERIAL PRIMARY KEY NOT NULL,
    category TEXT NOT NULL,
    rang TEXT NOT NULL,
    full_name TEXT NOT NULL,
    age_year INTEGER NOT NULL,
    location TEXT NOT NULL,
    total_time TIMESTAMP NOT NULL,
    run_link TEXT NOT NULL,
    run_year INTEGER NOT NULL);''')

conn.commit()

df_users = pd.read_csv('predefined_users_combined.csv', index_col=0, encoding = "ISO-8859-1")

############# regex df ##############################
df_users['total_time'] = df_users['total_time'].str.split(',').str[0]
#df_users['total_time'].str.extract(r"(\w+)(?=\,)")

# format to timestamp
df_users['total_time'] = df_users['total_time'].str.replace('.',':')

# format DQ to dummy variable
#df_users['total_time'] = df_users['total_time'].str.replace('-----','00:00:01,1')

for idx, u in df_users.iterrows():
    # Data cleaning

    q = cur.execute(
        '''INSERT INTO kam_users (category, rang, full_name, age_year, location, total_time, run_link, run_year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',
        (u.category, u.rang, u.full_name, u.original_age_year, u.location, u.total_time, u.run_link, u.run_year)
    )
    conn.commit()

cur.close()
conn.close()