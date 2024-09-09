import pandas as pd


df = pd.read_csv('predefined_users_combined.csv', index_col=0, encoding = "ISO-8859-1")

############# segment age group #####################
#df = pd.DataFrame(data, columns=['age_year'])

df['age_year'] = df['run_year'] - df['original_age_year']

bins = [0, 20, 31, 41, 51, 150]
group = ['<20', '21-30', '31-40', '41-50', '>50']
df['age_group'] = pd.cut(df['age_year'], bins=bins, labels=group, right=False).cat.add_categories('missing').fillna('missing')


df.to_csv('postdefined_users.csv')


