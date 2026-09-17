numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) != len(set(numbers)):
    print("Duplicates are present")
else:
    print("No duplicates found")