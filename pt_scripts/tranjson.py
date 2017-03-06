import json
import pandas as pd

with open('data-graduates/Introduction_01/data/countries.json') as data_file:

	data=json.load(data_file)


keys = data[0].keys()

df = pd.DataFrame(columns = keys)

for i in data:
	for k in i:

		print(value)
