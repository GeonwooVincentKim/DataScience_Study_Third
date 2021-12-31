import json
import json2xml
import xml

import requests
from collections import Counter
from dateutil.parser import  parse


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
with open("json_data.json", "w") as json_file:
    json.dump(serialized, json_file)


github_user = "GeonwooVincentKim"
endpoint = f"https://api.github.com/users/{github_user}/repos"

repos = json.loads(requests.get(endpoint).text)
print("Github Repositories -> {0}".format(repos))

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

print("\n\n---------------------------------\n\n")
print("Dates -> {0}\nMonth-Counts -> {1}\nWeekday-Counts -> {2}".format(dates, month_counts, weekday_counts))


last_5_repositories = sorted(
    repos,
    key=lambda r: r["pushed_at"],
    reverse=True
)[:5]

last_5_repositories = [
    repo["language"]
    for repo in last_5_repositories
]

print("\n------------------------------------------\n")
print("Last 5 Repositories in Github -> {0}".format(last_5_repositories))
