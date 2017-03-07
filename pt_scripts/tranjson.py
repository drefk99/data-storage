import json
import pandas as pd

with open('data-graduates/Introduction_01/data/countries.json') as data_file:

	data=json.load(data_file)


df = pd.DataFrame(data)

df_semi=df

for i in range(0, len(data)):

	df_semi['name'][i]=df['name'][i]['common']

csv_count = pd.read_csv('data-graduates/Introduction_01/data/countries.csv')

merge_count = pd.merge(csv_count, df_semi, on = 'name')
merge_count

	

		
