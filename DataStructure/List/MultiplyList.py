# Write a Python program to multiplies all the items in a list.
def product(items):
    num = 1
    for x in items:#iterating loop
        num *= x
    return num
#calling method
print(product([2,3,4,1,5]))