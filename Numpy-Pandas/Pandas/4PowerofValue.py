# Write a Python program to get the powers of an array values element-wise.
# Note: First array elements raised to powers from second array
# Expected Output:
# Original array
# [0 1 2 3 4 5 6]
# First array elements raised to powers from second array, element-wise:
# [ 0 1 8 27 64 125 216]

import numpy as np
x = np.arange(1,7)
print("Original array")
print(x)
print("First array elements raised to powers from second array, element-wise:")
print(np.power(x, 3))
