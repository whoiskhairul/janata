import json
f = open('stock_market_data.json')
data = json.load(f)
data = json.dumps(data)
print(type(data))