# Define a function to generate the first n Fibonacci numbers
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Call the function to generate the first 10 Fibonacci numbers
fib_list = fibonacci(10)

# Print the list of Fibonacci numbers
print(fib_list)