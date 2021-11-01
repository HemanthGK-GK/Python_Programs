#1. Write a Python program to create an array of 5 integers and display the array items.
#Access individual element through indexes.
from array import *
arr = array('i', [25,41,75,19,23])
for i in arr: #declare array 
    print(i)
print("Access Array items individually")
print(arr[0])
print(arr[4])
print(arr[1])