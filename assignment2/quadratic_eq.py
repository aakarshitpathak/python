# program to find the quadratic equation

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

root1= (-b+(b*b-4*a*c)**1/2)/(2*a)
root2= (-b-(b*b-4*a*c)**1/2)/(2*a) 

print(" first root of quadratic equation is: ",root1)
print(" second root of quadratic equation is: ",root2)