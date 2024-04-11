import requests
import pytest

URL='https://api.pokemonbattle.me'
TOKEN='6716d1f23065160d6988e0e4984ef267'
HEADERS={'Content-Type':'application/json', 'trainer_token':TOKEN}

def test_status_code():
    responce=requests.get(url= f'{URL}/pokemons')
    assert responce.status_code ==200
    
def test_user():
    responce1=requests.get(url= f'{URL}/trainers', params={"trainer_id": 2082})  
    assert responce1.json()['id'] =='2082'