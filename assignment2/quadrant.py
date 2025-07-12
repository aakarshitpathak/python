# program to find the quadrant of any point

x= int(input("Enter the X axis: "))
y= int(input("Enter the Y axis: "))

def quadrant(x,y):
    
    if x>0 and y>0:
        return "1st Quadrant"
    elif x<0 and y>0:
        return "2nd Quadrant"
    elif x<0 and y<0:
        return "3rd Quadrant"
    elif x>0 and y<0:
        return "4rth Quadrant"
    elif x==0 and y==0:
        return "Origin"
    elif x==0:
        return "Y axis"
    else:
        return "X axis"
    
print("The point lies in: ",quadrant(x,y))