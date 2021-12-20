import sys, re
import os
import csv

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



if __name__ == "__main__":
    with open("tab_delimited_stock_prices.txt", 'r', encoding='utf8',newline='') as f:
        tab_reader = csv.reader(f, delimiter="\t")
        print("Tab Reader -> {0}".format(tab_reader))

        for row in tab_reader:
            date = row[0]
            symbol = row[1]
            closing_price = float(row[2])

            process(date, symbol, closing_price)
