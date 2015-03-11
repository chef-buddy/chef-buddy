import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)
app_id = '2f20e297'
app_key = '0d63ae37825e03ca56ed19d7aa462dbb'

data = requests.get('https://api.edamam.com/search',
                    params={'q': 'chicken', 'to': 1},
                    auth=(app_id, app_key))
data = data.json()
pp.pprint(data['hits'])

for recipe in data['hits']:
    pp.pprint('Title: {}'.format(recipe['recipe']['label']))
    pp.pprint('Image: {}'.format(recipe['recipe']['image']))
    pp.pprint('URL: {}'.format(recipe['recipe']['url']))
    pp.pprint('Cooking Time: {}'.format(recipe['recipe']['cookingTime']))
    pp.pprint('Prep Time: {}'.format(recipe['recipe']['prepTime']))
    pp.pprint('Cooking Level: {}'.format(recipe['recipe']['level']))
    pp.pprint('Rating: {}'.format(recipe['recipe']['rating']))
    pp.pprint('Health Labels: {}'.format(recipe['recipe']['healthLabels']))

    ingredients = [ingredient['exactFood'] for ingredient in recipe['recipe']['ingredients']]
    pp.pprint('Ingredients: {}'.format(ingredients))

