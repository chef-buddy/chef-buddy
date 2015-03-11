import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)
app_id = '83d3feb6'
app_key = '9d5fcbd449d2f85767d52da8a2479246'

data = requests.get('https://api.edamam.com/search',
                    params={'q': 'chicken', 'count': 1},
                    auth=(app_id, app_key))
data = data.json()

pp.pprint(data['hits'])
