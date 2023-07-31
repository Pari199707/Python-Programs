def filterFunc(x):
    if x.isupper():
        return False
    return True

alphabets=['a','A','b','c','d','e']
lowers=list(filter(filterFunc,alphabets))
print(lowers)