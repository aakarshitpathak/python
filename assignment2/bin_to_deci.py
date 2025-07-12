# program to convert binary number in decimal number

n=int(input("Enter any number in form of 0 and 1: "))
sum=0
i=0
while (n>0):
    r=n%10
    deci=pow(2,i)*r
    sum=sum+deci
    n=int(n/10)
    i=i+1

print(sum)
