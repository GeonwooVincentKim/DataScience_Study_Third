import math
import random
from matplotlib import pyplot as plt

from collections import Counter

SQRT_TWO_PI = math.sqrt(2 * math.pi)


def random_kid():
    return random.choice(["boy", "girl"])


def uniform_pdf(x: float):
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x: float):
    if x < 0: return 0
    elif x < 1: return x
    else : return 1


# Normal Distribution 
def normal_pdf(x: float, mu: float = 0, sigma: float = 1):
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))


xs = [x / 10.0 for x in range(-50, 50)]
print(xs)

plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.plot(xs, [normal_pdf(x, mu=1) for x in xs], '.-', label='mu=1, sigma=1')

plt.legend()
plt.title("Various Normal PDFs")
plt.show()


# Cumulative Distribution Function
def normal_cdf(x:float, mu:float = 0, sigma: float = 1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0, sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0, sigma=0.5')
plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1, sigma=1')
plt.plot(xs, [normal_cdf(x, mu=1) for x in xs], '.-', label='mu=1, sigma=1')

plt.plot(xs, [normal_cdf(x, mu=-1, sigma=-1) for x in xs], '^', label='mu=-1, sigma=-1')
plt.plot(xs, [normal_cdf(x, sigma=-1) for x in xs], '*', label='mu=1, sigma=-1')

plt.legend(loc=4)
plt.title("Various Normal CDFs")
plt.show()


# Convert to Standard-Normal-Distribution if is not
def inverse_normal_cdf(p: float, mu: float=0, sigma: float=1, tolerance: float=0.0001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0
    hi_z = 10.0

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)

        if mid_p < p:
            low_z = mid_z

        else:
            hi_z = mid_z
    
    return mid_z


# Bernoulli Random Variable
def bernouli_trial(p: float):
    return 1 if random.random() < p else 0


def binomial(n: int, p: float):
    return sum(bernouli_trial(p) for _ in range(n))


def binomial_histogram(p: float, n: int, num_points: int):
    data = [binomial(n, p) for _ in range(num_points)]

    histogram = Counter(data)
    print(histogram)

    plt.bar(
        [x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8,
        color='0.75'
    )

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # Show as Line-Chart Approximated Normal-Distribution
    xs = range(min(data), max(data) + 1)
    ys = [
        normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
        for i in xs
    ]
    print(ys)

    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()


# binomial_histogram(0.2, 120, 80)
binomial_histogram(0.75, 100, 10000)


if __name__ == "__main__":

    #
    # CONDITIONAL PROBABILITY
    #

    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0)
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if older == "girl":
            older_girl += 1
        if older == "girl" and younger == "girl":
            both_girls += 1
        if older == "girl" or younger == "girl":
            either_girl += 1

    print("P(both | older) : {0}".format(both_girls / older_girl))      # 0.514 ~ 1/2
    print("P(both | either) : {0}".format(both_girls / either_girl))   # 0.342 ~ 1/3

