# Function to check prime number
def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Get user input
num = int(input("Enter a number: "))

if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")