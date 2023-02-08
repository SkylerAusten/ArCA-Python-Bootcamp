names = ["Dalton", "Kaitlyn", "Abby", "Tasha", "Tania"]
print(id(names))
print(names)
print(id(sorted(names, reverse=True)))

new_names = sorted(names)
names.sort()
names.remove("Kaitlyn")
names.pop()

print(names)



names.sort(reverse=True)
print(names)
print(id(names))


