def pranav(str):
    avantika = ""
    for i in str:
        avantika = i + avantika
    print("the reverse str is",avantika)

str = input("enter str:")
print("reversed str is:",str)
pranav(str)
