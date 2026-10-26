def check_even_odd(number: int) -> str:
    """Determine whether a given integer is even or odd."""
    if number % 2 == 0:
        return "Even"
    return "Odd"


def main():
    print("--- Even and Odd Number Checker ---")
    try:
        user_input = input("Enter an integer: ")
        num = int(user_input)

        result = check_even_odd(num)
        print(f"The number {num} is {result}.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()