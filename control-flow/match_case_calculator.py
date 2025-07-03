number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
result = 0

match operation:
    case '+':
        result = number1 + number2
        print("The result is: ", result)
    case '-':
        result = number1 - number2
        print("The result is: ", result)
    case '*':
        result = number1 * number2
        print("The result is: ", result)
    case '/':
        if number2 == 0:
            print("Cannor divide by zero")
        else:
            result = number1 / number2
            print("The result is: ", result)
    case _:
            print("Invalid operation")