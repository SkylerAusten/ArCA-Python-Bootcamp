def user_input():
    text_file = open("plaintext.txt", "r")
    plaintext = text_file.read()
    text_file.close()

    key = int(input("Secret Key: "))

    return plaintext, key

    
    
def encryption(plaintext, key):
    plaintext = plaintext.upper()

    ciphertext = ""

    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    message_len = len(plaintext)
    for i in range(message_len):
        plaintext_character = plaintext[i]
        # print(plaintext_character)

        if (not plaintext_character.isalpha()):
            ciphertext += plaintext_character
            continue

        alphabet_index = alphabet.index(plaintext_character)
        # print(alphabet_index)
    
        encrpyted_character_index = (alphabet_index + key) % 26
        # print(encrpyted_character_index)

        encrypted_character = alphabet[encrpyted_character_index]
        # print(encrypted_character)
        ciphertext += encrypted_character

    return ciphertext

def message_output(ciphertext):
    text_file = open("ciphertext.txt", "w")
    text_file.write(ciphertext)
    text_file.close()


def main():
    plaintext_message, key = user_input()
    ciphertext_message = encryption(plaintext_message, key)
    message_output(ciphertext_message)

main()

