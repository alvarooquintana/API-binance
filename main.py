from binance.client import Client
from pprint import pprint
from binance.enums import *
from password import *
client = Client(api_key,secret_key)


prices = client.get_all_tickers()
print(prices)



