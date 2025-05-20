import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '95af0591e7f27814597680f8a201d780'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRENER_ID = '33802'

def test_stus_code():
    response = requests.get(url=f'{URL}/pokemons', params={'trener_id' : TRENER_ID})
    assert response.status_code == 200