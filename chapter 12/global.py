# def fun():
#     a = 3
#     print(a)
# a=56
# print(a)
# fun()
# note: agar yahi a mai function se pehele rakhta toh woh phir wahi Value
# print karta aur hum function me koi bhi value na dete toh jaisa neeche diya 
# hua hai

# a=56
# def fun():
#    print(a)
# print(a)
# fun()

a=56
def fun():
    global a
    a = 3
    print(a)

fun()
print(a)
# global keyword changes the global variable