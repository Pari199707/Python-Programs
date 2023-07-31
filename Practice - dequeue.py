import collections
import string

deque1=collections.deque(string.ascii_lowercase)
len1=str(len(deque1))
print(len1)
print("Iterating over Deque")
for i in deque1:
    print(i,end=",")
print("Printing uppercase of letters in Deque")
for i in deque1:
    print(i.upper(),end=",")
print("Pop and Append Operations on Deque")
deque1.pop()
print(deque1)
deque1.popleft()
print(deque1)
deque1.append('z')
print(deque1)
deque1.appendleft('a')
print(deque1)
print("Rotating the Deque")
deque1.rotate(1)
print(deque1)
deque1.rotate(4)
print(deque1)
