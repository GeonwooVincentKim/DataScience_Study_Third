from typing import List, Dict
from collections import Counter
import math

import matplotlib.pyplot as plt


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
