class Animal:

    def sound(self):
        print("Animals make sounds")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


# Create objects
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()