# Generate squares of numbers using list comprehension

numbers = list(map(int, input("Enter numbers: ").split()))

squares = [num ** 2 for num in numbers]

print("Original numbers:", numbers)
print("Squares:", squares)