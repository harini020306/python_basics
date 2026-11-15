# Get user input
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

# Convert lists into sets
set1 = set(list1)
set2 = set(list2)

# Find unique elements
unique = set1.symmetric_difference(set2)

print("Unique Elements:", unique)