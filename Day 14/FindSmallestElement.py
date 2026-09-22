numbers = list(map(int,input().split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)