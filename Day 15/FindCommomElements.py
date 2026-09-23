list1 = map(int,input().split())
list2 = map(int,input().split())

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print(common)