# Write a Python program to create a symmetric difference.
set1 = set(["green", "blue","red"])
set2 = set(["blue", "red","white"])
print("Set elements :")
print(set1)
print(set2)
print("\nsymmetric Diffrence of two sets:")
result = set1.symmetric_difference(set2) #symmetric Diffrence of two sets
print(result)