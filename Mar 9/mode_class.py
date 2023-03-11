# Define our main function.
def main():
    # Open up mode data file.
    mode_file = open("mode_numbers.txt", "r")

    # Parse data file to store numbers in a list.
    file_text = mode_file.read()

    number_list = file_text.split(", ")

    # print(number_list)

    number_list = [int(i) for i in number_list]

    # print(number_list)

    # Set up a dictionary

    mode_dictionary = {}

    # Use each number in the list as a key, to increment its value in the dictionary
    for i in number_list:
        mode_dictionary[i] = 0

    for i in number_list:
        mode_dictionary[i] += 1

    # print(mode_dictionary)

    # Loop through all of the key value pairs to find the highest frequency.
    max = 0
    for i in mode_dictionary.values():
        if i > max:
            max = i

    mode = []
    for i in mode_dictionary.items():
        print(i)

    for key, value in mode_dictionary.items():
        if value == max:
            mode.append(key) 
    
    return mode


print(main())