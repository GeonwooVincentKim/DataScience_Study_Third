from typing import List
from typing import Tuple, Callable


Matrix = List[List[float]]
print(Matrix)

Vector = List[float]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]

for i in A:
    print("{0}".format(i))
    
    for j in i:
        print("{0}".format(j))    
    print("")

print("==================================")

for i in B:
    print("{0}".format(i))
    
    for j in i:
        print("{0}".format(j))
    print("")


def shape(A: Matrix):
    """Return (Number of Rows, Number of Columns)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    
    return num_rows, num_cols

# assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, i: int) -> Vector:
    """Return number `i` of `A`s row"""
    return A[i]


# True Case
print(get_row(A, 1) == [4, 5, 6])

# False Case
print(get_row(A, 1) == [1, 2, 3])


def get_column(A: Matrix, j: int) -> Vector:
    """Return number `j` of `A`s column"""
    return [A_i[j]
            for A_i in A]
    
# True Case
print(get_column(B, 1) == [2, 4, 6])
print(get_column(B, 0) == [1, 3, 5])

# False Case
print(get_column(B, 1) == [1, 2, 3])
print(get_column(B, 0) == [2, 4, 6])


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """
    Return `num_rows * num_cols` List that the number of `(i, j)`
    equals to `entry_fn(i, j)`
    """
    return [[entry_fn(i, j)
             for j in range(num_cols)]
            for i in range(num_rows)]
    

# make_matrix(1, 2, get_column((B, 1), j == (2, 4, 6)))
    

def identify_matrix(n: int) -> Matrix:
    """Return `n * n` unit matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


# assert identify_matrix(5) == [[1, 0, 0, 0, 0],
#                               [0, 1, 0, 0, 0],
#                               [0, 0, 1, 0, 0],
#                               [0, 0, 0, 1, 0],
#                               [0, 0, 0, 0, 1]]
print("Check Identify-Matrix -> {0}".format(
    identify_matrix(5) == [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ])
)

data = [
    [70, 170, 40],
    [65, 120, 26],
    [77, 250, 19],
    # ....
]


friendships_pairs = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

friend_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # user 1
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # user 2
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # user 3
                 [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # user 4
                 [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # user 5
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 6
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # user 7
                 [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # user 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # user 9

print(friend_matrix[0][2] == 1, "-> 0 and 2 are friends")
print(friend_matrix[0][8] == 0, "0 and 8 are not friends")

friends_of_five = [
    i
    for i, is_friend in enumerate(
        # identify_matrix(5) == [
        #     [1, 0, 0, 0, 0],
        #     [0, 1, 0, 0, 0],
        #     [0, 0, 1, 0, 0],
        #     [0, 0, 0, 1, 0],
        #     [0, 0, 0, 0, 1]
        # ]
        # identify_matrix(5)
        friend_matrix[5]
    )
    if is_friend
]
print(friends_of_five)
