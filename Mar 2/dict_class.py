import random

list = []

for i in range(5):
    temp_dict = {}
    temp_dict["id"] = i
    temp_dict["val"] = random.randint(0, 10)
    list.append(temp_dict)

print(list)

print(list[])