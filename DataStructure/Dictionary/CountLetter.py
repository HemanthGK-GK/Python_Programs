# Write a Python program to create a dictionary from a string.
from collections import defaultdict, Counter
string = 'MyStrings' 
dict = {}
for letter in string:
    dict[letter] = dict.get(letter, 0) + 1 #counting letter count
print(dict)