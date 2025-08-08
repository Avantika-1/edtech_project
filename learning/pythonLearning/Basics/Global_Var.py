x = "lovely"

def myfunction():
    x = 'fantastic'

print('astro is' + x)

myfunction()



#The global Keyword

#Normally, when you create a variable inside a function,
# that variable is local, and can only be used inside that function.

#To create a global variable inside a function,
# you can use the global keyword.

def newfunc():
    global y
    y = "avantika"

newfunc()

print(y + " is Tester")


# Also,we can use the global keyword if you want to change a global variable inside a function.

z = "avantika"

def test():
    global z
    z = "Sriti"
test()

print (z + " is Devloper")






