import os
import sys

from central_tendency_mean import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from collections import Counter
import matplotlib.pyplot as plt

num_friends = [
    100, 49, 41, 40, 25, 21, 21, 19, 19, 18,
    18, 16, 15, 15, 15, 15, 14, 14, 13, 13,
    13, 13, 12, 12, 11, 10, 10, 10, 10, 10,
    10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
    9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
    9, 9, 9, 9, 9, 9, 9, 9, 8, 8,
    8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
    8, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 7, 7, 7, 7, 7, 6, 6, 6, 6,
    6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
    6, 6, 6, 6, 6, 6, 6, 6, 5, 5,
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    5, 5, 5, 5, 5, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1
]

# Add non-duplicated data into friend_counts
friend_counts = Counter(num_friends)
for i in friend_counts:
    print(i)
    
print("============================================")

num_points = len(num_friends)
print("Num Friends Length : {0}".format(num_points))

largest_value = max(num_friends)
smallest_value = min(num_friends)
print("Largest Value : {0}\nSmallest Value : {1}".format(largest_value, smallest_value))

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]
print("Sorted Values : {0}\nSmallest Value (Sorted Num_friends) : {1}\n"
      "Secondly Smallest value : {2}\nSecondly Largest value : {3}"
      .format(sorted_values, smallest_value, second_smallest_value, second_largest_value))

print("Mean --> {0}".format(mean(num_friends)))
print("Median Check Odd : {0}".format(median([1, 10, 2, 9, 5])== 5))
print("Median Check Even : {0}".format(median([1, 9, 2, 10]) == (2 + 9) / 2))
print("Median check odd or even{0}".format(median(num_friends)))

print("Quantile -> {0}".format(quantile(num_friends, 0.10) == 1))
print("Quantile -> {0}".format(quantile(num_friends, 0.25) == 3))
print("Quantile -> {0}".format(quantile(num_friends, 0.75) == 9))
print("Quantile -> {0}".format(quantile(num_friends, 0.90) == 13))

print("Mode -> {0}".format(set(mode(num_friends)) == {1, 6}))

xs = range(101)
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])

plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.subplot()

plt.show()
