"""Add two user-input numbers (issue #4)."""


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
    total = a + b
    # Print integers without a trailing .0
    if total == int(total):
        total = int(total)
    print(f"The sum of {a:g} and {b:g} is {total}")


if __name__ == "__main__":
    main()
