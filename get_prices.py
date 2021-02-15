from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '2e784906-1ed8-4f00-a195-792d3957f69c',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)['data']
    coins = {coin['slug']: coin['quote'] for coin in data}
    with open("output.json", 'w') as fs:
        json.dump(coins, fs)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
