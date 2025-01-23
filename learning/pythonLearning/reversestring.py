a = "Hi, how are you?"
b = a[::-1]
print("the reverse string of a is :",b)


#Using Loop
str = "Hi want to reverse using loop"
str1 = ""
for i in str:
    str1 = i+str1

print("the reverse string of a is :",str1)

#User input
def reverse(string):

    abcd = ""
    for i in string:
        abcd = i + abcd

    print("the reverse string of a is :", abcd)

string = input("enter a string:")
print("enterd string",string)
reverse(string)