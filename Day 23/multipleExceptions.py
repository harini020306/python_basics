try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Error: Enter numbers only")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

finally:
    print("Program execution completed")