try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)

except ValueError:
    print("Error: Please enter a valid number")