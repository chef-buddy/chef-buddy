import requests
import pprint


pp = pprint.PrettyPrinter(indent=4)
api_key = '501a6ebe4bb5eb6de9d5faffd1e04a17'

# Run this to get all recipes
all_recipes = requests.get('http://food2fork.com/api/search', params={'key':api_key})
all_recipes = all_recipes.json()

for recipe in all_recipes['recipes']:
    recipe_get = requests.get('http://food2fork.com/api/get', params={'key':api_key,'rId':recipe['recipe_id']})
    pp.pprint(recipe_get.json())
