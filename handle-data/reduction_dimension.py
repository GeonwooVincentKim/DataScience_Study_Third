import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import tqdm

from vector_example import subtract, List, Vector, vector_mean, magnitude, dot, scalar_multiply
# from handle_scale import scale
from matrix_example import shape, make_matrix
from gradient_descent_example import *

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


def first_principal_component(data: List[Vector], n: int = 100, step_size: float = 0.1):
    # Stating from randomly guessed position
    guess = [1.0 for _ in data[0]]
    print("\n-----------------\nGuess ->{0}".format(guess))
    
    with tqdm.trange(n) as t:
        for _ in t:
            dv = directional_variance(data, guess)
            gradient = directional_variance(data, guess)
            guess = gradient_step(guess, gradient, step_size)
            t.set_description(f"dv: {dv:.3f}")

    return direction(guess)


def project(v: Vector, w: Vector) -> Vector:
    """
       Project `v` to the direction of `w`
    """
    projection_length = dot(v, w)
    return scalar_multiply(projection_length, w)


def remove_projection_from_vector(v: Vector, w: Vector) -> Vector:
    """
        Subtract `v` to the result of projection `v` to the `w`
    """
    return subtract(v, project(v, w))


def remove_projection(data: List[Vector], w: Vector) -> List[Vector]:
    return [remove_projection_from_vector(v, w) for v in data]
