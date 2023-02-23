import random
def main():
    while True:
        # Generate a random number between 1 and 10
        number = random.randint(1, 10)

        # Prompt the user to guess the number
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == -1:
            return
        
        total_guesses = 1

        # Loop until the user guesses the correct number
        while (guess != number) and (total_guesses <= 3):
            # Check if the guess is too high or too low
            if guess > number:
                print("Too high!\n")
            else:
                print("Too low!\n")
                
            # Prompt the user to guess again
            guess = int(input("Guess a number between 1 and 10: "))
            total_guesses += 1

        if guess == number:
            print("Congratulations, you guessed the number!\n")
            print("Starting a new game...\n")
        
        else:
            print("Sorry!  You ran out of guesses.")
            print("Starting a new game...\n")

main()