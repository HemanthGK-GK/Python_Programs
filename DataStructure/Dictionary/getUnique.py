#Write a Python program to print all unique values in a dictionary.
dict = {'key1': 'maintain', 'key2': 'silence', 'key3': 'please','key4':'maintain','key5':'in class'}
list =[str] # create empty list
for val in dict.values(): 
  if val in list: 
    continue 
  else:
    list.append(val)#storing unique value to list
print(list)