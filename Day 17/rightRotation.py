numbers = list(map(int,input().split()))

last = numbers.pop()
numbers.insert(0, last)

print("Right Rotated List:", numbers)