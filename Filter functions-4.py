def squares_computation(x):
    return x**2

nums=[1,2,3,4,5]
squares=list(map(squares_computation,nums))
print(squares)