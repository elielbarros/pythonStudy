import json

with open('206_json.json', 'r') as file:
    person = json.load(file)
    print(person)