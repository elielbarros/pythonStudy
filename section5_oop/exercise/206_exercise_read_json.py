import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person_list = []
with open('206_json.json', 'r') as file:
    person_list_dict = json.load(file)

    for person_dict in person_list_dict:
        person_list.append(Person(**person_dict))

for person in person_list:
    print(person.name, person.age)
