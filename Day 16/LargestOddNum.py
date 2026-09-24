numbers = list(map(int,input().split()))

largest = None

for num in numbers:
    if num % 2 != 0:
        if largest is None or num > largest:
            largest = num

print(largest)