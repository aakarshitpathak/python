'''
For n = 3
  *
 ***
*****

For n = 5
    *
   ***
  *****
 ********
**********

'''

n = int(input("Enter the number: "))
for i in range(1, n+1): 
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="") #end="" this statement prevent print statement to move to next line
    print("")