from typing import List, Dict
from collections import Counter

import math
import random
import matplotlib.pyplot as plt

from continuous_distribution_example import inverse_normal_cdf, Matrix, Vector, make_matrix


def bucketize(point: float, bucket_size: float):
    """
        Position each data that corresponds the section of 
        multiple time of `bucket_size`
    """
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points: List[float], bucket_size: float):
    """
        Generate the section, and then calculate the numbers of each data
        of each section
    """
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points: List[float], bucket_size: float, title: str=""):
    histogram = make_histogram(points, bucket_size)
    
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


# Initialize Random-Value
random.seed(0)

# Uniform-Distribution
uniform = [200 * random.random() - 100 for _ in range(10000)]
print("Uniform-Distribution -> {0}".format(uniform))

# Normal-Distribution
normal = [
    57 * inverse_normal_cdf(random.random())
    for _ in range(10000)
]
print("Normal-Distribution -> {0}".format(normal))


plot_histogram(uniform, 10, "Uniform Histogram")
plot_histogram(normal, 10, "Normal Histogram")


def random_normal():
    """
        Return Random-Number that follows `Standard-Normal-Distribution`
    """
    return inverse_normal_cdf(random.random())


xs = [random_normal() for _ in range(1000)]
print("XS -> {0}".format(xs))
print("\n\n\n")

ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]
print("YS1 -> {0}\nYS2 -> {1}".format(ys1, ys2))

plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')

plt.xlabel('xs')
plt.ylabel('ys')

# Display the Legend of Graph
plt.legend(loc=9)

plt.title("Very Different Joint Distributions")
plt.show()
