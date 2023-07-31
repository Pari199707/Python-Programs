n=int(input("Enter an integer"))
for i in range(n):
    for j in range(n-i):
        print('*',end=" ")
    print()