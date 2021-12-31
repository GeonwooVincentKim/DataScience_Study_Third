import json
import json2xml
import xml


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


# Write `JSON` Data (file)
with open("json_data.txt", "w") as json_file:
    json.dump(serialized, json_file)

# Get `JSON` data and write `XML` file

