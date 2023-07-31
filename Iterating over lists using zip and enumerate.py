DaysEng=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
DaysInd=['Ravivaar','Somvaar','Mangalvaar','Budhvaar','Guruvaar','Shukrvaar','Shanivaar']
print("String Output")
for i,m in zip(DaysEng,DaysInd):
    print(i,m)
print()
print("Tuple Output")
for i in zip(DaysEng,DaysInd):
    print(i)
print()
print("Using Zip and Enumerator and tuples")
for i,m in enumerate(zip(DaysEng,DaysInd),start=1):
    print(i,":",m)
print("Using Zip and Enumerator and tuple elements")
for i,m in enumerate(zip(DaysEng,DaysInd),start=1):
    print(i,":",m[0],"==",m[1],"in Indian Languages")
