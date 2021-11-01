# Write a Python program to find the repeated items of a tuple.
tup=(10,20,50,40,20,30,40)  
for i in tup:
    if tup.count(i) > 1:
        print(i)