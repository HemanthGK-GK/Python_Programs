#Write a Python program to print a specified list after removing the 0th, 4th and
#5th elements.
List = ['Zero', 'First', 'Second', 'Third', 'Fourth', 'Fifth']  
List = [x for (i,x) in enumerate(List) if i not in (0,4,5)]  
print(List)