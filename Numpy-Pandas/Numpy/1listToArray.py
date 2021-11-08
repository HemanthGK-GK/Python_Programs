# Write a Python program to convert a list of numeric value into a one-dimensional
# NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
import numpy as np
l = [12.23, 13.32, 100, 36.32]#creating list
print("Original List:",l)
a = np.array(l)#converting list to array
print("One-dimensional NumPy array: ",a)