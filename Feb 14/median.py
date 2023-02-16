numbers = [2, 4, 5, 8, 8, 10, 71, 72]
number_of_items = len(numbers)

if (number_of_items % 2 == 0):
    upper_middle_index = number_of_items // 2
    lower_middle_index = upper_middle_index - 1
    upper_middle_value = numbers[upper_middle_index]
    lower_middle_value = numbers[lower_middle_index]
    median = (upper_middle_value + lower_middle_value) / 2
    print("The median is", median)

else:
    middle_index = number_of_items // 2
    print("The median is", numbers[middle_index])
