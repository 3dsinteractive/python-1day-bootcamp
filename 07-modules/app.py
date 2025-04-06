# main.py

from animals.dog import Dog
from animals.cat import Cat

def main():
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Gray")

    print(dog.info())
    print(dog.speak())
    print(f"Breed: {dog.breed}")

    print(cat.info())
    print(cat.speak())
    print(f"Color: {cat.color}")

if __name__ == "__main__":
    main()
