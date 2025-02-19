
#us interviewr ko cjhiy tha ki 1-20 k sare even no aay..jo jo no 5 se divisble ho unk aage spcl no likh k aay
for i in range(1, 21):
    if i % 2 == 0 and i % 5 == 0:
       print(f"{i} is both even and divisible by 5 (spcl no)")
    if i % 2 == 0:
        print(f"{i} is an even number")
    elif i % 5 == 0:
        print(f"{i} is a spcl no (divisible by 5)")