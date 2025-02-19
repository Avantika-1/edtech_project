list = [4, -5, 9, 11, 25, 13, 12, 8]

sum = 20

for i in range(len(list)-1):
    for j in range(i+1, len(list)):
        a = list[i]
        b = list[j]

        if a+b == sum:
            print(f"{a}+{b} = {sum}")
            