def calculate_mode(numbers):
    # Create an empty dictionary to store the frequency of each number.
    frequencies = {}
    
    # Loop through the list of numbers and update the frequency of each number in the dictionary.
    for number in numbers:
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1
    
    # Find the number(s) with the highest frequency.
    max_frequency = max(frequencies.values())
    mode = []

    # Loop through the dictionary and identify the modes.
    for key, value in frequencies.items():
        if value == max_frequency:
            mode.append(key)


    # If there is only one mode, return it.
    if len(mode) == 1:
        return mode[0]
    
    # If there are multiple modes, return a list of them.
    else:
        return mode

# Example Usage
numbers = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
mode = calculate_mode(numbers)
print("The mode is:", mode)