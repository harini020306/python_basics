# Extract positive numbers using list comprehension

numbers = list(map(int, input("Enter numbers: ").split()))

positive = [num for num in numbers if num > 0]

print("Positive numbers:", positive)