numbers = list(map(int, input().split()))

n = len(numbers) + 1

expected = n * (n + 1) // 2
actual = sum(numbers)

print(expected - actual)