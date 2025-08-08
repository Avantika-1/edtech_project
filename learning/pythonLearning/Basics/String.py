# in python we use three qoutes to write multiline string
a = ('''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''')
print(a)

# String as Array-
# In many programming languages, strings can be treated as an array (or list) of characters.
# This means you can access individual characters using an index.

a = "Hello, World!"
print(a[1])
print(a[-1])
print(a[-5])

# Looping through a string

for x in "apple":
    print(x)

# find string length
a = "Hello, world"
print(len(a))

# Check string
# Check if "free" is present in the following text:
txt = "the best thing in life are free "
print("free" in txt) #will give bool value as tru and flase
if "free" in txt:  #will give value of print according to condition
    print("yes,'free is present'")

# Check if not
str = "Testing is easy" #will give value of print according to condition
print("free" not in txt) #will give bool value as tru and flase
if "difficult"  in str:
    print("yes")
else:
    print("NO")


