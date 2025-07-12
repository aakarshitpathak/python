# program to reverse a string

# def rev_string():
#     a=input("Enter any string: ")
#     rev=a[::-1]  # Note: [::-1] is a slicing operation
#     # i.e. (:) this refers that entire string is selected
#     # (-1) indicates that string will be read from left to right
#     print(rev)

# rev_string()

# or

# using reversed() and join()

# s="Aakarshit"
# rev=''.join(reversed(s)) #
# print(rev)

# using a Loop 

# a="Aakarshit"
# rev=""
# for ch in a:
#     rev=ch+rev # here (ch) will run in string a and add in rev variable
# and print it after adding which will be your reverse string

# print(rev)