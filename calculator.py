# Simple calculator using if-else statements

# Get user inputs
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation using if-else statements
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else: 
        result = "Error! Division by Zero!"
else:
    result = "Error, invalid operation!"

print(f"The result is: {result}")


