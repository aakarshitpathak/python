import random

def game():
    print("You are playing a game")
    score = random.randint(1,62)
    # fetch the high score
    with open("hiscoree.txt") as f:
        hiscoree = f.read()
        if(hiscoree!=""):
            hiscoree = int(hiscoree)
        else:
            hiscoree = 0

    print(f"Your score: {score}")
    if(score>hiscoree):
        # write this hiscore to the file
        with open("hiscoree.txt", "w") as f:
            f.write(str(score))

        return score
    
game()
        
    
