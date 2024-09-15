import plotly.express as px


import pandas as pd

df = pd.read_csv('postdefined_users_gpt.csv')



fig = px.histogram(df, x='run_year', color="age_group")
fig.update_xaxes(type='category')

fig.show()