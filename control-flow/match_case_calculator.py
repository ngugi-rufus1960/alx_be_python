# match_case_calculator.py

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match-case to perform the operation
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("Invalid operation selected.")
