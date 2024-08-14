import requests

url = "https://pokeapi.co/api/v2/pokemon/6"

response = requests.get(url)
pokemon = response.json()

print(f"Id 6 pokemon: {pokemon['name']}")