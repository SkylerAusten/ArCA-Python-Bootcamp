max = 5
counter = 1

print("Loop 1: Normal")
while (counter <= max):
    print("Counter:", counter)
    counter += 1


counter = 1
print("\nLoop 2: Break")

while (counter <= max):
    print("Counter:", counter)
    counter += 1

    if(counter == 3):
        print("Break!")
        break


counter = 0 # Starting at 0, not 1!
print("\nLoop 3: Continue")

while (counter <= max - 1):
    counter += 1

    if(counter == 3):
        print("Continue!")
        continue

    print("Counter:", counter)
