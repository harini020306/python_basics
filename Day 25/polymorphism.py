class Circle:

    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle:

    def area(self, length, breadth):
        return length * breadth


# User input
radius = float(input("Enter circle radius: "))

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))

c = Circle()
r = Rectangle()

print("Circle Area:", c.area(radius))
print("Rectangle Area:", r.area(length, breadth))