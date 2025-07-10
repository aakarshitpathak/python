def goodDay(name , ending):
    print("Good Day, " + name)
    print(ending)

goodDay("Aakarshit","Thankyou")
goodDay("sita","Thanks")

# now same program with return keyword
def goodDay(name , ending):
    print("Good Day, " + name)
    print(ending)
    return "done"
    

a= goodDay("Aakarshit","Thankyou")
print(a) 
# note if we don't use return keyword and call the function in any keyword
# then it will return none like this:
# Good Day, Aakarshit
# Thankyou
# None