print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

c = "Hello"
d = 14

print(bool(c))
print(bool(d))


'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
'''

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


'''Some Values are False

In fact, there are not many values that evaluate to False,
 except empty values, such as (), [], {}, "", 
 the number 0, and the value None. 
And of course the value False evaluates to False.'''

