fruits = ["Apple", "Orange", "Banana"]
# A - Add “Grape” to the end of the list using append().
fruits.append("Grape")

# B - Add “Mango” to the start of the list using insert().
fruits.insert(0, "Mango")
print(fruits)

# C - Delete the first item in the list using del.
del fruits[0]

# D - Remove & store the last item in the list using pop().
deleted_fruit = fruits.pop(-1)
print(deleted_fruit)

# E - Remove “Orange” from the list using remove().
fruits.remove("Orange")
print(fruits)