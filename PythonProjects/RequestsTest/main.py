import requests

URL='https://api.pokemonbattle.me'
TOKEN='6716d1f23065160d6988e0e4984ef267'
HEADERS={'Content-Type':'application/json', 'trainer_token':TOKEN}

body={
    "name": "generate",
    "photo": "generate"
}

responce=requests.post(url= f'{URL}/pokemons', headers= HEADERS, json=body)

print(responce.text)

body1={
    "pokemon_id": "14499",
    "name": "ASDs",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
responce1=requests.put(url= f'{URL}/pokemons', headers= HEADERS, json=body1)

print(responce1.text)

body2={
    "pokemon_id": "14499"

}
responce2=requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADERS, json=body2)

print(responce2.text)
