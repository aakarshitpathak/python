from functools import reduce

a= [1,2,35,434,657,780,334,34,54,55]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))