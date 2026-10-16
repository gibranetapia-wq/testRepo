"""Multiply two user-input numbers (issue #6)."""


def parse_number(prompt: str) -> float:
    """Read one number from the user, exiting with a message on bad input."""
    raw = input(prompt)
    try:
        return float(raw)
    except ValueError:
        raise SystemExit(f"Error: {raw!r} is not a number")


def main() -> None:
    a = parse_number("Enter the first number: ")
    b = parse_number("Enter the second number: ")
    product = a * b
    # Print integers without a trailing .0
    if product == int(product):
        product = int(product)
    print(f"The product of {a:g} and {b:g} is {product}")


if __name__ == "__main__":
    main()
