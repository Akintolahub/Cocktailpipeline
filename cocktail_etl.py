import requests
import json


url = 'https://www.thecocktaildb.com/api/json/v1/1/random.php'
r = requests.get(url)

randomCocktail = r.json()    

name = randomCocktail["drinks"][0]["strDrink"]
glass = randomCocktail["drinks"][0]["strGlass"]
instructions = randomCocktail["drinks"][0]["strInstructions"]
cocktail = []
ingredients_list = []

#test ingredients with id 11164
def ingredients(cocktail):
    for drink in randomCocktail.get("drinks", []):
        for i in range(1, 16):  # Assuming the ingredients are numbered from 1 to 15
            ingredient_key = f"strIngredient{i}"
            ingredient_value = drink.get(ingredient_key)

            if ingredient_value is not None:
                measure_key = f"strMeasure{i}"
                measure_value = drink.get(measure_key, "")
                ing = {
                    ingredient_value : measure_value
                }
                print(ing)
                # print(f"{ingredient_value}: {measure_value}")
        
ingredients(randomCocktail)
# ingredients_list.append(ingredients(randomCocktail))

# cocktail_info = {
#     "Cocktail" : name,
#     "Ingredients" : ingredients_list,
#     "Glass" : glass,
#     "Instructions" : instructions
# }

# cocktail.append(cocktail_info)

# print(ingredients_list) 