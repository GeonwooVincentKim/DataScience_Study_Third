from re import S
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

max_aapl_price = max(
    stock_price.closing_price
    for stock_price in data
    if stock_price.symbol == "AAPL"
)
print("Max AAPL Price -> {0}".format(max_aapl_price))


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

prices = {
    symbol: sorted(symbol_prices)
    for symbol, symbol_prices in prices.items()
}
print("After Sorted Symbol Prices -> {0}".format(prices))
print("\n--------------------------------\n")


def pct_change(yesterday: StockPrice, today: StockPrice) -> float:
    return today.closing_price / yesterday.closing_price - 1


# DailyChange Class
class DailyChange(NamedTuple):
    symbok: str
    date: datetime.date
    pct_change: float


print("< DailyChange Class >")


def day_over_day_changes(prices: List[StockPrice]) -> List[DailyChange]:
    """
        Estimates the `Stock-Price` that matches to `One-Stock` and is sorted
    """
    return [
        DailyChange(
            symbol=today.symbol,
            date=today.date,
            pct_change=pct_change(yesterday, today)
        )
        for yesterday, today in zip(prices, prices[1:])
    ]


all_changes = [
    change
    for symbol_prices in prices.values()
    for change in day_over_day_changes(symbol_prices)
]
print("All Changes -> {0}".format(all_changes))
print("\n")

max_change = max(all_changes, key=lambda change: change.pct_change)
print("Max Change -> {0}".format(max_change))
