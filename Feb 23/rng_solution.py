import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Prompt the user to guess the number
guess = int(input("Guess a number between 1 and 100: "))

# Loop until the user guesses the correct number
while guess != number:
    # Check if the guess is too high or too low
    if guess > number:
        print("Too high!")
    else:
        print("Too low!")
        
    # Prompt the user to guess again
    guess = int(input("Guess a number between 1 and 100: "))

# Print a message when the user guesses the correct number
print("Congratulations, you guessed the number!")