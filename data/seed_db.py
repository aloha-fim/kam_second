# Import csv to postgresql db

import psycopg2
import pandas as pd

# Update with your user name
conn = psycopg2.connect("host=localhost dbname=kam_users_db user=postgres")
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

df_users = pd.read_csv('./data/predefined_users.csv', index_col=0)
for idx, u in df_users.iterrows():
    # Data cleaning

    q = cur.execute(
        '''INSERT INTO kam_users (category, rang, full_name, age_year, location, total_time, run_link, run_year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)''',
        (u.category, u.rang, u.full_name, u.age_year, u.location, u.total_time, u.run_link, u.run_year)
    )
    conn.commit()

cur.close()
conn.close()