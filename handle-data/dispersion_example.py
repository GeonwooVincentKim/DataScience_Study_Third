import collections
import os
import sys
import math

from matplotlib import pyplot as plt

# from statistics_example.central_tendency_mean import *
from central_tendency_mean import *
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from typing import List
from linear_regression_example.matrix_example import *
from linear_regression_example.vector_example import dot, sum_of_squares
from friendcount_histogram import *


def data_range(xs: List[float]):
    return max(xs) - min(xs)


print("Check Data-Range ->", data_range(num_friends) == 99)


def de_mean(xs: List[float]):
    """Subtract average from all of `x` data-point (To make average 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]


def variance(xs: List[float]):
    print(len(xs) >= 2, "-> variance requires at least two elements")
    
    n = len(xs)
    deviations = de_mean(xs)
    
    return sum_of_squares(deviations) / (n - 1)


print("Variance ->", 81.54 < variance(num_friends) < 81.55)


def standard_deviation(xs: List[float]):
    return math.sqrt(variance(xs))


print("Standard Deviation ?? ->", 9.02 < standard_deviation(num_friends) < 9.04)


def interquartile_range(xs: List[float]):
    return quantile(xs, 0.75) - quantile(xs, 0.25)


print("Inter-Quartile-Range ->", interquartile_range(num_friends) == 6)


daily_minutes = [
    1, 68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22,
    34.76, 54.01, 38.79, 47.59, 49.1, 27.66, 41.03, 36.73, 48.65, 28.12,
    46.62, 35.57, 32.98, 35, 26.07, 23.77, 39.73, 40.57, 31.65, 31.21,
    36.32, 20.45, 21.93, 26.02, 27.34, 23.49, 46.94, 30.5, 33.8, 24.23,
    21.4, 27.94, 32.24, 40.57, 25.07, 19.42, 22.39, 18.42, 46.96, 23.72, 26.41,
    26.97, 36.76, 40.32, 35.02, 29.47, 30.2, 31, 38.11, 38.18, 36.31,
    21.03, 30.86, 36.07, 28.66, 29.08, 37.28, 15.28, 24.17, 22.31, 30.17,
    25.53, 19.85, 35.37, 44.6 ,17.23, 13.47, 26.33, 35.02, 32.09, 24.81,
    19.33, 28.77, 24.26, 31.98, 25.73, 24.86, 16.28, 34.51, 15.23, 39.72,
    40.8, 26.06, 35.76, 34.76, 16.13, 44.04, 18.03, 19.65, 32.62, 35.59,
    39.43, 14.18, 35.24, 40.13, 41.82, 35.45, 36.07, 43.67, 24.61, 20.9,
    21.9, 18.79, 27.61, 27.21, 26.61, 29.77, 20.59, 27.53, 13.82, 33.2,
    25, 33.1,36.65, 18.63, 14.87, 22.2, 36.81, 25.53, 24.62, 26.25,
    18.21, 28.08, 19.42, 29.79, 32.8, 35.99, 28.32, 27.79, 35.88, 29.06,
    36.28, 14.1, 36.63, 37.49, 26.9, 18.58, 38.48, 24.48, 18.95, 33.55,
    14.24, 29.04, 32.51, 25.63, 22.22, 19, 32.73, 15.16, 13.9, 27.2,
    32.01, 29.27, 33, 13.74, 20.42, 27.32, 18.23, 35.35, 28.48, 9.08,
    24.62, 20.12, 35.26, 19.92, 31.02, 16.49, 12.16, 30.7, 31.22, 34.65,
    13.13, 27.51, 33.2, 31.57, 14.1, 33.42, 17.44, 10.12, 24.42, 9.82,
    23.39, 30.93, 15.03, 21.67, 31.09, 33.29, 22.61, 26.89, 23.48, 8.38,
    27.81, 32.35, 23.84
]


def covariance(xs: List[float], ys: List[float]):
    print(len(xs) == len(ys), "- xs and ys must have same number of elements")
    return dot(de_mean(xs), de_mean(ys)) / (len(xs) - 1)


print("covariance ->", 22.42 < covariance(num_friends, daily_minutes) < 22.43)
print("covariance (divide by 60) ->", 22.42 / 60 < covariance(num_friends, daily_minutes) < 22.43 / 60)


def correlation(xs: List[float], ys: List[float]):
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    
    if(stdev_x > 0 and  stdev_y > 0):
        return covariance(xs, ys) / stdev_x / stdev_y
    else: 
        return 0

    
outlier = num_friends.index(100) # index of outlier

num_friends_good = [
    x 
    for i, x in enumerate(num_friends) 
    if i != outlier
]

daily_minutes_good = [
    x 
    for i, x in enumerate(daily_minutes) 
    if i != outlier
]

plt.scatter(num_friends_good, daily_minutes_good)
plt.show()
