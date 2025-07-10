with open("old.txt") as f:
    content = f.read()

with open("rename_old.txt" ,"w") as f:
    f.write(content)