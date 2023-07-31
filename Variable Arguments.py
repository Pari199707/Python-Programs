def add(*args):
    sum =0
    for i in args:
        sum+=i
    return sum

nums=[1,2,3,4,5]
print(add(*nums))
print(add(1,2,3,4,5,6))

def add(*marks):
    total_marks = 0
    for i in marks:
        total_marks += i
    return total_marks

marks=[1,2,3,4,5]
print(add(*marks))