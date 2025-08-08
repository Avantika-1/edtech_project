'''Built-in Data Types

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
'''

x = "Hello world"
print(type(x))

y = 20
print(type(y))

z = 1j
print(type(z))

a = ["apple", "banana", "cherry"]
print(a)
print(type(a))

b = ("apple", "banana", "cherry")
print(b)
print(type(b))

d = range(6)
print(d)
print(type(d))

c = {"name": "apple", "age": "30"}
print(c)
print(type(c))

e = frozenset({"apple", "banana", "cherry"})
print(e)
print(type(e))

f = True
print(type(f))

g = b"Hello"
print(g)
print(type(g))

h = bytearray(5)
print(h)
print(type(h))

i = memoryview(bytes(5))
print(i)
print(type(i))

j = None
print(j)
print(type(j))
