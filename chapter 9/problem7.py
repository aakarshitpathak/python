with open ("log.txt") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if("python"in line):
        print(f"Yes the word python is present, Line no: {lineno}")
        break
    lineno+=1

else:
    print("The word is not present")