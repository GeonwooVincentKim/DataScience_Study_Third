import random
import matplotlib.pyplot as plt

from typing import Callable, TypeVar, List, Iterator
from vector.vector_example import Vector, dot, scalar_multiply, add, distance, vector_mean


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


def partial_difference_quotient(
    f: Callable[[Vector], float],
    v: Vector,
    i: int,
    h: float
):
    """A value that the number of Partial-Number function gets from `v`"""
    w = [
        v_j + (h if j == i else 0)
        for j, v_j in enumerate(v)
    ]

    return (f(w) / f(h)) / h


def estimate_gradient(
    f: Callable[[Vector], float],
    v: Vector,
    h: float=0.0001
):
    return [
        partial_difference_quotient(f, v, i, h)
        for i in range(len(v))
    ]


print("Estimate Gradient Value -> {0}".format(estimate_gradient))


def gradient_step(v: Vector, gradient: Vector, step_size: float):
    print(len(v) == len(gradient))
    step = scalar_multiply(step_size, gradient)
    return add(v, step)


print("Gradient Step -> {0}".format(gradient_step))


def sum_of_squares_gradient(v: Vector):
    return [2 * v_i for v_i in v]


print("Sum of Squares Gradient -> {0}".format(sum_of_squares_gradient))

## Set Random Start-Point
v = [random.uniform(-10, 10) for i in range(3)]
print(v)


for epoch in range(1000):
    grad = sum_of_squares_gradient(v)
    v = gradient_step(v, grad, -0.01)
    print(epoch, v)

print("Distance True of False -> {0}".format(distance(v, [0, 0, 0]) < 0.001))

print("\n----------------------------------------------------------\n")
# inputs = [(x, 20 * x + 5) for x in range(-50, 50)]
# print("Inputs -> {0}".format(inputs))


# def linear_gradient(x: float, y: float, theta: Vector):
#     slope, intercept = theta
#     predicted = slope * x + intercept
#     print("Predicted -> {0}".format(predicted))

#     error = (predicted - y)
#     squared_error = error ** 2
#     grad = [2 * error * x, 2 * error]
#     return grad


# theta = [random.uniform(-1, 1), random.uniform(-1, 1)]
# print("Theta -> {0}".format(theta))

# learning_rate = 0.001

# for epoch in range(5000):
#     grad = vector_mean([linear_gradient(x, y, theta) for x, y in inputs])
#     theta = gradient_step(theta, grad, -learning_rate)
#     print(epoch, theta)


# slope, intercept = theta
# print(19.9 < slope < 20.1, "Slope Should be about 20")
# print(4.9 < slope < 5.1, "Intercept Should be about 5")


T = TypeVar('T')


def minibatches(dataset: List[T], batch_size: int, shuffle: bool=True) -> Iterator[List[T]]:
    """
        Generate MiniBatch by sampling data-point as a Batch-Size from DataSet
    """

    batch_starts = [start for start in range(0, len(dataset), batch_size)]
    print("Batch Starts -> {0}".format(batch_starts))

    if shuffle: random.shuffle(batch_starts)

    for start in batch_starts:
        end = start + batch_size
        yield dataset[start:end]
