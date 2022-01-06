import datetime
from collections import namedtuple
from typing import NamedTuple

from dataclasses import dataclass

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

print("\n--------------------\n")
print("<Use Named-Tuple Object>")


# Did not use the annotation
class StockPrice(NamedTuple):
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """
            Can add the method because it is method
        """
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']


price = StockPrice('MSFT', datetime.date(2018, 12, 14), 106.83)

print("Price - Symbol (StockPrice Class) (True or False) -> {0}".format(price.symbol == 'MSFT'))
print("Price - Closing-Price (StockPrice Class) (True or False) -> {0}".format(price.closing_price == 106.03))
print("Price - Is-High-Tech (StockPrice Class) (True or False) -> {0}".format(price.is_high_tech()))
print("\n--------------------------\n")


@dataclass
class StockPrice2:
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """
            Can add the method because it's method
        """
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']


price2 = StockPrice2('MSFT', datetime.date(2018, 12, 14), 106.03)

print("<Use Decorator Object>")
print("Price2 - Symbol (StockPrice2 Class) (True of False) -> {0}".format(price2.symbol == 'MSFT'))
print("Price2 - Symbol (StockPrice2 Class) (True of False) -> {0}".format(price2.closing_price == 106.03))
print("Price2 - Symbol (StockPrice2 Class) (True of False) -> {0}".format(price2.is_high_tech()))
