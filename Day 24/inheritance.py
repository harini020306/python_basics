# Parent class
class Person:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Name:", self.name)


# Child class
class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def display_course(self):
        print("Course:", self.course)


# Get user input
name = input("Enter student name: ")
course = input("Enter course: ")

# Create object
s1 = Student(name, course)

# Display details
s1.display_name()
s1.display_course()