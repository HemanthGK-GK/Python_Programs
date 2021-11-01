# Write a Python program to sum all the items in a list.
def sums(items):
    num = 0
    for x in items:#iterating loop
        num += x
    return num
#calling method
print(sums([8,4,6,9,7]))