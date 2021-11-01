# Write a Python program to print a dictionary in table format.
dict = {'one':[1,2,3],'two':[5,6,7],'three':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(dict.items()))):
    print(*row)