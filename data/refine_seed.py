import pandas as pd


df = pd.read_csv('predefined_users.csv')

############# segment age group #####################
#df = pd.DataFrame(data, columns=['age_year'])
bins = [0, 20, 31, 41, 51, 150]
group = ['<20', '21-30', '31-40', '41-50', '>50']
df['age_group'] = pd.cut(df['age_year'], bins=bins, labels=group, right=False).cat.add_categories('missing').fillna('missing')

############# regex df ##############################
df['total_time'] = df['total_time'].str.split(',').str[0]
#df['total_time'].str.extract(r"(\w+)(?=\,)")

df.to_csv('postdefined_users.csv')


