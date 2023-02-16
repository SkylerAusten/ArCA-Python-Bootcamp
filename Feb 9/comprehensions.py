# numbers = [value**2 for value in range(1, 11)]


numbers = [value for value in range(2, 101, 2)]
print(numbers)

names = ["Dalton", "Kaitlyn", "Abby", "Tasha", "Tania"]
print(names[::2])

for name in names[::2]:
    print(name)

    