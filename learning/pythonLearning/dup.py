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