import csv
import datetime
import os
import re

from collections import namedtuple
from typing import NamedTuple, List, Optional

from dataclasses import dataclass
from dateutil.parser import parse

from pathlib import Path as pd


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
print("Price2 - Closing-Price (StockPrice2 Class) (True of False) -> {0}".format(price2.closing_price == 106.03))
print("Price2 - Is-High-Tech (StockPrice2 Class) (True of False) -> {0}".format(price2.is_high_tech()))

print("\n----------------------------\n<Divide Stock>")
price2.closing_price /= 2
print("Check After Price2 - Closing-Price (StockPrice2 Instance) (True or False) -> {0}".format(price2.closing_price))
print("Check After Price2 - Closing-Price (StockPrice2 Instance) (True or False) -> {0}".format(price2.closing_price == 51.03))

print("\n------------------------------------\n")


def parse_now(row: List[str]) -> StockPrice:
    symbol, date, closing_price = row
    
    return StockPrice(
        symbol=symbol,
        date=parse(date).date(),
        closing_price=float(closing_price)
    )


stock = parse_now(["MSFT", "2018-12-14", "106.03"])
print("Stock -> {0}".format(stock))
print("Check `Stock Symbol` equals to `MSFT` -> {0}".format(stock.symbol == "MSFT"))
print("Check `Stock Date` equals to `2018-12-14` -> {0}".format(stock.date == datetime.date(2018, 12, 14)))
print("Check `Stock Closing Price` equals to `106.03 -> {0}".format(stock.closing_price == 106.03))

print("\n------------------------------------\n")


def try_parse_row(row: List[str]) -> Optional[StockPrice]:
    symbol, date_, closing_price_ = row

    # Every Stock-Symbol are composed of Capital-Letter
    if not re.match(r"^[A-Z]+$", symbol):
        return None

    try:
        date = parse(date_).date()
    except ValueError:
        return None

    try:
        closing_price = float(closing_price_)
    except ValueError:
        return None

    return StockPrice(symbol, date, closing_price)


print("Test Case 1. Try Parse Now -> {0}".format(try_parse_row(["MSFT0", "2018-12-14", "106.03"]) is None))
# assert try_parse_row(["MSFT0", "2018-12-14", "106.03"]) is None

print("Test Case 2. Try Parse Now -> {0}".format(try_parse_row(["MSFT", "2018-12--14", "106.03"]) is None))
# assert try_parse_row(["MSFT", "2018-12--14", "106.03"]) is None

print("Test Case 3. Try Parse Now -> {0}".format(try_parse_row(["MSFT", "2018-12-14", "x"]) is None))
# assert try_parse_row(["MSFT", "2018-12--14", "x"]) is None

print("Test Case 4. Try Parse Now -> {0}".format(try_parse_row(["MSFT", "2018-12-14", "106.03"]) == stock))
# assert try_parse_row(["MSFT", "2018-12-14", "x"]) == stock

print("\n------------------------------------\n")



data: List[StockPrice] = []
print("Data -> {0}".format(data))

# parent_directory = "E://Python_Data_Analysis_3//colon_delimited_stock_prices.csv"
# save_directory = "E://Python_Data_Analysis_3//handle-data//colon_delimited_stock_prices.csv"

# with open(os.path.join("path", "to", "colon_delimited_stock.csv"), "rU") as f:
with open('../colon_delimited_stock_price.csv') as f:
    reader = csv.reader(f)
    print("Reader -> {0}".format(reader))

