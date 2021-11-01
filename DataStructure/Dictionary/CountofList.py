# Write a Python program to count number of items in a dictionary value that is a list.
dict =  {'list1': ['value1', 'value2', 'value3'], 'list2': ['val4', 'val5']}
ctr = sum(map(len, dict.values()))
print(ctr)