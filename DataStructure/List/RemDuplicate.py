# Write a Python program to remove duplicates from a list.
list = [10,20,10,30,20,50,40]
dup_items = []
uniq_items = []
for i in list:
    if i not in dup_items:
        uniq_items.append(i)
    dup_items.append(i)

print(dup_items)
print(uniq_items)