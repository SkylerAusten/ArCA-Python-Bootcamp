# Import the random library.
import random

# Create a function for printing a list of characters as a string.
def list_to_string(list):
    word = ""
    for i in list:
        word += i

    print("Word:", word)
    return

# Create the driver function.
def main():

    # Randomly select a word for the game.
    word = list("cherry")

    # Create a list of underscores/blanks to be filled in.
    blanks = ["_"] * len(word)

    # Create variables for total guesses, wrong guesses, and guessed letters.
    total_guesses = 0
    wrong_guesses = 0
    guessed_letters = []

    # Use a while loop to keep playing until the word is found.
    while True:

        # Take in user input.
        input_char = input("Guess a letter: ")

        # Check if the input is more than one character.
        if len(input_char) > 1:
            print("Too many characters!")
            print()
            continue

        # Check if the character has already been used.
        if input_char in guessed_letters:
            print("You've already used that letter!")
            print()
            continue

        # Add the letter to the list of guessed letters.
        guessed_letters.append(input_char)
        total_guesses += 1

        # Initialize a loop counter index and a found boolean.
        index = 0
        found = False

        # Loop through the guessed word.
        for letter in word:

            # Check if the input character matches the word's letters.
            if input_char == letter:

                # If it does, update the blanks list.
                blanks[index] = input_char

                # Update the "character found" boolean.
                found = True

            # Increment the character index.
            index += 1

        # Display a message for if a character wasn't found.
        if found == False:

            # Increment the number of wrong guesses.
            wrong_guesses += 1
            print("That letter's not in this word!")
            list_to_string(blanks)
            print()

        # Display a message for if a character was found.
        else:
            print("You found a letter!")
            list_to_string(blanks)
            print()

        # Determine if the player has won to break the loop.
        if blanks == word:
            print("You win!\n")

            # Report the user's guess counts.
            print("Total Guesses:", total_guesses)
            print("Wrong Guesses:", wrong_guesses)
            break

# Execute the driver function.
main()


# Bonus: How can we pull the wordlist from a "dictionary" file?