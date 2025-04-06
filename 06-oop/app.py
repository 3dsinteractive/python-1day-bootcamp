# Demonstrating OOP with attributes, methods, and inheritance

class Animal:
    def __init__(self, name, species):
        self.name = name  # attribute
        self.species = species  # attribute

    def speak(self):  # method
        return f"{self.name} makes a sound."

    def info(self):  # method
        return f"{self.name} is a {self.species}."


# Inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # call parent constructor
        self.breed = breed  # new attribute

    def speak(self):  # method override
        return f"{self.name} says Woof!"


# Another subclass
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):  # method override
        return f"{self.name} says Meow!"


def main():
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Gray")

    print(dog.info())      # Inherited method
    print(dog.speak())     # Overridden method
    print(f"Breed: {dog.breed}")  # Unique attribute

    print(cat.info())      # Inherited method
    print(cat.speak())     # Overridden method
    print(f"Color: {cat.color}")  # Unique attribute


if __name__ == "__main__":
    main()
