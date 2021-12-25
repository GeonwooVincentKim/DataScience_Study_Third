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
