# Use map() to double each number

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = list(map(lambda x: x * 2, numbers))

print("Original numbers:", numbers)
print("Doubled numbers:", result)