def rev(str1):
    ab = ""
    for i in str1:
        ab= i + ab
    print("the reverse str is:",ab)

str1 = input("enrer sring:")
print("entered string,:",str1)
rev(str1)
