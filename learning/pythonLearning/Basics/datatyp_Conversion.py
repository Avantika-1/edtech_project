#Setting the Specific Data Type

#If you want to specify the data type,
# you can use the following constructor functions:

x = str("Hello World")  #	str
print(x)
print(type(x))

y = int(20) 	#int
print(y)

z = float(20.5) 	#float
print(z)

a = complex(1j) 	#complex
print(a)

b = list(("apple", "banana", "cherry")) 	#list
print(b)

c = tuple(("apple", "banana", "cherry")) 	#tuple
print(c)

d = range(6) 	#range
print(d)

e = dict(name="John", age=36) 	#dict
print(e)

f = set(("apple", "banana", "cherry")) 	#set
print(f)

g = frozenset(("apple", "banana", "cherry")) 	#frozenset
print(g)

h = bool(5) 	#bool
print(h)

i = bytes(5) 	#bytes
print(i)

j = bytearray(5) 	#bytearray
print(j)

h = memoryview(bytes(5)) 	#memoryview
print(h)