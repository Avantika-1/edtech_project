#Check if two strings are anagrams of each other
str1 = input("enter string1 ")
str2 = input("enter string2")
if len(str1)!=len(str2):
    print("not anagram")
else:
    if sorted(str1)==sorted(str2):
        print("numbers are anagrams")
    else:
        print("numbers are not anagram")

