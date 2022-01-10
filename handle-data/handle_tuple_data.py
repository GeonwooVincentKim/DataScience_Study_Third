from named_tuple import *
from collections import defaultdict
from typing import Dict, List


data = [
    StockPrice(
        symbol='MSFT',
        date=datetime.date(2018, 12, 24),
        closing_price=106.03
    )
]

print("Current Data Information -> {0}".format(data))
print("\n--------------------------------\n")

# max_aapl_price = max(
#     stock_price.closing_price
#     for stock_price in data
#     if stock_price.symbol == "AAPL"
# )
# print("Max AAPL Price -> {0}".format(max_aapl_price))


max_prices: Dict[str, float] = defaultdict(lambda: float('-inf'))
print("Max Prices -> {0}".format(max_prices))
print("\n--------------------------------\n")

for sp in data:
    symbol, closing_price = sp.symbol, sp.closing_price

    if closing_price > max_prices[symbol]:
        max_prices[symbol] = closing_price


prices: Dict[str, List[StockPrice]] = defaultdict(list)
print("Prices -> {0}".format(prices))

for sp in data:
    prices[sp.symbol].append(sp)

