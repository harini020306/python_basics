# Function to calculate factorial
def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

# Get user input
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial:", factorial(num))