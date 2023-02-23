# Import the random library.
import random

def list_to_string(list):
    output = ""
    for item in list:
        output += item
    
    return output


# Define driver function.
def main():

    # Randomly pick a word from a wordlist.
    wordlist = ["cherry", "lamp", "posters"]
    word = random.choice(wordlist)
    
    # Instantiate a blanks list.
    blanks = ["_"] * len(word)

    guessed_letters = []
    guess_count = 0

    # Loop user letter guesses.
    while True:

        guess_letter = input("Guess a letter: ")

        # Check the user only entered one letter.
        if len(guess_letter) > 1:
            print("You can only enter one letter!\n")
            continue

        # Check if letter has already been used.
        if guess_letter in guessed_letters:
            print("You've already used that letter!\n")
            continue

        guess_count = guess_count + 1
        guessed_letters.append(guess_letter)

        index = 0
        for character in word:
            if guess_letter == character:
                blanks[index] = guess_letter

            index += 1

        print("Word:", list_to_string(blanks))

        # Check if word has been found.
        if not ("_" in blanks):
            print("Word found!\n")
            return

main()