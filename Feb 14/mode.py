counter_list = [0] *  11
print(counter_list)
# print("[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")

# This assumes all values will be between one and ten!

mode_list = [2, 9, 4, 3, 2, 7, 4, 8, 3, 1, 2]

# Task 1: Calculate the number of occurences.
for number in mode_list:
    counter_list[number] += 1

print(counter_list)

highest_count = max(counter_list)
mode_index = counter_list.index(highest_count)
print(mode_index)
mode = mode_list[mode_index]
print("Mode is ", mode)

# Task 2: Print the number of occurences for each number, e.g.
# 1 - 1 Occurrence(s)
# 2 - 3 Occurrence(s)
# 3 - 2 Occurrence(s)
# etc...

# Task 3: Determine the mode.
