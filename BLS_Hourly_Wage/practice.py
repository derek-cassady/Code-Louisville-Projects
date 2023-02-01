import json
import csv

with open ('C:\\Users\\Derek\\Desktop\\Code_Louisville\\Project\\JSON.json', 'r') as f:
    json_data = json.load(f)

for series in json_data['Results']['series']:

    for item in ['series'][0]:
        #year = item['year']
        #period = item['period']
        #month = item['periodName']
        #value = item['value']

        print(item)


