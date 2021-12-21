import sys, re
import os
import csv

from bs4 import BeautifulSoup
import requests

sys.path.append(os.path.join(os.path.dirname(os.path.join(os.path.dirname(__file__)))))

# from File.FileManager import *

# regex = sys.argv[0]

# for line in sys.stdin:
#     if re.search(regex, line):
#         sys.stdout.write(line)

# count = 0
# for line in sys.stdin:
#     count += 1

# print(count)

# a = input()

# for i in range(a):
#     b, c = map(int, input().split(" "))
#     print("Case: #{0}: {1}".format((i + 1), b + c))

print("Tab Delimited Stock Price")


def process(date, symbol, price):
    print(date, symbol, price)


with open("tab_delimited_stock_prices.txt", 'r', encoding='utf8',newline='') as f:
    tab_reader = csv.reader(f, delimiter="\t")
    print("Tab Reader -> {0}".format(tab_reader))

    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])

        process(date, symbol, closing_price)

print()

with open("colon_delimited_stock_prices.txt", "r", encoding='utf8', newline='') as f:
    colon_reader = csv.DictReader(f, delimiter=':')
    print("Colon Delimited -> {0}".format(colon_reader))

    for dict_row in colon_reader:
        date = dict_row["date"]
        symbol = dict_row["symbol"]
        closing_price = float(dict_row["closing_price"])
        
        process(date, symbol, closing_price)

print()

todays_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

for price in todays_prices:
    print(price)


with open("comma_delimited_stock_prices.txt", 'w', encoding="utf8", newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    print("CSV-Writer -> {0}".format(csv_writer))

    for stock, price in todays_prices.items():
        csv_writer.writerow([stock, price])


url = (
    "https://raw.githubsercontent.com/"
    "joelgrus/data/master/getting-data.html"
)
print("URL -> {0}".format(url))

html = requests.get(url).text
print("HTML -> {0}".format(html))

soup = BeautifulSoup(html, "html5lib")
print("Soup -> {0}".format(soup))

first_paragraph = soup.find("p")
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

print("First Paragraph -> {0}".format(first_paragraph))
