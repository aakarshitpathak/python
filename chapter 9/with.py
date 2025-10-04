f = open("file.txt" ,"r")
print(f.read())
f.close()

# The same can be written as
with open("file.txt")as f:
    print(f.read())

# now you don't have to write explictly to close the file