import requests

URL:str = "https://api.coingecko.com/api/v3/simple/price"

PARAMS:str = {'ids':'ethereum','vs_currencies':'usd'}

r:requests.Response = requests.get(url = URL, params = PARAMS)

data:dict = r.json()

print(data["ethereum"]["usd"])