import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '95af0591e7f27814597680f8a201d780'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_creatpokemons = {
    "name": "Бульба",
    "photo_id": 15
}
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creatpokemons)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_name ={
    "pokemon_id": "320001",
    "name": "Капи",
    "photo_id": 20
}
response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

body_addpokeball = {
    "pokemon_id": "320001"
}
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(response_add.text)
