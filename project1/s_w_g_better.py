import random


computer=random.choice(["s","w","g"])
user=input("Enter your choice among: s,w,g =")
ydict={"s":"snake","w":"water","g":"gun"}

print(f"Your choice {ydict[user]}\nComputer choice {ydict[computer]}")

if computer == user:
    print("Its a draw")

else:
    if computer == "s" and user == "w":
        print("you lose!")

    elif computer == "s" and user == "g":
        print("you won!")

    elif computer == "w" and user == "s":
        print("you won!")

    elif computer == "w" and user == "g":
        print("you lose!")

    elif computer == "g" and user == "s":
        print("you lose! ")

    elif computer == "g" and user == "w":
        print("you won!")

    else:
        print("Something went wrong!")


