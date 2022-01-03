import datetime
from collections import namedtuple

# Using Dictionary-Style
# It could occurs lots of error by mistype the variable or some codes
print("<Use Dictionary only>")
stock_price = {
    'closing_price': 102.06,
    'date': datetime.date(2014, 8, 29),
    'symbol': 'AAPL'
}

for price in stock_price:
    print("Info -> {0}".format(price))

print("\n--------------------\n")
print("<Use Named-Tuple>")

StockPrice = namedtuple('StockPrice', ['symbol', 'date', 'closing_price'])
price = StockPrice('MSFT', datetime.date(2018, 12, 14), 106.03)

print("Price - Symbol -> {0}".format(price.symbol))
print("Price - Closing-Price -> {0}".format(price.closing_price))
