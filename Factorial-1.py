def fact(x):
    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * fact(x - 1))
x=int(input("Enter any integer"))
result=fact(x)
print("The factorial of",x,"is",result)