n=int(input("Enter the number of days :"))

if(n>=365):
    a=n%365

    b=n/365
    e=int(b)
    c=a%7

    d=a/7
    f=int(d)
    
    print(f"{e} years, {f} weeks and {c} days")

else:
    g=n%7
    h=n/7
    i=int(h)
    print(f"0 years, {i} weeks and {g} days")

# or













       



