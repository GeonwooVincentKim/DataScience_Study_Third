from typing import Callable
from vector.vector_example import Vector, dot


def sum_of_squares(v: Vector):
    """
        Calculate the belong items of `v` with `Sum of Squares` 
    """
    return dot(v, v)


def difference_quotient(
    f: Callable[[float], float],
    x: float,
    h: float
):
    return (f(x + h) - f(x)) / h 


def square(x: float):
    return x * x


def derivative(x: float):
    return 2 * x


xs = range(-10, 11)
print("XS -> {0}".format(xs))
