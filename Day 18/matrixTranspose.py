rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input())
        row.append(value)
    matrix.append(row)

transpose = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose of Matrix:")
for row in transpose:
    print(row)