import re
from typing import Dict, Set

from bs4 import BeautifulSoup
import requests


url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

print("Get URL Text -> {0}".format(text))

all_urls = [
    a['href']
    for a in soup('a')
    if a.has_attr('href')
]

print(len(all_urls))
print("All URLs -> {0}".format(all_urls))

print("\n------------------------------------------------------\n")
regex = r"^https?://.*\.house\.gov/?$"
print("Regex Print Text -> {0}".format(regex))

print(re.match(regex, "http://joel.house.gov"))
print(re.match(regex, "https://joel.house.gov"))
print(re.match(regex, "http://joel.house.gov/"))
print(re.match(regex, "https://joel.house.gov/"))
print(re.match(regex, "joel.house.gov"))
print(re.match(regex, "http://joel.house.com"))
print(re.match(regex, "http://joel.house.com"))
print(re.match(regex, "https://joel.house.gov/biography"))

good_urls = [url for url in all_urls if re.match(regex, url)]
print(len(good_urls))
print("All Good URLs -> {0}".format(good_urls))

html = requests.get("https://jayapal.house.gov").text
soup = BeautifulSoup(html, "html5lib")

links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
print(links)
print("Entire Links -> {0}".format(links))


press_releases: Dict[str, Set[str]] = {}

# for house_url in good_urls:
#     html = requests.get(house_url).text
#     soup = BeautifulSoup(html, "html5lib")
#     pr_links = {a['href'] for a in soup('a') if 'press release' in a.text.lower()}

#     print(f"{house_url}: {pr_links}")
#     press_releases[house_url] = pr_links
#     print("Press Releases -> {0}".format(press_releases[house_url]))


def paragraph_mentions(text: str, keyword: str):
    soup = BeautifulSoup(text, "html5lib")
    paragraphs = [p.get_text() for p in soup('p')]

    return any(
        keyword.lower() in paragraph.lower()
        for paragraph in paragraphs
    )


text = """<body><h1>Facebook</h1><p>Twitter</p>"""
print(paragraph_mentions(text, "twitter"))
print(not paragraph_mentions(text, "facebook"))

