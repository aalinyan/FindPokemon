import requests

light_pokemon_list = []

for i in range(1, 100):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    pokemon = response.json()
    
    if pokemon['weight'] < 50:
        light_pokemon_list.append({'name': pokemon['name'], 'weight': pokemon['weight']})

light_pokemon_list = sorted(light_pokemon_list, key=lambda x: x['weight'], reverse=True)

for j in light_pokemon_list:
    print(f"Name: {j['name']}, Weight: {j['weight']}")