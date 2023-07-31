from array import *
vals=array('i',[ ])
n=int(input('Enter the length of the array'))
for i in range(n):
    a =int(input("Enter tha array values"))
    vals.append(a)
print(vals)

val=int(input("Enter the value to be searched"))
k=0
for i in vals:
    if i==val:
        print(val,"found")
        break
    k+=1
print(val,"found at",k,"position")
