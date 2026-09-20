list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)