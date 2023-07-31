import itertools

def testFunc(x):
    return x<7

names=['parin','manju','teju','pavi','ranju']
nums=[1,2,10,11,12,13,14,15,3,4,5,6,7,8,9]
print("Cycle Iterator")
cycle_names=itertools.cycle(names)
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print(next(cycle_names))
print("Count Iterator")
count_numbers=itertools.count(0,10)
print(next(count_numbers))
print(next(count_numbers))
print(next(count_numbers))
print(next(count_numbers))
print(next(count_numbers))
sum=itertools.accumulate(nums)
print(list(sum))
max=itertools.accumulate(nums,max)
print(list(max))
x=itertools.chain("ABCD","1234")
print(list(x))
print(list(itertools.takewhile(testFunc,nums)))
print(list(itertools.dropwhile(testFunc,nums)))



