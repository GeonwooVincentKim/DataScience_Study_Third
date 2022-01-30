from vector_example import subtract, List, Vector, vector_mean, magnitude, dot
from handle_scale import scale
from matrix_example import shape, make_matrix

import numpy as np
import matplotlib as plt


def de_mean(data: List[Vector]) -> List[Vector]:
    """
        Re-alignment every dimension average become 0
    """
    mean = vector_mean(data)
    return [
        subtract(vector, mean)
        for vector in data
    ]


def direction(w: Vector) -> Vector:
    mag = magnitude(w)
    print("Magnitude -> {0}".format(mag))

    return [w_i / mag for w_i in w]


def directional_variance(data: List[Vector], w: Vector):
    """
        Return `X`s variance at the point to location of `w`
    """
    w_dir = direction(w)
    return sum(dot(v, w_dir) ** 2 for v in data)


def directional_variance_gradient(data: List[Vector], w: Vector):
    """
        Variance Gradient of certain direction related to `w`
    """
    w_dir = direction(w)
    return [
        sum(2 * dot(v, w_dir) * v[i] for v in data)
        for i in range(len(w))
    ]

