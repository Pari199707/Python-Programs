Dict = {}
print("Empty Dictionary",Dict)

dict1=({1:'Mathematics',2:'Science',3:'Social Sciences'})
print(dict1)

dict2 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(dict2)

dict3=dict({1:'Coding Ninjas',2:'Coding Blocks',3:'Pepcoding'})
print(dict3)

dict4=dict([(1,'Coding Minutes'),(2,'Amigoscode')])
print(dict4)

print("Printing indexes and keys of Dictionaries")
for i,names in enumerate(dict1,start=1):
    print(i,names)
print("Iterating over Dictionaries")
for k,v in dict1.items():
    print(k,v)
print("Merge Operation on Dictionaries")
dict5=(dict2|dict3)
print(dict5)