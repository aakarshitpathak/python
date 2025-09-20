try:
    a = int(input("Hey, Enter a number. "))
    print(a)
    
except Exception as e:
    print(e)

else:
    print("I am inside else")

# Note: if try is successful then it enters the else block otherwise ignores.