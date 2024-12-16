from sys import argv, exit, stdin
from string import punctuation


def no_arg_management():
    """
    Reads a line from standard input and returns it.
    Returns:
    str: The line read from standard input.
    """
    print("What is the text to count?")
    for line in stdin:
        return line


def main():
    """
    Main function
    """
    try:
        assert len(argv) <= 2, "provide a single argument"
    except AssertionError as e:
        print(f"Assertion Error: {e}")
        exit(1)
    if len(argv) == 2:
        text = argv[1]
    else:
        text = no_arg_management()
    if text is None:
        text = ""
    print(f"The text contains {len(text)} characters")
    print(sum(1 for c in text if c.isupper()), "upper letters")
    print(sum(1 for c in text if c.islower()), "lower letters")
    print(sum(1 for c in text if c in punctuation), "punctuation marks")
    print(sum(1 for c in text if c.isspace()), "spaces")
    print(sum(1 for c in text if c.isdigit()), "digits")


if __name__ == '__main__':
    main()
