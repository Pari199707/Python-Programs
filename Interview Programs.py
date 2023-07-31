
''' 1. Create a list of squared integers from a given list of integers. '''
user_list = list(range(1,11))
def squared_list(l):
 square=[]
 for i in l:
    square.append(i**2)
 return square
print(squared_list(user_list))



'''2.print even numbers from the list:'''
li = [1,2,3,4,5,6,7,8,9,10]
def lst_even(e):
 square=[]
 for i in li:
    if(i %2 ==0):
        square.append(i)
 return square
print(lst_even(li))


''' Create a list of vowels from a given string'''

text = input("Text:")
count = 0
for character in text:
 if(character in "aAeEiIoOuU"):
    count +=1
print(count)


'''4.Count the number of words from the give string'''
s=input("String:")
strlist=s.split()
print(len(strlist))




'''5.count all the positive numbers from the string'''
list=[23,-34,-56,76,-26,87]
positive=0
negitive=0
for i in list:
 if (i >0):
    positive=positive+1
 else:
    negitive=negitive+1
print("positive")
print("Negitive")



'''6.count the total sum of elements from the string'''
list=[1,2,3,4,5,6,7,8,9]
sum=0
for i in list:
 sum=sum+i
print(sum)

'''7.Find the unique words from the give input string'''
str=input("Enter the String: ").split()
l=list()
for ele in str:
    if ele not in l:
        l.append(ele)
print("Unique words",l)

'''8:count the upper case letter in the string'''
text=input("Text:")
count=0
for character in text:
 if(character.isupper()):
    count+=1
print("Count# ",count)

'''9: Create a list of all the first letters of words in a given sentence'''
st=" hello my self anil varma"
ff = [word[0] for word in st.split()]
print(ff)


'''10:Reverse the string'''
def reverse_string(str):
 str1=""
 for i in str:
    str1 = i+str
 return str1
str="varma"
print(reverse_string(str))

'''11 Removing vowels from given string:'''
str=input("Text:")
vowel_string="aeiouAEIOU"
for char in str:
 if char in vowel_string:
    str=str.replace(char,"")
print(str)
