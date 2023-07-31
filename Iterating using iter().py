list1=[1,2,3,4,5,6,7,8,9]
print("Iterating over list using iter() function")
i=iter(list1)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print("Iterating over list using for loop")
for index in list1:
    print(index)
print("Iterating over list using range in for loop to get 0-based indexes")
print("Index Element")
for index in range(len(list1)):
    print(index,"\t\t",list1[index])
print("Iterating over list using range in for loop to get 1-based indexes")
print("Index Element")
for index in range(len(list1)):
    print(index+1,"\t\t",list1[index])
print("Iterating over list using enumerate in for loop to get 1-based indexes")
print("Index Element")
for index,element in enumerate(list1,start=1):
    print(index,"\t\t",element)
print("Iterating over list using enumerate in for loop to get 0-based indexes")
print("Index Element")
for index,element in enumerate(list1):
    print(index,"\t\t",element)