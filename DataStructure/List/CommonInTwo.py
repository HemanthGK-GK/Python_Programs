# Write a Python function that takes two lists and returns True if they have at
#least one common member.
def data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(data([1,2,3,4,5], [5,4,7,8,9]))
print(data([1,2,3,4,5], [6,7,8,9]))