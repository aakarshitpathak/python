import random 
def toss():
    user_call= input ("Toss time! Enter 'Heads' or 'Tails': ".strip().lower())
    toss_result = random.choice(["heads", "tails"])
    print(f"Toss result: {toss_result.capitalize()}")
    if user_call == toss_result:
        print("You won the toss!\n")
        return input("choose to 'bat' or 'bowl': ".strip().lower())
    else:
        print("You lost the toss. Computer will decide...\n")
        return random.choice(["bat" , "bowl"])
    
def innings(user_batting, target_runs=None):
    total_runs = 0
    balls_played = 0

    while balls_played < max_balls:

        if user_batting:
            # user batting
            try:
                user_choice= int(input("\nChoose a number between 1 and 6:"))
            except ValueError:
                print("Invalid choice. Please choose a number between 1 and 6. ")
                continue
            
            if user_choice < 1 or user_choice > 6:
                print("Invalid choice. Choose a number between 1 and 6.")
                continue
            computer_choice=random.randint(1,6)

        else:
            # computer batting
            try:
                user_choice = int(input("\nchoose a number between 1 and 6 (Your bowl):"))
            except ValueError:                            
                print("No ball! Computer gets a free run. ")
                computer_choice = random.randint(1,6)
                total_runs += computer_choice
                print(f"Computer chose: {computer_choice}. Total runs: {total_runs}")
                continue

            if user_choice < 1 or user_choice > 6:
                print("No ball! Computer gets a free run. ")
                computer_choice = random.randint(1,6)
                total_runs += computer_choice
                print(f"Computer chose: {computer_choice}. Total runs: {total_runs}")
                continue

            computer_choice= random.randint(1,6)

        print(f"Computer chose:{computer_choice}")

        if user_choice == computer_choice:

            if user_batting:
                print("You are Out! ")

            else:
                print("Computer is Out! ")
            break #ends innings when out

        else:

            if user_batting:
                total_runs += user_choice
                print(f"Runs scored: {total_runs}")
       
            else:
                total_runs += computer_choice
                print(f"Computer total runs: {total_runs}")

        balls_played += 1

        if target_runs and total_runs > target_runs:
            break

    return total_runs

def cricket_game():
    print("Welcome to the Cricket game!:\n ")
    overs= int(input("Enter the number of overs: "))
    global max_balls 
    max_balls = overs*6
    user_choice = toss()

    if user_choice == "bat":
        print("You chose to bat first. ")
        print("Your innings starts now!")
        user_score = innings(user_batting=True)
        print(f"Your innings ends with {user_score} runs. ")

        print("\nComputer's turn to chase!")
        computer_score = innings(user_batting=False, target_runs=user_score)

        if computer_score > user_score:
            print(f"Computer wins! It scored {computer_score} runs.")

        else:
            print(f"Congartulations You won by {user_score - computer_score} runs \nComputer managed to score {computer_score} runs.")

    elif user_choice == "bowl":
        print("\nYou chose to bowl first. ")
        print("Computer innings starts now!")
        computer_score = innings(user_batting=False)
        print(f"Computer innings ends with {computer_score} runs. ")

        print("\nYour turn to chase!")
        user_score = innings(user_batting=True, target_runs=computer_score)

        if user_score> computer_score:
            print(f"You win! You managed to score {user_score} runs, following by {computer_score} runs")

        else:
            print(f"OOPS!\n You Lose by {computer_score - user_score} runs.\n Computer managed to score {computer_score} runs.")
    else:
        print("Invalid choice. Game over.")

# Run the cricket game
cricket_game()

    
                         