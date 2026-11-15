# Get user input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Check subset
if set1.issubset(set2):
    print("First set is a subset of second set")
else:
    print("First set is not a subset of second set")