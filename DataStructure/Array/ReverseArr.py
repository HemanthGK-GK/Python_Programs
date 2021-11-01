#Write a Python program to reverse the order of the items in the array.
from array import *
arr = array('i', [17,45,23,69,71,84])
print("Normal Array : "+str(arr))
arr.reverse()#reverse array using reverse()
print("Reverse Array :"+str(arr))
