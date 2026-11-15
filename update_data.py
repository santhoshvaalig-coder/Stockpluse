import os
import requests

API_KEY = os.getenv('API_KEY')
SYMBOLS = ['RELIANCE', 'NVDA', 'TATAMOTORS', 'AAPL']
DATA = {}

for symbol in SYMBOLS:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    DATA[symbol] = response.json()

print(DATA)
# Add logic to update index.html here
