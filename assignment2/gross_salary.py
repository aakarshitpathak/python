# program to calculate the gross salary

bs=int(input("Enter the basic salary"))

if bs<=4000:
    hra=(10/100)*bs
    da=(50/100)*bs
elif bs>=4001 and bs<8000:
    hra=(15/100)*bs
    da=(60/100)*bs
elif bs>=8001 and bs<=12000:
    hra=(20/100)*bs
    da=(70/100)*bs
elif bs>12000:
    hra=(25/100)*bs
    da=(80/100)*bs
else:
    print("wrong input")

gs = bs+hra+da

print("Gross salary is: ",gs)

