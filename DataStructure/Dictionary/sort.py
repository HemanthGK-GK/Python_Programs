#Write a Python script to sort (ascending and descending) a dictionary by value.
import operator
d = {1:10,4:40,3:30,2:20,7:70}
print('Original dictionary : ',d)
s = sorted(d.items(), key=operator.itemgetter(1))#sorting dictionary
print('Ascending order : ',s)
reverse = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))# reverse the sorted dictionary
print('Descending order : ',reverse)