import json
js = '''hiofsvfsvfsvfbj{
  "name": "Barsik",
  "age": 7,
  "meals": [
    "Wiskas",
    "Royal Canin",
    "Purina",
    "Hills",
    "Brit Care"
  ]
}'''
with open('cats.json') as file:
    data = json.load(file)
    d2 = json.loads(js)
    print(data)
    print(d2)