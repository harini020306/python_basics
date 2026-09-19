numbers = list(map(int, input().split()))

result = []

for num in numbers:
    if num != 0:
        result.append(num)

zeros = len(numbers) - len(result)

result += [0] * zeros

print(*result)