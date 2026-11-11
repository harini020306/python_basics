numbers = list(map(int,input().split()))

k = 2

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Original List:", numbers)
print("Rotated List:", rotated)