# A B C D E F
# Shift: +1
# B C D E F G

# Prompt the user for a message.
# Prompt the user for a shift/key.
# then output the ciphertext.

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

plaintext = input("Plaintext Message: ")
# print("Message =", plaintext, "\n")

key = int(input("Secret Key: "))
# print("Message =", key, "\n")

# Uppercase each character in the message.
plaintext = plaintext.upper()

# Create a new ciphertext variable
ciphertext = ""

# Parse plaintext character by character.
message_len = len(plaintext)
for i in range(message_len):
    plaintext_character = plaintext[i]
    # print(plaintext_character)

    if (not plaintext_character.isalpha()):
        ciphertext += plaintext_character
        continue

        # Do something with #'s and symbols

    alphabet_index = alphabet.index(plaintext_character)
    # print(alphabet_index)
    
    encrpyted_character_index = (alphabet_index + key) % 26
    # print(encrpyted_character_index)

    encrypted_character = alphabet[encrpyted_character_index]
    # print(encrypted_character)
    ciphertext += encrypted_character


print("Ciphertext Message: ", ciphertext)



