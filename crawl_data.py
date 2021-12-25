from bs4 import BeautifulSoup
import requests


url = "https://www.house.gov/representatives"
text = requests.get(url).text

print("Get URL Text -> {0}".format(text))
