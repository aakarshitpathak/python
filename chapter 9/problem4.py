word = "Donkey"

with open("mfile.txt" , "r") as f:
    content = f.read()

contentNew = content.replace(word ,"######")

with open("mfile.txt", "w") as f:
    f.write(contentNew)
