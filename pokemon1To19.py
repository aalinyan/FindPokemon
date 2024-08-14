import requests

pokemon_list = []

for i in range(1, 20):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    pokemon = response.json()
    
    name = pokemon['name']
    types = [t['type']['name'] for t in pokemon['types']]
    
    pokemon_list.append({'id': i, 'name': name, 'types': types})

for p in pokemon_list:
    print(f"ID: {p['id']}, Name: {p['name']}, Types: {', '.join(p['types'])}")