#This is a calculator


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers."""
    return a / b


def get_number(prompt: str) -> float:
    """Keep asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a valid number. Please try again.")


def main():
    while True:
        print()
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        operation = input("Choose an operation (1-5): ").strip()
        while operation not in ("1", "2", "3", "4", "5"):
            print("Invalid operation. Please choose 1, 2, 3, 4 or 5.")
            operation = input("Choose an operation (1-5): ").strip()

        if operation == "5":
            print("Goodbye!")
            break

        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        if operation == "1":
            print("Result:", add(a, b))
        elif operation == "2":
            print("Result:", subtract(a, b))
        elif operation == "3":
            print("Result:", multiply(a, b))
        elif operation == "4":
            if b == 0:
                print("Error: you cannot divide by zero.")
            else:
                print("Result:", divide(a, b))


# Quick checks that the functions work
assert add(2, 3) == 5
assert subtract(2, 3) == -1
assert multiply(2, 3) == 6
assert divide(2, 4) == 0.5

if __name__ == "__main__":
    main()
