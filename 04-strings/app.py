def main():
    name = "Alice"
    age = 30
    print(f"My name is {name} and I am {age} years old.")

    a = 5
    b = 10
    print(f"Sum of {a} and {b} is {a + b}.")

    pi = 3.1415926535
    print(f"Pi rounded to 2 decimal places: {pi:.2f}")

    price = 499.99
    print(f"Price: ${price:,.2f}")  # adds comma and formats to 2 decimals

    from datetime import datetime
    now = datetime.now()
    print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")

if __name__ == "__main__":
    main()

