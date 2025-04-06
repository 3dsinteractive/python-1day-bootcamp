from abc import ABC, abstractmethod

# Abstract base class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass  # Must be overridden by subclasses

    def describe(self):
        return f"This is {self.name}."


# Subclass 1
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


# Subclass 2
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Subclass 3
class Bird(Animal):
    def speak(self):
        return f"{self.name} says Tweet!"


def main():
    animals = [
        Dog("Buddy"),
        Cat("Whiskers"),
        Bird("Kiwi")
    ]

    for animal in animals:
        # Polymorphic behavior: same interface, different output
        print(animal.describe())
        print(animal.speak())


if __name__ == "__main__":
    main()
