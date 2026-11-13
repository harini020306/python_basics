n = int(input("Enter number of items: "))

data = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

search = input("Enter key to search: ")

if search in data:
    print("Value:", data[search])
else:
    print("Key not found")
    