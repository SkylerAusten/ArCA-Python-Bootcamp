import random

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, or scissors (or q to quit): ").lower()

    if user_choice == "q":
        break

    if user_choice not in options:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(options)

    print(f"You chose {user_choice}. The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("Tie!")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        
    else:
        print("Computer wins!")