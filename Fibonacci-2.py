a=0
b=1
def fib(x):
    global a, b
    for i in range(2,x):
        c=a+b
        a=b
        b=c
        print(c, end=" ")

n=int(input("Enter any integer"))
print("Fibonacci Series:", a, b, end=" ")
fib(n)
