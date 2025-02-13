import requests

url = "https://api.nobitex.ir/v3/orderbook/USDTIRT"
response = requests.get(url)
data = response.json()
usdt_price = data['lastTradePrice']
print(usdt_price)
