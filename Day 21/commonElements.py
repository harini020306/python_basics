# Get first list from user
list1 = list(map(int, input("Enter first list elements: ").split()))

# Get second list from user
list2 = list(map(int, input("Enter second list elements: ").split()))

# Convert lists into sets
set1 = set(list1)
set2 = set(list2)

# Find common elements
common = set1.intersection(set2)

print("Common Elements:", common)