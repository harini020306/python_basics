# Get user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

try:
    result = num1 / num2
    print("Division Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")