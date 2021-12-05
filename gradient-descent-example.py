from typing import Callable
from vector.vector_example import Vector, dot

import matplotlib.pyplot as plt


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
actuals = [derivative(x) for x in xs]
estimates = [difference_quotient(square, x, h=0.001) for x in xs]
print("XS -> {0}\nActuals -> {1}\nEstimates -> {2}".format(xs, actuals, estimates))

plt.title("Actual Derivatives vs. Estimates")
plt.plot(xs, actuals, 'rx', label='Actual')
plt.plot(xs, estimates, 'b+', label='Estimate')
plt.show()
