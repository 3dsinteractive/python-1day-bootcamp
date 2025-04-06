def main():
    print("🔢 Looping over a list:")
    list_of_numbers = [1, 2, 3, 4, 5]
    for number in list_of_numbers:
        print(number)

    print("\n🔁 Looping with enumerate:")
    for i, number in enumerate(list_of_numbers):
        print(f"Index: {i}, Number: {number}")

    print("\n👟 Looping over a tuple:")
    coordinates = (10.5, 20.3)
    for value in coordinates:
        print(value)

    print("\n📚 Looping over a dictionary:")
    person = {"name": "Alice", "age": 30, "city": "New York"}
    for key, value in person.items():
        print(f"{key}: {value}")

    print("\n📜 Looping over dictionary keys only:")
    for key in person:
        print(key)

    print("\n🎯 Looping over dictionary values only:")
    for value in person.values():
        print(value)

    print("\n🧬 Looping over a set:")
    unique_numbers = {7, 3, 5, 3, 1}
    for num in unique_numbers:
        print(num)  # order is not guaranteed

    print("\n🔤 Looping over a string:")
    text = "hello"
    for char in text:
        print(char)

    print("\n📂 Looping over lines in a file (assuming 'sample.txt'):")
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                print(line.strip())  # strip removes newline
    except FileNotFoundError:
        print("sample.txt not found. Create it to see this in action.")

    print("\n🎲 Looping over a range:")
    for i in range(1, 6):
        print(i)

    print("\n🧩 Looping over a list of tuples:")
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    for letter, number in pairs:
        print(f"Letter: {letter}, Number: {number}")


if __name__ == "__main__":
    main()
