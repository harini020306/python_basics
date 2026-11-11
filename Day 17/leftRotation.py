numbers =list(map(int,input().split()))

first = numbers.pop(0)
numbers.append(first)

print("Left Rotated List:", numbers)