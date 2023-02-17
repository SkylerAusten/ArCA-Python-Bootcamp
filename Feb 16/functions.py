def main():
    """What is this for?"""
    print("Main Function")
    a = 1
    b = 2

    # Scope Demonstration
    print("a =", a, "| b =", b)
    function_1()
    # function_2(a, b)


    # Paramaters & arguments don't have to match!
    num1 = 100
    num2 = 42
    # function_3(num1, num2)

main()


def function_1():
    print("Sub Function 1")
    a = 10
    b = 5
    print("a =", a, "| b =", b)


def function_2(a, b):
    print("Sub Function 2")
    print("a =", a, "| b =", b)


def function_3(a, b):
    print("Sub Function 3")
    print("a =", a, "| b =", b)
    print("Different variable names were fine!")



