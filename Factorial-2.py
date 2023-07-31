
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


n=int(input("Enter any integer"))
print("The factorial of ",n,"is",fact(n))