def divisible5(n):
    if (n%5 == 0):
        return True
    return False

a= [1,2,35434,657780,334345455]

f = list(filter(divisible5, a))
print(f)