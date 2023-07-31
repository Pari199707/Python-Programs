def fib(x):
    a=0
    b=1
    for i in range(2,x):
        c=a+b
        a=b
        b=c
    return c
n=int(input("Enter any integer"))
print("The fibonacci of ",n,"is",fib(n))