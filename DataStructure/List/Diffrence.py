# Write a Python program to get the difference between the two lists.
list1 = [10, 30, 15, 87, 90]
list2 =[10, 87, 26, 45, 87, 8]
diff1 = list(set(list1) - set(list2))
diff2 = list(set(list2) - set(list1))
total_diff = diff1 + diff2
print(total_diff)