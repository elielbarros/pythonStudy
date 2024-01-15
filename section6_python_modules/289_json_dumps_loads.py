import json
from pprint import pprint
from typing import TypedDict


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None


string_json = """
{
"title": "O Senhor dos Aneis: A sociedade do Anel",
"original_title": "The Lord of the Rings: The Fellowship of the Ring",
"is_movie": true,
"imdb_rating": 8.8,
"year": 2001,
"characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
"budget": null
}"""

movie: Movie = json.loads(string_json)

pprint(movie, width=40)

print()
print(type(movie))  # output: <class 'dict'>

print(movie["original_title"])  # output: The Lord of the Rings: The Fellowship of the Ring

string_json_from_dump = json.dumps(movie, ensure_ascii=False, indent=2)
print(type(string_json_from_dump), string_json_from_dump)
