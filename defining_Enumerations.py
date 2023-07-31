import collections
from enum import Enum, unique, auto


@unique
class Fruits(Enum):
    APPLE=1
    BANANA=2
    GRAPES=3
    MANGO=auto()

print(list(Fruits))
print(Fruits.APPLE)
print(type(Fruits.APPLE))
print(repr(Fruits.APPLE))

print(Fruits.APPLE.name,Fruits.APPLE.value)
print(Fruits(2).name,Fruits(2).value)

for fruit in (Fruits):
    print(fruit.value,"-",fruit)

myfruits={}
myfruits[Fruits.GRAPES]="Your Wish is my command"
print(myfruits)
print(myfruits[Fruits.GRAPES])

if Fruits.APPLE is Fruits.GRAPES:
    print("Both are same ")
else:
    print("Both are different ")

# Comparison using "!="
if Fruits.APPLE != Fruits.GRAPES:
    print("Both are different")
else:
    print("Both are same")
