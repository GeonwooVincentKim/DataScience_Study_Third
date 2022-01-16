import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from typing import Tuple, List

from vector_example import Vector, distance, vector_mean
from dispersion_example import standard_deviation


print("\n-------------------------------\n")

a_to_b = distance([63, 150], [67, 160])
a_to_c = distance([63, 150], [70, 171])
b_to_c = distance([67, 160], [70, 171])

print("A to B (1st) -> {0}".format(a_to_b))
print("B to C (1st) -> {0}".format(a_to_c))
print("B to C (1st) -> {0}".format(a_to_c))

a_to_b = distance([160, 150], [170.2, 160])
a_to_c = distance([160, 150], [177.8, 171])
b_to_c = distance([170.2, 160], [177.8, 171])

print("\n-------------------------------\n")
print("A to B (2nd) -> {0}".format(a_to_b))
print("B to C (2nd) -> {0}".format(a_to_c))
print("B to C (2nd) -> {0}".format(a_to_c))
print("\n-------------------------------\n")


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    """
        Print each columns `average` and `Standard-Deviation`
    """
    dimension = len(data[0])
    print("Dimension -> {0}".format(dimension))

    means = vector_mean(data)
    print("Meaning -> {0}".format(means))

    stdev = [
        standard_deviation(
            [vector[i] for vector in data]
        )
        for i in range(dimension)
    ]
    print("Standard Deviation -> {0}".format(stdev))


vectors = [[-3, -1, 1], [-1, 0, 1], [1, 1, 1]]
print("Vectors List -> {0}".format(vectors))

means, stdevs = scale(vectors)
# print(means == [-1, 0, 1])
# print(stdevs == [2, 1, 0])
# print("Meanings -> {0}".format(means))
# print("Standard-Deviations -> {0}".format(stdevs))
