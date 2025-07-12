# program to print fibonacci series

n=int(input("Enter a number: "))
n1=0
n2=1
count=0
while(count!=n):
    n3=n1+n2
    print(f"{n3}", end=" ") # use end=" " to print something on same line
    n1=n2
    n2=n3
    count=count+1
