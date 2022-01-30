from vector_example import subtract, List, Vector, vector_mean, magnitude
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
