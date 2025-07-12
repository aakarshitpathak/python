# program to find a number is a reverse number or not

n=int(input("Enter any number in form of 0 and 1: "))
sum=0
m=n
while (m>0):
    r=m%10
    sum=sum*10+r
    m=int(m/10)

if(n==sum):
    print("It is a reverse number")
else:
    print("It is not a reverse number")

print(n)
print(sum)