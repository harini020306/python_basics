n = int(input("Enter matrix size: "))

matrix = []

print("Enter matrix elements:")

for i in range(n):
    row = []
    for j in range(n):
        value = int(input())
        row.append(value)
    matrix.append(row)

total = 0

for i in range(n):
    total += matrix[i][i]

print("Diagonal Sum:", total)