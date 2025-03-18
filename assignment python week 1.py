# Basic Calculator Program

# Get user input
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform the chosen operation
if operation == '+':
    result = x + y
    print(f"{x} + {y} = {result}")
elif operation == '-':
    result = x - y
    print(f"{x} - {y} = {result}")
elif operation == '*':
    result = x * y
    print(f"{x} * {y} = {result}")
elif operation == '/':
    if x != 0:
        result = x / y
        print(f"{x} / {y} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered.")
