#Leagal variable name

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John" #Camel case
my_variable_name = "John" #snake case
MyVariableName = "John" #pascal case

#Multiple Variable

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

#If you have a collection of values in a list, tuple etc.
#Python allows you to extract the values into variables. This is called unpacking

fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)