# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# Each term is the sum of the two before it.

# Create a list of the first twenty Fibonacci Sequence numbers.

# Step 1: Define a function to generate the first n Fibonacci numbers.
def fibonacci(number):

    # Step 2: Initialize the list with the first two Fib numbers.
    numbers = [0, 1]

    # Step 3: Start a for loop to iterate until the specified n item.
    for i in range(0, number):

        # Step 4: Append the appropriate Fibonacci number to the end of the list.
        next_number = numbers[-1] + numbers[-2]
        numbers.append(next_number)

    # Step 5: Return the list from the function.
    return numbers

# Step 6: Print the list.
def main():
    list = fibonacci(10)
    print(list)

main()

