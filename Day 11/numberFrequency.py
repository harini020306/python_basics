numbers = list(map(int, input().split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

for num, count in frequency.items():
    print(num, "→", count)