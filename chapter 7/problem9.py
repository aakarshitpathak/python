'''

***
* *       for n = 3
***


'''
n = int(input("Enter the number: "))  # Take input from the user and convert it to an integer

for i in range(1, n+1):  # Loop from 1 to n (inclusive)
    if(i == 1 or i == n):  # If it's the first or last row
        print("*" * n, end="")  # Print a full row of '*' without a newline
    else:  # For all middle rows
        print("*", end="")  # Print the first '*'
        print(" " * (n-2), end="")  # Print (n-2) spaces for the hollow part
        print("*", end="")  # Print the last '*'
    print("")  # Move to the next line
