n=int(input("Enter any number: "))

for i in range(2, n):
    if(n%i)==0:
        print("It is not prime")
        break

else:
    print("It is a prime")



