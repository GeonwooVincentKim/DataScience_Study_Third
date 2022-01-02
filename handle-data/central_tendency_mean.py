from collections import Counter
from typing import List


"""
def mean(xs: List[float]) -> float:
    return sum (xs) / len(xs)
"""

def mean(xs: List[float]):
    """Average"""
    return sum (xs) / len(xs)


"""
def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs) // 2]
"""

def _median_odd(xs: List[float]):
    """Return Median value if `len(xs)` is Odd-Number"""
    return sorted(xs)[len(xs) // 2]


"""
def _median_even(xs: List[float]):
    sorted_xs = sorted(xs)
    hi_midPoint = len(xs) // 2
    return (sorted_xs[hi_midPoint - 1] + sorted_xs[hi_midPoint]) / 2
"""

def _median_even(xs: List[float]):
    """Return Median value if `len(xs)` is Even-Number"""
    sorted_xs = sorted(xs)
    hi_midPoint = len(xs) // 2
    return (sorted_xs[hi_midPoint - 1] + sorted_xs[hi_midPoint]) / 2


"""
def median(v: List[float]):
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)
"""

def median(v: List[float]):
    """Calculate Median-Number of `v`"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


"""
def quantile(xs: List[float], p: float):
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]
"""

def quantile(xs: List[float], p: float):
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


"""
"""

def mode(x: List[float]):
    counts = Counter(x)
    max_count = max(counts.values())
    
    return [x_i for x_i, count in counts.items()
            if count == max_count]
