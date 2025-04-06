def main():
    print("✅ Basic list comprehension:")
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print("Squares:", squares)

    print("\n🎯 List comprehension with condition (filtering):")
    evens = [x for x in numbers if x % 2 == 0]
    print("Even numbers:", evens)

    print("\n🔗 List comprehension with if-else (inline):")
    labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
    print("Labels:", labels)

    print("\n🧮 Nested loops in list comprehension:")
    pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
    print("Pairs:", pairs)

    print("\n🧼 With function calls:")
    def square(n): return n * n
    result = [square(x) for x in numbers]
    print("Squared (with function):", result)

    print("\n📦 Flattening a nested list:")
    matrix = [[1, 2], [3, 4], [5, 6]]
    flat = [num for row in matrix for num in row]
    print("Flattened list:", flat)

    print("\n🧪 Using range with list comprehension:")
    multiples_of_3 = [x for x in range(1, 21) if x % 3 == 0]
    print("Multiples of 3 (1-20):", multiples_of_3)

    print("\n🔁 Duplicating list values (e.g., for strings):")
    words = ["hi", "bye", "yo"]
    echoed = [word * 2 for word in words]
    print("Echoed words:", echoed)

    print("\n🔍 Working with strings:")
    sentence = "hello world"
    uppercase_letters = [char.upper() for char in sentence if char != " "]
    print("Uppercase (no spaces):", uppercase_letters)

    print("\n📐 Cartesian product using two lists:")
    colors = ["red", "blue"]
    sizes = ["S", "M", "L"]
    combos = [(color, size) for color in colors for size in sizes]
    print("Color-size combos:", combos)


if __name__ == "__main__":
    main()
