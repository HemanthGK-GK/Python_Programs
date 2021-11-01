#Write a Python program to remove the first occurrence of a specified element from an array.
from array import *
arr= array('i', [21,14,63,21,57,21])#declaring array
print("Original array: "+str(arr))
print("Remove the first occurrence of 21 from array:")
arr.remove(21)
print("New array: "+str(arr))

