# Write a Python program to create a null vector of size 10 and update sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11
# [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
import numpy as np
a = np.zeros(10)
print(a)
print("Update sixth index to 11")
a[6] = 11#updating 6th index value
print(a)