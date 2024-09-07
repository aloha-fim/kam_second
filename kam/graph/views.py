import plotly.express as px
import pandas as pd

data = pd.read_csv("./data/life_expectancy_years.csv")

long_df = px.data.medals_long()

fig = px.bar(long_df, x="country", y="count", color="medal", title="Long-Form Input")
fig.show()