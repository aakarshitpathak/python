# program to check a number is an armstrong number or not

n=int(input("Enter a number: "))
m=n
b=n
sum=0
count=0
while(b>0):
    b=int(b/10)
    count+=1
print(count)

while(m>0):
    r=m%10
    sum+=pow(r,count)
    m=int(m/10)

if(sum==n):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

print(n)
print(sum)