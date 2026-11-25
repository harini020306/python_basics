# Find the sum of digits using recursion

def digit_sum(n):
    if n == 0:
        return 0

    return (n % 10) + digit_sum(n // 10)


num = int(input("Enter a positive number: "))

if num < 0:
    print("Please enter a positive number")
else:
    print("Sum of digits:", digit_sum(num))