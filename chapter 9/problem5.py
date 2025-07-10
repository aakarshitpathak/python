words = ["Donkey" , "bekar" ,"ghatiya"]

with open("mfile.txt" , "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word ,"#" * len(word))


with open("mfile.txt", "w") as f:
    f.write(content)


