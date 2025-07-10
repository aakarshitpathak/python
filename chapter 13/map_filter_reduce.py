from functools import reduce

# Map example
l = [1,2,3,4,5]

square = lambda x: x*x
sqlist = map(square, l)
print(list(sqlist))

# Filter example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven=filter(even,l)
print(list(onlyEven))

# Reduce Example
def sum(a,b):
    return a+b

print(reduce(sum,l)) # reduce just repeat the operation using given operators until the list ends