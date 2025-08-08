print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

##FUnction

def my_function():
    return True

print(my_function())

def my_func():
    return True
if my_func():

    print("yes")
else:
    print("No!")

""" Python also has many built-in functions that 
return a boolean value, like the isinstance() function,
which can be used to determine if an object is of a certain data type:"""

x = 200
print(isinstance(x, int))
