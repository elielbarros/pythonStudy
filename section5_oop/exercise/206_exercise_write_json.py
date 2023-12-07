import json

person = {
    'name': 'John',
    'age': 28,
}

with open('206_json.json', 'w') as file:
    json.dump(person, file, ensure_ascii=False, indent=2)