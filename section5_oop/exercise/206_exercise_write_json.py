import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


with open('206_json.json', 'w') as file:
    person = Person('John', 28)
    person1 = Person('Mary', 24)
    person_list = [person.__dict__, vars(person1)]
    # If we try to make dump of person as class it will raise an exception
    # json.dump(person, file, ensure_ascii=False, indent=2) # TypeError: Object of type Person is not JSON serializable
    # To resolve that, we will convert Person to a dict using vars() or __dict__
    json.dump(person_list, file, ensure_ascii=False, indent=2)