import math
from typing import List

Vector = List[float]
print(Vector)

height_weight_age = [70, # Inch,
                     170, # Pount,
                     40] # Age

for i in height_weight_age:
    print(i)
    
print("----------------------------")

grades = [95, # Test 1 Score
          80, # Test 2 Score,
          75, # Test 3 Score,
          62] # Test 4 Score

for i in grades:
    print(i)
    
print("---------------------------------------")

"""[Vector Calculation Method]
    
    1. Add (a + b)
    a = [1, 2, 3]
    b = [4, 5, 6]
    => [5, 7, 9]
    
    
    2. Subtract (a - b)
    a = [5, 7, 9]
    b = [4, 5, 6]
    => [1, 2, 3]
    
    
    3. Sum ((a += original_list[i]) + (b += original_list[j]))
    original_list = [1, 2], [3, 4], [5, 6], [7, 8]
    
    a = original_list[i] 
    --> [1 + 3 + 5 + 7]
    b = original_list[j]
    --> [2 + 4 + 6 + 8]
    
    sum(a + b) => [16, 20]
    
    
    4. Scalar Multiply (c * a)
    c = 2
    
    a = [1, 2, 3]
    => [2 * 1, 2 * 2, 2 * 3] ==> [2, 4, 6] 
    
    
    5. mean (((a += original_list[i]) / original_list[i].length) + (b += original_list[j]) / original_list[j].length))
    original_list = [1, 2], [3, 4], [5, 6]
    
    a = original_list[i]
    --> [1 + 3 + 5]
    b = original_list[j]
    --> [2 + 4 + 6]
    
    sum(a + b) => [9, 15]
    avg(a, b) => [3, 4]
    
    
    6. dot (a_n * b_n)
    
    a = [1, 2, 3]
    b = [4, 5, 6]
    
    => [1 * 4 + 2 * 5 + 3 * 6] ==> [4 + 10 + 18] ==> 32
    
    
    7. sum_of_square (a^2)
    
    a = [1, 2, 3]
    => [1^2, 2^2, 3^2] ==> [1 + 4 + 9] ==> 14


    8. Magnitude (Square-Root) (a^2 + b^2 = c^2)
    
    a = 3
    b = 4
    
    => [3^2, 4^2] == 5^2 => [9 + 16] == 5^2 ==> 25 
    
    
    9. squared_distane ((a_n)^2 - (b_n)^2)
    10. distance ((a_1)^2 - (b_1)^2) + ((a_2)^2) - (b_2)^2)
"""


def add(v: Vector, w: Vector) -> Vector:
    """Plus Each Elements"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i + w_i for v_i, w_i in zip(v, w)]


# assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
print("Add is True?? -> {0}".format(add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]))


def subtract(v: Vector, w: Vector) -> Vector:
    """Extract Each elements"""
    assert len(v) == len(w), "vectors must be the same length"
    
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
print("Subtract is True?? -> {0}".format(subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]))


def vector_sum(vectors: List[Vector]) -> Vector:
    """Add each elements of Every Vector """
    assert vectors, "no vectors provided!"
    
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


# assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
print("Vector-Sum is True?? -> {0}".format(vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]))


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply Every elements with `c`"""
    return [c * v_i for v_i in v]


# assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]
print("Scalar-Multiply is True?? -> {0}".format(scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]))


def vector_mean(vectors: List[Vector]) -> Vector:
    """Calculate each elements average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


# assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
print("Vector-Mean is True?? -> {0}".format(vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]))


def dot(v: Vector, w: Vector) -> Vector:
    """v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1 * 4 + 2 * 5 + 3 * 6
print("v_1 * w_1 + ... + v_n * w_n -> {0}".format(dot([1, 2, 3], [4, 5, 6]) == 32 ))   # 1 * 4 + 2 * 5 + 3 * 6


def sum_of_squares(v: Vector) -> float:
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)
    

# assert sum_of_squares([1, 2, 3]) == 14  # 1 * 1 + 2 * 2 + 3 * 3
print("v_1 * v_1 + ... + v_n * w_n -> {0}".format(sum_of_squares([1, 2, 3])))


def magnitude(v: Vector) -> float:
    """Return the size of `v`"""
    return math.sqrt(sum_of_squares(v))    # math.sqrt is the function that calculates square-root


# assert magnitude([3, 4]) == 5
print("Magnitude is True?? -> {0}".format(magnitude([3, 4]) == 5))


def squared_distance(v: Vector, w: Vector) -> float:
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(subtract(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Calculate distance between vector `v` and vector `w`"""
    return math.sqrt(squared_distance(v, w))


def distance(v: Vector, w: Vector) -> float:
    """Calculate distance between vector `v` and vector `w`"""
    return magnitude(subtract(v, w))
