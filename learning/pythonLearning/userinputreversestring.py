def rev_userin(string_1):
    new_strig=""
    for i in string_1:
        new_strig = i + new_strig

    print("the reverse string is :",new_strig)


string_1 = input("enter new string:")
print("new reversed str",string_1)
rev_userin(string_1)

str = "hi pranav, how are you?"
new_str = str[::-1]
print(new_str)
