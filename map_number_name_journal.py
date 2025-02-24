import json

with open('./data/data.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

for obj in data: 
    if obj['journal'] == "19":
        obj['journal'] = 'ADED'
    elif obj['journal'] == "36":
        obj['journal'] = 'revistaenfermagem'

with open('./data/data.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
