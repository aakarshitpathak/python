# try:
#     a = int(input("Hey, Enter a number. "))
#     print(a)
    
# except Exception as e:
#     print(e)

# finally:
#     print("I am inside finally")

# Note: finally is used in function to run something at any cost.

def main():

    try:
        a = int(input("Hey, Enter a number. "))
        print(a)
        return
        
    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside else")

main()