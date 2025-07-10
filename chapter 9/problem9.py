with open("this.txt") as f:
    content1 = f.read()

with open("this_copy.txt") as f:
    content2 = f.read()

if(content1==content2):
    print("Yes these file are identical")

else:
    print("N0 this file are not identical")

