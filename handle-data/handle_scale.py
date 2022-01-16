import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from typing import Tuple

from vector_example import distance
from dispersion_example import standard_deviation


print("\n-------------------------------\n")

a_to_b = distance([63, 150], [67, 160])
a_to_c = distance([63, 150], [70, 171])
b_to_c = distance([67, 160], [70, 171])

print("A to B (1st) -> {0}".format(a_to_b))
print("B to C (1st) -> {0}".format(a_to_c))
print("B to C (1st) -> {0}".format(a_to_c))

a_to_b = distance([160, 150], [170.2, 160])
a_to_c = distance([160, 150], [177.8, 171])
b_to_c = distance([170.2, 160], [177.8, 171])

print("\n-------------------------------\n")
print("A to B (2nd) -> {0}".format(a_to_b))
print("B to C (2nd) -> {0}".format(a_to_c))
print("B to C (2nd) -> {0}".format(a_to_c))

