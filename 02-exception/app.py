def main():
    """This function demonstrates exception handling in Python."""
    try:
        # Attempt to open a non-existent file
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        # Handle the exception
        print(f"An error occurred: {e}")
    finally:
        print("This block always executes, regardless of exceptions.")

if __name__ == "__main__":
    main()
