import random

def play_game(player_name):
    '''Function to handle individual player's turn with a unique target number. '''
    target_number = random.randint(1 , 100)
    attempts = 0
    print(f"\n{player_name}, your target number has been generated. Start guessing!")
    while True:
        try:
            guess = int(input(f"{player_name}, enter your guess: "))
            attempts += 1
            if guess < target_number:
                print("Too low! Try a higher number. ")
            elif guess > target_number:
                print("Too high! Try a lower number. ")
            else:
                print(f"Congratulations, {player_name}: You guessed the number in {attempts} attempts. ")
                return attempts
            
        except ValueError:
            print("Please enter a valid number. ")

def main():
    '''Main function to execute the multiplayer numver guessing game.'''
    print("Welcome to the Number Guessing Game!: ")

    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players >0:
                break
            else:
                print("Please enter atleast 1 player. ")
        except ValueError:
            print("Invalid input! Please enter a valid number. ") 

    players=[]

    for i in range(num_players):
        name = input(f"Enter name of player {i + 1}: ").strip().capitalize()
        players.append(name)

    results= {}

    for player in players:
        print(f"\n{player}'s turn:")
        results[player]= play_game(player)

    print("\n--- Game Over! ---")
    print("Number of attempts taken by each player:")
    for player , attempts in results.items():
        print(f"{player} : {attempts} attempts")      

    #Sorting players by attempts and ranking top 3
    ranked_players = sorted(results.items(), key= lambda x:x[1])

    print("\nLeaderboard:")
    if len(ranked_players)>=1:
        print(f"First place: {ranked_players[0][0]} ({ranked_players[0][1]} attempts)")
    if len(ranked_players)>=2:
        print(f"Second place: {ranked_players[1][0]} ({ranked_players[1][1]} attempts)")
    if len(ranked_players)>=3:
        print(f"Third place: {ranked_players[2][0]} ({ranked_players[2][1]} attempts)")

if __name__ == "__main__":
    main()