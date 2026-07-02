def fib(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b

# Driver Code
n = int(input("Enter a number: "))
print("Fibonacci number:", fib(n))