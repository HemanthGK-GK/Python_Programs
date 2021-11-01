# Write a Python program to create a set.
set = {12, 24, 36, 48, 60} #creating set and adding values to set

for n in set:
    print(n, end=' ') #Iterating set

set.add(43)#adding values to set
set.add(50)

print(set)

set.discard(36)#Deleting value from set
print(set)

set.discard(24) #remove if that value in set

set.clear() #clear the test



