name = "Dalton"
print(id(name))
name = "Kaitlyn"
print(id(name))

my_favorite_colors = ["blue", "green", "red", "yellow"]
dalton_favorite_colors = my_favorite_colors

print(id(my_favorite_colors))
print(id(dalton_favorite_colors))

my_favorite_colors.append("Silver")
dalton_favorite_colors.append("Neon")

print(my_favorite_colors)
print(dalton_favorite_colors)

my_favorite_colors = ["blue", "green", "red", "yellow"]
dalton_favorite_colors = my_favorite_colors[:]

my_favorite_colors.append("Silver")
dalton_favorite_colors.append("Neon")

print(my_favorite_colors)
print(dalton_favorite_colors)

value = 3
#value = value + 2

value *= 2
print(value)