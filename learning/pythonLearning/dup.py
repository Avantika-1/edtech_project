list = [10,19,19,8,8,6,5,4,4,1,1]
newset = set()
duplicates = []
for i in list:
    if i in newset:
        duplicates.append(i)
    else:
        newset.add(i)

print(list)
print(newset)
print(duplicates)



list1 = [18,12,12,1,10,8,0]
a = set()
duplicates1 = []
for i in list1:
    if i in a:
         duplicates1.append(i)
    else:
        a.add(i)

print(duplicates1)

