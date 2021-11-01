#Write a Python program to remove a key from a dictionary.
Dict = {'key1':1,'key2':2,'key3':3,'key4':4}
print(Dict)
if 'key3' in Dict: #condition for matching 
    del Dict['a']
print(Dict)