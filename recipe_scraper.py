import requests
from bs4 import BeautifulSoup

url = input("Enter recipe URL: ")
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

recipe_name = soup.find('h1').get_text()

ingredients = []
for ingredient in soup.find_all('li', class_='ingredient'):
    ingredients.append(ingredient.get_text())

instructions = []
for instruction in soup.find_all('li', class_='instruction'):
    instructions.append(instruction.get_text())

print("Recipe Name: ", recipe_name)
print("Ingredients: ", ingredients)
print("Instructions: ", instructions)
