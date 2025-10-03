# f=open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("the word twinkle is present in file")

# else:
#     print("the word twinkle is not present in file")

# f.close()

with open("poem.txt") as f:
    content = f.read()
    if ("twinkle" in content):
        print("yes")
    else:
        print("no")