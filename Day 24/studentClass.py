# Create a Student class
class Student:

    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mark:", self.mark)


# Get user input
name = input("Enter student name: ")
age = int(input("Enter student age: "))
mark = float(input("Enter student mark: "))

# Create object
s1 = Student(name, age, mark)

# Display details
s1.display()