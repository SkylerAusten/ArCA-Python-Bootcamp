numbers = [22, 31, 56, 63, 7, 5, 2]

print(sum(numbers))
print(min(numbers))
print(max(numbers))

sum_total = 0
for number in numbers:
    sum_total += number

print("Sum:", sum_total)

current_max = 0
print(numbers)
for number in numbers:
    print("Number to check is", number)
    if(number > current_max):
        print(f"{number} is greater than {current_max}.")
        current_max = number
    else:
        print(f"{number} is less than or equal to {current_max}.")

print("Max Value:", current_max)

# numbers.sort(reverse=True)
# print(numbers)


# current_min = 0
# print(numbers)
# for number in numbers:
#     if(number < current_min):
#         current_min = number
# print("Min Value:", current_min)

numbers = [22, 31, 56, 63, 7, 5, 2]

sum_total = 0
number_of_items = 0
for number in numbers:
    sum_total = sum_total + number
    number_of_items += 1

print("Sum:", sum_total)
print("# of Items:", number_of_items)
average = sum_total / number_of_items
print("Avg:", average)








#for i in range(0, 7):
    #print(numbers[i])
