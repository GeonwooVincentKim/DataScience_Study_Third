from named_tuple import *


data = [
    StockPrice(
        symbol='MSFT',
        date=datetime.date(2018, 12, 24),
        closing_price=106.03
    )
]

print("Current Data Information -> {0}".format(data))
