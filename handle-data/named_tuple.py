import datetime

# Using Dictionary-Style
# It could occurs lots of error by mistype the variable or some codes
stock_price = {
    'closing_price': 102.06,
    'date': datetime.date(2014, 8, 29),
    'symbol': 'AAPL'
}

for price in stock_price:
    print("Info -> {0}".format(price))
