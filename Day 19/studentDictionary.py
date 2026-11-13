n = int(input("Enter number of students: "))

students = {}

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))
    students[name] = mark

print("\nStudent Details:")

for name, mark in students.items():
    print(name, ":", mark)