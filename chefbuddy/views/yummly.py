import json
import requests
import pprint


app_id = '83d3feb6'
app_key = '9d5fcbd449d2f85767d52da8a2479246'


data = requests.get('http://api.yummly.com/v1/api/recipes', auth=(app_id, app_key))
data = data.json()

pp = pprint.PrettyPrinter(indent=4)
# print(data.get('hits'))
pp.pprint(data)
