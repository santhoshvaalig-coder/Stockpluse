import os
import requests

API_KEY = os.getenv('API_KEY')
SYMBOLS = {
    'RELIANCE': '₹1,250.00',
    'NVDA': '$140.00',
    'TATAMOTORS': '₹950.00',
    'AAPL': '$225.00'
}

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

for symbol, default_price in SYMBOLS.items():
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    try:
        price = data['Global Quote']['05. price']
        if symbol in ['RELIANCE', 'TATAMOTORS']:
            price_formatted = f'₹{float(price):,.2f}'
        else:
            price_formatted = f'${float(price):,.2f}'
        html_content = html_content.replace(default_price, price_formatted)
        print(f"Updated {symbol} to {price_formatted}")
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error fetching data for {symbol}: {e}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Index.html updated successfully.")
