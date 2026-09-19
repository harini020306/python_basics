numbers = list(map(int, input().split()))

unique = list(set(numbers))
unique.sort()

if len(unique) < 2:
    print("No second largest number")
else:
    print(unique[-2])