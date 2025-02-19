a = [1, 2, 3, 4, 5, 2, 6, 3]
# A set to keep track of elements that have been seen
seen = set()
# A list to store duplicates found in the input list
duplicates = []
# Iterate over each element in the list
for i in a:
    if i in seen:
        duplicates.append(i)
    else:
        seen.add(i)

print(duplicates)

b = [1,2,3,4,5,6,7,3,8,9,9]
c = set()
duplicates = []
for i in b:
    if i in c:
        duplicates.append(i)
    else:
        c.add(i)
print(duplicates)
