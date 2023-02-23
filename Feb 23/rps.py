import random

# Step 1: Define a function for the game.
def main():
    while True:

        # Step 2: Prompt the player for their choice.
        while True:
            player_choice = input("rock, paper, scissors, quit: ").lower()
            if (player_choice == "rock" or player_choice == "paper" or player_choice == "scissors" or player_choice == "quit"):
                break
        
        if player_choice == "quit":
            return False

        # Step 3: Generate the computer’s choice.
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        # Step 4: Print the choices.
        print(f"User chose {player_choice}, and computer chose {computer_choice}.")

        # Step 5: Determine the winner using 5 if/elif/else statements.
        if player_choice == "rock" and computer_choice == "paper":
            print("Computer won!\n")
        
        elif player_choice == "rock" and computer_choice == "scissors":
            print("Player won!\n")

        elif player_choice == "paper" and computer_choice == "scissors":
            print("Computer won!\n")

        elif player_choice == "paper" and computer_choice == "rock":
            print("Player won!\n")

        elif player_choice == "scissors" and computer_choice == "rock":
            print("Computer won!\n")

        elif player_choice == "scissors" and computer_choice == "paper":
            print("Player won!\n")

        else:
            print("Users tied!\n")

main()
# Bonus: Can we use a while loop to verify the user entered a legal value?
# Bonus: Can we use a while loop to allow the user to repeat the program?