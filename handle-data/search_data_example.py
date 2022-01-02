from typing import List, Dict
from collections import Counter

import math
import random
import matplotlib.pyplot as plt

from continuous_distribution_example import inverse_normal_cdf
from matrix_example import *
from dispersion_example import correlation


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

print("\n\n")


def correlation_matrix(data: List[Vector]):
    """
        Return the matrix `len(data) x len(data)` that the number of `(i, j)`
        represents `Correlation` of `data[i]` and `data[j]`
    """
    def correlation_ij(i: int, j: int):
        return correlation(data[i], data[j])
    
    return make_matrix(len(data), len(data), correlation_ij)


def make_scatterplot_matrix():

    # first, generate some random data

    num_points = 100

    def random_row():
        row = [None, None, None, None]
        row[0] = random_normal()
        row[1] = -5 * row[0] + random_normal()
        row[2] = row[0] + row[1] + 5 * random_normal()
        row[3] = 6 if row[2] > -2 else 0
        return row

    random.seed(0)
    # Corr-Data is the list that have `four 100 dimension vector` 
    corr_data = [random_row()
            for _ in range(num_points)]

    num_vectors = len(corr_data)
    print("Num Vectors -> {0}".format(num_vectors))

    fig, ax = plt.subplots(num_vectors, num_vectors)

    for i in range(num_vectors):
        for j in range(num_vectors):

            # Dispersion that shows `X-Axis` for `Number J Row`, And `Y-Axis`' for `Number I Column`
            if i != j: ax[i][j].scatter(corr_data[j], corr_data[i])

            # Print `if i == j` on the title-bar
            else: ax[i][j].annotate(
                "series "  + str(i), (0.5, 0.5),
                xycoords='axes fraction',
                ha="center", va="center"
            )

            # Specify the Axis-Label that is locate the bottom and Left-Side Chart
            if i < num_vectors - 1: ax[i][j].xaxis.set_variable(False)
            if j > 0: ax[i][j].yaxis.set_visible(False)
            
            
    plt.show()


make_scatterplot_matrix()
