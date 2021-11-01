# Write a Python program to check multiple keys exists in a dictionary.
data = { 'k1':'value1','k2':'value2','k3':'value3'}
word=input("Enter word to check : ")
if word in data: #searching for perticular word 
    print(data[word])
else:
    print("Not Exist")