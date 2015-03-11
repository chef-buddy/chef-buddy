import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)
api_key = 'dvx5RsYxKUD7D205w6z7sOVNlcn7nXxT'

all_recipes = requests.get('http://api.bigoven.com/recipe/34',
                           params={'api_key':api_key},
                           headers={'content-type': 'application/json'})

pp.pprint(all_recipes.json())

# for recipe in all_recipes['recipes']:
#     recipe_get = requests.get('http://food2fork.com/api/get', params={'key':api_key,'rId':recipe['recipe_id']})
#     pp.pprint(recipe_get.json())