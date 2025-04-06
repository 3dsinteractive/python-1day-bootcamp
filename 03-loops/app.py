def main():
    list_of_numbers = [1, 2, 3, 4, 5]
    for number in list_of_numbers:
        print(number)

    for i, number in enumerate(list_of_numbers):
        print(f"Index: {i}, Number: {number}")

if __name__ == "__main__":
    main()
