#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example:Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#Without list comprehension you will have to write a for statement with a conditional test inside

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:
newfruits = ["apple","banana","cherry","kiwi","mango"]
n_list= [x for x in newfruits if "a" in x]
print(n_list)

newlist1 = [x for x in newfruits if x != "apple"]
print(newlist1)

# Iterable-> The iterable can be any iterable object, like a list, tuple, set etc.

#Comprehention condition- The condition is like a filter that only accepts the items that evaluate to True.
#i.e
newlist = [x for x in fruits if x != "apple"] # here it will accept all the vlaue in list except apple
print(newlist)

#Iterable->The iterable can be any iterable object, like a list, tuple, set etc.
newlist = [x for x in range(10)]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
