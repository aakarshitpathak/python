with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Yes the word python is present in context")

else:
    print("The word python is not present in context")