def fib(n):

    a=0
    b=1

    if n == 1:
        print(a)
    elif n == -1:
        print ("invalid")
    else:
        print("na")

    for i in range(0,n):

        c=a+b
        a=b
        b=c

        print(c)

fib(10)