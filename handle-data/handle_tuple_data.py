from named_tuple import *


data = [
    StockPrice(
        symbol='MSFT',
        date=datetime.date(2018, 12, 24),
        closing_price=106.03
    )
]

print("Current Data Information -> {0}".format(data))

max_aapl_price = max(
    stock_price.closing_price
    for stock_price in data
    if stock_price.symbol == "AAPL"
)
print("Max AAPL Price -> {0}".format(max_aapl_price))
