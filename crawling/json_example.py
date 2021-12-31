import json

serialized = """{
    "title": "Data Science Book",
    "author": "Joel Grus",
    "publicationYear": 2019,
    "topics": ["data", "science", "data science"]
}"""

deserialized = json.loads(serialized)
print("Deserialized -> {0}".format(deserialized))
print("Deserialized Publication-Year -> {0}".format(deserialized["publicationYear"]))
print("Deserialized Topics -> {0}".format("data science" in deserialized["topics"]))
